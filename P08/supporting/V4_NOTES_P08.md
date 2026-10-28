# P08 v3 → v4 freeze review — 2026-10-28

**BLOCKERS verdict: NONE.** Veltkamp is selected primary; Liu is the conditional fallback. This package is a draft for freeze, not a published preregistration or a runtime validation pass.

JOB.md, JOB_RULES.md, V4.md and FREEZE_CRITERIA govern this task. Historical TASK_COMMON “no files/full protocol in final” instructions are superseded by the current out-only job. Files were read through Python and all written files are under out/.

## Correction before study-level extraction or analysis

V3 called an unstated original model a primary feasibility failure and selected Liu. That was a criteria misapplication: F1 permits FEASIBLE-IMAGE, and F3 permits exactly one advance-fixed reproduction configuration with a stop rule. It was not a numerical reproduction failure.

V4 restores Veltkamp on its readable source evidence. Its original package, estimator, CI construction and pooling scale remain NOT STATED. We choose one R/metafor natural-scale REML/z configuration; we do not attribute that configuration to the authors. The printed pooled intervals motivate a declared natural-scale assumption, not trial-and-match fitting. No log-scale/alternative estimator trial is allowed. Failure means primary → cleared fallback → stop.

This is a correction made before study-level data were extracted or analysed and before any fitted results existed. It does not choose a candidate on results. All original point estimates and CIs remain unchanged.

## Each v3 blocker

| V3 item | F1–F6 assessment | V4 action |
|---|---|---|
| B1: missing REDTEAM and APP reviews | A missing job artifact is not itself an F criterion; its substantive gaps must be addressed | Performed V4 source-number, selection/gate, app-path, implementation and dependency reviews. SOURCE_CHECK, APP_CHECK and these notes supply this job's findings without inventing earlier report IDs or an independent-review claim. |
| B2: absent code and synthetic validation | Exact methods/options/comparison contract matter for F4; executing validation is explicitly post-release | Added fixed R reference and full-precision JS capture; specified remaining runner/diagnostic requirements. Synthetic R/browser/kit validation and runtime parity move to the mandatory post-release section. R/JS were not run here. |
| B3: stale/incompletely validated kit | Kit synchronization is explicitly post-release | Inspected historical codebooks/headline rules; recorded incompatible primary “no defaults” and fallback FE instructions. Incorporated a v4 verification/kit contract; source fields must retain NOT STATED separately from our assumptions. Full kit synchronization and runtime validation remain mandatory. |
| B4: Liu duration/assessment and independence mapping | Unresolved fallback eligibility, not primary F1 failure | Retained as a hard activation condition. Follow-up cannot silently become treatment duration; unresolved mapping means Liu cannot activate and the study stops. Primary independence/complete-case checks remain post-release gates. |
| B5: Liu profile eligibility | Does not undermine Veltkamp's target-journal profile | Retained a required source-based profile decision or explicit dated protocol deviation before Liu activation. Candidate approval/citation counts do not invent a threshold or waive the condition. |
| B6: incomplete novelty audit trail | F2 allows disclosed coverage limitations | Retained successful pc2 Europe PMC/OpenAlex findings and all counts/flags. Disclosed missing full citing lists/dispositions and unsuccessful supplemental PubMed access. No equivalent has been demonstrated. Liu's two query-hit dispositions remain conditional; no false exhaustive-clearance claim. |
| “Primary failure retained for audit”: unstated model | Resolvable F3 issue, not F1 failure | Corrected as above; primary FEASIBLE-IMAGE, one fixed configuration, strict stop rule. |

## Explicit F1–F6 verdict

- **F1 PASS:** primary ratio/CI image fields and text moderator fields are available/readable. Double extraction carries image risk. Complete-case numerical eligibility is not asserted before release.
- **F2 PASS with disclosed coverage limits:** supplied pc2 checks identified no equivalent analysis; Scholar substitution and incomplete audit trail are disclosed. Any confirmed equivalent excludes the candidate.
- **F3 PASS:** one natural-scale REML/z R/metafor configuration; all unstated choices named as assumptions, no model search, both original summaries required.
- **F4 PASS at specification level:** both routes, numeric eligibility, variances, estimators/inference, controls, model order, parsers, exact p capture and comparison tolerances fixed. R-only functions and outstanding harness work labelled honestly. No runtime pass claimed.
- **F5 PASS:** MAHMOOD_DECISIONS item 4 copied verbatim into the prereg. Operational verification retains every v3 threshold, all ties, exclusions and scheduling rule.
- **F6 PASS statically:** file/function/line/SHA-256 evidence supports ML/z multiple-moderator and PM/floored-HK single-moderator analyses. R-only tasks are labelled.

Therefore BLOCKERS_P08.md contains only `NONE`.

## Additional findings resolved or disclosed

1. Direct source verification confirms the primary HR/OR and fallback CRP pooled point/CIs and Liu “Ten studies.” V3's “40 cohorts” was not independently verified as a printed outcome count. It is not passed forward as certified k; no original paper number is changed. All quantitative k gates remain.
2. The real app path is `meta-regression/index.html` under ALLMETA. Core hashes match PIN.txt.
3. Direct scripts/styles, hub assets, glossary variants and PDF-export dependency are present. Optional live webR bundle/manifest are absent. The desktop-R comparison does not depend on live webR; runtime dependency closure remains untested.
4. Single-panel parsing can silently skip/accept malformed numeric strings. Require strict prevalidation, ten accepted rows and matching identities/values, not only a displayed k.
5. The public fallback results object omits slope p. The included capture uses the pinned t-tail functions and browser fit quantities, not rounded cards or R substitution.
6. The page auto-runs built-in examples. Runtime validation must replace defaults before scripts execute and clear restoration state, using only marked synthetic fixtures.
7. Exact section 7 new-versus-robust definitions are preserved from v3; no gate, 0.005 tolerance, app/R tolerance or verification scope is weakened.

## Mandatory post-release, pre-analysis conditions

- Complete the orchestration, comparison, deletion and verification runner before any real-data gate. For the fallback, capture both intercept and duration coefficient estimates, SEs and CI endpoints; compute each coefficient's t as coefficient/SE and its two-sided p with the frozen browser tTwoSidedP routine and df=k−2. Capture tau², q and df. Obtain the corresponding independent R quantities under the registered PM/adhoc model, including q=max(1,RSS/(k−2)) using residuals and weights from that fit, and df=k−2. Compare every required quantity at the registered tolerances and require exact row identity/order, term names, counts and classifications. A missing required field fails comparison. Ancillary permutation, QE and R² outputs do not replace required targets or enter classification. Exercise the complete path, both reproduction configurations, deletion fits, parsing/refusal paths and verification logs on marked synthetic fixtures with R 4.6.0/metafor 5.2.1. Record post-release code changes as dated deviations independent of real-data results. *(Replaced pre-freeze per REDTEAM2 RT2-01.)*
- Pass synthetic app/R parity and browser closure on the registered paths, including full-precision p capture, parsing, export and refusal boundaries. Optional live webR remains unavailable unless separately supplied; it is not registered.
- Synchronize and validate all kit schemas, prompts, codebooks, diagnostics and VERIFICATION_LOG.csv; no legacy FE/default-identification instruction may govern v4.
- Reserve human packets using the shared cross-paper ledger and exact caps; record actual independent/different-family AI logs. Binary S extrema retain all primary rows.
- Verify source hashes/identity/independence and extract only after the separate public P08 GitHub release plus Zenodo archival DOI exist. Release time/hash are not claimed here.
- If primary fails, resolve all conditional Liu source-duration/assessment/independence, profile and novelty issues before activating it; otherwise stop.
- Run quantitative eligibility and strict reproduction only after code validation; new analyses follow reproduction, and both app/R outputs must agree. Image rounding may fail the gate. Corrections are source-verified; post-release code changes are dated, synthetically validated deviations independent of real-data results.

No author contact, co-author message, ledger mutation, publication, clinical extraction or real-data analysis was performed.

## Artifact checks

supporting/audit_v4.py performs Python-only static checks of pooled-summary text, direct asset presence, supplied pins, exact binding verification text, unchanged v3 outcome definitions, supporting links and the ≤3,000-word limit. FILE_HASHES_P08.json records the final word count (Python whitespace split, including headings/tables/code), hashes and explicit NOT RUN runtime status. It is not a release timestamp or numerical-analysis result.
