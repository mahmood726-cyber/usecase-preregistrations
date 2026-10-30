# SYNTHETIC - not data
"""Offline v2 regression checks. All candidates/API replies are invented fixtures."""
import contextlib
import hashlib
import importlib.util
import io
import json
import socket
import unittest
from pathlib import Path
from unittest.mock import patch
import urllib.error

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("synthetic_v2_module", ROOT / "screen_P02_v2.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
LABEL = "SYNTHETIC - not data"


def raw(index=1, **changes):
    row = dict(id=str(index), source="MED", doi=f"10.9999/synthetic-{index}",
               title=LABEL, firstPublicationDate="2020-01-01",
               isOpenAccess="Y")
    row.update(changes)
    return row


def projected(index=1, **changes):
    return m.project_record("europe_pmc", "EPMC-1", raw(index, **changes))


def fake_fetch(pages):
    queue = iter(pages)
    return lambda url: (next(queue), {"fixture_label": LABEL})


def synthetic_archive(extra=0):
    # extra > 0 gives a complete-frame-shaped archive: 16 triaged rows followed by
    # `extra` never-triaged rows, like the real 1,798-row v1 frame (B2-S).
    dois = sorted((f"10.9999/synthetic-archive-{i}" for i in range(16 + extra)),
                  key=lambda d: (m.order_hash(d, m.V1_SEED), d))
    rows = [dict(fixture_label=LABEL, doi=d, frame_rank=i,
                 order_sha256=m.order_hash(d, m.V1_SEED),
                 screen_status="NOT_SCREENED", metadata=[])
            for i, d in enumerate(dois, 1)]
    inventory = [dict(rank=i, doi=d,
                      disposition="EXCLUDED_TA" if 6 <= i <= 9 else "TO_FULL_TEXT")
                 for i, d in enumerate(dois[:16], 1)]
    return rows, dict(V1_INVENTORY=inventory, V1_FULLSCREEN=frozenset(dois[:5]),
                      V1_TERMINAL_TA=frozenset(dois[5:9]), V1_DEFERRED=dois[9:16],
                      V1_FRAME_RECORD_COUNT=16 + extra,
                      HISTORICAL_EXCLUDED=frozenset(), EXCLUDED=frozenset(dois[:9]))


class MemoryStream(io.StringIO):
    def close(self):
        pass


class SyntheticTests(unittest.TestCase):
    def setUp(self):
        self.network = patch.object(socket, "create_connection",
                                    side_effect=AssertionError("Network forbidden in synthetic checks"))
        self.network.start()
        self.addCleanup(self.network.stop)
        self.http = patch.object(m.urllib.request, "urlopen",
                                 side_effect=AssertionError("Unmocked HTTP forbidden"))
        self.http.start()
        self.addCleanup(self.http.stop)

    def test_doi_normalization_and_suffix(self):
        self.assertEqual(m.normalize_doi(" https://DOI.org/10.9999/SYNTHETIC%3BX "),
                         "10.9999/synthetic;x")
        self.assertIsNone(m.normalize_doi("not a doi"))

    def test_date_edges_dedup_conflicts_and_exclusions(self):
        rows = [projected(1, firstPublicationDate=m.START),
                projected(2, firstPublicationDate=m.END),
                projected(3, firstPublicationDate="2016-10-27"),
                projected(4, firstPublicationDate="2026-10-29"),
                projected(5, firstPublicationDate="2020"),
                projected(6, isOpenAccess="N"),
                projected(7, isRetracted="Y"),
                projected(8, doi="invalid"),
                projected(9),
                projected(10, doi="10.9999/synthetic-1", firstPublicationDate="2020-02-01")]
        frame, excluded = m.make_frame(rows, excluded={"10.9999/synthetic-9"})
        self.assertEqual({r["doi"] for r in frame},
                         {"10.9999/synthetic-1", "10.9999/synthetic-2"})
        self.assertEqual(len(excluded), 7)
        self.assertTrue(next(r for r in frame if r["doi"].endswith("-1"))["date_conflict"])
        self.assertIsNone(projected()["is_retracted"])

    def test_seed_order_is_deterministic_and_no_scores(self):
        rows = [projected(i) for i in range(10)]
        a, _ = m.make_frame(rows, excluded=set())
        b, _ = m.make_frame(list(reversed(rows)), excluded=set())
        self.assertEqual(a, b)
        self.assertEqual(sum(r["within_five_screen_limit"] for r in a), 5)
        self.assertEqual(m.order_hash("10.9999/synthetic-0"),
                         hashlib.sha256(b"2026103002|P02|screen|10.9999/synthetic-0").hexdigest())
        self.assertNotEqual(m.SEED, m.V1_SEED)
        self.assertTrue(all(r["screen_status"] == "NOT_SCREENED" and "score" not in r for r in a))

    def test_full_pagination_and_true_zero(self):
        pages = [dict(hitCount=2, resultList={"result": [raw(1)]}, nextCursorMark="next"),
                 dict(hitCount=2, resultList={"result": [raw(2)]})]
        records, report = m.harvest("EPMC-1", "europe_pmc", m.EPMC_QUERY,
                                    fake_fetch(pages), lambda e: None, pace=False)
        self.assertEqual(len(records), 2)
        self.assertTrue(report["complete"])
        records, report = m.harvest("EPMC-1", "europe_pmc", m.EPMC_QUERY,
                                    fake_fetch([dict(hitCount=0, resultList={"result": []})]),
                                    lambda e: None, pace=False)
        self.assertEqual(records, [])
        self.assertTrue(report["complete"])

    def test_incomplete_and_drift_duplicate_bad_schema_fail(self):
        first = dict(hitCount=2, resultList={"result": [raw(1)]}, nextCursorMark="next")
        cases = [
            [dict(hitCount=2, resultList={"result": [raw(1)]})],
            [first, dict(hitCount=3, resultList={"result": [raw(2)]})],
            [first, dict(hitCount=2, resultList={"result": [raw(1)]})],
            [first, dict(hitCount=2, resultList={"result": []})],
            [dict(hitCount=True, resultList={"result": []})],
        ]
        for pages in cases:
            with self.subTest(pages=pages):
                events = []
                with self.assertRaises(m.FrameError):
                    m.harvest("EPMC-1", "europe_pmc", m.EPMC_QUERY,
                              fake_fetch(pages), events.append, pace=False)
                self.assertEqual(events[-1]["status"], "FAILED_BLOCKED")

    def test_schema_projection_discards_abstract_and_data(self):
        item = projected(abstractText="SYNTHETIC abstract", unknown_values=[1, 2])
        self.assertNotIn("abstractText", item)
        self.assertNotIn("unknown_values", item)

    def test_original_archive_validation_and_option_A(self):
        rows, overrides = synthetic_archive()
        with patch.multiple(m, create=True, **overrides):
            self.assertEqual(m.validate_v1_rows(rows), rows)
            continued = m.continuation_frame(rows)
            self.assertEqual([r["doi"] for r in continued], overrides["V1_DEFERRED"])
            self.assertEqual([r["order_sha256"] for r in continued],
                             [r["order_sha256"] for r in rows[9:]])
            self.assertEqual(sum(r["within_five_screen_limit"] for r in continued), 5)
            self.assertTrue(all(r["ordering_seed"] == m.V1_SEED for r in continued))

    def test_archive_mismatch_missing_duplicate_rank_hash_and_order_fail(self):
        rows, overrides = synthetic_archive()
        bad_cases = [rows[:-1], rows + [rows[-1]],
                     [{**r, "order_sha256": "0"*64} if i == 0 else r for i,r in enumerate(rows)],
                     [{**r, "frame_rank": 2} if i == 0 else r for i,r in enumerate(rows)],
                     [rows[1], rows[0]] + rows[2:]]
        with patch.multiple(m, create=True, **overrides):
            for bad in bad_cases:
                with self.assertRaises(m.FrameError):
                    m.validate_v1_rows(bad)

    def test_complete_frame_shaped_archive_is_accepted_for_option_A(self):
        # B2-S: the protocol's required input is the complete original v1 frame
        # (1,798 rows), not a 16-row file. Its 16 triaged rows lead the archive.
        rows, overrides = synthetic_archive(extra=8)
        self.assertEqual(len(rows), 24)
        with patch.multiple(m, create=True, **overrides):
            self.assertEqual(m.validate_v1_rows(rows), rows)
            continued = m.continuation_frame(rows)
            self.assertEqual([r["doi"] for r in continued], overrides["V1_DEFERRED"])
            self.assertEqual([r["v1_frame_rank"] for r in continued], list(range(10, 17)))
            self.assertEqual(sum(r["within_five_screen_limit"] for r in continued), 5)

    def test_sixteen_row_cut_and_bad_untriaged_rows_are_refused(self):
        rows, overrides = synthetic_archive(extra=8)
        bad_cases = [rows[:16],  # a reconstructed 16-row cut of the complete frame
                     rows[:-1],
                     [{**r, "order_sha256": "0"*64} if i == 20 else r for i, r in enumerate(rows)],
                     [{**r, "frame_rank": 99} if i == 20 else r for i, r in enumerate(rows)],
                     rows[:20] + [rows[21], rows[20]] + rows[22:],
                     rows[:20] + [rows[3]] + rows[21:]]
        with patch.multiple(m, create=True, **overrides):
            for bad in bad_cases:
                with self.assertRaises(m.FrameError):
                    m.validate_v1_rows(bad)

    def test_option_A_never_labels_untriaged_rows_as_terminal_screens(self):
        result, streams, rows, overrides = self.run_memory(
            "A", lambda url: self.fail("Option A must not fetch"), extra=8)
        self.assertEqual(result["status"], "COMPLETE")
        self.assertEqual(result["frame_count"], 7)
        exclusions = [json.loads(s) for s in
                      streams["metadata_exclusions_P02_v2.jsonl"].getvalue().splitlines()]
        reasons = {x["doi"]: x["reason"] for x in exclusions}
        triaged = {x["doi"] for x in overrides["V1_INVENTORY"]}
        for row in rows:
            if row["doi"] in overrides["V1_DEFERRED"]:
                self.assertNotIn(row["doi"], reasons)
            elif row["doi"] in triaged:
                self.assertEqual(reasons[row["doi"]], "v1_terminal_screen")
            else:
                self.assertEqual(reasons[row["doi"]], "v1_never_triaged_outside_option_A_queue")

    def test_archive_byte_hash_mismatch(self):
        body = b'{"fixture_label":"SYNTHETIC - not data"}\n'
        with patch.object(Path, "read_bytes", return_value=body):
            with self.assertRaises(m.FrameError):
                m.load_v1_frame("synthetic_frame.jsonl", "0"*64)

    def test_draft_lock_prevents_read_or_network(self):
        # Retained lock check: a copy with DRAFT_ONLY=True still refuses before any file access.
        with patch.object(m, "DRAFT_ONLY", True),              patch.object(Path, "read_text", side_effect=AssertionError("Must fail before file access")):
            with self.assertRaisesRegex(m.FrameError, "DRAFT"):
                m.check_release("synthetic_receipt.json", "A")

    def test_final_copy_fixes_option_A_and_refuses_B_before_file_access(self):
        # Mahmood 2026-10-30: Option A approved; Option B not chosen.
        self.assertIs(m.DRAFT_ONLY, False)
        self.assertEqual(m.APPROVED_OPTION, "A")
        self.assertEqual(m.V1_SEED, "2026102802")
        with patch.object(Path, "read_text", side_effect=AssertionError("Must fail before file access")):
            with self.assertRaisesRegex(m.FrameError, "not chosen"):
                m.check_release("synthetic_receipt.json", "B")

    def synthetic_receipt(self, option="A"):
        return dict(fixture_label=LABEL, paper="P02", version="P02-screen-v2",
                    frame_option=option, new_seed=m.SEED,
                    ordering_seed=m.V1_SEED if option == "A" else m.SEED,
                    decision_by="Mahmood", decision="APPROVE_ONE_FIVE_SCREEN_BATCH",
                    decision_evidence="SYNTHETIC test only; no real approval",
                    approved_at_utc="2020-01-01T00:00:00Z",
                    released_at_utc="2020-01-02T00:00:00Z",
                    v1_inventory_reconciled=True, v1_inventory_record_count=16,
                    v1_frame_sha256="1"*64,
                    github_release_url="https://github.com/mahmood726-cyber/usecase-preregistrations/releases/tag/P02-screen-v2",
                    zenodo_doi="PENDING", script_sha256=m.sha256_bytes(b"synthetic bytes"),
                    prereg_sha256=m.sha256_bytes(b"synthetic bytes"))

    def test_approved_copy_receipt_contract_using_only_synthetic_bytes(self):
        receipt = self.synthetic_receipt()
        with patch.object(m, "DRAFT_ONLY", False), \
             patch.object(Path, "read_text", return_value=json.dumps(receipt)), \
             patch.object(Path, "read_bytes", return_value=b"synthetic bytes"):
            self.assertEqual(m.check_release("synthetic_receipt.json", "A"), receipt)

    def test_receipt_rejects_v1_wrong_option_unreconciled_and_wrong_hash(self):
        receipt = self.synthetic_receipt()
        mutations = [dict(version="P02-screen-v1"), dict(frame_option="B"), dict(ordering_seed=m.SEED),
                     dict(v1_inventory_reconciled=False), dict(script_sha256="0"*64),
                     dict(decision_evidence=""), dict(released_at_utc="2099-01-01T00:00:00Z")]
        for change in mutations:
            with patch.object(m, "DRAFT_ONLY", False), \
                 patch.object(Path, "read_text", return_value=json.dumps({**receipt, **change})), \
                 patch.object(Path, "read_bytes", return_value=b"synthetic bytes"):
                with self.assertRaises(m.FrameError):
                    m.check_release("synthetic_receipt.json", "A")

    def run_memory(self, option, fetch, extra=0):
        rows, overrides = synthetic_archive(extra)
        streams = {}
        def memory_open(path, mode="r", *args, **kwargs):
            self.assertEqual(mode, "x")
            stream = MemoryStream()
            streams[path.name] = stream
            return stream
        receipt = self.synthetic_receipt(option)
        with patch.multiple(m, create=True, **overrides), \
             patch.object(Path, "open", memory_open), \
             patch.object(Path, "exists", return_value=False), \
             patch.object(Path, "mkdir", return_value=None):
            try:
                result = m.execute(ROOT / "synthetic_memory_run", receipt, option, rows,
                                   fetch=fetch, pace=False)
            except m.FrameError:
                result = None
        return result, streams, rows, overrides

    def test_option_A_execution_makes_no_query(self):
        result, streams, rows, _ = self.run_memory(
            "A", lambda url: self.fail("Option A must not fetch"))
        self.assertEqual(result["frame_count"], 7)
        self.assertEqual(result["full_screens_planned"], 5)
        self.assertEqual(result["queries"], [])
        self.assertFalse(result["candidate_screening_performed"])

    def test_option_B_excludes_entire_v1_including_deferred(self):
        rows, _ = synthetic_archive()
        responses = [dict(hitCount=2, resultList={"result": [
            raw(1, doi=rows[-1]["doi"]), raw(2, doi="10.9999/synthetic-fresh")]} )]
        result, streams, _, _ = self.run_memory("B", fake_fetch(responses))
        self.assertEqual(result["frame_count"], 1)
        written = [json.loads(s) for s in streams["frame_P02_v2.jsonl"].getvalue().splitlines()]
        self.assertEqual(written[0]["doi"], "10.9999/synthetic-fresh")
        exclusions = streams["metadata_exclusions_P02_v2.jsonl"].getvalue()
        self.assertIn("v1_deferred_reserved_outside_fresh_frame_not_a_failure", exclusions)

    def test_failure_manifest_never_becomes_zero_frame(self):
        result, streams, _, _ = self.run_memory(
            "B", fake_fetch([dict(hitCount=2, resultList={"result": []})]))
        self.assertIsNone(result)
        report = json.loads(streams["run_manifest_P02_v2.json"].getvalue())
        self.assertEqual(report["status"], "FAILED_BLOCKED")
        self.assertNotIn("frame_count", report)
        self.assertNotIn("frame_P02_v2.jsonl", streams)

    def test_output_containment_and_overwrite_refusal(self):
        rows, overrides = synthetic_archive()
        with patch.multiple(m, create=True, **overrides):
            with self.assertRaises(m.FrameError):
                m.execute(ROOT.parent, self.synthetic_receipt("A"), "A", rows)
            with patch.object(Path, "exists", return_value=True):
                with self.assertRaises(m.FrameError):
                    m.execute(ROOT / "synthetic_existing", self.synthetic_receipt("A"), "A", rows)

    def test_5xx_retry_budget_and_no_bot_retry(self):
        url = "https://www.ebi.ac.uk/synthetic"
        def error(body=b"SYNTHETIC service failure", status=503):
            return urllib.error.HTTPError(url, status, "SYNTHETIC",
                                          {"Content-Type": "text/plain"}, io.BytesIO(body))
        with patch.object(m.urllib.request, "urlopen", side_effect=[error() for _ in range(5)]) as opener, \
             patch.object(m.time, "sleep") as sleeper:
            with self.assertRaises(m.FrameError):
                m.fetch_json(url)
            self.assertEqual(opener.call_count, 5)
            self.assertEqual([x.args[0] for x in sleeper.call_args_list], [1, 2, 4, 8])
        with patch.object(m.urllib.request, "urlopen",
                          side_effect=error(b"SYNTHETIC captcha", 503)) as opener, \
             patch.object(m.time, "sleep") as sleeper:
            with self.assertRaises(m.FrameError):
                m.fetch_json(url)
            self.assertEqual(opener.call_count, 1)
            sleeper.assert_not_called()

    def test_403_and_transport_are_not_retried(self):
        failures = [
            urllib.error.HTTPError("https://synthetic.invalid", 403, "SYNTHETIC",
                                   {"Content-Type": "text/plain"}, io.BytesIO(b"SYNTHETIC")),
            urllib.error.URLError("SYNTHETIC transport failure"),
        ]
        for failure in failures:
            with patch.object(m.urllib.request, "urlopen", side_effect=failure) as opener:
                with self.assertRaises(m.FrameError):
                    m.fetch_json("https://synthetic.invalid")
                self.assertEqual(opener.call_count, 1)

    def test_offline_queries_and_cli_refusal(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(m.main(["--print-queries"]), 0)
        self.assertIn("cursorMark=%2A", output.getvalue())
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                m.main([])
            with self.assertRaises(SystemExit):
                m.main(["--run", "--frame-option", "B"])
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(m.main(["--run", "--frame-option", "B", "--fetch",
                                     "--release-record", "synthetic_receipt.json",
                                     "--v1-frame", "synthetic_frame.jsonl"]), 1)


if __name__ == "__main__":
    stream = io.StringIO()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(SyntheticTests)
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    report = "# SYNTHETIC - not data\n\n"
    report += "Offline draft-code checks on generated bibliographic fixtures and mocked HTTP only.\n"
    report += "No live requests, real candidate frames, screening, scoring or analysis were run.\n"
    report += "All test frames/manifests/receipts were held in memory; no approval receipt was issued.\n\n"
    report += f"Tests: {result.testsRun}; failures: {len(result.failures)}; errors: {len(result.errors)}.\n\n"
    report += "Validates DOI/date handling, exclusions, seeded ordering, original-frame reconciliation, "
    report += "A/B separation, draft/receipt locks, pagination, failure manifests, access refusal and output guards.\n\n"
    report += "Limitations: no live API compatibility, real inventory completeness, source eligibility, novelty, "
    report += "candidate selection, statistical validation or app/R parity is established.\n\n"
    report += "```text\n" + stream.getvalue() + "```\n"
    (ROOT / "synthetic_screen_P02_v2_checks.md").write_text(report, encoding="utf-8")
    print(stream.getvalue())
    raise SystemExit(0 if result.wasSuccessful() else 1)
