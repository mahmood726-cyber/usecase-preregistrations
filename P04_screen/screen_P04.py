#!/usr/bin/env python3
"""Frozen P04 bibliographic frame builder. No full-text screening or analysis.

Default output is this script's directory (out/). Network mode requires the
public screening-release identifiers and matching local frozen-file hashes.
Discovery uses Europe PMC ONLY. OpenAlex is used only by the optional
per-candidate citing-works helper, never to populate the discovery frame.
"""
import argparse
from datetime import date, datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
import time
from urllib.parse import quote, unquote, urlencode, urlsplit

PAPER = "P04"
SEED = "2026102804"
START = "2016-10-28"
END = "2026-10-28"
EUROPE_PMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
OPENALEX = "https://api.openalex.org/works"
EPMC_QUERY = (
    '(TITLE_ABS:"network meta-analysis" OR TITLE_ABS:"network meta-analyses" '
    'OR TITLE_ABS:"network meta analysis" OR TITLE_ABS:"network metaanalysis" '
    'OR TITLE_ABS:"mixed treatment comparison" '
    'OR TITLE_ABS:"mixed-treatment comparison") '
    'AND (TITLE_ABS:diabet* OR TITLE_ABS:antidiabet* '
    'OR TITLE_ABS:antihyperglyc*) '
    'AND FIRST_PDATE:[2016-10-28 TO 2026-10-28] AND OPEN_ACCESS:Y'
)
EPMC_RETRY_DELAYS = (1, 2, 4, 8)  # Initial request + four retries; 15 s total backoff.
OA_CITES_PAGE_SIZE = 100
OA_CITES_LIMIT = 10000
EXCLUDED_DOIS = frozenset({
    "10.1111/dom.15725",
    "10.1186/s12933-023-02035-8",
    "10.1007/s00125-024-06144-1",
    "10.1136/bmj-2023-076410",
    "10.1111/1753-0407.70192",
})


class RetrievalError(RuntimeError):
    pass


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def canonical_doi(value):
    """Lowercase DOI; decode resolver paths; never strip suffix punctuation."""
    if not isinstance(value, str):
        return None
    value = value.strip()
    if value.lower().startswith(("https://", "http://")):
        parsed = urlsplit(value)
        if parsed.hostname not in ("doi.org", "dx.doi.org", "www.doi.org"):
            return None
        value = parsed.path.lstrip("/")
    elif value.lower().startswith("doi:"):
        value = value[4:].strip()
    value = unquote(value).lower()
    return value if re.fullmatch(r"10\.\d{4,9}/\S+", value) else None


def valid_date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return None
    try:
        date.fromisoformat(value)
    except ValueError:
        return None
    return value


def specifications():
    yield "epmc", "epmc-01", {
        "query": EPMC_QUERY, "format": "json", "resultType": "lite",
        "pageSize": "1000",
    }


def query_url(provider, params, cursor="*"):
    if provider != "epmc":
        raise ValueError("Discovery frame is Europe PMC only")
    params = dict(params)
    params["cursorMark"] = cursor
    return EUROPE_PMC + "?" + urlencode(params, quote_via=quote)


def normalise_record(provider, query_id, item):
    if not isinstance(item, dict):
        raise RetrievalError("Non-object metadata record")
    if provider == "epmc":
        record_id = f"{item.get('source', '')}:{item.get('id', '')}"
        if not item.get("source") or not item.get("id"):
            raise RetrievalError("Europe PMC record lacks source/id")
        return {
            "provider": provider, "query_id": query_id, "record_id": record_id,
            "doi_raw": item.get("doi"), "title": item.get("title"),
            "publication_date": item.get("firstPublicationDate"),
            "is_oa": item.get("isOpenAccess") == "Y",
            "journal": item.get("journalTitle"),
            "pmcid": item.get("pmcid"), "cited_by_count": item.get("citedByCount"),
        }
    raise RetrievalError("Discovery frame is Europe PMC only")


def get_json(url, audit, *, opener=None, sleep=None):
    # Lazy import permits completely offline tests on restricted desktop nodes.
    from urllib.error import HTTPError, URLError
    from urllib.request import Request, urlopen

    opener = opener or urlopen
    sleep = sleep or time.sleep
    parsed = urlsplit(url)
    is_epmc = (parsed.scheme == "https" and parsed.netloc == "www.ebi.ac.uk"
               and parsed.path.startswith("/europepmc/webservices/rest/"))
    delays = EPMC_RETRY_DELAYS if is_epmc else ()
    for attempt in range(len(delays) + 1):
        entry = {"url": url, "requested_at_utc": utc_now(), "attempt": attempt + 1}
        audit["requests"].append(entry)
        try:
            request = Request(url, headers={
                "User-Agent": "P04-screen-prereg/2.0 (public bibliographic metadata)",
                "Accept": "application/json",
            })
            with opener(request, timeout=45) as response:
                entry["http_status"] = response.status
                raw = response.read()
            entry["response_sha256"] = sha256(raw)
            try:
                obj = json.loads(raw)
            except (UnicodeError, json.JSONDecodeError) as exc:
                entry["status"] = "blocked_or_non_json"
                raise RetrievalError("Non-JSON response; no bypass or alternate endpoint") from exc
            if not isinstance(obj, dict):
                entry["status"] = "schema_error"
                raise RetrievalError("JSON response is not an object")
            entry["status"] = "ok"
            return obj
        except HTTPError as exc:
            entry["http_status"] = exc.code
            entry["status"] = "blocked" if exc.code in (401, 403, 429) else "http_error"
            retryable = 500 <= exc.code <= 599 and is_epmc
            exc.close()
            if retryable and attempt < len(delays):
                entry["status"] = "retryable_5xx"
                entry["backoff_seconds"] = delays[attempt]
                sleep(delays[attempt])
                continue
            if retryable:
                entry["status"] = "5xx_retries_exhausted"
            raise RetrievalError(f"HTTP {exc.code}; retrieval failed; no login or workaround") from exc
        except (URLError, TimeoutError, OSError) as exc:
            entry["status"] = "transport_error"
            raise RetrievalError(f"Transport failure: {type(exc).__name__}") from exc


def retrieve_query(provider, query_id, params, get_page, audit):
    if provider != "epmc":
        raise RetrievalError("Discovery frame is Europe PMC only")
    cursor, seen_cursors, total, received = "*", set(), None, 0
    records = []
    seen_records = set()
    summary = {
        "provider": provider, "query_id": query_id, "params": params,
        "status": "incomplete", "reported_count": None, "received": 0,
        "records": records,
    }
    audit["queries"].append(summary)
    while True:
        if cursor in seen_cursors:
            raise RetrievalError(f"{query_id}: repeated pagination cursor")
        seen_cursors.add(cursor)
        url = query_url(provider, params, cursor)
        obj = get_page(url, audit)
        try:
            count = obj["hitCount"]
            items = obj["resultList"]["result"]
            next_cursor = obj.get("nextCursorMark")
        except (KeyError, TypeError) as exc:
            raise RetrievalError(f"{query_id}: unsupported response schema") from exc
        if isinstance(count, bool) or not isinstance(count, int) or count < 0:
            raise RetrievalError(f"{query_id}: invalid total")
        if not isinstance(items, list):
            raise RetrievalError(f"{query_id}: results is not a list")
        if total is None:
            total = count
            summary["reported_count"] = count
        elif count != total:
            raise RetrievalError(f"{query_id}: total changed during pagination")
        for item in items:
            record = normalise_record(provider, query_id, item)
            if record["record_id"] in seen_records:
                raise RetrievalError(f"{query_id}: duplicate source/id during pagination")
            seen_records.add(record["record_id"])
            records.append(record)
        received += len(items)
        summary["received"] = received
        if received > total:
            raise RetrievalError(f"{query_id}: more rows than reported")
        if received == total:
            summary["status"] = "complete"
            return records
        if not items or not isinstance(next_cursor, str) or not next_cursor:
            raise RetrievalError(f"{query_id}: incomplete pagination")
        cursor = next_cursor


def openalex_cites_url(work_id, page):
    if not re.fullmatch(r"W[0-9]+", work_id or ""):
        raise ValueError("Use the candidate's canonical OpenAlex W identifier")
    if isinstance(page, bool) or not isinstance(page, int) or not 1 <= page <= 100:
        raise ValueError("OpenAlex citation page must be 1..100")
    return OPENALEX + "?" + urlencode({
        "filter": "cites:" + work_id, "per-page": OA_CITES_PAGE_SIZE, "page": page,
    }, quote_via=quote)


def retrieve_openalex_citations(work_id, get_page, audit):
    """Candidate novelty metadata only; no discovery or equivalence decision.

    Stop at an empty page, or at 10,000 records / 100 pages. Never use a cursor
    or exceed the basic-paging cap. Exactly 10,000 remains incomplete if an
    empty terminal page cannot be observed within that cap. Preserve partial
    bibliographies and source/retrieved totals separately.
    """
    openalex_cites_url(work_id, 1)
    summary = {
        "provider": "openalex", "purpose": "candidate_novelty_only", "work_id": work_id,
        "status": "incomplete", "reported_count": None, "received": 0,
        "empty_terminal_page": False, "records": [], "pages": [],
    }
    audit.setdefault("novelty_queries", []).append(summary)
    seen_ids, total = set(), None
    try:
        for page in range(1, OA_CITES_LIMIT // OA_CITES_PAGE_SIZE + 1):
            url = openalex_cites_url(work_id, page)
            obj = get_page(url, audit)
            try:
                count, items = obj["meta"]["count"], obj["results"]
            except (KeyError, TypeError) as exc:
                raise RetrievalError("OpenAlex: unsupported citation response schema") from exc
            if isinstance(count, bool) or not isinstance(count, int) or count < 0:
                raise RetrievalError("OpenAlex: invalid citation total")
            if not isinstance(items, list) or len(items) > OA_CITES_PAGE_SIZE:
                raise RetrievalError("OpenAlex: invalid citation page")
            if total is None:
                total = count
                summary["reported_count"] = count
            elif count != total:
                raise RetrievalError("OpenAlex: citation total changed during pagination")
            summary["pages"].append({"page": page, "url": url, "received": len(items)})
            if not items:
                summary["empty_terminal_page"] = True
                if summary["received"] == total and total <= OA_CITES_LIMIT:
                    summary["status"] = "complete"
                else:
                    summary["reason"] = "reported_and_retrieved_counts_differ"
                return summary
            for item in items:
                if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not item["id"]:
                    raise RetrievalError("OpenAlex: citation lacks id")
                if item["id"] in seen_ids:
                    raise RetrievalError("OpenAlex: duplicate citing-work id during pagination")
                seen_ids.add(item["id"])
                summary["records"].append(item)
                summary["received"] += 1
            if summary["received"] > total:
                raise RetrievalError("OpenAlex: more citations than reported")
        summary["reason"] = ("reported_count_exceeds_10000" if total > OA_CITES_LIMIT
                             else "page_cap_without_empty_terminal_page")
    except Exception as exc:
        summary["reason"] = "retrieval_failed"
        summary["error"] = f"{type(exc).__name__}: {exc}"
    return summary


def ordered_frame(records):
    """Bibliographic eligibility only; never infer clinical eligibility."""
    grouped, exclusions = {}, []
    for record in records:
        doi = canonical_doi(record.get("doi_raw"))
        if doi is None:
            exclusions.append({"reason": "missing_or_invalid_doi", "record": record})
        else:
            grouped.setdefault(doi, []).append(record)
    frame = []
    for doi, group in sorted(grouped.items()):
        # Identical records may be returned by multiple frozen queries.
        unique = {json.dumps(r, sort_keys=True, ensure_ascii=True): r for r in group}
        group = [unique[k] for k in sorted(unique)]
        dates = sorted({d for r in group if (d := valid_date(r.get("publication_date")))})
        reasons = []
        if doi in EXCLUDED_DOIS:
            reasons.append("already_screened")
        if not dates:
            reasons.append("no_complete_publication_date")
        elif not START <= dates[0] <= END:
            reasons.append("earliest_observed_publication_date_outside_window")
        if not any(r.get("is_oa") is True for r in group):
            reasons.append("no_positive_oa_flag")
        if reasons:
            exclusions.append({"doi": doi, "reasons": reasons, "records": group})
            continue
        digest = sha256(f"{SEED}|{PAPER}|screen|{doi}".encode("utf-8"))
        frame.append({
            "doi": doi, "screen_hash": digest,
            "publication_date": dates[0],
            "observed_publication_dates": dates,
            "metadata_conflict": len(dates) > 1 or any(r.get("is_oa") is not True for r in group),
            "records": group, "screen_status": "UNSCREENED",
        })
    frame.sort(key=lambda r: (r["screen_hash"], r["doi"]))
    for rank, record in enumerate(frame, 1):
        record["screen_order"] = rank
    exclusions.sort(key=lambda r: json.dumps(r, sort_keys=True, ensure_ascii=True))
    return frame, exclusions


def harvest(get_page, audit):
    records = []
    audit["metadata_records"] = records
    for provider, query_id, params in specifications():
        records.extend(retrieve_query(provider, query_id, params, get_page, audit))
    frame, excluded = ordered_frame(records)
    audit["metadata_exclusions"] = excluded
    audit["frame_count"] = len(frame)
    return frame


def check_release(args):
    if not re.fullmatch(
        r"https://github\.com/mahmood726-cyber/usecase-preregistrations/releases/tag/[^\s?#]+",
        args.screen_release_url or "",
    ):
        raise ValueError("Supply the public screening release tag URL")
    if not ((args.screen_release_doi or "PENDING") == "PENDING" or re.fullmatch(r"https://doi\.org/10\.\d{4,9}/\S+", args.screen_release_doi)):
        raise ValueError("Supply the screening release's archival DOI URL")
    base = Path(__file__).resolve().parent
    files = {
        "prereg": (base / "PREREG_P04_screen.md", args.prereg_sha256),
        "script": (Path(__file__).resolve(), args.script_sha256),
    }
    hashes = {}
    for label, (path, expected) in files.items():
        actual = sha256(path.read_bytes())
        if not expected or actual != expected.lower():
            raise ValueError(f"{label}: local bytes do not match supplied frozen sha256")
        hashes[label] = actual
    # Syntax/local integrity checks only: pc2 must verify the public release,
    # its server timestamp, archived bytes and DOI before issuing this command.
    return {
        "screen_release_url": args.screen_release_url,
        "screen_release_doi": args.screen_release_doi,
        "local_sha256": hashes,
        "public_release_verified_by_script": False,
    }


def output_directory(directory):
    base = Path(__file__).resolve().parent
    chosen = Path(directory).resolve() if directory else base
    if not chosen.is_relative_to(base):
        raise ValueError("Output directory must be the script's out/ directory or a child")
    chosen.mkdir(parents=True, exist_ok=True)
    return chosen


def resolve_outputs(directory):
    chosen = output_directory(directory)
    frame_path = chosen / "frame_P04.jsonl"
    audit_path = chosen / "frame_P04_audit.json"
    if frame_path.exists() or audit_path.exists():
        raise ValueError("Refusing to overwrite a prior frame/audit; preserve the run")
    return frame_path, audit_path


def novelty_output(directory, work_id):
    openalex_cites_url(work_id, 1)
    path = output_directory(directory) / f"novelty_P04_openalex_{work_id}.json"
    if path.exists():
        raise ValueError("Refusing to overwrite a prior novelty audit")
    return path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--print-queries", action="store_true", help="Offline; no network or files")
    parser.add_argument("--openalex-cites", metavar="W_ID",
                        help="Candidate novelty only; never builds a discovery frame")
    parser.add_argument("--screen-release-url")
    parser.add_argument("--screen-release-doi")
    parser.add_argument("--prereg-sha256")
    parser.add_argument("--script-sha256")
    parser.add_argument("--output-dir", help="Default: beside this script, under out/")
    args = parser.parse_args(argv)
    if args.print_queries and args.openalex_cites:
        parser.error("--print-queries lists discovery only; do not combine modes")
    if args.print_queries:
        for provider, query_id, params in specifications():
            print(query_id + "\n" + query_url(provider, params))
        return 0
    try:
        release = check_release(args)
        if args.openalex_cites:
            citation_path = novelty_output(args.output_dir, args.openalex_cites)
        else:
            frame_path, audit_path = resolve_outputs(args.output_dir)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    audit = {
        "paper": PAPER, "seed": SEED, "date_window": [START, END],
        "status": "incomplete", "started_at_utc": utc_now(),
        "discovery_provider": "Europe PMC only",
        "release": release, "requests": [], "queries": [],
        "excluded_dois": sorted(EXCLUDED_DOIS),
        "note": "Bibliographic metadata only; no candidate screened or data extracted.",
    }
    if args.openalex_cites:
        audit["purpose"] = "candidate_novelty_only"
        summary = retrieve_openalex_citations(args.openalex_cites, get_json, audit)
        audit["status"] = summary["status"]
        audit["completed_at_utc"] = utc_now()
        audit["note"] = "OpenAlex citing metadata only; Europe PMC checks and equivalence adjudication remain separate."
        with citation_path.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(audit, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        print("OpenAlex novelty retrieval " + summary["status"] + ": " + str(citation_path))
        return 0 if summary["status"] == "complete" else 2
    try:
        frame = harvest(get_json, audit)
        payload = "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in frame)
        audit["frame_sha256"] = sha256(payload.encode("utf-8"))
        audit["status"] = "complete"
        audit["completed_at_utc"] = utc_now()
    except Exception as exc:
        audit["status"] = "failed_blocked"
        audit["retrieval_complete"] = False
        audit["screen_status"] = "FAILED_BLOCKED"
        audit["frame_count"] = None
        audit["error"] = f"{type(exc).__name__}: {exc}"
        audit["stopped_at_utc"] = utc_now()
        with audit_path.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(audit, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        print("STOP: screen FAILED/BLOCKED; incomplete retrieval, never zero; no frame written. See " + str(audit_path), file=sys.stderr)
        return 2
    # Every Europe PMC discovery page is required. OpenAlex is not in the frame.
    # No frame is ever emitted by a failed/partial retrieval.
    with audit_path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(audit, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    with frame_path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(payload)
    print(f"Wrote {len(frame)} UNSCREENED metadata records to {frame_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
