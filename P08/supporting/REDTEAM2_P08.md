# P08 second-round adversarial review

Date: 2026-10-28. Package: C_P08_V4/out/. Verdict: **FREEZE_OK**. No P0 failure of F1–F6 was established. This is a freeze-specification judgement, not a runtime, extraction, fallback-activation or real-data-analysis pass.

Below, PREREG, SOURCE_CHECK, APP_CHECK, VERIFICATION, REFERENCE and NOTES refer to the corresponding v4 files, using observed line numbers. V3 was read directly from C:/Users/User/ucjobs/B_P08_V3/out/. Files were read with Python. No statistical model, browser app, bundled clinical example or real-data gate was run; no dataset was assembled. Retain the review-handling deviation in RT2-03: an unqualified assertion that no study-row text entered this review would be false.

Reviewed PREREG SHA-256: 17d264ff2b28852dfa4086e2124f3deef0ccf505dcca67280dda50fbfd8c70ea.
Reviewed SOURCE_CHECK SHA-256: d93a7a22cd0f1f4b6e53f199ae7b98c811c125e66f0f8bdcb05ec76418ef17ac.
V3 PREREG SHA-256: 9ddff153e1d8431729b6e388281817e328e770b4b4c6427981b022e591535703.

## Numbered findings and exact replacement text

1. **RT2-01 — P1: complete the comparison record before analysis. This execution condition is not a P0.**

   Evidence: PREREG 74–78 fixes inference and full-precision agreement; APP_CHECK 34 includes both coefficient vectors and fallback q/df. capture_app_P08.js 53–66 supplies intercept estimates/SEs/CIs but adds only slope t/p. REFERENCE::p08_values, 170–175, does not return fallback q/df. The orchestration/identity/classification/deletion/logging runner is expressly unfinished (REFERENCE 185–192; NOTES 50). A partial comparison must not be called a pass. All four copied browser t-tail helper bodies independently matched the pinned page verbatim. This is completion of fixed arithmetic/workflow, not an absent registered app model.

   Exact replacement for NOTES 50:

   > Complete the orchestration, comparison, deletion and verification runner before any real-data gate. For the fallback, capture both intercept and duration coefficient estimates, SEs and CI endpoints; compute each coefficient's t as coefficient/SE and its two-sided p with the frozen browser tTwoSidedP routine and df=k−2. Capture tau², q and df. Obtain the corresponding independent R quantities under the registered PM/adhoc model, including q=max(1,RSS/(k−2)) using residuals and weights from that fit, and df=k−2. Compare every required quantity at the registered tolerances and require exact row identity/order, term names, counts and classifications. A missing required field fails comparison. Ancillary permutation, QE and R² outputs do not replace required targets or enter classification. Exercise the complete path, both reproduction configurations, deletion fits, parsing/refusal paths and verification logs on marked synthetic fixtures with R 4.6.0/metafor 5.2.1. Record post-release code changes as dated deviations independent of real-data results.

2. **RT2-02 — P2: narrow an assertion about the original analysis.**

   Evidence: PREREG 9 says the original reports individual moderator analyses, “not this joint model.” SOURCE_CHECK 11/61 more carefully says the supplement does not specify the added joint model. Main Methods, Figure 6 and S6A–C captions establish reported covariate analyses but do not supply a complete original regression specification. Absence of an explicit report is supported; categorical reconstruction of every original fitted model is stronger. This does not establish an equivalent prior re-analysis or F2 failure.

   Exact replacement for the final sentence of PREREG 9:

   > The supplied main Methods, Figure 6 and supplementary Figures S6A–C report covariate analyses; no explicit joint diabetes-prevalence-plus-cardiovascular-surgery model was located in those materials. This is a bounded statement about reported methods. A subsequently confirmed equivalent analysis excludes this candidate under the existing novelty rule.

3. **RT2-03 — P1, review-process deviation: unintended study-table text entered tool output. This is not an identified v4 defect or F1–F6 failure.**

   Evidence: an initial Python read serialized a parent XML section containing nested tables and inadvertently emitted study-row text to the tool transcript. A later publisher-search result also included neighboring table rows. This was inconsistent with JOB_RULES' prohibition on transcribing study rows. None is reproduced in these deliverables, assembled into a dataset or used in calculations. Subsequent local text reads were restricted to metadata, headers, model statements and pooled summaries; supplied figures were inspected for feasibility without transcribing their rows. Existing v4 choices and thresholds were not changed using exposed values.

   Exact text for the review deviation record, adopted here:

   > 2026-10-28, REDTEAM2 handling deviation: broad XML-section output and publisher-search context inadvertently exposed study-table text in the review transcript before release. No study-row values were carried into deliverable files or calculations. Do not reuse that transcript as an extraction. Preserve the incident record for coordinator assessment and retain the required independent, mutually blinded post-release extraction and verification process. Do not describe this review as having avoided all study-row transcription.

   Open disposition: coordinator assessment of this review-process incident. It does not justify relaxing a gate or altering a source number.

## Independent F1–F6 judgement

| Criterion | Judgement | Evidence and limits |
|---|---|---|
| F1: feasible primary | **PASS, FEASIBLE-IMAGE** | Supplied Figure 2 contains HR/OR panels and printed effects/limits; XML Table 1 tbl1/thead contains Setting and DM (%) beneath AKI/no AKI. Required field types are available. Image risk remains in double extraction. This does not certify complete moderators or independent eligible k. PREREG 34–40 and VERIFICATION 7–15 retain mapping, missingness, independence and complete-case refusals. |
| F2: novelty | **PASS with disclosed coverage limits** | P08 entries in both supplied novelty JSONs match SOURCE_CHECK's identifiers/counts/flags. PREREG 98–108 discloses absent full citing lists/dispositions and Scholar substitution. No equivalent is established. F2 expressly permits disclosed coverage limitations. Liu's unresolved hit dispositions remain conditional. |
| F3: single reproduction configuration | **PASS** | PREREG 58–66 and REFERENCE 43–69 fix one natural-scale REML/z primary configuration, variance formula, weights, controls, both panel targets and 0.005 gate. R is stated by the source; metafor/REML/z is explicitly the preregistration's implementation assumption, not an author-package attribution or universal R default. Natural-scale pooling is also explicitly assumed. No alternative trial is permitted. Liu has one DL/z configuration with figure-label precedence. Unstated original details alone do not justify refusal under F3. |
| F4: complete analysis specification | **PASS at specification level** | PREREG 26–40, 58–94 fixes outcomes, scales, HR preference, eligibility, moderators, models, inference, options, numeric agreement and classification. REFERENCE fixes arguments/refusals; VERIFICATION fixes keys, deletion and sampling. Remaining code assembly/runtime validation is expressly allowed after release. RT2-01 is required execution work, not permission to choose methods later. |
| F5: verification | **PASS** | Python confirmed PREREG 46 exactly copies MAHMOOD_DECISIONS item 4. PREREG 48–54 and VERIFICATION preserve different-family AI passes, fourth-pass escalation, headline triggers, seeded 5%, >2% escalation, ≤30-minute packets, one per ISO week, Mahmood and seven-day reassignment. Binary-setting extrema still require checking every eligible primary row. |
| F6: static app capability | **PASS** | Direct code inspection and matching hashes establish multiple-moderator ML/z and single-moderator PM/floored-HK. File/function evidence follows. Reproduction/deletion/verification remain R-only/workflow; browser closure and runtime parity are not claimed. |

The NONE blocker file is supported under the supplied criteria. Runtime, kit, scheduling and conditional-fallback tasks are not automatically F1–F6 failures.

## Source-check verification ledger

Only permitted pooled summaries, metadata, headings and model statements are reported here. MATCH supports the specified claim at its location; it does not certify an extracted dataset. Reviewer-chosen thresholds are specifications, not original-article numbers.

Web searches and local checks were performed on 2026-10-28.

- [Veltkamp publisher article](https://academic.oup.com/ndt/article/40/11/2143/8151584), [publisher issue listing](https://academic.oup.com/ndt/issue/40/11), and [PubMed](https://pubmed.ncbi.nlm.nih.gov/40424522/): publisher/PubMed search results support bibliographic details; an initial publisher-PDF search result supports pooled summaries and licence. Direct opening of the clean article URL subsequently failed with an inaccessible publisher redirect: **blocked/unavailable**, not retried or bypassed. Detailed Methods checks use supplied XML, not a claimed successful live article read.
- [Liu publisher article](https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2024.1434613/full): accessible; metadata, CRP summary/count, Methods and licence confirmed. Historical PMC/PubMed/Scholar blocked routes were not revisited.

| V4 claim | Result | Source location / qualification |
|---|---|---|
| Veltkamp DOI/year/volume/issue/pages | **MATCH** | Publisher issue listing, PubMed search result and XML front: 10.1093/ndt/gfaf093; 2025; 40(11); 2143–2158. Author list/title agree with XML. Journal placement supports profile eligibility. |
| Veltkamp CC BY 4.0 | **MATCH** | XML front/license links to /licenses/by/4.0/; publisher-PDF search result agrees. |
| HR 2.38 (95%CI 1.93–2.84) | **MATCH** | Primary XML sec4-3 opening pooled paragraph; Figure 2 HR summary; publisher-PDF search result. |
| OR 2.92 (95%CI 2.64–3.20) | **MATCH** | Same paragraph and Figure 2 OR summary; publisher-PDF search result. |
| Independent outcome-specific k; former v3 “40 cohorts” | **UNVERIFIABLE as a printed independent outcome count** | V3 states 40; v4 withdraws certification. No matching printed narrative count located in inspected text/captions. Forest lines were not counted or converted into independent cohorts. This is a package-audit limitation, not a finding against a publication. |
| Primary random-effects statement | **MATCH locally; live article check UNVERIFIABLE** | Methods sec3-5 opening paragraph includes “using a random effects model to calculate the weighted means”. No tau² estimator, CI construction or pooling transformation is specified there. |
| R 4.3.2 / RStudio v.2023.09.1+494 | **MATCH locally; live article check UNVERIFIABLE** | Methods sec3-5 final paragraph. No synthesis package/function named. Metafor REML/z is the registered assumption. |
| HR preference over OR for regression | **MATCH** | Methods sec3-5 regression paragraph and Figure 6 caption. This does not certify independence of plotted rows. |
| Primary field locations/headers | **MATCH** | supp/gfaf093fig2.jpg: Authors, Year; HR/OR panels; Clinical setting; OR/HR [95% CI]; outcome/adjustment annotations. XML tbl1/thead: Authors, Year, Setting, DM (%), with AKI/no AKI spanner. Preserve the AKI component. |
| Primary supplements and page counts | **MATCH** | Nested gfaf093_supplemental_files.zip: C.Figures_Supplements_S1_to_S6_20022025.pdf, 13 pages; C.Tables_Supplements_S1_to_S3_20022025.pdf, 11 pages. Both opened in memory using Python/pypdf. |
| Supplement scope/model reporting | **MATCH, bounded** | S6A–C captions, pp.11–13: CKD incidence; kidney failure; kidney failure stratified by follow-up duration. No explicit added joint specification located. Tables PDF headings cover search, exclusions and risk of bias. See RT2-02. |
| Liu DOI/year/volume/article number | **MATCH** | Publisher and XML front: 10.3389/fnut.2024.1434613; 2024; 11:1434613. Author list/title agree. |
| Liu CC BY, version unspecified in supplied XML | **MATCH** | XML licence has no version; publisher also identifies CC BY. V4 invents no version. |
| SMD: −0.34; 95% CI: −0.62, −0.07 | **MATCH** | Publisher §3.5.1, XML sec24 and Figure 4A total. |
| “Ten studies”; I² = 37% | **MATCH** | Publisher §3.5.1 and XML sec24; I² also in Figure 4A. Published count does not certify independence or duration completeness. |
| RevMan 5.4; generic I² >50% rule | **MATCH** | Publisher §2.6 and XML sec13. The generic rule and outcome-specific random label both exist; v4 fixes figure-label precedence and reports both neutrally. |
| Figure 4A “IV, Random, 95% CI”; overall-effect Z | **MATCH** | Supplied fnut-11-1434613-g004.jpg panel A headers/footer, loaded with Python. Printed effect/CI precision is two decimals. No row values copied here. |
| Liu Table 1 headers | **MATCH, duration meaning conditional** | XML tab1/thead: Authors, Study period, Study design, Intervention, Median follow-up (months), Comparator. Follow-up alone does not certify treatment duration at the CRP assessment; v4 retains that activation condition. |
| Liu DOCX supplies no extra CRP inputs | **MATCH to inspected structure** | Data_Sheet_1.docx: search-term table and risk-of-bias material/captions; no extra CRP effect/duration input table identified. |
| Historical primary supplement timeout/current availability | **MATCH observed facts; acquisition provenance UNVERIFIABLE** | FETCH_LOG primary entry records XML success and supplement timeout. Current archive exists and opens. Later acquisition date/route is not recorded; v4 does not invent one. |
| Source and package hashes | **MATCH** | Recomputed all 36 source-file, 44 listed-present app-file and nine output-file hashes in FILE_HASHES_P08.json: no mismatch or missing listed-present file. Integrity evidence is not runtime validation. |

Primary XML SHA-256: 6103b90bd8a9c2fe4b9f040bac284db31d5d0a6cfd99a067b85e2c1ed960e7e0.
Fallback XML SHA-256: b2ba7938c00f06a4a2a9c5c5a20863d09f12c84d246ffcd590b191df22e6814f.

The [metafor reference](https://wviechtb.github.io/metafor/reference/rma.uni.html) supports REML/z defaults and the floored adhoc adjustment. The [Review Manager 5 algorithms](https://training.cochrane.org/handbook/current/statistical-methods-revman5), especially PDF p.8, support DL. These documents support declared implementation assumptions, not attribution of unstated methods to the original authors.

SOURCE_CHECK's novelty entries match both supplied P08 JSON records: Europe PMC primary 31 cited / 33 retrieved / 33 hitcount, fallback 37/37/37; OpenAlex primary 45/45, fallback 46/46, both complete=true and error=null; PubMed method-query counts 0 and 2. Both exact supplied query strings and fallback PMIDs 41102471/35070839 match. Primary flags are MED 41637990 / W7127111770 and W7221515842; fallback flag is MED 39758318 / W4405654446. These are historical retrieval records, not refreshed citation counts. Full citing lists, exact citation-API requests and complete dispositions are absent. V3 records its limited commentary assessment and failed direct-record checks; this review does not upgrade those claims to fresh independent full-text clearance. Scholar substitution matches MAHMOOD_DECISIONS item 3.

## Static app evidence

Paths are relative to C:/Users/User/ucjobs/allmeta_14dc545/, supplied commit 14dc545bcba87a02158b2f445c28450e7eaf6b89. Commit identity is supplied provenance; file hashes were independently recomputed without git.

| File / functions | Observed capability | Matching SHA-256 |
|---|---|---|
| meta-regression/plus-engine.js; fit:44, compute:81 | ML, normal tests/CIs, reduced intercept+D versus full intercept+D+S, likelihood comparison and fixed rank/convergence handling. | 9b002c0594ab787c403ebb606a83f6d58d1492d091b1a68c9d5b117e719723b3 |
| meta-regression/plus-ui.js; parse:9, run:66, exportPayload:70 | Strict numeric multi-moderator input/order/interaction; unrounded input/results export. | d56667f6ba8f6ea0781f852cd9c0d9958b5ade8fb501c7da38a888d0ea35156f |
| meta-regression/index.html; parseStudies:189, fitPM:251, hksj:277, tTwoSidedP:355, __almResults:817 | PM; q floor 1; t(k−2); cached coefficient/SE/CI quantities. Permissive parsing requires the registered prevalidation. | 263d040ca4bd53d7125181b00687c78be3630efb41ba4573da0d8b95c81ed067 |
| meta-regression/validate/reference.R; plus_reference / nested fit | Pinned independent ML/z reference, not a P08 runtime pass. | 1db73c17a432c35d858f3d4bad971babd9f809f5799e1d0dda41a6e0404271b8 |

The fallback capture's lnGamma, betaCF, betaInc and tTwoSidedP bodies match the pinned page exactly. Optional live-webR assets remain absent and excluded from the registered desktop-R comparison. Static presence does not establish browser closure. The missing complete P08 runner is not claimed as an existing app feature.

## V3 comparison, deferrals and selection honesty

- **Gates unchanged:** v3 73 and v4 58 both require point and each CI endpoint within 0.005, unrounded. Original panel membership is preserved for reproduction. No model search, tolerance widening, input reconstruction or result-based candidate return.
- **Agreement unchanged:** v3 135/142 and v4 78 retain scaled 1e−8 numeric and 1e−6 p tolerances, full precision, identity/count/term/classification agreement and nonfinite refusal. RT2-01 completes coverage.
- **Definitions unchanged:** Python confirmed the entire substantive v3/v4 section 7 is verbatim equal: 0.01 reduced-slope floor; sign reversal/50% attenuation; positive slopes/CIs excluding zero with ≤20% relative change; fallback CI-sign rules; other patterns inconclusive.
- **Verification unchanged:** v3 42–69 and v4 44–54 plus VERIFICATION preserve all ties, both primary weight sets, 0.5-SE/10% triggers, seed 2026102808, minimum-one 5% sampling when a pool exists, fourth pass, >2% escalation and packet rules. Binary S still makes every eligible primary row a headline row.
- **Legitimate changes:** restoring the designated primary applies F3's before-analysis single-configuration permission. Withdrawing the unsupported 40-cohort certification is honest. Liu DL/z and figure-label precedence already existed in v3. Selection rests on designated candidates, journal placement, reported questions and source availability, not fitted results.
- **Legitimate deferrals:** synthetic execution, runtime parity, browser closure, kit synchronization and packets are expressly post-release in FREEZE_CRITERIA. Conditional Liu feasibility/novelty/profile clearance may remain pending while the primary freezes. Source-supported identity/independence has fixed refusal rules; quantitative completeness cannot be certified without extraction. No specific F1–F6 failure was found hidden in the execution list.
- **Hidden-choice check:** no free choice of outcome, estimator, CI method, transformation, moderator, interaction, sign definition or numeric classification threshold was found. Same-type ties, unresolved dependence, missing moderators, nonfinite results and inadequate complete-case/category counts have refusal rules. Runtime corrections cannot become a route to changing these choices after results.

TASK_COMMON/protocol requirements were checked against the later job-specific freeze rules: outcomes, fallback/stop triggers, effect scales, numeric reproduction and agreement gates, exact additional analyses, verification logistics, no outcome switching, published-feature selection and prohibited priority claims are addressed. R_ENV supplies R 4.6.0/metafor 5.2.1; manuscript.txt confirms metafor validation but does not independently name the target journal. COAUTHOR_LOAD confirms MA, SMA, QFH, HK and AW. Existing software examples are retained; PREREG 120 fixes 150–250 words, one moderator/effect figure, ecological limitations, equal reporting of outcomes and Mahmood's final paragraph. No author contact, blocked-route bypass, ledger assignment or publication occurred.

## Every remaining open condition/problem

1. RT2-01: finish and synthetically validate the reference/capture/comparison/deletion/verification runner. R/browser runtime validation was not performed here.
2. Establish synthetic app/R parity and browser closure, with input identity/value checks, capture/export and refusal paths. Suppress bundled clinical examples before scripts execute. Optional live webR stays unavailable/excluded.
3. Align the extraction kit, replacing stale primary-default and fallback-FE instructions; validate schemas, actual model identities/families, keys, sampling/escalation/corrections. Schedule ≤30-minute packets through the shared ledger with weekly caps, Mahmood and seven-day reassignment. Every eligible primary row requires checking.
4. Primary independent outcome-specific k, complete-case k, category counts/variation and identity/independence mapping remain uncertified. Reproduction/agreement gates are unrun; image precision may cause a legitimate stop. No substitute k/model is authorized.
5. Before Liu activation: clear duration-versus-follow-up/assessment meaning, independence/arm mapping, all-ten-study completeness, profile eligibility or an explicit dated deviation, and novelty including both query hits. Otherwise stop.
6. Novelty audit limitations remain: no full citing lists, exact citation-API requests or complete dispositions. Historical blocked/unusable routes are not negative results. No exhaustive independent clearance is claimed.
7. Primary supplement acquisition date/route is undocumented. The live primary article failed; detailed Methods checks rely on XML. Original primary package/estimator/scale/CI details remain NOT STATED, handled by the single fixed assumption. Target journal comes from TASK_PAPER, not manuscript.txt.
8. RT2-02 is proposed, not applied to v4. RT2-03 is recorded; coordinator disposition remains open.
9. Release hashes/UTC time, the separate public P08 GitHub release and Zenodo DOI are not established here. Required conditions must precede the relevant extraction/analysis steps; synthetic validation must precede every real-data reproduction gate.

Only this review and the one-line verdict were written under the current job's out/. No source, v3/v4 file, app, ledger or release was modified.
