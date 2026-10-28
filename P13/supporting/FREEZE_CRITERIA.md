# Freeze criteria (pc2 coordinator decision, 2026-10-28; Mahmood: "push hard", no gate shortcuts)

A pre-registration may be frozen and released when ALL of the following hold. These are the protocol's own gates. Nothing here relaxes them.

**F1. Feasible chosen candidate.** Its SOURCE_CHECK verdict is FEASIBLE or FEASIBLE-IMAGE: every input is printed in a permitted open source and is readable. FEASIBLE-IMAGE carries its image-reading risk into double extraction and verification.

**F2. Novelty.** The Europe PMC and OpenAlex checks found no equivalent prior re-analysis; the Scholar substitution is recorded as a deviation. A coverage limitation, such as a partial citing-works list, is DISCLOSED in the prereg. It does not block the freeze.

**F3. Original model fixed in advance.** Either the original model is stated in the paper, or the prereg fixes exactly ONE reproduction configuration, chosen before any data from the paper's stated software and that software's defaults, with every remaining choice named. There is no model search. If the gate fails under that single configuration, the stop rule applies: primary, then fallback, then stop. A model that is NOT STATED is handled by this rule. It is not a reason to refuse to freeze.

**F4. Analysis and outcomes fully specified.** The exact analysis (app and R), every option, the agreement tolerances, and numeric definitions of new versus robust. No degree of freedom is left open that could be decided after seeing data.

**F5. Verification spec.** It is copied exactly from MAHMOOD_DECISIONS.md item 4.

**F6. App capability evidenced statically.** The pinned app code implements the registered app analysis, cited by file, function and sha256. Anything not implemented is labelled R-only.

These are NOT freeze criteria. Each is a **mandatory post-release, pre-analysis condition**, and the prereg lists it as such:
- running the analysis code on synthetic fixtures;
- runtime parity between the app and R on synthetic fixtures;
- browser dependency closure;
- syncing the extraction kit to the frozen prereg;
- assigning COAUTHOR_LOAD packets.

**The code must pass synthetic validation before any real-data reproduction gate is run.** Any code change after release is logged as a dated deviation and never depends on real-data results.

Fallback: the fallback's own feasibility and novelty status is stated honestly. If the fallback is not yet cleared, the prereg says that the fallback activates only if it clears those checks first, and otherwise the study stops. This does not block freezing the primary route.

**BLOCKERS file:** list ONLY failures of F1 to F6, or write the single line `NONE`.
