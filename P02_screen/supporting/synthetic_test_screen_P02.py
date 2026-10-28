# SYNTHETIC - not data
"""Offline checks on fabricated bibliographic metadata, never candidate data."""
import contextlib
import datetime as dt
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import unittest
from unittest import mock
import urllib.error
import urllib.parse

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("synthetic_screen_module", ROOT / "screen_P02.py")
screen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(screen)
LABEL = "SYNTHETIC - not data"


def synthetic_record(suffix, date="2020-01-02", oa=True, **extra):
    value = {"fixture_label": LABEL, "source": "synthetic", "query_id": "synthetic",
             "record_id": "synthetic_" + suffix, "doi_raw": "10.9999/synthetic_" + suffix,
             "title": LABEL, "publication_date": date, "is_oa": oa,
             "is_retracted": False}
    value.update(extra)
    return value


def synthetic_epmc(identifier):
    return {"fixture_label": LABEL, "source": "SYNTHETIC", "id": identifier,
            "title": LABEL, "doi": "10.9999/synthetic_" + identifier,
            "firstPublicationDate": "2020-01-02", "isOpenAccess": "Y"}


def synthetic_oa(identifier):
    return {"fixture_label": LABEL, "id": "https://openalex.org/W" + str(identifier),
            "title": LABEL, "doi": "https://doi.org/10.9999/synthetic_" + str(identifier),
            "publication_date": "2020-01-02", "cited_by_count": 123}


def synthetic_response(data):
    response = mock.MagicMock()
    response.__enter__.return_value = response
    response.status = 200
    response.geturl.return_value = "https://example.invalid"
    response.headers = {"Content-Type": "application/json"}
    response.read.return_value = json.dumps(data).encode()
    return response


def synthetic_http_error(status, body=LABEL):
    return urllib.error.HTTPError("https://example.invalid", status, LABEL, {},
                                  io.BytesIO(body.encode()))


@contextlib.contextmanager
def synthetic_filesystem():
    """Entirely in-memory output capture, including manifests and failure logs."""
    files = {}
    @contextlib.contextmanager
    def open_file(path, mode="r", **kwargs):
        key = str(path)
        if mode == "x" and key in files:
            raise FileExistsError(key)
        stream = io.StringIO(files.get(key, ""))
        try:
            yield stream
        finally:
            if mode in ("x", "w"):
                files[key] = stream.getvalue()
    with mock.patch.object(Path, "open", open_file), \
         mock.patch.object(Path, "mkdir"), \
         mock.patch.object(Path, "exists", lambda path: str(path) in files), \
         mock.patch.object(Path, "read_bytes", lambda path: files[str(path)].encode()):
        yield files


def synthetic_fetch_pages(pages):
    synthetic_iterator = iter(pages)
    def fetch(url):
        return next(synthetic_iterator), {"fixture_label": LABEL, "http_status": 200}
    return fetch


class SyntheticChecks(unittest.TestCase):
    def setUp(self):
        self.synthetic_network_guard = mock.patch.object(
            screen.urllib.request, "urlopen", side_effect=AssertionError("Live network forbidden"))
        self.synthetic_network_guard.start()
        self.addCleanup(self.synthetic_network_guard.stop)

    def test_doi_normalization_and_valid_suffix_punctuation(self):
        self.assertEqual(screen.normalize_doi(" HTTPS://DX.DOI.ORG/10.9999/SYNTHETIC%28A%29 "),
                         "10.9999/synthetic(a)")
        self.assertEqual(screen.normalize_doi("doi: 10.9999/synthetic."), "10.9999/synthetic.")
        for value in (None, "", "no-doi", "10.9999/has space"):
            self.assertIsNone(screen.normalize_doi(value))

    def test_seed_hash_independent_oracle_and_order_invariance(self):
        synthetic_records = [synthetic_record(str(i)) for i in range(9)]
        synthetic_frame, _ = screen.make_frame(synthetic_records)
        synthetic_expected = sorted(
            [row["doi_raw"] for row in synthetic_records],
            key=lambda doi: (hashlib.sha256(("2026102802|P02|screen|" + doi).encode()).hexdigest(), doi))
        self.assertEqual([row["doi"] for row in synthetic_frame], synthetic_expected)
        self.assertEqual(screen.make_frame(list(reversed(synthetic_records)))[0], synthetic_frame)
        self.assertEqual(len(synthetic_frame), 9)
        self.assertEqual(sum(row["within_five_screen_limit"] for row in synthetic_frame), 5)
        self.assertTrue(all(row["screen_status"] == "NOT_SCREENED" for row in synthetic_frame))

    def test_deduplication_retains_provenance_and_date_conflict(self):
        synthetic_a = synthetic_record("a")
        synthetic_b = dict(synthetic_a, source="other", query_id="other",
                           doi_raw="https://doi.org/10.9999/SYNTHETIC_A",
                           publication_date="2021-01-02")
        synthetic_frame, synthetic_excluded = screen.make_frame([synthetic_b, synthetic_a, synthetic_a])
        self.assertEqual(len(synthetic_frame), 1)
        self.assertEqual(len(synthetic_frame[0]["metadata"]), 2)
        self.assertEqual(synthetic_frame[0]["publication_date"], "2020-01-02")
        self.assertTrue(synthetic_frame[0]["date_conflict"])
        self.assertFalse(synthetic_excluded)

    def test_all_five_previous_dois_excluded_case_insensitively(self):
        synthetic_records = [synthetic_record(str(i), doi_raw="https://doi.org/" + doi.upper())
                             for i, doi in enumerate(sorted(screen.EXCLUDED))]
        synthetic_frame, synthetic_excluded = screen.make_frame(synthetic_records)
        self.assertFalse(synthetic_frame)
        self.assertEqual(len(synthetic_excluded), 5)
        self.assertEqual({row["reason"] for row in synthetic_excluded}, {"previously_screened"})

    def test_dates_oa_retraction_and_missing_doi(self):
        synthetic_records = [
            synthetic_record("start", date="2016-10-28"),
            synthetic_record("end", date="2026-10-28"),
            synthetic_record("early", date="2016-10-27"),
            synthetic_record("late", date="2026-10-29"),
            synthetic_record("partial", date="2020"),
            synthetic_record("invalid", date="2020-02-31"),
            synthetic_record("closed", oa=False),
            synthetic_record("retracted", is_retracted=True),
            synthetic_record("nodoi", doi_raw=None),
        ]
        synthetic_frame, synthetic_excluded = screen.make_frame(synthetic_records)
        self.assertEqual({row["doi"] for row in synthetic_frame},
                         {"10.9999/synthetic_start", "10.9999/synthetic_end"})
        self.assertEqual(len(synthetic_excluded), 7)
        # Conflicting later metadata must not rescue an earlier out-of-window date.
        synthetic_pair = [synthetic_record("conflict", date="2016-10-27"),
                          synthetic_record("conflict", date="2016-10-28", source="other")]
        self.assertFalse(screen.make_frame(synthetic_pair)[0])

    def test_epmc_multi_page_complete(self):
        synthetic_pages = [
            {"hitCount": 2, "resultList": {"result": [synthetic_epmc("a")]}, "nextCursorMark": "NEXT"},
            {"hitCount": 2, "resultList": {"result": [synthetic_epmc("b")]}, "nextCursorMark": "NEXT"},
        ]
        synthetic_log = []
        synthetic_rows, synthetic_report = screen.harvest(
            "synthetic_epmc", "europe_pmc", screen.EPMC_QUERY,
            synthetic_fetch_pages(synthetic_pages), synthetic_log.append, pace=False)
        self.assertEqual(len(synthetic_rows), 2)
        self.assertEqual(synthetic_report["pages"], 2)
        self.assertTrue(synthetic_report["complete"])
        self.assertIn("cursorMark=NEXT", synthetic_log[1]["url"])

    def test_epmc_complete_zero_and_invalid_pagination(self):
        synthetic_rows, synthetic_report = screen.harvest(
            "synthetic_zero", "europe_pmc", screen.EPMC_QUERY,
            synthetic_fetch_pages([{"hitCount": 0, "resultList": {"result": []}}]),
            lambda event: None, pace=False)
        self.assertEqual(synthetic_rows, [])
        self.assertTrue(synthetic_report["complete"])
        synthetic_cases = [
            [{"hitCount": 2, "resultList": {"result": [synthetic_epmc("a")]}}],
            [{"hitCount": 2, "resultList": {"result": [synthetic_epmc("a")]}, "nextCursorMark": "*"}],
            [{"hitCount": 2, "resultList": {"result": [synthetic_epmc("a")]}, "nextCursorMark": "NEXT"},
             {"hitCount": 3, "resultList": {"result": [synthetic_epmc("b")]}}],
            [{"hitCount": 2, "resultList": {"result": [synthetic_epmc("a")]}, "nextCursorMark": "NEXT"},
             {"hitCount": 2, "resultList": {"result": [synthetic_epmc("a")]}}],
            [{"hitCount": 2, "resultList": {"result": []}}],
            [{"hitCount": True, "resultList": {"result": []}}],
            [{"hitCount": 0, "resultList": {"result": [synthetic_epmc("a")]}}],
            [{"error": LABEL}],
            [{"hitCount": 1, "resultList": []}],
        ]
        for synthetic_pages in synthetic_cases:
            with self.subTest(pages=synthetic_pages):
                synthetic_log = []
                with self.assertRaises(screen.FrameError):
                    screen.harvest("synthetic_failure", "europe_pmc", screen.EPMC_QUERY,
                                   synthetic_fetch_pages(synthetic_pages), synthetic_log.append, pace=False)
                self.assertEqual(synthetic_log[-1]["event"], "query_failure")
                self.assertEqual(synthetic_log[-1]["status"], "FAILED_BLOCKED")

    def test_projection_omits_abstracts_and_nonbibliographic_payloads(self):
        synthetic_raw = synthetic_epmc("a")
        synthetic_raw["abstractText"] = LABEL
        synthetic_raw["unwanted_table"] = LABEL
        synthetic_projected = screen.project_record("europe_pmc", "synthetic", synthetic_raw)
        self.assertNotIn("abstractText", synthetic_projected)
        self.assertNotIn("unwanted_table", synthetic_projected)

    def test_exact_frozen_query_parameters(self):
        synthetic_ep = urllib.parse.parse_qs(urllib.parse.urlsplit(
            screen.request_url("europe_pmc", screen.EPMC_QUERY)).query)
        self.assertEqual(synthetic_ep["query"], [screen.EPMC_QUERY])
        self.assertEqual(synthetic_ep["cursorMark"], ["*"])
        self.assertEqual(synthetic_ep["resultType"], ["lite"])
        self.assertEqual(screen.QUERIES, (("EPMC-1", "europe_pmc", screen.EPMC_QUERY),))
        with self.assertRaises(ValueError):
            screen.request_url("openalex", "synthetic")
        with self.assertRaises(screen.FrameError):
            screen.harvest("synthetic", "openalex", "synthetic",
                           mock.Mock(), mock.Mock(), pace=False)
        with self.assertRaises(screen.FrameError):
            screen.project_record("openalex", "synthetic", synthetic_oa(1))

    def test_cli_is_offline_by_default_and_query_printing_is_offline(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as caught:
            screen.main([])
        self.assertEqual(caught.exception.code, 2)
        synthetic_stdout = io.StringIO()
        with contextlib.redirect_stdout(synthetic_stdout):
            self.assertEqual(screen.main(["--print-queries"]), 0)
        self.assertEqual(len(synthetic_stdout.getvalue().splitlines()), 1)
        self.assertNotIn("openalex", synthetic_stdout.getvalue())

    def test_http_forbidden_and_html_are_failures(self):
        synthetic_error = urllib.error.HTTPError("https://example.invalid", 403,
                                                 LABEL, {}, None)
        with mock.patch.object(screen.urllib.request, "urlopen", side_effect=synthetic_error):
            with self.assertRaisesRegex(screen.FrameError, "HTTP 403"):
                screen.fetch_json("https://example.invalid")
        synthetic_response = mock.MagicMock()
        synthetic_response.__enter__.return_value = synthetic_response
        synthetic_response.status = 200
        synthetic_response.geturl.return_value = "https://example.invalid"
        synthetic_response.headers = {"Content-Type": "text/html"}
        synthetic_response.read.return_value = b"SYNTHETIC - not data"
        with mock.patch.object(screen.urllib.request, "urlopen", return_value=synthetic_response):
            with self.assertRaisesRegex(screen.FrameError, "non-JSON"):
                screen.fetch_json("https://example.invalid")

    def test_release_hash_mismatch_stops(self):
        synthetic_receipt = {"fixture_label": LABEL, "script_sha256": "bad"}
        with mock.patch.object(Path, "read_text", return_value=json.dumps(synthetic_receipt)):
            with self.assertRaisesRegex(screen.FrameError, "script_sha256"):
                screen.check_release("synthetic_receipt.json")

    def test_jsonl_output_round_trip_in_memory(self):
        synthetic_rows = [{"fixture_label": LABEL, "title": "synthetic unicode \u03b1"},
                          {"fixture_label": LABEL, "screen_status": "NOT_SCREENED"}]
        synthetic_buffer = io.StringIO()
        synthetic_path = mock.Mock()
        synthetic_path.open.return_value = contextlib.nullcontext(synthetic_buffer)
        screen.write_jsonl(synthetic_path, synthetic_rows)
        self.assertEqual([json.loads(line) for line in synthetic_buffer.getvalue().splitlines()],
                         synthetic_rows)
        self.assertTrue(synthetic_buffer.getvalue().endswith("\n"))
        self.assertEqual(synthetic_path.open.call_args.args[0], "x")

    def test_output_root_restriction_before_writes(self):
        with self.assertRaisesRegex(screen.FrameError, "under"):
            screen.execute(ROOT.parent, {"fixture_label": LABEL})

    def test_document_urls_exclusions_and_verification_are_synchronized(self):
        synthetic_document = (ROOT / "PREREG_P02_screen.md").read_text(encoding="utf-8")
        for _, synthetic_source, synthetic_query in screen.QUERIES:
            self.assertIn(screen.request_url(synthetic_source, synthetic_query), synthetic_document)
        for synthetic_doi in screen.EXCLUDED:
            self.assertIn(synthetic_doi, synthetic_document)
        self.assertIn("2026102802|P02|screen|<doi>", synthetic_document)
        synthetic_decisions = (ROOT.parent / "MAHMOOD_DECISIONS.md").read_text(encoding="utf-8")
        synthetic_verification = next(line[3:] for line in synthetic_decisions.splitlines()
                                      if line.startswith("4. Human verification:"))
        self.assertIn(synthetic_verification, synthetic_document)


    def test_5xx_retry_backoff_and_success_receipt(self):
        synthetic_payload = {"fixture_label": LABEL, "hitCount": 0, "resultList": {"result": []}}
        synthetic_failures = [synthetic_http_error(code) for code in (500, 502, 503, 504)]
        with mock.patch.object(screen.urllib.request, "urlopen",
                               side_effect=synthetic_failures + [synthetic_response(synthetic_payload)]) as call, \
             mock.patch.object(screen.time, "sleep") as sleep:
            synthetic_data, synthetic_receipt = screen.fetch_json("https://example.invalid")
        self.assertEqual(synthetic_data, synthetic_payload)
        self.assertEqual(call.call_count, 5)
        self.assertEqual([x.args[0] for x in sleep.call_args_list], [1, 2, 4, 8])
        self.assertEqual([x["http_status"] for x in synthetic_receipt["attempts"]],
                         [500, 502, 503, 504, 200])
        self.assertEqual(len({x.args[0].full_url for x in call.call_args_list}), 1)

    def test_5xx_exhaustion_is_bounded_and_logged(self):
        with mock.patch.object(screen.urllib.request, "urlopen",
                               side_effect=[synthetic_http_error(503) for _ in range(5)]) as call, \
             mock.patch.object(screen.time, "sleep") as sleep:
            with self.assertRaisesRegex(screen.FrameError, "not zero") as caught:
                screen.fetch_json("https://example.invalid")
        self.assertEqual(call.call_count, 5)
        self.assertEqual(len(caught.exception.attempts), 5)
        self.assertEqual([x.args[0] for x in sleep.call_args_list], [1, 2, 4, 8])

    def test_access_errors_challenges_and_transport_never_retry(self):
        for synthetic_error in [synthetic_http_error(401), synthetic_http_error(403),
                                synthetic_http_error(429),
                                synthetic_http_error(503, LABEL + " captcha"),
                                urllib.error.URLError(LABEL)]:
            with self.subTest(error=str(synthetic_error)):
                with mock.patch.object(screen.urllib.request, "urlopen",
                                       side_effect=synthetic_error) as call, \
                     mock.patch.object(screen.time, "sleep") as sleep:
                    with self.assertRaises(screen.FrameError):
                        screen.fetch_json("https://example.invalid")
                self.assertEqual(call.call_count, 1)
                sleep.assert_not_called()

    def test_discovery_execute_only_epmc_and_complete_output(self):
        synthetic_urls = []
        def fetch(url):
            synthetic_urls.append(url)
            return {"hitCount": 1, "resultList": {"result": [synthetic_epmc("a")]}}, {"fixture_label": LABEL}
        synthetic_dir = ROOT / "synthetic_run"
        with synthetic_filesystem() as files:
            synthetic_manifest = screen.execute(synthetic_dir, {"fixture_label": LABEL}, fetch, pace=False)
        self.assertEqual(synthetic_manifest["status"], "COMPLETE")
        self.assertEqual(synthetic_manifest["frame_count"], 1)
        self.assertEqual(len(synthetic_urls), 1)
        self.assertTrue(all(urllib.parse.urlsplit(url).hostname == "www.ebi.ac.uk"
                            for url in synthetic_urls))
        synthetic_frame = json.loads(files[str(synthetic_dir / "frame_P02.jsonl")])
        self.assertEqual(synthetic_frame["screen_status"], "NOT_SCREENED")
        self.assertEqual(synthetic_frame["doi"], "10.9999/synthetic_a")

    def test_discovery_failed_manifest_no_frame_and_no_zero(self):
        synthetic_dir = ROOT / "synthetic_failed"
        synthetic_calls = []
        def fetch(url):
            synthetic_calls.append(url)
            if len(synthetic_calls) == 1:
                return {"hitCount": 2, "resultList": {"result": [synthetic_epmc("a")]},
                        "nextCursorMark": "NEXT"}, {"fixture_label": LABEL}
            raise screen.FrameError("SYNTHETIC - not data; HTTP 503 exhausted",
                                    [{"fixture_label": LABEL, "http_status": 503}])
        with synthetic_filesystem() as files:
            with self.assertRaises(screen.FrameError):
                screen.execute(synthetic_dir, {"fixture_label": LABEL}, fetch, pace=False)
        synthetic_manifest = json.loads(files[str(synthetic_dir / "run_manifest_P02.json")])
        self.assertEqual(synthetic_manifest["status"], "FAILED_BLOCKED")
        self.assertNotIn("frame_count", synthetic_manifest)
        self.assertNotIn(str(synthetic_dir / "frame_P02.jsonl"), files)
        synthetic_log = [json.loads(line) for line in files[str(synthetic_dir / "query_log_P02.jsonl")].splitlines()]
        self.assertEqual(synthetic_log[-1]["retrieved_count"], 1)
        self.assertEqual(synthetic_log[-1]["reported_count"], 2)
        self.assertEqual(synthetic_log[-1]["attempts"][0]["http_status"], 503)

    def test_complete_zero_requires_successful_response(self):
        synthetic_dir = ROOT / "synthetic_zero"
        with synthetic_filesystem() as files:
            synthetic_manifest = screen.execute(
                synthetic_dir, {"fixture_label": LABEL},
                synthetic_fetch_pages([{"hitCount": 0, "resultList": {"result": []}}]), pace=False)
        self.assertEqual(synthetic_manifest["status"], "COMPLETE")
        self.assertEqual(synthetic_manifest["frame_count"], 0)
        self.assertEqual(files[str(synthetic_dir / "frame_P02.jsonl")], "")

    def test_openalex_novelty_pages_until_empty_without_discovery_filters(self):
        synthetic_log = []
        synthetic_rows, synthetic_report = screen.harvest_openalex_citations(
            "W999", synthetic_fetch_pages([
                {"meta": {"count": 2}, "results": [synthetic_oa(1)]},
                {"meta": {"count": 2}, "results": [synthetic_oa(2)]},
                {"meta": {"count": 2}, "results": []},
            ]), synthetic_log.append, pace=False)
        self.assertTrue(synthetic_report["complete"])
        self.assertTrue(synthetic_report["terminal_empty_page"])
        self.assertEqual(len(synthetic_rows), 2)
        self.assertEqual(synthetic_report["pages"], 3)
        for synthetic_page, synthetic_event in enumerate(synthetic_log, 1):
            synthetic_params = urllib.parse.parse_qs(urllib.parse.urlsplit(synthetic_event["url"]).query)
            self.assertEqual(synthetic_params, {"filter": ["cites:W999"], "per-page": ["100"],
                                                 "page": [str(synthetic_page)]})

    def test_openalex_novelty_empty_zero_is_complete(self):
        synthetic_rows, synthetic_report = screen.harvest_openalex_citations(
            "W999", synthetic_fetch_pages([{"meta": {"count": 0}, "results": []}]),
            lambda event: None, pace=False)
        self.assertEqual(synthetic_rows, [])
        self.assertTrue(synthetic_report["complete"])
        self.assertEqual(synthetic_report["reported_count"], 0)

    def test_openalex_limit_and_exact_boundary_are_explicitly_incomplete(self):
        for synthetic_count in (10000, 10001):
            synthetic_requested_pages = []
            def fetch(url):
                page = int(urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)["page"][0])
                synthetic_requested_pages.append(page)
                return {"meta": {"count": synthetic_count},
                        "results": [synthetic_oa(i) for i in range((page - 1) * 100 + 1, page * 100 + 1)]}, {"fixture_label": LABEL}
            synthetic_rows, synthetic_report = screen.harvest_openalex_citations(
                "W999", fetch, lambda event: None, pace=False)
            self.assertEqual(len(synthetic_rows), 10000)
            self.assertEqual(synthetic_requested_pages, list(range(1, 101)))
            self.assertFalse(synthetic_report["complete"])
            self.assertFalse(synthetic_report["terminal_empty_page"])
            self.assertEqual(synthetic_report["status"], "INCOMPLETE_LIMIT")
            self.assertEqual(synthetic_report["reported_count"], synthetic_count)

    def test_openalex_incomplete_partial_count_duplicate_schema_and_access(self):
        synthetic_first = {"meta": {"count": 2}, "results": [synthetic_oa(1)]}
        synthetic_cases = [
            [synthetic_first, {"meta": {"count": 2}, "results": []}],
            [synthetic_first, {"meta": {"count": 3}, "results": [synthetic_oa(2)]}],
            [synthetic_first, {"meta": {"count": 2}, "results": [synthetic_oa(1)]}],
            [synthetic_first, {"meta": {}, "results": []}],
            [synthetic_first, {"meta": {"count": True}, "results": []}],
        ]
        for synthetic_pages in synthetic_cases:
            synthetic_log = []
            synthetic_rows, synthetic_report = screen.harvest_openalex_citations(
                "W999", synthetic_fetch_pages(synthetic_pages), synthetic_log.append, pace=False)
            self.assertFalse(synthetic_report["complete"])
            self.assertEqual(synthetic_report["status"], "FAILED_BLOCKED")
            self.assertEqual(len(synthetic_rows), 1)
            self.assertEqual(synthetic_report["reported_count"], 2)
            self.assertEqual(synthetic_log[-1]["event"], "novelty_failure")
        synthetic_fetch = mock.Mock(side_effect=[
            (synthetic_first, {"fixture_label": LABEL}), screen.FrameError("HTTP 401; " + LABEL)])
        synthetic_rows, synthetic_report = screen.harvest_openalex_citations(
            "W999", synthetic_fetch, lambda event: None, pace=False)
        self.assertEqual(synthetic_report["status"], "FAILED_BLOCKED")
        self.assertEqual(synthetic_report["retrieved_count"], 1)
        self.assertEqual(len(synthetic_rows), 1)

    def test_openalex_novelty_output_keeps_lookup_profile_and_does_not_clear_gate(self):
        synthetic_dir = ROOT / "synthetic_novelty"
        synthetic_lookup = synthetic_oa(999)
        synthetic_lookup["abstract_inverted_index"] = {"synthetic": [1]}
        with synthetic_filesystem() as files:
            synthetic_report = screen.execute_openalex_novelty(
                synthetic_dir, {"fixture_label": LABEL}, "10.9999/synthetic_999",
                synthetic_fetch_pages([synthetic_lookup,
                                       {"meta": {"count": 0}, "results": []}]), pace=False)
        self.assertTrue(synthetic_report["complete"])
        self.assertEqual(synthetic_report["candidate_metadata"]["cited_by_count"], 123)
        self.assertFalse(synthetic_report["equivalence_assessed"])
        self.assertFalse(synthetic_report["novelty_cleared"])
        self.assertNotIn("abstract", files[str(synthetic_dir / "novelty_openalex_P02.jsonl")])
        self.assertFalse(any("frame_P02" in path for path in files))

    def test_openalex_lookup_failure_is_recorded_not_zero(self):
        synthetic_dir = ROOT / "synthetic_novelty_failed"
        with synthetic_filesystem() as files:
            synthetic_report = screen.execute_openalex_novelty(
                synthetic_dir, {"fixture_label": LABEL}, "10.9999/synthetic_999",
                mock.Mock(side_effect=screen.FrameError("HTTP 401; " + LABEL)), pace=False)
        self.assertFalse(synthetic_report["complete"])
        self.assertIsNone(synthetic_report["reported_count"])
        self.assertEqual(synthetic_report["status"], "FAILED_BLOCKED")
        self.assertIn(str(synthetic_dir / "novelty_openalex_P02.json"), files)

    def test_novelty_cli_requires_release_and_uses_separate_mode(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            screen.main(["--fetch", "--novelty-doi", "10.9999/synthetic_a"])
        with mock.patch.object(screen, "check_release", return_value={"fixture_label": LABEL}), \
             mock.patch.object(screen, "execute") as discovery, \
             mock.patch.object(screen, "execute_openalex_novelty",
                               return_value={"status": "INCOMPLETE_LIMIT", "complete": False}) as novelty, \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(screen.main(["--fetch", "--release-record", "synthetic_receipt.json",
                                          "--novelty-doi", "10.9999/synthetic_a"]), 1)
        discovery.assert_not_called()
        novelty.assert_called_once()

    def test_preserved_screening_rules_and_pre_freeze_amendment(self):
        synthetic_document = (ROOT / "PREREG_P02_screen.md").read_text(encoding="utf-8")
        synthetic_previous = (ROOT.parent / "S_P02_SCREENPREREG" / "out" /
                              "PREREG_P02_screen.md").read_text(encoding="utf-8")
        for start, end in [("## 3.", "## 4."), ("## 4.", "## 5."), ("## 6.", "## 7.")]:
            self.assertEqual(synthetic_document.split(start)[1].split(end)[0],
                             synthetic_previous.split(start)[1].split(end)[0])
        for synthetic_count in ("835,052", "834,162", "6,191", "2,237", "56,404",
                                "4,496", "56,430", "6,555", "22,577"):
            self.assertIn(synthetic_count, synthetic_document)
        self.assertIn("pre-freeze", synthetic_document.lower())
        self.assertIn("INCOMPLETE_LIMIT", synthetic_document)
        self.assertEqual((ROOT / "BLOCKERS_P02_screen.md").read_text(encoding="utf-8"), "NONE\n")


if __name__ == "__main__":
    synthetic_log = io.StringIO()
    synthetic_suite = unittest.defaultTestLoader.loadTestsFromTestCase(SyntheticChecks)
    synthetic_result = unittest.TextTestRunner(stream=synthetic_log, verbosity=2).run(synthetic_suite)
    synthetic_report = [
        LABEL,
        "# Offline P02 screening-script checks - amendment A1",
        "",
        "UTC: " + dt.datetime.now(dt.timezone.utc).isoformat(),
        "Python: " + sys.version.split()[0],
        "Script SHA-256: " + hashlib.sha256((ROOT / "screen_P02.py").read_bytes()).hexdigest(),
        "Prereg SHA-256: " + hashlib.sha256((ROOT / "PREREG_P02_screen.md").read_bytes()).hexdigest(),
        "",
        f"Checks: {synthetic_result.testsRun}; failures: {len(synthetic_result.failures)}; errors: {len(synthetic_result.errors)}.",
        "All API responses, candidate metadata and run-output fixtures were fabricated in memory.",
        "Coverage: Europe-PMC-only discovery; bounded 5xx retries; failed/blocked versus zero;",
        "OpenAlex page-based novelty, empty termination and 10,000-record limits; unchanged screening rules.",
        "No network calls, candidate screens, real-data extraction or statistical fits were performed.",
        "These checks do not certify live APIs, retrieval yield, real source feasibility or app/R parity.",
        "",
        "```text",
        synthetic_log.getvalue().rstrip(),
        "```",
        "",
    ]
    (ROOT / "synthetic_screen_P02_checks.md").write_text("\n".join(synthetic_report), encoding="utf-8")
    print(LABEL + f": {synthetic_result.testsRun} checks; passed={synthetic_result.wasSuccessful()}")
    raise SystemExit(0 if synthetic_result.wasSuccessful() else 1)
