# P15 pre-registration v6: study-cluster robust inference for dependent meta-analytic effects

Status: DRAFT for freeze; F1-F6 pass under the binding deterministic scale-check decision. No extraction or analysis has been performed. The scale check is unrun; fallback remains unavailable for its complete workflow.

**Paper:** P15. **Target journal:** PLOS ONE. **Date:** 2026-10-28. Not released; no extraction or analysis. See [blockers](BLOCKERS_P15.md).

## 2. Chosen meta-analysis and fallback

**Selected primary:** Rytwinski T, Soanes K, Jaeger JAG, Fahrig L, Findlay CS, Houlahan J, van der Ree R, van der Grift EA. (2016). *How Effective Is Road Mitigation at Reducing Road-Kill? A Meta-Analysis*. PLOS ONE 11(11):e0166941. [DOI: 10.1371/journal.pone.0166941](supporting/evidence/primary/fulltext.xml). CC BY 4.0.

Selection rests on target-journal publication, infrastructure decisions and dependent wildlife outcomes retained in the complete synthesis. The original already reports aggregation to 67 synthetic effects; this existing dependence sensitivity is acknowledged. The proposed contribution is study-cluster CORR/CR2/Satterthwaite inference.

**Fallback:** Batteux E, Ferguson E, Tunney RJ. (2019). *Do our risk preferences change when we make decisions for others? A meta-analysis of self-other differences in decisions involving risk*. PLOS ONE 14(5):e0216566. [DOI: 10.1371/journal.pone.0216566](supporting/evidence/fallback/fulltext.xml). Creative Commons Attribution; the local displayed licence statement does not specify its version. Its target-journal setting, surrogate-decision question and unaggregated moderator analyses support the choice.

Primary source verdict: **FEASIBLE** under [item 9 and the v6 decision](supporting/evidence/V6_JOB_P15.md); section 4 fixes the mandatory scale check. Fallback remains **NOT FEASIBLE for its full registered workflow**: original overall aggregation/variance construction is unresolved. Activation requires independent feasibility, novelty and prospective reproduction clearance; otherwise stop. Fallback unavailability does not independently fail [freeze criteria](supporting/evidence/FREEZE_CRITERIA.md).

Switch only for documented source/scale-check failure, an equivalent prior re-analysis, or failure of the registered original-result reproduction. The fallback must independently pass every prerequisite. If it remains unavailable or fails, report both dispositions and perform no new analysis. Both candidates require no more than 60 independent study clusters and an estimated no more than four hours of Codex work; effect rows are separate. No result-based selection, primary-study reconstruction, outcome substitution or post-hoc subset is permitted.

## 3. Fixed outcome and estimand

| Specification | Primary | Fallback |
|---|---|---|
| Outcome | Road-kill with mitigation versus control/before mitigation; complete synthesis | Risk-taking for others versus self; domain moderation of the complete unaggregated synthesis |
| Scale/null | Printed Hedges' d; positive means reduced road-kill; null 0 | Printed Hedges' g; positive means greater risk-taking for others; null 0 |
| Published synthesis counts | 50 studies; complete dataset n = 99 | Overall k = 49; unaggregated moderator dataset k = 78 |
| Original overall pooled target | 0.75 (95% CI: 0.50, 1.00) | g = 0.009, CI (-0.092, 0.109) |
| Original model | Independent-effects random-effects, DL | Random-effects overall after within-study aggregation; mixed-effects moderation |
| Unstated settings | CI method; separately scoped global software/version statement | Heterogeneity estimator, CI method, R/package versions and exact within-study aggregation construction |

Primary estimand: CORR-weighted mean d. Fallback: domain coefficients with financial reference and medical/interpersonal indicators, plus an R-only joint test. Original domain-only moderation is `Q = 26.732, p < .001`; the medical-domain unaggregated summary is `g = -0.267, CI (-0.430, -0.105), k = 15`. This k counts effects. Do not substitute article Table 1's simultaneous all-moderator model for the domain-only comparison. Neither target is a ratio; log/natural ratio pooling is inapplicable.

## 4. Data source and feasibility

The [source check](supporting/SOURCE_CHECK_P15.md) records quotations and [hashes](supporting/EVIDENCE_SHA256.md). Header-only inspection of [S2 Table](supporting/evidence/primary/pone.0166941.s003.docx) confirms `Study*`, `NC`, `NT`, `d`, `se`: n1=NC (control/before), n2=NT (impact/after). No row values were inspected. Eq. (3) has a radical; S2 Fig says "standard error". Conflicting wording remains: S2 says "variances for d (se)"; Methods says "The sampling variance of is given by:". These prevent assuming either scale now, without contradicting the prospective check.

**After release, extraction and verification, BEFORE reproduction**, apply the [fixed rule](supporting/SCALE_CHECK_P15.md) to every S2 observation:

1. From printed n1, n2 and d compute `A = sqrt[(n1+n2)/(n1*n2) + d^2/(2*(n1+n2))]`; `B = A^2`.
2. Preserve printed `se` text, including trailing zeros. For p decimal places, `t = (1/2)*10^(-p)`; three decimals give `0.5*0.001 = 0.0005`. Scientific exponent e gives `t = (1/2)*10^(e-p)`. Never round A/B or propagate n/d rounding.
3. SE iff `abs(se-A)<=t` only; VAR iff `abs(se-B)<=t` only; both matches = AMBIGUOUS; neither = NONE. Inclusive boundaries use exact arithmetic as specified in the supporting rule.
4. All SE: `vi=se^2`. All VAR: `vi=se`. Any AMBIGUOUS, NONE, missing n or mixed classes: **STOP the primary**. Invalid required inputs also stop; never drop failing rows.

Preserve printed fields; log row keys, tolerances, comparisons, classes and the single mapping before pooled calculation. The procedure is fixed now, never selected by pooled results. Never try both mappings on the gate or switch after failure. Only an independently cleared fallback may follow; otherwise stop.

Fallback **S2 Appendix**, `supp/pone.0216566.s002.docx`: `Author`, `Year`, `Study`, `g`, `Variance`, `Domain`. **S3 Appendix** (`.s003.docx`) defines domains; Medical/Safety maps to medical. Retain other S2 fields for provenance. S4 Appendix (`.s004.docx`) and article `sec033` identify the original domain-only comparison.

Effect/uncertainty text and three-decimal display were documented in the prior review; v6 did not inspect numerical cells. Preserve actual printed precision. Repeated headers are structural. Rows remain confined to their own meta-analysis.

## 5. Extraction and verification

Binding specification, copied exactly from [MAHMOOD_DECISIONS.md item 4](supporting/evidence/MAHMOOD_DECISIONS.md):

> Human verification: humans check headline rows, a seeded 5% of the other rows (at least 1), and only the fields still disputed after a third-model adjudication plus a fourth AI re-check (agy, different family). If the sample error is over 2%: a full AI re-extraction plus a human re-check of the headline rows. Packets are about 30 minutes or less; at most one per person per week across all papers (COAUTHOR_LOAD.md); Mahmood is in the rota; a packet not returned in 7 days is reassigned.

After release, Codex and agy independently double-extract, blind to each other. Pin agy to a different model family from Codex and read back its model identity from its log line.

A third model adjudicates every discrepant field against the source. A fourth AI pass—agy using a different family from the adjudicator—rechecks every adjudicated field. Only disagreements remaining after that pass go to humans.

Co-authors of P15 and/or Mahmood verify:

- **Headline-driving rows:** all rows in any cluster whose deletion, at any registered rho, changes the headline significance category, changes any reported coefficient by ≥0.10, or changes its CI width by ≥10%; also all rows in clusters contributing ≥10% of total fitted weight. Deletion diagnostics are R-only and never justify exclusions.
- **Random remainder:** Row key is the lowercase DOI without a URL prefix, followed by "|" and the exact source DOCX filename, followed by "|table1|row" and the base-10, unpadded, one-based position of the w:tr element in the sole source table. Positions include structural header rows, although headers are never eligible observations. Hash the UTF-8 bytes of "2026102815|P15|" followed by that row key, without a BOM, newline or trailing whitespace. Sort lowercase hexadecimal SHA-256 digests ascending; break ties by bytewise ascending row key. Take max(1, ceiling(0.05*n)) eligible remainder rows when n>0, and none when n=0. Preserve physical positions through corrections.
- **Unresolved fields:** every field still disputed after the fourth AI pass.

Record initials, date, source location and decision in `VERIFICATION_LOG.csv`. A sampled row is erroneous if any required field disagrees with its source. If erroneous sampled rows/sample rows exceeds 2%, repeat full AI double extraction and adjudication, followed by human rechecking of headline rows only. This does not trigger full human verification.

Budget approximately 25 minutes per ten-row packet, including instructions; split larger assignments. No co-author receives more than one packet weekly across papers. Coordinate assignments through the live pipeline/COAUTHOR_LOAD.md shared with P14/P06, including Mahmood in the rota. The bundled supporting/evidence/COAUTHOR_LOAD.md is a historical snapshot and must not be used to determine current availability. Reassign packets after seven days, never skip them. Corrections require rerunning gates and diagnostics until newly driving rows are checked.

## 6. Original-result reproduction gate

After release, verified extraction and a passing primary scale check, require absolute differences in the pooled estimate **and each CI endpoint** no greater than **0.005** for primary and **0.0005** for fallback. Never widen tolerances or change printed inputs to compensate for rounding.

Original-method evidence is in the source check. Primary global DL is stated; R 3.0.3 / metafor 1.9–4 are explicitly named for meta-regression. Global CI method is **NOT STATED**. The single primary attempt on pc2 is:

```r
original <- metafor::rma.uni(
  yi = yi, vi = vi, data = d, method = "DL", test = "z", level = 95,
  measure = "GEN", intercept = TRUE, weighted = TRUE, control = list()
)
```

Use [pinned R 4.6.0 and metafor 5.2.1](supporting/evidence/R_ENV.txt). F3 permits one software-default attempt: z for primary; REML and z for fallback. These are assumptions, not proof of historical settings. The [second-round review](supporting/evidence/REDTEAM2_P15.md) documents the default-setting evidence. No custom weights, subset, scale model, transformations or tau-squared override; complete finite inputs only. All other controls retain the pinned version's defaults, with no tuning or alternative attempts. These settings also govern the conditional fallback models below.

Fallback overall reproduction requires its original within-study summary construction first. The paper names Cooper's shifting-unit method but does not fully specify weighting/covariance; `rma.uni` supplies no default aggregation algorithm. Until permissible published material resolves this through a prospective amendment, fallback activation is blocked. Once resolved, use `rma.uni(..., method="REML", test="z", level=95)` for the overall summary inputs and for the unaggregated domain-only model (`mods = ~ medical + interpersonal`). Additionally require domain Q to agree within **0.0005** before comparing moderation.

The domain-Q target is exclusively the main-text sec033 value 26.732. S4 Appendix separately prints 27.666; retain it as source context, never as an alternative gate target. Failure against 26.732 invokes the unchanged stop rule.

Do not test alternative estimators, HK settings, correlations or aggregation rules to obtain a match. A valid-input primary mismatch activates the fallback only if its prerequisites are met. Missing n or failed scale classification stops the primary before reproduction; other unresolved source fields prevent eligibility. If both candidates fail or are unavailable, report that and stop. No gate has run.

## 7. Exact new analysis and agreement

Cluster by study. Primary uses the documented `Study*` identity across all its outcomes; fallback preserves `Author|Year|Study` identity and groups dependent outcomes within that study. Preserve experiment identifiers without splitting dependent outcomes into separate clusters. Source-documented cross-report overlap must be resolved; unresolved identity/overlap prevents eligibility. Do not equate effect counts or aggregated main-analysis units with verified independent clusters.

Use pinned `rve-meta/index.html`: primary input exactly `cluster,yi,vi`; fallback adds numeric `medical,interpersonal` indicators in that order. Financial has both indicators zero. Centre predictors **off**. Keep provenance outside the app input because extra columns are treated as predictors. Use identical physical-source row order and character cluster IDs in both implementations; prefix each resolved identity with `P15|` to prevent numeric/logical parser coercion. Preserve the original identity separately. Do not impute, floor nonpositive variances, recalculate effects or silently exclude rows.

Set rho=0.8; refit the fixed grid `{0,0.2,0.4,0.6,0.8,1}`. Use CORR weights, Hedges–Tipton–Johnson moment tau-squared, CR2, coefficient-specific Satterthwaite df, two-sided tests and 95% Student-t CIs. Do not override tau-squared or use CR1.

Independent R: Windows R 4.6.0, `LC_COLLATE=C`, robumeta 2.1, clubSandwich 0.7.0:

```r
Sys.setlocale("LC_COLLATE", "C")
f <- robumeta::robu(
  FORMULA, data = d, studynum = cluster, var.eff.size = vi,
  modelweights = "CORR", rho = RHO, small = TRUE
)
ct <- clubSandwich::coef_test(f, vcov = "CR2", test = "Satterthwaite")
```

`FORMULA` is `yi ~ 1` or `yi ~ medical + interpersonal`. Refit every rho; CIs are estimate ± `qt(.975, df) * SE`. Fallback joint domain test is **R-only**:

```r
clubSandwich::Wald_test(
  f, constraints = clubSandwich::constrain_zero(2:3),
  vcov = "CR2", test = "HTZ"
)
```

For estimates, SEs, t, df and tau-squared require `abs(app-R)/max(1,abs(R)) <= 1e-9`. For CI endpoints and p-values require absolute differences <=1e-9. Counts/status must match exactly: app `k_effects` / `k_total` means effect rows; `m_clusters` means clusters. Match terms and rho explicitly. Use full-precision JSON/CSV, not rounded screen/report values. Report both outputs and all disagreements. Undefined results do not establish substantive agreement.

Compare reproduced original and CORR estimates, CI widths and significance; differences reflect weighting/heterogeneity changes as well as robust inference. Original-model reproduction, cluster deletion diagnostics, joint testing, classification and the figure are R-only. The full operational `code/` remains absent; deliver, hash and synthetically validate it under the mandatory conditions below. The app-generated R export alone is insufficient.

## 8. New versus robust

Primary **new finding:** at any registered rho, relative to reproduction, sign or zero-exclusion status changes, d shifts by >=0.10, or the CI-width ratio lies outside `[0.80,1.25]`. **Robust:** none occurs and every CI remains strictly positive.

Fallback **new finding:** joint domain p>=0.05 at any rho, or either domain coefficient changes sign, shifts by >=0.10, or has a CI-width ratio outside `[0.80,1.25]` versus the reproduced domain-only model. **Robust:** joint p<0.05 throughout and none of those coefficient changes occurs.

State every triggering rho and criterion. Exact zero is its own sign category; a CI touching zero does not exclude it. A required coefficient df<4, required joint-test denominator df<4, undefined fit/ratio or failed agreement makes the overall classification indeterminate. No new/robust label overrides a failed gate. Thresholds are reporting rules, not clinical-importance cutoffs; report every outcome without switching.

All coefficient shifts are absolute differences. CI-width ratios are CORR/original. Deletion diagnostics refit every rho; width change is abs(width_deleted/width_full - 1), and cluster weight share is its summed weights/total weight at each rho. Headline significance categories are primary CI strictly positive/strictly negative/including zero and fallback joint p<0.05 versus p>=0.05. Required coefficient df includes every reported coefficient, including the intercept. Failed deletion diagnostics leave verification incomplete.

## 9. Novelty-check log

**Europe PMC and OpenAlex replace Google Scholar because Scholar showed a bot check ("unusual traffic") on 2026-10-28; it was not bypassed.** The [novelty log](supporting/NOVELTY_LOG_P15.md) preserves queries, evidence hashes, coverage history and pc2's disposition.

| Candidate/index | Lookup; date 2026-10-28 | Recorded result |
|---|---|---|
| Primary / Europe PMC | MED / PMID 27870889 | 82/82 citing records |
| Primary / OpenAlex | W2556258011 | 343/343 unique citing works; page-based, per-page 100 |
| Fallback / Europe PMC | MED / PMID 31067283 | 26/26 citing records |
| Fallback / OpenAlex | W2943919874 | 74/74 citing records |
| Both / PubMed | Exact queries in supporting log | 0 each |
| Both / Google Scholar | Protocol attempt | blocked; no count |

The earlier cursor request stopped at 200/343 with HTTP 401. The [paged JSON](supporting/evidence/NOVELTY_openalex_P15primary_paged_2026-10-28.json) contains 343 distinct IDs. The [v4 coordinator note](supporting/evidence/V4_JOB_P15.md) and [v5 decision](supporting/evidence/V5_JOB_P15.md) attribute seven-title screening to pc2: none applies RVE/dependence modelling to this dataset. This is not independent full-text adjudication. The older eight flagged entries have no documented mapping to those seven titles. No equivalent was identified; index limits, overlap and title-truncated PubMed queries limit coverage.

An **equivalent prior re-analysis** must actually re-analyse this candidate's same synthesis/outcome and effect set (or the same complete set recovered from its supplements), using study-cluster correlated-effects robust variance estimation with CR2/Satterthwaite inference for the registered mean/domain question. A materially identical small-sample RVE implementation qualifies regardless of software branding. Merely citing the candidate, using another dataset, or the primary's original ICC aggregation sensitivity does not qualify. A suspected equivalent requires methods-level confirmation before candidate exclusion; no priority claim is made.

## 10. App-implementation evidence

Pin: `14dc545bcba87a02158b2f445c28450e7eaf6b89`; [snapshot record](supporting/evidence/PIN.txt).

The incorporated [app audit](supporting/APP_AUDIT_P15.md) records file/function/line evidence and SHA-256 for the entry page and every loaded dependency. Static inspection confirms `rve-meta/index.html::run()/runSensitivity()`, `shared/rve.js::fitCORR()/summary()`, and `shared/rve-extras.js::parseStudies()/rhoSensitivity()/buildResult()/toRScript()`. CORR moment heterogeneity, CR2 and coefficient-specific Student-t inference are implemented; `shared/rve-eigen.js` embeds the WebAssembly eigensolver and `shared/stats-qt.js` supplies t probabilities/quantiles.

All ten direct script/stylesheet dependencies exist, including `hub/app-style.css` and `hub/shared/a11y-landmarks.js`. Static availability does not certify browser/runtime closure. The embedded build stamp is older than the supplied pin; preserve it and record the actual file hashes separately. R-only work is labelled in section 7. Independent reviews and synthetic runtime validation remain outstanding.

## 11. Write-up plan

Write 150–250 words framed as “a re-analysis illustrating …”, plus one figure comparing reproduced original estimates and app/R CORR intervals across rho. Fallback adds domain coefficients and the labelled R-only joint test. Report study/effect counts, df, agreement, all gate failures and indeterminate outcomes. Preserve the existing use case. Mahmood dictates the final paragraph. No clinical recommendations, priority/ranking claims or publication-error allegations.

## 12. Deviations, amendments and freeze

| Date | Amendment/deviation | Reason/timing |
|---|---|---|
| 2026-10-28 | Europe PMC/OpenAlex replace Google Scholar | Binding decision; bot check not bypassed; before extraction |
| 2026-10-28 | V6: replace RT2-P15-01 with deterministic scale check | Item 9; NC/NT headers confirmed; after-release execution before reproduction |
| 2026-10-28 | OpenAlex gap closed; fallback status disclosed; operational work moved below | V4/FREEZE_CRITERIA; no gate weakened |
| 2026-10-28 | V5: portable evidence, count locator, exact row-key serialization | RT2-P15-02/03/04 applied; gates retained |

### Mandatory post-release, pre-analysis conditions

- Deliver/hash operational `code/`: imports/cluster checks, the R-only scale check, original gates, CORR grid, app/R comparison, deletion, classification and verification sampling/logging. Log post-release code changes as dated deviations independent of real-data results.
- Run generated `synthetic_*` fixtures, marked "SYNTHETIC - not data" in the first line/column; cover scale classes, missing/invalid inputs, mixed sets and exact boundaries. **Code must pass synthetic validation before any real-data reproduction gate.**
- Demonstrate app/R runtime parity at the registered tolerances, including rho endpoints, parser/variance handling, invalid inputs and indeterminate fits. Report failures; no real-data tuning.
- Close browser dependencies and verify WebAssembly loading, fitting and full-precision exports on synthetic inputs. Replace bundled example input before its automatic initial fit; use a clean browser state.
- Synchronise extraction/packet/log templates to this registration before extraction; assign packets through the shared COAUTHOR_LOAD ledger before sending, within its weekly cap. Eligible P15 verifiers: MA, SMA, NA, CM, AW. First-round REDTEAM/APP_CHECK reports remain absent; review any delivered findings before analysis.

The [v6 notes](V5_NOTES_P15.md) map every finding and F1-F6 decision. This freeze candidate awaits REDTEAM2. Archive supporting files in P15's GitHub release and Zenodo, with hashes and server-side timestamp/DOI. Extraction starts only after P15's release exists and archive conditions are satisfied. No scale check, gate, synthetic run or human verification occurred here. Archive extraction/model-identity logs, verification, scale decisions, gates, scripts and both outputs. Amendments remain dated and prospective.

**sha256 and UTC freeze time recorded at release**
