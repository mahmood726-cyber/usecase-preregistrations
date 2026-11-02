# SYNTHETIC - not data
# P02-screen-v3, approved for freeze and release; not yet released. Offline regression checks.
"""All frames, articles, ledgers and API replies here are invented fixtures.

No network: socket connections and urlopen are patched to fail. No real candidate
is read, screened or scored by these tests.
"""
import contextlib
import hashlib
import importlib.util
import io
import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
# Works both in the working folder (tests beside the script) and in the release package
# (tests in supporting/, script one level up), like the v2 package layout.
ROOT = HERE if (HERE / "screen_P02_v3.py").exists() else HERE.parent
FIELD_COPY = ROOT / "supporting" / "FIELD_USE_CASE_PROTOCOL.md"
spec = importlib.util.spec_from_file_location("synthetic_v3_module", ROOT / "screen_P02_v3.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
LABEL = "SYNTHETIC - not data"


def meta(title=LABEL, pubtype="meta-analysis; journal article", pmcid="PMC0000001", **extra):
    row = dict(title=title, type=pubtype, pmcid=pmcid, is_oa=True, is_retracted=False,
               publication_date="2020-01-01", fixture_label=LABEL)
    row.update(extra)
    return row


def synthetic_frame(n_extra=30, titles=None, pubtypes=None, pmcids=None):
    """Complete-frame-shaped fixture: 16 triaged rows, then n_extra never-triaged rows.

    Returns (rows, patches) where patches rebinds the module's inventory constants to the
    fixture, exactly like the v2 suite's synthetic_archive."""
    titles = titles or {}
    pubtypes = pubtypes or {}
    pmcids = pmcids or {}
    dois = sorted((f"10.9999/synthetic-v3-{i}" for i in range(16 + n_extra)),
                  key=lambda d: (m.order_hash(d), d))
    rows = []
    for rank, doi in enumerate(dois, 1):
        rows.append(dict(
            fixture_label=LABEL, doi=doi, frame_rank=rank,
            order_sha256=m.order_hash(doi), publication_date="2020-01-01",
            screen_status="NOT_SCREENED",
            metadata=[meta(title=titles.get(rank, f"{LABEL} title {rank}"),
                           pubtype=pubtypes.get(rank, "meta-analysis; journal article"),
                           pmcid=pmcids.get(rank, f"PMC{1000 + rank}"), doi_raw=doi)]))
    inventory = [dict(rank=i, doi=d, disposition="EXCLUDED_TA" if 6 <= i <= 9 else "TO_FULL_TEXT")
                 for i, d in enumerate(dois[:16], 1)]
    patches = dict(
        V1_INVENTORY=inventory,
        V1_FULLSCREEN=frozenset(dois[:5]),
        V2_FULLSCREEN=frozenset(dois[9:14]),
        PRE_V1_DOIS=frozenset({"10.9999/synthetic-pre-v1-a", "10.9999/synthetic-pre-v1-b"}),
        PRE_V1_TITLES={"10.9999/synthetic-pre-v1-a": "SYNTHETIC pre-v1 review title A"},
        V1_FRAME_RECORD_COUNT=16 + n_extra,
    )
    return rows, patches


@contextlib.contextmanager
def fixture_constants(patches):
    with contextlib.ExitStack() as stack:
        for key, value in patches.items():
            stack.enter_context(patch.object(m, key, value))
        yield


def jats(body_secs, abstract="SYNTHETIC abstract text.", licence="CC BY 4.0",
         licence_href="https://creativecommons.org/licenses/by/4.0/", title="SYNTHETIC title"):
    secs = "".join(body_secs)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<article xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:ali="http://www.niso.org/schemas/ali/1.0/" '
        'article-type="review-article"><front><journal-meta><journal-title-group>'
        '<journal-title>SYNTHETIC Journal</journal-title></journal-title-group></journal-meta>'
        '<article-meta><title-group><article-title>' + title + '</article-title></title-group>'
        '<permissions><license xlink:href="' + licence_href + '"><license-p>' + licence +
        '</license-p></license></permissions>'
        '<abstract><p>' + abstract + '</p></abstract>'
        '<abstract abstract-type="graphical"><p>SYNTHETIC graphical abstract MUST-NOT-APPEAR</p></abstract>'
        '<kwd-group><kwd>SYNTHETIC keyword</kwd></kwd-group></article-meta></front>'
        '<body>' + secs + '</body><back><ref-list><ref><mixed-citation>SYNTHETIC REF MUST-NOT-APPEAR'
        '</mixed-citation></ref></ref-list></back></article>').encode("utf-8")


def sec(title, text, sec_type=None, inner=""):
    attr = f' sec-type="{sec_type}"' if sec_type else ""
    return f"<sec{attr}><title>{title}</title><p>{text}</p>{inner}</sec>"


def f_ledger(queue, dispositions):
    out = []
    for entry, disp in zip(queue, dispositions):
        row = dict(queue_pos=entry["queue_pos"], doi=entry["doi"], disposition=disp,
                   fixture_label=LABEL)
        if disp == "F_FAIL":
            row["terminal_gate"] = "F-G1-DESIGN"
        out.append(row)
    return out


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

    # ---- identity, constants and locks ------------------------------------------------
    def test_draft_lock_and_pinned_constants(self):
        self.assertFalse(m.DRAFT_ONLY, "approved copy: --run is gated by the release receipt")
        self.assertEqual(m.VERSION, "P02-screen-v3")
        self.assertEqual(m.V1_SEED, "2026102802")
        self.assertFalse(hasattr(m, "SEED"), "v3 introduces no new seed")
        self.assertEqual(m.V1_FRAME_SHA256,
                         "c2aad90cf12b746b9de40dd5a88113ab43eccddb23c406f33008e53a7eff1a04")
        self.assertEqual(m.FIELD_PROTOCOL_SHA256,
                         "4f6e05206d46059cdbb9bcc6c8a34ac47ebad6e7bb7483e5a5398b6037ce9bac")
        self.assertEqual((m.N_F, m.N_S, m.POOL_FIRST_V1_RANK), (40, 5, 17))
        self.assertEqual((m.F_CAP_MINUTES, m.CANDIDATE_CAP_MINUTES), (20, 60))
        self.assertEqual(m.order_hash("10.9999/synthetic-0"),
                         hashlib.sha256(b"2026102802|P02|screen|10.9999/synthetic-0").hexdigest())

    def test_dispositioned_set_is_the_nineteen_known_dois(self):
        self.assertEqual(len(m.PRE_V1_DOIS), 5)
        self.assertEqual(len(m.V1_FULLSCREEN), 5)
        self.assertEqual(len(m.V1_TERMINAL_TA()), 4)
        self.assertEqual(len(m.V2_FULLSCREEN), 5)
        self.assertEqual(len(m.dispositioned_dois()), 19)
        self.assertIn("10.1016/j.eclinm.2026.103847", m.dispositioned_dois())
        self.assertIn("10.3390/nu14010174", m.dispositioned_dois())
        # v1 ranks 14 and 16 were triaged TO_FULL_TEXT but never screened: not dispositioned,
        # yet outside the pool because the pool starts at v1 rank 17.
        self.assertNotIn("10.1186/s40795-025-01152-9", m.dispositioned_dois())

    def test_field_protocol_copy_is_byte_identical(self):
        body = FIELD_COPY.read_bytes()
        self.assertEqual(hashlib.sha256(body).hexdigest(), m.FIELD_PROTOCOL_SHA256)
        self.assertEqual(m.verify_field_protocol(FIELD_COPY),
                         m.FIELD_PROTOCOL_SHA256)
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "FIELD_USE_CASE_PROTOCOL.md"
            bad.write_bytes(body + b"\n")
            with self.assertRaises(m.FrameError):
                m.verify_field_protocol(bad)

    # ---- archived frame validation (unchanged v2 contract) -------------------------------
    def test_complete_frame_accepted_and_cuts_refused(self):
        rows, patches = synthetic_frame()
        with fixture_constants(patches):
            self.assertEqual(len(m.validate_v1_rows(rows)), len(rows))
            for broken in (rows[:16], rows[:-1],
                           rows[:20] + [dict(rows[20], order_sha256="0" * 64)] + rows[21:],
                           rows[:20] + [dict(rows[20], frame_rank=99)] + rows[21:],
                           [rows[1], rows[0]] + rows[2:],
                           rows[:-1] + [dict(rows[-1], doi=rows[0]["doi"])]):
                with self.assertRaises(m.FrameError):
                    m.validate_v1_rows(broken)

    def test_frame_byte_hash_is_checked(self):
        rows, patches = synthetic_frame()
        body = "".join(json.dumps(r) + "\n" for r in rows).encode("utf-8")
        with tempfile.TemporaryDirectory() as tmp, fixture_constants(patches):
            path = Path(tmp) / "frame.jsonl"
            path.write_bytes(body)
            self.assertEqual(len(m.load_v1_frame(path, hashlib.sha256(body).hexdigest())), len(rows))
            with self.assertRaises(m.FrameError):
                m.load_v1_frame(path, "0" * 64)
            with self.assertRaises(m.FrameError):
                m.load_v1_frame(path)  # default = the real archived frame hash, which differs

    # ---- Stage F queue: pool, exclusions, order -----------------------------------------
    def test_pool_is_never_triaged_ranks_in_seeded_order(self):
        rows, patches = synthetic_frame(n_extra=30)
        with fixture_constants(patches):
            queue, excl = m.build_stage_f_queue(rows)
        self.assertEqual([q["v1_frame_rank"] for q in queue], list(range(17, 47)))
        self.assertEqual([q["queue_pos"] for q in queue], list(range(1, 31)))
        self.assertEqual(len(queue) + len(excl), len(rows))
        self.assertTrue(all(e["reason"].startswith("v1_triaged_rank_1_16") for e in excl))
        self.assertEqual(sum(q["within_stage_f_window"] for q in queue), 30)
        self.assertTrue(all(q["stage_f_status"] == "NOT_VISITED" and "score" not in q for q in queue))
        keys = [(q["order_sha256"], q["doi"]) for q in queue]
        self.assertEqual(keys, sorted(keys))

    def test_stage_f_window_is_first_forty(self):
        rows, patches = synthetic_frame(n_extra=55)
        with fixture_constants(patches):
            queue, _ = m.build_stage_f_queue(rows)
        self.assertEqual(sum(q["within_stage_f_window"] for q in queue), 40)
        self.assertTrue(all(q["within_stage_f_window"] == (q["queue_pos"] <= 40) for q in queue))

    def test_dispositioned_doi_and_title_duplicates_are_excluded(self):
        rows, patches = synthetic_frame(n_extra=10)
        # rank 17 repeats (case/punctuation-insensitively) the title of v2 full screen rank 10;
        # rank 18 repeats a verified pre-v1 title; rank 19 carries a pre-v1 DOI itself.
        rows[16]["metadata"][0]["title"] = "  " + rows[9]["metadata"][0]["title"].upper() + "!! "
        rows[17]["metadata"][0]["title"] = "Synthetic PRE-v1 review title A."
        with fixture_constants(patches):
            pre = sorted(m.PRE_V1_DOIS)[0]
            rows[18] = dict(rows[18], doi=pre)
            queue, excl = m.build_stage_f_queue(rows, validate=False)
        reasons = {e["v1_frame_rank"]: e["reason"] for e in excl}
        self.assertEqual(reasons[17], "duplicate_title_of_dispositioned")
        self.assertEqual(reasons[18], "duplicate_title_of_dispositioned")
        self.assertEqual(reasons[19], "prior_disposition")
        self.assertNotIn(17, [q["v1_frame_rank"] for q in queue])

    def test_ranks_14_and_16_style_deferred_rows_are_outside_pool(self):
        rows, patches = synthetic_frame(n_extra=5)
        with fixture_constants(patches):
            queue, excl = m.build_stage_f_queue(rows)
        deferred_unscreened = [e for e in excl if e["v1_frame_rank"] in (15, 16)]
        self.assertTrue(all(e["reason"] == "v1_triaged_rank_1_16_not_screened_outside_v3_pool"
                            for e in deferred_unscreened))

    def test_metadata_non_original_and_retraction_exclusions(self):
        pubtypes = {17: "published erratum; correction", 18: "protocol; journal article",
                    19: "preprint", 20: "letter; comment", 21: "meta-analysis; retracted publication; journal article",
                    22: "retraction of publication; retraction notice", 23: "editorial",
                    24: "meta-analysis; systematic review; journal article"}
        titles = {25: "Corrigendum: SYNTHETIC dose-response meta-analysis",
                  26: "SYNTHETIC exposure and outcome: protocol for a systematic review and meta-analysis",
                  27: "SYNTHETIC exposure: a systematic review and meta-analysis protocol",
                  28: "Plain language summary of SYNTHETIC review",
                  29: "Effect of an exercise protocol on SYNTHETIC outcome: a dose-response meta-analysis",
                  30: "Response to: SYNTHETIC letter"}
        rows, patches = synthetic_frame(n_extra=16, titles=titles, pubtypes=pubtypes)
        with fixture_constants(patches):
            queue, excl = m.build_stage_f_queue(rows)
        reasons = {e["v1_frame_rank"]: e["reason"] for e in excl}
        self.assertEqual(reasons[17], "non_original_pubtype")
        self.assertEqual(reasons[18], "non_original_pubtype")
        self.assertEqual(reasons[19], "non_original_pubtype")
        self.assertEqual(reasons[20], "non_original_pubtype")
        self.assertEqual(reasons[21], "metadata_reports_retracted")
        self.assertEqual(reasons[22], "metadata_reports_retracted")
        self.assertEqual(reasons[23], "non_original_pubtype")
        self.assertEqual(reasons[25], "non_original_title")
        self.assertEqual(reasons[26], "non_original_title")
        self.assertEqual(reasons[27], "non_original_title")
        self.assertEqual(reasons[28], "non_original_title")
        self.assertEqual(reasons[30], "non_original_title")
        kept = [q["v1_frame_rank"] for q in queue]
        self.assertIn(24, kept)
        self.assertIn(29, kept, "an exercise 'protocol' is not a study protocol")
        self.assertEqual(kept, sorted(kept))
        self.assertEqual([q["queue_pos"] for q in queue], list(range(1, len(queue) + 1)))

    def test_within_pool_title_duplicate_is_flagged_not_removed(self):
        titles = {20: "SYNTHETIC same review", 25: "Synthetic: same review."}
        rows, patches = synthetic_frame(n_extra=12, titles=titles)
        with fixture_constants(patches):
            queue, _ = m.build_stage_f_queue(rows)
        by_rank = {q["v1_frame_rank"]: q for q in queue}
        self.assertIsNone(by_rank[20]["title_duplicate_of_queue_pos"])
        self.assertEqual(by_rank[25]["title_duplicate_of_queue_pos"], by_rank[20]["queue_pos"])

    def test_missing_pmcid_is_kept_and_flagged(self):
        rows, patches = synthetic_frame(n_extra=4, pmcids={18: None})
        with fixture_constants(patches):
            queue, _ = m.build_stage_f_queue(rows)
        flagged = {q["v1_frame_rank"]: q["fixed_stage_f_source"] for q in queue}
        self.assertIsNone(flagged[18])
        self.assertEqual(flagged[17],
                         "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1017/fullTextXML")

    # ---- Stage F view: allowed sections only --------------------------------------------
    def test_stage_f_view_keeps_headers_methods_and_licence_only(self):
        body = [sec("Introduction", "INTRO-MUST-NOT-APPEAR"),
                sec("Methods", "METHODS-TEXT-KEEP", sec_type="methods",
                    inner='<sec><title>Statistical analysis</title><p>STATS-KEEP</p>'
                          '<table-wrap><label>Table 1</label><table><tr><td>TABLE-MUST-NOT-APPEAR</td></tr></table></table-wrap>'
                          '<fig><caption><p>FIG-MUST-NOT-APPEAR</p></caption></fig>'
                          '<supplementary-material><p>SUPP-MUST-NOT-APPEAR</p></supplementary-material>'
                          # JATS allows floats INSIDE a paragraph; they must still be removed.
                          '<p>INLINE-KEEP <fig><caption><p>INLINE-FIG-MUST-NOT-APPEAR</p></caption></fig>'
                          '<supplementary-material><caption><p>INLINE-SUPP-MUST-NOT-APPEAR</p></caption>'
                          '</supplementary-material><table-wrap><table><tr><td>INLINE-TABLE-MUST-NOT-APPEAR'
                          '</td></tr></table></table-wrap><inline-graphic/></p></sec>'),
                sec("Results", "RESULTS-MUST-NOT-APPEAR"),
                sec("Discussion", "DISCUSSION-MUST-NOT-APPEAR")]
        view = m.stage_f_view(jats(body))
        text = json.dumps(view)
        for keep in ("METHODS-TEXT-KEEP", "STATS-KEEP", "INLINE-KEEP","SYNTHETIC abstract text.", "SYNTHETIC keyword",
                     "CC BY 4.0", "creativecommons.org/licenses/by/4.0", "SYNTHETIC Journal", "SYNTHETIC title"):
            self.assertIn(keep, text)
        for drop in ("INTRO-MUST-NOT-APPEAR", "RESULTS-MUST-NOT-APPEAR", "DISCUSSION-MUST-NOT-APPEAR",
                     "TABLE-MUST-NOT-APPEAR", "FIG-MUST-NOT-APPEAR", "SUPP-MUST-NOT-APPEAR",
                     "INLINE-FIG-MUST-NOT-APPEAR", "INLINE-SUPP-MUST-NOT-APPEAR", "INLINE-TABLE-MUST-NOT-APPEAR",
                     "REF MUST-NOT-APPEAR", "graphical abstract MUST-NOT-APPEAR"):
            self.assertNotIn(drop, text)
        self.assertTrue(view["methods_found"])
        self.assertEqual(view["methods_rule"], "titled_or_typed")
        self.assertGreaterEqual(view["removed_elements"]["table-wrap"], 1)

    def test_stage_f_view_title_variants_and_positional_fallback(self):
        for title in ("2. Materials and Methods", "Methods and analysis", "Patients and methods", "METHODOLOGY"):
            view = m.stage_f_view(jats([sec("Background", "BG-NO"), sec(title, "M-YES"),
                                        sec("Results", "R-NO")]))
            self.assertTrue(view["methods_found"], title)
            self.assertIn("M-YES", json.dumps(view))
            self.assertNotIn("R-NO", json.dumps(view))
        # No titled Methods: sections between Introduction and Results are taken.
        view = m.stage_f_view(jats([sec("Introduction", "I-NO"), sec("Search strategy", "S-YES"),
                                    sec("Statistical analysis", "A-YES"), sec("Results", "R-NO"),
                                    sec("Discussion", "D-NO")]))
        text = json.dumps(view)
        self.assertTrue(view["methods_found"])
        self.assertEqual(view["methods_rule"], "positional_before_results")
        self.assertIn("S-YES", text)
        self.assertIn("A-YES", text)
        self.assertNotIn("I-NO", text)
        self.assertNotIn("R-NO", text)

    def test_stage_f_view_without_methods_or_xml_fails_closed(self):
        view = m.stage_f_view(jats([sec("Results", "R-NO"), sec("Discussion", "D-NO")]))
        self.assertFalse(view["methods_found"])
        self.assertEqual(view["methods"], [])
        with self.assertRaises(m.FrameError):
            m.stage_f_view(b"<html><body>Just a moment... captcha</body></html>")
        with self.assertRaises(m.FrameError):
            m.stage_f_view(b"not xml at all")

    # ---- retraction rule ----------------------------------------------------------------
    def test_retraction_status_requires_both_sources(self):
        doi = "10.9999/synthetic-r"
        epmc_ok = {"doi": doi, "pubTypeList": {"pubType": ["meta-analysis", "journal article"]},
                   "commentCorrectionList": {"commentCorrection": [{"type": "Erratum in"}]}}
        oa_ok = {"doi": "https://doi.org/" + doi, "is_retracted": False}
        self.assertEqual(m.retraction_status(doi, epmc_ok, oa_ok)["status"], "CLEAR")
        self.assertEqual(m.retraction_status(doi, epmc_ok, oa_ok)["errata_recorded"], 1)
        self.assertEqual(m.retraction_status(doi, None, oa_ok)["status"], "UNVERIFIED")
        self.assertEqual(m.retraction_status(doi, epmc_ok, None)["status"], "UNVERIFIED")
        self.assertEqual(m.retraction_status(doi, dict(epmc_ok, doi="10.9999/other"), oa_ok)["status"],
                         "UNVERIFIED")
        self.assertEqual(m.retraction_status(doi, epmc_ok, dict(oa_ok, is_retracted=True))["status"],
                         "RETRACTED")
        self.assertEqual(m.retraction_status(
            doi, dict(epmc_ok, pubTypeList={"pubType": ["Retracted Publication"]}), oa_ok)["status"], "RETRACTED")
        self.assertEqual(m.retraction_status(
            doi, dict(epmc_ok, commentCorrectionList={"commentCorrection": [{"type": "Retraction in"}]}),
            oa_ok)["status"], "RETRACTED")
        self.assertEqual(m.retraction_status(
            doi, dict(epmc_ok, commentCorrectionList={"commentCorrection": [{"type": "Expression of concern in"}]}),
            oa_ok)["status"], "CONCERN")
        self.assertEqual(m.retraction_status(doi, epmc_ok, dict(oa_ok, is_retracted=None))["status"],
                         "UNVERIFIED")
        # A Europe PMC core record without pubTypeList cannot show retraction status.
        no_types = {k: v for k, v in epmc_ok.items() if k != "pubTypeList"}
        self.assertEqual(m.retraction_status(doi, no_types, oa_ok)["status"], "UNVERIFIED")

    # ---- Stage F ledger -> Stage S queue -------------------------------------------------
    def _queue(self, n_extra=50):
        rows, patches = synthetic_frame(n_extra=n_extra)
        with fixture_constants(patches):
            queue, _ = m.build_stage_f_queue(rows)
        return queue

    def test_stage_s_queue_from_complete_f_ledger(self):
        queue = self._queue()
        disps = ["F_FAIL"] * 40
        for i in (2, 5, 9, 11, 13, 17, 19, 23, 29, 31, 37, 39):
            disps[i] = "F_PASS"
        s_queue = m.derive_stage_s_queue(f_ledger(queue[:40], disps), queue)
        self.assertEqual(len(s_queue), 12)
        self.assertEqual([s["queue_pos"] for s in s_queue], [3, 6, 10, 12, 14, 18, 20, 24, 30, 32, 38, 40])
        self.assertEqual(sum(s["within_stage_s_limit"] for s in s_queue), 5)
        self.assertEqual([s["s_pos"] for s in s_queue], list(range(1, 13)))

    def test_stage_f_ledger_refuses_skips_reorders_early_stop_and_overrun(self):
        queue = self._queue()
        good = f_ledger(queue[:40], ["F_FAIL"] * 39 + ["F_PASS"])
        bad_cases = [
            good[:39],                                   # stopped early
            good + f_ledger(queue[40:41], ["F_PASS"]),   # a 41st disposition
            [good[1], good[0]] + good[2:],               # reordered
            good[:5] + good[6:] + f_ledger(queue[40:41], ["F_FAIL"]),  # skipped a record
            [dict(good[0], disposition="MAYBE")] + good[1:],
            [dict(good[0], disposition="F_FAIL", terminal_gate="F-UNKNOWN")] + good[1:],
            [dict(good[0], doi="10.9999/not-in-queue")] + good[1:],
        ]
        for ledger in bad_cases:
            with self.assertRaises(m.FrameError):
                m.derive_stage_s_queue(ledger, queue)

    def test_short_queue_needs_every_record(self):
        queue = self._queue(n_extra=7)
        s_queue = m.derive_stage_s_queue(f_ledger(queue, ["F_PASS"] * 7), queue)
        self.assertEqual(len(s_queue), 7)
        with self.assertRaises(m.FrameError):
            m.derive_stage_s_queue(f_ledger(queue[:6], ["F_PASS"] * 6), queue)

    def test_title_duplicate_flag_forces_f_fail_duplicate(self):
        queue = self._queue()
        queue[3] = dict(queue[3], title_duplicate_of_queue_pos=2)
        ledger = f_ledger(queue[:40], ["F_FAIL"] * 40)
        ledger[3] = dict(ledger[3], disposition="F_PASS")
        ledger[3].pop("terminal_gate", None)
        with self.assertRaises(m.FrameError):
            m.derive_stage_s_queue(ledger, queue)
        ledger[3] = dict(ledger[3], disposition="F_FAIL", terminal_gate="F-G0-DUPLICATE")
        self.assertEqual(m.derive_stage_s_queue(ledger, queue), [])

    # ---- effort and selection -----------------------------------------------------------
    def test_effort_formula_quarter_hours_and_cap(self):
        e = m.effort_upper_bound(k=10, image_only_inputs=False, supplement_files=0, unit_conversions=False)
        self.assertEqual(e["components_quarter_hours"],
                         {"extraction_checking": 5, "reproduction": 3, "app_R_comparison": 2,
                          "figure": 1, "short_write_up": 2})
        self.assertEqual(e["total_quarter_hours"], 13)
        # Calibration point: the highest prior human estimate (pre-v1 Liang, k=12, unit
        # conversions, one supplement) was 3.5-4 h; the formula gives exactly 16 = 4.0 h.
        liang = m.effort_upper_bound(k=12, image_only_inputs=False, supplement_files=1, unit_conversions=True)
        self.assertEqual(liang["total_quarter_hours"], 16)
        self.assertTrue(liang["within_cap"])
        self.assertTrue(m.effort_upper_bound(k=24, image_only_inputs=False, supplement_files=0,
                                             unit_conversions=False)["within_cap"])
        self.assertFalse(m.effort_upper_bound(k=25, image_only_inputs=False, supplement_files=0,
                                              unit_conversions=False)["within_cap"])
        self.assertTrue(e["within_cap"])
        big = m.effort_upper_bound(k=60, image_only_inputs=True, supplement_files=2, unit_conversions=True)
        self.assertFalse(big["within_cap"])
        self.assertEqual(m.effort_upper_bound(k=31, image_only_inputs=False, supplement_files=0,
                                              unit_conversions=False)["components_quarter_hours"]["extraction_checking"], 10)
        for bad_k in (4, 61, None, True, 7.5):
            with self.assertRaises(m.FrameError):
                m.effort_upper_bound(k=bad_k, image_only_inputs=False, supplement_files=0, unit_conversions=False)

    def test_selection_lexicographic_primary_fallback_only(self):
        def s(doi, disp="PASS", fit=1, prof=1, live=1, eff=12, h=None):
            return dict(doi=doi, disposition=disp, audit_fit=fit, profile=prof, live_question=live,
                        effort_quarter_hours=eff, order_sha256=h or hashlib.sha256(doi.encode()).hexdigest(),
                        fixture_label=LABEL)
        ledger = [s("10.9999/a", fit=1, prof=3), s("10.9999/b", fit=2, prof=1),
                  s("10.9999/c", fit=2, prof=1, live=3), s("10.9999/d", disp="FAIL", fit=2, prof=3, live=3),
                  s("10.9999/e", fit=2, prof=1, live=3, eff=8)]
        sel = m.select(ledger)
        self.assertEqual(sel["primary"], "10.9999/e")
        self.assertEqual(sel["fallback"], "10.9999/c")
        self.assertEqual(sel["status"], "PRIMARY_AND_FALLBACK")
        self.assertEqual(m.select([s("10.9999/x")])["status"], "PRIMARY_ONLY_FALLBACK_ABSENT")
        self.assertEqual(m.select([s("10.9999/x", disp="FAIL")])["status"], "STOP_NO_PASS")
        tie = [s("10.9999/p", h="f" * 64), s("10.9999/q", h="0" * 64)]
        self.assertEqual(m.select(tie)["primary"], "10.9999/q")
        with self.assertRaises(m.FrameError):
            m.select([s("10.9999/x", fit=3)])

    # ---- receipt, CLI and outputs -------------------------------------------------------
    def test_run_refused_in_draft_before_file_access(self):
        with patch.object(m, "DRAFT_ONLY", True), \
                patch.object(m.Path, "read_text", side_effect=AssertionError("must not read")):
            with self.assertRaises(m.FrameError):
                m.check_release(Path("unused.json"))

    def test_receipt_contract_on_synthetic_bytes(self):
        good = dict(paper="P02", version="P02-screen-v3", ordering_seed="2026102802",
                    decision_by="Mahmood", decision="APPROVE_V3_TWO_STAGE_SCREEN",
                    decision_evidence=LABEL, approved_at_utc="2026-01-01T00:00:00Z",
                    released_at_utc="2026-01-02T00:00:00Z", n_f=40, n_s=5,
                    f_cap_minutes=20, candidate_cap_minutes=60,
                    v1_frame_sha256=m.V1_FRAME_SHA256, field_protocol_sha256=m.FIELD_PROTOCOL_SHA256,
                    github_release_url="https://github.com/mahmood726-cyber/usecase-preregistrations/releases/tag/P02-screen-v3",
                    zenodo_doi="PENDING", script_sha256="0" * 64, prereg_sha256="0" * 64)
        with tempfile.TemporaryDirectory() as tmp, patch.object(m, "DRAFT_ONLY", False), \
                patch.object(m, "_local_hash", side_effect=lambda which: "0" * 64):
            path = Path(tmp) / "receipt.json"
            path.write_text(json.dumps(good), encoding="utf-8")
            self.assertEqual(m.check_release(path)["version"], "P02-screen-v3")
            for key, value in (("version", "P02-screen-v2"), ("ordering_seed", "2026103002"),
                               ("n_f", 41), ("n_s", "10"), ("f_cap_minutes", 30),
                               ("candidate_cap_minutes", 80), ("decision", "APPROVE_ONE_FIVE_SCREEN_BATCH"),
                               ("field_protocol_sha256", "0" * 64), ("v1_frame_sha256", "0" * 64),
                               ("released_at_utc", "2025-12-31T00:00:00Z"), ("zenodo_doi", "TBD"),
                               ("github_release_url", "https://github.com/x/y/releases/tag/P02-screen-v2"),
                               ("script_sha256", "1" * 64)):
                path.write_text(json.dumps(dict(good, **{key: value})), encoding="utf-8")
                with self.assertRaises(m.FrameError, msg=key):
                    m.check_release(path)

    def test_dry_build_writes_labelled_outputs_and_refuses_overwrite(self):
        rows, patches = synthetic_frame(n_extra=45, pubtypes={17: "preprint", 18: "retracted publication"},
                                        titles={19: "SYNTHETIC: study protocol"})
        body = "".join(json.dumps(r) + "\n" for r in rows).encode("utf-8")
        with tempfile.TemporaryDirectory() as tmp, fixture_constants(patches):
            frame = Path(tmp) / "frame.jsonl"
            frame.write_bytes(body)
            out = Path(tmp) / "dry"
            manifest = m.dry_build(frame, out, expected_hash=hashlib.sha256(body).hexdigest())
            self.assertEqual(manifest["status"], "DRY_BUILD_NOT_A_RUN")
            self.assertEqual(manifest["network_requests"], 0)
            self.assertEqual(manifest["queue_count"], 42)
            # D6: the metadata filter is a DECLARED, counted and reported stage.
            self.assertEqual(manifest["declared_filter_stage"], {
                "name": "declared metadata filter stage (protocol section 3.3)",
                "counted_and_reported": True,
                "input_pool_records": 45,
                "removed": {"prior_disposition": 0, "duplicate_title_of_dispositioned": 0,
                            "metadata_reports_retracted": 1, "non_original_pubtype": 1,
                            "non_original_title": 1},
                "removed_total": 3, "remaining": 42})
            self.assertEqual(manifest["stage_f_window_count"], 40)
            self.assertEqual(manifest["queue_count"] + manifest["exclusion_count"], len(rows))
            for name in m.DRY_OUTPUTS:
                self.assertTrue((out / name).exists(), name)
            q = [json.loads(x) for x in (out / "stage_f_queue_P02_v3_DRYBUILD.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual(manifest["output_hashes"]["stage_f_queue_P02_v3_DRYBUILD.jsonl"],
                             hashlib.sha256((out / "stage_f_queue_P02_v3_DRYBUILD.jsonl").read_bytes()).hexdigest())
            self.assertTrue(all(r["stage_f_status"] == "NOT_VISITED" for r in q))
            with self.assertRaises(m.FrameError):
                m.dry_build(frame, out, expected_hash=hashlib.sha256(body).hexdigest())

    def test_offline_cli(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.assertEqual(m.main(["--print-queries"]), 0)
        text = buf.getvalue()
        self.assertIn("fullTextXML", text)
        self.assertIn("resultType=core", text)
        self.assertIn("api.openalex.org/works/https://doi.org/<doi>", text)
        err = io.StringIO()
        with contextlib.redirect_stderr(err), self.assertRaises(SystemExit):
            m.main([])
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(m.main(["--run", "--release-record", "x.json", "--v1-frame", "y.jsonl",
                                     "--out-dir", "z"]), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
