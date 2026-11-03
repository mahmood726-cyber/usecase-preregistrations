"""Tests for screen_P04_v4.py. Run: python -I supporting/synthetic_test_screen_P04_v4.py (from the package root)
or with pytest. Uses only the archived v3 bytes in supporting/v3_archive and constructed records; no network."""
import argparse
import importlib.util
import json
from pathlib import Path
import sys

PKG = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("screen_P04_v4", PKG / "screen_P04_v4.py")
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)
A = PKG / "supporting" / "v3_archive"


def _raw():
    return ((A / "queue_P04_v3.jsonl").read_bytes(), (A / "STAGE_F_LOG_P04_v3.jsonl").read_bytes(),
            (A / "STAGE_S_LOG_P04_v3.jsonl").read_bytes())


def _raises(fn, *a, **k):
    try:
        fn(*a, **k)
    except ValueError:
        return True
    return False


def _gates(v3, terminal=None):
    gates = {}
    for g in v3.S_GATES:
        if terminal is None or v3.S_GATES.index(g) < v3.S_GATES.index(terminal):
            gates[g] = {"status": "PASS"}
        elif g == terminal:
            gates[g] = {"status": "FAIL"}
        else:
            gates[g] = {"status": "NOT ASSESSED"}
    return gates


def _rec(row, v3, terminal="S3_k", **extra):
    rec = {"v3_queue_order": row["v3_queue_order"], "doi": row["doi"], "minutes": 10, "cap_expired": False,
           "gates": _gates(v3, terminal), "s_disposition": "PASS" if terminal is None else "FAIL"}
    rec.update(extra)
    return rec


def test_queue_is_the_four_remaining_f_passers_in_order():
    rows, _ = m.build_v4_queue()
    assert [r["v3_queue_order"] for r in rows] == [25, 32, 37, 40]
    assert [r["v4_stage_s_order"] for r in rows] == [1, 2, 3, 4]
    assert all(r["screen_status"] == "UNSCREENED" and r["stage"] == "S" for r in rows)
    queue = {json.loads(l)["v3_queue_order"]: json.loads(l)["doi"] for l in _raw()[0].decode().splitlines() if l.strip()}
    assert [r["doi"] for r in rows] == [queue[o] for o in (25, 32, 37, 40)]


def test_growth_factor_records_18_and_33_are_not_added():
    rows, _ = m.build_v4_queue()
    assert not {18, 33} & {r["v3_queue_order"] for r in rows}


def test_v3_screened_records_are_not_rescreened():
    rows, _ = m.build_v4_queue()
    assert not set(m.V3_SCREENED) & {r["v3_queue_order"] for r in rows}


def test_tampered_f_log_is_refused():
    q, f, s = _raw()
    v3 = m.load_v3_module()
    assert _raises(m.build_v4_queue_from_bytes, q, f.replace(b"F-FAIL", b"F-PASS", 1), s, v3)


def test_tampered_s_log_and_queue_are_refused():
    q, f, s = _raw()
    v3 = m.load_v3_module()
    assert _raises(m.build_v4_queue_from_bytes, q, f, s + b"\n{}", v3)
    assert _raises(m.build_v4_queue_from_bytes, q + b" ", f, s, v3)


def test_tampered_v3_script_is_refused(tmp=None):
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "screen_P04_v3.py"
        p.write_bytes((A / "screen_P04_v3.py").read_bytes().replace(b"N_S = 5", b"N_S = 9"))
        assert _raises(m.load_v3_module, p)


def test_planted_queue_including_18_fails_closed():
    q, f, s = _raw()
    v3 = m.load_v3_module()
    saved = m.V4_QUEUE_ORDERS
    try:
        m.V4_QUEUE_ORDERS = (18, 25, 32, 37, 40)
        assert _raises(m.build_v4_queue_from_bytes, q, f, s, v3)
    finally:
        m.V4_QUEUE_ORDERS = saved


def test_s_log_validator_accepts_four_terminal_fails():
    rows, v3 = m.build_v4_queue()
    assert m.validate_v4_stage_s_log(rows, [_rec(r, v3) for r in rows], v3) == []


def test_s_log_validator_rejects_a_fifth_screen_and_wrong_order():
    rows, v3 = m.build_v4_queue()
    log = [_rec(r, v3) for r in rows]
    assert m.validate_v4_stage_s_log(rows, log + [dict(log[0])], v3)
    assert m.validate_v4_stage_s_log(rows, list(reversed(log)), v3)
    assert m.validate_v4_stage_s_log(rows, log[:3], v3, final=True)


def test_s_log_validator_enforces_pass_thresholds_and_cap():
    rows, v3 = m.build_v4_queue()
    log = [_rec(r, v3) for r in rows]
    log[0] = _rec(rows[0], v3, terminal=None, k=70, M=1, L=1, P=1, E=3.0)
    assert m.validate_v4_stage_s_log(rows, log, v3)
    log[0] = _rec(rows[0], v3, terminal=None, k=20, M=1, L=1, P=1, E=3.0)
    assert m.validate_v4_stage_s_log(rows, log, v3) == []
    log[0]["minutes"] = 75
    assert m.validate_v4_stage_s_log(rows, log, v3)


def test_release_check_rejects_earlier_tags_and_bad_hashes():
    good = dict(screen_release_url=m.RELEASE_URL, screen_release_doi="PENDING", prereg_sha256="0" * 64, script_sha256="0" * 64)
    assert _raises(m.check_release, argparse.Namespace(**good))
    v3_tag = dict(good, screen_release_url=m.RELEASE_URL.replace("v4", "v3"))
    assert _raises(m.check_release, argparse.Namespace(**v3_tag))
    assert not m.DRAFT and m.N_S_V4 == 4


def test_output_dir_must_be_inside_package():
    assert _raises(m.release_output_dir, PKG.parent)
    assert _raises(m.release_output_dir, PKG)


if __name__ == "__main__":
    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_") and callable(f)]
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print("PASS", name)
        except Exception as exc:  # report every failure, then exit non-zero
            failed += 1
            print("FAIL", name, type(exc).__name__, exc)
    print("%d/%d passed" % (len(tests) - failed, len(tests)))
    sys.exit(1 if failed else 0)
