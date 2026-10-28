# P12 v4 normative analysis and verification contract

Date: 2026-10-28. This file is part of the freeze candidate and must be released and hashed with [PREREG_P12_usecase.md](../PREREG_P12_usecase.md). It preserves the v3 detailed rules; implementation alignment remains mandatory after release and before real-data analysis. No study-level rows or real-data calculations are included.

Sections 2-7 below retain their numbering. References to sections 2-7 mean this contract; section 1 means the main preregistration. Both documents fix the same candidate, targets and gates. This file's detail is normative, not optional guidance. The exact Mahmood item 4 is reproduced in the main preregistration; these operational rules implement it without replacing it.

## 2. Fixed outcomes and estimands

| Specification | Primary | Fallback |
|---|---|---|
| Outcome | VAP incidence, original overall synthesis and trial-specific follow-up | Hospital length of stay, observational synthesis |
| Comparison | Probiotics/synbiotics versus placebo/usual care in mechanically ventilated adults | ICU rounding checklist versus no checklist |
| Published pooled estimate and 95% CI | RR 0.68 [0.55, 0.84] | SMD -0.19 [-0.36, -0.03] |
| k | 18 | 11 |
| Analysis scale/direction | Log RR; negative favours probiotics | SMD, checklist minus control; negative favours checklist |
| Original model stated | IV DL random effects; RevMan 5.4 | IV DL random effects; RevMan 5.4, Stata/MP 15.1 and RStudio 1.4.1106 named |
| Fixed reproduction attempt | Log RR, classic normal 95% CI | Printed SMD, classic normal 95% CI |

The exact CI algorithm is **NOT STATED** in either paper; both forests print a Z test. The primary's pooling transformation and the fallback's per-forest software assignment/SMD variant are **NOT STATED**. Under FREEZE_CRITERIA F3, use the single documented RevMan 5 default attempt specified above, with no search over models. These are declared defaults, not source-confirmed quotations. Source quotes and the official default reference are in [EVIDENCE_P12.md](EVIDENCE_P12.md).

For either outcome, the sensitivity estimand is beta0 = beta_r + tau * alpha_r, the expected effect as SE approaches zero under the extended random-effects model. It is distinct from the ordinary Egger intercept.

## 3. Sources and frozen input mapping

Primary: `P12_primary/supp/nutrients-14-01600-g003.jpg`, Figure 3 (publisher-PDF locator page 8), headers `Study or Subgroup` and `Risk Ratio / IV, Random, 95% CI`. Source-panel ID: `Cheema2022_Fig3_VAP`.

Fallback: `P12_fallback/supp/cc9-6-e1140-s001.pdf`, Figure S8, printed/PDF page 36, headers `Study or Subgroup` and `Std. Mean Difference / IV, Random, 95% CI`. Source-panel ID: `MacKinnon2024_FigS8_hospitalLOS`.

Both numerical forests are readable images with effects and CI endpoints printed to two decimals and no direct SE column. Extract their printed effect and both endpoints only after release. Preserve numerical strings and exact labels separately from derived inputs. With z = 1.959963984540054, primary yi = log(RR), sei = (log(U)-log(L))/(2*z); fallback yi = SMD, sei = (U-L)/(2*z). No additional rounding. Rounded CIs may fail reproduction.

Use the designated panel, source order, population, outcome and follow-up exactly. Main tables provide identity/context checks, not numerical substitutes. No counts/means reconstruction, plot-coordinate digitisation, primary-study retrieval, borrowed dataset, imputation, new continuity correction, SMD correction, arm splitting/combination, exclusion or alternate time point. Conflicting representations do not permit choosing whichever reproduces. A required missing/nonfinite value, unresolved mapping, or dependence incompatible with the original independent or already adjusted/combined contrast fails the gate. The app cannot detect shared controls or supply missing adjustments.

Use header-free direct `effect,SE,label` text in `#src`, decimal points and full precision. Labels are unique comma-free/newline-free safe row IDs, mapped to untouched printed labels. Verify exact k, order and values against reconciled R input. Avoid the permissive loader/bus. Transformations occur outside the app; exponentiate the primary estimate and both CI endpoints for RR presentation, never its SE.

## 4. Extraction and verification

After release, Codex and agy independently double-extract, blind to each other. Pin agy to a different model family from Codex and read back its actual model identity from its log line.

A third model adjudicates each discrepant field against the source. A fourth AI pass, agy using a different family from the adjudicator, re-checks every adjudicated field. Only disagreements remaining after this pass require human discrepancy adjudication. Record models, source locations and decisions.

Co-authors of P12 and/or Mahmood perform human verification, recording initials/date in `VERIFICATION_LOG.csv`:

- **Headline rows:** every row with normalized DL weight >=10%; every minimum/maximum-SE row; and every row whose deletion changes beta0 by >=0.10 analysis-scale units, changes its sign, CI null-exclusion status or section 7 classification, or produces a refusal.
- **Random sample:** among remaining rows, order by lowercase SHA-256 of UTF-8 `2026102812|P12|<row key>`; take the first `max(1, ceil(0.05 * n))` when n > 0. Row key is DOI, source panel, source-order index and printed study label; break hash ties lexically.
- **Unresolved fields:** all disagreements surviving the fourth AI pass.

A sampled row is erroneous if any required field or mapping differs from the source. If erroneous sampled rows/sample size exceeds 2%, repeat full AI double extraction and adjudication under the same rules, plus human re-check of headline rows only. Do not replace this with universal human checking. Corrections require rerunning gates and recomputing headline membership.

Budget five minutes per checked row plus five minutes administration: maximum five rows per approximately 30-minute packet; split larger workloads. Coordinate through `pipeline/COAUTHOR_LOAD.md` with P14/P06, including Mahmood in the rota. No co-author receives more than one packet weekly across papers. Reassign packets outstanding after seven days; never skip them.

Operational definitions preserve this verification specification. Normalize the review DOI to lowercase, retain the frozen panel ID, use a one-based integer source-order index, and normalize the label to Unicode NFC for the key only. Serialize those four components as a compact JSON array with no separator spaces and unescaped Unicode, then UTF-8 encode; use the review DOI, never a study DOI. Break hash ties by the serialized key. Freeze source-order IDs before sampling; take no sample when n = 0.

For deletion i, refit both models on the same retained dataset and compare its classification with the full-data classification. Compare deletion beta0 with full-data beta0 for the 0.10/sign/CI triggers. Include all tied SE extrema and every refused or indeterminate deletion. Use unrounded values, without a threshold epsilon. Keep the union of all headline rows ever flagged after corrections, tracking changed labels/keys through stable source IDs. Retain the original sample, numerator and denominator; never redraw to dilute an error. Check newly flagged or changed rows, retain the fourth-pass dispute requirement during escalation, and release no substantive result before verification completes.

## 5. Ordered reproduction gate

After release and AI reconciliation, resolve calculation-blocking disputes and run only the original-model reproduction in R. Require each of the point estimate and two CI endpoints separately within **0.005** of its section 2 target, with matching k, direction and null-exclusion category. Compare on RR scale for the primary and SMD scale for the fallback.

No real app load or limitmeta call precedes a passing recorded gate: the app calculates the sensitivity fit when run. On initial failure permit one source-documented transcription correction through the same adjudication workflow and one rerun of the unchanged gate. Otherwise stop that candidate and activate the fallback; fallback failure ends the analysis.

Do not alter printed source numbers, widen tolerance, choose alternative models or change input conventions to obtain agreement. Any new documentary evidence contradicting the frozen defaults requires a public pre-extraction amendment; it cannot justify post-result tuning.

A passing gate allows provisional limit/deletion fits solely to complete the planned analysis and verification targeting. Human checks and any mandated AI re-extraction follow. Source corrections invalidate prior results and require the gate and analyses to be rerun; this is verification escalation, not a tuning retry. After sensitivity results exist, unresolved correction/gate/implementation failure is indeterminate, without candidate switching.

## 6. Exact app, independent R and agreement

Use `ALLMETA/limit-ma/index.html`, ALLMETA = `C:/Users/User/ucjobs/allmeta_14dc545`, commit `14dc545bcba87a02158b2f445c28450e7eaf6b89`, with its hub/shared dependencies. Use automatic linear axes, DL and beta0; no moderators or subgroup exclusions. Normal CIs use estimate +/- 1.959963984540054 * SE. The comparison panel retains alpha 0.10; automatic unselected methods are provenance only, outside inference.

Independent R is **R 4.6.0, meta 8.5.0, metasens 1.5.3**, with metafor 5.2.1. Assert these versions and archive sessionInfo and installed function signatures/help. WebR's meta 8.3-0 is not a substitute.

```r
m <- meta::metagen(
  TE = yi, seTE = sei, studlab = label,
  sm = "GEN", common = FALSE, random = TRUE,
  method.tau = "DL", method.random.ci = "classic",
  method.tau.ci = "", prediction = FALSE,
  level = .95, level.ma = .95, backtransf = FALSE
)
# code/ must generate this receipt from the fixed gate, not a manual override.
stopifnot(gate_receipt$status == "GATE_PASS")
l <- metasens::limitmeta(
  m, method.adjust = "beta0",
  level = .95, level.ma = .95, backtransf = FALSE
)
```

GEN prevents automatic transformations of yi. Secondary outputs are tau-squared, alpha_r, beta_r, G-squared, Q.small and Q.resid. Use chi-square tests with 1 and k-2 degrees of freedom, respectively. Egger is `meta::metabias(m, method.bias="Egger", k.min=10)`, two-sided t with k-2 degrees of freedom. P-values are descriptive.

Archive main output and raw `AlmLimitPlusUI.snapshot().results` after comparison, with input identity and alpha. Run validation/comparisons before deletions, save those captures, then run every deletion and immediately capture main JSON and dedicated deletion CSV. A rerun clears deletion state and requires recapture. Main exports do not contain the comparison p-values.

The comparison-panel limit status is authoritative for app full-fit convergence; preserve main and R statuses beside it. Main-panel finite output does not override comparison/R refusal. Matching refusals mean agreement on failure and an indeterminate substantive result. Preserve internal REML refusals without changing optimizer, controls or estimator. A matched undefined secondary diagnostic is reported with its reason and alone does not invalidate an agreed finite primary fit. Unmatched/unclassified statuses or unresolved discrepancies prevent classification.

The manifest covers k; ordinary and beta0 estimates, SEs and both CI limits; DL tau-squared and tau; Q, alpha_r, beta_r, G-squared and beta0-minus-ordinary shift; Q.small/Q.resid and their df/p-values; Egger statistic/df/p-value; normalized DL weights; and every deletion's row ID, k, both refitted estimates/SEs/CIs, tau-squared, beta0 change and classification. Capture absent ordinary deletion SE/CIs with the pinned `AlmMaCore.pool(y,v,{method:'DL'})`, v = SE squared, and the same normal formula, independently of R. External audited code handles classification, verification targeting and sampling.

For every finite scalar, including derived/deletion quantities, require **abs(app-R)/max(1,abs(R)) <= 1e-9**. Match identities, order, lengths, statuses, df and classifications exactly. Retain raw messages and map refusals to invalid-input, singular-design, internal-REML-nonconvergence, nonfinite-fit or undefined-diagnostic; unknown reasons remain unresolved. Explicitly compare undefined fields; never silently omit them. Report both implementations and all refusals/discrepancies.

## 7. New versus robust

On analysis scale, theta is the unadjusted estimate and L is beta0. Sign has negative/zero/positive categories. A 95% CI is negative-excluding-zero if upper < 0, positive-excluding-zero if lower > 0, otherwise null-including, including boundaries at zero.

**New:** a sign change, a CI-category change, or abs(L-theta)/abs(theta) >= 0.20. **Robust:** same sign and CI category, with relative change < 0.20. With theta = 0, a sign/CI change is New; otherwise indeterminate because relative change is undefined. Undefined primary fits and unresolved implementation disagreement are indeterminate, never robust. Deletions use their own unadjusted fit and limit fit. Report attenuation or amplification explicitly. Thresholds are descriptive, not clinical-importance thresholds; report whichever outcome occurs.


## 8. Explicit implementation boundaries and fixed remaining settings

The preceding analysis, thresholds, statuses and verification scope are unchanged. These details close implementation descriptions without claiming functions that the app lacks.

- **R-only input preparation and presentation:** preserve source strings/labels, make the specified CI-to-SE and log transformations, create safe row IDs, check the source/contrast map and later exponentiate only primary estimates/CI endpoints. Original-image reading is an extraction task after release, not an app facility. No new adjustment is inferred from a design label.
- **R-only orchestration:** implement the ordered gate receipt, verification targeting, compact-JSON/NFC sampling, retained sample/error history, stable-identity headline union, new/robust/indeterminate classification and packet preparation. These are not capabilities of the pinned browser UI. To retain the app/R comparison manifest, apply the same prespecified derived rules separately to independently captured app scalars and R scalars; never populate an app fit field from an R fit.
- **R-only derived weights:** for each implementation separately use w_i = 1/(sei_i^2 + tau2), normalize by their sum, and compare the resulting app-derived and R-derived weights at the finite-scalar tolerance. Use the agreed weights for verification. Apply classification independently to each captured estimate/CI pair before requiring exact classification agreement.
- **App-based ordinary deletion uncertainty:** call the pinned JavaScript `AlmMaCore.pool(yi, vi, {method:'DL', knha:false, knhaFloor:false, level:0.95, pi:false})` on each retained dataset, vi = sei squared; do not override tau2. Capture its mu, se and tau2; form CI endpoints with z = 1.959963984540054 in JavaScript and retain them at full precision. This function exists, although the dedicated LOO export omits these fields. The surrounding capture/comparator must still be aligned and validated. R computes its own metagen uncertainty.
- **R-only publication composition:** the app's drawFunnel supplies the effect-versus-SE funnel/fitted curve. Compose the ordinary/limit CI inset and combined publication figure in R from archived, agreed outputs. The inset is not claimed as an existing app feature. Use SVG for the browser funnel export, linear automatic axes, and the unrounded analysis-scale estimates/95% CIs for the inset; labels identify the scale and both models. Styling must not change data, limits or fitted values.
- Comparison alpha remains 0.10. Leave binary measure/count controls empty, perform no subgroup/moderator/alternative-method inference, and use only the registered ordinary/beta0 outputs for the publication inset. The extra methods automatically computed in plus.js are archived as provenance, not eligible sensitivity choices. A comparison-panel exception or unavailable authoritative status prevents classification.
- Run R in a clean session without a preloaded workspace, custom meta settings or changed global defaults. The exact section 6 calls and pinned versions govern. Unspecified internal optimization controls remain the untouched defaults of these pinned packages, with no retries using different controls. No common-effect inference, HK correction, tau CI, prediction interval, selection model, continuity correction or arm reconstruction is added. Archive installed signatures/help before any real-data run; incompatibility is a stop condition requiring a dated, synthetic-validated implementation correction, never a choice made using real results.
- R full-fit fields include m$TE.random, m$seTE.random, m$lower.random, m$upper.random, m$tau2, m$tau and m$Q; l$TE.adjust, l$seTE.adjust, l$lower.adjust, l$upper.adjust, l$alpha.r, l$beta.r, l$G.squared, l$Q.small and l$Q.resid. Use `pchisq(Q.small, 1, lower.tail=FALSE)` and `pchisq(Q.resid, k-2, lower.tail=FALSE)`. Retain metabias statistic, df and pval. Repeat the same metagen/limitmeta settings on every retained deletion dataset. The independent full manifest remains mandatory, even where older oracle scripts capture fewer fields.
- Match signed numeric values, not formatted strings; preserve raw labels/messages separately. Undefined diagnostic fields must match as explicitly unavailable with an adjudicated reason, not as fabricated zeroes. Unknown reasons remain unresolved. Keep the main, comparison and R statuses separately; do not erase the main engine's lack of the comparison/deletion internal REML check.

## 9. Mandatory post-release, pre-analysis conditions

B1 from v3 becomes implementation alignment, kit synchronization and versioned packaging of the already fixed contract. B2 becomes actual synthetic runtime validation, including app/R parity, complete field/status comparison, export fidelity, browser closure and figure construction. None is asserted completed here. Do not launch any real-data reproduction until all relevant implementation/synthetic checks pass.

Fixtures must be generated afresh, named `synthetic_*` and marked "SYNTHETIC - not data" in their first line or column. Marking is metadata, never a fake numeric observation in the analysis. Exercise valid unequal-SE inputs, strict/header-free entry and safe labels, ratio/SMD scale preparation, invalid/nonfinite/zero-SE/equal-SE refusals, zero/null-touching and exact-threshold classifications, singular designs, internal REML refusals, undefined secondary diagnostics, ordinary and limit deletion uncertainty, refusal/unknown-reason comparison and persistence through corrections.

Test actual comparison capture, main JSON/CSV downloads, dedicated LOO CSV, escaping/null precision, input identity, comparison-before-deletion ordering, rerun invalidation/recapture, the funnel SVG and R-composed inset. Historical Python/KIT passes and archived oracle tests do not substitute.

Dependency closure includes direct resources, glossary fetches, stylesheet clones and the selected export route. A clean browser has no restored URL, autosave or bus input. Since index.html runs on load, ensure a controlled synthetic harness replaces any initial example before scripts execute and prevents example/hero actions and corpus replay. Record harness provenance and original app hashes; do not modify the pinned statistical functions. Never run bundled real examples or archived corpora. WebR and its optional missing packages are outside the desktop-R route.

The prior CODE/KIT directories are referenced in v3 but not supplied here. Obtain them from the coordinator, reconcile their documented key/capture/state differences, and version/hash the final bundle. Every code change after release is logged as a dated deviation independent of real-data results. Unexplained parity/export/identity failures block real analysis; matching refusals are retained as refusals under section 6, not successful numerical results.

Synchronize the extraction kit with the released documents and shared COAUTHOR_LOAD ledger. Reserve the ledger slot before sending any packet, retain the cross-paper ISO-week cap and reassign overdue packets. No packet is assigned in this job. The GitHub release and Zenodo DOI remain prerequisites for extraction.
