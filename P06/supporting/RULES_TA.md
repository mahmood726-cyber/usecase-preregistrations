# Title/abstract screen (stage B) — instructions for the screener

You screen bibliographic records (title + abstract only) for a meta-research pilot. You are NOT selecting
interesting reviews. Never consider the direction, size or significance of any result. Never record any
effect estimate, CI, p-value or participant number.

Pilot ID is given in the batch file header: P14 (paediatrics) or P06 (oncology).

Decide for each record: `FULLTEXT` (needs full-text check) or `EXCLUDE` (abstract alone shows a clear
failure). **When in doubt, FULLTEXT.** Exclude only when the title/abstract makes the failure explicit.

Exclude codes (use the first that applies, in this order):
- `NOT_MA` — not a quantitative meta-analysis (narrative/scoping/systematic review stated as without
  meta-analysis, editorial, letter, commentary, correction/erratum notice, retraction notice, trial report,
  or a protocol for a future review).
- `DESIGN` — the quantitative synthesis is clearly not a conventional pairwise meta-analysis of randomized
  trials: network meta-analysis (as the main synthesis), diagnostic-test-accuracy, prognostic/biomarker,
  prevalence/incidence, observational/nonrandomized studies only, umbrella review/overview of reviews,
  individual-patient-data-only, dose-response-only, Bayesian-only, trial-sequential-analysis-only report of a
  previous meta-analysis, single-arm/proportion meta-analysis, cost-effectiveness.
- `POPULATION` —
  - P14: participants are clearly not children aged 0–17 at trial entry (adult-only; or trials randomize
    pregnant women before birth; or the population explicitly spans adults and children with no
    paediatric-only primary analysis indicated). A paediatric subgroup mentioned only as secondary does not rescue it.
  - P06: participants clearly do not all have a diagnosed malignant cancer (primary prevention or
    screening in people without cancer; cancer incidence as an adverse event in non-cancer trials; benign
    disease; cancer-free carriers of risk mutations; precancerous lesions only). Supportive care and survivorship in people with
    a cancer diagnosis are IN. Paediatric oncology is IN.
- `K_LT_10` — the abstract states the TOTAL number of included randomized trials (or included studies) and
  it is fewer than 10. (If the abstract gives only a larger total, or no number, do not use this code.)

Otherwise `FULLTEXT`.

Return one entry per record, in the input order, with the record's `rank`, `decision`, `reason_code`
(`NONE` for FULLTEXT) and a reason of at most 25 words that quotes or paraphrases the decisive phrase.
