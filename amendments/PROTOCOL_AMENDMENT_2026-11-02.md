# Protocol amendment, 2 November 2026: headers-only screening, and deciding rules fixed before screening

Amends `FIELD_USE_CASE_PROTOCOL.md` (27 Oct 2026), `FREEZE_CRITERIA.md` (F1–F6) and `MAHMOOD_DECISIONS.md`. Where they conflict, this amendment wins for the papers it names. **It is committed and released publicly before any candidate it governs is screened.** Its release timestamp is the evidence that the rules below are independent of data. Nothing here relaxes F1–F6.

Notation: k = number of effects pooled; p = number of decimal places printed for a published quantity; half-unit tolerance h(p) = 0.5 × 10^(−p).

## A. Headers-only screening rule

**A0. Scope.** Applies to the replacement P17 screen, the Cowman clearance for P20, and every paper from P23 onward. It covers every candidate search, source check, feasibility check and licence check before that paper's GitHub release. It does not apply retroactively to P16 or P18, whose candidates are already fixed.

**A1. Permitted material.**
1. Title, journal, authors, year, DOI, licence and copyright notices.
2. Abstract sentences in sections headed Objective, Background, Methods, Design, Data sources, Eligibility, Study selection or Data synthesis. **Unstructured abstracts are not shown.**
3. The Methods section.
4. Table and figure captions, and table column headers (the header row only).
5. Printed counts of studies or effects (k) and of participants, from the material above.

**A2. Forbidden material.** Any table body row; forest-plot rows; any study-level value; supplementary data rows; effect sizes, CIs, p-values or prediction intervals from Results; the Discussion's or Conclusion's statements of findings; graphical abstracts; press or news summaries.

**A3. Mechanics.**
1. Text is extracted by section, by script, before any person or model sees it. JATS XML is used where it exists: `<sec>` titles are matched case-insensitively against `method|materials|data synthesis|statistical analysis|search strategy|eligibility`, and `<caption>` and `<thead>` are kept. Every Results, Discussion and Conclusion `<sec>`, every `<tbody>`, and every supplementary data file are dropped before display.
2. PDF-only sources: Methods is taken from the line matching `^\s*\d*\.?\s*(Methods?|Materials and methods)\b` up to the next line matching `^\s*\d*\.?\s*(Results?|Discussion)\b`. Captions are the paragraph starting `^(Table|Fig\.?|Figure)\s+\w+`. **PDF table header rows are not shown** (see P16, section C). If a boundary cannot be found by these patterns, the candidate is **not screenable** and the next candidate is taken.
3. **Decimal redaction.** Every token in the shown text that matches `[-−–]?\d*[.·]\d+` is replaced by `#` before display. Integers are kept.
4. **Log.** `SCREEN_LOG_Pnn.jsonl` gets one line per file opened, with: path or URL, SHA-256, sections shown, extractor script SHA-256, recipient (person, or model and family), and UTC time. The extractor's output is archived with the log.
5. **Exposure.** Any display of A2 material, whether found at the time or by a later audit of the archived displayed text, **disqualifies that candidate permanently for every paper**. It is logged and replaced by the next candidate in the seeded order. It is never kept with a disclosure.

**A4. Selection.** Selection uses only A1 features and the eligibility criteria in section B. Candidates are screened in the order fixed by the paper's seed (B1.6), and the first eligible candidate is chosen, with the second as fallback. Screening notes record only pass or fail per criterion. **No screening note may name an expected headline, direction, magnitude, interval or significance.** A note that does so disqualifies the candidate under A3.5.

## B. Deciding rules fixed now

**B0. Shared rules.**
- **R1. Reproduction configuration.** Use the paper's stated model elements: effect metric, transformation, fixed or random effects, and τ² estimator. For each element the paper does not state, use exactly one value, in this order:
  - (a) if the paper names CMA, RevMan or Stata `metan` but not the estimator: DerSimonian–Laird;
  - (b) otherwise, the `metafor::rma.uni` defaults: `method="REML"`, `test="z"`, `level=95`, `weighted=TRUE`, `intercept=TRUE`, `control=list()`, no Knapp–Hartung, no moderators.
  
  There is no model search, and nothing is retried after a failure.
- **R2. Reproduction gate.** Compare the unrounded pooled estimate and both 95% CI endpoints, each with its printed value. Each must be within h(p), and k must match exactly. Tolerances are not widened for input rounding. Failure leads to the fallback, which runs only if it has been cleared independently; if it fails too, the study stops and the failure is reported.
- **R3. Environment.** R 4.6.0 with `LC_COLLATE=C` and `options(na.action="na.fail")`. Package versions are pinned in each prereg. Synthetic validation must pass before any real-data gate is run.
- **R4.** Any failed gate, failed parity check, non-finite value, convergence failure, silently omitted row or unverified row makes the result **Indeterminate**, and that overrides every other label. A robust result is reported.

### B1. P17: correlation meta-analysis, Fisher z (replacement candidate)

1. **Eligibility.** A candidate is eligible only if ALL of these hold, judged from A1 material only:
   - (a) the licence is CC0, CC BY, CC BY-SA, CC BY-NC or CC BY-NC-SA (ND and unlicensed sources are excluded);
   - (b) it is a meta-analysis that pools Pearson r with a Fisher z transformation stated in its Methods;
   - (c) it has a random-effects model;
   - (d) one effect per study row, with no multilevel or robust-variance model stated;
   - (e) the printed overall k satisfies 10 ≤ k ≤ 60;
   - (f) a table or supplement has column headers for study, r (or correlation) and N (or sample size);
   - (g) it was published 2016–2026;
   - (h) it is not Paterna, nor any paper already screened under the 27 Oct protocol;
   - (i) the Europe PMC and OpenAlex novelty checks (F2) find no prediction-interval re-analysis.
   
   The method is the allmeta `correlation-ma` app.
2. **Outcome.** The overall pooled correlation, meaning the analysis with the largest printed k in A1 material. Ties go to the first such analysis in caption order.
3. **Reproduction.** R1 with `yi=atanh(r)` and `vi=1/(n−3)`, using `metafor::rma.uni(yi, vi, measure="GEN", …)`. Gate quantities: tanh(μ) and tanh(μ ± z₀.₉₇₅·SE), checked against the printed values under R2.
4. **Prediction interval.** Computed explicitly, not with `predict()`. On the Fisher-z scale it is μ ± t₀.₉₇₅,ₖ₋₁ · √(τ² + SE²). It is back-transformed as PI_r = [tanh(μ − t·√(τ²+SE²)), tanh(μ + t·√(τ²+SE²))], with τ² and SE from the R1 fit. The same formula is used when τ² = 0. The required condition k ≥ 10 keeps the interval defined.
5. **App/R parity.** The pinned `correlation-ma` app is run on the same input. For μ_z, SE_z, τ²_z, r, both CI endpoints and both PI endpoints, |app − R| ≤ 1e-4. The two must also give identical labels. If the app's estimator differs from the R1 value, the PI is labelled R-only and app parity covers only the quantities the app computes with that estimator.
6. **"New" vs "robust".** Let L and U be the r-scale PI endpoints, and C the mean CI. All values are unrounded.
   - C excludes 0, and L ≤ 0 ≤ U: **new** (the PI reaches or crosses zero).
   - C excludes 0, and the PI excludes 0: **robust**.
   - C includes or touches 0: **no pooled association to generalise**. This is reported, and is neither new nor robust.
   - Zero is inclusive in "new". tanh is monotone, so the labels are identical on the z scale.
7. **Order.** The Europe PMC query `(TITLE:"meta-analysis" OR TITLE:"meta-analytic") AND (ABSTRACT:"correlation" OR ABSTRACT:"correlations") AND OPEN_ACCESS:y AND PUB_YEAR:[2016 TO 2026]` is run once. All hits are shuffled with `set.seed(20261102); sample()` in R 4.6.0. Candidates are screened in that order. Screening stops after 2 eligible candidates or 40 screened, whichever comes first. With fewer than 1 eligible candidate, P17 stops.

### B2. P18: bivariate random-effects MA of DBP and SBP (Brand et al. 2022, Cochrane)

Fixed by Mahmood's decision of 2 Nov 2026, before any study data are read. This supersedes the P18 draft's supplied-covariance input.

1. **Estimand.** Unchanged from P18 prereg §3: the two-component mean true effect (DBP, SBP; low-sodium salt substitute minus regular salt; mmHg) among studies reporting both outcomes, under a bivariate normal random-effects model. The univariate reproduction gate is unchanged (DL, z, R2).
2. **Assumed within-study correlation.** Within-study correlations are not reported. The analysis uses an assumed common ρ_w ∈ {0, 0.5, 0.8}. All three are pre-specified, and **there is no single primary ρ_w**. For each study i, S_i = [[v1_i, ρ_w√(v1_i·v2_i)], [ρ_w√(v1_i·v2_i), v2_i]].
3. **Model, run once per ρ_w.**
   - Fit `mvmeta::mvmeta(Y ~ 1, S=S, method="reml", bscov="unstr")` with the P18 prereg §7 control list.
   - Cross-check with `metafor::rma.mv(yi, V, mods=~outcome-1, random=~outcome|study, struct="UN", method="REML", test="z")`.
   - The app gets the same R-computed covariance, written to 17 significant digits, in `multivariate-ma` supplied-covariance mode (`label,y1,v1,y2,v2,cov`).
   - The comparator is the paired univariate REML fit (independent of ρ_w). Parity and convergence rules are as in P18 §7.
4. **Classification at each ρ_w.** Apply P18 prereg §8 unchanged, giving C(ρ_w) ∈ {new, robust, no threshold-defined change, indeterminate}. The §8 triggers are a sign change, an interval-category change, |Δμ| ≥ 1.0 mmHg, or a width ratio outside [0.80, 1.25].
5. **Final rule.** If any C(ρ_w) is indeterminate, the result is **Indeterminate**. Otherwise, if C(0) = C(0.5) = C(0.8), report that label as **invariant to ρ_w**; only this case may be called robust to ρ_w. Otherwise the result is **ρ-sensitive**: report all three labels and the triggering criteria, and do not headline any single ρ_w.

### B3. P20: effect-size conversion (Cowman et al. 2021, Schizophr Bull, doi:10.1093/schbul/sbab033)

1. **Clearance first.** Cowman replaces Pilling only after a rule-A source check confirms all of the following:
   - (a) the licence permits reuse; the institutional copy is labelled CC BY-NC 4.0, and the publisher version must also be checked;
   - (b) column headers show the native statistic (OR, β or t) and n for the rows of the longitudinal general-cognition-versus-functioning analysis;
   - (c) at least one row was converted from OR, β or t;
   - (d) F2 novelty passes.
   
   If any of these fails, P20 stops.
2. **Reproduction.** R1 and R2 on Cowman's printed study-level r. Pooling uses Fisher z with vi = 1/(n−3) if Cowman's Methods state Fisher z, and otherwise raw r with Cowman's stated variance. If no variance is stated, the candidate is not feasible.
3. **Conversion sets.** The primary set P is the conversion Cowman's Methods state for each metric. Where no conversion is stated, P uses the defaults below. The alternative set A uses the other formula on each line.
   - **OR → r.** Logistic: d = ln(OR)·√3/π. Normal: d = ln(OR)/1.65. Then r = d/√(d² + a), with a = (n₁+n₂)²/(n₁n₂), or a = 4 if the arm sizes are not printed. Default P: logistic. A: the other one.
   - **β → r.** Peterson–Brown: r = β + 0.05·λ, with λ = 1 if β ≥ 0 and 0 otherwise. Direct: r = β. Default P: Peterson–Brown; A: direct. A row with |β| > 0.5 uses r = β in both sets, and this is logged.
   - **t → r.** r = t/√(t² + df), with df = the printed df if it is printed and n − 2 otherwise. This formula is exact, so it is identical in P and A (there is no alternative).
   - Rows printed natively as r are unchanged in both sets.
4. **Compatibility gate.** Each set-P converted row must equal Cowman's printed r within h(p). If it does not, P20 stops.
5. **App/R parity.** The pinned `effect-size-converter` computes the conversions it implements; the static audit is cited in the P20 prereg, and every other conversion is R-only. For each converted value, |app − R| / max(1, |R|) ≤ 1e-9.
6. **New/robust, comparing the pooled r under A with the pooled r under P.** **New** if any of these holds:
   - (a) the sign category differs;
   - (b) whether the CI excludes 0 differs;
   - (c) the r-band differs, with bands <0.10, [0.10, 0.30), [0.30, 0.50) and ≥0.50;
   - (d) |Δr| ≥ 0.05 (half the narrowest r-band width, 0.10; fixed by the coordinator, who has not seen any Cowman result);
   - (e) the CI-width ratio A/P lies outside [0.80, 1.25].
   
   **Robust** if none of these holds and every gate passes. Otherwise **Indeterminate** (R4). Boundaries: equal to 0.05 triggers; equal to 0.80 or 1.25 does not.

### B4. P16: NMA inconsistency (Hodkinson et al. 2022, BMJ)

1. **Estimand unchanged** from P16 prereg §3: global between-design incoherence and all estimable direct-minus-indirect MD differences in non-HDL cholesterol. The §8 classification is also unchanged.
2. **App.** `nma-inconsistency` gains multi-arm support. It is built test-first against netmeta, using only synthetic fixtures and netmeta's bundled example data, never P16 data. The commit is pinned in P16's prereg before release. The app may not change after the P16 release.
3. **Parity.** As in P16 §7:
   - estimates, SEs, test statistics, τ² and CI endpoints: |app − R| ≤ 1e-8·max(1, |R|);
   - raw p-values: absolute difference ≤ 1e-8;
   - counts, df and treatment/design identities: exact equality.
   
   Any miss makes the result **Indeterminate**.

## C. Why

1. **P17 (Paterna) is dropped.** Its 27 Oct screening recorded "Text readable, including Table 1", and named a possible headline. The run-4 red team (`cxPREP17/REDTEAM_agy.run4.txt`) found two failures:
   - **F3:** "no source in the record that is independent and dated before the exposure" fixed the unstated model parts.
   - **F4:** the prediction-interval rule "could have gone either way, and it was settled after the exposure".
   
   **Verdict: FAIL.** Exposure cannot be undone. The remedy is to fix the rules before screening, with a public timestamp (section B), and to screen without row exposure (section A).
2. **P16 run 3** (`cxPREP16/out/P16/supporting/PRE_RELEASE_DEVIATIONS_P16.md`). A header-display script with a generic y ≥ 470 cutoff exposed study-characteristic cells, an adverse-event row and pooled comparison cells on 11 supplement pages. Rule A3.2 therefore forbids PDF header-band extraction.
3. **P20.** The earlier P20 screening recorded Cowman's published pooled r and CI (`cxPREP20/out/P20/supporting/SOURCE_CHECK_P20.md`), a results-section value that A2 now forbids. No Cowman study-level row is recorded as seen. This predates this amendment and is disclosed; C4 decides it.
4. **Decision on Cowman (coordinator, under Mahmood's delegated 2 Nov decision "clear the Cowman 2021 fallback, then move to it").** Cowman is **not disqualified**. Reasons:
   - (i) A3.5 governs screens run under this amendment. It is not applied retroactively.
   - (ii) The prior exposure was to Cowman's published POOLED summary only. The reproduction gate (R2) must read that value anyway. No study-level row was seen.
   - (iii) The P20 new/robust rule (B3.6) compares conversion set A with conversion set P, not with the published value.
   - (iv) The one threshold drafted by an agent that had read the pooled summary line (|Δr| ≥ 0.025) was replaced before this commit by 0.05. That value is derived as half the narrowest r-band, and was fixed by a coordinator who has not seen any Cowman result.
   
   This exposure is disclosed in the P20 pre-registration. The Cowman clearance itself runs under rule A.