# P13 pre-registration v5: study-inclusion sensitivity of pooled prevalence

**DRAFT for freeze; no extraction or analysis has been performed.**
Paper: P13, GOSH browser application. Target journal: *Rheumatology Advances in Practice*. Date: 2026-10-28. **Freeze candidate: F1–F6 satisfied under the binding decision; not released.** No real-data gate has run.

The [analysis contract](supporting/ANALYSIS_CONTRACT_P13.md) and [verification specification](supporting/VERIFICATION_P13.md) are normative parts of this registration and must be released with it. [Evidence](supporting/EVIDENCE_P13.md), the [evidence/hash manifest](supporting/evidence_manifest_P13.json), and [v5 dispositions](V5_NOTES_P13.md) document its basis. They contain no extracted study rows.

## 1. Candidate and fixed fallback

Primary: Almutairi NA, Greenwood DC, Sivan M. *The prevalence of dysautonomia in chronic musculoskeletal pain: a systematic review and meta-analysis*. Rheumatology Advances in Practice. 2026;10(2):rkag034. DOI 10.1093/rap/rkag034; [archived article](supporting/evidence/primary/fulltext.xml); CC BY 4.0. Selection uses published target-journal placement, k = 17 and I² = 93%, supporting a question about study-combination sensitivity.

Mandatory fallback: Tang H, Singh BSM, Fong W. *Prevalence and factors associated with fatigue in patients with axial spondyloarthritis: a systematic review and meta-analysis*. Rheumatology Advances in Practice. 2023;7(3):rkad084. DOI 10.1093/rap/rkad084; [archived article](supporting/evidence/fallback/fulltext.xml); CC BY-NC 4.0. Published fatigue burden, target-journal placement, k = 30 and I² = 94.6% support its method-question fit. No calculated sensitivity informed either choice.

Order: **primary → fallback → stop**. Both source verdicts are **FEASIBLE-IMAGE**; supplied novelty screens identify no equivalent. Primary remains the proposed route. Both reproduction configurations are fixed before extraction in the normative [reproduction contract](supporting/REPRODUCTION_P13.md). Fallback activates only after its own feasibility, novelty, mapping and fixed-model eligibility are independently confirmed; otherwise stop. No numerical reproduction pass is claimed.

At a freeze decision, unresolved primary F1–F6 eligibility invokes that order. After release, source-mapping or reproduction failure also invokes it, using a fallback specification fixed before its extraction. At most one candidate receives a completed new analysis. Valid sensitivity or robustness results never trigger switching; delayed verification or app/R disagreement stays incomplete/unresolved.

The existing four-active-hour cap runs from the v3 handoff across both candidates, including setup, follow-up, extraction, verification coordination and drafting. Exclude waiting and unattended computation; log durations. Exhaustion stops work without resetting the allowance. Historical active time is not established. Before further implementation or extraction work, recover a documented conservative upper bound for active time since the v3 handoff, including both candidate routes, and subtract it from the original four-hour allowance. If no defensible remaining allowance can be established, stop under the effort cap; do not assign a new four-hour budget or treat missing time as zero. Log subsequent start/stop durations. Wu remains outside this plan.

## 2. Outcome and published target

| Item | Primary | Fallback |
|---|---|---|
| Outcome | Overall dysautonomia prevalence in chronic musculoskeletal pain | Overall fatigue prevalence in axial spondyloarthritis |
| Comparison | Single population; exclude healthy-control ratios and subgroups | Single population; exclude predictors and subtype contrasts |
| Published target | **64% (95% CI 51, 76; I² = 93%)** | **0.56 (95% CI: 0.49, 0.63; I² = 94.6%)** |
| Published k | **17** | **30** |
| Stated model | Random effects; Freeman–Tukey transformed proportion | Random effects |
| Stated software | **NOT STATED** | RStudio **v.2022.12.0**; statistical package/function and R version **NOT STATED** |

The papers do not state the remaining numerical conventions. Tang's transformation is NOT STATED in the supplied article/supplement; v5 therefore prospectively fixes raw proportions for its reproduction. These assumptions are not attributed to either paper. The fallback forest's **I² = 95%** remains distinct from the abstract's **I² = 94.6%**. Neither changes the gate. Log-versus-natural ratio pooling is inapplicable.

The new-analysis estimand is half-Freeman–Tukey prevalence in radians. Its DL model remains separate from the prospective REML reproduction gate.

## 3. Sources and eligibility

Primary: final Figure 1, rkag034.pdf page 5 / supp/rkag034f1.jpg, columns **Study**, **Total**, **Number with Dysautonomia**, **Prevalence % [95% CI]**. Counts and percentages/endpoints are printed as integers. Final Table 1, PDF page 4 / XML rkag034-T1, supplies identity and assessment context: **Study (author, year)**, **Medical diagnosis**, **Sample size, n**, **Method used**, **Subjective**, **Objective**.

Fallback: final Figure 2 / supp/rkad084f2.jpg, columns **Study**, **Fatigued**, **Total**, **Proportion**, **95%-CI**, **Weight**. Counts are integers; proportions/endpoints have two decimals. Weights are not inputs. rkad084_supplementary_data.docx Tables S1–S2 provide identity, population, fatigue tool and definition.

The v3 source screen established readable forest images and context tables; the six logged downloads still match their hashes. No P13 source is recorded blocked. Final forests control contributions, order, counts and estimates. The accepted primary supplement's overall Supplementary Figure 2 (PDF page 20) is corroboration only; the final supplement's Figure 2 is subjective-only. Never mix those locators.

After release, independently extract identity, order, selected assessment, directly printed integer x/n, printed prevalence/CI and field provenance. Preserve the reviews' selections and matched denominators; do not repeat their instrument/outcome-selection procedures. Require registered k, unique identifiable contributions and independence. Published overlap-exclusion policies support feasibility but do not certify every row.

Missing counts, ambiguous pairing/identity, conflicting versions or unresolved overlap fail the candidate. No inferred counts, unidentified-CI reconstruction, row omission/merging, alternative dataset or primary-study hunting. A row from one meta-analysis is used only for that meta-analysis. Image-reading risk carries into double extraction and verification.

Source-specific independence alert: the primary article's Limitations explicitly leave possible cohort overlap unresolved. Its general overlap-exclusion policy does not settle that warning. The registered independence condition must be resolved from the permitted review/supplement sources before the primary reproduction gate. If it remains unresolved, the primary fails eligibility and only the independently cleared, already specified fallback may proceed; otherwise stop. Do not assume independence from different assessment methods, matching pooled results, or legible forest columns. Do not omit or merge contributions.

## 4. Extraction and verification

Binding [MAHMOOD_DECISIONS.md](supporting/evidence/instructions/MAHMOOD_DECISIONS.md) item 4, copied exactly:

> Human verification: humans check headline rows, a seeded 5% of the other rows (at least 1), and only the fields still disputed after a third-model adjudication plus a fourth AI re-check (agy, different family). If the sample error is over 2%: a full AI re-extraction plus a human re-check of the headline rows. Packets are about 30 minutes or less; at most one per person per week across all papers (COAUTHOR_LOAD.md); Mahmood is in the rota; a packet not returned in 7 days is reassigned.

Codex and agy independently double-extract, blind to each other; verify different model families from actual logs. Adjudicate all discrepant fields with a third model, then re-check adjudicated fields with agy from a different family. Humans check only the binding scope.

Headline rows include every threshold flag and every tied maximum absolute estimate or I² contrast, with the union of app/R tied maxima. The normative verification supplement fixes seed **2026102813-HV**, SHA-256 row-key encoding, the 5% minimum-one sample, fixed initial error denominator, correction/rerun rules and packet accounting. Preserve the original sample through corrections; never resample to reset errors. No final classification before required checks finish.

## 5. Original-model reproduction gate

Before GOSH, reproduce in R the published pooled estimate and **both CI endpoints separately**. Inclusive tolerances remain **0.5 percentage points** for primary and **0.005 proportion units** for fallback. Never widen them. I² is descriptive.

[JOB.md](supporting/evidence/instructions/JOB.md) and Mahmood item 7 fix one prospective configuration per candidate, not the authors' unknown historical implementation. Exact source support, conflicting wording considered, every remaining choice and executable R definitions are in [REPRODUCTION_P13.md](supporting/REPRODUCTION_P13.md).

Both use **metafor 5.2.1**, inverse-variance random effects, intercept only, rma(method="REML", test="z", level=95, weighted=TRUE). Primary uses escalc(measure="PFT", xi=x, ni=n, add=0, to="none"), the half-Freeman–Tukey normalization, and **transf.ipft.hm using the harmonic mean of n**, targs=list(ni=n), for estimate and both endpoints, then ×100. Tang uses escalc(measure="PR", xi=x, ni=n, vtype="LS", add=0, to="none"), variance p(1−p)/n, and identity back-transformation. Its unbounded Wald CI is not clipped.

No continuity correction, omission, moderator, user weights, fixed tau², alternate optimizer or retry. Primary retains zero/all-event rows; Tang's resulting zero variance fails that candidate. Nonfinite values, warnings or nonconvergence fail closed. Fixed REML controls use the package's HE initialization, nonnegative tau², threshold 1e−5, 100 iterations and step adjustment 1. The reproduction supplement fixes all remaining conventions.

**NO switching model, transform, inverse or sample-size convention on gate failure; no model search.** Failure stops the primary, then permits only the independently cleared fallback under its already fixed configuration; otherwise stop. A fallback failure stops the study. Report failures; no new analysis for a failed candidate.

## 6. Exact new analysis and agreement

The full [analysis contract](supporting/ANALYSIS_CONTRACT_P13.md) preserves v3's formulas, arguments, capture requirements and every comparison.

R-only preprocessing: half-Freeman–Tukey y and v = 1/(4n+2), using metafor::escalc(measure="PFT", xi=x, ni=n, add=0, to="none"); retain zero/all-event rows. Validate integer 0 ≤ x ≤ n, n > 0 and independence.

App and independent R parse the same headerless y, sqrt(v), canonical-label payload with at least 17 significant digits; preserve source labels separately. R comparison uses parsed SE², archiving formula v separately.

App: pinned **gosh/index.html**, DL, linear axes, automatic x, I² 0–100; reassert after autosave. English tooltips are fixed for dependency validation. R: **4.6.0**, **metafor 5.2.1**, rma.uni(yi=y, vi=v, method="DL", test="z", level=95, weighted=TRUE), with DL re-estimated per subset. Singleton y is retained; Q/I²/tau² are zero. R-only 95% Wald intervals remain in radians. No inverse transformation for new-analysis outputs.

Primary: exact mode; 5,000 incidental preview draws; **131,071 nonempty subsets**, including singletons; 100 × 100 grid and type-7 quartiles. Require completed sampled=false/exact-streamed state, complete unique masks and full-precision exact/per_study output. Capture unchanged engine fit(mask) for every mask; reconcile with the page and membership-matched metafor::gosh output.

Fallback: sample mode, **50,000 draws**, no exact worker, pinned initial state **[0xdeadbeef, 0x12345678, 0xabcdef01, 0x87654321]**. Size is uniform over 2…30; membership is without replacement within draws. Preserve ordered members, occurrence order and duplicate draws. Capture the existing validation hook with snapshot/restore and URL-write suspension; refresh identical extras. Independently refit every occurrence in R. No rerolls, additional draws or deduplication.

Unrounded acceptance: **abs(app−R)/max(1,abs(R)) ≤ 10⁻⁹** except every I²-valued quantity uses **abs(app−R)/100 ≤ 10⁻⁹**. Compare every subset's estimate/Q/tau²/I², all registered summaries/contrasts, exact discrete memberships/counts/flags and all **10,000 primary grid cells**. Fallback median contrasts are mandatory. The supplement fixes grid boundaries, flattening and every field.

Reject missing/nonfinite/failed fits, stale inputs, cancellation, previews, incomplete coverage, empty inclusion groups and disagreement. Singleton normalization is the sole specified exception. Unresolved implementation states never count as robustness. Report both implementations.

## 7. New versus robust

Use equal subset/occurrence weights. Signed Δy is mean pooled estimate with a row included minus mean with it excluded; ΔI² is analogous. Flag if **|Δy| ≥ 0.10 radians OR |ΔI²| ≥ 10 percentage points**, inclusive, independently on unrounded app/R values.

Conditional on novelty, reproduction, verification and agreement, one or more flags constitute a **registered sensitivity finding**. No flags means **robust under the registered inclusion rule**; fallback wording is **robust under the registered 50,000-draw inclusion rule**, limited to those draws. Report all signed contrasts/flags and both maximum absolute contrasts with every tie. No clustering, visual subgroup selection, significance testing, deletion, clinical-importance inference or outcome switching.

## 8. Novelty and deviation

Europe PMC and OpenAlex replace Google Scholar under Mahmood's decision: Scholar showed "unusual traffic" on 2026-10-28 and was not bypassed. This is a recorded protocol deviation.

An equivalent applies GOSH/all-subsets heterogeneity analysis to the same review's overall outcome/contributions, regardless of software, estimator, sampling or thresholds. Confirmed equivalence invokes fallback/stop; unresolved potentially equivalent records block that candidate.

Supplied 2026-10-28 screens report no equivalent and empty flags for both candidates. Primary Europe PMC counts are 0/0/0; OpenAlex 1/1. Fallback Europe PMC metadata/retrieved/hitcount are **14/15/15**, preserved separately; OpenAlex 18/18. Both OpenAlex logs report complete=true. Do not sum cross-index counts.

Exact available queries and records are linked in [evidence](supporting/EVIDENCE_P13.md) and its manifest. Original citing-request URLs and complete record-level screening lists are unavailable; prior unsuccessful searches remain unassessed. No independent record-level rereview or guarantee about unindexed work is claimed. This disclosed coverage/audit limitation does not fail F2.

## 9. Static app evidence

Snapshot declaration: **14dc545bcba87a02158b2f445c28450e7eaf6b89**. Evidence cites each core file, function and SHA-256. All 28 direct script/stylesheet dependencies and required dynamic assets are archived and hashed. The four core GOSH pins match. F6 is static evidence only; browser tests remain unexecuted.

The build-info embedded identity remains **42a94da2110a02200d0b5bff4c56f636b9cbffa9**. Preserve both identities and actual byte hashes; runtime and Git ancestry are not certified. Optional app webR/companion replay paths are outside this registered route. Registered independent validation uses native R.

Original reproduction, PFT preprocessing, dependence validation, subset CIs, threshold classification, human-packet selection and the combined figure are R-only/external; do not advertise them as native app capabilities.

## Mandatory post-release, pre-analysis conditions

These remain compulsory and are not additional freeze criteria:

1. Complete and hash the specified code package; integrate the fixed original-model function and every retained implementation obligation in [V5_NOTES](V5_NOTES_P13.md). The supplied R gate module is unexecuted and is not the completed GOSH pipeline.
2. On pc2, run only generated **synthetic_*** fixtures marked **SYNTHETIC - not data** in their first line/column. Validate original-gate pass/fail/endpoints, PFT boundaries, full k=17 exact and k=30 sampled workloads, comparisons and refusal/lifecycle cases.
3. Establish actual app/R synthetic parity and runtime/browser dependency closure; archive environments, versions, logs and hashes.
4. Synchronize extraction kit, identity maps, verification logs and packet tooling to the released registration and its supplements.
5. Assign eligible P13 packets through the shared COAUTHOR_LOAD ledger, reserving a planned slot before sending; honor both the ISO-week cap and retained rolling-seven-day cap. Mahmood is eligible; Izataku remains unassignable pending the recorded authorship decision.

**Code must pass synthetic validation before any real-data reproduction gate.** Every post-release code change is a dated deviation, independent of real-data results. Mapping/independence and verification checks remain mandatory after release; never turn uncertainty into a pass.

## 10. Write-up and release

Produce 150–250 words plus one external figure: primary exact density or fallback fixed sampled scatter, with signed contrast strips in forest order, all rows and both threshold signs shown. No study-specific highlighting or data-dependent zoom. Label half-Freeman–Tukey radians and I² percent; distinguish exact/sample scope. Preserve the BCG example. Frame as "a re-analysis illustrating study-inclusion sensitivity of pooled prevalence"; report gates, classification, ties and agreement. Mahmood dictates the final paragraph. No clinical recommendations, priority or ranking claims.

V5 applies Mahmood item 7, verifies source wording, fixes PFT/harmonic-mean inverse for primary and PR for Tang, and archives exact evidence bytes. REDTEAM2 follows this job; no report or findings were supplied, so none are claimed resolved. No gate, verification or outcome definition is relaxed.

Freeze only when F1–F6 clear. Release this registration, normative supplements and available code in P13/ of **mahmood726-cyber/usecase-preregistrations**, recording hashes, commit, GitHub release URL/server-side UTC timestamp and Zenodo DOI. Neither release nor DOI exists in this package. Extraction waits for both. Archive verified extraction, logs, environments, lossless inputs/memberships, both outputs, failures and deviations. Every reported number must trace to published text or verified archived output. Preserve original numbers. No contact, login, paywall workaround or bot-check bypass.

**sha256 and UTC freeze time recorded at release**
