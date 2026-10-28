# P11 second-round adversarial review of v4

Review date: 2026-10-28. **Verdict: FREEZE_OK.** No P0 finding; no P1 finding; one P2 documentation finding. This verdict applies to freezing the primary route under FREEZE_CRITERIA.md. It does not certify a release, completed extraction, executable analysis, runtime parity, or permission to start real-data gates.

The reviewed package is `C_P11_V4/out/`. Instructions followed: JOB.md, JOB_RULES.md, REDTEAM2.md, REDTEAM.md, FREEZE_CRITERIA.md, MAHMOOD_DECISIONS.md, TASK_COMMON.md, TASK_PAPER.md, FIELD_USE_CASE_PROTOCOL.md and COAUTHOR_LOAD.md. The current job supersedes TASK_COMMON's old no-file/final-only instruction; FREEZE_CRITERIA supersedes v3's pre-freeze runtime requirements.

All local reads used Python. Source inspection was limited to structure, headers, readability, permitted aggregate results, k, bibliographic information and methods. No study row is reproduced in this report, no dataset was assembled, and no real-data analysis or supplied-corpus calculation was run. No author contact, login or blocked-route bypass occurred.

## 1. Numbered findings and exact replacement text

### 1. R2-01 — P2: fallback Table 1 header hierarchy is described incorrectly

**Evidence:** `supporting/SOURCE_CHECK_P11.md:102` associates “N, Age (year), Female (%)” with “Population”. In the supplied fallback `fulltext.xml`, `table-wrap[@id="Tab1"]/table/thead`, **Study population** spans those three subordinate columns. **Population** is a separate header. The same wording already occurs in v3; v4 did not introduce it.

**Effect:** This is a source-location documentation mismatch, not a mismatch in a published estimate and not an F1 failure. The fallback's registered numerical inputs are in Figure 2e, while Table 1 supplies contextual mapping. The primary route is unaffected. Correct this description when preparing the release/supporting source map.

**Exact replacement for SOURCE_CHECK line 102:**

> Table 1 has two header rows. The top row is Author/year; Study population (spanning three columns); Population; Type of interventions; Follow-up lengths; Outcome parameters; Jadad score. The three subheaders under Study population are N, Age (year), and Female (%). Population is a separate column. No study rows copied.

No change to any source-paper number, analytical input, model, gate, verification rule or classification definition is proposed. `BLOCKERS_P11.md` may remain the single line `NONE`.

## 2. Freeze criteria F1–F6

| Criterion | Judgment | Independently checked evidence |
|---|---|---|
| F1 — Feasible chosen candidate | **PASS** | Primary DOCX Appendix D is the second table in word/document.xml, with 14 body rows and four labelled, readable integer count columns. The forest image is readable. All seven hashes in SOURCE_CHECK match the supplied source files. FETCH_LOG records HTTP 200/OK for each candidate's XML and supplementary ZIP, with matching hashes. Primary FEASIBLE is supported. Fallback FEASIBLE-IMAGE is supported by direct image inspection, with the image risk retained. |
| F2 — Novelty | **PASS within the criterion's stated scope** | Both supplied novelty logs contain the P11 records reproduced in supporting/NOVELTY_P11.json; source hashes and record equality match. Primary Europe PMC retrieval is 18/hitcount 18, distinct from cited_by 16; OpenAlex is 34/34 and complete. Neither screen flags an equivalent analysis. Main §8 explicitly records the Scholar substitution, title/citing-record scope, and coverage limits. This is not proof of universal absence or a new independent full-text novelty screen. The conditional fallback provision is applied honestly. |
| F3 — Original model fixed beforehand | **PASS** | SOURCE_CHECK §§3–5 fixes one primary ML/log-RR/normal attempt and one fallback panel-specific fixed-MH/normal attempt. Missing original details are explicitly assumptions fixed to named defaults, not claimed recovered facts. Correction rules, package versions, original-result comparison fields, exact k/direction, 0.005 componentwise tolerance and primary → eligible fallback → stop are specified. No estimator or scale search is permitted. |
| F4 — Analysis and outcomes specified | **PASS** | Main §§2–7 and normative SOURCE_CHECK §§5–6 fix inputs, outcome, full/deletion REML analysis, optimizer settings, clean-process defaults, complete comparison quantities, normalized tolerances, exact flags/identities/classifications, sensitive/robust thresholds, tie handling, and stop rules. The entire v3 original-model/diagnostic call contract is preserved. Missing executable scripts and synthetic runtime validation are explicitly permitted later conditions; they are not unspecified analytical choices. |
| F5 — Verification specification | **PASS** | The full text of MAHMOOD_DECISIONS item 4 occurs verbatim in main §4; Python exact-substring comparison passed. Operational additions retain independent blind extraction, family-log checks, third-model adjudication, fourth AI re-check, headline checks, seeded 5% sample, >2% escalation, ≤30-minute packets, weekly cap, Mahmood rota and seven-day reassignment. |
| F6 — Static app capability | **PASS** | Inspected the pinned implementation and independently rehashed the five capability files listed below. REML, all single deletions, specified diagnostics, normal inference and unrounded exports exist. Original ML/MH gates, count transformations, classification and verification selection are explicitly R-only/procedural. Missing optional browser-R resources and untested runtime closure do not negate this static criterion. |

### Static capability evidence

Paths below are relative to `C:/Users/User/ucjobs/allmeta_14dc545/`, supplied commit `14dc545bcba87a02158b2f445c28450e7eaf6b89`.

| File / function or location | Verified SHA-256 |
|---|---|
| influence/index.html — parse:216, tau2_REML:249, pool:253, run:336, single-deletion diagnostics:361–387, drawLOO:566, study/JSON exports:693/702/762 | `48c65317a4090a7e72ea3b70cf177a1e77dbf2620a2eed1d1c5e9805c0773d25` |
| shared/ma-core.js — _tau2Guarded:121, tau2REML:137–362 | `fef6ab267ec7fd5582e3431381f090daee11267010effc0858834d9e5fc44bc8` |
| influence/influence-extra.js — pnormUpper:45, pchisqUpper:50, summarize:53 | `54a7c60ff2919a8a2a3b7e00738e3ada8c4fbabf84100210c925902aaddfa67c` |
| influence/r-script.js — AlmInfluenceR.build:21–125 | `f1b6a5cbeb7e490925696496e0ac3be2a083b563ca55422f7bc63197fae0e677` |
| hub/shared/results-export.js — init / window.alm.resultsExport; JSON.stringify export:150 | `16ffa76bc74275565214c2e142d7f0d0847a5a8eded2614efb04aa172acd71f4` |

All 16 PIN hashes match. All 26 direct HTML script/stylesheet references exist. All 37 manifest entries agree with actual existence, sizes and hashes where present. The only absent entries are `r-shiny/shinylive/webr/webr.mjs` and `r-shiny/shinylive/webr/repo/manifest.json`, already disclosed. This is static verification only.

The flag rule in index.html:377–378 is fixed: absolute DFFITS > 3/sqrt(k−1), OR Cook's D > 0.4549364231195727, OR hat > 3/k, OR absolute DFBETAS > 1. SOURCE_CHECK requires exact flag agreement and rejects nonfinite required quantities; the exported checker's paired-NA acceptance is therefore not the governing validator. The app's global REML search and R's scalar-start procedure can disagree; v4 preserves a stop on unresolved disagreement.

## 3. Published-number and bibliographic audit

Web search and direct publisher/PubMed inspection were performed on 2026-10-28. Local XML and forest images independently support the relevant aggregate claims. MATCH means the quoted item is supported; it does not mean reproduction succeeded.

| Quoted item | Status | Evidence / URL |
|---|---|---|
| Primary citation: authors/title, DOI 10.1007/s10916-024-02059-x, 2024, volume 48, article 40 | **MATCH** | [Primary publisher article](https://link.springer.com/article/10.1007/s10916-024-02059-x), citation and publication metadata. Article number 40 is correctly treated as an article number, not a page range. |
| Primary licence: CC BY 4.0 | **MATCH** | Same publisher page, Rights and permissions; local XML permissions agrees. |
| Primary pooled target 0.99 (95% CI 0.95–1.03), k=14, I² 64.3% | **MATCH** | Same publisher page, Results of Syntheses, and local Figure 2 overall row. No per-study values were recorded. |
| Primary model: random effects, maximum likelihood, log relative risk, R/metafor | **MATCH** | Same publisher page, Study Context / Data Analysis Methods, and XML Sec5/Sec7. |
| Primary original CI construction, variance formula, correction details, software versions and optimizer details | **UNVERIFIABLE as historical settings / correctly labelled NOT STATED** | They are not specified in the inspected methods. V4 fixes one assumption-based attempt; it does not claim that these settings were printed. |
| Fallback citation: authors/title, DOI 10.1007/s10741-019-09801-5, online 2019, 2020 volume 25, pages 231–243 | **MATCH** | [Fallback publisher article](https://link.springer.com/article/10.1007/s10741-019-09801-5) and [PubMed 31197564](https://pubmed.ncbi.nlm.nih.gov/31197564/). |
| Fallback licence: CC BY 4.0 | **MATCH** | Fallback publisher Rights and permissions; local XML agrees. |
| Fallback pooled target OR 0.75, 95% CI 0.62–0.90; k=15; I² 49% | **MATCH** | Fallback publisher mortality subsection and local Figure 2e. |
| Fallback model statements: general random effects/Mantel–Haenszel, RevMan 5.2; panel e fixed MH, 95% CI and Z test | **MATCH, with both source statements retained** | XML Sec8 and directly inspected Figure 2e. V4's prospective preference for the outcome-specific panel is explicit; this review makes no allegation about the publication. |
| Fallback exact CI variance formula, generic random-effects tau² estimator, explicit transformation and zero handling | **UNVERIFIABLE as historical settings / correctly labelled NOT STATED** | Named defaults are prospective reproduction assumptions, not quotations from the original. |
| Dated fallback citation-profile justification | **Current publisher display MATCH; historical snapshot UNVERIFIABLE independently** | Publisher currently displays 171 citations. The 27 October snapshot is supplied screening provenance; v4 does not use the metric as an analytical threshold. |

The primary [PubMed URL](https://pubmed.ncbi.nlm.nih.gov/38594411/) returned no substantive article record through the web reader, so that route was **UNVERIFIABLE**, not a zero-hit novelty result. The accessible publisher page supplied the checks. No bot challenge was bypassed. The historical Scholar block is retained as supplied provenance, not independently re-enacted.

## 4. Audit of every SOURCE_CHECK source-claim group

Locations refer to the reviewed `supporting/SOURCE_CHECK_P11.md`. Source roots are those in JOB.md.

| SOURCE_CHECK location / claim | Status and direct check |
|---|---|
| Lines 9–18: feasibility, source roots, retrieval and logged hashes | **MATCH** for files, roots, four HTTP 200/OK records and hashes. No required P11 item is marked BLOCKED. Historical assertions about earlier failed requests/no bypass cannot be independently reconstructed from the source contents; they are not needed to infer present readability. |
| Lines 20–28: seven individual source hashes | **MATCH**, all recomputed from Python-read bytes. The DOCX and image hashes match as well as the four logged XML/ZIP hashes. |
| Lines 32–43: Appendix D title, table position, k, headers and representation | **MATCH**. It is table 2, headed Results of individual studies, with the stated descriptive subtitle, 14 body rows, and the listed eight headers. The four analytic count columns are integer text with zero decimal places. Age (mean) and Incentive are separate unused columns. No count-table footnote/endnote references or tracked insertions/deletions were found; no separately printed analysis-total or administrative-loss header is present. No cell values were emitted. |
| Lines 36–41: primary Figure 2 cross-check columns and precision | **MATCH** by image inspection: identity, weight and RR/CI headers are as stated; ratios/endpoints and percentage weights have two decimal places. The complete overall synthesis is the fixed target. |
| Lines 45–51: Appendix C dictionary and three quoted definitions | **MATCH**. It is table 1, headed Data element / Instructions / Description. Arm N, Loss to follow-up and Admin Loss definitions match the supplied document, disregarding trailing whitespace only. |
| Line 53: primary input contract | **Supported prospective rule**, not a claim of separately printed totals. Retained/lost columns exist; deriving totals once and prohibiting additional inferred adjustments leaves no selectable source reconstruction. Whether the eventual source-to-forest mapping is consistent remains a post-release check with a fixed failure rule. |
| Lines 57–71: primary section locations and six quoted passages, including the figure-caption passage | **MATCH**. All six passages occur in the supplied XML at the stated sections/caption; none required correction. |
| Lines 73–86: primary stated/unstated distinction and pooled target | **MATCH** for printed model/scale/summary; **NOT STATED retained** for historical settings. Fixed defaults are assessed as the prospective F3 contract, not additional original-paper facts. |
| Lines 90–99: fallback filename, middle panel e, k and image headers | **MATCH**. Fig2b_HTML.jpg contains d/e/f; e is the middle panel with 15 study rows. The events/totals are readable integers; OR/CI values have two decimals; weights have one decimal. The numerical and graphical ratio columns both carry the fixed-MH label. No per-study entry was transcribed. |
| Lines 100–102: fallback Table 1 location/header structure | **Location MATCH; hierarchy MISMATCH**, finding R2-01. The XML table is machine-readable, but N/Age/Female are nested under Study population, not Population. |
| Line 104: fallback input contract | **Supported prospective rule**. The named experimental/control Events and Total headers exist; deriving non-events from each arm's total and events is fixed. The selected follow-up is Figure 2e's synthesis; no alternate endpoint or arm construction is allowed. |
| Lines 106–118: fallback Sec8 and four quoted passages, including the caption | **MATCH**. All four occur in the supplied XML; the panel-specific fixed label and overall Z test are visible in the image. |
| Lines 120–131: fallback model policy and aggregate target | **MATCH** for printed facts; **NOT STATED retained** for unreported historical choices. The single fixed-MH attempt is a declared policy, not an assertion that the general Methods says fixed effects. |
| Lines 133–202: code, defaults, parity and execution boundaries | **Prospective specification**, not a claimed run or source-paper result. The quoted calls and numerical comparison contract are unchanged from v3. Independent code is absent from the supplied output package. R-only/procedural boundaries match the inspected app. |
| Lines 84, 129, 204: package-documentation support | **MATCH for current documentation; historical installed APIs remain UNVERIFIABLE here.** Official [escalc documentation](https://wviechtb.github.io/metafor/reference/escalc.html) gives the stated add/to/drop00/vtype defaults; [rma.uni documentation](https://wviechtb.github.io/metafor/reference/rma.uni.html) supports normal inference. The [meta authors' manual](https://guido-s.r-universe.dev/meta/doc/manual.html) identifies version 9.0-0 and describes the RevMan-style MH correction. It does not establish the installed 8.5.0 API or original unpublished settings. |

No unchanged original number is proposed for replacement. Unreported historical settings remain disclosed assumptions even if the eventual reproduction passes.

## 5. Direct v3 comparison and deferred-condition audit

The actual v3 package was found at `C:/Users/User/ucjobs/C_P11_V4/B_P11_V3/out/`. It was read directly; the review does not rely solely on V4_NOTES' description. All seven reviewed v4 output files are byte-identical to the neighbouring original C_P11_V4 job's outputs.

Comparison anchors:

- v3 PREREG SHA-256: `63d0cf0309c500353c896e535ac8abd9c5e1938953353c0aa17aedf78f2bd8c7`.
- v4 PREREG SHA-256: `0ba88b74da4d151199254670405b4bff960b5ad5aef629bd028c222232c0457e`.
- v4 SOURCE_CHECK SHA-256: `7b38142282c6de8cab7f6266e6308c058701d04f676207f43e8aae7f5941e7b5`.

**No gate, verification obligation, or numeric new-versus-robust definition was weakened.** Python comparison found the complete SOURCE_CHECK block from “One original-result attempt per candidate” through the end of the diagnostics contract identical after trimming surrounding whitespace. The main document preserves:

- 0.005 absolute tolerance separately for the original pooled ratio and both CI endpoints; exact k/direction; no rounding allowance or model search.
- REML normal inference, each deletion re-estimating tau², fixed optimizer controls, normalized 1e-6 and 1e-9 comparisons, exact identities/flags/CI/S decisions, and stop on unresolved/nonfinite output.
- Sensitive if any CI category changes or S_i ≥ 0.5; robust only if every category is unchanged and every S_i < 0.5. “New/additional” still requires prior-report clearance. Previously reported sensitivity is now more explicitly separated from an additional-finding claim.
- The same seeded sample, headline rule including tied maxima, escalation threshold and packet constraints. V4 adds the exact binding item-4 paragraph.
- The four-hour combined effort cap, fixed candidate/outcome, prohibition on switching after diagnostics, and reporting of robustness or unresolved work.

| V3 blocker moved or resolved | Judgment under FREEZE_CRITERIA |
|---|---|
| B1: executable code/API checks and synthetic validation | **Legitimate later condition.** The analysis contract already fixes choices. Independent implementation and synthetic validation must precede any real-data reproduction gate; this was not changed into permission to select methods later. |
| B2: absent hub files/dependency closure/runtime parity | **Static absence resolved; runtime work legitimately deferred.** All nine formerly absent scripts are present and hashed. Optional browser-R files remain absent and explicitly disclosed. F6 does not require runtime parity or browser closure. |
| B3: stale extraction kit | **Legitimate later condition.** Synchronization is additionally required before extraction. The old builder is explicitly prohibited from regenerating outdated rules. |
| B4: fallback eligibility | **Legitimate conditional route.** The fallback remains uncleared. Its own feasibility/novelty must clear before activation/extraction; otherwise primary failure ends the study. This is expressly permitted by FREEZE_CRITERIA. |
| B5: packet capacity | **Legitimate later condition.** A supplied shared ledger and P11 eligibility list now exist; no assignment/capacity is falsely claimed. Assignment remains mandatory before verification. |

No demonstrated F1–F6 failure has been moved into a post-release heading. A future amendment that changes a frozen analytical choice or tolerance would not be mere implementation and must not be justified by real-data results.

## 6. Remaining protocol checks and researcher discretion

Selection is justified by published journal placement, the retention question, reported heterogeneity and the k/effort limits. No new calculation was used to select the primary. Earlier screening's prospective influence expectations are not adopted as findings.

The fixed outcome, comparison, complete inventory, a/b/c/d mapping, administrative row identity, source-only restriction, no row repair, no alternate follow-up, no collective deletion, and no moderators prevent material data-dependent selection. Display settings and input precision are now fixed. Known app/R numerical differences lead to a stop rather than tuning. Unstated package options are anchored to the clean-process pinned defaults.

The write-up remains 150–250 words and one specified figure, retains the existing example, reports both app and R, confines the clinical scope, and preserves the ban on priority/ranking claims and clinical recommendations. The original-document figures are unchanged. The target journal is a supplied project decision, not independently confirmed by manuscript.txt.

The main document exceeds TASK_COMMON's 900–1,600-word aim; the preceding V4 job applies a 3,000-word cap and independently counting the main document confirms 2,295 words. This is not a freeze criterion and is not treated as a methodological failure.

## 7. Every open problem and required next step

1. **P2 correction:** apply R2-01 to the supporting Table 1 header description; synchronize that correction into any source map.
2. **Independent implementation and pinned environment:** executable R scripts, installed API/default checks and sessionInfo remain missing. R cannot run on this node. On pc2, validate only newly generated synthetic_* fixtures marked “SYNTHETIC - not data”, including specified boundary/failure cases, before any real-data reproduction gate.
3. **App/R runtime parity:** no runtime pass is established. Validate every registered full/deletion/diagnostic quantity, exact identity/exclusion/flag/classification and round-trip export. The global-app versus scalar-start-R difference remains an explicit unresolved runtime risk.
4. **Browser dependency closure:** required workflow loading/export is untested; the optional webR entry and package manifest are absent. Close required dependencies or prove the unavailable optional route is not entered by the external-pc2 workflow. Do not claim built-in live R works.
5. **Extraction kit:** schemas, codebooks, blind prompts, adjudication/fourth-pass instructions and helpers still need synchronization and synthetic checks; prevent the stale v2 builder from restoring old rules. Finish before extraction.
6. **Verification capacity:** reserve ≤30-minute packets in the single cross-paper ledger, respecting one per person per ISO week, the P11 eligibility list and seven-day reassignment. Model-family logs, reviewer initials/dates and completed verification are future records, not current evidence.
7. **Fallback eligibility:** its nonspecific prior sensitivity analysis and the 35 PubMed IDs still lack adequate dispositions. Clear under the fixed equivalence definition before activation, or stop after primary failure. Its raster-reading risk remains part of future independent extraction/verification.
8. **Evidence limitations:** novelty coverage remains index/title/citing-record limited; no universal absence claim is supported. Original unreported settings remain assumptions. Historical access/citation snapshots and supplied commit attribution were not independently reconstructed; current content/hash checks are complete. The target-journal submission destination is unconfirmed.
9. **Release and real-data gates:** no GitHub release/server timestamp, release digest record or Zenodo DOI exists from this review. Release separately with all normative companions. Then complete applicable prerequisites, independent extraction, reproduction, diagnostics and human verification before classification/reporting. All post-release code changes must be dated deviations independent of real-data results.

These open conditions are not P0 findings under the supplied freeze criteria. The primary may be frozen; real-data work remains gated.
