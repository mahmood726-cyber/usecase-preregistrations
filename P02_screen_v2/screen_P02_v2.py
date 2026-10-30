# P02-screen-v2 (FINAL for release). Mahmood 2026-10-30: "P02 and P04: Option A v2 approved. Proceed."
# Option A only; Option B NOT CHOSEN. Execution still requires the public P02-screen-v2 release receipt.
"""P02 v2 bibliographic frame builder (Option A); no candidate screening.
No candidate screening, equivalence adjudication or extraction is automated.
Standard library only. Network is opt-in, after a screening release receipt.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

PAPER = "P02"
SEED = "2026103002"
V1_SEED = "2026102802"
DRAFT_ONLY = False  # Approved copy (Mahmood decision 2026-10-30).
APPROVED_OPTION = "A"  # Option B was NOT CHOSEN; it is refused below.
START, END = "2016-10-28", "2026-10-28"
OUT_ROOT = Path(__file__).resolve().parent
EXCLUDED = frozenset({
    "10.1186/s13643-025-02800-8", "10.1016/j.envint.2020.105739",
    "10.1136/bmj.j5855", "10.1016/j.envint.2020.105746",
    "10.3390/nu14010174",
})
# Historical metadata only; no new screen or candidate score.
HISTORICAL_EXCLUDED = EXCLUDED
V1_INVENTORY = [{'rank': 1, 'doi': '10.1136/bmjopen-2026-117508', 'disposition': 'EXCLUDED_TA'}, {'rank': 2, 'doi': '10.1016/j.eclinm.2023.102308', 'disposition': 'TO_FULL_TEXT'}, {'rank': 3, 'doi': '10.7717/peerj.20570', 'disposition': 'TO_FULL_TEXT'}, {'rank': 4, 'doi': '10.1136/bmjopen-2018-026232', 'disposition': 'EXCLUDED_TA'}, {'rank': 5, 'doi': '10.1038/s41598-019-38723-3', 'disposition': 'TO_FULL_TEXT'}, {'rank': 6, 'doi': '10.1093/ajcn/nqz178', 'disposition': 'TO_FULL_TEXT'}, {'rank': 7, 'doi': '10.1038/s41598-020-76306-9', 'disposition': 'TO_FULL_TEXT'}, {'rank': 8, 'doi': '10.1186/s12889-018-5041-5', 'disposition': 'TO_FULL_TEXT'}, {'rank': 9, 'doi': '10.1186/s12884-020-03036-1', 'disposition': 'TO_FULL_TEXT'}, {'rank': 10, 'doi': '10.3389/fphys.2022.955702', 'disposition': 'TO_FULL_TEXT'}, {'rank': 11, 'doi': '10.7762/cnr.2024.13.3.186', 'disposition': 'EXCLUDED_TA'}, {'rank': 12, 'doi': '10.1002/fsn3.72357', 'disposition': 'TO_FULL_TEXT'}, {'rank': 13, 'doi': '10.1016/j.eclinm.2026.103847', 'disposition': 'TO_FULL_TEXT'}, {'rank': 14, 'doi': '10.1186/s40795-025-01152-9', 'disposition': 'TO_FULL_TEXT'}, {'rank': 15, 'doi': '10.1007/s40279-023-01966-2', 'disposition': 'EXCLUDED_TA'}, {'rank': 16, 'doi': '10.1161/jaha.124.038714', 'disposition': 'TO_FULL_TEXT'}]
V1_FULLSCREEN = frozenset(['10.1016/j.eclinm.2023.102308', '10.7717/peerj.20570', '10.1038/s41598-019-38723-3', '10.1093/ajcn/nqz178', '10.1038/s41598-020-76306-9'])
V1_DEFERRED = ['10.1186/s12889-018-5041-5', '10.1186/s12884-020-03036-1', '10.3389/fphys.2022.955702', '10.1002/fsn3.72357', '10.1016/j.eclinm.2026.103847', '10.1186/s40795-025-01152-9', '10.1161/jaha.124.038714']
V1_TERMINAL_TA = frozenset(x["doi"] for x in V1_INVENTORY if x["disposition"] == "EXCLUDED_TA")
# Pre-release correction B2-S (2026-10-30): the archive is the COMPLETE original v1 frame
# (SHA-256 c2aad90cf12b746b9de40dd5a88113ab43eccddb23c406f33008e53a7eff1a04). Ranks 1-16
# are the triaged inventory; ranks 17-1,798 were never triaged and are not in Option A's queue.
V1_FRAME_RECORD_COUNT = 1798
EXCLUDED = HISTORICAL_EXCLUDED | V1_FULLSCREEN | V1_TERMINAL_TA

EPMC_QUERY = (
    '(TITLE_ABS:"dose-response" OR TITLE_ABS:"dose response") AND '
    '(TITLE_ABS:"meta-analysis" OR TITLE_ABS:"meta analysis") AND '
    'FIRST_PDATE:[2016-10-28 TO 2026-10-28] AND OPEN_ACCESS:Y'
)
QUERIES = (("EPMC-1", "europe_pmc", EPMC_QUERY),)
RETRY_DELAYS = (1, 2, 4, 8)  # Five attempts total; 15 seconds of backoff.
OA_PAGE_SIZE = 100
OA_RECORD_LIMIT = 10000


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
    # Suffix punctuation can be part of the DOI: do not strip it.
    return value if re.fullmatch(r"10\.\d{4,9}/[^\s]+", value) else None


def order_hash(doi, seed=SEED):
    return sha256_bytes(f"{seed}|{PAPER}|screen|{doi}".encode("utf-8"))


def request_url(source, query, cursor="*"):
    if source == "europe_pmc":
        endpoint = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
        params = [("query", query), ("format", "json"), ("resultType", "lite"),
                  ("pageSize", "1000"), ("cursorMark", cursor)]
    else:
        raise ValueError("Discovery frame is Europe PMC ONLY")
    return endpoint + "?" + urllib.parse.urlencode(params)


class FrameError(RuntimeError):
    def __init__(self, message, attempts=None):
        super().__init__(message)
        self.attempts = attempts or []


def project_record(source, query_id, raw):
    """Keep bibliographic metadata only; never save abstracts/full text."""
    if not isinstance(raw, dict):
        raise FrameError("Invalid bibliographic record")
    if source == "europe_pmc":
        if not raw.get("id") or not raw.get("source"):
            raise FrameError("Europe PMC record lacks source/id")
        return {
            "source": source, "query_id": query_id,
            "record_id": str(raw["source"]) + "/" + str(raw["id"]),
            "doi_raw": raw.get("doi"), "title": raw.get("title"),
            "publication_date": raw.get("firstPublicationDate"),
            "publication_year": raw.get("pubYear"),
            "is_oa": raw.get("isOpenAccess") == "Y",
            "pmid": raw.get("pmid"), "pmcid": raw.get("pmcid"),
            "journal": raw.get("journalTitle"), "type": raw.get("pubType"),
            "cited_by_count": raw.get("citedByCount"), "is_retracted": True if any(str(raw.get(k, "")).lower() in {"y", "yes", "true"} for k in ("isRetracted", "is_retracted", "retracted")) else None,
        }
    raise FrameError("OpenAlex cannot supply discovery records")


def challenge_response(body):
    text = body[:65536].decode("utf-8", errors="replace").lower()
    return any(marker in text for marker in (
        "captcha", "unusual traffic", "cf-chl-", "cf-turnstile",
        "verify you are human", "checking your browser", "just a moment",
        "challenge-platform",
    ))


def fetch_json(url):
    # Retry server failures only; never retry a bot challenge or access refusal.
    req = urllib.request.Request(url, headers={
        "User-Agent": "P02-screen-v2-draft/1.0",
        "Accept": "application/json",
    })
    attempts = []
    for attempt in range(len(RETRY_DELAYS) + 1):
        entry = {"attempt": attempt + 1, "requested_at_utc": utc_now()}
        attempts.append(entry)
        try:
            try:
                with urllib.request.urlopen(req, timeout=60) as response:
                    if urllib.parse.urlsplit(response.geturl()).netloc != urllib.parse.urlsplit(url).netloc:
                        raise FrameError("Unexpected cross-host API redirect")
                    content_type = response.headers.get("Content-Type", "")
                    body, status = response.read(), response.status
            except urllib.error.HTTPError as exc:
                status = exc.code
                content_type = (exc.headers or {}).get("Content-Type", "")
                try:
                    body = exc.read(65536)
                finally:
                    exc.close()
            entry.update(received_at_utc=utc_now(), http_status=status,
                         response_sha256=sha256_bytes(body))
            if status != 200:
                if challenge_response(body):
                    raise FrameError(f"HTTP {status}; bot check blocked; no retry or bypass")
                if 500 <= status <= 599 and attempt < len(RETRY_DELAYS):
                    entry["retry_after_seconds"] = RETRY_DELAYS[attempt]
                    time.sleep(RETRY_DELAYS[attempt])
                    continue
                raise FrameError(f"HTTP {status}; failed/blocked, not zero results; retry budget exhausted or not applicable")
            if "json" not in content_type.lower():
                raise FrameError(f"HTTP {status}, non-JSON/blocked response; no bypass")
            try:
                data = json.loads(body)
            except (UnicodeError, ValueError) as exc:
                raise FrameError("Invalid JSON; failed/blocked, not zero results") from exc
            if not isinstance(data, dict):
                raise FrameError("Unexpected API response schema")
            return data, {"requested_at_utc": attempts[0]["requested_at_utc"],
                          "received_at_utc": entry["received_at_utc"],
                          "http_status": status, "response_sha256": sha256_bytes(body),
                          "attempts": attempts}
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            entry.update(received_at_utc=utc_now(), error=type(exc).__name__)
            raise FrameError(f"API transport failed: {type(exc).__name__}; not zero results", attempts) from exc
        except FrameError as exc:
            entry.setdefault("received_at_utc", utc_now())
            entry["error"] = str(exc)
            exc.attempts = attempts
            raise


def harvest(query_id, source, query, fetch, emit, pace=True):
    if source != "europe_pmc":
        raise FrameError("Discovery frame is Europe PMC ONLY")
    cursor, expected, retrieved = "*", None, 0
    cursors, record_ids, projected = set(), set(), []
    while True:
        if cursor in cursors:
            raise FrameError(f"{query_id}: repeated cursor")
        cursors.add(cursor)
        url = request_url(source, query, cursor)
        try:
            data, receipt = fetch(url)
            total = data.get("hitCount")
            result_list = data.get("resultList")
            if not isinstance(result_list, dict):
                raise FrameError(f"{query_id}: invalid resultList")
            rows = result_list.get("result")
            next_cursor = data.get("nextCursorMark")
            if not isinstance(total, int) or isinstance(total, bool) or total < 0 or not isinstance(rows, list):
                raise FrameError(f"{query_id}: missing/invalid count or results list")
            if expected is None:
                expected = total
            if total != expected:
                raise FrameError(f"{query_id}: hit count changed during pagination")
            page = [project_record(source, query_id, row) for row in rows]
            for record in page:
                key = record["record_id"]
                if key in record_ids:
                    raise FrameError(f"{query_id}: repeated record across pages")
                record_ids.add(key)
            retrieved += len(page)
            if retrieved > expected:
                raise FrameError(f"{query_id}: retrieved more than reported")
            emit({"event": "page", "query_id": query_id, "source": source,
                  "url": url, "receipt": receipt, "reported_count": total,
                  "retrieved_so_far": retrieved, "next_cursor": next_cursor,
                  "records": page})
            projected.extend(page)
            if retrieved == expected:
                return projected, {"query_id": query_id, "reported_count": expected,
                                   "retrieved_count": retrieved, "pages": len(cursors),
                                   "complete": True}
            if not rows or not next_cursor or next_cursor in cursors:
                raise FrameError(f"{query_id}: incomplete pagination ({retrieved}/{expected})")
            cursor = str(next_cursor)
            if pace:
                time.sleep(1)
        except Exception as exc:
            emit({"event": "query_failure", "query_id": query_id, "url": url,
                  "at_utc": utc_now(), "error": str(exc), "complete": False,
                  "reported_count": expected, "retrieved_count": retrieved,
                  "status": "FAILED_BLOCKED", "attempts": getattr(exc, "attempts", [])})
            raise


def exact_date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return None
    try:
        return dt.date.fromisoformat(value).isoformat()
    except ValueError:
        return None


def make_frame(records, excluded=EXCLUDED):
    groups, exclusions = {}, []
    for record in records:
        doi = normalize_doi(record.get("doi_raw"))
        if doi is None:
            exclusions.append({"reason": "missing_or_invalid_doi", "metadata": record})
        else:
            groups.setdefault(doi, []).append(record)
    frame = []
    for doi, items in sorted(groups.items()):
        evidence = [json.loads(s) for s in sorted({canonical_json(x) for x in items})]
        dates = sorted({d for x in evidence if (d := exact_date(x.get("publication_date")))})
        date = dates[0] if dates else None
        reason = None
        if doi in excluded:
            reason = "previously_screened"
        elif any(x.get("is_retracted") is True for x in evidence):
            reason = "metadata_reports_retracted"
        elif date is None:
            reason = "no_exact_publication_date"
        elif not START <= date <= END:
            reason = "publication_date_outside_window"
        elif not any(x.get("is_oa") is True for x in evidence):
            reason = "no_open_access_metadata"
        if reason:
            exclusions.append({"doi": doi, "reason": reason, "metadata": evidence})
            continue
        frame.append({
            "doi": doi, "order_sha256": order_hash(doi),
            "publication_date": date, "all_exact_dates": dates,
            "date_conflict": len(dates) > 1,
            "screen_status": "NOT_SCREENED", "metadata": evidence,
        })
    frame.sort(key=lambda row: (row["order_sha256"], row["doi"]))
    for rank, row in enumerate(frame, 1):
        row["frame_rank"] = rank
        row["within_five_screen_limit"] = rank <= 5
    exclusions.sort(key=canonical_json)
    return frame, exclusions


def write_jsonl(path, rows):
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        for row in rows:
            stream.write(canonical_json(row) + "\n")


def validate_v1_rows(rows):
    """Reconcile archived metadata, not candidate eligibility.

    The input is the complete original v1 frame. A reconstructed 16-row cut is refused."""
    if len(rows) != V1_FRAME_RECORD_COUNT:
        raise FrameError("Archived v1 frame is not the complete original frame "
                         f"({V1_FRAME_RECORD_COUNT} records); a cut or rebuilt frame is refused")
    if len(V1_INVENTORY) > len(rows):
        raise FrameError("Archived v1 frame is shorter than the triaged inventory")
    seen = set()
    prior = None
    for rank, row in enumerate(rows, 1):
        doi = row.get("doi")
        if normalize_doi(doi) != doi or doi in seen:
            raise FrameError("Invalid or duplicate v1 DOI; reconcile before release")
        if rank <= len(V1_INVENTORY) and V1_INVENTORY[rank - 1]["doi"] != doi:
            raise FrameError("Unexpected v1 DOI in the triaged inventory ranks; reconcile before release")
        seen.add(doi)
        digest = order_hash(doi, V1_SEED)
        if row.get("frame_rank") != rank:
            raise FrameError("v1 archived rank differs from retained triage evidence")
        if row.get("order_sha256") != digest:
            raise FrameError("v1 archived ordering digest mismatch")
        key = (digest, doi)
        if prior is not None and key <= prior:
            raise FrameError("v1 frame is not in its original seeded order")
        prior = key
    if [r["doi"] for r in rows if r["doi"] in V1_DEFERRED] != V1_DEFERRED:
        raise FrameError("Deferred v1 queue differs from the supplied C1 remainder")
    return rows


def load_v1_frame(path, expected_hash):
    body = Path(path).read_bytes()
    if sha256_bytes(body) != expected_hash:
        raise FrameError("Original v1 frame hash does not match the reconciled release receipt")
    rows = [json.loads(line) for line in body.decode("utf-8").splitlines() if line.strip()]
    if not all(isinstance(r, dict) for r in rows):
        raise FrameError("v1 frame must be JSON objects")
    return validate_v1_rows(rows)


def continuation_frame(rows):
    """Option A retains v1 hashes and order; never applies the new seed."""
    result = []
    for row in rows:
        if row["doi"] not in V1_DEFERRED:
            continue
        item = dict(row)
        item.update(v1_frame_rank=row["frame_rank"], frame_rank=len(result) + 1,
                    frame_option="A", ordering_seed=V1_SEED,
                    screen_status="NOT_SCREENED",
                    within_five_screen_limit=len(result) < 5)
        result.append(item)
    if [x["doi"] for x in result] != V1_DEFERRED:
        raise FrameError("Incomplete continuation queue")
    return result


def require_utc(value):
    try:
        stamp = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        if stamp.utcoffset() != dt.timedelta(0) or stamp > dt.datetime.now(dt.timezone.utc):
            raise ValueError("Not a past UTC timestamp")
        return stamp
    except (AttributeError, TypeError, ValueError) as exc:
        raise FrameError("A valid past UTC timestamp is required") from exc


def check_release(path, option):
    """Local assertions only: the coordinator must verify approval and release."""
    if DRAFT_ONLY:
        raise FrameError("DRAFT: no execution authorized. A new Mahmood decision and approved frozen copy are required")
    if option != APPROVED_OPTION:
        raise FrameError("Option " + str(option) + " was not chosen (Mahmood 2026-10-30 approved Option A only); refusing")
    receipt = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(receipt, dict):
        raise FrameError("Release receipt must be an object")
    required = {
        "paper": PAPER, "version": "P02-screen-v2", "frame_option": option,
        "new_seed": SEED, "ordering_seed": V1_SEED if option == "A" else SEED,
        "decision_by": "Mahmood", "decision": "APPROVE_ONE_FIVE_SCREEN_BATCH",
        "v1_inventory_reconciled": True,
        "v1_inventory_record_count": len(V1_INVENTORY),
    }
    for key, value in required.items():
        if type(receipt.get(key)) is not type(value) or receipt.get(key) != value:
            raise FrameError("Release/decision receipt mismatch: " + key)
    if not isinstance(receipt.get("decision_evidence"), str) or not receipt["decision_evidence"].strip():
        raise FrameError("Recorded Mahmood decision evidence is required")
    approved = require_utc(receipt.get("approved_at_utc"))
    released = require_utc(receipt.get("released_at_utc"))
    if approved > released:
        raise FrameError("Approval must precede release")
    expected_url = "https://github.com/mahmood726-cyber/usecase-preregistrations/releases/tag/P02-screen-v2"
    if receipt.get("github_release_url") != expected_url:
        raise FrameError("A distinct public P02-screen-v2 release is required; v1 cannot authorize v2")
    doi = receipt.get("zenodo_doi")
    if not isinstance(doi, str) or not (doi == "PENDING" or re.fullmatch(r"10\.5281/zenodo\.\d+", doi)):
        raise FrameError("Record the screening DOI or PENDING")
    for field, file in (
        ("script_sha256", Path(__file__).resolve()),
        ("prereg_sha256", OUT_ROOT / "PREREG_P02_screen_v2_DRAFT.md"),
    ):
        if receipt.get(field) != sha256_bytes(file.read_bytes()):
            raise FrameError("Local frozen hash mismatch: " + field)
    if not isinstance(receipt.get("v1_frame_sha256"), str) or not re.fullmatch(r"[0-9a-f]{64}", receipt["v1_frame_sha256"]):
        raise FrameError("Reconciled original v1 frame SHA-256 required")
    return receipt


def execute(out_dir, receipt, option, v1_rows, fetch=fetch_json, pace=True):
    """Construct bibliographic metadata only; this never screens or scores."""
    if option not in {"A", "B"}:
        raise FrameError("Choose exactly one authorized option")
    if receipt.get("frame_option") != option:
        raise FrameError("Receipt option mismatch")
    validate_v1_rows(v1_rows)
    out_dir = Path(out_dir).resolve()
    if not out_dir.is_relative_to(OUT_ROOT) or out_dir == OUT_ROOT:
        raise FrameError("Use a fresh run subdirectory below this script's out/")
    names = ["query_log_P02_v2.jsonl", "frame_P02_v2.jsonl",
             "metadata_exclusions_P02_v2.jsonl", "run_manifest_P02_v2.json"]
    if any((out_dir / name).exists() for name in names):
        raise FrameError("Preserve earlier runs; output files will not be overwritten")
    out_dir.mkdir(parents=True, exist_ok=True)
    excluded = EXCLUDED if option == "A" else EXCLUDED | {r["doi"] for r in v1_rows}
    manifest = {
        "paper": PAPER, "version": "P02-screen-v2", "frame_option": option,
        "new_seed": SEED, "ordering_seed": V1_SEED if option == "A" else SEED,
        "started_at_utc": utc_now(), "status": "INCOMPLETE",
        "candidate_screening_performed": False, "candidate_scoring_performed": False,
        "release_receipt": receipt, "v1_frame_sha256": receipt["v1_frame_sha256"],
        "discovery_sources": ["archived_v1_frame"] if option == "A" else ["europe_pmc"],
        "date_window": [START, END], "excluded_dois": sorted(excluded), "queries": [],
    }
    try:
        with (out_dir / names[0]).open("x", encoding="utf-8", newline="\n") as stream:
            def emit(event):
                stream.write(canonical_json(event) + "\n")
                stream.flush()
            if option == "A":
                frame = continuation_frame(v1_rows)
                triaged = {x["doi"] for x in V1_INVENTORY}
                exclusions = [
                    {"doi": r["doi"], "v1_frame_rank": r["frame_rank"],
                     "reason": ("v1_terminal_screen" if r["doi"] in triaged
                                else "v1_never_triaged_outside_option_A_queue"),
                     "metadata": r.get("metadata", [])}
                    for r in v1_rows if r["doi"] not in V1_DEFERRED
                ]
                emit({"event": "archived_v1_continuation", "network_requests": 0,
                      "v1_frame_sha256": receipt["v1_frame_sha256"],
                      "preserved_v1_ranks": [r["v1_frame_rank"] for r in frame]})
            else:
                records = []
                for query_id, source, query in QUERIES:
                    rows, report = harvest(query_id, source, query, fetch, emit, pace)
                    records.extend(rows)
                    manifest["queries"].append(report)
                frame, exclusions = make_frame(records, excluded=excluded)
                for row in frame:
                    row.update(frame_option="B", ordering_seed=SEED)
                for row in exclusions:
                    if row.get("doi") in V1_DEFERRED:
                        row["reason"] = "v1_deferred_reserved_outside_fresh_frame_not_a_failure"
                manifest["raw_record_count"] = len(records)
            write_jsonl(out_dir / names[2], exclusions)
            write_jsonl(out_dir / names[1], frame)
            manifest.update(status="COMPLETE", frame_count=len(frame),
                            metadata_exclusion_count=len(exclusions),
                            full_screens_planned=min(5, len(frame)))
    except Exception as exc:
        manifest.update(status="FAILED_BLOCKED", error=f"{type(exc).__name__}: {exc}")
        raise
    finally:
        manifest["ended_at_utc"] = utc_now()
        manifest["output_hashes"] = {
            name: sha256_bytes((out_dir / name).read_bytes())
            for name in names[:3] if (out_dir / name).exists()
        }
        with (out_dir / names[3]).open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    return manifest


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--print-queries", action="store_true",
                        help="Print exact prospective URLs without network or files")
    parser.add_argument("--run", action="store_true", help="Build an authorized metadata frame")
    parser.add_argument("--fetch", action="store_true", help="Opt in to Option B metadata retrieval")
    parser.add_argument("--frame-option", choices=("A", "B"))
    parser.add_argument("--release-record", type=Path)
    parser.add_argument("--v1-frame", type=Path, help="Original complete archived frame, not a reconstructed queue")
    parser.add_argument("--out-dir", type=Path, default=OUT_ROOT / "screen_run_P02_v2")
    args = parser.parse_args(argv)
    if args.print_queries:
        if args.run or args.fetch:
            parser.error("--print-queries is an offline-only mode")
        for qid, source, query in QUERIES:
            print(qid + " " + request_url(source, query))
        print("OpenAlex novelty DOI lookup: https://api.openalex.org/works/https://doi.org/<doi>")
        print("OpenAlex novelty citations: https://api.openalex.org/works?filter=cites:<W_ID>&per-page=100&page=1")
        return 0
    if not args.run or not args.frame_option or not args.release_record or not args.v1_frame:
        parser.error("--run, --frame-option, --release-record and --v1-frame are required; no default action")
    if (args.frame_option == "B") != args.fetch:
        parser.error("Option B requires --fetch; Option A must not request fresh retrieval")
    try:
        receipt = check_release(args.release_record, args.frame_option)
        rows = load_v1_frame(args.v1_frame, receipt["v1_frame_sha256"])
        manifest = execute(args.out_dir, receipt, args.frame_option, rows)
    except (FrameError, OSError, ValueError, TypeError, KeyError) as exc:
        print("STOP: " + str(exc), file=sys.stderr)
        return 1
    print(f"Metadata frame COMPLETE: {manifest['frame_count']} records; no candidate screened or scored.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
