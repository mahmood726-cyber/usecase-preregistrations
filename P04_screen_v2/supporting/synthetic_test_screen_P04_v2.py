# SYNTHETIC - not data. Offline tests only; no candidate records or network.
"""All generated fixtures use invented DOI/ID metadata, not study inputs."""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

sys.dont_write_bytecode = True
BASE = Path(__file__).resolve().parent
SOURCE = BASE / "screen_P04_v2.py"
m = types.ModuleType("synthetic_screen_module")
m.__file__ = str(SOURCE)
exec(compile(SOURCE.read_text(encoding="utf-8"), str(SOURCE), "exec"), m.__dict__)
MARKER = "SYNTHETIC - not data"


def record(suffix, day="2020-01-01", oa=True):
    return {"fixture": MARKER, "doi_raw": "10.9999/synthetic-" + suffix,
            "publication_date": day, "is_oa": oa, "record_id": suffix,
            "provider": "epmc", "query_id": "synthetic-query", "title": MARKER}


def item(suffix):
    return {"fixture": MARKER, "source": "SYNTHETIC", "id": suffix,
            "doi": "10.9999/synthetic-" + suffix, "firstPublicationDate": "2020-01-01",
            "isOpenAccess": "Y", "title": MARKER}


class Tests(unittest.TestCase):
    def test_draft_stops_before_network_and_outputs(self):
        # Retained lock check: a copy with DRAFT=True / no option still stops first.
        with patch.object(m, "DRAFT", True), patch.object(m, "APPROVED_OPTION", None), \
             patch.object(m, "get_json", side_effect=AssertionError("NETWORK FORBIDDEN")), \
             patch.object(m, "resolve_outputs", side_effect=AssertionError("NO OUTPUT")), \
             contextlib.redirect_stderr(io.StringIO()) as err:
            with self.assertRaises(SystemExit) as caught:
                m.main([])
        self.assertEqual(caught.exception.code, 2)
        self.assertIn("DRAFT", err.getvalue())
        self.assertNotEqual(m.NEW_SEED, m.V1_SEED)

    def test_final_copy_is_option_A_and_stops_without_release(self):
        # Mahmood 2026-10-30: Option A approved; Option B not chosen.
        self.assertIs(m.DRAFT, False)
        self.assertEqual(m.APPROVED_OPTION, "A")
        self.assertEqual(m.V1_SEED, "2026102804")
        with patch.object(m, "get_json", side_effect=AssertionError("NETWORK FORBIDDEN")), \
             patch.object(m, "resolve_outputs", side_effect=AssertionError("NO OUTPUT")), \
             patch.object(m, "continuation_frame", side_effect=AssertionError("NO FRAME")), \
             contextlib.redirect_stderr(io.StringIO()) as err:
            with self.assertRaises(SystemExit) as caught:
                m.main([])
        self.assertEqual(caught.exception.code, 2)
        self.assertIn("public screening release", err.getvalue())

    def test_normalization_and_date_boundaries(self):
        self.assertEqual(m.canonical_doi(" HTTPS://DOI.ORG/10.9999/SYNTHETIC-a%28x%29 "),
                         "10.9999/synthetic-a(x)")
        self.assertIsNone(m.canonical_doi("https://other.invalid/10.9999/synthetic-a"))
        self.assertIsNone(m.valid_date("2020"))
        self.assertIsNone(m.valid_date("2020-02-31"))
        rows = [record("start", m.START), record("end", m.END),
                record("early", "2016-10-27"), record("late", "2026-10-29")]
        frame, excluded = m.ordered_frame(rows)
        self.assertEqual({x["doi"] for x in frame},
                         {"10.9999/synthetic-start", "10.9999/synthetic-end"})
        self.assertEqual(len(excluded), 2)

    def test_new_seed_order_dedup_and_exclusions(self):
        rows = [record("a"), record("b"), record("c"), record("b"),
                record("no-date", "2020"), record("no-oa", oa=False)]
        with patch.object(m, "EXCLUDED_DOIS", frozenset({"10.9999/synthetic-b"})):
            frame, excluded = m.ordered_frame(rows)
            reverse, _ = m.ordered_frame(list(reversed(rows)))
        self.assertEqual(frame, reverse)
        expected = sorted(["10.9999/synthetic-a", "10.9999/synthetic-c"],
                          key=lambda d: hashlib.sha256(
                              (m.NEW_SEED + "|P04|screen|" + d).encode()).hexdigest())
        self.assertEqual([x["doi"] for x in frame], expected)
        self.assertTrue(all(x["screen_status"] == "UNSCREENED" for x in frame))
        self.assertEqual(len(excluded), 3)

    def test_complete_pages_and_true_zero(self):
        pages = iter([{"hitCount": 2, "resultList": {"result": [item("a")]},
                       "nextCursorMark": "synthetic-next"},
                      {"hitCount": 2, "resultList": {"result": [item("b")]}}])
        rows = m.retrieve_query("epmc", "synthetic", {}, lambda *a: next(pages),
                                {"queries": []})
        self.assertEqual(len(rows), 2)
        self.assertEqual(m.retrieve_query("epmc", "synthetic", {},
                         lambda *a: {"hitCount": 0, "resultList": {"result": []}},
                         {"queries": []}), [])

    def test_incomplete_duplicate_and_changed_count_rejected(self):
        cases = [
            [{"hitCount": 2, "resultList": {"result": [item("a")]}}],
            [{"hitCount": 2, "resultList": {"result": [item("a"), item("a")]}}],
            [{"hitCount": 2, "resultList": {"result": [item("a")]},
              "nextCursorMark": "synthetic-next"},
             {"hitCount": 3, "resultList": {"result": [item("b")]}}],
        ]
        for objects in cases:
            with self.subTest(objects=objects):
                pages = iter(objects)
                with self.assertRaises(m.RetrievalError):
                    m.retrieve_query("epmc", "synthetic", {}, lambda *a: next(pages),
                                     {"queries": []})

    def test_bounded_5xx_and_no_auth_retry(self):
        url = m.EUROPE_PMC + "?synthetic=true"
        for code, attempts in [(503, 5), (403, 1), (429, 1)]:
            audit, delays = {"requests": []}, []
            def opener(*args, **kwargs):
                raise HTTPError(url, code, MARKER, {}, None)
            with self.assertRaises(m.RetrievalError):
                m.get_json(url, audit, opener=opener, sleep=delays.append)
            self.assertEqual(len(audit["requests"]), attempts)
            self.assertEqual(delays, [1, 2, 4, 8] if code == 503 else [])

    def test_continuation_preserves_original_order_and_rejects_wrong_bytes(self):
        with patch.object(m, "SEED", m.V1_SEED), \
             patch.object(m, "EXCLUDED_DOIS", frozenset()):
            rows, _ = m.ordered_frame([record("a"), record("b"), record("c")])
        rows = [{"fixture": MARKER, **r} for r in rows]
        removed = rows[1]["doi"]
        raw = ("\n".join(json.dumps(x) for x in rows) + "\n").encode()
        with patch.object(m.Path, "read_bytes", return_value=raw) as reader, \
             patch.object(m, "V1_FRAME_SHA256", hashlib.sha256(raw).hexdigest()), \
             patch.object(m, "EXCLUDED_DOIS", frozenset({removed})), \
             patch.object(m, "V1_TRIAGED_DOIS", frozenset({removed})):
            audit = {}
            kept = m.continuation_frame("synthetic_v1_frame.jsonl", audit)
            self.assertEqual([x["doi"] for x in kept], [rows[0]["doi"], rows[2]["doi"]])
            self.assertEqual([x["v1_frame_order"] for x in kept], [1, 3])
            self.assertEqual([x["v2_screen_order"] for x in kept], [1, 2])
            self.assertFalse(audit["network_discovery_performed"])
            reader.return_value = raw + b"\n"
            with self.assertRaises(ValueError):
                m.continuation_frame("synthetic_v1_frame.jsonl", {})

    def test_v1_release_cannot_activate_v2(self):
        args = types.SimpleNamespace(screen_release_doi="PENDING", screen_release_url=
            "https://github.com/mahmood726-cyber/usecase-preregistrations/releases/tag/P04-screen-v1")
        with patch.object(m, "DRAFT", False), patch.object(m, "APPROVED_OPTION", "B"):
            with self.assertRaisesRegex(ValueError, "v1 release"):
                m.check_release(args)

    def test_citations_require_empty_terminal_page(self):
        pages = iter([{"meta": {"count": 1}, "results": [{"id": "SYNTHETIC-W1"}]},
                      {"meta": {"count": 1}, "results": []}])
        summary = m.retrieve_openalex_citations("W999999999", lambda *a: next(pages), {})
        self.assertEqual(summary["status"], "complete")
        self.assertEqual(len(summary["pages"]), 2)
        self.assertTrue(summary["empty_terminal_page"])

    def test_exact_ten_thousand_without_terminal_empty_is_incomplete(self):
        def get_page(url, audit):
            page = int(url.rsplit("page=", 1)[1])
            return {"meta": {"count": 10000},
                    "results": [{"id": "SYNTHETIC-" + str(page) + "-" + str(i)}
                                for i in range(100)]}
        summary = m.retrieve_openalex_citations("W999999999", get_page, {})
        self.assertEqual(summary["received"], 10000)
        self.assertEqual(summary["status"], "incomplete")
        self.assertEqual(len(summary["pages"]), 100)
        self.assertFalse(summary["empty_terminal_page"])

    def test_output_path_cannot_escape_out(self):
        with self.assertRaises(ValueError):
            m.output_directory(str(BASE.parent))


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    report = ("SYNTHETIC - not data\n\n# Offline P04 v2 draft software validation\n\n"
              "Invented bibliographic fixtures only. No candidate was fetched, screened, "
              "ranked or scored; no network call was made. This is not a clinical result "
              "or release certification. Fixtures ran in memory; outputs are confined to out/.\n\n"
              "~~~text\n" + stream.getvalue() + "~~~\n\n"
              "Live API availability, remote release existence, actual candidate feasibility "
              "and app/R runtime parity remain untested.\n")
    (BASE / "synthetic_validation_P04_screen_v2.md").write_text(report, encoding="utf-8")
    print(stream.getvalue())
    raise SystemExit(0 if result.wasSuccessful() else 1)
