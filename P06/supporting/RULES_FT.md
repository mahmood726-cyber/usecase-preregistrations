# Full-text eligibility screen (stage C) — instructions for the screener

You check ONE review's full text (`paper.txt`, converted from the Europe PMC JATS XML; figures appear only
as captions with a `[FIGURE id=...]` marker, tables appear as text). `record.json` gives the pilot (P14 or
P06) and bibliographic metadata.

**Hard prohibitions.** Do not extract or record any trial-level effect, CI, event count, mean, SD or
participant number, and do not record the review's pooled estimate, CI, p-value, I² or its direction or
significance. You may record only the facts requested below. Ignore result direction/size entirely: it must
not influence any decision. Do not use the internet.

## Step 1 — designate exactly one synthesis (mechanical, before judging eligibility)
1. The first explicitly named primary outcome in Methods; otherwise the first efficacy outcome listed in
   Methods. Co-primary outcomes: Methods order.
2. Within it, the authors' primary comparison and primary follow-up; if unspecified, their first displayed
   overall forest plot for that outcome, then its first comparison and time point in document order.
3. If that designated synthesis fails eligibility, the review is excluded. Never move to a secondary outcome.

## Step 2 — facts to record for the designated synthesis
- `design`: is the review a conventional pairwise meta-analysis of randomized trials for this synthesis?
  Note network/Bayesian/multilevel/multivariate/IPD/DTA/prognostic/nonrandomized or inseparably mixed designs.
- `population`:
  - P14: children 0–17 years at trial entry. A paediatric-only pooled analysis inside a mixed review counts
    only if it IS the designated primary synthesis. Trials randomizing pregnant women (child not yet born
    at entry) are not paediatric. Caregiver-delivered interventions count when the designated outcome is
    measured in the (already born) child.
  - P06: all participants have a diagnosed malignant solid or haematological cancer (incl. paediatric
    oncology; anticancer treatment, supportive care, survivorship). Prevention/screening without cancer,
    benign or precancerous disease, or inseparable cancer/non-cancer populations fail.
- `k_designated`: number of independent trials (not reports, not comparisons) contributing to the
  designated synthesis, with the location you counted it from (e.g. "Figure 2 caption", "Results para 3",
  "Table 2"). Null if not determinable from the text.
- `independence`: multi-arm trials contributing >1 contrast, split shared controls, cluster/crossover
  trials without adjusted estimates, duplicate/overlapping reports.
- `per_study_data`: where per-study estimates with SE/CI (or arm-level numbers sufficient to compute them)
  for the designated synthesis are printed: `TABLE` (in the text tables — say which), `FIGURE` (forest plot
  figure id; the image cannot be seen by you, a later step checks it), `SUPPLEMENT_ONLY`, or `NONE`.
- `pooled_reported`: does the paper report the original pooled estimate WITH its CI for the designated
  synthesis? yes/no only. Do not copy the numbers.
- `model`: the pooling model for the designated synthesis exactly as described (quote ≤30 words):
  effect measure (RR/OR/HR/RD/MD/SMD/other), fixed vs random, weighting method (inverse variance,
  Mantel–Haenszel, Peto), tau² estimator (DL, REML, PM, other, unstated), CI method (Wald/normal, HKSJ,
  unstated), software and version exactly as named (e.g. "Review Manager 5.4", "Stata 16 metan", "R meta 6.2").
  Record what the paper states; do not infer an unstated estimator yourself (the coordinator applies the
  fixed identification rule below). `model_conditional`: yes if the paper chose fixed vs random depending on
  heterogeneity (e.g. "random if I² > 50%"), else no.
  Mantel–Haenszel random effects (RevMan "M-H, Random") is recorded as weighting=mantel_haenszel, random.
- P14 only: `trial_years_min`, `trial_years_max` (publication years of the included trial reports in the
  designated synthesis, from the included-studies table or reference list; null if not determinable) and
  `participants_per_trial_available` (yes/no: a per-trial randomized N for the designated comparison is printed; for a multi-arm trial this
  means the sizes of the two arms in the designated contrast, not total trial enrolment).
- `flags`: retraction/correction notices, protocol only, publication date outside 2017–2025, language,
  licence statement found in the text (quote it).

## Step 3 — verdict
- `ELIGIBLE` only if ALL hold: pairwise RCT meta-analysis for the designated synthesis; population rule
  met; 10 ≤ k_designated ≤ 60 independent trials; per-study data printed (TABLE, FIGURE or SUPPLEMENT_ONLY —
  FIGURE and SUPPLEMENT_ONLY are provisional pending a later image/supplement check); pooled estimate with CI reported; the model is identifiable from the
  text under amendment A3 (inverse-variance fixed effect; or inverse-variance random effects with tau²
  stated as DL or REML, or with software named as Review Manager/RevMan version 5.x whose random-effects
  estimator is DL; CI = Hartung–Knapp only if stated, otherwise Wald; Mantel–Haenszel, Peto, PM and other
  estimators are unsupported; "random-effects model" with no estimator and no RevMan 5.x is NOT identifiable;
  a heterogeneity-conditional fixed/random choice is identifiable only if the model actually used for the
  designated synthesis is stated or labelled); P14: trial year span (max − min) ≥ 5 and per-trial participant counts available.
- `EXCLUDE` with the FIRST failing criterion as `reason_code`, in this order:
  `DESIGN`, `POPULATION`, `K_OUT_OF_RANGE` (k<10 or k>60), `K_UNDETERMINABLE`, `NONINDEPENDENT`,
  `NO_PER_STUDY_DATA` (NONE), `NO_POOLED_RESULT`, `MODEL_UNSUPPORTED` (identified but
  outside the allowed set, e.g. Mantel–Haenszel fixed effect, Peto, PM, Bayesian), `MODEL_UNIDENTIFIABLE`,
  `CHRONOLOGY` (P14: span < 5 years or years missing), `PARTICIPANTS_MISSING` (P14), `OTHER`.
- `UNRESOLVED` when a criterion genuinely cannot be decided from the text (state which and why).

Also list in `ambiguities` any place where the rules themselves were unclear for this paper (not where the
paper was unclear). Be brief and factual.
