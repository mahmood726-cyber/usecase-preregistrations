# P08 pre-registration v4: study-level moderators in nephrology meta-analysis

**DRAFT for freeze; no extraction or analysis has been performed**

2026-10-28. Paper P08; target journal: **Nephrology Dialysis Transplantation** (TASK_PAPER.md; manuscript.txt does not independently identify the journal). This is a freeze candidate, not a release. F1–F6 verdict: **NONE** outstanding; execution conditions remain mandatory.

## 1. Chosen meta-analysis and fallback

**Selected primary:** Veltkamp DMJ, Porras CP, Gant CM, Tiel Groenestege WM, Kok MB, Verhaar MC, van Solinge WW, Haitjema S, Vernooij RWM. Long-term risks of adverse kidney outcomes after acute kidney injury: a systematic review and meta-analysis. *Nephrology Dialysis Transplantation*. 2025;40(11):2143–2158. DOI: https://doi.org/10.1093/ndt/gfaf093. CC BY 4.0. Target-journal publication meets the profile criterion. The clinical question concerns kidney outcomes after AKI; the added question concerns diabetes prevalence adjusted for cardiovascular-surgery setting. The supplied main Methods, Figure 6 and supplementary Figures S6A–C report covariate analyses; no explicit joint diabetes-prevalence-plus-cardiovascular-surgery model was located in those materials. This is a bounded statement about reported methods. A subsequently confirmed equivalent analysis excludes this candidate under the existing novelty rule. *(Narrowed pre-freeze per REDTEAM2 RT2-02.)*

**Fallback:** Liu C, Yang L, Wei W, Fu P. Efficacy of probiotics/synbiotics supplementation in patients with chronic kidney disease: a systematic review and meta-analysis of randomized controlled trials. *Frontiers in Nutrition*. 2024;11:1434613. DOI: https://doi.org/10.3389/fnut.2024.1434613. CC BY, version unspecified in supplied XML. Published duration subgroups motivate continuous-duration regression.

V3 incorrectly treated Veltkamp's unstated original model as an automatic feasibility failure. V4 corrects that criteria misapplication before any study-level data were extracted or analysed. F1 is FEASIBLE-IMAGE; F3 is resolved by one fixed configuration below. Liu remains the fallback.

Switch only for failure of primary source access, novelty, source-supported identity/independence mapping, complete-case eligibility, or the fixed reproduction gate. Liu activates only after its own feasibility, novelty and profile clearance, including assessment-duration and independence mapping; otherwise stop. If Liu fails, stop; no third candidate, result-based return or outcome switching. Implementation failure pauses work for synthetic-only correction, never selects a candidate. Effort ceiling: four hours of analysis work, excluding verification queues.

## 2. Fixed outcome and estimand

| Item | Veltkamp | Liu |
|---|---|---|
| Outcome/comparison | CKD incidence or progression combined; AKI versus no AKI | Figure 4A CRP contrast; probiotics/synbiotics versus original control |
| Printed pooled result | HR **2.38 (95%CI 1.93–2.84)**; OR **2.92 (95%CI 2.64–3.20)** | **SMD: −0.34; 95% CI: −0.62, −0.07** |
| Count | Independent outcome-specific k not certified; v3's “40 cohorts” was not verified as a printed count | **Ten studies** |
| Reported model | Random effects; original package/function, estimator, CI construction and pooling scale NOT STATED | Figure 4A: **IV, Random, 95% CI**; synthesis software RevMan 5.4 |

Primary estimand: study-level log-ratio slope per 10 percentage-point higher AKI-group diabetes prevalence, adjusted for cardiovascular-surgery setting. Prefer HR; use OR only when HR is unavailable for that independent cohort. This mixed-measure slope is descriptive, not a common HR or individual causal effect.

Fallback estimand: CRP SMD slope per additional treatment month. Negative means greater CRP reduction. Table 1's **Median follow-up (months)** must be shown to represent treatment duration at the plotted assessment; it is not automatically equivalent. No substitute follow-up estimand.

## 3. Data sources and eligibility

[Source audit](supporting/SOURCE_CHECK_P08.md) and [file hashes](supporting/FILE_HASHES_P08.json) are incorporated.

Veltkamp: supplied `P08_primary/supp/gfaf093fig2.jpg`, Figure 2 HR/OR panels, **Authors, Year**, **OR/HR [95% CI]**, setting, outcome/adjustment annotations. Table 1 (`tbl1`) in `fulltext.xml`: Authors, Year, Setting, AKI component of **DM (%)** under AKI/no AKI. Forest numbers are readable images; moderator cells are text. Supplied supplement figures S1–S6 and tables are accessible. No digitization from plotted symbol positions.

Liu: `P08_fallback/supp/fnut-11-1434613-g004.jpg`, **Figure 4A only**, Study or Subgroup, printed SMD and limits; Table 1 (`tab1`), Authors, Study period, Study design, Intervention, Median follow-up (months), Comparator. The DOCX supplement supplies no additional CRP inputs. Printed effects/limits have two decimals.

After release preserve raw fields separately from derivations. Do not reconstruct effects from arm counts, impute, choose assessments by effects, contact authors or retrieve primary studies. Resolve overlap/shared controls and assessment mapping from permitted sources. Unresolved identities, ties after HR preference, or dependence fail eligibility. Reproduce each original HR/OR panel with its own membership, irrespective of moderator completeness; deduplicate for the new regression only. Rows from one meta-analysis are used only to re-analyse that meta-analysis.

Primary regression requires **10–60** independent complete cohorts, **at least five per setting**, varying diabetes within each setting, and full rank. Define `D=AKI DM percentage/10`; `S=1` for Table 1's cardiovascular-surgery category, `0` for other known categories. Unknown setting/DM is missing, never zero. Fallback requires **all ten** independent CRP studies with unambiguous varying duration in months as printed, finite effects and positive variances. Quantitative eligibility remains unrun.

## 4. Extraction and verification

Binding MAHMOOD_DECISIONS.md item 4, copied exactly:

> Human verification: humans check headline rows, a seeded 5% of the other rows (at least 1), and only the fields still disputed after a third-model adjudication plus a fourth AI re-check (agy, different family). If the sample error is over 2%: a full AI re-extraction plus a human re-check of the headline rows. Packets are about 30 minutes or less; at most one per person per week across all papers (COAUTHOR_LOAD.md); Mahmood is in the rota; a packet not returned in 7 days is reassigned.

Independent, mutually blinded Codex and agy extractions; agy's different family and exact identifier are confirmed from logs. Third-model adjudication is followed by a fourth agy pass from a different family than the adjudicator. Only still-disputed fields escalate.

Headline rows are the union of deletion-induced target-slope change ≥**0.5 full-fit SE**, sign or CI-exclusion change, section 7 classification change, fitting failure, ≥**10%** fitted weight, and all moderator extrema including ties. Primary weight checks use both full/reduced models; target slope is adjusted D. Fallback uses the duration model. Binary S extrema select **every eligible primary row**; this consequence is retained.

Seed `2026102808`; order remaining rows by lowercase SHA-256 of UTF-8 `2026102808|P08|<row key>`, then key; take `max(1,ceil(0.05*n))` if any remain. A sampled row is erroneous if any required field or identity/assessment mapping disagrees with its source. Error rate is erroneous sampled rows / sampled rows, by round; **>2%**, not ≥2%, triggers escalation. Keep membership and corrections logged. Rerun reproduction and analysis after corrections.

[Verification and kit contract](supporting/VERIFICATION_P08.md) fixes keys, deletion fits, excluded-row disputes and packet implementation. Record source, fields, decisions, initials and dates in `VERIFICATION_LOG.csv`. Maximum five rows per packet: five minutes setup plus five per row. Split further if needed. Use the shared COAUTHOR_LOAD ledger; eligible P08 verifiers are MA, SMA, QFH, HK and AW.

## 5. One reproduction configuration and stop rule

R-only reproduction precedes every new regression. Compare the point and **each** CI endpoint, unrounded, within **0.005** on the printed scale. Require finite ordered intervals containing each printed estimate and positive derived variances. Correct only source-verified transcription/mapping mistakes; never widen tolerance or search models.

**Veltkamp:** R 4.3.2/RStudio are stated; a meta-analysis package and pooling details are NOT STATED. Prespecify R/metafor as the implementation, using its REML/z estimator/inference defaults. This is our assumption within the stated R ecosystem, not an attribution of metafor use to the authors or a claim that R has a universal meta-analysis default. Symmetric-looking pooled ratio intervals motivate the explicit **natural-scale** assumption.

For HR and OR separately, set `yi=printed ratio`, `vi=((upper-lower)/(2*1.959963984540054))^2`; fit an inverse-variance, intercept-only random-effects model with `method="REML",test="z",level=95,weighted=TRUE`. No logarithm/back-transform for reproduction. Fix control to `threshold=1e-12*max(1,var(yi)),stepadj=0.5,maxiter=10000`; remaining numerical defaults are pinned to metafor 5.2.1. Both summaries must pass. Do not try log pooling, DL, PM, alternative variance formulas or CI methods.

**Liu:** Figure 4A's outcome-specific random-effects label takes precedence over the generic Methods I² threshold. Use printed SMDs and the same identity-scale CI-width variance formula, `method="DL",test="z",level=95,weighted=TRUE`, intercept only. DL/z are declared RevMan 5 algorithm assumptions where the article is silent. Do not reconstruct SMDs from arm data or try fixed effects.

[Executable R reference and fixed options](supporting/reference_P08.R) implement these choices; documentation links and distinctions from author statements are in the source audit. R runtime validation is pending. Persistent primary reproduction failure activates only a cleared fallback; persistent fallback failure ends the use case with no new analysis.

## 6. Exact additional analyses and agreement

R **4.6.0**, metafor **5.2.1**; two-sided tests, 95% intervals. [App audit](supporting/APP_CHECK_P08.md) fixes paths and functions.

**Primary:** on identical complete rows, use `yi=log(ratio)`, `vi=((log(upper)-log(lower))/(2*1.959963984540054))^2`, requiring positive inputs. Fit `metafor::rma(yi,vi,mods=~D,method="ML",test="z")` and `mods=~D+S`, with the control above and level 95. Compare with `anova(reduced,full)`, one added degree of freedom. App: `meta-regression/index.html`, **Multiple moderators and model comparison**, header `yi,vi,D,S`, in that order; interaction unchecked. Report intercepts/slopes, SEs, z/p, CIs, residual τ², log likelihood, AIC/BIC and LRT.

**Fallback:** `metafor::rma(yi,vi,mods=~duration_months,method="PM",test="adhoc",level=95,control=list(tol=1e-12))`. Single-moderator panel, `label,estimate,SE,duration_months`, linear display. PM τ²; floored HK with `q=max(1,RSS/(k-2))`, t intervals/tests, df `k-2`. No dialysis adjustment or location-scale model. Prevalidate strict numeric input; require ten accepted rows, input identity/value agreement and zero unexplained parser warnings. Automatic permutation output is ancillary, excluded from inference, classification and selection.

Use full-precision `AlmMetaPlusUI.exportPayload()` for primary; fallback `__almResults()` plus [pinned browser capture](supporting/capture_app_P08.js), which uses the same t-tail implementation and fitted browser quantities. Never substitute an R p-value or rounded cards.

Compare every specified coefficient, SE, CI, τ², test statistic/p, and applicable comparison quantity; require identical counts, terms, rows and classifications. Numeric differences ≤`1e-8*max(1,abs(R value))`; p differences ≤`1e-6`. Reject nonfinite results. Report both implementations. Unresolved disagreement is implementation failure, not robustness. Reproduction and leave-one-row-out verification fits are R-only; no additional moderators/interactions.

## 7. New versus robust

For Veltkamp, let `bR` and `bF` denote reduced and adjusted diabetes slopes. If `abs(bR)<0.01` per 10 percentage points, classify the comparison as inconclusive.

Otherwise:

- **New:** sign reversal, or at least **50%** reduction in absolute slope after setting adjustment.
- **Robust:** both slopes positive, both CIs exclude zero, and `abs(bF−bR)/abs(bR)≤0.20`.
- **Inconclusive/intermediate:** all other patterns.

Report uncertainty; attenuation alone does not establish confounding.

For Liu, **robust** means the duration slope’s upper CI is below zero; **new, directionally contrasting** means its lower CI is above zero; otherwise **inconclusive**. Null inclusion is not proof of no duration association.

All outcomes are reportable. No outcome, moderator or model switching follows results.

## 8. Novelty-check log

On **2026-10-28**, pc2's Europe PMC/OpenAlex screening identified no equivalent prior re-analysis. Equivalence means the same source corpus/outcome/comparison and added joint diabetes-plus-setting question, or continuous-duration CRP question; eligible subsets count. Different software/estimators do not evade equivalence. Original univariable plots, duration subgroups or a commentary alone do not qualify.

| Supplied retrieval | Veltkamp | Liu |
|---|---|---|
| Europe PMC MED/PMID | 40424522: cited_by 31; retrieved/hitcount 33/33 | 39166132: 37; 37/37 |
| OpenAlex | W4410765724: 45/45; complete=true | W4401368310: 46/46; complete=true |
| PubMed method/title query | 0 records | 2: 41102471, 35070839 |

[Source audit](supporting/SOURCE_CHECK_P08.md) preserves exact PubMed queries, retrieval keys, flags and access limitations. Supplied JSON contains counts/flags, not full citing lists or per-record dispositions: coverage and audit-trail limitations are disclosed, not treated as F2 failure. No exhaustive independent clearance is claimed. Liu's query-hit dispositions remain a fallback activation condition.

**Deviation:** Europe PMC and OpenAlex replace Google Scholar because Scholar showed an “unusual traffic” bot check on 2026-10-28; not bypassed. Historical blocked PMC/PubMed routes remain blocked; supplied local sources were used.

## 9. App-implementation evidence

Pin: **14dc545bcba87a02158b2f445c28450e7eaf6b89**, `C:/Users/User/ucjobs/allmeta_14dc545/`. The path is `meta-regression/`, not the old `app/meta-regression/` alias.

The app audit cites file, function, line and SHA-256 for `plus-engine.js::fit/compute`, `plus-ui.js::parse/run/exportPayload`, and `index.html::fitPM/hksj/tTwoSidedP/__almResults`. Hashes match supplied PIN.txt. Multiple moderators implement ML/z; single moderator implements PM/floored HK.

Direct scripts/styles and dynamic glossary/PDF assets are present and hashed. Optional live webR assets are absent; live webR is outside the registered desktop-R comparison. Static presence does not certify browser closure or numerical parity. Reproduction/verification diagnostics remain explicitly R-only.

## 10. Write-up plan

Retain the existing software example. Add **150–250 words**, “a re-analysis illustrating …”, with the original citation, eligible count, reproduction status, slopes/CIs, agreement and ecological limitations. One moderator/effect figure: primary holds setting at its arithmetic mean and labels observed effects unadjusted; fallback explains that native radius increases with inverse variance, not area proportional to weight. Archive exclusions and verification records. Report robust/inconclusive outcomes equally. Mahmood dictates the final paragraph. No clinical recommendations, priority or ranking claims; never alter original printed numbers or name a publication as containing an error.

## 11. Deviations and amendment log

2026-10-28, before study-level extraction/analysis: retain the Scholar substitution; correct v3's F3 misapplication and restore Veltkamp; fix one natural-scale REML/z reproduction configuration; retain Liu DL/z; disclose the unverified v3 cohort count; replace missing-review assumptions with this job's documented static audits. No new-versus-robust threshold, tolerance or verification gate changed. Subsequent amendments are dated, justified and independent of real-data results.

## 12. Mandatory post-release, pre-analysis conditions

1. Pass meaningful synthetic-only validation of R code, browser capture, parsing, eligibility/refusal paths, boundary classifications and verification mechanics. All fixtures are named `synthetic_*` and start with “SYNTHETIC - not data”.
2. Establish app/R runtime parity on synthetic fixtures and browser dependency closure for the registered paths. Replace automatic examples before script execution; never run bundled clinical demos as validation.
3. Sync and validate the extraction kit against v4, including reproduction defaults, row identities and the exact human-verification rules.
4. Reserve ≤30-minute packets in the shared COAUTHOR_LOAD ledger, respecting cross-paper ISO-week caps, Mahmood's rota and seven-day reassignment; record actual different-family model logs.
5. Check source availability/hashes, source-supported identity/independence mapping and, if activated, every conditional Liu clearance. Numerical completeness and the unchanged reproduction gate then apply to verified extraction.

These are mandatory conditions, not F1–F6 freeze failures. **No real-data reproduction gate may run before code passes synthetic validation.** Log every post-release code change as a dated deviation; validate it synthetically without using real-data outcomes to choose changes.

Freeze this text and incorporated supporting files with hashes. Extraction requires this paper's public GitHub release and Zenodo archival DOI; neither is claimed here. [V4 notes](V4_NOTES_P08.md) dispose of every v3 blocker and list outstanding execution work.

**sha256 and UTC freeze time recorded at release**

## Pre-freeze review-process incident (REDTEAM2 RT2-03, coordinator-assessed)

2026-10-28, REDTEAM2 handling deviation: broad XML-section output and publisher-search context inadvertently exposed study-table text in the review transcript before release. No study-row values were carried into deliverable files or calculations. Do not reuse that transcript as an extraction. Preserve the incident record for coordinator assessment and retain the required independent, mutually blinded post-release extraction and verification process. Do not describe this review as having avoided all study-row transcription.

Coordinator assessment (pc2, 2026-10-28): the reviewer is not an extractor; no exposed value entered any deliverable, registered choice, threshold or calculation; post-release extraction remains blind, independent and double. The incident is disclosed, not treated as an extraction, and does not relax any gate.
