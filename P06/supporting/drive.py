"""Run screening in seeded rank order, in chunks, until 30 records are ELIGIBLE with every lower-ranked record
finally dispositioned (no PENDING/ERROR), or the frame is exhausted. usage: python -I drive.py <pilot> [chunk] [workers]"""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import screen, decide

def status_table(p):
    L = screen.read_ledger(p)
    ranks = sorted({r for r, _ in L})
    out = {}
    for r in ranks:
        a = L.get((r, "A")); b = L.get((r, "B")); c = L.get((r, "C")); d = L.get((r, "D"))
        if a["decision"] == "EXCLUDE": out[r] = ("EXCLUDE", "A:" + a["reason_code"]); continue
        if not b: out[r] = ("PENDING", "B"); continue
        if b["decision"] == "EXCLUDE": out[r] = ("EXCLUDE", "B:" + b["reason_code"]); continue
        if b["decision"] == "ERROR": out[r] = ("ERROR", "B"); continue
        if not c: out[r] = ("PENDING", "C"); continue
        if c["decision"] == "ERROR": out[r] = ("ERROR", "C:" + c["reason_code"]); continue
        if "facts" not in c: out[r] = (c["decision"], "C:" + c["reason_code"]); continue
        s, code, _ = decide.decide(p, screen.facts_for(L, r), d["d"] if d and not d["d"].get("_error") else None)
        if s == "PENDING_D": out[r] = ("PENDING", "D"); continue
        out[r] = (s, ("D:" if d else "C:") + code)
    return out

def first30_resolved(p):
    st = status_table(p); n = 0
    for r in sorted(st):
        s = st[r][0]
        if s in ("PENDING", "ERROR"): return False, n, r
        if s == "ELIGIBLE":
            n += 1
            if n == 30: return True, n, r
    return False, n, None

if __name__ == "__main__":
    p = sys.argv[1]; chunk = int(sys.argv[2]) if len(sys.argv) > 2 else 150; w = sys.argv[3] if len(sys.argv) > 3 else "2"
    nframe = sum(1 for _ in open(os.path.join(screen.FRAMES, f"{p}_frame_ordered.jsonl"), encoding="utf-8"))
    hi = max([r for r, _ in screen.read_ledger(p)] or [0])
    while True:
        hi = min(hi + chunk, nframe)
        for attempt in range(2):  # second pass retries ERROR rows once
            subprocess.run([sys.executable, "-I", os.path.join(screen.HERE, "screen.py"), p, str(hi), w], check=True)
            subprocess.run([sys.executable, "-I", os.path.join(screen.HERE, "stage_d.py"), p, w], check=True)
        done, n, at = first30_resolved(p)
        print(f"[{p}] screened to rank {hi}: eligible-in-order={n} done={done} blocking_rank={at}", flush=True)
        if done or hi >= nframe:
            break
        if at is not None:
            # a lower-ranked record is still PENDING/ERROR after a retry: stop and surface it instead of spinning
            st = status_table(p)
            if st[at][0] == "ERROR" or (st[at][0] == "PENDING" and at <= hi):
                print(f"[{p}] STOP: rank {at} unresolved after retry: {st[at]}", flush=True); break
