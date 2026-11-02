# P02-screen-v3 two-stage screening script: approved for freeze and release; not yet released.
# Decisions: dispatch, under Mahmood's delegation, 2026-11-02 (supporting/DECISION_v3_2026-11-02.md).
# --run still requires the public P02-screen-v3 release receipt.
"""P02 v3 Stage F queue builder and mechanical helpers; no candidate screening.

- Builds the Stage F queue OFFLINE from the archived, complete v1 frame (1,798 rows,
  v1 seed 2026102802 order). No new seed, no discovery retrieval.
- Enforces the pool (never-triaged v1 ranks 17-1,798), the exclusions and the order.
- stage_f_view() turns a JATS full-text XML into the only material a Stage F screener
  may read: headers (title, abstract, keywords, bibliographic metadata), the licence
  statement and the Methods section, with every table, figure and supplement removed.
- derive_stage_s_queue(), retraction_status(), effort_upper_bound() and select()
  implement the protocol's mechanical rules. Judgement-free by construction; they never
  read candidate data.
Standard library only. This script makes NO network request in any mode.
"""
import argparse
import datetime as dt
import hashlib
import html
import json
import math
import re
import sys
import unicodedata
import urllib.parse
import urllib.request  # imported only so tests can prove it is never called
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

PAPER = "P02"
VERSION = "P02-screen-v3"
V1_SEED = "2026102802"          # ordering seed of the archived v1 frame; v3 adds no seed
DRAFT_ONLY = False              # approved copy (decision 2026-11-02); --run needs the release receipt
ROOT = Path(__file__).resolve().parent
PREREG_NAME = "PREREG_P02_screen_v3_DRAFT.md"

V1_FRAME_SHA256 = "c2aad90cf12b746b9de40dd5a88113ab43eccddb23c406f33008e53a7eff1a04"
V1_FRAME_RECORD_COUNT = 1798
FIELD_PROTOCOL_SHA256 = "4f6e05206d46059cdbb9bcc6c8a34ac47ebad6e7bb7483e5a5398b6037ce9bac"

# ---- numbers fixed by the decision of 2026-11-02 (supporting/DECISION_v3_2026-11-02.md) --
POOL_FIRST_V1_RANK = 17         # D2: never-triaged ranks only
N_F = 40                        # D3: Stage F feasibility dispositions
N_S = 5                         # D4: Stage S full screens (= field protocol "up to 5")
F_CAP_MINUTES = 20              # D5: per Stage F disposition
CANDIDATE_CAP_MINUTES = 60      # D5: Stage F + Stage S combined, per candidate (v2 cap)
EFFORT_CAP_QUARTER_HOURS = 16   # four hours, unchanged from v2

# ---- prior dispositions (v1 and v2) -------------------------------------------------
PRE_V1_DOIS = frozenset({
    "10.1186/s13643-025-02800-8", "10.1016/j.envint.2020.105739",
    "10.1136/bmj.j5855", "10.1016/j.envint.2020.105746", "10.3390/nu14010174",
})
# Verified titles only (CANDIDATES_P02.md, 27 Oct 2026). Descatha and Suksatan titles are
# not available from a local verified source, so they are excluded by DOI only.
PRE_V1_TITLES = {
    "10.1186/s13643-025-02800-8": "Ultra-processed foods and risk of all-cause mortality: an updated systematic review and dose-response meta-analysis of prospective cohort studies",
    "10.1016/j.envint.2020.105739": "The effect of exposure to long working hours on ischaemic heart disease: A systematic review and meta-analysis from the WHO/ILO Joint Estimates of the Work-related Burden of Disease and Injury",
    "10.1136/bmj.j5855": "Low cigarette consumption and risk of coronary heart disease and stroke: meta-analysis of 141 cohort studies in 55 study reports",
}
V1_INVENTORY = [{'rank': 1, 'doi': '10.1136/bmjopen-2026-117508', 'disposition': 'EXCLUDED_TA'}, {'rank': 2, 'doi': '10.1016/j.eclinm.2023.102308', 'disposition': 'TO_FULL_TEXT'}, {'rank': 3, 'doi': '10.7717/peerj.20570', 'disposition': 'TO_FULL_TEXT'}, {'rank': 4, 'doi': '10.1136/bmjopen-2018-026232', 'disposition': 'EXCLUDED_TA'}, {'rank': 5, 'doi': '10.1038/s41598-019-38723-3', 'disposition': 'TO_FULL_TEXT'}, {'rank': 6, 'doi': '10.1093/ajcn/nqz178', 'disposition': 'TO_FULL_TEXT'}, {'rank': 7, 'doi': '10.1038/s41598-020-76306-9', 'disposition': 'TO_FULL_TEXT'}, {'rank': 8, 'doi': '10.1186/s12889-018-5041-5', 'disposition': 'TO_FULL_TEXT'}, {'rank': 9, 'doi': '10.1186/s12884-020-03036-1', 'disposition': 'TO_FULL_TEXT'}, {'rank': 10, 'doi': '10.3389/fphys.2022.955702', 'disposition': 'TO_FULL_TEXT'}, {'rank': 11, 'doi': '10.7762/cnr.2024.13.3.186', 'disposition': 'EXCLUDED_TA'}, {'rank': 12, 'doi': '10.1002/fsn3.72357', 'disposition': 'TO_FULL_TEXT'}, {'rank': 13, 'doi': '10.1016/j.eclinm.2026.103847', 'disposition': 'TO_FULL_TEXT'}, {'rank': 14, 'doi': '10.1186/s40795-025-01152-9', 'disposition': 'TO_FULL_TEXT'}, {'rank': 15, 'doi': '10.1007/s40279-023-01966-2', 'disposition': 'EXCLUDED_TA'}, {'rank': 16, 'doi': '10.1161/jaha.124.038714', 'disposition': 'TO_FULL_TEXT'}]
V1_FULLSCREEN = frozenset(['10.1016/j.eclinm.2023.102308', '10.7717/peerj.20570', '10.1038/s41598-019-38723-3', '10.1093/ajcn/nqz178', '10.1038/s41598-020-76306-9'])
V2_FULLSCREEN = frozenset(['10.1186/s12889-018-5041-5', '10.1186/s12884-020-03036-1', '10.3389/fphys.2022.955702', '10.1002/fsn3.72357', '10.1016/j.eclinm.2026.103847'])


def V1_TERMINAL_TA():
    return frozenset(x["doi"] for x in V1_INVENTORY if x["disposition"] == "EXCLUDED_TA")


def dispositioned_dois():
    """Every DOI with any v1/v2 disposition: pre-v1 screens, v1 full screens,
    v1 terminal title triage and v2 full screens (19 DOIs)."""
    return PRE_V1_DOIS | V1_FULLSCREEN | V1_TERMINAL_TA() | V2_FULLSCREEN


# ---- declared metadata filter stage (protocol section 3.3): counted and reported -------
DECLARED_FILTER_RULES = ("prior_disposition", "duplicate_title_of_dispositioned",
                         "metadata_reports_retracted", "non_original_pubtype", "non_original_title")
RETRACTION_PUBTYPES = frozenset({"retracted publication", "retraction of publication", "retraction notice"})
NON_ORIGINAL_PUBTYPES = frozenset({
    "published erratum", "correction", "protocol", "clinical trial protocol", "letter",
    "comment", "reply", "editorial", "news", "preprint",
})
NON_ORIGINAL_TITLE_PATTERNS = (
    ("correction_notice", re.compile(r"^\s*(?:(?:author|publisher)\s+)?(?:correction|corrigendum|erratum|errata|addendum)\s*(?::|to\b|for\b|$)", re.I)),
    ("retraction_notice", re.compile(r"^\s*(?:retraction\b|retracted\b|notice of retraction\b|withdrawn\s*:|expression of concern\b)", re.I)),
    ("protocol", re.compile(r"\bstudy protocol\b|\bprotocol for an? (?:systematic|scoping|umbrella|updated|living|network|meta-analysis)|\b(?:review|meta-analysis|research) protocol\b|:\s*an?\s+(?:[\w-]+\s+){0,4}protocol\.?\s*$", re.I)),
    ("plain_language_summary", re.compile(r"\bplain[- ]language summary\b", re.I)),
    ("letter_reply", re.compile(r"^\s*(?:re:|reply to\b|in reply\b|response to\b|comment on\b|commentary on\b|letter to\b)", re.I)),
)

F_FAIL_CODES = frozenset({
    "F-G0-RETRACTION", "F-G0-NONORIGINAL", "F-G0-DUPLICATE", "F-SRC-UNAVAILABLE",
    "F-SRC-NO-METHODS", "F-G1-NOT-MA", "F-G1-TARGET", "F-G1-FIELD", "F-G1-DESIGN",
    "F-G1-K", "F-G4-NONLINEAR", "F-G4-AUDIT", "F-G2-LICENCE", "F-G2-INPUT-TYPE",
    "F-TIMEOUT",
})

EPMC_FULLTEXT = "https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
EPMC_CORE = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%22{doi}%22"
             "&format=json&resultType=core&pageSize=25")
OPENALEX_WORK = "https://api.openalex.org/works/https://doi.org/{doi}"

DRY_OUTPUTS = ("stage_f_queue_P02_v3_DRYBUILD.jsonl", "stage_f_exclusions_P02_v3_DRYBUILD.jsonl",
               "dry_build_manifest_P02_v3.json")
RUN_OUTPUTS = ("stage_f_queue_P02_v3.jsonl", "stage_f_exclusions_P02_v3.jsonl",
               "run_manifest_P02_v3.json")


class FrameError(RuntimeError):
    pass


def canonical_json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(value):
    return hashlib.sha256(value).hexdigest()


def utc_now():
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def normalize_doi(value):
    if not isinstance(value, str):
        return None
    value = value.strip()
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value, flags=re.I)
    value = re.sub(r"^doi:\s*", "", value, flags=re.I)
    value = urllib.parse.unquote(value).strip().lower()
    return value if re.fullmatch(r"10\.\d{4,9}/[^\s]+", value) else None


def normalize_title(value):
    """Title identity key: unescape twice, drop tags, NFKD, casefold, keep [a-z0-9]."""
    if not isinstance(value, str):
        return ""
    value = html.unescape(html.unescape(value))
    value = re.sub(r"<[^>]*>", " ", value)
    value = unicodedata.normalize("NFKD", value)
    value = "".join(c for c in value if not unicodedata.combining(c)).casefold()
    return re.sub(r"[^a-z0-9]+", "", value)


def order_hash(doi, seed=V1_SEED):
    return sha256_bytes(f"{seed}|{PAPER}|screen|{doi}".encode("utf-8"))


def pubtype_tokens(value):
    return {t.strip().lower() for t in (value or "").split(";") if t.strip()}


def verify_field_protocol(path):
    digest = sha256_bytes(Path(path).read_bytes())
    if digest != FIELD_PROTOCOL_SHA256:
        raise FrameError("FIELD_USE_CASE_PROTOCOL.md copy is not byte-identical to the cited sha256")
    return digest


# ---- archived frame -----------------------------------------------------------------
def validate_v1_rows(rows):
    """Unchanged v2 (B2-S) contract: the complete original v1 frame, in seeded order."""
    if len(rows) != V1_FRAME_RECORD_COUNT:
        raise FrameError(f"Archived v1 frame is not the complete original frame ({V1_FRAME_RECORD_COUNT} rows)")
    seen, prior = set(), None
    for rank, row in enumerate(rows, 1):
        doi = row.get("doi")
        if normalize_doi(doi) != doi or doi in seen:
            raise FrameError("Invalid or duplicate v1 DOI")
        if rank <= len(V1_INVENTORY) and V1_INVENTORY[rank - 1]["doi"] != doi:
            raise FrameError("Triaged ranks 1-16 differ from the v1 inventory")
        seen.add(doi)
        digest = order_hash(doi)
        if row.get("frame_rank") != rank:
            raise FrameError("v1 archived rank mismatch")
        if row.get("order_sha256") != digest:
            raise FrameError("v1 archived ordering digest mismatch")
        key = (digest, doi)
        if prior is not None and key <= prior:
            raise FrameError("v1 frame is not in its original seeded order")
        prior = key
    return rows


def load_v1_frame(path, expected_hash=None):
    body = Path(path).read_bytes()
    if sha256_bytes(body) != (expected_hash or V1_FRAME_SHA256):
        raise FrameError("Archived v1 frame bytes do not match the expected sha256")
    rows = [json.loads(line) for line in body.decode("utf-8").splitlines() if line.strip()]
    if not all(isinstance(r, dict) for r in rows):
        raise FrameError("v1 frame rows must be JSON objects")
    return validate_v1_rows(rows)


def _first_meta(row):
    md = row.get("metadata") or [{}]
    if len(md) != 1:
        # The real archive has exactly one metadata record per row; refuse to guess.
        raise FrameError("Expected exactly one metadata record per v1 frame row")
    return md[0]


def build_stage_f_queue(rows, validate=True):
    """Return (queue, exclusions). Every frame row lands in exactly one of the two."""
    if validate:
        validate_v1_rows(rows)
    disp = dispositioned_dois()
    disp_titles = {normalize_title(t): d for d, t in PRE_V1_TITLES.items() if d in disp}
    for row in rows[:POOL_FIRST_V1_RANK - 1]:
        if row["doi"] in disp:
            disp_titles.setdefault(normalize_title(_first_meta(row).get("title")), row["doi"])
    disp_titles.pop("", None)
    queue, exclusions, seen_titles = [], [], {}
    for row in rows:
        rank, doi = row["frame_rank"], row["doi"]
        md = _first_meta(row)
        title = md.get("title")
        tokens = pubtype_tokens(md.get("type"))
        base = {"doi": doi, "v1_frame_rank": rank, "title": title, "pubtype": md.get("type")}
        if rank < POOL_FIRST_V1_RANK:
            reason = ("v1_triaged_rank_1_16_dispositioned" if doi in disp
                      else "v1_triaged_rank_1_16_not_screened_outside_v3_pool")
            exclusions.append(dict(base, reason=reason))
            continue
        if doi in disp:
            exclusions.append(dict(base, reason="prior_disposition"))
            continue
        key = normalize_title(title)
        if key and key in disp_titles:
            exclusions.append(dict(base, reason="duplicate_title_of_dispositioned",
                                   detail=disp_titles[key]))
            continue
        hit = sorted(tokens & RETRACTION_PUBTYPES)
        if hit:
            exclusions.append(dict(base, reason="metadata_reports_retracted", detail=hit))
            continue
        hit = sorted(tokens & NON_ORIGINAL_PUBTYPES)
        if hit:
            exclusions.append(dict(base, reason="non_original_pubtype", detail=hit))
            continue
        hit = [name for name, pat in NON_ORIGINAL_TITLE_PATTERNS if pat.search(title or "")]
        if hit:
            exclusions.append(dict(base, reason="non_original_title", detail=hit))
            continue
        pos = len(queue) + 1
        pmcid = md.get("pmcid")
        if not (isinstance(pmcid, str) and re.fullmatch(r"PMC\d+", pmcid)):
            pmcid = None
        queue.append({
            "queue_pos": pos, "v1_frame_rank": rank, "doi": doi,
            "order_sha256": row["order_sha256"], "ordering_seed": V1_SEED,
            "publication_date": row.get("publication_date"), "title": title,
            "journal": md.get("journal"), "pubtype": md.get("type"), "pmcid": pmcid,
            "fixed_stage_f_source": EPMC_FULLTEXT.format(pmcid=pmcid) if pmcid else None,
            "title_duplicate_of_queue_pos": seen_titles.get(key) if key else None,
            "within_stage_f_window": pos <= N_F,
            "stage_f_status": "NOT_VISITED",
        })
        if key:
            seen_titles.setdefault(key, pos)
    if len(queue) + len(exclusions) != len(rows):
        raise FrameError("Conservation failure: queue + exclusions != frame rows")
    return queue, exclusions


# ---- Stage F view (allowed sections only) ---------------------------------------------
DROP_TAGS = frozenset({"fig", "fig-group", "table-wrap", "table-wrap-group", "table",
                       "supplementary-material", "graphic", "inline-graphic", "media"})
METHODS_TITLE = re.compile(
    r"^(?:materials?\s+and\s+methods?|methods?(?:\s+and\s+(?:materials?|analysis|design))?|methodology"
    r"|(?:patients|subjects|participants)\s+and\s+methods?|(?:study|research)\s+design\s+and\s+methods?)$")
RESULTS_OR_LATER = re.compile(r"^(?:results?|findings|discussion|conclusions?|summary)\b")
INTRO_TITLE = re.compile(r"^(?:introduction|background|rationale|aims?|objectives?|purpose)\b")
CHALLENGE_MARKERS = ("captcha", "unusual traffic", "cf-chl-", "cf-turnstile", "verify you are human",
                     "checking your browser", "just a moment", "challenge-platform")
EXCLUDED_ABSTRACT_TYPES = ("graphical", "teaser", "toc", "video", "author-highlights")


def _local(tag):
    return tag.rsplit("}", 1)[-1] if isinstance(tag, str) else ""


def _text(el):
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip() if el is not None else ""


def _clean_title(sec):
    t = next((c for c in sec if _local(c.tag) == "title"), None)
    raw = _text(t)
    # Strip a leading section number ("2.", "2.1 ", "II.", "iv)") but never a leading letter
    # of a word: "Introduction" must stay "introduction".
    return raw, re.sub(r"^(?:(?:\d+(?:\.\d+)*|[IVXivx]+)[.)]\s*|\d+(?:\.\d+)*\s+)", "", raw).strip().lower()


def _sec_block(sec, path=""):
    raw, _ = _clean_title(sec)
    here = (path + " / " + raw).strip(" /") if raw else path
    out = {"section": here, "sec_id": sec.get("id"), "paragraphs": []}
    blocks = [out]
    for child in sec:
        tag = _local(child.tag)
        if tag in ("p", "list", "disp-quote", "def-list", "boxed-text", "disp-formula"):
            out["paragraphs"].append({"id": child.get("id"), "text": _text(child)})
        elif tag == "sec":
            blocks.extend(_sec_block(child, here))
    return blocks


def stage_f_view(xml_bytes):
    """Return the Stage F view of a JATS article: headers, licence, Methods only."""
    if not isinstance(xml_bytes, (bytes, bytearray)):
        raise FrameError("Stage F view needs the raw XML bytes")
    head = bytes(xml_bytes[:65536]).decode("utf-8", errors="replace").lower()
    if any(mark in head for mark in CHALLENGE_MARKERS):
        raise FrameError("Bot check / challenge page, not an article: F-SRC-UNAVAILABLE; no bypass")
    try:
        root = ET.fromstring(bytes(xml_bytes))
    except ET.ParseError as exc:
        raise FrameError("Not well-formed XML: F-SRC-UNAVAILABLE") from exc
    if _local(root.tag) != "article":
        raise FrameError("Root element is not a JATS <article>: F-SRC-UNAVAILABLE")
    removed = Counter()
    for parent in list(root.iter()):
        for child in list(parent):
            if _local(child.tag) in DROP_TAGS:
                removed[_local(child.tag)] += 1
                parent.remove(child)
    front = next((c for c in root if _local(c.tag) == "front"), None)
    meta = next((c for c in front.iter() if _local(c.tag) == "article-meta"), None) if front is not None else None
    header = {"article_type": root.get("article-type"), "journal_title": None, "publisher": None,
              "article_title": None, "article_ids": {}, "pub_dates": [], "subjects": [],
              "abstracts": [], "keywords": [], "licence": [], "copyright": []}
    if front is not None:
        for el in front.iter():
            tag = _local(el.tag)
            if tag == "journal-title" and header["journal_title"] is None:
                header["journal_title"] = _text(el)
            elif tag == "publisher-name" and header["publisher"] is None:
                header["publisher"] = _text(el)
    if meta is not None:
        for el in meta.iter():
            tag = _local(el.tag)
            if tag == "article-title" and header["article_title"] is None:
                header["article_title"] = _text(el)
            elif tag == "article-id":
                header["article_ids"][el.get("pub-id-type") or "unknown"] = _text(el)
            elif tag == "pub-date":
                header["pub_dates"].append({"type": el.get("pub-type") or el.get("date-type"),
                                            "text": _text(el)})
            elif tag == "subject":
                header["subjects"].append(_text(el))
            elif tag == "abstract":
                kind = (el.get("abstract-type") or "").lower()
                if not any(x in kind for x in EXCLUDED_ABSTRACT_TYPES):
                    header["abstracts"].append({"abstract_type": kind or None, "text": _text(el)})
            elif tag == "kwd":
                header["keywords"].append(_text(el))
            elif tag == "license":
                href = next((v for k, v in el.attrib.items() if k.endswith("href")), None)
                header["licence"].append({"href": href, "text": _text(el)})
            elif tag == "license_ref":
                header["licence"].append({"href": _text(el), "text": "ali:license_ref"})
            elif tag == "copyright-statement":
                header["copyright"].append(_text(el))
    body = next((c for c in root if _local(c.tag) == "body"), None)
    top = [c for c in body if _local(c.tag) == "sec"] if body is not None else []
    titles = [_clean_title(s) for s in top]
    chosen, rule = [], None
    typed = [s for s, (_, t) in zip(top, titles)
             if "method" in (s.get("sec-type") or "").lower() or METHODS_TITLE.match(t)]
    if typed:
        chosen, rule = typed, "titled_or_typed"
    else:
        later = next((i for i, (_, t) in enumerate(titles) if RESULTS_OR_LATER.match(t)), None)
        if later is not None:
            chosen = [s for s, (_, t) in zip(top[:later], titles[:later]) if not INTRO_TITLE.match(t)]
            rule = "positional_before_results" if chosen else None
    methods = []
    for s in chosen:
        methods.extend(b for b in _sec_block(s) if b["paragraphs"] or b["section"])
    return {
        "label": "STAGE F VIEW - headers, licence statement and Methods only (protocol section 4.2)",
        "source_sha256": sha256_bytes(bytes(xml_bytes)),
        "header": header,
        "methods_found": bool(chosen),
        "methods_rule": rule,
        "methods": methods,
        "dropped_top_level_section_titles": [raw for s, (raw, _) in zip(top, titles) if s not in chosen],
        "removed_elements": dict(removed),
    }


# ---- retraction rule (protocol section 5, G0-R) --------------------------------------
def retraction_status(doi, epmc_core_record, openalex_work):
    """CLEAR only if BOTH fixed sources resolve this DOI and neither flags it."""
    result = {"doi": doi, "status": "UNVERIFIED", "reasons": [], "errata_recorded": 0}
    if not isinstance(epmc_core_record, dict) or not isinstance(openalex_work, dict):
        result["reasons"].append("a fixed source did not return a record")
        return result
    if normalize_doi(epmc_core_record.get("doi")) != doi or normalize_doi(openalex_work.get("doi")) != doi:
        result["reasons"].append("DOI mismatch between query and returned record")
        return result
    flag = openalex_work.get("is_retracted")
    if not isinstance(flag, bool):
        result["reasons"].append("OpenAlex is_retracted missing or not boolean")
        return result
    type_list = (epmc_core_record.get("pubTypeList") or {}).get("pubType")
    if not isinstance(type_list, list) or not type_list:
        result["reasons"].append("Europe PMC core record lacks pubTypeList")
        return result
    pub_types = [str(x).lower() for x in type_list]
    comments = [str((c or {}).get("type", "")).lower()
                for c in ((epmc_core_record.get("commentCorrectionList") or {}).get("commentCorrection") or [])]
    result["errata_recorded"] = sum(c.startswith(("erratum in", "correction in")) for c in comments)
    if flag or any(p in RETRACTION_PUBTYPES for p in pub_types) or any(c.startswith("retraction in") for c in comments):
        result.update(status="RETRACTED", reasons=["retraction flag in a fixed source"])
    elif any("expression of concern" in c for c in comments):
        result.update(status="CONCERN", reasons=["expression of concern recorded"])
    else:
        result["status"] = "CLEAR"
    return result


# ---- Stage F ledger -> Stage S queue -------------------------------------------------
def derive_stage_s_queue(f_ledger, queue):
    expected = min(N_F, len(queue))
    if len(f_ledger) != expected:
        raise FrameError(f"Stage F needs exactly {expected} dispositions in queue order; got {len(f_ledger)}")
    s_queue = []
    for i, row in enumerate(f_ledger):
        q = queue[i]
        if row.get("queue_pos") != q["queue_pos"] or row.get("doi") != q["doi"]:
            raise FrameError(f"Stage F ledger row {i + 1} is out of order, skipped or not in the queue")
        disp = row.get("disposition")
        if disp not in ("F_PASS", "F_FAIL"):
            raise FrameError(f"Invalid Stage F disposition at row {i + 1}")
        if disp == "F_FAIL" and row.get("terminal_gate") not in F_FAIL_CODES:
            raise FrameError(f"Stage F failure at row {i + 1} lacks a registered gate code")
        if q.get("title_duplicate_of_queue_pos") and (disp, row.get("terminal_gate")) != ("F_FAIL", "F-G0-DUPLICATE"):
            raise FrameError(f"Row {i + 1} is a flagged title duplicate and must be F-G0-DUPLICATE")
        if q.get("fixed_stage_f_source") is None and disp == "F_PASS":
            raise FrameError(f"Row {i + 1} has no fixed Stage F source and cannot pass")
        if disp == "F_PASS":
            s_queue.append({"s_pos": len(s_queue) + 1, "queue_pos": q["queue_pos"], "doi": q["doi"],
                            "v1_frame_rank": q.get("v1_frame_rank"), "order_sha256": q.get("order_sha256"),
                            "within_stage_s_limit": len(s_queue) < N_S, "stage_s_status": "NOT_SCREENED"})
    return s_queue


# ---- G5 effort formula (protocol section 5, G5) ---------------------------------------
def effort_upper_bound(k, image_only_inputs, supplement_files, unit_conversions):
    if not isinstance(k, int) or isinstance(k, bool) or not 5 <= k <= 60:
        raise FrameError("k must be the printed integer k of the designated synthesis, 5-60")
    if not isinstance(supplement_files, int) or isinstance(supplement_files, bool) or supplement_files < 0:
        raise FrameError("supplement_files must be a non-negative integer")
    components = {
        "extraction_checking": 2 + math.ceil(k / 4) + (2 if image_only_inputs else 0)
                               + supplement_files + (2 if unit_conversions else 0),
        "reproduction": 3, "app_R_comparison": 2, "figure": 1, "short_write_up": 2,
    }
    total = sum(components.values())
    return {"components_quarter_hours": components, "total_quarter_hours": total,
            "upper_bound_hours": total / 4, "within_cap": total <= EFFORT_CAP_QUARTER_HOURS}


# ---- selection (protocol section 7) ----------------------------------------------------
def select(s_ledger):
    passes = []
    for row in s_ledger:
        if row.get("disposition") != "PASS":
            continue
        fit, prof, live, eff = (row.get("audit_fit"), row.get("profile"), row.get("live_question"),
                                row.get("effort_quarter_hours"))
        if fit not in (1, 2) or prof not in (1, 2, 3) or live not in (1, 2, 3) \
                or not isinstance(eff, int) or isinstance(eff, bool) or eff < 0 \
                or not re.fullmatch(r"[0-9a-f]{64}", str(row.get("order_sha256", ""))):
            raise FrameError("A passing Stage S record has an invalid score field")
        passes.append(row)
    ranked = sorted(passes, key=lambda r: (-r["audit_fit"], -r["profile"], -r["live_question"],
                                           r["effort_quarter_hours"], r["order_sha256"], r["doi"]))
    status = ("STOP_NO_PASS" if not ranked else
              "PRIMARY_ONLY_FALLBACK_ABSENT" if len(ranked) == 1 else "PRIMARY_AND_FALLBACK")
    return {"status": status, "primary": ranked[0]["doi"] if ranked else None,
            "fallback": ranked[1]["doi"] if len(ranked) > 1 else None,
            "ranking": [r["doi"] for r in ranked]}


# ---- release receipt -----------------------------------------------------------------
def _local_hash(which):
    path = Path(__file__).resolve() if which == "script" else ROOT / PREREG_NAME
    return sha256_bytes(path.read_bytes())


def _utc(value):
    try:
        stamp = dt.datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if stamp.utcoffset() != dt.timedelta(0) or stamp > dt.datetime.now(dt.timezone.utc):
            raise ValueError
        return stamp
    except (TypeError, ValueError) as exc:
        raise FrameError("A valid past UTC timestamp is required") from exc


def check_release(path):
    """Local assertions only; the coordinator verifies the public release and decision."""
    if DRAFT_ONLY:
        raise FrameError("Unapproved copy: no execution is authorized")
    receipt = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(receipt, dict):
        raise FrameError("Release receipt must be a JSON object")
    required = {
        "paper": PAPER, "version": VERSION, "ordering_seed": V1_SEED,
        "decision_by": "Mahmood", "decision": "APPROVE_V3_TWO_STAGE_SCREEN",
        "n_f": N_F, "n_s": N_S, "f_cap_minutes": F_CAP_MINUTES,
        "candidate_cap_minutes": CANDIDATE_CAP_MINUTES,
        "v1_frame_sha256": V1_FRAME_SHA256, "field_protocol_sha256": FIELD_PROTOCOL_SHA256,
        "github_release_url": "https://github.com/mahmood726-cyber/usecase-preregistrations/releases/tag/P02-screen-v3",
    }
    for key, value in required.items():
        if type(receipt.get(key)) is not type(value) or receipt.get(key) != value:
            raise FrameError("Release/decision receipt mismatch: " + key)
    if not isinstance(receipt.get("decision_evidence"), str) or not receipt["decision_evidence"].strip():
        raise FrameError("Recorded Mahmood decision evidence is required")
    if _utc(receipt.get("approved_at_utc")) > _utc(receipt.get("released_at_utc")):
        raise FrameError("Approval must precede release")
    doi = receipt.get("zenodo_doi")
    if not isinstance(doi, str) or not (doi == "PENDING" or re.fullmatch(r"10\.5281/zenodo\.\d+", doi)):
        raise FrameError("Record the screening DOI or PENDING")
    for field, which in (("script_sha256", "script"), ("prereg_sha256", "prereg")):
        if receipt.get(field) != _local_hash(which):
            raise FrameError("Local frozen hash mismatch: " + field)
    return receipt


# ---- queue outputs -------------------------------------------------------------------
def declared_filter_counts(exclusions, queue):
    """The declared metadata filter stage reports its own counts (decision D6)."""
    removed = {rule: sum(1 for e in exclusions if e["reason"] == rule) for rule in DECLARED_FILTER_RULES}
    total = sum(removed.values())
    return {"name": "declared metadata filter stage (protocol section 3.3)",
            "counted_and_reported": True, "input_pool_records": total + len(queue),
            "removed": removed, "removed_total": total, "remaining": len(queue)}


def _write_queue(frame_path, out_dir, expected_hash, names, status, receipt=None):
    out_dir = Path(out_dir).resolve()
    if out_dir == ROOT:
        raise FrameError("Write the queue to a separate output folder, never into the package folder")
    if any((out_dir / n).exists() for n in names):
        raise FrameError("Earlier outputs exist; nothing is overwritten")
    rows = load_v1_frame(frame_path, expected_hash)
    queue, exclusions = build_stage_f_queue(rows)
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, data in ((names[0], queue), (names[1], exclusions)):
        with (out_dir / name).open("x", encoding="utf-8", newline="\n") as stream:
            for row in data:
                stream.write(canonical_json(row) + "\n")
    manifest = {
        "paper": PAPER, "version": VERSION, "status": status, "built_at_utc": utc_now(),
        "network_requests": 0, "candidate_screening_performed": False,
        "ordering_seed": V1_SEED, "v1_frame_sha256": sha256_bytes(Path(frame_path).read_bytes()),
        "field_protocol_sha256": FIELD_PROTOCOL_SHA256, "script_sha256": _local_hash("script"),
        "frame_rows": len(rows), "queue_count": len(queue), "exclusion_count": len(exclusions),
        "declared_filter_stage": declared_filter_counts(exclusions, queue),
        "exclusions_by_reason": dict(sorted(Counter(e["reason"] for e in exclusions).items())),
        "stage_f_window_count": sum(q["within_stage_f_window"] for q in queue),
        "title_duplicate_flags": sum(1 for q in queue if q["title_duplicate_of_queue_pos"]),
        "title_duplicate_flags_in_window": sum(1 for q in queue if q["title_duplicate_of_queue_pos"]
                                               and q["within_stage_f_window"]),
        "missing_fixed_source": sum(1 for q in queue if q["fixed_stage_f_source"] is None),
        "window_v1_ranks": [q["v1_frame_rank"] for q in queue if q["within_stage_f_window"]],
        "n_f": N_F, "n_s": N_S,
    }
    if receipt is not None:
        manifest["release_receipt"] = receipt
    manifest["output_hashes"] = {n: sha256_bytes((out_dir / n).read_bytes()) for n in names[:2]}
    with (out_dir / names[2]).open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    return manifest


def dry_build(frame_path, out_dir, expected_hash=None):
    """Offline dry build for checking only. It is not a run and authorizes nothing."""
    return _write_queue(frame_path, out_dir, expected_hash, DRY_OUTPUTS, "DRY_BUILD_NOT_A_RUN")


def run(release_record, frame_path, out_dir):
    receipt = check_release(release_record)
    return _write_queue(frame_path, out_dir, receipt["v1_frame_sha256"], RUN_OUTPUTS,
                        "COMPLETE_STAGE_F_QUEUE", receipt)


def print_queries():
    print("Stage F fixed source: " + EPMC_FULLTEXT.format(pmcid="<PMCID>"))
    print("G0-R retraction, Europe PMC: " + EPMC_CORE.format(doi="<doi>"))
    print("G0-R retraction, OpenAlex: " + OPENALEX_WORK.format(doi="<doi>"))
    print("G3 Europe PMC identity: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%22<doi>%22&format=json&resultType=lite")
    print("G3 Europe PMC citations: https://www.ebi.ac.uk/europepmc/webservices/rest/<source>/<id>/citations?format=json&page=1&pageSize=1000")
    print("G3 OpenAlex cites: https://api.openalex.org/works?filter=cites:<W_ID>&per-page=100&page=1")
    print('G3 Europe PMC search 1: "<DOI>" AND (reanalysis OR "re-analysis" OR "dose unit" OR harmonisation OR harmonization OR plausibility)')
    print('G3 Europe PMC search 2: "<TITLE>" AND (reanalysis OR "re-analysis" OR "dose unit" OR harmonisation OR harmonization OR plausibility)')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--print-queries", action="store_true", help="Print fixed request templates; offline")
    mode.add_argument("--dry-build", action="store_true", help="Offline dry queue build (not a run) into --out-dir")
    mode.add_argument("--stage-f-view", type=Path, metavar="XML", help="Write the Stage F view of a JATS file")
    mode.add_argument("--run", action="store_true", help="Build the authorized queue (needs the release receipt)")
    parser.add_argument("--release-record", type=Path)
    parser.add_argument("--v1-frame", type=Path)
    parser.add_argument("--out-dir", type=Path)
    parser.add_argument("--out", type=Path, help="Output JSON for --stage-f-view")
    args = parser.parse_args(argv)
    try:
        if args.print_queries:
            print_queries()
            return 0
        if args.stage_f_view:
            if not args.out:
                parser.error("--stage-f-view needs --out")
            view = stage_f_view(args.stage_f_view.read_bytes())
            with args.out.open("x", encoding="utf-8", newline="\n") as stream:
                stream.write(json.dumps(view, ensure_ascii=False, indent=1) + "\n")
            print(f"Stage F view written; methods_found={view['methods_found']} rule={view['methods_rule']}")
            return 0
        if not args.v1_frame or not args.out_dir:
            parser.error("--v1-frame and --out-dir are required")
        if args.dry_build:
            manifest = dry_build(args.v1_frame, args.out_dir)
        else:
            if not args.release_record:
                parser.error("--run needs --release-record")
            manifest = run(args.release_record, args.v1_frame, args.out_dir)
    except (FrameError, OSError, ValueError, KeyError, TypeError) as exc:
        print("STOP: " + str(exc), file=sys.stderr)
        return 1
    flt = manifest["declared_filter_stage"]
    print(f"{manifest['status']}: declared filter stage: input {flt['input_pool_records']}, removed "
          f"{flt['removed']} (total {flt['removed_total']}), remaining {flt['remaining']}; Stage F window "
          f"{manifest['stage_f_window_count']}; nothing screened.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
