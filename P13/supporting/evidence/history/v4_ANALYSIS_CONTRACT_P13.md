# P13 v4 normative analysis contract

This supplement is part of the frozen registration, not optional implementation advice. The v3 new-analysis, agreement, classification and figure rules below are retained verbatim. Section references point to the same-numbered sections of the main registration. No real data were extracted or analysed.

## 6. Registered new analysis and agreement contract

### Input and models

R-only preprocessing:

y_i = 0.5 × {asin[sqrt(x_i/(n_i+1))] + asin[sqrt((x_i+1)/(n_i+1))]},
v_i = 1/(4n_i+2).

Use `metafor::escalc(measure="PFT", xi=x, ni=n, add=0, to="none")`. Retain zero/all-event contributions; validate integer 0 ≤ x ≤ n, positive n, finite y, finite positive v and independence. Do not add a continuity correction.

Write headerless **y, sqrt(v), label** lines with at least 17 significant digits and safe canonical labels **S001, S002, …**. Preserve exact source labels in a separate identity map; never strip punctuation to satisfy the parser. Synthetic payloads retain the required first-line/column marker through a synthetic label prefix. App and R comparison must parse the **same serialized file**; R comparison variance is parsed SE squared, with formula-derived v archived separately. Verify every imported value, label, order and count; reject omissions/coercion.

Run **gosh/index.html relative to the pinned allmeta root**, locally C:/Users/User/ucjobs/allmeta_14dc545/gosh/index.html. Set **DL**, linear axes, I² range **0–100**, automatic x limits. Reassert settings after autosave; re-estimate DL tau² for every subset. App computations have no native PFT/inverse, covariance/dependence handling, subset CI/test or threshold classifier.

Independent R: **R 4.6.0; metafor 5.2.1**; log actual runtime versions and sessionInfo. Fit `rma.uni(yi=y, vi=v, method="DL", test="z", level=95, weighted=TRUE)` using parsed SE² as v. Singleton estimate = y; Q = I² = tau² = 0. R-only normal 95% Wald intervals stay on the radian scale. No new-analysis inverse transformation is planned.

### Primary exact run

Set enum-mode="exact"; incidental preview draws **5,000**. Enumerate **131,071** nonempty subsets, including singletons; 100 × 100 density grid; type-7 quartiles. Require completed **sampled=false**, **enumeration="exact-streamed"**, n_subsets=expected_subsets=131071 and grid sum 131071. Use full-precision `_almLastGosh().exact` and its per_study output, never the preview or sampled extras.

Capture `AlmGoshExactEngine.createEngine(y,se,"DL",{gridX:100,gridY:100}).fit(mask)` for masks 1…131071, with bit j−1 identifying source-order row j. Archive memberships and estimate/I²/Q/tau²; reconcile their summaries with the completed page. The ordinary __almGoshValidationRun suppresses exact mode and cannot establish primary coverage.

R uses `gosh(fit, subsets=131071, parallel="no", progbar=FALSE)`. Derive masks from its inclusion matrix; match by membership, not row position. Require complete unique coverage; per-study group counts are 65,536 included / 65,535 excluded (design counts).

### Fallback sampled run

Set enum-mode="sample", **50,000 draws**, no active exact worker. Keep the pinned generator's initial state **[0xdeadbeef, 0x12345678, 0xabcdef01, 0x87654321]**. Subset size is uniform over 2…30, membership without replacement within a draw; retain duplicate draws.

Capture `__almGoshValidationRun(headerlessText,"DL",50000,{x:[null,null],y:[0,100]})` with snapshot/restore and alm.urlState.withoutWrites, following plus.js. Archive occurrence index, ordered members and raw fits. Refresh extras on identical inputs/settings; archive AlmGoshPlus.state and verify its draws match. R refits every occurrence in original member order with the specified rma.uni model; no deduplication or alternative sampler. No rerolls, seed changes or extra draws after inspection. An empty inclusion group is unresolved.

### Exact numerical acceptance

Use unrounded values: **abs(app−R)/max(1,abs(R)) ≤ 10⁻⁹** for non-I² quantities; **abs(app−R)/100 ≤ 10⁻⁹** for every I²-valued quantity, including summaries/contrasts.

Compare every subset estimate, Q, tau² and I². Require identical memberships, occurrence counts/order, per-study with/without counts and threshold flags. For both modes compare mean/min/max of estimate, I², Q and tau²; type-7 25th/50th/75th percentiles of estimate and I²; zero-I² and positive-tau² counts; all per-study with/without estimate and I² means and signed contrasts. Reconcile quantities exposed by the actual main panel. For Tang additionally compare extras' **with_median, without_median, diff_median** and all inclusion-summary fields; means alone are insufficient.

Primary grid: x0=min(y), x1=max(y); if equal, expand to y−0.5 and y+0.5. Set ix=floor((estimate−x0)×100/(x1−x0)), iy=floor(I²×100/100); clamp each to 0…99; flatten as iy×100+ix. Compare all **10,000 cells exactly**, total and dimensions, plus continuous bounds. These are unpadded density bounds, distinct from display limits. Never repair boundary differences by moving bins.

Reject missing/nonfinite outputs, failed fits, stale inputs, cancellation, surviving previews, incomplete coverage and any disagreement. Singleton normalization is the only registered exception. Such outcomes remain implementation-unresolved, never robustness. Report both implementations.

## 7. Sensitivity, robustness and figure rule

No unsupervised clustering, visual cluster selection, significance testing or study deletion.

Define signed Δy = mean(pool | included) − mean(pool | excluded), and ΔI² analogously, weighting every enumerated subset or sampled occurrence equally. Flag a row if **|Δy| ≥ 0.10 radians OR |ΔI²| ≥ 10 percentage points**, evaluated independently on unrounded app/R outputs. These descriptive thresholds are not clinical-importance cutoffs or causal attribution.

Conditional on novelty eligibility, reproduction, verification and app/R agreement: ≥1 flag is a **registered sensitivity finding**; all rows below both thresholds is **robust under the registered inclusion rule**. For Tang use **robust under the registered 50,000-draw inclusion rule**, with no claim about unobserved subsets. Report every signed contrast/flag and both largest absolute contrasts, including ties. Neither classification establishes homogeneity or correctness of a clinical conclusion. No outcome switching.

## 10. Write-up

Produce **150–250 words plus one figure**, framed as “a re-analysis illustrating study-inclusion sensitivity of pooled prevalence.” Preserve the existing BCG example. State reproduction status, classification, largest contrasts/ties and app/R agreement, with extended data containing all contrasts, verification and failures. The contribution is joint subset/inclusion sensitivity beyond the published pooled and subgroup summaries.

Construct the figure externally from accepted output: completed primary exact density or Tang's fixed sampled scatter, alongside signed contrast strips in original forest order, all rows shown, positive/negative thresholds marked. No study-specific highlight or data-dependent zoom. Label half-Freeman–Tukey radians and I² percent; distinguish exhaustive from sampled scope. No clinical recommendations, priority or ranking claims. Mahmood dictates the final paragraph.


## Capability boundary and implementation obligations

The app supplies the DL subset fits, primary exact summaries/grid/per-study means and fallback occurrence/inclusion outputs documented in EVIDENCE_P13.md. R-only/external work supplies original reproduction, PFT input transformation, independence/input verification, subset Wald intervals, threshold classification, headline/sample selection, comparison and the combined publication figure. No native app support is claimed for those operations.

For fallback global summaries absent from the native main panel, calculate the registered summary from captured unrounded app fits in the external comparator and independently from R refits, then compare. Native main-panel and extras quantities must also reconcile. Do not label externally derived summaries as native app UI outputs. This fixes implementation ownership without dropping any v3 comparison.

For the registered English browser environment, fix tooltip language to en and archive browser settings. Clear/reassert autosaved controls. Treat the pinned generator's actual implementation as authoritative; a generic replacement PRNG bearing the same name is not interchangeable.

Native R execution, real browser capture and all parity/refusal checks remain mandatory post-release, pre-analysis work. Run only generated synthetic_* fixtures marked SYNTHETIC - not data in the first line/column. Do not replay bundled real-data corpora. Any post-release code change is logged as a dated deviation independent of real-data results. The original-model branch stays fail-closed until the F3 configuration is fixed; this supplement is not that configuration.
