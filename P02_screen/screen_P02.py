#!/usr/bin/env python3
"""P02 Europe-PMC-only frame and per-candidate OpenAlex citation retrieval.
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
SEED = "2026102802"
START, END = "2016-10-28", "2026-10-28"
OUT_ROOT = Path(__file__).resolve().parent
EXCLUDED = frozenset({
    "10.1186/s13643-025-02800-8", "10.1016/j.envint.2020.105739",
    "10.1136/bmj.j5855", "10.1016/j.envint.2020.105746",
    "10.3390/nu14010174",
})
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


def order_hash(doi):
    return sha256_bytes(f"{SEED}|{PAPER}|screen|{doi}".encode("utf-8"))


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
            "cited_by_count": raw.get("citedByCount"), "is_retracted": False,
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
        "User-Agent": "P02-preregistered-bibliographic-frame/2.0",
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


def openalex_work_id(value):
    if not isinstance(value, str):
        raise FrameError("OpenAlex record lacks a valid W identifier")
    value = value.removeprefix("https://openalex.org/")
    if not re.fullmatch(r"W[0-9]+", value):
        raise FrameError("OpenAlex record lacks a valid W identifier")
    return value


def citing_works_url(work_id, page):
    work_id = openalex_work_id(work_id)
    if isinstance(page, bool) or not isinstance(page, int) or not 1 <= page <= 100:
        raise FrameError("OpenAlex novelty page must be between 1 and 100")
    return "https://api.openalex.org/works?" + urllib.parse.urlencode([
        ("filter", "cites:" + work_id), ("per-page", OA_PAGE_SIZE), ("page", page),
    ])


def project_citing_work(raw):
    if not isinstance(raw, dict):
        raise FrameError("Invalid OpenAlex citing record")
    work_id = openalex_work_id(raw.get("id"))
    return {
        "source": "openalex", "record_id": work_id,
        "doi": normalize_doi(raw.get("doi")), "title": raw.get("title"),
        "publication_date": raw.get("publication_date"),
        "cited_by_count": raw.get("cited_by_count"),
    }


def harvest_openalex_citations(work_id, fetch, emit, pace=True):
    """Per-candidate novelty only. An empty terminal page establishes completion.
    At 100 pages/10,000 records, retain the partial list and disclose the limit.
    No equivalence judgment or novelty clearance is made by this function.
    """
    work_id = openalex_work_id(work_id)
    records, seen = [], set()
    report = {"work_id": work_id, "reported_count": None, "retrieved_count": 0,
              "pages": 0, "complete": False, "status": "INCOMPLETE",
              "terminal_empty_page": False, "record_limit": OA_RECORD_LIMIT}
    url = None
    try:
        for page in range(1, OA_RECORD_LIMIT // OA_PAGE_SIZE + 1):
            url = citing_works_url(work_id, page)
            data, receipt = fetch(url)
            meta = data.get("meta")
            if not isinstance(meta, dict):
                raise FrameError("OpenAlex novelty: invalid meta")
            count, rows = meta.get("count"), data.get("results")
            if (isinstance(count, bool) or not isinstance(count, int) or count < 0
                    or not isinstance(rows, list) or len(rows) > OA_PAGE_SIZE):
                raise FrameError("OpenAlex novelty: invalid count/results/page size")
            if report["reported_count"] is None:
                report["reported_count"] = count
            if count != report["reported_count"]:
                raise FrameError("OpenAlex novelty: count changed during pagination")
            projected = [project_citing_work(row) for row in rows]
            page_ids = [row["record_id"] for row in projected]
            if len(set(page_ids)) != len(page_ids) or seen.intersection(page_ids):
                raise FrameError("OpenAlex novelty: repeated record across pages")
            if len(records) + len(projected) > count:
                raise FrameError("OpenAlex novelty: retrieved more than reported")
            seen.update(page_ids)
            records.extend(projected)
            report.update(pages=page, retrieved_count=len(records))
            emit({"event": "novelty_page", "source": "openalex", "url": url,
                  "receipt": receipt, "page": page, "reported_count": count,
                  "retrieved_count": len(records), "records": projected})
            if not rows:
                report["terminal_empty_page"] = True
                if len(records) != count:
                    raise FrameError("OpenAlex novelty: empty page before reported total")
                report.update(complete=True, status="COMPLETE")
                return records, report
            if len(records) >= OA_RECORD_LIMIT or page == OA_RECORD_LIMIT // OA_PAGE_SIZE:
                report.update(status="INCOMPLETE_LIMIT",
                              error="Page/10,000-record ceiling reached before an empty terminal page")
                emit({"event": "novelty_incomplete", "at_utc": utc_now(), **report})
                return records, report
            if pace:
                time.sleep(1)
    except Exception as exc:
        report.update(status="FAILED_BLOCKED", error=f"{type(exc).__name__}: {exc}")
        emit({"event": "novelty_failure", "url": url, "at_utc": utc_now(),
              "attempts": getattr(exc, "attempts", []), **report})
        return records, report


def execute_openalex_novelty(out_dir, receipt, doi, fetch=fetch_json, pace=True):
    """Save a citation-coverage report; human equivalence review remains required."""
    doi = normalize_doi(doi)
    if doi is None:
        raise FrameError("A normalized candidate DOI is required")
    out_dir = Path(out_dir).resolve()
    if not out_dir.is_relative_to(OUT_ROOT):
        raise FrameError("Output directory must be under the script's out/ directory")
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir / "novelty_openalex_P02.jsonl"
    report_path = out_dir / "novelty_openalex_P02.json"
    if log_path.exists() or report_path.exists():
        raise FrameError("Preserve existing novelty outputs; use a new candidate subdirectory")
    report = {"paper": PAPER, "candidate_doi": doi, "started_at_utc": utc_now(),
              "release_receipt": receipt, "purpose": "per_candidate_novelty_only",
              "complete": False, "status": "INCOMPLETE", "retrieved_count": 0,
              "reported_count": None, "equivalence_assessed": False,
              "novelty_cleared": False}
    with log_path.open("x", encoding="utf-8", newline="\n") as stream:
        def emit(event):
            stream.write(canonical_json(event) + "\n")
            stream.flush()
        url = "https://api.openalex.org/works/https://doi.org/" + urllib.parse.quote(doi, safe="/")
        try:
            data, lookup_receipt = fetch(url)
            if normalize_doi(data.get("doi")) != doi:
                raise FrameError("OpenAlex DOI lookup does not match candidate")
            work_id = openalex_work_id(data.get("id"))
            report["candidate_metadata"] = project_citing_work(data)
            emit({"event": "novelty_lookup", "url": url, "receipt": lookup_receipt,
                  "record": report["candidate_metadata"]})
            _, coverage = harvest_openalex_citations(work_id, fetch, emit, pace)
            report.update(coverage)
        except Exception as exc:
            report.update(status="FAILED_BLOCKED", error=f"{type(exc).__name__}: {exc}")
            emit({"event": "novelty_failure", "url": url, "at_utc": utc_now(),
                  "error": report["error"], "complete": False,
                  "attempts": getattr(exc, "attempts", [])})
    report.update(ended_at_utc=utc_now(), log_sha256=sha256_bytes(log_path.read_bytes()))
    with report_path.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    return report


def exact_date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return None
    try:
        return dt.date.fromisoformat(value).isoformat()
    except ValueError:
        return None


def make_frame(records):
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
        if doi in EXCLUDED:
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


def check_release(path):
    """Check a coordinator receipt locally, not the remote release's existence."""
    receipt = json.loads(Path(path).read_text(encoding="utf-8"))
    for field, file in (("script_sha256", Path(__file__).resolve()),
                        ("prereg_sha256", OUT_ROOT / "PREREG_P02_screen.md")):
        if receipt.get(field) != sha256_bytes(file.read_bytes()):
            raise FrameError(f"Release receipt {field} does not match local file")
    url = receipt.get("github_release_url", "")
    if not url.startswith("https://github.com/mahmood726-cyber/usecase-preregistrations/releases/tag/") or not url.rsplit("/", 1)[-1]:
        raise FrameError("A public screening GitHub release URL is required")
    if not (receipt.get("zenodo_doi") == "PENDING" or re.fullmatch(r"10\.5281/zenodo\.\d+", receipt.get("zenodo_doi", ""))):
        raise FrameError("The screening release's Zenodo DOI is required")
    try:
        released = dt.datetime.fromisoformat(receipt["released_at_utc"].replace("Z", "+00:00"))
        if released.utcoffset() != dt.timedelta(0) or released > dt.datetime.now(dt.timezone.utc):
            raise ValueError("Invalid UTC timestamp")
    except (KeyError, ValueError, TypeError) as exc:
        raise FrameError("Valid server release UTC timestamp required") from exc
    return {key: receipt[key] for key in (
        "script_sha256", "prereg_sha256", "github_release_url", "zenodo_doi",
        "released_at_utc")}


def write_jsonl(path, rows):
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        for row in rows:
            stream.write(canonical_json(row) + "\n")


def execute(out_dir, receipt, fetch=fetch_json, pace=True):
    out_dir = Path(out_dir).resolve()
    if not out_dir.is_relative_to(OUT_ROOT):
        raise FrameError("Output directory must be under the script's out/ directory")
    out_dir.mkdir(parents=True, exist_ok=True)
    names = ["query_log_P02.jsonl", "frame_P02.jsonl", "metadata_exclusions_P02.jsonl",
             "run_manifest_P02.json"]
    if any((out_dir / name).exists() for name in names):
        raise FrameError("Preserve existing outputs; use a new run subdirectory")
    manifest = {"paper": PAPER, "seed": SEED, "started_at_utc": utc_now(),
                "status": "INCOMPLETE", "candidate_screening_performed": False,
                "discovery_sources": ["europe_pmc"],
                "release_receipt": receipt, "queries": [],
                "date_window": [START, END], "excluded_dois": sorted(EXCLUDED)}
    log_path = out_dir / names[0]
    try:
        with log_path.open("x", encoding="utf-8", newline="\n") as stream:
            def emit(event):
                stream.write(canonical_json(event) + "\n")
                stream.flush()
            all_records = []
            for query_id, source, query in QUERIES:
                rows, report = harvest(query_id, source, query, fetch, emit, pace)
                all_records.extend(rows)
                manifest["queries"].append(report)
            frame, exclusions = make_frame(all_records)
            write_jsonl(out_dir / names[2], exclusions)
            write_jsonl(out_dir / names[1], frame)
            manifest.update(status="COMPLETE", raw_record_count=len(all_records),
                            frame_count=len(frame), metadata_exclusion_count=len(exclusions),
                            full_screens_planned=min(5, len(frame)))
    except Exception as exc:
        manifest["status"] = "FAILED_BLOCKED"
        manifest["error"] = f"{type(exc).__name__}: {exc}"
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
                        help="Print frozen URLs; no network or files")
    parser.add_argument("--novelty-doi", help="Retrieve OpenAlex citations for this screened DOI only")
    parser.add_argument("--fetch", action="store_true",
                        help="Fetch bibliographic metadata after release")
    parser.add_argument("--release-record", type=Path, help="Coordinator release-receipt JSON")
    parser.add_argument("--out-dir", type=Path, default=OUT_ROOT / "screen_run_P02")
    args = parser.parse_args(argv)
    if args.print_queries:
        for query_id, source, query in QUERIES:
            print(query_id + " " + request_url(source, query))
        return 0
    if not args.fetch or not args.release_record:
        parser.error("No network by default: --fetch and --release-record are both required")
    try:
        receipt = check_release(args.release_record)
        if args.novelty_doi:
            report = execute_openalex_novelty(args.out_dir, receipt, args.novelty_doi)
            print(f"OpenAlex citation coverage: {report['status']}; equivalence not assessed.")
            return 0 if report["complete"] else 1
        manifest = execute(args.out_dir, receipt)
    except (FrameError, OSError, ValueError, TypeError) as exc:
        print("STOP: " + str(exc), file=sys.stderr)
        return 1
    print(f"Bibliographic frame complete: {manifest['frame_count']} records; no candidates screened.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
