# Feasibility of P14 and P06 multi-meta-analysis pilots

DRAFT ONLY. Search date: **2026-10-27**; screening completed 2026-10-28. A provisional, unlocked screening selection exists; no trial data have been extracted and no meta-analysis run. Nothing has been published or deposited. Read with [P14 draft](PREREG_DRAFT_P14.md), [P06 draft](PREREG_DRAFT_P06.md), [search/access log](SEARCH_LOG.md), and [complete count-screen ledger](SCREENING_COUNTS.md).

## Observed yield (frame retrieved 2026-10-27; screening completed 2026-10-28)

This section replaces the 2026-10-27 "access failed" statements. The sandbox could not reach Europe PMC; pc2 could, and it retrieved both complete frames. The first-page web counts F14/F06/F06b below are kept for the record. They were never Europe PMC totals and play no part in the frame.

| Pilot | hitCount | Retrieved | Deduplicated frame | Screened | Eligible (after AM-S8) | UNRESOLVED (not eligible) | Yield (Wilson 95% CI) | Eligible in frame |
|---|---:|---:|---:|---|---:|---:|---|---|
| P14 | 3436 | 3436 | 3433 | 3433 (frame exhausted) | **18** | 152 | 0.52% (0.33%-0.83%) | 18 (complete count) |
| P14 reserve (AM-P14-R) | 730 | 730 | 730 | 730 (frame exhausted) | **5** | 42 | 0.68% (0.29%-1.59%) | 5 (complete count) |
| P06 | 5207 | 5207 | 5205 | 3300 (selection = first 30, stopping rank 2769) | **36** | 67 | 1.09% (0.79%-1.51%) | ~57 projected (41-78) |

Sources:
- `MMA_frames_2026-10-27/<pilot>_pull_manifest.json`
- `<pilot>_dedup_log.json`
- `screening/SCREENING_LEDGER_<pilot>.csv` (every screened record with its stage and reason)
- `screening/YIELD_SUMMARY.json`
- `screening/SELECTION_<pilot>_provisional.json`

**Leading exclusion reasons (first failing criterion).**
- **P14:** title/abstract POPULATION 838; title/abstract fewer than 10 RCTs 626; title/abstract DESIGN 600; not a meta-analysis 365; full-text DESIGN 286; full-text POPULATION 269; full-text k outside 10-60 244.
- **P06:** title/abstract DESIGN 991; title/abstract fewer than 10 RCTs 818; title/abstract POPULATION 407; full-text DESIGN 278; not a meta-analysis 227; full-text k outside 10-60 209.

**Feasibility decision: established at the screening level for both pilots** (P14 18 plus a reserve of 5, P06 36; at least 10 each). Gate attrition, from extraction agreement, reproduction and app/R agreement, is still ahead. P14 has 18 main reviews plus a pre-specified reserve of 5 (AM-P14-R). Its age rule (AM-S6, kept under AM-S6b) is the binding constraint.

Earlier first-page web counts, kept for the record:

| Search / source | Records returned for inspection | Likely-eligible proxy | Unresolved | Visible exclusion | Confirmed eligible |
|---|---:|---:|---:|---:|---:|
| F14, first returned web-search page | 14 | 3 | 6 | 5 | 0 |
| F06, first returned web-search page | 14 | 0 | 4 | 10 | 0 |
| F06b, additional exploratory web-search page | 14 | 2 | 4 | 8 | 0 |

## Harness-store topic overlap

Source: in/meta-harness_topics.txt, read 2026-10-27. The file contains **43 entries: 38 clinical topic folders, 2 support folders and 3 JSON files**. Exclude `cache/comparators`, `cache/regulatory`, `cache/dual_spans_sample.json`, `cache/embeddings.json`, and `cache/recover_spans_sample.json` from topic denominators.

The mapping below is a deliberately broad *label-level possibility* assessment. "Plausible" means the named intervention/outcome can occur in the field; "conditional" means the actual age/cancer subgroup and endpoint would have to match. No folder contents or trial rows were examined. This is not a count of eligible reviews, matching trials, or validated reusable datasets.

| Clinical topic, under cache/ | P14 paediatrics | P06 oncology | Required limitation |
|---|---|---|---|
| antibiotics-vs-appendectomy-appendicitis | Plausible | No designated overlap | Actual paediatric trial membership required. |
| probiotics-aad-prevention | Plausible | Conditional | Cancer use must concern antibiotic-associated diarrhoea, not a different diarrhoea endpoint. |
| vitamin-d-acute-respiratory-infection | Plausible | No designated overlap | Paediatric respiratory-infection effects only; cancer outcomes cannot be substituted. |
| zinc-common-cold-duration | Plausible | No designated overlap | Paediatric duration data required. |
| balanced-crystalloids-vs-saline-mortality | Conditional | No designated overlap | Paediatric mortality, not adult ICU effects or a different endpoint. |
| colchicine-recurrent-pericarditis | Conditional | No designated overlap | Paediatric recurrence data required; adult trials cannot be transferred. |
| corticosteroids-cap-mortality | Conditional | No designated overlap | Child pneumonia mortality in the exact original comparison. |
| hfnc-vs-conventional-o2-reintubation | Conditional | No designated overlap | Paediatric reintubation; not bronchiolitis escalation of care. |
| melatonin-primary-insomnia-sol | Conditional | No designated overlap | Child primary-insomnia sleep-onset latency; other sleep disorders do not automatically match. |
| prone-positioning-ards-mortality | Conditional | No designated overlap | Paediatric ARDS mortality, not adult ARDS. |
| semaglutide-obesity-weight | Conditional | No designated overlap | Adolescent weight outcomes, not adult cardiovascular events. |
| doac-vte-recurrence | No designated overlap | Conditional | Cancer-associated VTE recurrence and the same comparator; general-population estimates do not suffice. |
| denosumab-vertebral-fracture | No designated overlap | Conditional | Cancer-therapy fracture prevention; skeletal-related events or metastasis endpoints are not interchangeable. |

Counts: **P14 11 possible topic overlaps = 4 plausible + 7 conditional; P06 3 conditional possible overlaps, with 0 explicitly cancer-labelled folders.** One topic (probiotics) overlaps both lists, so their union is 13/38, not 14. The remaining 25 have no designated overlap under this title-level rule. This is a reproducible conservative mapping, not an assertion that other cross-field relationships are impossible.

Remaining topic labels: azithromycin-copd-exacerbation; colchicine-postop-af; colchicine-secondary-cv-prevention; corticosteroids-covid19-mortality; dapagliflozin-hfpef-hosp; dpp4-mace-t2d; empagliflozin-hfpef-hosp; esketamine-trd-madrs; finerenone-ckd-t2d-renal; glp1-ra-mace-t2d; iv-iron-hfref-hosp; metformin-pcos-ovulation; noac-vs-warfarin-af-stroke; omega3-cardiovascular-events; pcsk9-mace; sacubitril-valsartan-hfref; semaglutide-obesity-mace; sglt2-ckd-progression; sglt2-hfref-hosp-cvdeath; sglt2-primary-prevention-hf; spironolactone-hfref-mortality; statins-primary-prevention-elderly; ticagrelor-vs-clopidogrel-acs; tocilizumab-covid19-mortality; tranexamic-acid-pph. Their labels predominantly describe adult cardiometabolic, obstetric or other populations/endpoints; no specific paediatric/cancer match is inferred merely because such patients can have comorbidities. Potential cancer-incidence endpoints in cardiovascular trials are not the cardiovascular rows stored here.

**Verified review-level matches: 0 for each pilot; actual reusable-row counts unknown.** These zeros record the absence of verification in this lane, not a finding of no overlap.

## Reuse and interpretation constraints

A row originating in meta-analysis X can only be used to reanalyse X. It must match X's trial membership, population, comparison, outcome, time point and effect metric and be checked against X's forest plot. Topic coincidence or a shared trial citation is insufficient. All other rows must be independently double-extracted by Codex and agy, adjudicated, and reproduce the original pooled estimate within the preregistered rounding tolerance. Reused rows receive independent source verification and the same gates.

P14 will distinguish later publications from documented later recruitment starts; missing start dates produce bounds, not an assertion of wasted participants. P06 will distinguish an asymmetry flag from the result of its fixed PET-PEESE adjustment. Null, unchanged, and non-estimable outcomes must all be reported transparently.

LANE DONE
