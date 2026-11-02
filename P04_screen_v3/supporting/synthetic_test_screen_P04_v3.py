# SYNTHETIC - not data. P04-screen-v3: approved for freeze and release; not yet released. Offline tests only.
"""P04-screen-v3: synthetic tests, written before each behaviour change (red before green).

Every fixture uses invented 10.9999/synthetic-* DOIs and invented titles, nodes and
labels. Nothing here is a study input, a screening judgement or a candidate result.
"""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

sys.dont_write_bytecode = True
BASE = Path(__file__).resolve().parent
SOURCE = BASE / "screen_P04_v3.py"
if not SOURCE.exists():  # release package layout: tests live in supporting/, script at top level
    SOURCE = BASE.parent / "screen_P04_v3.py"
SCRIPT_DIR = SOURCE.parent
m = types.ModuleType("synthetic_screen_v3_module")
m.__file__ = str(SOURCE)
exec(compile(SOURCE.read_text(encoding="utf-8"), str(SOURCE), "exec"), m.__dict__)
MARKER = "SYNTHETIC - not data"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def synth_v1(n, titles=None, record_ids=None):
    """Invented v1-format frame ordered by the v1 seed hash, as the archive is."""
    titles, record_ids = titles or {}, record_ids or {}
    rows = []
    for i in range(n):
        doi = "10.9999/synthetic-%03d" % i
        rows.append({
            "doi": doi,
            "screen_hash": sha(("%s|P04|screen|%s" % (m.V1_SEED, doi)).encode()),
            "screen_status": "UNSCREENED", "metadata_conflict": False,
            "publication_date": "2020-01-01", "observed_publication_dates": ["2020-01-01"],
            "records": [{"fixture": MARKER, "doi_raw": doi, "is_oa": True,
                         "title": titles.get(i, "SYNTHETIC network meta-analysis of invented node set %03d" % i),
                         "record_id": record_ids.get(i, "SYNTHETIC:%03d" % i),
                         "provider": "epmc", "query_id": "synthetic", "journal": MARKER,
                         "pmcid": None, "publication_date": "2020-01-01", "cited_by_count": 0}],
        })
    rows.sort(key=lambda r: (r["screen_hash"], r["doi"]))
    for rank, row in enumerate(rows, 1):
        row["screen_order"] = rank
    return rows


def derive_v2(v1_rows, prior):
    out = []
    for row in v1_rows:
        if row["doi"] in prior:
            continue
        x = dict(row)
        x["v1_frame_order"] = row["screen_order"]
        x["v2_screen_order"] = len(out) + 1
        out.append(x)
    return out


def raw(rows):
    return "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows).encode("utf-8")


@contextlib.contextmanager
def world(v1_rows, prior, n_visited=5):
    """Patch the frozen constants so the synthetic frames stand in for the archive."""
    v2_rows = derive_v2(v1_rows, prior)
    visited = tuple(r["doi"] for r in v2_rows[:n_visited])
    v1_raw, v2_raw = raw(v1_rows), raw(v2_rows)
    with patch.multiple(m, V1_FRAME_SHA256=sha(v1_raw), V2_FRAME_SHA256=sha(v2_raw),
                        V1_FRAME_ROWS=len(v1_rows), V2_FRAME_ROWS=len(v2_rows),
                        PRIOR_V1_EXCLUDED=frozenset(prior), V2_VISITED=visited):
        yield v1_raw, v2_raw, v2_rows


def f_record(order, doi, statuses, disposition, minutes=5.0, sections=("title", "abstract", "methods"),
             cap_expired=False):
    steps = {name: {"status": s, "reason": MARKER} for name, s in zip(m.F_STEPS, statuses)}
    return {"v3_queue_order": order, "doi": doi, "steps": steps, "f_disposition": disposition,
            "sections_read": list(sections), "minutes": minutes, "cap_expired": cap_expired}


def all_pass_f():
    return ["PASS"] * (len(m.F_STEPS) - 2) + ["DEFERRED", "DEFERRED"]


def s_record(order, doi, disposition="PASS", k=20, M=2, L=1, P=1, E=3.5, minutes=30.0):
    status = "PASS" if disposition == "PASS" else "FAIL"
    gates = {name: {"status": "PASS", "reason": MARKER} for name in m.S_GATES}
    if status == "FAIL":
        gates[m.S_GATES[0]]["status"] = "FAIL"
        for name in m.S_GATES[1:]:
            gates[name]["status"] = "NOT ASSESSED"
    return {"v3_queue_order": order, "doi": doi, "gates": gates, "s_disposition": disposition,
            "k": k, "M": M, "L": L, "P": P, "E": E, "minutes": minutes, "cap_expired": False}


class Locks(unittest.TestCase):
    def test_final_copy_stops_before_reading_without_release(self):
        self.assertIs(m.DRAFT, False)
        with patch.object(m, "build_queue", side_effect=AssertionError("NO QUEUE")), \
             patch.object(m.Path, "read_bytes", side_effect=AssertionError("NO READ")), \
             contextlib.redirect_stderr(io.StringIO()) as err:
            with self.assertRaises(SystemExit) as caught:
                m.main(["--build", "--v1-frame", "x", "--v2-frame", "y"])
        self.assertEqual(caught.exception.code, 2)
        self.assertIn("public screening release", err.getvalue())

    def test_draft_flag_still_locks(self):
        with patch.object(m, "DRAFT", True):
            with self.assertRaisesRegex(ValueError, "DRAFT"):
                m.check_release(types.SimpleNamespace())

    def release_args(self, tag="P04-screen-v3", doi="PENDING", prereg=None, script=None):
        prereg_sha = prereg if prereg is not None else sha((SCRIPT_DIR / m.PREREG_FILENAME).read_bytes())
        script_sha = script if script is not None else sha(SOURCE.read_bytes())
        return types.SimpleNamespace(
            screen_release_url="https://github.com/mahmood726-cyber/usecase-preregistrations/releases/tag/" + tag,
            screen_release_doi=doi, prereg_sha256=prereg_sha, script_sha256=script_sha)

    def test_check_release(self):
        with patch.object(m, "__file__", str(SOURCE)):
            ok = m.check_release(self.release_args())
            self.assertFalse(ok["public_release_verified_by_script"])
            self.assertEqual(m.check_release(self.release_args(doi="https://doi.org/10.5281/zenodo.1"))["screen_release_doi"],
                             "https://doi.org/10.5281/zenodo.1")
            for bad in (self.release_args(tag="P04-screen-v2"), self.release_args(tag="P04-screen-v1"),
                        self.release_args(prereg="0" * 64), self.release_args(script="0" * 64),
                        self.release_args(doi="10.5281/zenodo.1")):
                with self.subTest(bad=bad):
                    with self.assertRaises(ValueError):
                        m.check_release(bad)

    def test_release_build_end_to_end_and_no_overwrite(self):
        v1 = synth_v1(12)
        prior = {v1[2]["doi"]}
        with tempfile.TemporaryDirectory() as tmp, world(v1, prior) as (v1_raw, v2_raw, _):
            tmp = Path(tmp)
            pkg = tmp / "pkg"
            pkg.mkdir()
            (tmp / "v1.jsonl").write_bytes(v1_raw)
            (tmp / "v2.jsonl").write_bytes(v2_raw)
            argv = ["--build", "--screen-release-url", "SYNTHETIC", "--v1-frame", str(tmp / "v1.jsonl"),
                    "--v2-frame", str(tmp / "v2.jsonl"), "--output-dir", str(pkg / "out" / "v3_run_01")]
            release = {"screen_release_url": "SYNTHETIC", "public_release_verified_by_script": False}
            with patch.object(m, "__file__", str(pkg / "screen_P04_v3.py")), \
                 patch.object(m, "check_release", return_value=release), \
                 contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(m.main(argv), 0)
                audit = json.loads((pkg / "out" / "v3_run_01" / "queue_P04_v3_audit.json").read_text(encoding="utf-8"))
                self.assertEqual(audit["release"], release)
                self.assertIn("declared_filter", audit)
                self.assertTrue((pkg / "out" / "v3_run_01" / "queue_P04_v3.jsonl").exists())
                with self.assertRaises(SystemExit):
                    m.main(argv)
                with self.assertRaises(SystemExit):
                    m.main(argv[:-1] + [str(tmp / "outside")])

    def test_frozen_numbers_and_exclusion_composition(self):
        self.assertEqual((m.N_F, m.N_S, m.CAP_F_MIN, m.CAP_S_MIN), (40, 5, 20, 60))
        self.assertEqual(m.RELEASE_TAG, "P04-screen-v3")
        self.assertEqual(m.ACCEPTED_LICENCES, ("CC BY", "CC0"))
        self.assertEqual((m.K_MIN, m.K_MAX, m.E_MAX_HOURS), (5, 60, 4.0))
        self.assertEqual(m.V1_SEED, "2026102804")
        self.assertEqual(m.V1_FRAME_SHA256,
                         "fef70cafb5a84c329c62b8b8122d2c634e5a43301455c1c5065a7bbe4053063f")
        self.assertEqual(m.V2_FRAME_SHA256,
                         "3563a7efe93c2f74d6a2718fef647ec5a0132cfc21e32870f0fe69fda7277d1d")
        self.assertEqual((len(m.PRE_V1_EXCLUDED), len(m.V1_TRIAGED), len(m.PRIOR_V1_EXCLUDED)), (5, 21, 26))
        self.assertEqual(m.V2_VISITED, ("10.1007/s40123-026-01434-w", "10.3389/fendo.2022.895458",
                                        "10.3389/fendo.2025.1462104", "10.1097/md.0000000000028365",
                                        "10.1111/dom.70742"))
        self.assertEqual(len(m.excluded_dois()), 31)
        self.assertFalse(hasattr(m, "NEW_SEED"), "v3 must not introduce a seed")

    def test_dry_build_cannot_write_into_package_or_overwrite(self):
        with self.assertRaises(ValueError):
            m.dry_output_paths(str(SCRIPT_DIR))
        with self.assertRaises(ValueError):
            m.dry_output_paths(str(SCRIPT_DIR / "child"))
        with tempfile.TemporaryDirectory() as tmp:
            q, a = m.dry_output_paths(tmp)
            q.write_text(MARKER, encoding="utf-8")
            with self.assertRaises(ValueError):
                m.dry_output_paths(tmp)


class Queue(unittest.TestCase):
    def setUp(self):
        self.v1 = synth_v1(14)
        self.prior = {self.v1[1]["doi"], self.v1[4]["doi"]}

    def test_queue_starts_after_v2_visits_and_preserves_order(self):
        with world(self.v1, self.prior) as (v1_raw, v2_raw, v2_rows):
            queue, audit = m.build_queue_from_bytes(v1_raw, v2_raw)
        expected = [r["doi"] for r in v2_rows[5:]]
        self.assertEqual([q["doi"] for q in queue], expected)
        self.assertEqual([q["v3_queue_order"] for q in queue], list(range(1, len(expected) + 1)))
        self.assertEqual([q["v2_screen_order"] for q in queue], list(range(6, 6 + len(expected))))
        self.assertTrue(all(q["screen_status"] == "UNSCREENED" for q in queue))
        self.assertEqual(audit["pool_before_rules"], len(expected))
        self.assertEqual(audit["queue_count"], len(expected))
        self.assertFalse(audit["network_access"])
        declared = audit["declared_filter"]
        self.assertEqual((declared["rows_in"], declared["distinct_rows_removed"], declared["rows_kept"]),
                         (len(expected), 0, len(expected)))
        self.assertEqual(declared["rule_item_counts"], {})
        self.assertFalse(declared["removed_rows_use_stage_f_slots"])

    def test_wrong_bytes_rejected(self):
        with world(self.v1, self.prior) as (v1_raw, v2_raw, _):
            with self.assertRaises(ValueError):
                m.build_queue_from_bytes(v1_raw, v2_raw + b"\n")
            with self.assertRaises(ValueError):
                m.build_queue_from_bytes(v1_raw + b"\n", v2_raw)

    def test_v2_frame_must_be_exact_continuation_of_v1(self):
        v2 = derive_v2(self.v1, self.prior)
        v2[7]["v1_frame_order"] += 1
        bad = raw(v2)
        with world(self.v1, self.prior) as (v1_raw, _, _):
            with patch.object(m, "V2_FRAME_SHA256", sha(bad)):
                with self.assertRaises(ValueError):
                    m.build_queue_from_bytes(v1_raw, bad)

    def test_annotated_or_reordered_v2_rejected(self):
        for mutate in ("status", "swap", "visited"):
            v2 = derive_v2(self.v1, self.prior)
            if mutate == "status":
                v2[6]["screen_status"] = "FAIL"
            elif mutate == "swap":
                v2[6], v2[7] = v2[7], v2[6]
            with self.subTest(mutate=mutate), world(self.v1, self.prior) as (v1_raw, _, _):
                bad = raw(v2)
                patches = {"V2_FRAME_SHA256": sha(bad)}
                if mutate == "visited":
                    patches["V2_VISITED"] = tuple(r["doi"] for r in v2[1:6])
                with patch.multiple(m, **patches):
                    with self.assertRaises(ValueError):
                        m.build_queue_from_bytes(v1_raw, bad)

    def test_prior_disposition_in_tail_is_excluded(self):
        # A v2-visited DOI cannot reappear; simulate by listing a tail DOI as excluded.
        with world(self.v1, self.prior) as (v1_raw, v2_raw, v2_rows):
            tail = v2_rows[8]["doi"]
            with patch.object(m, "excluded_dois", lambda: frozenset(self.prior) | {tail} | set(m.V2_VISITED)):
                queue, audit = m.build_queue_from_bytes(v1_raw, v2_raw)
        self.assertNotIn(tail, [q["doi"] for q in queue])
        self.assertIn("prior_disposition", json.dumps(audit["queue_exclusions"]))


class Rules(unittest.TestCase):
    def test_non_original_title_markers(self):
        positives = [
            "Summary of Research: SYNTHETIC invented review title",
            "Plain Language Summary of a SYNTHETIC network meta-analysis",
            "Correction to: SYNTHETIC network meta-analysis",
            "Correction: SYNTHETIC network meta-analysis",
            "Erratum: SYNTHETIC network meta-analysis",
            "Corrigendum to SYNTHETIC network meta-analysis",
            "Retraction Note: SYNTHETIC network meta-analysis",
            "RETRACTED: SYNTHETIC network meta-analysis",
            "WITHDRAWN: SYNTHETIC network meta-analysis",
            "Expression of Concern: SYNTHETIC network meta-analysis",
            "Comment on: SYNTHETIC network meta-analysis",
            "Reply to SYNTHETIC letter on a network meta-analysis",
            "Letter to the Editor regarding a SYNTHETIC NMA",
            "SYNTHETIC drugs for invented disease: a protocol for systematic review and network meta-analysis",
            "SYNTHETIC drugs for invented disease: protocol for a network meta-analysis",
            "SYNTHETIC drugs for invented disease: a study protocol",
            "SYNTHETIC drugs for invented disease network meta-analysis protocol",
        ]
        negatives = [
            "Correction of SYNTHETIC hyperglycaemia: a network meta-analysis",
            "SYNTHETIC insulin titration protocols compared: a network meta-analysis",
            "Glycaemic response to SYNTHETIC drugs: a network meta-analysis",
            "SYNTHETIC summary statistics in network meta-analysis of invented drugs",
            "Commentary-free SYNTHETIC network meta-analysis",
        ]
        for title in positives:
            with self.subTest(title=title):
                self.assertTrue(m.non_original_reasons(title), title)
        for title in negatives:
            with self.subTest(title=title):
                self.assertEqual(m.non_original_reasons(title), [], title)

    def test_preprints_excluded_by_prefix_or_source(self):
        self.assertTrue(m.preprint_reasons("10.21203/rs.3.rs-0000000/v1", ["SYNTHETIC:1"]))
        self.assertTrue(m.preprint_reasons("10.1101/2020.01.01.000000", ["SYNTHETIC:1"]))
        self.assertTrue(m.preprint_reasons("10.9999/synthetic-x", ["PPR:PPR000000"]))
        self.assertEqual(m.preprint_reasons("10.9999/synthetic-x", ["MED:000000"]), [])

    def test_derivative_and_duplicate_rules_in_build(self):
        excluded_title = "SYNTHETIC excluded network meta-analysis of invented node set alpha"
        titles = {0: excluded_title,
                  1: "Summary of Research - SYNTHETIC excluded network meta-analysis of invented node set alpha",
                  2: "Updated SYNTHETIC excluded network meta-analysis of invented node set alpha",
                  3: "SYNTHETIC duplicate title kept once for invented node set beta",
                  4: "SYNTHETIC duplicate title kept once for invented node set beta",
                  5: "Short SYNTHETIC title"}
        v1 = synth_v1(16, titles=titles, record_ids={6: "PPR:PPR000001"})
        excluded_doi = "10.9999/synthetic-000"
        prior = {excluded_doi}
        with world(v1, prior, n_visited=1) as (v1_raw, v2_raw, v2_rows):
            queue, audit = m.build_queue_from_bytes(v1_raw, v2_raw)
        reasons = {e["doi"]: e["reasons"] for e in audit["queue_exclusions"]}
        visited = v2_rows[0]["doi"]
        in_queue = {q["doi"] for q in queue}
        for i in (1, 2):
            doi = "10.9999/synthetic-%03d" % i
            if doi == visited:
                continue
            self.assertNotIn(doi, in_queue)
            self.assertTrue(any(r.startswith("derivative_or_version_of_excluded") for r in reasons[doi]))
        # Exact-title duplicate GROUPS are removed whole (stricter reading, DECISION_v3 D-OD6):
        # no keep-rule and no screener choice between an original and a same-title notice.
        dup = ["10.9999/synthetic-003", "10.9999/synthetic-004"]
        if visited not in dup:
            for d in dup:
                self.assertNotIn(d, in_queue)
                self.assertIn("exact_title_duplicate_group", reasons[d])
            self.assertEqual(audit["declared_filter"]["rule_item_counts"]["exact_title_duplicate_group"], 2)
        declared = audit["declared_filter"]
        self.assertEqual(declared["distinct_rows_removed"], len(audit["queue_exclusions"]))
        self.assertEqual(declared["rows_kept"] + declared["distinct_rows_removed"], declared["rows_in"])
        self.assertNotIn("10.9999/synthetic-006", in_queue)
        self.assertIn("10.9999/synthetic-005", in_queue | {visited})

    def test_licence_list_is_exact(self):
        accept = ["http://creativecommons.org/licenses/by/4.0/",
                  "https://creativecommons.org/licenses/by/3.0/igo/",
                  "https://creativecommons.org/publicdomain/zero/1.0/"]
        reject = ["https://creativecommons.org/licenses/by-sa/4.0/",
                  "https://creativecommons.org/licenses/by-nc/4.0/",
                  "https://creativecommons.org/licenses/by-nd/4.0/",
                  "https://creativecommons.org/licenses/by-nc-nd/4.0/",
                  "https://creativecommons.org/licenses/by-nc-sa/4.0/",
                  "https://www.elsevier.com/open-access/userlicense/1.0/",
                  "https://onlinelibrary.wiley.com/termsAndConditions#vor"]
        for url in accept:
            with self.subTest(url=url):
                self.assertEqual(m.licence_verdict([url], [])["status"], "PASS")
        for url in reject:
            with self.subTest(url=url):
                self.assertEqual(m.licence_verdict([url], [])["status"], "FAIL")
        self.assertEqual(m.licence_verdict([], [])["status"], "FAIL")
        self.assertEqual(m.licence_verdict([], ["This article is distributed under the terms of the "
                                                "Creative Commons Attribution 4.0 International License"])["status"], "PASS")
        self.assertEqual(m.licence_verdict([], ["Creative Commons Attribution-ShareAlike 4.0 International"])["status"],
                         "FAIL")
        self.assertEqual(m.licence_verdict([], ["Creative Commons Attribution-NonCommercial 4.0 International"])["status"],
                         "FAIL")
        self.assertEqual(m.licence_verdict([], ["Distributed under CC0 1.0"])["status"], "PASS")
        self.assertEqual(m.licence_verdict([], ["Creative Commons Attribution-NonCommercial-NoDerivatives "
                                                "4.0 International License"])["status"], "FAIL")
        self.assertEqual(m.licence_verdict(["https://creativecommons.org/licenses/by/4.0/",
                                            "https://creativecommons.org/licenses/by-nc-nd/4.0/"], [])["status"],
                         "FAIL")

    def test_retraction_urls_are_fixed(self):
        urls = m.retraction_urls("10.9999/synthetic-(a)")
        self.assertEqual(urls["europepmc"],
                         "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.9999%2Fsynthetic-%28a%29%22"
                         "&format=json&resultType=core&pageSize=1000&cursorMark=%2A")
        self.assertEqual(urls["openalex"], "https://api.openalex.org/works/https://doi.org/10.9999%2Fsynthetic-%28a%29")
        self.assertEqual(urls["crossref"],
                         "https://api.crossref.org/works?filter=updates%3A10.9999%2Fsynthetic-%28a%29&rows=1000")

    def test_retraction_verdicts(self):
        doi = "10.9999/synthetic-r"

        def epmc(cc_types=(), pub_types=("Journal Article",), title="SYNTHETIC title", match=True):
            rec = {"doi": doi if match else "10.9999/other", "title": title,
                   "pubTypeList": {"pubType": list(pub_types)},
                   "commentCorrectionList": {"commentCorrection": [{"type": t} for t in cc_types]}}
            return {"hitCount": 1, "resultList": {"result": [rec]}}
        ok_oa = (200, {"is_retracted": False})
        ok_cr = (200, {"message": {"items": []}})

        def cr(kind, target=doi):
            return (200, {"message": {"items": [{"DOI": "10.9999/notice", "update-to": [{"DOI": target, "type": kind}]}]}})
        self.assertEqual(m.retraction_verdict(doi, epmc(), ok_oa, ok_cr)["status"], "PASS")
        self.assertEqual(m.retraction_verdict(doi, epmc(["Retraction in"]), ok_oa, ok_cr)["status"], "FAIL")
        self.assertEqual(m.retraction_verdict(doi, epmc(["Partial retraction in"]), ok_oa, ok_cr)["status"], "FAIL")
        self.assertEqual(m.retraction_verdict(doi, epmc(pub_types=["Retracted Publication"]), ok_oa, ok_cr)["status"], "FAIL")
        self.assertEqual(m.retraction_verdict(doi, epmc(title="WITHDRAWN: SYNTHETIC"), ok_oa, ok_cr)["status"], "FAIL")
        self.assertEqual(m.retraction_verdict(doi, epmc(["Expression of concern in"]), ok_oa, ok_cr)["status"], "UNRESOLVED")
        erratum = m.retraction_verdict(doi, epmc(["Erratum in"]), ok_oa, ok_cr)
        self.assertEqual(erratum["status"], "PASS")
        self.assertIn("Erratum in", erratum["flags_for_stage_s"])
        self.assertEqual(m.retraction_verdict(doi, epmc(), (200, {"is_retracted": True}), ok_cr)["status"], "FAIL")
        not_indexed = m.retraction_verdict(doi, epmc(), (404, None), ok_cr)
        self.assertEqual(not_indexed["status"], "PASS")
        self.assertTrue(not_indexed["coverage_limitations"])
        self.assertEqual(m.retraction_verdict(doi, epmc(), (503, None), ok_cr)["status"], "UNRESOLVED")
        self.assertEqual(m.retraction_verdict(doi, epmc(match=False), ok_oa, ok_cr)["status"], "UNRESOLVED")
        self.assertEqual(m.retraction_verdict(doi, None, ok_oa, ok_cr)["status"], "UNRESOLVED")
        self.assertEqual(m.retraction_verdict(doi, epmc(), ok_oa, cr("retraction"))["status"], "FAIL")
        self.assertEqual(m.retraction_verdict(doi, epmc(), ok_oa, cr("withdrawal"))["status"], "FAIL")
        self.assertEqual(m.retraction_verdict(doi, epmc(), ok_oa, cr("expression_of_concern"))["status"], "UNRESOLVED")
        corrected = m.retraction_verdict(doi, epmc(), ok_oa, cr("correction"))
        self.assertEqual(corrected["status"], "PASS")
        self.assertIn("crossref:correction", corrected["flags_for_stage_s"])
        self.assertEqual(m.retraction_verdict(doi, epmc(), ok_oa, cr("retraction", "10.9999/other"))["status"], "PASS")
        self.assertEqual(m.retraction_verdict(doi, epmc(), ok_oa, (503, None))["status"], "UNRESOLVED")
        self.assertEqual(m.retraction_verdict(doi, epmc(), ok_oa, (200, {"message": {}}))["status"], "UNRESOLVED")

    def test_outcome_lock_rules(self):
        P, D = "participant_level", "derived_index"
        # v2 ambiguity 3 (CEI): a sole designated derived index fails; no component substitution.
        locked, reason = m.lock_outcome([{"label": "SYNTHETIC efficacy index", "kind": D}],
                                        [{"label": "HbA1c", "kind": P}, {"label": "body weight", "kind": P}])
        self.assertIsNone(locked)
        self.assertIn("C2", reason)
        locked, _ = m.lock_outcome([{"label": "MACE", "kind": P}],
                                   [{"label": "all-cause mortality", "kind": P}])
        self.assertEqual(locked, "MACE")  # C1: designated composite is kept; components never substitute
        locked, _ = m.lock_outcome([{"label": "SYNTHETIC index", "kind": D}, {"label": "change in HbA1c", "kind": P},
                                    {"label": "body weight change", "kind": P}], [])
        self.assertEqual(locked, "change in HbA1c")  # C3
        locked, _ = m.lock_outcome([], [{"label": "body weight", "kind": P}, {"label": "HbA1c", "kind": P},
                                        {"label": "cardiovascular death", "kind": P}])
        self.assertEqual(locked, "cardiovascular death")  # C4 hierarchy
        locked, _ = m.lock_outcome([], [{"label": "proportion achieving HbA1c target", "kind": P},
                                        {"label": "Alpha SYNTHETIC outcome", "kind": P}])
        self.assertEqual(locked, "Alpha SYNTHETIC outcome")  # target attainment is not the HbA1c tier
        locked, _ = m.lock_outcome([], [{"label": "mortality", "kind": P},
                                        {"label": "cardiovascular mortality", "kind": P}])
        self.assertEqual(locked, "mortality")
        locked, _ = m.lock_outcome([], [{"label": "cardiovascular death or hospitalisation for heart failure", "kind": P},
                                        {"label": "body weight", "kind": P}])
        self.assertEqual(locked, "body weight")  # a label matching two tiers belongs to none
        self.assertEqual(m.lock_outcome([], [{"label": "SYNTHETIC index", "kind": D}]), (None, m.lock_outcome([], [])[1]))

    def test_design_rule_independent_trials(self):
        # v2 ambiguity 2: an NMA whose eligible designs include observational studies fails.
        self.assertEqual(m.design_verdict({"rct", "cohort", "case_control", "cross_sectional"}, False), "FAIL")
        self.assertEqual(m.design_verdict({"rct"}, False), "PASS")
        self.assertEqual(m.design_verdict({"rct", "cohort"}, True), "PASS")
        self.assertEqual(m.design_verdict(set(), False), "UNRESOLVED")
        self.assertEqual(m.design_verdict({"rct", "quasi_randomised"}, False), "FAIL")
        with self.assertRaises(ValueError):
            m.design_verdict({"rct", "SYNTHETIC-unknown"}, False)

    def test_k_rules(self):
        self.assertEqual(m.k_verdict([], "S")["status"], "FAIL")          # v2 #5: no printed outcome k
        self.assertEqual(m.k_verdict([], "F")["status"], "DEFERRED")
        self.assertEqual(m.k_verdict([(18, "articles")], "S")["status"], "FAIL")
        self.assertEqual(m.k_verdict([(4, "trials")], "S")["status"], "FAIL")
        self.assertEqual(m.k_verdict([(61, "RCTs")], "S")["status"], "FAIL")
        self.assertEqual(m.k_verdict([(5, "trials")], "S")["status"], "PASS")
        self.assertEqual(m.k_verdict([(60, "studies")], "S")["status"], "PASS")
        both = m.k_verdict([(12, "trials"), (14, "studies")], "S")
        self.assertEqual((both["status"], both["k"]), ("PASS", 14))
        self.assertEqual(m.k_verdict([(12, "trials"), (62, "studies")], "S")["status"], "FAIL")
        self.assertEqual(m.k_verdict([], "F", review_totals=[(4, "RCTs")])["status"], "FAIL")
        self.assertEqual(m.k_verdict([], "F", review_totals=[(70, "RCTs")])["status"], "DEFERRED")

    def test_drug_node_scope(self):
        # v2 #3 shape: exercise and acupuncture against background medication -> fail.
        self.assertEqual(m.network_scope_verdict({"A": "exercise", "B": "acupuncture",
                                                  "C": "standard_care_background"}), "FAIL")
        self.assertEqual(m.network_scope_verdict({"A": "drug", "B": "exercise", "C": "placebo"}), "FAIL")
        self.assertEqual(m.network_scope_verdict({"A": "drug", "B": "drug_class", "C": "placebo"}), "PASS")
        with self.assertRaises(ValueError):
            m.network_scope_verdict({"A": "SYNTHETIC-unknown"})
        # Stricter reading (DECISION_v3 D-OD16): sponsor-code-only investigational nodes are OUT.
        self.assertEqual(m.network_scope_verdict({"A": "drug", "B": "investigational_code_only", "C": "placebo"}), "FAIL")
        with self.assertRaises(ValueError):
            m.network_scope_verdict({"A": "drug", "B": "investigational_drug"})

    def test_target_choice(self):
        nodes = {"Bdrug", "Adrug", "Cdrug", "Placebo", "Ddrug"}
        pharm = {"Adrug", "Bdrug", "Cdrug", "Ddrug"}
        edges = {frozenset(p) for p in [("Adrug", "Placebo"), ("Bdrug", "Placebo"), ("Cdrug", "Adrug")]}
        self.assertEqual(m.choose_target(nodes, edges, pharm, []), ("Adrug", "Bdrug"))
        self.assertEqual(m.choose_target(nodes, edges, pharm, [("Cdrug", "Bdrug")]), ("Bdrug", "Cdrug"))
        self.assertEqual(m.choose_target(nodes, edges, pharm, [("Adrug", "Cdrug")]), ("Adrug", "Bdrug"))
        self.assertIsNone(m.choose_target({"Adrug", "Bdrug"}, {frozenset(("Adrug", "Bdrug"))}, {"Adrug", "Bdrug"}, []))

    def test_effort_formula(self):
        self.assertEqual(m.effort_hours(20), 3.25)
        self.assertEqual(m.effort_hours(50), 4.0)
        self.assertEqual(m.effort_hours(60), 4.5)
        self.assertEqual(m.effort_hours(20, image_only=True, multi_arm=True, conversion=True, multi_file=True), 4.25)
        self.assertEqual(m.effort_hours(5), 2.75)


class Stages(unittest.TestCase):
    def setUp(self):
        self.queue = [{"v3_queue_order": i, "doi": "10.9999/synthetic-q%03d" % i} for i in range(1, 61)]

    def valid_log(self, n=40, passes=(2, 3, 5)):
        log = []
        for i in range(1, n + 1):
            if i in passes:
                log.append(f_record(i, self.queue[i - 1]["doi"], all_pass_f(), "F-PASS"))
            else:
                st = ["PASS", "FAIL"] + ["NOT ASSESSED"] * (len(m.F_STEPS) - 2)
                log.append(f_record(i, self.queue[i - 1]["doi"], st, "F-FAIL"))
        return log

    def test_valid_stage_f_log(self):
        self.assertEqual(m.validate_stage_f_log(self.queue, self.valid_log(), final=True), [])

    def test_stage_f_violations(self):
        cases = {}
        log = self.valid_log(); del log[3]; cases["skipped row"] = log
        log = self.valid_log(n=40) + [f_record(41, self.queue[40]["doi"], all_pass_f(), "F-PASS")]; cases["41st"] = log
        cases["early stop"] = self.valid_log(n=39)
        log = self.valid_log(); log[1]["sections_read"] = ["title", "results"]; cases["results read"] = log
        log = self.valid_log(); log[1]["sections_read"] = ["supplement"]; cases["supplement read"] = log
        log = self.valid_log(); log[1]["steps"][m.F_STEPS[2]]["status"] = "DEFERRED"; cases["bad deferral"] = log
        log = self.valid_log(); log[0]["steps"][m.F_STEPS[5]]["status"] = "PASS"; cases["assessed after terminal"] = log
        log = self.valid_log(); log[0]["f_disposition"] = "F-PASS"; cases["wrong disposition"] = log
        log = self.valid_log(); log[1]["minutes"] = 20.5; cases["over cap"] = log
        log = self.valid_log(); log[1]["cap_expired"] = True; cases["pass after cap"] = log
        for name, log in cases.items():
            with self.subTest(case=name):
                self.assertTrue(m.validate_stage_f_log(self.queue, log, final=True), name)

    def test_exhaustion_allows_short_log(self):
        short_queue = self.queue[:7]
        log = self.valid_log(n=7)
        self.assertEqual(m.validate_stage_f_log(short_queue, log, final=True), [])

    def test_stage_s_queue_is_first_five_passers_in_order(self):
        passes = (1, 4, 6, 7, 9, 12, 15, 18, 21, 22, 30, 33)
        log = self.valid_log(passes=passes)
        s_queue = m.stage_s_queue(self.queue, log)
        self.assertEqual([x["v3_queue_order"] for x in s_queue], list(passes[:5]))

    def test_stage_s_validation_and_selection(self):
        s_queue = [{"v3_queue_order": o, "doi": "10.9999/synthetic-q%03d" % o} for o in (2, 3, 5)]
        log = [s_record(2, s_queue[0]["doi"], M=1, L=2, P=3, E=2.0),
               s_record(3, s_queue[1]["doi"], M=2, L=1, P=1, E=3.75),
               s_record(5, s_queue[2]["doi"], disposition="FAIL")]
        self.assertEqual(m.validate_stage_s_log(s_queue, log, final=True), [])
        six_queue = [{"v3_queue_order": o, "doi": "10.9999/synthetic-q%03d" % o} for o in range(1, 7)]
        six = [s_record(o, q["doi"], disposition="FAIL") for o, q in zip(range(1, 7), six_queue)]
        self.assertTrue(m.validate_stage_s_log(six_queue, six, final=True))  # a 6th S screen is invalid
        primary, fallback = m.select_passers(log)
        self.assertEqual((primary["v3_queue_order"], fallback["v3_queue_order"]), (3, 2))
        for field, value in (("k", 61), ("k", 4), ("E", 4.25), ("M", 0), ("L", 0), ("P", 0), ("minutes", 61.0)):
            bad = [dict(r) for r in log]
            bad[0][field] = value
            with self.subTest(field=field, value=value):
                self.assertTrue(m.validate_stage_s_log(s_queue, bad, final=True))

    def test_selection_tiebreaks(self):
        log = [s_record(9, "10.9999/synthetic-b", M=2, L=2, P=1, E=3.0),
               s_record(4, "10.9999/synthetic-a", M=2, L=2, P=1, E=3.0),
               s_record(1, "10.9999/synthetic-c", M=2, L=2, P=1, E=3.5)]
        primary, fallback = m.select_passers(log)
        self.assertEqual((primary["v3_queue_order"], fallback["v3_queue_order"]), (4, 9))
        self.assertEqual(m.select_passers([s_record(1, "10.9999/synthetic-z", disposition="FAIL")]), (None, None))


class StageFSections(unittest.TestCase):
    JATS = (b'<?xml version="1.0"?><article xmlns:xlink="http://www.w3.org/1999/xlink"><front><article-meta>'
            b'<title-group><article-title>SYNTHETIC title</article-title></title-group>'
            b'<abstract><p>SYNTHETIC abstract text.</p></abstract>'
            b'<kwd-group><kwd>SYNTHETIC keyword</kwd></kwd-group>'
            b'<permissions><license xlink:href="https://creativecommons.org/licenses/by/4.0/">'
            b'<license-p>SYNTHETIC licence text</license-p></license></permissions>'
            b'</article-meta></front><body>'
            b'<sec><title>Introduction</title><p>SYNTHETIC introduction FORBIDDEN-INTRO</p></sec>'
            b'<sec sec-type="methods"><title>2. Methods</title><p>SYNTHETIC methods ALLOWED-METHODS</p>'
            b'<table-wrap><caption>FORBIDDEN-TABLE</caption></table-wrap>'
            b'<fig><caption>FORBIDDEN-FIG</caption></fig>'
            b'<sec><title>Outcomes</title><p>ALLOWED-SUBSEC</p></sec></sec>'
            b'<sec><title>Results</title><p>FORBIDDEN-RESULTS</p></sec>'
            b'<sec><title>Discussion</title><p>FORBIDDEN-DISCUSSION</p></sec></body>'
            b'<back><sec sec-type="data-availability"><p>FORBIDDEN-DATA</p></sec>'
            b'<supplementary-material><caption>FORBIDDEN-SUPP</caption></supplementary-material></back></article>')

    def test_only_headers_methods_and_licence_survive(self):
        out = m.extract_stage_f_sections(self.JATS)
        blob = json.dumps(out)
        for token in ("ALLOWED-METHODS", "ALLOWED-SUBSEC", "SYNTHETIC abstract text", "SYNTHETIC keyword",
                      "SYNTHETIC licence text", "creativecommons.org/licenses/by/4.0"):
            self.assertIn(token, blob)
        for token in ("FORBIDDEN-INTRO", "FORBIDDEN-TABLE", "FORBIDDEN-FIG", "FORBIDDEN-RESULTS",
                      "FORBIDDEN-DISCUSSION", "FORBIDDEN-DATA", "FORBIDDEN-SUPP"):
            self.assertNotIn(token, blob)
        self.assertTrue(out["methods_found"])

    def test_methods_by_title_and_missing_methods(self):
        jats = self.JATS.replace(b'<sec sec-type="methods"><title>2. Methods</title>',
                                 b'<sec><title>Materials and Methods</title>')
        self.assertIn("ALLOWED-METHODS", json.dumps(m.extract_stage_f_sections(jats)))
        none = self.JATS.replace(b'<sec sec-type="methods"><title>2. Methods</title>',
                                 b'<sec><title>Approach</title>')
        out = m.extract_stage_f_sections(none)
        self.assertFalse(out["methods_found"])
        self.assertNotIn("ALLOWED-METHODS", json.dumps(out))


if __name__ == "__main__":
    suite = unittest.TestSuite()
    for case in (Locks, Queue, Rules, Stages, StageFSections):
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(case))
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    report = ("SYNTHETIC - not data\n\n# Offline P04-screen-v3 software validation (approved for freeze; not yet released)\n\n"
              "Invented bibliographic fixtures only. No candidate was fetched, screened, ranked or scored; "
              "no network call was made. This is not a clinical result or a release certification.\n\n"
              "~~~text\n" + stream.getvalue() + "~~~\n\n"
              "Live API behaviour, remote release existence, real candidate feasibility and app/R parity remain untested.\n")
    if "--write-report" in sys.argv[1:]:  # never rewrite a frozen package file by default
        (BASE / "synthetic_validation_P04_screen_v3.md").write_text(report, encoding="utf-8", newline="\n")
    print(stream.getvalue())
    raise SystemExit(0 if result.wasSuccessful() else 1)
