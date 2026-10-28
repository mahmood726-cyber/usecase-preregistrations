# SYNTHETIC - not data
"""Offline regression tests. Every API response below is invented metadata.
No API request, clinical analysis, real frame, or temporary fixture file is made.
Run: python out/synthetic_test_screen_P04.py
"""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import sys
import types
import unittest
from urllib.error import HTTPError, URLError
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

def deny_network(event, args):
    if event in ("socket.connect", "socket.getaddrinfo"):
        raise AssertionError("Live network forbidden in synthetic validation")


sys.addaudithook(deny_network)
sys.dont_write_bytecode = True
BASE = Path(__file__).resolve().parent
SCRIPT = BASE / "screen_P04.py"
m = types.ModuleType("synthetic_screen_under_test")
m.__file__ = str(SCRIPT)
exec(compile(SCRIPT.read_text(encoding="utf-8"), str(SCRIPT), "exec"), m.__dict__)


def record(doi="10.9999/synthetic-a", day="2020-01-01", oa=True, provider="epmc"):
    return {
        "data_status": "SYNTHETIC - not data",
        "provider": provider, "query_id": "synthetic-query",
        "record_id": "synthetic-id", "doi_raw": doi,
        "title": "SYNTHETIC - not data", "publication_date": day,
        "is_oa": oa, "journal": "Synthetic journal",
    }


def epmc_item(suffix="a"):
    return {
        "data_status": "SYNTHETIC - not data",
        "source": "MED", "id": "synthetic-" + suffix,
        "doi": "10.9999/synthetic-" + suffix,
        "title": "SYNTHETIC - not data",
        "firstPublicationDate": "2020-01-01", "isOpenAccess": "Y",
    }


def oa_item(suffix="a"):
    return {
        "data_status": "SYNTHETIC - not data",
        "id": "https://openalex.org/W_SYNTHETIC_" + suffix,
        "doi": "https://doi.org/10.9999/synthetic-" + suffix,
        "display_name": "SYNTHETIC - not data",
        "publication_date": "2020-01-01", "open_access": {"is_oa": True},
    }


def epmc_page(count, items, cursor=None):
    return {"data_status": "SYNTHETIC - not data", "hitCount": count,
            "resultList": {"result": items}, "nextCursorMark": cursor}


def oa_page(count, items, cursor=None):
    return {"data_status": "SYNTHETIC - not data",
            "meta": {"count": count, "next_cursor": cursor}, "results": items}


def paginate(provider, pages):
    urls, iterator = [], iter(pages)
    def fake_get(url, audit):
        urls.append(url)
        return next(iterator)
    audit = {"queries": [], "requests": []}
    rows = m.retrieve_query(provider, "synthetic-query", {}, fake_get, audit)
    return rows, urls, audit


class MemoryBuffer(io.StringIO):
    def close(self):
        pass


class MemoryPath:
    """Captures writes in memory; no fixture file is created."""
    def __init__(self, name):
        self.name, self.buffer, self.opens = name, MemoryBuffer(), 0

    def open(self, mode, **kwargs):
        if mode != "x":
            raise AssertionError("Must refuse overwrite")
        self.opens += 1
        return self.buffer

    def __str__(self):
        return self.name


class FrameTests(unittest.TestCase):
    def test_resolver_and_case_deduplication(self):
        self.assertEqual(m.canonical_doi(" HTTPS://doi.org/10.9999/SYNTHETIC%2DA "),
                         "10.9999/synthetic-a")
        self.assertEqual(m.canonical_doi("doi: 10.9999/SYNTHETIC-A"),
                         "10.9999/synthetic-a")
        frame, excluded = m.ordered_frame([
            record(), record("https://doi.org/10.9999/SYNTHETIC-A", provider="epmc")])
        self.assertEqual(len(frame), 1)
        self.assertEqual(len(frame[0]["records"]), 2)
        self.assertEqual(excluded, [])

    def test_preserves_significant_suffix(self):
        self.assertEqual(m.canonical_doi("10.9999/SYNTHETIC(a)."),
                         "10.9999/synthetic(a).")

    def test_invalid_doi_is_audited(self):
        for bad in [None, "", "synthetic", "10.9999/synthetic a", "https://example.org/10.9999/a"]:
            self.assertIsNone(m.canonical_doi(bad))
        frame, excluded = m.ordered_frame([record(doi=None)])
        self.assertEqual(frame, [])
        self.assertEqual(excluded[0]["reason"], "missing_or_invalid_doi")

    def test_seed_order_is_independent_of_input_order(self):
        rows = [record(f"10.9999/synthetic-{i}") for i in range(8)]
        first, exc1 = m.ordered_frame(rows)
        reverse, exc2 = m.ordered_frame(list(reversed(rows)))
        expected = sorted(
            [r["doi_raw"] for r in rows],
            key=lambda d: (hashlib.sha256(("2026102804|P04|screen|" + d).encode()).hexdigest(), d),
        )
        self.assertEqual(first, reverse)
        self.assertEqual(exc1, exc2)
        self.assertEqual([r["doi"] for r in first], expected)
        self.assertEqual([r["screen_order"] for r in first], list(range(1, 9)))
        self.assertTrue(all(r["screen_status"] == "UNSCREENED" for r in first))

    def test_no_five_hit_truncation(self):
        frame, _ = m.ordered_frame([record(f"10.9999/synthetic-{i}") for i in range(7)])
        self.assertEqual(len(frame), 7)

    def test_previously_screened_exclusion_survives_aliases(self):
        with patch.object(m, "EXCLUDED_DOIS", frozenset({"10.9999/synthetic-a"})):
            frame, excluded = m.ordered_frame([record("https://doi.org/10.9999/SYNTHETIC-A")])
        self.assertEqual(frame, [])
        self.assertIn("already_screened", excluded[0]["reasons"])

    def test_date_boundaries_and_missing_date(self):
        rows = [
            record("10.9999/synthetic-low", "2016-10-28"),
            record("10.9999/synthetic-high", "2026-10-28"),
            record("10.9999/synthetic-early", "2016-10-27"),
            record("10.9999/synthetic-late", "2026-10-29"),
            record("10.9999/synthetic-year", "2020"),
        ]
        frame, excluded = m.ordered_frame(rows)
        self.assertEqual({r["doi"] for r in frame},
                         {"10.9999/synthetic-low", "10.9999/synthetic-high"})
        self.assertEqual(len(excluded), 3)
        self.assertIsNone(m.valid_date("2020-02-31"))

    def test_earliest_conflicting_date_determines_eligibility(self):
        frame, excluded = m.ordered_frame([record(day="2016-10-27"),
                                          record(day="2016-10-28", provider="epmc")])
        self.assertEqual(frame, [])
        self.assertIn("earliest_observed_publication_date_outside_window",
                      excluded[0]["reasons"])

    def test_oa_conflicts_retained_and_flagged(self):
        frame, excluded = m.ordered_frame([record(oa=False), record(oa=True, provider="epmc")])
        self.assertEqual(len(frame), 1)
        self.assertTrue(frame[0]["metadata_conflict"])
        self.assertEqual(excluded, [])
        frame, excluded = m.ordered_frame([record(oa=False)])
        self.assertEqual(frame, [])
        self.assertIn("no_positive_oa_flag", excluded[0]["reasons"])

    def test_hash_collision_tie_break(self):
        with patch.object(m, "sha256", return_value="0" * 64):
            frame, _ = m.ordered_frame([record("10.9999/synthetic-z"),
                                        record("10.9999/synthetic-a")])
        self.assertEqual([r["doi"] for r in frame],
                         ["10.9999/synthetic-a", "10.9999/synthetic-z"])


class PaginationTests(unittest.TestCase):
    def test_epmc_complete_cursor_walk(self):
        rows, urls, audit = paginate("epmc", [
            epmc_page(2, [epmc_item("a")], "synthetic+/="),
            epmc_page(2, [epmc_item("b")]),
        ])
        self.assertEqual(len(rows), 2)
        self.assertEqual(parse_qs(urlsplit(urls[1]).query)["cursorMark"], ["synthetic+/="])
        self.assertEqual(audit["queries"][0]["status"], "complete")

    def test_true_empty_query_completes(self):
        rows, _, audit = paginate("epmc", [epmc_page(0, [])])
        self.assertEqual(rows, [])
        self.assertEqual(audit["queries"][0]["status"], "complete")

    def test_missing_cursor_cannot_certify_partial_frame(self):
        with self.assertRaisesRegex(m.RetrievalError, "incomplete pagination"):
            paginate("epmc", [epmc_page(2, [epmc_item()])])

    def test_repeating_cursor_stops(self):
        with self.assertRaisesRegex(m.RetrievalError, "repeated pagination cursor"):
            paginate("epmc", [epmc_page(3, [epmc_item()], "*")])

    def test_changing_count_stops(self):
        with self.assertRaisesRegex(m.RetrievalError, "total changed"):
            paginate("epmc", [epmc_page(2, [epmc_item()], "next"),
                              epmc_page(3, [epmc_item("b")])])

    def test_empty_intermediate_page_stops(self):
        with self.assertRaisesRegex(m.RetrievalError, "incomplete pagination"):
            paginate("epmc", [epmc_page(2, [], "next")])

    def test_oversized_result_stops(self):
        with self.assertRaisesRegex(m.RetrievalError, "more rows"):
            paginate("epmc", [epmc_page(1, [epmc_item(), epmc_item("b")])])

    def test_unexpected_schema_and_invalid_count_stop(self):
        for page in [{}, epmc_page(True, []), epmc_page(1, "not a list")]:
            with self.subTest(page=page), self.assertRaises(m.RetrievalError):
                paginate("epmc", [page])

    def test_missing_identity_stops(self):
        with self.assertRaisesRegex(m.RetrievalError, "lacks source/id"):
            paginate("epmc", [epmc_page(1, [{"title": "SYNTHETIC - not data"}])])

    def test_duplicate_source_ids_do_not_satisfy_total(self):
        with self.assertRaisesRegex(m.RetrievalError, "duplicate source/id"):
            paginate("epmc", [epmc_page(2, [epmc_item()], "next"),
                              epmc_page(2, [epmc_item()])])

    def test_discovery_is_epmc_only_and_harvests_every_page(self):
        called = []
        pages = iter([epmc_page(2, [epmc_item()], "next"),
                      epmc_page(2, [epmc_item("b")])])
        def fake_get(url, audit):
            called.append(url)
            self.assertEqual(urlsplit(url).netloc, "www.ebi.ac.uk")
            return next(pages)
        audit = {"queries": [], "requests": []}
        frame = m.harvest(fake_get, audit)
        self.assertEqual(len(called), 2)
        self.assertEqual(len(frame), 2)
        self.assertEqual(len(audit["queries"]), 1)
        self.assertEqual(audit["queries"][0]["status"], "complete")
        self.assertEqual([x[0] for x in m.specifications()], ["epmc"])
        with self.assertRaises(m.RetrievalError):
            paginate("openalex", [oa_page(0, [])])
        with self.assertRaises(ValueError):
            m.query_url("openalex", {})

    def test_partial_pages_retained_in_failed_audit(self):
        audit = {"queries": [], "requests": []}
        pages = iter([epmc_page(2, [epmc_item()], "next")])
        def fake_get(url, log):
            try:
                return next(pages)
            except StopIteration:
                raise m.RetrievalError("synthetic later-page 503 exhausted")
        with self.assertRaises(m.RetrievalError):
            m.harvest(fake_get, audit)
        self.assertEqual(audit["queries"][0]["received"], 1)
        self.assertEqual(len(audit["queries"][0]["records"]), 1)
        self.assertEqual(audit["queries"][0]["status"], "incomplete")


class FakeRequest:
    def __init__(self, url, headers):
        self.full_url, self.headers = url, headers


class FakeResponse:
    def __init__(self, payload):
        self.status = 200
        self.raw = json.dumps(payload).encode("utf-8") if isinstance(payload, dict) else payload

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self):
        return self.raw


def fake_http_error(code):
    return HTTPError("https://synthetic.invalid/", code, "SYNTHETIC - not data", {}, None)


@contextlib.contextmanager
def synthetic_http(responses):
    # No urllib.request import or socket access, even on nodes without SSL DLLs.
    events, sleeps, iterator = [], [], iter(responses)
    fake_module = types.ModuleType("urllib.request")
    fake_module.Request = FakeRequest
    def opener(request, timeout):
        events.append((request.full_url, timeout))
        value = next(iterator)
        if isinstance(value, Exception):
            raise value
        return FakeResponse(value)
    fake_module.urlopen = opener
    with patch.dict(sys.modules, {"urllib.request": fake_module}), patch.object(m.time, "sleep", side_effect=sleeps.append):
        yield events, sleeps


class RetryTests(unittest.TestCase):
    def test_epmc_503_recovers_same_url_and_logs_each_attempt(self):
        audit = {"requests": []}
        url = m.query_url("epmc", {"query": "SYNTHETIC - not data"})
        with synthetic_http([fake_http_error(503), fake_http_error(502), epmc_page(0, [])]) as (events, sleeps):
            obj = m.get_json(url, audit)
        self.assertEqual(obj["hitCount"], 0)
        self.assertEqual(sleeps, [1, 2])
        self.assertEqual(events, [(url, 45)] * 3)
        self.assertEqual([r["attempt"] for r in audit["requests"]], [1, 2, 3])
        self.assertEqual([r["http_status"] for r in audit["requests"]], [503, 502, 200])
        self.assertIn("response_sha256", audit["requests"][-1])

    def test_5xx_retries_are_bounded(self):
        audit = {"requests": []}
        with synthetic_http([fake_http_error(503) for _ in range(5)]) as (events, sleeps):
            with self.assertRaisesRegex(m.RetrievalError, "HTTP 503"):
                m.get_json(m.EUROPE_PMC, audit)
        self.assertEqual(len(events), 5)
        self.assertEqual(sleeps, [1, 2, 4, 8])
        self.assertEqual(audit["requests"][-1]["status"], "5xx_retries_exhausted")

    def test_auth_bot_rate_limit_and_other_4xx_never_retry(self):
        for code in [400, 401, 403, 404, 429]:
            with self.subTest(code=code):
                audit = {"requests": []}
                with synthetic_http([fake_http_error(code)]) as (events, sleeps):
                    with self.assertRaises(m.RetrievalError):
                        m.get_json(m.EUROPE_PMC, audit)
                self.assertEqual(len(events), 1)
                self.assertEqual(sleeps, [])
                if code in (401, 403, 429):
                    self.assertEqual(audit["requests"][0]["status"], "blocked")

    def test_openalex_5xx_does_not_gain_epmc_retry_policy(self):
        audit = {"requests": []}
        with synthetic_http([fake_http_error(503)]) as (events, sleeps):
            with self.assertRaises(m.RetrievalError):
                m.get_json(m.openalex_cites_url("W999900", 1), audit)
        self.assertEqual(len(events), 1)
        self.assertEqual(sleeps, [])

    def test_non_json_schema_and_transport_failures_never_retry(self):
        for value in [b"<html>SYNTHETIC bot check</html>", b"[]",
                      URLError("synthetic failure"), TimeoutError("synthetic timeout")]:
            with self.subTest(value=str(value)):
                audit = {"requests": []}
                with synthetic_http([value]) as (events, sleeps):
                    with self.assertRaises(m.RetrievalError):
                        m.get_json(m.EUROPE_PMC, audit)
                self.assertEqual(len(events), 1)
                self.assertEqual(sleeps, [])

    def test_later_cursor_page_retries_without_duplicating_first_page(self):
        responses = [epmc_page(2, [epmc_item()], "synthetic-next"),
                     fake_http_error(503), epmc_page(2, [epmc_item("b")])]
        audit = {"queries": [], "requests": []}
        with synthetic_http(responses) as (events, sleeps):
            frame = m.harvest(m.get_json, audit)
        self.assertEqual(len(frame), 2)
        self.assertEqual(events[1], events[2])
        self.assertNotEqual(events[0], events[1])
        self.assertEqual(sleeps, [1])


class OpenAlexNoveltyTests(unittest.TestCase):
    def retrieve(self, pages):
        urls, iterator = [], iter(pages)
        def fake_get(url, audit):
            urls.append(url)
            value = next(iterator)
            if isinstance(value, Exception):
                raise value
            return value
        audit = {"requests": []}
        summary = m.retrieve_openalex_citations("W999900", fake_get, audit)
        return summary, urls, audit

    def test_numbered_pages_continue_after_short_page_until_empty(self):
        summary, urls, audit = self.retrieve([
            oa_page(2, [oa_item("a")]), oa_page(2, [oa_item("b")]), oa_page(2, [])])
        self.assertEqual(summary["status"], "complete")
        self.assertEqual(summary["received"], 2)
        self.assertTrue(summary["empty_terminal_page"])
        for page, url in enumerate(urls, 1):
            params = parse_qs(urlsplit(url).query)
            self.assertEqual(params, {"filter": ["cites:W999900"],
                                     "per-page": ["100"], "page": [str(page)]})
        self.assertNotIn("metadata_records", audit)

    def test_zero_requires_successful_empty_response(self):
        summary, urls, _ = self.retrieve([oa_page(0, [])])
        self.assertEqual(summary["status"], "complete")
        self.assertEqual(summary["received"], 0)
        failed, _, _ = self.retrieve([m.RetrievalError("synthetic 401")])
        self.assertEqual(failed["status"], "incomplete")
        self.assertIsNone(failed["reported_count"])
        self.assertEqual(failed["reason"], "retrieval_failed")

    def test_citation_cap_and_exact_cap_do_not_claim_empty_termination(self):
        for count in [10000, 10001]:
            with self.subTest(count=count):
                pages = [oa_page(count, [oa_item(str(p * 100 + j)) for j in range(100)])
                         for p in range(100)]
                summary, urls, _ = self.retrieve(pages)
                self.assertEqual(len(urls), 100)
                self.assertEqual(summary["received"], 10000)
                self.assertEqual(summary["status"], "incomplete")
                self.assertFalse(summary["empty_terminal_page"])
                self.assertEqual(summary["reason"], "reported_count_exceeds_10000" if count > 10000
                                 else "page_cap_without_empty_terminal_page")

    def test_9900_can_observe_empty_page_100(self):
        pages = [oa_page(9900, [oa_item(str(p * 100 + j)) for j in range(100)])
                 for p in range(99)] + [oa_page(9900, [])]
        summary, urls, _ = self.retrieve(pages)
        self.assertEqual(summary["status"], "complete")
        self.assertEqual(len(urls), 100)

    def test_mismatch_duplicate_and_changing_totals_are_incomplete(self):
        for pages in [
            [oa_page(2, [oa_item()]), oa_page(2, [])],
            [oa_page(2, [oa_item()]), oa_page(2, [oa_item()])],
            [oa_page(2, [oa_item()]), oa_page(3, [oa_item("b")])],
            [oa_page(0, [oa_item()])],
            [oa_page(True, [])], [oa_page(1, "invalid")], [{}],
            [oa_page(1, [{"title": "SYNTHETIC - not data"}])],
        ]:
            summary, _, _ = self.retrieve(pages)
            self.assertEqual(summary["status"], "incomplete")

    def test_later_failure_preserves_partial_bibliography(self):
        summary, _, _ = self.retrieve([oa_page(2, [oa_item()]),
                                       m.RetrievalError("synthetic 401")])
        self.assertEqual(summary["status"], "incomplete")
        self.assertEqual(summary["received"], 1)
        self.assertEqual(len(summary["records"]), 1)
        self.assertEqual(summary["reported_count"], 2)

    def test_work_id_and_page_validation(self):
        for wid in ["", "W1&cursor=*", "https://openalex.org/W1", "synthetic"]:
            with self.assertRaises(ValueError):
                m.openalex_cites_url(wid, 1)
        for page in [0, 101, True, "2"]:
            with self.assertRaises(ValueError):
                m.openalex_cites_url("W999900", page)


class HandoffTests(unittest.TestCase):
    def test_offline_query_display_never_fetches(self):
        with patch.object(m, "get_json", side_effect=AssertionError("Network forbidden")), \
             contextlib.redirect_stdout(io.StringIO()) as capture:
            self.assertEqual(m.main(["--print-queries"]), 0)
        self.assertIn("OPEN_ACCESS", capture.getvalue())
        self.assertEqual(capture.getvalue().count("https://"), 1)

    def test_missing_release_stops_before_network(self):
        with patch.object(m, "get_json", side_effect=AssertionError("Network forbidden")), \
             contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as caught:
                m.main([])
        self.assertEqual(caught.exception.code, 2)

    def test_output_path_cannot_escape_out(self):
        with self.assertRaisesRegex(ValueError, "Output directory"):
            m.resolve_outputs(str(BASE.parent))

    def test_prior_frame_or_audit_not_overwritten(self):
        with patch.object(Path, "exists", return_value=True):
            with self.assertRaisesRegex(ValueError, "overwrite"):
                m.resolve_outputs(str(BASE))

    def test_synthetic_release_hash_guard(self):
        args = types.SimpleNamespace(
            screen_release_url="https://github.com/mahmood726-cyber/usecase-preregistrations/releases/tag/SYNTHETIC",
            screen_release_doi="https://doi.org/10.9999/synthetic-release",
            prereg_sha256="0" * 64, script_sha256="0" * 64)
        with self.assertRaisesRegex(ValueError, "do not match"):
            m.check_release(args)

    def test_incomplete_fetch_writes_audit_only_in_memory(self):
        frame, audit = MemoryPath("synthetic_frame"), MemoryPath("synthetic_audit")
        with patch.object(m, "check_release", return_value={"data_status": "SYNTHETIC - not data"}), \
             patch.object(m, "resolve_outputs", return_value=(frame, audit)), \
             patch.object(m, "get_json", side_effect=m.RetrievalError("synthetic blocked")), \
             contextlib.redirect_stderr(io.StringIO()):
            code = m.main([])
        self.assertEqual(code, 2)
        self.assertEqual(frame.opens, 0)
        self.assertEqual(audit.opens, 1)
        obj = json.loads(audit.buffer.getvalue())
        self.assertEqual(obj["status"], "failed_blocked")
        self.assertEqual(obj["screen_status"], "FAILED_BLOCKED")
        self.assertIsNone(obj["frame_count"])
        self.assertFalse(obj["retrieval_complete"])

    def test_success_emits_unscreened_frame_and_hash_in_memory(self):
        frame, audit = MemoryPath("synthetic_frame"), MemoryPath("synthetic_audit")
        def fake_get(url, audit):
            return epmc_page(1, [epmc_item()]) if "europepmc" in url else oa_page(1, [oa_item()])
        with patch.object(m, "check_release", return_value={"data_status": "SYNTHETIC - not data"}), \
             patch.object(m, "resolve_outputs", return_value=(frame, audit)), \
             patch.object(m, "get_json", side_effect=fake_get), \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(m.main([]), 0)
        payload = frame.buffer.getvalue()
        self.assertEqual(json.loads(payload)["screen_status"], "UNSCREENED")
        obj = json.loads(audit.buffer.getvalue())
        self.assertEqual(obj["status"], "complete")
        self.assertEqual(obj["frame_sha256"], hashlib.sha256(payload.encode()).hexdigest())

    def test_exhausted_503_never_writes_a_zero_frame(self):
        frame, audit = MemoryPath("synthetic_frame"), MemoryPath("synthetic_audit")
        with patch.object(m, "check_release", return_value={"data_status": "SYNTHETIC - not data"}), \
             patch.object(m, "resolve_outputs", return_value=(frame, audit)), \
             synthetic_http([fake_http_error(503) for _ in range(5)]), \
             contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(m.main([]), 2)
        obj = json.loads(audit.buffer.getvalue())
        self.assertEqual(obj["status"], "failed_blocked")
        self.assertIsNone(obj["frame_count"])
        self.assertEqual(len(obj["requests"]), 5)
        self.assertEqual(frame.opens, 0)

    def test_verified_empty_discovery_is_distinct_from_failure(self):
        frame, audit = MemoryPath("synthetic_frame"), MemoryPath("synthetic_audit")
        with patch.object(m, "check_release", return_value={"data_status": "SYNTHETIC - not data"}), \
             patch.object(m, "resolve_outputs", return_value=(frame, audit)), \
             patch.object(m, "get_json", return_value=epmc_page(0, [])), \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(m.main([]), 0)
        obj = json.loads(audit.buffer.getvalue())
        self.assertEqual(obj["status"], "complete")
        self.assertEqual(obj["frame_count"], 0)
        self.assertEqual(frame.opens, 1)
        self.assertEqual(frame.buffer.getvalue(), "")

    def test_novelty_mode_does_not_build_a_frame(self):
        audit = MemoryPath("synthetic_novelty_audit")
        with patch.object(m, "check_release", return_value={"data_status": "SYNTHETIC - not data"}), \
             patch.object(m, "novelty_output", return_value=audit), \
             patch.object(m, "harvest", side_effect=AssertionError("No discovery allowed")), \
             patch.object(m, "resolve_outputs", side_effect=AssertionError("No frame allowed")), \
             patch.object(m, "get_json", return_value=oa_page(0, [])), \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(m.main(["--openalex-cites", "W999900"]), 0)
        obj = json.loads(audit.buffer.getvalue())
        self.assertEqual(obj["purpose"], "candidate_novelty_only")
        self.assertEqual(obj["novelty_queries"][0]["status"], "complete")

    def test_novelty_failure_is_recorded_and_nonzero(self):
        audit = MemoryPath("synthetic_novelty_audit")
        with patch.object(m, "check_release", return_value={"data_status": "SYNTHETIC - not data"}), \
             patch.object(m, "novelty_output", return_value=audit), \
             patch.object(m, "get_json", side_effect=m.RetrievalError("synthetic blocked")), \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(m.main(["--openalex-cites", "W999900"]), 2)
        obj = json.loads(audit.buffer.getvalue())
        self.assertEqual(obj["status"], "incomplete")
        self.assertIsNone(obj["novelty_queries"][0]["reported_count"])

    def test_novelty_missing_release_stops_before_network(self):
        with patch.object(m, "get_json", side_effect=AssertionError("Network forbidden")), \
             contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                m.main(["--openalex-cites", "W999900"])

    def test_novelty_output_guards(self):
        with self.assertRaises(ValueError):
            m.novelty_output(str(BASE.parent), "W999900")
        with patch.object(Path, "exists", return_value=True):
            with self.assertRaisesRegex(ValueError, "overwrite"):
                m.novelty_output(str(BASE), "W999900")

    def test_mixed_cli_modes_are_rejected(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                m.main(["--print-queries", "--openalex-cites", "W999900"])


class PreservedSpecificationTests(unittest.TestCase):
    def test_selection_gates_and_rules_unchanged(self):
        current = (BASE / "PREREG_P04_screen.md").read_text(encoding="utf-8")
        # Frozen hashes of unchanged sections in the supplied prior registration.
        # Configuration assertions only; no candidate data or external package needed.
        expected_sections = [
    [
        "### G1.",
        "### G3.",
        "5794d7a30a7c81917842a43c5c522717cee69ead96031c13919c75e7f35e76e7"
    ],
    [
        "**Same equivalence definition as v3:**",
        "### G4.",
        "8fa60485b087bce862380f3d48def51ad367c68c6281ed8bdb8de769fe3bed9d"
    ],
    [
        "### G4.",
        "## 6.",
        "0aea6c9bf7d0d3247bf3f32038c1ce883b4fbc4c1021d96b5db096eddf446de3"
    ],
    [
        "Before reading numerical result cells",
        "## 4.",
        "4004a06a1ed9b5fd44912a19b67cda10f6cb88092a454d2c4197c96c5961696e"
    ],
    [
        "F5 carries forward",
        "Static scope evidence",
        "49af1fd77937f14e9313738201ba1760d4bd19d397378ebfbebb928f0752da99"
    ]
]
        for first, last, expected_hash in expected_sections:
            section = current[current.index(first):current.index(last)]
            self.assertEqual(hashlib.sha256(section.encode("utf-8")).hexdigest(), expected_hash)
        self.assertEqual(m.SEED, "2026102804")
        self.assertEqual(m.START, "2016-10-28")
        self.assertEqual(m.END, "2026-10-28")
        expected = {
            "10.1111/dom.15725", "10.1186/s12933-023-02035-8",
            "10.1007/s00125-024-06144-1", "10.1136/bmj-2023-076410",
            "10.1111/1753-0407.70192",
        }
        self.assertEqual(m.EXCLUDED_DOIS, expected)
        # Frozen hash of the prior EPMC_QUERY literal, unchanged by this amendment.
        self.assertEqual(hashlib.sha256(m.EPMC_QUERY.encode("utf-8")).hexdigest(),
                         "09825e8d48586ab80abc3a5c228815b2648b0ba4e565a2a91f811a4411e8d7e8")

    def test_printed_discovery_url_matches_script_and_excludes_openalex_search(self):
        text = (BASE / "PREREG_P04_screen.md").read_text(encoding="utf-8")
        section = text[text.index("## 2."):text.index("## 3.")]
        for provider, _, params in m.specifications():
            self.assertIn(m.query_url(provider, params), section)
        self.assertNotIn("https://api.openalex.org/works?search=", text)


if __name__ == "__main__":
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__])
    )
    report = [
        "SYNTHETIC - not data",
        "",
        "# Offline amended frame-builder and novelty-helper validation",
        "",
        f"Tests run: {result.testsRun}; failures: {len(result.failures)}; errors: {len(result.errors)}.",
        "API responses and hypothetical candidate metadata are SYNTHETIC - not data.",
        "Real exclusion DOIs and frozen query strings are checked only as unchanged configuration.",
        "No live API, candidate screening or statistical engine ran; a socket audit hook forbids network access.",
        "Fake output streams stayed in memory; no real frame_P04.jsonl was generated.",
        "This validates Europe PMC-only discovery, bounded 5xx retries, failure/zero separation, page-based",
        "OpenAlex novelty limits, metadata ordering and preserved rules. It does not validate live API availability, query semantics,",
        "a public release, candidate feasibility/novelty, or app/R parity.",
        "",
        "~~~text",
        stream.getvalue().strip(),
        "~~~",
        "",
        "## Files to freeze (SHA-256 of current local bytes)",
        "",
    ]
    for name in ["PREREG_P04_screen.md", "screen_P04.py", "synthetic_test_screen_P04.py", "BLOCKERS_P04_screen.md"]:
        digest = hashlib.sha256((BASE / name).read_bytes()).hexdigest()
        report.append(f"- {name}: {digest}")
    report.append("")
    (BASE / "synthetic_validation_P04_screen.md").write_text(
        "\n".join(report), encoding="utf-8", newline="\n"
    )
    print(stream.getvalue())
    raise SystemExit(0 if result.wasSuccessful() else 1)
