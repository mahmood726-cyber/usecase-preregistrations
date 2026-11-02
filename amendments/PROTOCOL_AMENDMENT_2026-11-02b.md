# Protocol amendment 2, 2 November 2026: screening mechanics fix and generic P18 rule

This amends `amendments/PROTOCOL_AMENDMENT_2026-11-02.md` (commit 4fadf392). It is committed before any further screening. Anything not changed here stands.

## Why

The first headers-only screen (P17 candidates 1-25, and the Cowman clearance for P20) found a contradiction inside amendment 1. Rule A3.1 drops every supplementary data file before display. Eligibility criteria B1.1(f) and B3.1(b) need column headers that, for many reviews, exist only in a supplement. Applied literally, any candidate whose study table is in a supplement fails automatically. This is a defect in the screening mechanics, not a deciding rule. It is fixed below. The re-screen then restarts from candidate 1 in the original archived order, so the fix cannot be used to choose a candidate.

P18 (Brand et al. 2022) is disqualified. An exposure audit of its pre-registration lane found that its 19 study-level DBP forest rows were displayed before freeze, with digits masked but signs and interval patterns visible, along with unmasked study-level DBP/SBP ranges. Under amendment 1, rule A3.5, it is replaced by a new candidate screened under rule A. Rule B2 is made generic below for that candidate.

## A3.1a. Supplement header rows (added)

A supplementary file in .docx, .xlsx, .xls, .ods or .csv format may be opened by a script that outputs only the first row of each table or sheet, plus the table caption or sheet name. Those values are decimal-redacted under A3.3, and nothing else from the file is shown. The script, its SHA-256 and its output are archived per A3.4. PDF supplements stay excluded (A3.2). A file that the script cannot reduce to header rows is not shown, and the criterion that needed it is judged "not verifiable", not "fail".

## A3.1b. Methods sentences carrying results (added)

Before display, a Methods sentence is dropped if it contains a test result or heterogeneity statistic. That means a sentence matching any of `\bp\s*[<=>≤≥]`, `I\s*(2|²)\s*[=<>]`, `τ\s*(2|²)?\s*=`, `tau\s*(2|²|\^2)?\s*=`, `\bQ\s*[=(]`, `chi\s*(2|²|-square)`, `χ`, or `\bsignifican(t|ce)\b`. (Screen 1 showed one such sentence, for candidate C14. C14 was disqualified, and it was ineligible anyway.)

## A4a. Order is the archived order (clarified)

For P17, the candidate order is the archived file `screen_1102/P17/display/ORDER_first40.txt`, SHA-256 `1edd2f3fc118de820b6a568cb1ead32a19ab48101299c9a99e2ba0d8394d852d`. It is Europe PMC's returned order, shuffled with `set.seed(20261102)` in R 4.6.0. The re-screen starts again at candidate 1 and stops at the first eligible candidate (primary) and the second (fallback), or after candidate 40 (B1.7).

## B2'. P18 replacement: generic bivariate SBP/DBP rule (replaces the candidate-specific parts of B2)

1. **Eligibility.** Judged from A1 material plus A3.1a header rows. A candidate is eligible only if all of the following hold:
   - (a) its licence permits reuse and redistribution of the extracted data (CC BY, CC0 or equivalent);
   - (b) it is a meta-analysis that pools both systolic and diastolic blood pressure as mean differences under a stated random-effects model;
   - (c) headers in a table or a supplement show, per study, an MD with an SE or CI for each of SBP and DBP;
   - (d) the printed number of studies reporting both outcomes satisfies 10 ≤ k ≤ 60;
   - (e) it is not Brand et al. 2022;
   - (f) it passes F2 novelty (no prior bivariate re-analysis of this meta-analysis).
2. **Order.** The Europe PMC query `(TITLE:"meta-analysis") AND (ABSTRACT:"systolic" AND ABSTRACT:"diastolic") AND OPEN_ACCESS:y AND PUB_YEAR:[2016 TO 2026]` is run once, with no abstract fields returned. Hits are shuffled with `set.seed(20261103)` in R 4.6.0, and the returned and shuffled orders are archived with SHA-256 before any candidate is screened. The first eligible candidate is the primary and the second is the fallback. Screening stops after candidate 40, and P18 then stops.
3. **Estimand.** The two-component mean true effect (DBP, SBP; intervention minus comparator; mmHg) among studies that report both outcomes, under a bivariate normal random-effects model.
4. **Reproduction gate.** For each outcome separately: univariate DerSimonian-Laird with a z-based CI (`metafor::rma.uni(..., method="DL", test="z")`) on the printed study-level inputs, compared with the printed pooled values under R2. Where the paper states a different estimator, the stated estimator is used (R1). If either gate fails, the fallback is used; if the fallback also fails, P18 stops.
5. **Assumed within-study correlation, model and final rule.** These are B2.2, B2.3 and B2.5 of amendment 1, unchanged: ρ_w ∈ {0, 0.5, 0.8}, with no single primary value. Software defaults are used for every control list. App/R parity is |app − R| ≤ 1e-4 on every reported quantity.
6. **Classification at each ρ_w.** The bivariate result is compared with the paired univariate REML fit. The classification is **new** if any of the following holds for either outcome:
   - (i) the sign of μ differs;
   - (ii) whether the 95% CI excludes 0 differs;
   - (iii) |Δμ| ≥ 1.0 mmHg;
   - (iv) the CI-width ratio (bivariate over univariate) is outside [0.80, 1.25].
   It is **robust** if none of these holds and every gate passes, and **indeterminate** if any fit fails to converge or a gate cannot be evaluated. Boundaries: a |Δμ| equal to 1.0 triggers; a ratio equal to 0.80 or 1.25 does not.

## P20 note

Cowman's criterion (b) was "not verifiable" in screen 1 only because of the A3.1 contradiction. The Cowman clearance is re-run under A3.1a. B3.1 is otherwise unchanged: if any of (a)-(d) fails, P20 stops.
