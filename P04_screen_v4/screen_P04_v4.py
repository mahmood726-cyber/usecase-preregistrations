# P04-screen-v4: approved for freeze and release (Mahmood, relayed by dispatch, 2026-11-03); not yet released.
"""P04-screen-v4: the final P04 screen. Builds the v4 Stage S queue and validates the v4 Stage S log.

What this script does:
  * verifies the archived, released v3 inputs byte-for-byte (v3 script, v3 queue, v3 Stage F log,
    v3 Stage S log) against pinned sha256 values;
  * takes every F-PASS record of the v3 Stage F log, removes the five already full-screened in v3,
    and checks that exactly the four pinned records remain (v3 queue orders 25, 32, 37, 40);
  * re-uses the v3 gate rules and validators unchanged (imported from the archived v3 script).

What it never does: network access, new Stage F visits, re-screening of any v3 record, or selection by
itself. --build runs only with the public P04-screen-v4 release arguments and matching local sha256 values.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re

PAPER = "P04"
VERSION = "v4"
DRAFT = False  # Approved for freeze (Mahmood via dispatch, 2026-11-03); not yet released.
RELEASE_TAG = "P04-screen-v4"
RELEASE_URL = "https://github.com/mahmood726-cyber/usecase-preregistrations/releases/tag/" + RELEASE_TAG
PREREG_FILENAME = "PREREG_P04_screen_v4.md"

BASE = Path(__file__).resolve().parent
ARCHIVE = BASE / "supporting" / "v3_archive"
V3_FILES = {  # released P04-screen-v3 package bytes (script) and the v3 run outputs, pinned
    "screen_P04_v3.py": "91161f79715e7eb337d761fb1a5714c6c47e0305f5b5c8df5d065845b7d1c6e5",
    "queue_P04_v3.jsonl": "2a88570287edd5f180861075f7c7833bed8017163be75ff22f213c0b8ce6b03f",
    "STAGE_F_LOG_P04_v3.jsonl": "547574a44d3542c46facc5c39dc511df662cc845b94cc81e1650c6b683f34807",
    "STAGE_S_LOG_P04_v3.jsonl": "b0f430c2aed97be0cb5d011711956fc58b2808bb4e738ef4361e7ef5da7b8c0b",
}
V3_SCREENED = (4, 9, 12, 22, 24)      # v3 Stage S (N_S = 5), all FAIL or UNRESOLVED
V4_QUEUE_ORDERS = (25, 32, 37, 40)    # the remaining v3 F-PASS records, in v3 queue order
N_S_V4 = len(V4_QUEUE_ORDERS)         # 4: every remaining F-passer; nothing else is added (section 2)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def load_v3_module(path=None):
    path = Path(path or ARCHIVE / "screen_P04_v3.py")
    if sha256(path.read_bytes()) != V3_FILES["screen_P04_v3.py"]:
        raise ValueError("archived v3 script bytes do not match the released P04-screen-v3 script")
    spec = importlib.util.spec_from_file_location("screen_P04_v3_archived", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _jsonl(raw, label):
    if sha256(raw) != V3_FILES[label]:
        raise ValueError(label + ": bytes do not match the pinned v3 sha256")
    return [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]


def build_v4_queue_from_bytes(queue_raw, f_log_raw, s_log_raw, v3):
    queue = _jsonl(queue_raw, "queue_P04_v3.jsonl")
    f_log = _jsonl(f_log_raw, "STAGE_F_LOG_P04_v3.jsonl")
    s_log = _jsonl(s_log_raw, "STAGE_S_LOG_P04_v3.jsonl")
    errors = v3.validate_stage_f_log(queue, f_log, final=True)
    if errors:
        raise ValueError("archived v3 Stage F log fails its own validator: " + "; ".join(errors))
    v3_s_queue = v3.stage_s_queue(queue, f_log)
    errors = v3.validate_stage_s_log(v3_s_queue, s_log, final=True)
    if errors:
        raise ValueError("archived v3 Stage S log fails its own validator: " + "; ".join(errors))
    screened = tuple(r["v3_queue_order"] for r in s_log)
    if screened != V3_SCREENED or any(r["s_disposition"] == "PASS" for r in s_log):
        raise ValueError("v3 Stage S is not the archived five non-passing screens")
    by_order = {q["v3_queue_order"]: q for q in queue}
    passed = [r["v3_queue_order"] for r in f_log if r["f_disposition"] == "F-PASS"]
    remaining = tuple(o for o in passed if o not in screened)
    if remaining != V4_QUEUE_ORDERS:
        raise ValueError("remaining v3 F-passers %r differ from the pinned v4 queue %r" % (remaining, V4_QUEUE_ORDERS))
    rows = []
    for order in remaining:
        row = dict(by_order[order])
        row.update({"stage": "S", "screen_status": "UNSCREENED", "v4_stage_s_order": len(rows) + 1})
        rows.append(row)
    return rows


def build_v4_queue(archive=ARCHIVE):
    archive = Path(archive)
    v3 = load_v3_module(archive / "screen_P04_v3.py")
    rows = build_v4_queue_from_bytes((archive / "queue_P04_v3.jsonl").read_bytes(),
                                     (archive / "STAGE_F_LOG_P04_v3.jsonl").read_bytes(),
                                     (archive / "STAGE_S_LOG_P04_v3.jsonl").read_bytes(), v3)
    return rows, v3


def validate_v4_stage_s_log(s_queue, log, v3, final=True):
    """The v3 Stage S validator (gate order, terminal rule, cap, PASS thresholds), with the v4 queue."""
    errors = []
    if len(log) > N_S_V4:
        errors.append("more than N_S=%d v4 Stage S screens" % N_S_V4)
    return errors + v3.validate_stage_s_log(s_queue, log, final=final)


def check_release(args):
    """Local syntax/hash checks only; pc2 must verify the public release and its server time first."""
    if DRAFT:
        raise ValueError("DRAFT: not approved; no screening queue may be built")
    url = (getattr(args, "screen_release_url", None) or "").rstrip("/")
    if url != RELEASE_URL:
        raise ValueError("Supply the public screening release URL for " + RELEASE_TAG + " (v1-v3 releases cannot authorize v4)")
    doi = getattr(args, "screen_release_doi", None) or "PENDING"
    if not (doi == "PENDING" or re.fullmatch(r"https://doi\.org/10\.\d{4,9}/\S+", doi)):
        raise ValueError("Supply the screening release DOI as https://doi.org/... or PENDING")
    hashes = {}
    for label, path, expected in (("prereg", BASE / PREREG_FILENAME, getattr(args, "prereg_sha256", None)),
                                  ("script", Path(__file__).resolve(), getattr(args, "script_sha256", None))):
        actual = sha256(path.read_bytes())
        if not expected or actual != str(expected).lower():
            raise ValueError(label + ": local bytes do not match the supplied frozen sha256")
        hashes[label] = actual
    return {"screen_release_url": url, "screen_release_doi": doi, "local_sha256": hashes,
            "public_release_verified_by_script": False}


def release_output_dir(directory):
    chosen = Path(directory).resolve()
    if chosen == BASE or not chosen.is_relative_to(BASE):
        raise ValueError("Output directory must be a child of the script's directory")
    chosen.mkdir(parents=True, exist_ok=True)
    return chosen


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--print-constants", action="store_true")
    parser.add_argument("--build", action="store_true", help="Needs the public release arguments")
    parser.add_argument("--screen-release-url")
    parser.add_argument("--screen-release-doi")
    parser.add_argument("--prereg-sha256")
    parser.add_argument("--script-sha256")
    parser.add_argument("--output-dir")
    args = parser.parse_args(argv)
    if args.print_constants:
        print(json.dumps({"draft": DRAFT, "N_S_v4": N_S_V4, "v4_queue_orders": V4_QUEUE_ORDERS,
                          "v3_screened": V3_SCREENED, "v3_files": V3_FILES}, indent=1))
        return 0
    if not args.build:
        parser.error("Choose --print-constants or --build")
    try:
        release = check_release(args)
        if not args.output_dir:
            raise ValueError("Supply --output-dir (a child of the script's directory)")
        out_dir = release_output_dir(args.output_dir)
        rows, _ = build_v4_queue()
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    target = out_dir / "stage_s_queue_P04_v4.json"
    if target.exists():
        parser.error("Refusing to overwrite a previous v4 queue; preserve the run")
    payload = {"stage_s_queue": rows, "release": release, "v3_inputs_sha256": V3_FILES,
               "built_at_utc": datetime.now(timezone.utc).isoformat(), "note": "Nothing screened."}
    payload["queue_sha256"] = sha256(json.dumps(rows, ensure_ascii=False, sort_keys=True).encode("utf-8"))
    with target.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=1)
        handle.write("\n")
    print("Wrote %d UNSCREENED v4 Stage S rows to %s" % (len(rows), target))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
