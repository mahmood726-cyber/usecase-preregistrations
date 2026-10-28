"""Write per-record screening ledgers (CSV) and yield summaries with Wilson 95% CIs. usage: python -I summarize.py"""
import csv, json, math, os, sys, collections, hashlib, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import screen, drive, decide

def wilson(x, n, z=1.959963984540054):
    if n == 0: return (None, None)
    p = x / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))

def cell(s):  # CSV formula-injection guard
    s = "" if s is None else str(s)
    return "'" + s if s[:1] in ("=", "+", "@", "\t", "\r") else s

out = {}
for p in ("P14", "P06"):
    frame = {r["rank"]: r for r in screen.load_frame(p)}
    st = drive.status_table(p); L = screen.read_ledger(p)
    done, n_elig_order, block = drive.first30_resolved(p)
    # contiguous fully-dispositioned prefix: ranks 1..R with no PENDING/ERROR
    R = 0
    for r in sorted(st):
        if r != R + 1 or st[r][0] in ("PENDING", "ERROR"): break
        R = r
    rows = []
    for r in range(1, R + 1):
        x = frame[r]; s, code = st[r]
        stage = code.split(":")[0]; e = L.get((r, stage)) or {}
        reason = e.get("reason", "")
        if stage in ("C", "D") and "facts" in L.get((r, "C"), {}):
            d = L.get((r, "D"))
            reason = decide.decide(p, screen.facts_for(L, r), d["d"] if d and not d["d"].get("_error") else None)[2]
        rows.append({"rank": r, "canonical_key": x["canonical_key"], "pmcid": x.get("pmcid"), "pubYear": x.get("pubYear"),
                     "journal": x.get("journal"), "title": x.get("title"), "index_licence": x.get("license"),
                     "final_status": s, "decided_at_stage": stage, "reason_code": code, "reason": reason})
    fn = os.path.join(screen.HERE, f"SCREENING_LEDGER_{p}.csv")
    with open(fn, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["rank"])
        w.writeheader()
        for row in rows: w.writerow({k: cell(v) for k, v in row.items()})
    n = len(rows); x = sum(1 for r in rows if r["final_status"] == "ELIGIBLE")
    unres = sum(1 for r in rows if r["final_status"] == "UNRESOLVED")
    lo, hi = wilson(x, n)
    N = len(frame)
    res = {"pilot": p, "frame_deduplicated": N, "screened_contiguous_prefix": n, "eligible": x, "unresolved": unres,
           "excluded": n - x - unres, "eligible_ranks": [r["rank"] for r in rows if r["final_status"] == "ELIGIBLE"],
           "yield": x / n if n else None, "yield_wilson95": [lo, hi],
           "projected_eligible_in_frame": round(x / n * N, 1) if n else None,
           "projected_eligible_in_frame_wilson95": [round(lo * N, 1), round(hi * N, 1)] if n else None,
           "upper_bound_if_all_unresolved_eligible": (x + unres) / n if n else None,
           "selected_ranks_seeded_order": [r["rank"] for r in rows if r["final_status"] == "ELIGIBLE"][:30],
           "stopping_rank": ([r["rank"] for r in rows if r["final_status"] == "ELIGIBLE"][29] if x >= 30 else None),
           "unresolved_within_selection_window": [{"rank": r["rank"], "code": r["reason_code"], "reason": r["reason"][:200]} for r in rows
               if r["final_status"] == "UNRESOLVED" and (x < 30 or r["rank"] < [q["rank"] for q in rows if q["final_status"] == "ELIGIBLE"][29])],
           "screened_beyond_stopping_rank": (n - [r["rank"] for r in rows if r["final_status"] == "ELIGIBLE"][29]) if x >= 30 else 0,
           "stopping_rule_met_30": done, "frame_exhausted": n == N,
           "reason_counts": dict(collections.Counter(r["reason_code"] for r in rows).most_common()),
           "ledger_csv": os.path.basename(fn), "ledger_csv_sha256": hashlib.sha256(open(fn, "rb").read()).hexdigest(),
           "computed_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "note": "Projection treats the screened ranks as a simple random sample of the frame (they are the first n of a seeded hash permutation); UNRESOLVED counted as not eligible."}
    out[p] = res
json.dump(out, open(os.path.join(screen.HERE, "YIELD_SUMMARY.json"), "w"), indent=1)
for p, r in out.items():
    print(p, {k: r[k] for k in ("screened_contiguous_prefix", "eligible", "unresolved", "yield_wilson95", "projected_eligible_in_frame", "projected_eligible_in_frame_wilson95")})
