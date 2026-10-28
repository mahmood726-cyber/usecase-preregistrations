# P04: preregistration of the next five candidate screens

**DRAFT for screening freeze, 2026-10-28. No new candidate search, screening, extraction or real-data analysis has been performed in this job. Not frozen or released.**

Paper: P04. Field: diabetes pharmacotherapy network meta-analysis (NMA). Preferred journal: *Diabetes, Obesity and Metabolism*, as assigned in the inherited P04 task; publication there is preferred, not mandatory. Seed: **2026102804**.

## 1. Authority, purpose and exclusions

**Ayesh et al. (2024), doi:10.1111/dom.15725, is DROPPED ENTIRELY** by Mahmood's decision of 2026-10-28 ("leave Wiley in that case and use the other way you suggested"; MAHMOOD_DECISIONS.md item 14) because its source was inaccessible: the Data S1 supplement is bot-blocked at Wiley (HTTP 403, not bypassed) and no open-access copy exists (OpenAlex: publisher copy only, no repository full text; no PMC/Europe PMC copy; no preprint). **This decision was made before any data from Ayesh were seen**; no Ayesh trial-level value was ever read or extracted. It is a source-feasibility disposition, not a result-based switch.

This is a preregistration of SCREENING ONLY. JOB.md, JOB_RULES.md and SCREENPREREG.md govern this job, superseding the older TASK_COMMON/TASK_PAPER instructions to choose from the previous list or deliver a use-case registration. Mahmood's decisions 8 and 12 fix prospective, seeded screening; The inherited screening registration applies P04 route (c); this job amends only the retrieval instrument before freeze. No network queries were run here, including API documentation or discovery queries.

Every previously approved candidate failed a pre-specified source-feasibility gate. The primary was blocked, and the independently checked fallback lacked the necessary published inputs. These are source failures, not failed numerical reproductions. Do not reopen them or substitute another endpoint in this screen.

| Excluded review | DOI (canonical lowercase) | Published-feature gate and supplied evidence |
|---|---|---|
| Ayesh et al. (2024) | 10.1111/dom.15725 | Source gate: Data S1 was HTTP 403/BLOCKED; main Figure 3A contains pooled estimates, not complete trial inputs. B_P04_V3/out/SOURCE_CHECK_P04.md sections 1-2 and BLOCKERS_P04.md B1. S_P04_SCREENPREREG/out/PREREG_P04_screen.md section 1 records route (a) exhausted (OpenAlex publisher-only copy; no repository/PMC/Europe PMC/preprint copy found in the prior search) and route (b) unavailable without blocked Wiley. No bypass. |
| Chen et al. (2023) | 10.1186/s12933-023-02035-8 | Source gate: the locally readable XML/DOCX/ZIP lacks complete trial-level diabetes-subgroup mortality effects/uncertainties or deaths/analysed denominators. Its numerical panels are pooled outputs. SOURCE_CHECK sections 1 and 3; BLOCKERS B1. This supersedes the earlier report that the supplement was merely unreadable. |
| Karagiannis et al. (2024) | 10.1007/s00125-024-06144-1 | Source gate: complete study effects and uncertainty not located in the accessible article/ESM; dataset offered on request. CANDIDATES_P04.md section 3. Author contact and primary-trial reconstruction are outside the protocol. |
| Yao et al. (2024) | 10.1136/bmj-2023-076410 | Effort and added-insight gates: estimated 4.5-6 hours exceeds four hours; original already includes leave-one-out and other sensitivity work; trial inputs unverified. CANDIDATES_P04.md, "Other candidates screened" and "Yao source and novelty". |
| Bernardi et al. (2026) | 10.1111/1753-0407.70192 | Profile and source gates: qualifying high profile not established and complete published trial inputs unverified. CANDIDATES_P04.md, "Other candidates screened" and "Bernardi source and novelty". |

All five DOIs are excluded regardless of endpoint, title variant, later access change or database order. The first two were the approved primary/fallback; the other three were also substantively screened. An exclusion is not a claim that a publication contains an error.

Evidence used: CANDIDATES_P04.md; B_P04_V3/out/SOURCE_CHECK_P04.md; B_P04_V3/out/BLOCKERS_P04.md; the v3 PREREG and CHANGELOG; MAHMOOD_DECISIONS.md; FIELD_USE_CASE_PROTOCOL.md; FREEZE_CRITERIA.md; JOB.md. Only a v3 package is supplied here; no v4 source report is claimed. The later FREEZE_CRITERIA supersede v3's treatment of synthetic runtime validation as a pre-freeze blocker.

## 2. Frozen discovery frame and executable queries

Eligible scope is a published original NMA of pharmacological treatments in people with diabetes, or an explicitly separable diabetes subgroup. Exclude protocols, nonnumerical reviews, primary trials, nonpharmacological-only networks, and obesity-only populations without a diabetes-specific outcome network. Include all journals and languages if the required published material is readable. No citation threshold or target-journal restriction is used to collect search hits.

Publication window: **2016-10-28 through 2026-10-28 inclusive**. Open access is required. The frame is **Europe PMC ONLY**, using the registered TITLE_ABS phrase query below, not a claim of all diabetes NMAs in existence. Search phrases, indexing and mandatory DOI availability limit coverage.

Europe PMC query (literal parameter value):

~~~text
(TITLE_ABS:"network meta-analysis" OR TITLE_ABS:"network meta-analyses" OR TITLE_ABS:"network meta analysis" OR TITLE_ABS:"network metaanalysis" OR TITLE_ABS:"mixed treatment comparison" OR TITLE_ABS:"mixed-treatment comparison") AND (TITLE_ABS:diabet* OR TITLE_ABS:antidiabet* OR TITLE_ABS:antihyperglyc*) AND FIRST_PDATE:[2016-10-28 TO 2026-10-28] AND OPEN_ACCESS:Y
~~~

The first-page URL is a copy-pasteable public GET request. Subsequent pages change only cursorMark. Do not add API keys, credentials, title-specific rescue searches, journal filters or search terms. The script prints this exact URL with --print-queries without accessing the network.

~~~text
epmc-01
https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28TITLE_ABS%3A%22network%20meta-analysis%22%20OR%20TITLE_ABS%3A%22network%20meta-analyses%22%20OR%20TITLE_ABS%3A%22network%20meta%20analysis%22%20OR%20TITLE_ABS%3A%22network%20metaanalysis%22%20OR%20TITLE_ABS%3A%22mixed%20treatment%20comparison%22%20OR%20TITLE_ABS%3A%22mixed-treatment%20comparison%22%29%20AND%20%28TITLE_ABS%3Adiabet%2A%20OR%20TITLE_ABS%3Aantidiabet%2A%20OR%20TITLE_ABS%3Aantihyperglyc%2A%29%20AND%20FIRST_PDATE%3A%5B2016-10-28%20TO%202026-10-28%5D%20AND%20OPEN_ACCESS%3AY&format=json&resultType=lite&pageSize=1000&cursorMark=%2A
~~~

Europe PMC: JSON, resultType=lite, pageSize=1000, cursorMark=*. Retrieve all pages before ordering, with no record cap or five-hit truncation. A successful zero requires hitCount=0 and an empty result list. A complete nonempty retrieval must reach the stable hitCount using distinct source/ID records; changing counts, duplicate identities, repeated cursors or a missing next cursor before that count fail the run. Preserve partial metadata for audit but never screen or emit an incomplete frame.

For Europe PMC HTTP 5xx, retry the **same URL** at most four times after the initial attempt, with backoff of **1, 2, 4 and 8 seconds** (five attempts total; 45-second timeout per attempt). Record each attempt, UTC time, HTTP status and backoff. This applies equally to subsequent cursor pages. No retry of 401/403/429, bot/non-JSON responses, transport or schema failures; no credentials, mirror changes or bypass. If retrieval is still incomplete, record the screen as **FAILED/BLOCKED**, frame_count=null (unknown, never zero), write the failure audit and exit nonzero without frame_P04.jsonl.

**OpenAlex is removed from discovery.** No OpenAlex search= query, cursor or metadata record may enlarge this frame. It remains only for each visited candidate's novelty work/lookup and associated profile counter under the unchanged G4 rule; the exact candidate novelty requests are in G3. This pre-freeze instrument correction overrides SCREENPREREG.md's older request for a dual-index discovery frame; its supplied count evidence is recorded in section 7.

Bibliographic rules applied by screen_P04.py:
- Normalize DOI strings by removing a DOI resolver prefix or "doi:", URL-decoding, trimming outer whitespace and lowercasing. Preserve suffix punctuation. Deduplicate by canonical DOI across the returned Europe PMC records, retaining source IDs, titles, dates, OA flags and query provenance.
- Missing/invalid DOI records are logged as metadata exclusions, never assigned an invented identifier or a title-based hash. This fixes an explicit DOI-addressable frame; there is no discretionary manual DOI rescue.
- Use the earliest valid complete publication date observed for that DOI across the returned metadata. Retain it only within the inclusive window and with at least one positive OA flag. Log all conflicting dates/flags. If no complete date is available, exclude with reason. No year-only date imputation.
- Exclude the five previous DOIs. Any otherwise retained hit remains **UNSCREENED**: an OA flag does not establish a reuse licence, clinical scope, input completeness, k, or novelty.
- Any discovery failure remaining after the specified Europe PMC 5xx retry schedule prevents emission of a complete frame. Record FAILED/BLOCKED with an incomplete retrieval audit and stop; do not substitute OpenAlex, a truncated frame or a zero count. HTTP 401/403/429 is recorded as blocked without retry or workaround.
- Preserve requests, UTC times, response hashes, reported counts, retrieved counts, metadata and metadata exclusions in frame_P04_audit.json. Bibliographic dates/index counts may differ; never add citation counters across databases.

The frame builder performs no clinical screening. k is an outcome-specific published count of independent trials, not arms, contrast rows or review-wide k. The manual gate requires **5 <= k <= 60**, readable per-study arm or contrast inputs, and at least one target comparison never made head-to-head in that outcome network. These features cannot be reliably filtered in the discovery APIs.

## 3. Order, fixed units and stopping

For each retained canonical DOI compute the lowercase hexadecimal SHA-256 of UTF-8:

~~~text
2026102804|P04|screen|<doi>
~~~

Sort ascending by digest, then by canonical DOI in the theoretical event of a hash tie. screen_P04.py writes the entire ordered Europe PMC frame to frame_P04.jsonl; it does not truncate to five or label any candidate eligible.

After the screening registration has a public release, pc2 runs the queries once and preserves that timestamped frame and audit. Screen records strictly in this order until **five have a completed screening disposition, or the frame is exhausted**. Do not skip an unpromising title, a bot-blocked record or a failure to obtain five passers. Each visited record consumes one of the five slots, including an out-of-field hit or terminal gate failure. Complete its gate sheet with PASS, FAIL, UNRESOLVED or NOT ASSESSED (with the blocking reason); do not bypass an access restriction merely to fill a later field. No sixth replacement is allowed. Unvisited records stay UNSCREENED.

Before reading numerical result cells, fix one outcome, population, follow-up rule and target contrast for each visited candidate. Use the original's explicitly designated primary outcome; if several, use the following priority order. If none is designated, apply the same order to its reported outcomes: all-cause mortality; cardiovascular mortality; major adverse cardiovascular events; heart-failure admission; kidney composite outcome; HbA1c; body-weight change; severe hypoglycaemia; remaining outcomes alphabetically by the original label. Do not promote another outcome if the fixed one fails k or source feasibility. Use the original's designated primary follow-up; if none, its longest reported outcome-level analysis time. Do not copy trial-level follow-up or outcome rows.

Choose a never-directly-compared pair that the original explicitly motivates in its title/objectives; if several qualify, or none is named there, choose the alphabetically earliest unordered pair of the original treatment-node labels among such pairs. Comparison scope is the fixed outcome network and the original dose/node definitions, not a claim that the drugs have never been compared anywhere. Confirm indirect-only status from an explicit original statement or its labelled network structure, never by computing effects. No new merging of doses or nodes. Record the target before inspecting its pooled estimate. If absence of a direct edge cannot be verified without numerical extraction, the method-fit gate is unresolved and the record cannot pass.

## 4. Candidate gates, published features only

Apply the following gates to each visited record. A positive decision requires all to pass; an unresolved required input is not assumed present. No trial row, trial effect, count, CI, dose or moderator may be transcribed, copied or paraphrased during screening. Record only source locations, column headers, qualitative completeness/readability, published aggregate k/model statements and the fixed analysis question. No candidate data are calculated, reconstructed, digitised, uploaded to the app or tested in R.

### G1. Permitted source, licence and readable complete inputs

Require a printed open licence compatible with this research use (such as CC BY, CC BY-SA, CC0, or CC BY-NC for this noncommercial use), including the relevant supplement's terms. Record the exact licence text identifier and locator; an OA index flag alone is insufficient. Sources must be the candidate's own article, printed forest/table, or published supplement, including a permitted OA copy of that same material. No author contact, login, paid access, primary-trial hunting, combining reviews or inversion of pooled outputs.

Require a complete source for the fixed outcome: either trial effects and labelled SE/CI, or arm-level outcome means with SD/SE and analysed n, or events and analysed denominators, as appropriate. Multi-arm trials must retain all arms and adequate dependence information; a future conversion to complete contrast pairs must be possible under a source-backed rule. Unsupported dependence, invented covariance, imputation or incident-rate-to-event reconstruction does not pass. Numeric results in league tables or treatment-level network plots are not trial inputs.

Record FEASIBLE (text) or FEASIBLE-IMAGE (printed numerals readable in an image) only if completeness is established without recording rows. Image uncertainty must carry into later verification. Unreadable/missing/uncertain inputs mean NOT FEASIBLE. Any required-source bot check means **NOT FEASIBLE, reason "blocked"**; record it and move on. Do not cycle through mirrors after a block. A repository copy advertised by the index can be the initial permitted route.

### G2. Clinical scope, size, method fit and added insight

Require the diabetes pharmacotherapy scope, a published outcome-specific k between 5 and 60, an indirect-only target, and a connected network described in the original. If only review-wide k is printed and the outcome-specific count cannot be established from published summary material, fail without building an inventory of study rows.

The common prospective operation is the inherited v3 whole-trial omission analysis: omit every arm/contrast of one whole trial at a time, refit the NMA and examine dependence of the fixed indirect target effect/CI. This job does not run that operation. Merely repeating a published indirect contrast, changing software, or redrawing treatment ordering cannot qualify.

Method-fit score M:
- **2:** the original has an indirect-only target not numerically reported there, and does not already perform the target whole-trial omission analysis.
- **1:** the target indirect estimate is already reported, but the original's published limitations/structure motivate a specific unreported whole-trial dependence question; its full text and supplement confirm that operation is absent.
- **0:** neither condition is established; fail.

M=1 preserves the v3 robustness interpretation of the approved P04 use case; it does not present a previously reported basic contrast as new. An equivalent operation in the original also fails, regardless of who performed it.

### G3. Novelty: Europe PMC citations and OpenAlex citing works

**Deviation:** Europe PMC and OpenAlex replace Google Scholar because Google Scholar showed a bot check ("unusual traffic") on 2026-10-28 and was not bypassed (MAHMOOD_DECISIONS.md item 3). No Scholar recheck is required.

For each candidate use its canonical DOI to identify records, then paginate both citation lists. The following are fixed request templates; URL-encode the actual DOI/IDs, log all instantiated requests and actual access dates, and retain the bibliographies:

~~~text
https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%22<URLENCODED_DOI>%22&format=json&resultType=lite&pageSize=1000&cursorMark=%2A
https://www.ebi.ac.uk/europepmc/webservices/rest/<SOURCE>/<ID>/citations?format=json&page=1&pageSize=1000
https://api.openalex.org/works/https://doi.org/<URLENCODED_DOI>
https://api.openalex.org/works?filter=cites%3A<OPENALEX_W_ID>&per-page=100&page=1
~~~

Use every Europe PMC source/ID matching the DOI; paginate page numbers and deduplicate citations by DOI or index identity. Use the canonical OpenAlex W identifier, filter=cites:<W>, per-page=100, and **page=1,2,... until an empty results page**, with at most **10,000 citing works / 100 nonempty pages**. No cursor paging, search= queries or credentials. Do not stop at a short nonempty page or merely because the reported total has been reached. Above 10,000 the check is incomplete: retain the retrieved bibliography and disclose the cap. At exactly 10,000, if no empty terminal page is available within pages 1..100, conservatively record incomplete termination coverage too; do not request an out-of-range page or falsely certify completion. An empty terminal page with a count mismatch, duplicate IDs, changing totals, invalid schema or access failure also leaves the check incomplete. Preserve both reported and retrieved counts; missing results are never zero hits. The candidate's work lookup supplies its G4 profile counter, without reintroducing OpenAlex discovery.

The optional script mode below retrieves **only** OpenAlex citing metadata for the already identified, visited candidate. It uses the same frozen-release safeguards as discovery and writes novelty_P04_openalex_<W_ID>.json under out/, preserving partial results and returning nonzero for incomplete coverage. It never writes frame_P04.jsonl or decides equivalence. The Europe PMC DOI/citation checks, all returned-title/abstract review and permitted-source adjudication remain mandatory under this unchanged gate.

~~~text
python out/screen_P04.py --openalex-cites <OPENALEX_W_ID> --screen-release-url <PUBLIC_GITHUB_RELEASE_URL> --screen-release-doi <ZENODO_DOI_URL> --prereg-sha256 <FROZEN_PREREG_SHA256> --script-sha256 <FROZEN_SCRIPT_SHA256>
~~~ Retain source totals and retrieved totals separately. Screen all returned citing titles/abstracts, not just titles containing "reanalysis", and inspect plausible equivalents through permitted published sources. Novelty coverage is through the actual screening date; the discovery publication window stays fixed.

**Same equivalence definition as v3:** a numerical re-analysis reuses this same review's fixed outcome-specific trial network and target, omits each whole trial with all arms, and refits the remaining NMA to assess target effect/CI dependence. Different software or thresholds do not make it different. Updated/overlapping reviews, other outcomes, alternative-model analyses, bias-restricted subsets, sequential accumulation and nonnumerical commentary are not automatically equivalent. Establish equivalence from published methods, not a title match. For M=2 also check that the proposed previously unreported contrast is not already supplied by the original supplement or later exact-network work.

Equivalent prior work means FAIL. Successful searches finding none mean "no equivalent identified", never proof of absence. A partial citation list is disclosed and does not itself block later freeze under F2. A failed request is not a zero-hit result: both indexes must return a usable search/citation response, including a verified zero-hit response if applicable. A wholly failed index leaves novelty UNRESOLVED; a successful DOI lookup with no indexed record is a disclosed coverage limitation, not a failed request. An unresolved plausible exact equivalent prevents selection; a required adjudication source blocked by a bot check is recorded as blocked/NOT FEASIBLE. Do not infer clearance from inaccessible content.

### G4. Protocol "powerful" features

All evidence must be present in the original or establish the protocol's external profile/ongoing-question criterion; later sources are not used to predict an analytical result.

Profile score P (take highest applicable; require P >= 1):
- **3:** published in the assigned target journal.
- **2:** the exact review is substantively cited in a readable clinical guideline; verify the guideline context, not a search snippet.
- **1:** at least 100 OpenAlex cited_by_count at the timestamped screen. This is the pre-stated operational definition of "widely cited", not a bibliometric assertion about previous candidates.
- **0:** none established; fail. Missing counters are unknown, not zero; another verified profile route may qualify.

Live-question score L (require L >= 1):
- **2:** the original explicitly identifies an unresolved clinical controversy or a claim with practice-changing implications for the fixed target.
- **1:** the original documents ongoing trials or an explicitly unresolved comparative-treatment decision for that target.
- **0:** no published support; fail.

Record the supporting non-row passage/location and a prospective clinical question. Do not score the size, direction, significance or treatment ordering of any recalculated effect. Stable results are as acceptable as changes.

### G5. Effort cap

At most **four analytical hours** for one outcome from one review, including input preparation/checking, original reproduction, one focused omission analysis, one figure and a short letter. Independent extraction/adjudication and mandated human verification time are additional and not erased from the project plan. Estimate each analytical component in 0.25-hour increments from the printed source format/complexity, and sum to E; require E <= 4. No primary-report reconstruction or author contact can rescue an over-cap record.

Budget at most 60 minutes for each screening disposition itself, separate from E. Unresolved mandatory gates when this screening cap expires mean NOT CLEARED and consume the slot. Record coverage/time limits; do not silently extend a preferred candidate's cap.

## 5. Selection and complete audit

Among passers only, choose the strongest by this fixed lexicographic order:

1. Higher M (method fit and demonstrable addition).
2. Higher L (live clinical question).
3. Higher P (profile, with target-journal preference).
4. Lower E (estimated analytical hours).
5. Earlier seeded screen order; canonical DOI is the final hash tie-break.

This is internal candidate selection, not a claim of clinical treatment superiority. Do not change weights or choose based on any new calculation. The second passer under this ordering is the fallback. If no candidate passes, stop and report every failure. If exactly one passes, report a provisional primary and "no cleared fallback"; do not relabel a failed record as fallback, screen a sixth, or advance a fictitious pair. Resolving an unavailable pair needs a later, separately registered decision.

The later screen log must contain each visited DOI, frame order/hash, timestamps, fixed endpoint/population/follow-up/target, published k locator, licence and source locators/headers, gate decisions and reasons, bot/access failures, exact novelty requests and coverage, equivalence disposition, M/L/P/E evidence and estimates, total screening minutes, final decision, and primary/fallback ordering. Keep aggregate summaries only; no per-study fields. Retain every exclusion and every terminal failure. Preserve the full original frame and untouched unvisited records.

No calculated result on candidate data can inform eligibility, scoring, ranking or switching. No real-data model runs, trial-row transcription, author contact, numbers changed, priority claims or publication-error allegations are authorised.

## 6. Freeze, execution and what follows

Before query execution or candidate screening, freeze this document and screen_P04.py at a public paper-specific release in mahmood726-cyber/usecase-preregistrations, and record both file SHA-256 digests and the server-side UTC release time. **The public GitHub release is the precondition for query execution and screening.** The Zenodo DOI is recorded when minted (value `PENDING` until then); it is not a precondition (pre-freeze amendment, coordinator, 2026-10-28, consistent with Mahmood's rule "no extraction or analysis before the release exists"). This local draft is not that release. Future changes must be dated and released before applying them; never silently alter terms, exclusions, order or cap after seeing hits.

pc2 first verifies the release, archived bytes and DOI, then runs:

~~~text
python out/screen_P04.py --screen-release-url <PUBLIC_GITHUB_RELEASE_URL> --screen-release-doi <ZENODO_DOI_URL> --prereg-sha256 <FROZEN_PREREG_SHA256> --script-sha256 <FROZEN_SCRIPT_SHA256>
~~~

Arguments are required safeguards; the script verifies local hashes and identifier syntax, not the remote release's existence or timestamp. Default files are beside the script under out/. Existing frame/audit files are never overwritten. A failed attempt is preserved; a permitted later retry must be logged and use a fresh child directory via --output-dir, with unchanged queries and no screening of partial results. A bot check or authentication requirement is reported, not bypassed. No credentials or external login are requested by this job.

After five dispositions (or exhaustion), the selected pair enters the same use-case pipeline: candidate-specific F1-F6 documentation, REDTEAM2 review, resolution of its F1-F6 failures, use-case freeze and separate GitHub/Zenodo release, then authorised extraction. The screening release alone does not authorise extraction.

F1 requires independently FEASIBLE/FEASIBLE-IMAGE inputs for each activating candidate. F2 preserves equivalence checks and disclosed coverage limits. F3 fixes one original reproduction configuration before data, including documented defaults for unstated choices; no model search. F4 fixes the outcome, estimand, all app/R settings, numeric tolerances, new/robust definitions and fallback triggers before extraction. Those values cannot be chosen for nonexistent candidates in this screening registration. F6 requires file/function/hash evidence of actual implemented app features, with unsupported operations labelled R-only.

F5 carries forward MAHMOOD_DECISIONS.md item 4 exactly:

> Human verification: humans check headline rows, a seeded 5% of the other rows (at least 1), and only the fields still disputed after a third-model adjudication plus a fourth AI re-check (agy, different family). If the sample error is over 2%: a full AI re-extraction plus a human re-check of the headline rows. Packets are about 30 minutes or less; at most one per person per week across all papers (COAUTHOR_LOAD.md); Mahmood is in the rota; a packet not returned in 7 days is reassigned.

Under FREEZE_CRITERIA.md, synthetic code validation, synthetic app/R parity, browser dependency closure, extraction-kit synchronisation and packet assignments are mandatory post-release/pre-analysis conditions, not additional freeze blockers. All synthetic tests must pass before any real reproduction. Use R 4.6.0/netmeta 3.7.0 on pc2; no R or browser engine ran here.

Static scope evidence from the prior screening registration, with file hashes rechecked in this job at supplied allmeta pin 14dc545bcba87a02158b2f445c28450e7eaf6b89:
- nma/index.html: parseContrasts, analyseState, relEffect, __almNmaCompute; SHA-256 b1c85af5cf30b44a34528ff97493572195823295268c9450d737fa1b097a6239.
- shared/nma-multiarm-v1.js: buildStudies, auditStudies, fit, analyse; SHA-256 1eaebe7b73b3f5e0fcbb6cf39c015b7a18dc393993ffe64946aeb8ae9313104a. This fingerprints supplied bytes; independent commit provenance for this shared file was not established by PIN.txt.

The source implements contrast-based fits and whole-study multi-arm checks; input effects are treatment2 minus treatment1. Arm-to-contrast conversion requires a later fixed, source-supported contract. Repeated omission orchestration is external to these individual app fits and is not claimed to be a built-in UI feature. v3's numerical/refusal guard and installation concerns are carried forward for candidate-specific review, not claimed repaired here. Static review is not runtime or app/R parity validation.

If the primary later fails a gate, activate only the independently cleared, pre-specified fallback under its own frozen specification; if it also fails or is unavailable, stop. Reproduce the original within pre-frozen printed-number tolerances before new analysis. Report robust outcomes and failures. Keep the protocol's 150-250-word, one-figure plan, no clinical recommendations and no priority/ranking claims.

## 7. Status, limitations and amendment record

No new search results or candidates were obtained; no frame was generated. Only offline synthetic tests of the metadata builder, bounded retry behavior and OpenAlex candidate-citation helper are authorised here. Their separate report is a software check, never a clinical finding.

Outstanding handoff conditions: this screening release/DOI and frozen digests do not yet exist; live retrieval with the corrected instrument remains to be run on pc2 after release; the supplied pc2 count/access observations below are not a completed frame; all future candidate feasibility, novelty and selection remain unknown. Do not substitute a partial frame or login if access fails. The subsequent F1-F6/REDTEAM2, release, synthetic runtime, browser, extraction-kit, verification and reproduction requirements remain prospective. No v4 source-check package was supplied.

BLOCKERS_P04_screen.md reports blockers to this screening specification only; NONE does not certify a candidate, a public release or later analysis readiness.

| Date | Amendment | Timing |
|---|---|---|
| 2026-10-28 | Initial screening-only registration under binding route (c); fixed queries, exclusions, order, operational criteria and stopping rules | Prior S_P04_SCREENPREREG package; before new candidate screening |
| 2026-10-28 | **Pre-freeze INSTRUMENT FIX (binding JOB.md): Europe PMC-only discovery; same registered TITLE_ABS phrases and cursorMark/all-pages retrieval; bounded 5xx retry; failed/incomplete retrieval recorded FAILED/BLOCKED, never zero. OpenAlex removed from discovery and retained for candidate novelty via filter=cites:<W>, per-page=100, page paging, maximum 10,000.** | Before freeze, data extraction or any new candidate screening; based only on pc2 instrument counts/access observations |

The amendment relies on the observations supplied in this job's JOB.md, **not new queries run here**. pc2's 2026-10-28 instrument check fetched only meta.count / hitCount for the registered query URLs. It found unbounded fuzzy OpenAlex search= frames:

| Historical OpenAlex query position | Reported P04 count |
|---|---:|
| 1: diabetes "network meta-analysis" | 6,191 |
| 2: diabetic "network meta-analysis" | 2,237 |
| 3: antidiabetic "network meta-analysis" | 2,237 |
| 4: diabetes "network meta-analyses" | 56,404 |
| 5: diabetes "network meta analysis" | 4,496 |
| 6: diabetes "network metaanalysis" | 56,430 |
| 7: diabetes "mixed treatment comparison" | 6,555 |
| 8: diabetes "mixed-treatment comparison" | 22,577 |

The same supplied instrument check reported P02 counts **835,052 and 834,162**. These are provider query counts, not candidates screened, unique eligible reviews or results. JOB.md also records OpenAlex cursor paging returning **HTTP 401 beyond the first page without an API key**, observed earlier on 2026-10-28, and Europe PMC temporarily returning **503**. The binding decision therefore uses Europe PMC's phrase-precise TITLE_ABS/cursorMark route with bounded recovery from 5xx; it does not treat an outage as an empty field.

The seed **2026102804**, DOI normalization and exclusions, date window, OA requirement, seeded order, five-disposition cap, outcome/target rules, all candidate gates and equivalence definition, M/L/P/E selection and tie-break, effort caps and subsequent pipeline remain unchanged. The extra cap/status safeguards implement retrieval completeness; they do not choose candidates or alter the partial-coverage rule in G3/F2.

**Screening freeze: SHA-256 digests and UTC server release time to be recorded at release.**
