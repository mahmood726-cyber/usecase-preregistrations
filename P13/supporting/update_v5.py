"""Update active v5 registration from supplied v4; no statistical execution."""
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]
V4=OUT.parent/"C_P13_V4/out"
p=(V4/"PREREG_P13_usecase.md").read_text(encoding="utf-8")
changes={
"pre-registration v4:":"pre-registration v5:",
"**BLOCKERS: F3 remains; do not freeze or extract.**":"**Freeze candidate: F1–F6 satisfied under the binding decision; not released.**",
"[dependency/hash manifest](supporting/browser_dependencies_P13.json)":"[evidence/hash manifest](supporting/evidence_manifest_P13.json)",
"[v4 dispositions](V4_NOTES_P13.md)":"[v5 dispositions](V5_NOTES_P13.md)",
"[DOI](https://doi.org/10.1093/rap/rkag034)":"DOI 10.1093/rap/rkag034; [archived article](supporting/evidence/primary/fulltext.xml)",
"[DOI](https://doi.org/10.1093/rap/rkad084)":"DOI 10.1093/rap/rkad084; [archived article](supporting/evidence/fallback/fulltext.xml)",
"Primary remains the proposed route, but its original-model configuration is unresolved. Fallback also lacks a cleared reproduction configuration. Fallback activates only after its own feasibility, novelty and fully fixed original-model configuration clear; otherwise stop. Its incomplete clearance does not independently block a cleared primary.":"Primary remains the proposed route. Both reproduction configurations are fixed before extraction in the normative [reproduction contract](supporting/REPRODUCTION_P13.md). Fallback activates only after its own feasibility, novelty, mapping and fixed-model eligibility are independently confirmed; otherwise stop. No numerical reproduction pass is claimed.",
"Specific weighting, tau² estimator, pooled-CI method, variance, inverse/normalization and boundary conventions are unstated; fallback transformation is also unstated.":"The papers do not state the remaining numerical conventions. Tang's transformation is NOT STATED in the supplied article/supplement; v5 therefore prospectively fixes raw proportions for its reproduction. These assumptions are not attributed to either paper.",
"It does not supply the original reproduction model.":"Its DL model remains separate from the prospective REML reproduction gate.",
"Binding MAHMOOD_DECISIONS.md item 4":"Binding [MAHMOOD_DECISIONS.md](supporting/evidence/instructions/MAHMOOD_DECISIONS.md) item 4",
"All 28 direct script/stylesheet dependencies and all 11 previously missing assets exist; supplied GOSH pins match. Seven relevant hub browser test files exist, unexecuted.":"All 28 direct script/stylesheet dependencies and required dynamic assets are archived and hashed. The four core GOSH pins match. F6 is static evidence only; browser tests remain unexecuted.",
"Optional webR/native reproduction paths remain unavailable.":"Optional app webR/companion replay paths are outside this registered route.",
"1. Complete and hash the specified code package, preserving fail-closed original-model behavior until F3 is resolved; apply every v3 B4 alignment item in V4_NOTES.":"1. Complete and hash the specified code package; integrate the fixed original-model function and every retained implementation obligation in [V5_NOTES](V5_NOTES_P13.md). The supplied R gate module is unexecuted and is not the completed GOSH pipeline.",
"Exact available queries and records are archived in the evidence/manifest.":"Exact available queries and records are linked in [evidence](supporting/EVIDENCE_P13.md) and its manifest.",
"V4 records pre-data reclassification under FREEZE_CRITERIA, exact verification wording, preserved normative supplements and refreshed dependency hashes. No gate or outcome definition is relaxed.":"V5 applies Mahmood item 7, verifies source wording, fixes PFT/harmonic-mean inverse for primary and PR for Tang, and archives exact evidence bytes. REDTEAM2 follows this job; no report or findings were supplied, so none are claimed resolved. No gate, verification or outcome definition is relaxed."
}
for a,b in changes.items():
    assert a in p,a
    p=p.replace(a,b)
a=p.index("F3 permits exactly one prospective configuration")
b=p.index("## 6. Exact new analysis",a)
p=p[:a]+"""[JOB.md](supporting/evidence/instructions/JOB.md) and Mahmood item 7 fix one prospective configuration per candidate, not the authors' unknown historical implementation. Exact source support, conflicting wording considered, every remaining choice and executable R definitions are in [REPRODUCTION_P13.md](supporting/REPRODUCTION_P13.md).

Both use **metafor 5.2.1**, inverse-variance random effects, intercept only, rma(method="REML", test="z", level=95, weighted=TRUE). Primary uses escalc(measure="PFT", xi=x, ni=n, add=0, to="none"), the half-Freeman–Tukey normalization, and **transf.ipft.hm using the harmonic mean of n**, targs=list(ni=n), for estimate and both endpoints, then ×100. Tang uses escalc(measure="PR", xi=x, ni=n, vtype="LS", add=0, to="none"), variance p(1−p)/n, and identity back-transformation. Its unbounded Wald CI is not clipped.

No continuity correction, omission, moderator, user weights, fixed tau², alternate optimizer or retry. Primary retains zero/all-event rows; Tang's resulting zero variance fails that candidate. Nonfinite values, warnings or nonconvergence fail closed. Fixed REML controls use the package's HE initialization, nonnegative tau², threshold 1e−5, 100 iterations and step adjustment 1. The reproduction supplement fixes all remaining conventions.

**NO switching model, transform, inverse or sample-size convention on gate failure; no model search.** Failure stops the primary, then permits only the independently cleared fallback under its already fixed configuration; otherwise stop. A fallback failure stops the study. Report failures; no new analysis for a failed candidate.

"""+p[b:]
(OUT/"PREREG_P13_usecase.md").write_text(p,encoding="utf-8",newline="\n")
(OUT/"BLOCKERS_P13.md").write_text("NONE\n",encoding="utf-8",newline="\n")
print("v5 main registration words:",len(p.split()))
