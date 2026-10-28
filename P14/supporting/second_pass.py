"""AM-S8 second pass on UNRESOLVED C:NONINDEPENDENT records (pre-specified in both drafts, 2026-10-28).
Codex transcribes ONLY the row labels (and any arm / shared-control annotations) of the trials contributing to the
designated pooled result. Independence is then decided deterministically here; the result is written as ledger
stage "E" and applied through screen.facts_for, so decide.py and stage D treat it like any other fact.
usage: python -I second_pass.py <pilot> [workers]"""
import concurrent.futures as cf, json, os, re, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path: sys.path.insert(0, HERE)
import screen, drive, stage_d

from indep import norm_label, independence  # single source for the AM-S8 rule

RULES = """# AM-S8 second pass: row labels only
`target.json` names the review's designated synthesis and where its per-study data are. Look at the attached
forest-plot image(s) (or the named table in paper.txt if the data are in a table). Identify the rows that
contribute to the DESIGNATED pooled result (right outcome, comparison, time point).
Transcribe ONLY: each contributing row's study label exactly as printed (e.g. "Smith 2010a"), and any printed
annotation that marks an arm, dose, subgroup of the same trial or a shared/split control. Do NOT transcribe any
number from the plot other than what is part of the label (no estimates, CIs, weights, events, totals, p, I²).
Return `source_found` yes/no, `source` (figure/table used), `labels` (list, in printed order), `annotations`
(list; empty if none), `note` (<=40 words).
"""
SCHEMA = {"type": "object", "additionalProperties": False, "required": ["source_found", "source", "labels", "annotations", "note"],
          "properties": {"source_found": {"type": "string", "enum": ["yes", "no"]}, "source": {"type": "string"},
                         "labels": {"type": "array", "items": {"type": "string"}}, "annotations": {"type": "array", "items": {"type": "string"}},
                         "note": {"type": "string"}}}

def run_one(p, L, rank):
    f = L[(rank, "C")]["facts"]
    rdir = os.path.join(HERE, p, "ft", f"r{rank:05d}")
    edir = os.path.join(rdir, "stage_e"); os.makedirs(edir, exist_ok=True)
    rec = json.load(open(os.path.join(rdir, "record.json"), encoding="utf-8"))
    z, url = stage_d.fetch_zip(rdir, rec["pmcid"])
    imgs = []
    if z is not None:
        for n in stage_d.pick_images(rdir, z, f["per_study_location"])[:8]:
            out = os.path.join(edir, os.path.basename(n)); open(out, "wb").write(z.read(n)); imgs.append(out)
    shutil.copy(os.path.join(rdir, "paper.txt"), edir)
    open(os.path.join(edir, "RULES_E.md"), "w", encoding="utf-8").write(RULES)
    json.dump(SCHEMA, open(os.path.join(edir, "schema_e.json"), "w"))
    json.dump({k: f[k] for k in ("designated_outcome", "designated_comparison", "designated_timepoint", "k_designated", "per_study_data", "per_study_location")},
              open(os.path.join(edir, "target.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    extra = []
    for im in imgs: extra += ["-i", im]
    res, err = screen.run_codex(edir, "Read RULES_E.md and target.json (and paper.txt if the data are in a table); inspect the attached images. Answer per RULES_E.md as JSON matching the output schema.",
                                os.path.join(edir, "schema_e.json"), timeout=1200, extra=extra)
    if err: return {"rank": rank, "stage": "E", "decision": "ERROR", "reason_code": err, "reason": err}
    ind, why = independence(res, f.get("k_designated"))
    return {"rank": rank, "key": L[(rank, "C")]["key"], "stage": "E", "decision": {"yes": "MET", "no": "NOT_MET", None: "UNRESOLVED"}[ind],
            "reason_code": "AM-S8", "reason": why, "independence": ind, "e": res, "images_used": [os.path.basename(i) for i in imgs]}

def main():
    p = sys.argv[1]; workers = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    L = screen.read_ledger(p); st = drive.status_table(p)
    todo = [r for r, v in sorted(st.items()) if v == ("UNRESOLVED", "C:NONINDEPENDENT")
            and ((r, "E") not in L or L[(r, "E")]["decision"] == "ERROR")]
    print(p, "second-pass todo", len(todo), flush=True)
    with cf.ThreadPoolExecutor(workers) as ex:
        for e in ex.map(lambda r: run_one(p, L, r), todo):
            screen.append(p, e); print("E", e["rank"], e["decision"], e["reason"][:80], flush=True)

if __name__ == "__main__":
    main()
