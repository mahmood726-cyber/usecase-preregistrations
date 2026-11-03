# Protocol amendment 3, 3 November 2026: filter fix, four screening decisions, licence rule, and a redesigned P16

This amends `amendments/PROTOCOL_AMENDMENT_2026-11-02.md` (amendment 1, commit 4fadf392) and `amendments/PROTOCOL_AMENDMENT_2026-11-02b.md` (amendment 2, commit 6a2cdbb6). **It is committed and pushed before any candidate it governs is screened or re-screened.** Anything not changed here stands. The decisions in sections D–H are Mahmood Ahmad's, delegated on 3 November 2026; section C is a defect fix by the coordinator.

## Why

Under amendments 1 and 2 all five papers P16–P20 stopped without a release. Two of the stops came from defects or gaps in my own screening rules, not from the candidates:

- A3.1b did not match "significantly", and it was applied to Methods sentences only. P18 candidate C15 showed eight figure captions that stated the direction of pooled findings. C15 was disqualified (and was ineligible anyway).
- A3.1a showed only the first row of a supplement table. When that row is a merged title cell, the column headers sit in row 2 and could never be shown (P20, Cowman, criterion (b)).

The other stops came from eligibility rules that were stricter than the analysis needs (P17 Fisher z only; P18 criterion (d) observable only in Results; non-commercial licences). P16 stopped because its source does not publish per-study inputs.

## C. A3.1b fixed (replaces the A3.1b pattern list and its scope)

1. **Pattern.** The term `\bsignifican(t|ce)\b` is replaced by `\w*significan\w*`. This matches "significant", "significance", "significantly", "nonsignificant", "non-significant" and "insignificant". All A3.1b patterns are applied case-insensitively.
2. **Scope.** A3.1b now applies to **every sentence shown**, not only Methods: abstract sections permitted under A1.2, Methods, table captions, figure captions, and supplement captions or sheet names. Header cells are not sentences and are governed by A3.1c.
3. **Planted test.** Before first use, the extractor must drop each of these synthetic sentences: "Pain was significantly reduced (Figure 2).", "Results were non-significant.", "No insignificant trend was seen.", "Figure 3. Forest plot showing a significantly lower risk." It must keep "Heterogeneity was assessed with the I2 statistic." The test and its output are archived per A3.4.

## D. A3.1c. All header rows above the first data row (replaces "first row" in A3.1a; applies to every paper governed by rule A)

1. For a table in JATS `<thead>`, or in a supplement file opened under A3.1a, the display shows rows from the top **down to, but not including, the first data row**, at most 5 rows. Decimal redaction (A3.3) and A3.1b apply.
2. A row is a **data row** if any of the following holds:
   - (a) any cell contains a four-digit year from 1900 to 2099 (a study label such as "Smith 2010");
   - (b) at least half of its non-empty cells are numeric after removing spaces, `%`, `±`, parentheses, brackets, commas and range or CI dashes;
   - (c) it is a JATS `<tbody>` row.
3. A merged title cell, a column label, a unit label or a sub-header is a header row. If no data row is found within the first 5 rows, only row 1 is shown and any criterion that needed the column labels is judged **not verifiable**.
4. The row rule is applied by script before display. The number of rows shown per table is logged.

## E. P17 (B1) changes

1. **B1.1(b) replaced:** "it is a meta-analysis that pools Pearson correlation coefficients, either Fisher z-transformed or as untransformed r, with the pooling scale stated in its Methods". If Methods do not state the scale, (b) fails.
2. **B1.3 extended:** if the stated scale is untransformed r, R1 uses `yi = r` and `vi = (1 − r²)²/(n − 1)` (`metafor::escalc(measure="COR")`), unless the paper states another variance, in which case the stated one is used. Gate quantities are μ and μ ± z₀.₉₇₅·SE on the r scale, under R2.
3. **B1.4 extended:** on the untransformed scale the PI is μ ± t₀.₉₇₅,ₖ₋₁·√(τ² + SE²), on the r scale. An endpoint beyond ±1 is truncated to ±1, and the truncation is reported. The B1.6 labels then apply to these endpoints unchanged.
4. **B1.5:** if the pinned `correlation-ma` app does not pool untransformed r, every quantity on that scale is labelled R-only, and this is disclosed.
5. **Order:** unchanged (A4a). The re-screen starts again at candidate 1 of the archived order and stops at the second eligible candidate or after candidate 40.

## F. P18 (B2') changes

1. **B2'.1(d) replaced:** "the number of studies reporting both SBP and DBP, judged from a per-study table's caption or header rows (A3.1c) or from Methods, satisfies 10 ≤ k ≤ 60". The value used is the first that applies:
   - (i) a stated count of studies reporting both outcomes;
   - (ii) the smaller of stated per-outcome counts for SBP and DBP;
   - (iii) the stated number of included studies, when Methods state that both outcomes were pooled.
2. **Check at extraction.** If the extracted paired count is below 10, the candidate fails F1 and the next eligible candidate in the seeded order is used. This is not a data-driven choice: it only removes candidates that could not have met (d).
3. **B2'.1(a):** the licence list follows section G.
4. **Order:** unchanged (seed 20261103, archived orders). The re-screen starts again at candidate 1. C15 and C07 stay disqualified.

## G. Licences, from P16 onward

1. CC BY-NC and CC BY-NC-SA are acceptable, alongside CC0, CC BY and CC BY-SA, **for extracting numeric data** for this non-commercial academic reanalysis. ND licences, all-rights-reserved notices and unlicensed sources stay excluded.
2. **What is archived:** only the extracted numbers, with a full citation of the source. The article's text, tables and figures are never archived or redistributed.
3. This applies to P16 onward. The frozen rules of P02 and P04 are not changed.

## H. P20 (B3) change

Cowman's clearance is re-run with A3.1c in place of A3.1a's "first row". B3.1(a)–(d) are otherwise unchanged. If any of them fails, P20 stops.

## I. B4'. P16 redesigned: NMA inconsistency in a network whose per-study inputs are published (replaces B4.1; B4.2 and B4.3 stand)

Hodkinson et al. 2022 is dropped. Its supplement does not publish per-study non-HDL inputs (`cxPREP16/run4/P16/supporting/F1_HEADINGS_P16.txt`). A new candidate is screened under rule A.

1. **Eligibility.** All of the following must hold, judged from A1 material plus A3.1c header rows:
   - (a) licence as in section G;
   - (b) a frequentist network meta-analysis, with the model or software named in Methods (for example netmeta, Stata `network` or `mvmeta`, or a contrast-based graph-theoretical or multivariate model). Bayesian or unstated → fail;
   - (c) Methods state a global or local inconsistency assessment (design-by-treatment, node-splitting, side-splitting or loop-specific);
   - (d) the primary outcome is the first outcome Methods name as primary, otherwise the first named outcome. Its metric is OR, RR, HR, SMD or MD;
   - (e) header rows show per-study inputs for that outcome:
     - arm-level: treatment and n with events, or treatment, n, mean and SD;
     - or contrast-level: comparison, effect and SE or CI.
     
     An MD outcome needs arm-level SDs (see I.4);
   - (f) the printed k for that outcome, otherwise the printed number of included studies, satisfies 10 ≤ k ≤ 100;
   - (g) it was published 2016–2026, it is not Hodkinson 2022, and it is not a candidate disqualified under A3.5;
   - (h) F2 novelty: no published re-analysis of this network's inconsistency.
2. **Order.** The Europe PMC query `(TITLE:"network meta-analysis") AND OPEN_ACCESS:y AND PUB_YEAR:[2016 TO 2026]` is run once, with no abstract fields returned. Hits are shuffled with `set.seed(20261104); sample()` in R 4.6.0. The returned and shuffled orders are archived with SHA-256 before any candidate is screened. The first eligible candidate is the primary and the second is the fallback. Screening stops after candidate 40; if none is eligible, P16 stops.
3. **Reproduction gate.**
   - R1 applies. Unstated elements take the pinned netmeta defaults.
   - The gate quantity is the random-effects network estimate (or the common-effect estimate, if that is the only one the source reports) and its 95% CI:
     - for the first non-reference treatment in the source's primary-outcome league table or forest plot, against the source's reference;
     - if the source prints neither, for the first network estimate printed for the primary outcome.
   - R2 applies. Ratio measures are compared on the printed scale. If the gate fails, the fallback is used; if that fails too, P16 stops.
4. **Estimand and classification.** These are P16 prereg §7 and §8 with outcome-specific terms made generic. The diagnostics are:
   - the global between-design Q (`decomp.design`, Q.inc.random.preset);
   - the back-calculation `netsplit` random-effects differences, with Holm adjustment over all eligible pairs.

   A local signal is Holm p < .05 **and** |δ| at least:
   - ln(1.25) for log OR, RR or HR;
   - 0.20 for SMD;
   - for MD, 0.2 × the median arm-level SD of the extracted input rows. This is computed from the inputs before any network is fitted.

   "Previously reported comparisons" are the pairs the source itself reports as inconsistent at p < .05. Those pairs are read only at extraction, after release. The labels New, Robust, Previously reported pattern only, and Indeterminate are as in §8.
5. **App.** The `nma-inconsistency` app with multi-arm support (allmeta PR #464). The commit is pinned in the P16 prereg before release. Parity is as in B4.3.
