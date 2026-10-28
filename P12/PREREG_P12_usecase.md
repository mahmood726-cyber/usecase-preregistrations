# P12 pre-registration v4: limit meta-analysis of probiotics and ventilator-associated pneumonia

**DRAFT for freeze; no extraction or analysis has been performed.** Date: 2026-10-28. F1-F6 verdict: **NONE outstanding**; this is not a public release.

Paper: P12, *Limit meta-analysis in the browser: a tool validated against the R package metasens*. Target journal: Critical Care Explorations, task-specified; manuscript confirmation remains unavailable. [CONTRACT_P12.md](supporting/CONTRACT_P12.md) is a normative part of this preregistration, retaining the complete input, verification, analysis and comparison rules. [EVIDENCE_P12.md](supporting/EVIDENCE_P12.md) supplies source, novelty and static implementation evidence; [DEPENDENCIES_P12.json](supporting/DEPENDENCIES_P12.json) records measured hashes.

## 1. Selected meta-analysis and fallback

**Primary:** Cheema HA et al. *Probiotics for the Prevention of Ventilator-Associated Pneumonia: An Updated Systematic Review and Meta-Analysis of Randomised Controlled Trials*. Nutrients. 2022;14(8):1600. [DOI 10.3390/nu14081600](https://doi.org/10.3390/nu14081600). CC BY 4.0.

**Mandatory fallback:** MacKinnon KM, Seshadri S, Mailman JF, Sy E. *Impact of Rounding Checklists on the Outcomes of Patients Admitted to ICUs: A Systematic Review and Meta-Analysis*. Critical Care Explorations. 2024;6(8):e1140. [DOI 10.1097/CCE.0000000000001140](https://doi.org/10.1097/CCE.0000000000001140). CC BY-NC-ND 4.0.

Selection uses published features: the primary's unresolved clinical question, Egger p = 0.012, I-squared = 61% and k = 18. Its DOI was previously found in a search-indexed official AWMF evidence appendix; direct retrieval was blocked, so no inspected recommendation or endorsement is claimed. The fallback offers target-journal relevance and its own reported hospital-LOS asymmetry. Neither an extracted SE distribution nor an adjusted result informed selection; attenuation is not presumed.

Both candidates are **FEASIBLE-IMAGE**, with no equivalent application identified in the supplied approved novelty checks. Before sensitivity analysis, source infeasibility, confirmed equivalence or final reproduction failure activates the fallback. The fallback activates only while its own feasibility and novelty checks are cleared; otherwise stop. Pending/blocked evidence is not a zero-hit finding: resolve it or record exclusion through a public pre-extraction amendment. Both-fail means report both reasons and stop, with no other candidate/outcome. After any sensitivity result, failures produce an indeterminate report without switching.

The total effort cap is four analyst hours across both candidates, clearance, extraction handling, reproduction, analysis and drafting, excluding human-verification waiting. At exhaustion report the incomplete stage without relaxing checks.

## 2. Fixed outcomes, original model and estimand

| Item | Primary | Fallback |
|---|---|---|
| Outcome | VAP incidence; original overall synthesis and trial-specific follow-up | Hospital length of stay; observational synthesis |
| Comparison | Probiotics/synbiotics versus placebo/usual care in mechanically ventilated adults | ICU rounding checklist versus no checklist |
| Published pooled target | RR 0.68 [0.55, 0.84] | SMD -0.19 [-0.36, -0.03] |
| k | 18 | 11 |
| Analysis scale | Log RR; negative favours probiotics | Printed SMD, checklist minus control; negative favours checklist |
| Stated model | IV DL random effects; RevMan 5.4 | IV DL random effects; RevMan 5.4, Stata/MP 15.1 and RStudio 1.4.1106 named |

The exact CI algorithm is **NOT STATED**; both forests print a Z test. Explicit ratio-pooling transformation and the fallback's per-forest software assignment/SMD variant are **NOT STATED**. F3 fixes exactly one RevMan 5 default reproduction configuration: inverse-variance DL random effects, log RR or unchanged printed SMD, classic normal 95% CI, with no HK, alternative estimator/software search, continuity correction or reconstruction from arm summaries. These are prespecified defaults, not claims of explicit source documentation. Contract sections 2, 3 and 6 fix the remaining input and R options.

The sensitivity estimand is beta0 = beta_r + tau * alpha_r, the expected effect as SE approaches zero under the extended random-effects model, distinct from the ordinary Egger intercept.

## 3. Sources and frozen inputs

Primary: `P12_primary/supp/nutrients-14-01600-g003.jpg`, Figure 3, publisher-PDF locator page 8; `Study or Subgroup` and `Risk Ratio / IV, Random, 95% CI`. Panel ID: `Cheema2022_Fig3_VAP`.

Fallback: `P12_fallback/supp/cc9-6-e1140-s001.pdf`, Figure S8, PDF/printed page 36; `Study or Subgroup` and `Std. Mean Difference / IV, Random, 95% CI`. Panel ID: `MacKinnon2024_FigS8_hospitalLOS`.

After release, independently read labels, effects and CI endpoints from these readable images; retain exact strings and source order. Effects/endpoints have two printed decimals; no SE column. With z = 1.959963984540054, primary yi = log(RR), sei = (log(U)-log(L))/(2*z); fallback yi = SMD, sei = (U-L)/(2*z). Do not round further or recenter estimates. R-only preparation performs these transformations and exponentiates primary estimates/CI endpoints for presentation, never SEs.

No counts/means reconstruction, digitisation of plot coordinates, imputation, new correction, arm splitting/combination, primary-study retrieval, borrowed rows, exclusions or alternate time points. Rows from a review are used only for that review. Missing/nonfinite required values, unresolved mapping or incompatible dependence fail the gate; the app cannot detect shared controls or supply missing design adjustments. Contract section 3 fixes the numerical-source hierarchy and header-free `effect,SE,label` entry into `#src`, with unique safe IDs and exact k/order/value checking.

## 4. Extraction and verification

**Verbatim MAHMOOD_DECISIONS.md item 4:**

Human verification: humans check headline rows, a seeded 5% of the other rows (at least 1), and only the fields still disputed after a third-model adjudication plus a fourth AI re-check (agy, different family). If the sample error is over 2%: a full AI re-extraction plus a human re-check of the headline rows. Packets are about 30 minutes or less; at most one per person per week across all papers (COAUTHOR_LOAD.md); Mahmood is in the rota; a packet not returned in 7 days is reassigned.

After release, Codex and agy double-extract independently and blind to one another; agy's different model family is read back from its log. A third model adjudicates discrepant fields; agy in a family different from that adjudicator re-checks every adjudicated field. Only remaining disputes go to humans. Record sources, model identities, decisions and verifier initials/date in `VERIFICATION_LOG.csv`.

Headline rows have normalized DL weight >=10%, any tied minimum/maximum SE, or a deletion changing beta0 by >=0.10 analysis-scale units, its sign, CI null-exclusion status or classification; refused/indeterminate deletions are included. Each deletion uses its own refitted ordinary and limit models.

Order remaining rows by lowercase SHA-256 of UTF-8 `2026102812|P12|<row key>`; sample `max(1, ceil(0.05*n))` when n > 0, none when n = 0. Contract section 4 fixes compact-JSON serialization of lowercase review DOI, panel ID, one-based source index and NFC label, lexical tie-breaking, stable identities, the union of ever-flagged headlines and retention of the original sample/error denominator.

Any required-field/mapping error makes a sampled row erroneous. Above 2%, repeat full AI double extraction/adjudication and human headline re-check, retaining unresolved-dispute checks. Never replace this with universal human review or redraw to dilute errors. Corrections require gate/analysis reruns and checks of newly flagged/changed rows. Release no substantive result before verification completes.

Allow five minutes per row plus five administration: at most five rows per approximately 30-minute packet; split further as needed. Eligible P12 verifiers are MA, SA, GKA, AK, AO and AW. Claim a planned slot in the shared `pipeline/COAUTHOR_LOAD.md` ledger before sending; enforce one packet per ISO week across all papers, include Mahmood, and reassign after seven days.

## 5. Ordered reproduction gate

Only after public release, mandatory implementation/synthetic conditions and AI reconciliation, run the original-model reproduction in R. Require the point estimate and each CI endpoint separately within **0.005** of the section 2 printed targets, with exact k and matching direction and null-exclusion category. Compare RR on its presentation scale and SMD on its original scale.

No real-data app load or `limitmeta` call precedes a code-generated passing receipt. On initial failure allow one source-documented transcription correction through the same adjudication workflow and one unchanged-gate rerun; otherwise primary, fallback, stop. Do not change printed numbers, conventions, models or tolerances to obtain agreement.

A passing gate permits provisional sensitivity/deletion fits for verification targeting. Corrections invalidate prior results and require reproduction and analyses again; this is verification escalation, not another tuning attempt. After sensitivity begins, unresolved correction, gate or implementation failure is indeterminate without candidate switching. Contradictory documentary evidence requires a public pre-extraction amendment, never post-result model tuning.

## 6. Exact analysis and agreement

Use `ALLMETA/limit-ma/index.html`, supplied commit `14dc545bcba87a02158b2f445c28450e7eaf6b89`; automatic linear axes, DL/beta0, 95% normal intervals, comparison alpha 0.10, binary-count input empty, no moderators or subgroups. Automatically computed unselected methods are provenance only.

Independent desktop R is **4.6.0**, **meta 8.5.0**, **metasens 1.5.3**, **metafor 5.2.1**. Contract section 6 fixes exact `meta::metagen`, `metasens::limitmeta` and `meta::metabias` calls, including GEN input, DL, classic CI, no prediction interval or tau CI, no backtransformation, and beta0 adjustment. Assert versions and archive sessionInfo/signatures/help. Preserve package internal REML refusals without optimizer/control substitutions.

Secondary outputs are tau-squared, alpha_r, beta_r, G-squared, Q.small/Q.resid with chi-square df 1/k-2, and Egger's two-sided t statistic with df k-2 and k.min=10. P-values are descriptive.

Contract section 6 fixes the entire full/deletion manifest and capture order, raw comparison snapshot, main JSON/CSV, dedicated deletion CSV and state invalidation. Obtain missing ordinary-deletion SE/CIs independently through pinned `AlmMaCore.pool` and the normal formula, never by reconstructing them from R's output. Its section 8 labels external transformations, weights/classification, verification orchestration and figure composition **R-only**, with each implementation's quantities kept separate.

Every finite scalar must satisfy **abs(app-R)/max(1,abs(R)) <= 1e-9**, including derived/deletion quantities. Identities, order, lengths, statuses, df and classifications match exactly. The comparison-panel full-fit status is authoritative; finite main output cannot override refusal. Preserve raw messages and explicit undefined values. Matched primary refusals imply indeterminate results; a matched undefined secondary diagnostic alone does not invalidate a finite agreed primary fit. Unknown/unmatched statuses or unresolved discrepancies prohibit classification.

## 7. New versus robust

On analysis scale let theta be the ordinary estimate and L be beta0. Sign categories are negative/zero/positive. A 95% CI is negative-excluding-zero if upper < 0, positive-excluding-zero if lower > 0, otherwise null-including, including endpoints exactly zero.

**New:** sign change, CI-category change, or abs(L-theta)/abs(theta) >= 0.20. **Robust:** same sign and CI category with relative change < 0.20. If theta = 0, sign/CI change is New; otherwise indeterminate. Undefined primary fits or unresolved implementation disagreement are indeterminate, never robust. Each deletion uses its own ordinary/limit pair. Apply unrounded values without epsilon. Report attenuation or amplification; these are descriptive, not clinical-importance thresholds.

## 8. Novelty screening and deviation

Europe PMC and OpenAlex replace Google Scholar under Mahmood's decision: Scholar showed a bot check ("unusual traffic") on 2026-10-28 and was not bypassed.

| Candidate | Europe PMC: metadata / hitcount / retrieved | OpenAlex: metadata / retrieved | Flagged in each |
|---|---|---|---|
| Cheema | 28 / 31 / 31 | 45 / 44 | 0 |
| MacKinnon | 4 / 4 / 4 | 3 / 3 | 0 |

The supplied 2026-10-28 logs identify no equivalent application; both candidates clear the approved screening. OpenAlex's logged `complete=true` does not eliminate the primary's count discrepancy. These summary logs lack complete citing-record inventories/full request URLs and are not a full-text citation audit. Do not sum overlapping indexes. Literal supplementary PubMed queries, counts (7/0), record IDs and historical blocked attempts are retained in the evidence file.

Equivalence means beta0 limit meta-analysis of this review's same fixed outcome and included synthesis, irrespective of software/agreement. Confirmed equivalence excludes; uncertain overlap requires source-based clearance before extraction.

## 9. Static app evidence

[EVIDENCE_P12.md](supporting/EVIDENCE_P12.md) maps files, functions and SHA-256 to every registered app capability; [DEPENDENCIES_P12.json](supporting/DEPENDENCIES_P12.json) records all 32 direct resources, which exist, plus named dynamic targets. Six source hashes match v3. Static availability is not runtime certification.

The embedded build-info commit differs from the supplied pin; the snapshot lacks Git ancestry. Use the supplied pin and measured bytes, not the display stamp. Optional WebR runtime/package-manifest files are absent; desktop R is required. No browser/R execution or corpus replay occurred here.

## 10. Mandatory post-release, pre-analysis conditions

1. Synchronize CODE/KIT with the normative contract: JSON/NFC keys, source IDs, ordinary-deletion uncertainty capture, persistent headline/sample history, all options, manifest, statuses and ordered release/gate safeguards. Obtain prior CODE/KIT artifacts from the coordinator; they are not included in this workspace. Version/hash the aligned `code/` bundle.
2. Run only newly generated `synthetic_*` fixtures marked "SYNTHETIC - not data" in their first line or column. Pass the complete app/R manifest at unchanged tolerances, refusal/undefined/boundary cases, export round trips, deletion invalidation and figure/inset checks.
3. Demonstrate browser dependency closure for the registered route, including dynamic loads and actual exports. Prevent bundled examples, restored inputs and archived corpora from running; the page automatically runs on load. Optional WebR is outside this route.
4. Sync the extraction kit to the released preregistration and assign compliant COAUTHOR_LOAD packets before human verification.

**Code must pass synthetic validation before any real-data reproduction gate.** Every post-release code change is a dated deviation independent of real-data results. Unresolved parity discrepancies stop analysis; static readiness does not waive these conditions. Extraction also requires the release records below.

## 11. Write-up and amendments

Retain the existing example; add 150-250 words plus one figure, or Extended data where necessary. Start with one clinical sentence about sensitivity of the designated association and explain beta0's added information. Report original/reproduced/limit estimates, uncertainty, classification, both implementations and limitations regardless of outcome.

Frame as "a re-analysis illustrating sensitivity to small-study effects." Clinical differences related to precision can produce asymmetry; adjustment neither proves publication bias nor removes confounding. Show the analysis-scale effect-versus-SE funnel/fitted curve with an R-only inset of ordinary/limit estimates/CIs. Mahmood dictates the final paragraph. No clinical recommendations, priority/ranking claims or publication-error allegations.

2026-10-28 amendments: preserve the approved Scholar substitution and v3 fixed-default/source decisions; v4 applies F1-F6, reproduces item 4 verbatim, labels R-only work and moves implementation/runtime conditions to section 10. Detailed blocker dispositions are in [V4_NOTES_P12.md](V4_NOTES_P12.md). Subsequent substantive amendments require a public version, reason and disclosure of data/results already seen; prospective status cannot be assigned retrospectively.

## 12. Freeze and release

F1-F6 are satisfied; [BLOCKERS_P12.md](BLOCKERS_P12.md) contains `NONE`. Release P12 separately in `mahmood726-cyber/usecase-preregistrations` at `P12/PREREG_P12_usecase.md`, including these normative supporting files and versioned implementation provenance. Record exact file hashes, public GitHub release URL/server UTC timestamp and Zenodo archival DOI. Neither public record exists in this job; both must precede extraction and real-data analysis.

Archive source provenance, model identities, verified extraction, logs, code, both implementations' outputs and deviations. Every reported number must trace to an unchanged published pooled summary, verified extraction or preserved calculation. No author contact, login, paywall workaround or bot-check bypass.

**sha256 and UTC freeze time recorded at release**
