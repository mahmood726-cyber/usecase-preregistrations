# P04-screen-v3: approved for freeze and release; not yet released.
# Approval: dispatch, under Mahmood's delegation, 2026-11-02 (supporting/DECISION_v3_2026-11-02.md).
"""P04-screen-v3: offline Stage F queue builder, deterministic gate rules and log validators.

What this script does:
  * builds the Stage F queue OFFLINE from the archived v2 frame (v2_screen_order 6..540),
    cross-checked byte-for-byte against the archived v1 frame it was derived from;
  * removes every DOI with a v1/v2 disposition (31) and applies the fixed metadata rules
    (non-original title markers, preprint prefixes/sources, derivative/version-of-excluded)
    while preserving the archived seeded order;
  * provides the deterministic rules the protocol fixes (licence list, retraction verdict,
    outcome lock, design rule, k rule, drug-node scope, target choice, effort formula) and
    validators for the Stage F and Stage S logs (order, caps, sections read, terminal-gate rule).

What it never does: network access, new seeds, re-retrieval, or scoring/selection by itself.
--build and --stage-f-extract run only with the public P04-screen-v3 release arguments and matching
local sha256 values. --print-constants and --dry-build (into a folder OUTSIDE this package) are offline
utilities and never produce a screening queue.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import quote
import xml.etree.ElementTree as ET

PAPER = "P04"
VERSION = "v3"
DRAFT = False  # Approved for freeze (dispatch under Mahmood's delegation, 2026-11-02); not yet released.
RELEASE_TAG = "P04-screen-v3"
RELEASE_URL = "https://github.com/mahmood726-cyber/usecase-preregistrations/releases/tag/" + RELEASE_TAG
PREREG_FILENAME = "PREREG_P04_screen_v3.md"

# ---- Frozen inputs (archived; nothing is re-retrieved or re-seeded) --------------------------
V1_SEED = "2026102804"  # the v1/v2 seed; v3 introduces no seed
V1_FRAME_SHA256 = "fef70cafb5a84c329c62b8b8122d2c634e5a43301455c1c5065a7bbe4053063f"
V1_FRAME_ROWS = 561
V2_FRAME_SHA256 = "3563a7efe93c2f74d6a2718fef647ec5a0132cfc21e32870f0fe69fda7277d1d"
V2_FRAME_ROWS = 540

# ---- Stage numbers (fixed by the 2026-11-02 dispatch decision) ------------------------------------
N_F = 40          # Stage F stops at the first 40 feasibility dispositions (or queue exhaustion)
N_S = 5           # Stage S: at most 5 full screens (FIELD_USE_CASE_PROTOCOL "Screen up to 5 candidates")
CAP_F_MIN = 20    # minutes per Stage F disposition
CAP_S_MIN = 60    # minutes per Stage S full screen (unchanged from v2)
K_MIN, K_MAX = 5, 60
E_MAX_HOURS = 4.0

# ---- Exclusions: every DOI with any v1/v2 disposition -----------------------------------------
PRE_V1_EXCLUDED = frozenset({
    "10.1111/dom.15725", "10.1186/s12933-023-02035-8", "10.1007/s00125-024-06144-1",
    "10.1136/bmj-2023-076410", "10.1111/1753-0407.70192",
})
V1_TRIAGED = frozenset({
    "10.1007/s13300-023-01459-5", "10.1007/s40122-025-00789-5", "10.1007/s40123-025-01247-3",
    "10.1007/s40123-026-01377-2", "10.1038/s41598-021-89620-7", "10.1038/s41598-024-63316-0",
    "10.1097/md.0000000000031823", "10.1111/jdi.13603", "10.1186/s12912-025-04065-x",
    "10.1186/s12962-020-00208-w", "10.1186/s13098-026-02226-9", "10.1186/s13613-025-01471-x",
    "10.1186/s13643-022-01986-5", "10.3389/fendo.2023.1282584", "10.3389/fendo.2026.1891173",
    "10.3389/fmed.2025.1721311", "10.3389/fphar.2021.751496", "10.3389/fphar.2023.1226778",
    "10.3389/fpubh.2022.959073", "10.3389/fpubh.2023.1201818", "10.7759/cureus.100927",
})
PRIOR_V1_EXCLUDED = PRE_V1_EXCLUDED | V1_TRIAGED  # the 26 removed when v2 was derived from v1
V2_VISITED = (  # v2_screen_order 1..5, all FAIL (P04-screen-v2 run)
    "10.1007/s40123-026-01434-w", "10.3389/fendo.2022.895458", "10.3389/fendo.2025.1462104",
    "10.1097/md.0000000000028365", "10.1111/dom.70742",
)


def excluded_dois():
    return frozenset(PRIOR_V1_EXCLUDED) | frozenset(V2_VISITED)


# ---- Fixed metadata rules (section 3 of the protocol) ----------------------------------------
PREPRINT_DOI_PREFIXES = ("10.21203/", "10.1101/", "10.20944/", "10.2139/", "10.31219/",
                         "10.22541/", "10.48550/", "10.31234/", "10.31222/")
PREPRINT_RECORD_SOURCES = ("PPR:",)
DERIVATIVE_MIN_TITLE_CHARS = 40
_LEAD = r"^\s*"
_SEP = r"\s*(?:to|for|on|of)?\s*(?::|[\-–—]\s)"  # a colon, or a dash followed by whitespace
RAW_TITLE_MARKERS = (  # applied to the raw title (punctuation matters: "Correction:" vs "Correction of")
    ("erratum_correction", re.compile(_LEAD + r"(?:correction|corrigendum|corrigenda|erratum|errata)" + _SEP, re.I)),
    ("retraction_withdrawal", re.compile(_LEAD + r"(?:retraction(?: note| notice)?|retracted(?: article)?|withdrawn|withdrawal)" + _SEP, re.I)),
    ("expression_of_concern", re.compile(_LEAD + r"expression of concern" + _SEP, re.I)),
    ("comment_reply_letter", re.compile(_LEAD + r"(?:comment|commentary|reply|response|letter|editorial)" + _SEP, re.I)),
)
NORM_TITLE_MARKERS = (  # applied to the normalised title (lower case, punctuation -> space)
    ("plain_language_summary", re.compile(r"\b(?:summary of research|plain language summar(?:y|ies))\b")),
    ("erratum_correction", re.compile(r"^(?:correction|corrigendum|erratum) to\b")),
    ("retraction_withdrawal", re.compile(r"^(?:retraction of|retraction note|retraction notice)\b")),
    ("expression_of_concern", re.compile(r"\bexpression of concern\b")),
    ("comment_reply_letter", re.compile(r"\b(?:comment on|commentary on|reply to|in reply to|letter to the editor|authors reply)\b")),
    ("protocol", re.compile(r"\bprotocol for (?:a |an |the )?(?:systematic|network|meta|bayesian|living|updated|umbrella|review)")),
    ("protocol", re.compile(r"\b(?:a|an|study|review|research) protocol\b")),
    ("protocol", re.compile(r"\bprotocol$")),
)


def canonical_doi(value):
    if not isinstance(value, str):
        return None
    value = value.strip().lower()
    return value if re.fullmatch(r"10\.\d{4,9}/\S+", value) else None


def normalise_title(title):
    if not isinstance(title, str):
        return ""
    text = html.unescape(re.sub(r"<[^>]+>", " ", title))
    text = unicodedata.normalize("NFKC", text).casefold()
    return re.sub(r"[^0-9a-z]+", " ", text).strip()


def non_original_reasons(title):
    reasons = []
    raw_title = html.unescape(re.sub(r"<[^>]+>", " ", title or ""))
    for label, pattern in RAW_TITLE_MARKERS:
        if pattern.search(raw_title):
            reasons.append("non_original_title:" + label)
    norm = normalise_title(title)
    for label, pattern in NORM_TITLE_MARKERS:
        if pattern.search(norm):
            reasons.append("non_original_title:" + label)
    return sorted(set(reasons))


def preprint_reasons(doi, record_ids):
    reasons = []
    if any(doi.startswith(p) for p in PREPRINT_DOI_PREFIXES):
        reasons.append("preprint_doi_prefix")
    if any(isinstance(r, str) and r.startswith(PREPRINT_RECORD_SOURCES) for r in record_ids):
        reasons.append("preprint_record_source")
    return reasons


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def _rows(raw, label):
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(label + ": not UTF-8") from exc
    rows = [json.loads(line) for line in text.splitlines() if line.strip()]
    if not all(isinstance(r, dict) for r in rows):
        raise ValueError(label + ": non-object row")
    return rows


def _seed_hash(doi):
    return sha256(("%s|%s|screen|%s" % (V1_SEED, PAPER, doi)).encode("utf-8"))


def _titles(row):
    return [r.get("title") for r in row.get("records", []) if isinstance(r, dict) and isinstance(r.get("title"), str)]


def verify_v1(raw):
    if sha256(raw) != V1_FRAME_SHA256:
        raise ValueError("v1 frame bytes do not match the archived sha256")
    rows = _rows(raw, "v1 frame")
    if len(rows) != V1_FRAME_ROWS:
        raise ValueError("v1 frame row count differs from the archive")
    previous, seen = None, set()
    for rank, row in enumerate(rows, 1):
        doi = canonical_doi(row.get("doi"))
        if doi is None or doi != row.get("doi") or doi in seen:
            raise ValueError("v1 frame: missing, noncanonical or duplicate DOI")
        seen.add(doi)
        key = (_seed_hash(doi), doi)
        if row.get("screen_hash") != key[0] or row.get("screen_order") != rank or (previous and key <= previous):
            raise ValueError("v1 frame: hash, rank or physical order invalid")
        if row.get("screen_status") != "UNSCREENED":
            raise ValueError("v1 frame: annotated copy, not the archive")
        previous = key
    return rows


def verify_v2(raw, v1_rows):
    if sha256(raw) != V2_FRAME_SHA256:
        raise ValueError("v2 frame bytes do not match the archived sha256")
    rows = _rows(raw, "v2 frame")
    if len(rows) != V2_FRAME_ROWS:
        raise ValueError("v2 frame row count differs from the archive")
    expected = [r for r in v1_rows if r["doi"] not in PRIOR_V1_EXCLUDED]
    if len(expected) != len(rows):
        raise ValueError("v2 frame is not the v1 continuation (count)")
    for index, (row, source) in enumerate(zip(rows, expected), 1):
        if row.get("v2_screen_order") != index:
            raise ValueError("v2 frame: v2_screen_order not contiguous in physical order")
        if row.get("v1_frame_order") != source["screen_order"] or row.get("doi") != source["doi"]:
            raise ValueError("v2 frame is not the exact v1 continuation")
        stripped = {k: v for k, v in row.items() if k not in ("v1_frame_order", "v2_screen_order")}
        if stripped != source:
            raise ValueError("v2 frame row differs from its v1 source row")
        if row.get("screen_status") != "UNSCREENED":
            raise ValueError("v2 frame: annotated copy, not the archive")
    if tuple(r["doi"] for r in rows[:len(V2_VISITED)]) != tuple(V2_VISITED):
        raise ValueError("v2 frame: orders 1..5 are not the five v2-visited DOIs")
    return rows


def build_queue_from_bytes(v1_raw, v2_raw):
    """Default v3 pool = v2_screen_order 6..540, minus the fixed rules; archived order preserved."""
    v1_rows = verify_v1(v1_raw)
    v2_rows = verify_v2(v2_raw, v1_rows)
    excluded = excluded_dois()
    excluded_titles = {}
    for row in v1_rows:
        if row["doi"] in excluded:
            for title in _titles(row):
                norm = normalise_title(title)
                if len(norm) >= DERIVATIVE_MIN_TITLE_CHARS:
                    excluded_titles.setdefault(norm, row["doi"])
    tail = v2_rows[len(V2_VISITED):]
    title_groups = {}
    for row in tail:
        for norm in {normalise_title(t) for t in _titles(row)} - {""}:
            title_groups.setdefault(norm, set()).add(row["doi"])
    queue, exclusions = [], []
    for row in tail:
        doi = row["doi"]
        titles = _titles(row)
        record_ids = [r.get("record_id") for r in row.get("records", []) if isinstance(r, dict)]
        reasons = []
        if doi in excluded:
            reasons.append("prior_disposition_v1_or_v2")
        reasons += preprint_reasons(doi, record_ids)
        for title in titles:
            reasons += non_original_reasons(title)
            norm = normalise_title(title)
            for ex_title, ex_doi in excluded_titles.items():
                if ex_doi != doi and ex_title in norm:
                    reasons.append("derivative_or_version_of_excluded:" + ex_doi)
        # Exact-title duplicate GROUPS are removed whole: archived hash order cannot tell an original
        # from a same-title correction notice, and no keep-rule or screener choice is allowed.
        if any(len(title_groups.get(normalise_title(t), ())) > 1 for t in titles):
            reasons.append("exact_title_duplicate_group")
        if not titles:
            reasons.append("no_title_in_archived_metadata")
        reasons = sorted(set(reasons))
        if reasons:
            exclusions.append({"doi": doi, "v2_screen_order": row["v2_screen_order"],
                               "v1_frame_order": row["v1_frame_order"], "reasons": reasons})
            continue
        first = row["records"][0]
        queue.append({
            "doi": doi, "v3_queue_order": len(queue) + 1,
            "v2_screen_order": row["v2_screen_order"], "v1_frame_order": row["v1_frame_order"],
            "screen_hash": row["screen_hash"], "title": first.get("title"),
            "journal": first.get("journal"), "publication_date": row.get("publication_date"),
            "pmcid": first.get("pmcid"), "stage": "F", "screen_status": "UNSCREENED",
        })
    counts = {}
    for item in exclusions:
        keys = {reason if reason.startswith("non_original_title") else reason.split(":", 1)[0]
                for reason in item["reasons"]}
        for key in keys:
            counts[key] = counts.get(key, 0) + 1
    audit = {
        "paper": PAPER, "version": VERSION, "draft": DRAFT,
        "v1_frame_sha256": sha256(v1_raw), "v2_frame_sha256": sha256(v2_raw),
        "v2_rows": len(v2_rows), "v2_visited": list(V2_VISITED),
        "pool_before_rules": len(tail), "queue_count": len(queue),
        "excluded_by_rules": len(exclusions), "exclusion_reason_counts": dict(sorted(counts.items())),
        "declared_filter": {
            "stage": "declared offline metadata filter (protocol section 2.3); removed rows are not visits",
            "rows_in": len(tail), "distinct_rows_removed": len(exclusions), "rows_kept": len(queue),
            "rule_item_counts": dict(sorted(counts.items())),
            "note": "an item matching several rules is counted under each rule; distinct_rows_removed counts it once",
            "removed_rows_use_stage_f_slots": False,
        },
        "excluded_dois_total": len(excluded), "excluded_titles_available": len(excluded_titles),
        "queue_exclusions": exclusions, "network_access": False, "seed": V1_SEED, "new_seed": None,
        "stage_numbers": {"N_F": N_F, "N_S": N_S, "CAP_F_MIN": CAP_F_MIN, "CAP_S_MIN": CAP_S_MIN},
    }
    return queue, audit


def build_queue(v1_path, v2_path):
    return build_queue_from_bytes(Path(v1_path).read_bytes(), Path(v2_path).read_bytes())


# ---- Licence (exact list) --------------------------------------------------------------------
ACCEPTED_LICENCES = ("CC BY", "CC0")
_CC_URL = re.compile(r"creativecommons\.org/(?:licenses/(by|by-sa|by-nc|by-nd|by-nc-nd|by-nc-sa|by-sa-nc)/\d(?:\.\d)?"
                     r"|publicdomain/(zero)/1\.0)", re.I)
_URL_CODE = {"by": "CC BY", "by-sa": "CC BY-SA", "by-nc": "CC BY-NC", "zero": "CC0"}
_TEXT_ND = re.compile(r"no ?deriv|\bnd\b|-nd\b", re.I)
_TEXT_RULES = (
    ("CC BY-NC-SA", re.compile(r"attribution[- ]non-?commercial[- ]share-?alike|\bcc[- ]by[- ]nc[- ]sa\b", re.I)),
    ("CC BY-NC", re.compile(r"attribution[- ]non-?commercial\b|\bcc[- ]by[- ]nc\b", re.I)),
    ("CC BY-SA", re.compile(r"attribution[- ]share-?alike|\bcc[- ]by[- ]sa\b", re.I)),
    ("CC0", re.compile(r"\bcc0\b|cc zero|public domain dedication", re.I)),
    ("CC BY", re.compile(r"creative commons attribution\b|\bcc[- ]by\b", re.I)),
)


def licence_verdict(hrefs, texts):
    """URLs govern; text is read only if no licence URL is printed. Anything else FAILs."""
    codes = set()
    for href in hrefs or []:
        match = _CC_URL.search(href or "")
        if not match:
            return {"status": "FAIL", "reason": "licence URL not on the accepted list", "printed": href}
        code = _URL_CODE.get((match.group(1) or match.group(2) or "").lower())
        if code is None:
            return {"status": "FAIL", "reason": "licence not on the accepted list", "printed": href}
        codes.add(code)
    if not hrefs:
        joined = " ".join(t for t in texts or [] if isinstance(t, str))
        if _TEXT_ND.search(joined):
            return {"status": "FAIL", "reason": "NoDerivatives licence", "printed": joined}
        for code, pattern in _TEXT_RULES:
            if pattern.search(joined):
                codes.add(code)
                break
    if not codes:
        return {"status": "FAIL", "reason": "no printed accepted licence"}
    if len(codes) > 1:
        return {"status": "FAIL", "reason": "conflicting licences printed", "codes": sorted(codes)}
    code = codes.pop()
    if code not in ACCEPTED_LICENCES:
        return {"status": "FAIL", "reason": code + " is not on the accepted list"}
    return {"status": "PASS", "licence": code}


# ---- Retraction check (fixed sources and queries) ----------------------------------------------
EPMC_REST = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
OPENALEX_WORK = "https://api.openalex.org/works/https://doi.org/"
CROSSREF_UPDATES = "https://api.crossref.org/works?filter=updates%3A"
CROSSREF_FAIL_TYPES = frozenset({"retraction", "partial_retraction", "withdrawal", "removal"})
CROSSREF_UNRESOLVED_TYPES = frozenset({"expression_of_concern"})
RETRACTION_FAIL_TYPES = frozenset({"Retraction in", "Partial retraction in"})
RETRACTION_FAIL_PUBTYPES = frozenset({"Retracted Publication", "Retraction of Publication", "retracted-article"})
RETRACTION_UNRESOLVED_TYPES = frozenset({"Expression of concern in"})
RETRACTION_FLAG_TYPES = frozenset({"Erratum in", "Correction in", "Corrected and republished in",
                                   "Update in", "Republished in"})


def retraction_urls(doi):
    q = quote(doi, safe="")
    return {"europepmc": EPMC_REST + "?query=DOI%3A%22" + q + "%22&format=json&resultType=core&pageSize=1000&cursorMark=%2A",
            "openalex": OPENALEX_WORK + q,
            "crossref": CROSSREF_UPDATES + q + "&rows=1000"}


def _as_list(value):
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def retraction_verdict(doi, epmc_obj, openalex, crossref):
    """openalex/crossref = (http_status, json_or_None). Any unusable required answer -> UNRESOLVED (cannot pass)."""
    out = {"status": "PASS", "reasons": [], "flags_for_stage_s": [], "coverage_limitations": []}
    try:
        results = epmc_obj["resultList"]["result"]
    except (KeyError, TypeError):
        return dict(out, status="UNRESOLVED", reasons=["Europe PMC response unusable"])
    matches = [r for r in results if isinstance(r, dict) and canonical_doi(r.get("doi")) == canonical_doi(doi)]
    if not matches:
        return dict(out, status="UNRESOLVED", reasons=["Europe PMC returned no record with this DOI"])
    status = "PASS"
    for rec in matches:
        pub_types = set(_as_list((rec.get("pubTypeList") or {}).get("pubType")))
        cc_types = {c.get("type") for c in _as_list((rec.get("commentCorrectionList") or {}).get("commentCorrection"))
                    if isinstance(c, dict)}
        if pub_types & RETRACTION_FAIL_PUBTYPES or cc_types & RETRACTION_FAIL_TYPES \
                or re.match(r"^(withdrawn|retracted)\b", normalise_title(rec.get("title"))):
            status = "FAIL"
            out["reasons"].append("Europe PMC retraction/withdrawal marker")
        elif cc_types & RETRACTION_UNRESOLVED_TYPES and status != "FAIL":
            status = "UNRESOLVED"
            out["reasons"].append("Expression of concern")
        out["flags_for_stage_s"] += sorted(cc_types & RETRACTION_FLAG_TYPES)
    http_status, obj = openalex if isinstance(openalex, tuple) else (None, None)
    if http_status == 200 and isinstance(obj, dict) and obj.get("is_retracted") is True:
        status = "FAIL"
        out["reasons"].append("OpenAlex is_retracted=true")
    elif http_status == 404:
        out["coverage_limitations"].append("OpenAlex: DOI not indexed (disclosed, not a failure)")
    elif not (http_status == 200 and isinstance(obj, dict) and isinstance(obj.get("is_retracted"), bool)):
        if status != "FAIL":
            status = "UNRESOLVED"
        out["reasons"].append("OpenAlex response unusable")
    cr_status, cr_obj = crossref if isinstance(crossref, tuple) else (None, None)
    try:
        items = cr_obj["message"]["items"] if cr_status == 200 else None
    except (KeyError, TypeError):
        items = None
    if not isinstance(items, list):
        if status != "FAIL":
            status = "UNRESOLVED"
        out["reasons"].append("Crossref response unusable")
    else:
        for item in items:
            for update in _as_list(item.get("update-to") if isinstance(item, dict) else None):
                if not isinstance(update, dict) or canonical_doi(update.get("DOI")) != canonical_doi(doi):
                    continue
                kind = str(update.get("type", "")).lower()
                if kind in CROSSREF_FAIL_TYPES:
                    status = "FAIL"
                    out["reasons"].append("Crossref update: " + kind)
                elif kind in CROSSREF_UNRESOLVED_TYPES:
                    if status != "FAIL":
                        status = "UNRESOLVED"
                    out["reasons"].append("Crossref update: " + kind)
                elif kind:
                    out["flags_for_stage_s"].append("crossref:" + kind)
    out["status"] = status
    out["flags_for_stage_s"] = sorted(set(out["flags_for_stage_s"]))
    return out


# ---- Outcome lock (C1-C5) ----------------------------------------------------------------------
HIERARCHY = (
    ("all_cause_mortality", ("all cause mortality", "all cause death", "death from any cause",
                             "overall mortality", "total mortality"), ("mortality", "death")),
    ("cardiovascular_mortality", ("cardiovascular mortality", "cardiovascular death", "cv death",
                                  "cv mortality", "death from cardiovascular causes"), ()),
    ("mace", ("mace", "major adverse cardiovascular event", "major adverse cardiovascular events",
              "3 point mace", "3p mace", "4 point mace"), ()),
    ("hf_admission", ("hospitalization for heart failure", "hospitalisation for heart failure",
                      "heart failure hospitalization", "heart failure hospitalisation", "hhf",
                      "heart failure admission", "hospital admission for heart failure"), ()),
    ("kidney_composite", ("kidney composite", "renal composite", "composite kidney outcome",
                          "composite renal outcome", "composite kidney endpoint", "composite renal endpoint"), ()),
    ("hba1c", ("hba1c", "hb a1c", "a1c", "glycated haemoglobin", "glycated hemoglobin",
               "glycosylated haemoglobin", "glycosylated hemoglobin"), ()),
    ("body_weight", ("body weight", "weight change", "weight loss", "change in weight"), ()),
    ("severe_hypoglycaemia", ("severe hypoglycaemia", "severe hypoglycemia", "level 3 hypoglycaemia",
                              "level 3 hypoglycemia"), ()),
)
ATTAINMENT_MARKERS = ("target", "proportion", "achiev", "responder", "at least", "percentage of")
OUTCOME_KINDS = ("participant_level", "derived_index")


def hierarchy_tier(label):
    norm = normalise_title(label)
    if any(marker in norm for marker in ATTAINMENT_MARKERS):
        return None
    hits = []
    for index, (_, phrases, exact_only) in enumerate(HIERARCHY):
        if norm in exact_only or any(re.search(r"\b" + re.escape(p) + r"\b", norm) for p in phrases):
            hits.append(index)
    return hits[0] if len(hits) == 1 else None


def _by_hierarchy(items):
    def key(item):
        tier = hierarchy_tier(item["label"])
        return (tier if tier is not None else len(HIERARCHY), normalise_title(item["label"]), item["label"])
    return sorted(items, key=key)[0]["label"]


def lock_outcome(designated, analysed):
    for item in list(designated) + list(analysed):
        if item.get("kind") not in OUTCOME_KINDS:
            raise ValueError("outcome kind must be participant_level or derived_index")
    if designated:
        eligible = [d for d in designated if d["kind"] == "participant_level"]
        if not eligible:
            return None, "C2: designated primary is a derived ranking index; no component substitution"
        if len(designated) == 1:
            return eligible[0]["label"], "C1: single designated primary"
        return _by_hierarchy(eligible), "C3: several designated primaries; hierarchy among participant-level ones"
    eligible = [a for a in analysed if a["kind"] == "participant_level"]
    if not eligible:
        return None, "C4: no participant-level NMA outcome listed in Methods"
    return _by_hierarchy(eligible), "C4: no designated primary; hierarchy over Methods-listed NMA outcomes"


# ---- Independent trials and k ------------------------------------------------------------------
DESIGNS = frozenset({"rct", "quasi_randomised", "non_randomised_controlled", "cohort", "case_control",
                     "cross_sectional", "single_arm", "other"})
K_UNITS = frozenset({"trials", "rcts", "studies", "randomised controlled trials", "randomized controlled trials"})


def design_verdict(eligible_designs, nma_restricted_to_rct):
    unknown = set(eligible_designs) - DESIGNS
    if unknown:
        raise ValueError("unknown design category: " + ", ".join(sorted(unknown)))
    if nma_restricted_to_rct is True:
        return "PASS"
    if not eligible_designs:
        return "UNRESOLVED"
    return "PASS" if set(eligible_designs) == {"rct"} else "FAIL"


def k_verdict(printed, stage, review_totals=()):
    usable = [int(v) for v, unit in printed if str(unit).strip().lower() in K_UNITS]
    totals = [int(v) for v, unit in review_totals if str(unit).strip().lower() in K_UNITS]
    if any(t < K_MIN for t in totals):
        return {"status": "FAIL", "reason": "review-wide trial total below 5 bounds outcome k below 5"}
    if not usable:
        if stage == "F":
            return {"status": "DEFERRED", "reason": "outcome-specific k not printed in headers/Methods"}
        return {"status": "FAIL", "reason": "outcome-specific k not established by a printed number"}
    if any(not K_MIN <= v <= K_MAX for v in usable):
        return {"status": "FAIL", "reason": "a printed outcome-specific k is outside 5-60", "values": usable}
    return {"status": "PASS", "k": max(usable), "values": usable}


# ---- Drug-node scope ---------------------------------------------------------------------------
NODE_IN = frozenset({"drug", "drug_class", "drug_combination", "drug_plus_nonpharm"})  # INN or proposed INN
NODE_CONTROL = frozenset({"placebo", "no_treatment", "usual_care", "standard_care_background"})
NODE_OUT = frozenset({"exercise", "diet", "behavioural_education", "psychological", "surgery_procedure",
                      "device", "acupuncture", "herbal_traditional", "supplement_vitamin_mineral_probiotic",
                      "cell_gene_tissue_therapy", "investigational_code_only", "other_nonpharm"})


def network_scope_verdict(node_categories):
    unknown = set(node_categories.values()) - NODE_IN - NODE_CONTROL - NODE_OUT
    if unknown:
        raise ValueError("unknown node category: " + ", ".join(sorted(unknown)))
    active_drugs = [n for n, c in node_categories.items() if c in NODE_IN]
    return "PASS" if len(active_drugs) >= 2 else "FAIL"


def choose_target(nodes, direct_edges, pharm_nodes, motivated_pairs):
    adjacency = {n: set() for n in nodes}
    for edge in direct_edges:
        a, b = tuple(edge)
        adjacency.setdefault(a, set()).add(b)
        adjacency.setdefault(b, set()).add(a)
    component, label = {}, 0
    for start in sorted(adjacency):
        if start in component:
            continue
        stack = [start]
        while stack:
            node = stack.pop()
            if node in component:
                continue
            component[node] = label
            stack.extend(adjacency[node] - component.keys())
        label += 1

    def key(pair):
        return tuple(sorted(pair, key=lambda s: (s.casefold(), s)))

    qualifying = set()
    pharm = sorted(pharm_nodes)
    for i, a in enumerate(pharm):
        for b in pharm[i + 1:]:
            if frozenset((a, b)) in direct_edges or component.get(a) is None or component.get(a) != component.get(b):
                continue
            qualifying.add(key((a, b)))
    motivated = {key(p) for p in motivated_pairs} & qualifying
    pool = motivated or qualifying
    if not pool:
        return None
    return sorted(pool, key=lambda p: ([s.casefold() for s in p], p))[0]


# ---- Effort (deterministic; hundredths of an hour) ----------------------------------------------
E_BASE = 250            # reproduction 1.00 + whole-trial omission 0.50 + figure 0.50 + letter 0.50
E_PREP_TEXT = 2         # per trial, inputs printed as text/table
E_PREP_IMAGE = 4        # per trial, inputs only as printed numerals inside images
E_CHECK = 1             # per trial
E_SURCHARGE = 25        # each: multi-arm present, arm-to-contrast conversion, inputs split over >=2 files


def effort_hours(k, image_only=False, multi_arm=False, conversion=False, multi_file=False):
    total = E_BASE + k * ((E_PREP_IMAGE if image_only else E_PREP_TEXT) + E_CHECK)
    total += E_SURCHARGE * sum(bool(x) for x in (multi_arm, conversion, multi_file))
    total = -(-total // 25) * 25
    return total / 100


# ---- Stage logs ---------------------------------------------------------------------------------
F_STEPS = ("F1_identity_queue", "F2_article_type_non_original", "F3_retraction", "F4_licence",
           "F5_population", "F6_drug_nodes", "F7_design_rct_only", "F8_outcome_lock",
           "F9_k_precheck", "F10_follow_up_precheck")
F_DEFERRABLE = frozenset({"F9_k_precheck", "F10_follow_up_precheck"})
ALLOWED_F_SECTIONS = frozenset({"title", "abstract", "keywords", "bibliographic_metadata", "methods",
                                "licence_statement"})
S_GATES = ("S1_retraction_recheck", "S2_design_recheck", "S3_k", "S4_follow_up", "S5_licence_sources",
           "S6_complete_inputs", "S7_connected_target", "S8_M", "S9_P", "S10_L", "S11_G3_novelty",
           "S12_G5_effort")
STATUSES = frozenset({"PASS", "FAIL", "UNRESOLVED", "NOT ASSESSED", "DEFERRED"})


def _terminal_check(names, steps, deferrable, prefix):
    errors, terminal = [], None
    for name in names:
        status = (steps.get(name) or {}).get("status")
        if status not in STATUSES:
            errors.append(prefix + name + ": invalid or missing status")
            continue
        if terminal is None:
            if status == "DEFERRED" and name not in deferrable:
                errors.append(prefix + name + ": DEFERRED not allowed")
            elif status == "NOT ASSESSED":
                errors.append(prefix + name + ": NOT ASSESSED before the terminal step")
            elif status in ("FAIL", "UNRESOLVED"):
                terminal = (name, status)
        elif status != "NOT ASSESSED":
            errors.append(prefix + name + ": assessed after terminal step " + terminal[0])
    return errors, terminal


def validate_stage_f_log(queue, log, final=True):
    errors = []
    if len(log) > N_F:
        errors.append("more than N_F=%d Stage F dispositions" % N_F)
    if final and len(log) < min(N_F, len(queue)):
        errors.append("Stage F stopped before N_F dispositions without exhausting the queue")
    for i, rec in enumerate(log):
        prefix = "F record %d: " % (i + 1)
        if i >= len(queue) or rec.get("v3_queue_order") != queue[i]["v3_queue_order"] or rec.get("doi") != queue[i]["doi"]:
            errors.append(prefix + "does not follow the v3 queue order")
            continue
        bad_sections = set(rec.get("sections_read") or []) - ALLOWED_F_SECTIONS
        if bad_sections or not rec.get("sections_read"):
            errors.append(prefix + "sections outside headers/Methods/licence: " + ", ".join(sorted(bad_sections)))
        step_errors, terminal = _terminal_check(F_STEPS, rec.get("steps") or {}, F_DEFERRABLE, prefix)
        errors += step_errors
        expected = "F-PASS" if terminal is None else ("F-FAIL" if terminal[1] == "FAIL" else "F-UNRESOLVED")
        if rec.get("f_disposition") != expected:
            errors.append(prefix + "disposition must be " + expected)
        minutes = rec.get("minutes")
        if not isinstance(minutes, (int, float)) or isinstance(minutes, bool) or minutes < 0:
            errors.append(prefix + "minutes missing")
        elif minutes > CAP_F_MIN and not rec.get("cap_expired"):
            errors.append(prefix + "over the Stage F cap without cap_expired")
        if rec.get("cap_expired") and rec.get("f_disposition") == "F-PASS":
            errors.append(prefix + "cap expired: cannot be F-PASS")
    return errors


def stage_s_queue(queue, f_log):
    passed = [r for r in f_log if r.get("f_disposition") == "F-PASS"]
    order = {q["v3_queue_order"]: q for q in queue}
    return [order[r["v3_queue_order"]] for r in passed][:N_S]


def validate_stage_s_log(s_queue, log, final=True):
    errors = []
    if len(log) > N_S:
        errors.append("more than N_S=%d Stage S screens" % N_S)
    if final and len(log) != len(s_queue):
        errors.append("Stage S must screen every queued F-passer (at most N_S)")
    for i, rec in enumerate(log):
        prefix = "S record %d: " % (i + 1)
        if i >= len(s_queue) or rec.get("v3_queue_order") != s_queue[i]["v3_queue_order"] or rec.get("doi") != s_queue[i]["doi"]:
            errors.append(prefix + "does not follow the Stage S queue order")
            continue
        step_errors, terminal = _terminal_check(S_GATES, rec.get("gates") or {}, frozenset(), prefix)
        errors += step_errors
        expected = "PASS" if terminal is None else terminal[1]
        if rec.get("s_disposition") != expected:
            errors.append(prefix + "disposition must be " + expected)
        minutes = rec.get("minutes")
        if not isinstance(minutes, (int, float)) or minutes < 0 or (minutes > CAP_S_MIN and not rec.get("cap_expired")):
            errors.append(prefix + "minutes missing or over the Stage S cap")
        if rec.get("cap_expired") and rec.get("s_disposition") == "PASS":
            errors.append(prefix + "cap expired: cannot PASS")
        if rec.get("s_disposition") == "PASS":
            if not (isinstance(rec.get("k"), int) and K_MIN <= rec["k"] <= K_MAX):
                errors.append(prefix + "PASS needs 5 <= k <= 60")
            if rec.get("M") not in (1, 2) or rec.get("L") not in (1, 2) or rec.get("P") not in (1, 2, 3):
                errors.append(prefix + "PASS needs M>=1, L>=1, P>=1")
            e = rec.get("E")
            if not isinstance(e, (int, float)) or e > E_MAX_HOURS or abs(e * 4 - round(e * 4)) > 1e-9:
                errors.append(prefix + "PASS needs E <= 4.0 in 0.25-hour steps")
    return errors


def select_passers(s_log):
    passers = [r for r in s_log if r.get("s_disposition") == "PASS"]
    ranked = sorted(passers, key=lambda r: (-r["M"], -r["L"], -r["P"], r["E"], r["v3_queue_order"], r["doi"]))
    return (ranked[0] if ranked else None), (ranked[1] if len(ranked) > 1 else None)


# ---- Stage F section extraction (headers + Methods + licence ONLY) -----------------------------
METHODS_TITLE = re.compile(r"^\s*(?:[0-9IVX]+(?:\.[0-9]+)*\.?\s*)?(?:materials?\s+and\s+methods|methods?(?:\s+and\s+materials?)?"
                           r"|methodology|patients\s+and\s+methods|subjects\s+and\s+methods|research\s+design\s+and\s+methods)\s*$",
                           re.I)
DROP_TAGS = frozenset({"table-wrap", "table-wrap-group", "fig", "fig-group", "supplementary-material",
                       "graphic", "media", "inline-supplementary-material", "table"})
XLINK = "{http://www.w3.org/1999/xlink}href"


def _local(tag):
    return tag.rsplit("}", 1)[-1] if isinstance(tag, str) else ""


def _text(elem):
    parts = []

    def walk(node):
        if _local(node.tag) in DROP_TAGS:
            if node.tail:
                parts.append(node.tail)
            return
        if node.text:
            parts.append(node.text)
        for child in node:
            walk(child)
        if node.tail and node is not elem:
            parts.append(node.tail)
    walk(elem)
    return re.sub(r"\s+", " ", "".join(parts)).strip()


def extract_stage_f_sections(xml_bytes):
    """Return only title, abstract(s), keywords, licence and top-level Methods sections (tables/figures dropped)."""
    root = ET.fromstring(xml_bytes)
    meta = next((e for e in root.iter() if _local(e.tag) == "article-meta"), None)
    out = {"title": "", "abstract": [], "keywords": [], "licence_hrefs": [], "licence_texts": [],
           "methods": [], "methods_found": False}
    if meta is not None:
        title = next((e for e in meta.iter() if _local(e.tag) == "article-title"), None)
        out["title"] = _text(title) if title is not None else ""
        out["abstract"] = [_text(e) for e in meta.iter() if _local(e.tag) in ("abstract", "trans-abstract")]
        out["keywords"] = [_text(e) for e in meta.iter() if _local(e.tag) == "kwd"]
        for lic in (e for e in meta.iter() if _local(e.tag) in ("license", "license_ref")):
            href = lic.get(XLINK) or (lic.text.strip() if _local(lic.tag) == "license_ref" and lic.text else None)
            if href:
                out["licence_hrefs"].append(href)
            if _local(lic.tag) == "license":
                out["licence_texts"].append(_text(lic))
    body = next((e for e in root if _local(e.tag) == "body"), None)
    if body is not None:
        for sec in (c for c in body if _local(c.tag) == "sec"):
            sec_type = (sec.get("sec-type") or "").lower()
            title = next((c for c in sec if _local(c.tag) == "title"), None)
            title_text = _text(title) if title is not None else ""
            if "method" in sec_type or METHODS_TITLE.match(title_text):
                out["methods"].append(_text(sec))
                out["methods_found"] = True
    return out


# ---- Release checks and outputs ------------------------------------------------------------------
def check_release(args):
    """Local syntax/hash checks only; pc2 must verify the public release and its server time first."""
    if DRAFT:
        raise ValueError("DRAFT: not approved; no screening queue may be built")
    url = (getattr(args, "screen_release_url", None) or "").rstrip("/")
    if url != RELEASE_URL:
        raise ValueError("Supply the public screening release URL for " + RELEASE_TAG + " (v1/v2 releases cannot authorize v3)")
    doi = getattr(args, "screen_release_doi", None) or "PENDING"
    if not (doi == "PENDING" or re.fullmatch(r"https://doi\.org/10\.\d{4,9}/\S+", doi)):
        raise ValueError("Supply the screening release DOI as https://doi.org/... or PENDING")
    base = Path(__file__).resolve().parent
    hashes = {}
    for label, path, expected in (("prereg", base / PREREG_FILENAME, getattr(args, "prereg_sha256", None)),
                                  ("script", Path(__file__).resolve(), getattr(args, "script_sha256", None))):
        actual = sha256(path.read_bytes())
        if not expected or actual != str(expected).lower():
            raise ValueError(label + ": local bytes do not match the supplied frozen sha256")
        hashes[label] = actual
    return {"screen_release_url": url, "screen_release_doi": doi, "local_sha256": hashes,
            "public_release_verified_by_script": False}


def release_output_dir(directory):
    base = Path(__file__).resolve().parent
    chosen = Path(directory).resolve()
    if chosen == base or not chosen.is_relative_to(base):
        raise ValueError("Output directory must be a child of the script's directory")
    chosen.mkdir(parents=True, exist_ok=True)
    return chosen


# ---- CLI -----------------------------------------------------------------------------------------
def dry_output_paths(directory):
    base = Path(__file__).resolve().parent
    chosen = Path(directory).resolve()
    if chosen == base or chosen.is_relative_to(base):
        raise ValueError("Dry builds go to a scratch folder OUTSIDE the package")
    chosen.mkdir(parents=True, exist_ok=True)
    queue_path = chosen / "queue_P04_v3_DRYRUN.jsonl"
    audit_path = chosen / "queue_P04_v3_DRYRUN_audit.json"
    if queue_path.exists() or audit_path.exists():
        raise ValueError("Refusing to overwrite a previous dry build")
    return queue_path, audit_path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--print-constants", action="store_true")
    parser.add_argument("--dry-build", action="store_true", help="Offline check only; output outside the package")
    parser.add_argument("--build", action="store_true", help="Needs the public release arguments")
    parser.add_argument("--stage-f-extract", metavar="JATS_XML",
                        help="Write the Stage F sections (headers + Methods + licence) of one article; needs release args")
    parser.add_argument("--screen-release-url", help="Release-time field: public P04-screen-v3 release tag URL")
    parser.add_argument("--screen-release-doi", help="Release-time field: Zenodo DOI URL, or PENDING")
    parser.add_argument("--prereg-sha256", help="Release-time field: frozen prereg sha256")
    parser.add_argument("--script-sha256", help="Release-time field: frozen script sha256")
    parser.add_argument("--v1-frame")
    parser.add_argument("--v2-frame")
    parser.add_argument("--output-dir")
    args = parser.parse_args(argv)
    if args.print_constants:
        print(json.dumps({"draft": DRAFT, "N_F": N_F, "N_S": N_S, "CAP_F_MIN": CAP_F_MIN, "CAP_S_MIN": CAP_S_MIN,
                          "K": [K_MIN, K_MAX], "E_MAX_HOURS": E_MAX_HOURS, "excluded_dois": len(excluded_dois()),
                          "v1_frame_sha256": V1_FRAME_SHA256, "v2_frame_sha256": V2_FRAME_SHA256}, indent=1))
        return 0
    if args.build or args.stage_f_extract:
        try:
            release = check_release(args)
            if not args.output_dir:
                raise ValueError("Supply --output-dir (a child of the script's directory)")
            out_dir = release_output_dir(args.output_dir)
        except (ValueError, OSError) as exc:
            parser.error(str(exc))
        if args.stage_f_extract:
            target = out_dir / ("stage_f_" + Path(args.stage_f_extract).stem + ".json")
            try:
                extract = extract_stage_f_sections(Path(args.stage_f_extract).read_bytes())
                with target.open("x", encoding="utf-8", newline="\n") as handle:
                    json.dump({"release": release, "source_sha256": sha256(Path(args.stage_f_extract).read_bytes()),
                               "allowed_sections": extract}, handle, ensure_ascii=False, indent=1)
                    handle.write("\n")
            except (ValueError, OSError, ET.ParseError) as exc:
                parser.error(str(exc))
            print("Stage F sections written: " + str(target))
            return 0
        if not (args.v1_frame and args.v2_frame):
            parser.error("--build needs --v1-frame and --v2-frame")
        queue_path, audit_path = out_dir / "queue_P04_v3.jsonl", out_dir / "queue_P04_v3_audit.json"
        if queue_path.exists() or audit_path.exists():
            parser.error("Refusing to overwrite a previous queue/audit; preserve the run")
        try:
            queue, audit = build_queue(args.v1_frame, args.v2_frame)
        except (ValueError, OSError) as exc:
            parser.error(str(exc))
        payload = "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in queue)
        audit.update({"release": release, "queue_sha256": sha256(payload.encode("utf-8")),
                      "built_at_utc": datetime.now(timezone.utc).isoformat(),
                      "note": "Bibliographic metadata only; nothing screened."})
        with audit_path.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(audit, handle, ensure_ascii=False, indent=1)
            handle.write("\n")
        with queue_path.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(payload)
        print("Wrote %d UNSCREENED Stage F queue rows to %s" % (len(queue), queue_path))
        return 0
    if not args.dry_build:
        parser.error("Choose --print-constants or --dry-build")
    if not (args.v1_frame and args.v2_frame and args.output_dir):
        parser.error("--dry-build needs --v1-frame, --v2-frame and --output-dir")
    try:
        queue_path, audit_path = dry_output_paths(args.output_dir)
        queue, audit = build_queue(args.v1_frame, args.v2_frame)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    payload = "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in queue)
    audit.update({"label": "DRY RUN - NOT A SCREENING QUEUE (offline check; no release arguments)",
                  "queue_sha256": sha256(payload.encode("utf-8")),
                  "script_sha256": sha256(Path(__file__).resolve().read_bytes()),
                  "built_at_utc": datetime.now(timezone.utc).isoformat()})
    with queue_path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(payload)
    with audit_path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(audit, handle, ensure_ascii=False, indent=1)
        handle.write("\n")
    print("DRY RUN (not a screening queue): %d rows -> %s" % (len(queue), queue_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
