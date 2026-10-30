# P04 screening v2 (P04-screen-v2): Option A approved (NOT YET RELEASED)

Drafted 2026-10-30; finalized 2026-10-30 after Mahmood's decision, relayed in chat on 2026-10-30: "P02 and P04: Option A v2 approved. Proceed." That decision authorizes one further five-disposition screen under **Option A as specified in section 2 of this document**: continue the archived v1 seeded order from original frame rank 22, after excluding all 26 DOIs listed in section 2 and Appendix A (including the seven title-screened referrals). **Option B was NOT CHOSEN**; it is retained only as a record of the alternative considered and can never be executed under this registration. Nothing may be queried, screened, scored, selected, extracted or analysed before the public **P04-screen-v2** GitHub release exists (section 7). The file keeps its historical basename, `PREREG_P04_screen_v2_DRAFT.md`, which is the name the script checks (section 7).

## 1. Why this draft exists, and what v1 concluded

The released **P04-screen-v1** ended as a **pre-registered feasibility failure: 5/5 full-screen dispositions FAIL, zero passers, no primary and no fallback**. Its "if nothing passes, stop and report" rule ended this use case. **V2 exists only because v1 found no feasible candidate.** A second attempt requires a new decision; it is not an automatic continuation, a rescue of a failed candidate, or evidence of an analytical result.

Authority: JOB.md; JOB_RULES.md; SCREENPREREG.md; MAHMOOD_DECISIONS.md items 3-6, 12 and 14; [released v1 specification](../P04_screen/PREREG_P04_screen.md), [FREEZE.json](../P04_screen/FREEZE.json), [full-screen log](../C1_P04_FULLSCREEN/out/FULLSCREEN_P04.jsonl), and [screen notes](../C1_P04_FULLSCREEN/out/SCREEN_NOTES_P04.md), especially Ordered dispositions and Coverage and sequence deviations. V1 was frozen at 2026-10-28T21:53:34+00:00. Its historical embedded "DRAFT" wording does not undo the release established by JOB.md and FREEZE.json. No release was remotely checked in this job.

The following are historical screening findings, not new screens. G3 novelty was NOT ASSESSED in C1; no claim that novelty failed or cleared is made. All five also had unresolved G4 profile evidence. The cap was reached; the referral list and original frame were not exhausted.

| Full screen / v1 frame rank | DOI | Recorded failure and locator | Same requirement checked earlier in v2 |
|---|---|---|---|
| 1 / 2 | 10.1186/s13613-025-01471-x | G1: characteristics/protocols and pooled outputs do not supply complete mortality inputs; main Table 1, Fig3, supplement eTable1/eTable2 | Inspect input-source headers and coverage before pooled results or novelty work |
| 2 / 5 | 10.3389/fendo.2026.1891173 | G1 UNRESOLVED: readable S23-S28 do not certify comparator/shared-arm/whole-trial mapping; Fig2D and Table S26 | Require source-backed mapping completeness at G1; readable numerals alone cannot pass |
| 3 / 6 | 10.1038/s41598-021-89620-7 | G1: no complete obese-subgroup inputs, data on request (notes2); follow-up unresolved (Sec10-Sec13) | Check data-availability route, completeness and fixed outcome-level follow-up before target-result inspection |
| 4 / 7 | 10.1186/s13098-026-02226-9 | G2: published outcome k=105, above 60 (Sec14/Sec16); G1 also fails, reuse compatibility unresolved | Lock outcome, then verify its published k and licence; no smaller endpoint substitution |
| 5 / 9 | 10.1007/s40123-025-01247-3 | G2: published DME-network k=three, below five (Sec9/supplement p2); G1 incomplete/nonpublic inputs (Sec8/Sec10/notes3) | Require outcome-network k and complete permitted published inputs; never substitute review-wide k |

Earlier exclusions remain: Ayesh 10.1111/dom.15725 (blocked required supplement; dropped entirely before data were seen); Chen 10.1186/s12933-023-02035-8 (complete subgroup inputs absent); Karagiannis 10.1007/s00125-024-06144-1 (complete inputs not located; on-request route); Yao 10.1136/bmj-2023-076410 (over four-hour effort and existing sensitivity work); Bernardi 10.1111/1753-0407.70192 (profile and input completeness unestablished). Evidence: v1 section 1 and the locally available [CANDIDATES_P04.md](../../S2_P04_SCREENPREREG/CANDIDATES_P04.md), [v3 SOURCE_CHECK sections 1-3](../../S2_P04_SCREENPREREG/B_P04_V3/out/SOURCE_CHECK_P04.md) and [v3 BLOCKERS B1](../../S2_P04_SCREENPREREG/B_P04_V3/out/BLOCKERS_P04.md). Older suggestions to reopen Ayesh are superseded by Mahmood's item 14. No v4 source-check package was located; none is claimed.

## 2. Decision options and exhaustive disposition of the old frame

The adjacent local triage archive was found and read using Python; no candidate article was opened. Its [frame](../../T_P04_TRIAGE/frame_P04.jsonl) has 561 records. [TRIAGE_P04.jsonl](../../T_P04_TRIAGE/out/TRIAGE_P04.jsonl) records ranks 1-21: nine title exclusions and twelve referrals. Five referrals received full screens; seven did not. Ranks 22-561 (540 records) were never triaged. The audit explicitly distinguishes the historical 12-referral stage from v1's written five-disposition limit; this draft does not rewrite that history.

**Conservative exclusion rule:** "already screened" includes ANY completed title-level triage, not just a full-text failure. Therefore all 21 triaged DOIs are excluded under BOTH options, plus the five pre-v1 exclusions: 26 DOIs in total. In particular, the seven referred-but-never-full-screened records are not silently re-entered. This is a stricter sampling exclusion, not a relaxed gate. Their historical referral status is not recast as a full-screen failure.

Those seven are:

| v1 frame rank | DOI | A and B treatment |
|---|---|---|
| 11 | 10.7759/cureus.100927 | Excluded: already title-screened, never full-screened |
| 14 | 10.3389/fendo.2023.1282584 | Excluded: already title-screened, never full-screened |
| 17 | 10.3389/fphar.2021.751496 | Excluded: already title-screened, never full-screened |
| 18 | 10.3389/fmed.2025.1721311 | Excluded: already title-screened, never full-screened |
| 19 | 10.1111/jdi.13603 | Excluded: already title-screened, never full-screened |
| 20 | 10.1007/s40122-025-00789-5 | Excluded: already title-screened, never full-screened |
| 21 | 10.1007/s13300-023-01459-5 | Excluded: already title-screened, never full-screened |

Appendix A lists all 21 triaged exclusions. Appendix B lists **every one of the 556 v1-frame records never full-screened, by DOI and original rank**, including the nine title exclusions, seven pending referrals and 540 untouched records. This is a provenance inventory, not a new eligibility assessment.

**Option A (CHOSEN) - continue the archived v1 seeded order.** After a new decision and screening release, use the exact archived frame bytes, remove all 26 excluded DOIs, and preserve the remaining original order. Start at original frame rank 22. Preserve the original hash/rank and add a v2 visit index; do not refresh metadata or recompute order using the new seed. Untouched records remain unassessed until visited. No new discovery request is needed. The archive hash must match Appendix C; otherwise stop, with no substitute query.

**Option B (NOT CHOSEN; record of the rejected alternative only) - a fresh frame with a NEW seed fixed now: 2026103004.** After a new decision and screening release, rerun the exact Europe PMC query in section 3 once, preserving its unchanged date window and OA requirement, then remove all 26 excluded DOIs and deduplicate. Order every retained DOI by sha256("2026103004|P04|screen|<doi>"), ascending hexadecimal digest, then canonical DOI. This seed differs from v1's 2026102804. No new seed was tested against real candidates. The 540 untouched old-frame DOIs may enter only if returned by this complete fresh retrieval and still bibliographically eligible; they have no reserved slots or priority. A missing old-frame DOI is not manually added. The nine title exclusions and seven uncompleted referrals remain excluded regardless of fresh retrieval.

**Decision: A** (Mahmood, 2026-10-30), the option this draft recommended, because an intact timestamped frame and unused seeded order exist. It avoids index drift, an unnecessary new retrieval and a new ordering decision after failure, while preserving all requirements. Its loss of the seven triaged referrals is disclosed above. The decision named A before any v2 query or screen. B is not a backup to invoke after seeing A's outcomes; the unused option cannot be tried automatically.

## 3. Scope, discovery instrument and metadata rules

Unchanged field: original pharmacological NMA in people with diabetes or an explicitly separable diabetes subgroup, including qualifying diabetes complications. Exclude protocols, nonnumerical reviews, primary trials, nonpharmacological-only networks and obesity-only populations without a diabetes-specific outcome network. All journals/languages are allowed if readable. Assigned preferred journal: Diabetes, Obesity and Metabolism; preference is operationalised by G4, not a discovery restriction.

Publication dates: **2016-10-28 to 2026-10-28 inclusive**. Require OA; later require the printed compatible licence. A qualifying fixed outcome must have **5 <= k <= 60 independent trials**, complete printed arm-level or contrast-level inputs, a connected network, and at least one target comparison never made head-to-head in that same outcome network under the original node definitions.

Preserve v1's pre-freeze instrument correction: **Europe PMC only for discovery; OpenAlex only for novelty and profile**. SCREENPREREG.md's generic dual-index request is satisfied by specifying both services' roles and exact templates below, without reversing the released correction. No OpenAlex search= frame is reintroduced. V1 section 7 records earlier fuzzy counts and access limits; no claim about current API availability is made.

Literal Europe PMC query:
~~~text
(TITLE_ABS:"network meta-analysis" OR TITLE_ABS:"network meta-analyses" OR TITLE_ABS:"network meta analysis" OR TITLE_ABS:"network metaanalysis" OR TITLE_ABS:"mixed treatment comparison" OR TITLE_ABS:"mixed-treatment comparison") AND (TITLE_ABS:diabet* OR TITLE_ABS:antidiabet* OR TITLE_ABS:antihyperglyc*) AND FIRST_PDATE:[2016-10-28 TO 2026-10-28] AND OPEN_ACCESS:Y
~~~

The exact copy-pasteable first-page URL is printed in Appendix D and by the script's offline --print-queries mode. Use JSON, resultType=lite, pageSize=1000 and cursorMark=*. Retrieve all pages before ordering. Require a stable hitCount, unique source/ID records and complete count; zero means a successful hitCount=0 with an empty list. Changing counts, duplicates, invalid/missing cursors or malformed schema stop the run. No five-hit truncation.

Retry Europe PMC HTTP 5xx only, on the same URL, at 1, 2, 4 and 8 seconds after the initial attempt; five attempts total, each with a 45-second timeout. Log every attempt, status, UTC time, response hash and backoff. Do not retry 401/403/429, non-JSON/bot responses, transport or schema failures. No login, credentials, mirrors or bypass. Incomplete discovery means FAILED/BLOCKED, frame_count=null (unknown, never zero), failure audit and nonzero exit; no frame may be screened or emitted.

Normalize DOI by trimming whitespace, removing DOI resolver/doi: prefixes, URL-decoding and lowercasing, preserving suffix punctuation. Deduplicate by canonical DOI; retain source IDs, titles, dates, OA flags and provenance. Missing/invalid DOI has a logged metadata exclusion, never a made-up ID or discretionary rescue. Use the earliest valid complete observed publication date; exclude no complete date or outside window; require at least one positive OA flag, and log date/flag conflicts. Metadata retention is UNSCREENED, never evidence that clinical gates pass.

Option A inherits these recorded discovery rules without rerunning them; Option B (not chosen) would have run them unchanged except its new exclusions and seed. Record frame/audit bytes and SHA-256. Never overwrite a run. Script outputs are frame_P04.jsonl and frame_P04_audit.json in its out/ directory or a fresh child selected with --output-dir, labelled version v2 and option. No such v2 frame is produced by this drafting job.

## 4. Visit order, early stops and fixed question

After approval AND a new public screening release, visit strictly in the chosen order until five completed screening dispositions or frame exhaustion. Each visited record consumes one slot, even a title-level failure, early G1/G2 failure, blocked source or unresolved gate at timeout. There is no new 12-referral pre-screening stage, unlimited cheap triage, sixth replacement or search for five passers. This preserves the stricter written v1 rule. Terminal failures receive a completed gate sheet; later gates are NOT ASSESSED with the reason. This is the full-screen disposition convention even when failure is established early.

Before numerical result cells: fix the original's designated primary outcome; if several or absent, use all-cause mortality, cardiovascular mortality, major adverse cardiovascular events, heart-failure admission, kidney composite outcome, HbA1c, body-weight change, severe hypoglycaemia, then remaining outcome labels alphabetically. Fix the original population/diabetes subgroup, original designated primary follow-up or otherwise its longest reported outcome-level analysis time. No trial-row inventory may supply an unreported outcome-level time. No alternate endpoint is substituted after failure.

Proposed early-check sequence: bibliographic/scope confirmation and outcome lock; published outcome-specific k and follow-up; licence/permitted source and input/dependence completeness; connected network and indirect target; method addition and profile/live question; novelty and final effort certification. Existing published evidence can establish a terminal failure at any earlier step. Profile metadata can be recorded early, but missing counters are not zero. This changes inspection order only.

Choose a never-directly-compared pair explicitly motivated in the original title/objectives; if multiple or none, take the alphabetically earliest unordered pair of original treatment-node labels among qualifying pairs. Confirm no direct edge from an explicit statement or labelled network, without effect calculation. Do not merge doses/nodes. Record target before its pooled estimate. If target status requires numerical extraction, it is unresolved and cannot pass. Lock outcome and k before elaborate target work so an ineligible network cannot be rescued by changing question.

## 5. All v1 gates retained: no gate loosened

**G1 - source, licence and complete inputs.** Require a printed open licence compatible with the intended research use, including relevant supplements; record exact identifier and locator (e.g. CC BY, CC BY-SA, CC0, CC BY-NC for the specified noncommercial use). OA metadata alone is insufficient. Restrictive/uncertain reuse terms remain unresolved, not implicitly cleared. Use the review's own article, printed forest/table or published supplement, including a permitted OA copy. An index-advertised repository can be the initial route. A required-source bot check means NOT FEASIBLE, reason "blocked"; no cycling mirrors.

For the fixed outcome require complete trial effects with labelled SE/CI, or complete arm means with SD/SE and analysed n, or events with analysed denominators, as appropriate. Require whole-trial/report, original treatment/control, shared-arm and follow-up mapping, all multi-arm contributions and adequate dependence information. A future source-backed complete-pair conversion must be possible. No invented covariance, imputation, incident-rate reconstruction, primary-trial hunting, pooled-output inversion, combining reviews, contact, login or paid access. On-request or nonpublic inputs cannot establish feasibility. Characteristics, league tables and treatment-level results are not trial inputs.

Record FEASIBLE (text) or FEASIBLE-IMAGE only when completeness is established without recording rows. Readable images remain allowed; image uncertainty carries into verification. Missing/unreadable/uncertain inputs cannot pass. Inspect source locations, headers, captions and qualitative completeness only; do not copy any study effects, counts, CIs, doses or moderators or assemble a trial inventory. Published pooled results, aggregate k and model statements may be recorded exactly as printed, after the question is locked.

**G2 - scope, outcome k, indirect target, connectedness and addition.** Retain all section 3 conditions; k counts independent trials in the fixed outcome, never arms, contrast rows, a broad review total or an invented inventory. If outcome k cannot be established from published summary material, fail. The common prospective operation remains omission of each whole trial (all arms/contrasts together), refitting the NMA to assess the fixed indirect target effect/CI dependence. Merely repeating an indirect estimate, changing software or treatment ordering does not qualify.

M=2: the original does not numerically report this indirect-only target and does not perform the target whole-trial omission operation. M=1: the target is reported, but published limitations/structure motivate a specific unreported whole-trial dependence question; full text and supplement establish the operation's absence. M=0 otherwise: fail. An equivalent operation already in the original fails. M>=1 is unchanged from v1, not a new relaxation of the basic-indirect-comparison wording.

**G3 - novelty.** Preserve the approved Europe PMC/OpenAlex substitution for Google Scholar: Scholar showed "unusual traffic" on 2026-10-28 and was not bypassed (Mahmood item 3). For a visited candidate, use its DOI in the following fixed GET templates; URL-encode substituted DOI/source/IDs. These are templates, not claims that a new candidate was queried:
~~~text
https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%22<URLENCODED_DOI>%22&format=json&resultType=lite&pageSize=1000&cursorMark=%2A
https://www.ebi.ac.uk/europepmc/webservices/rest/<SOURCE>/<ID>/citations?format=json&page=1&pageSize=1000
https://api.openalex.org/works/https://doi.org/<URLENCODED_DOI>
https://api.openalex.org/works?filter=cites%3A<OPENALEX_W_ID>&per-page=100&page=1
~~~
Resolve all Europe PMC source/ID records matching the DOI; paginate citation lists and deduplicate by DOI or index identity. OpenAlex uses the canonical W ID, per-page=100, page=1,2,... until an empty page, capped at 100 pages/10,000 works. Never use cursor paging or credentials. Do not terminate merely at a short nonempty page or the reported count. At exactly 10,000 with no empty page inside the cap, termination coverage remains incomplete; do not request page 101. Changed totals, duplicates, schema/access errors and mismatched terminal totals mean incomplete coverage. Retain requests, actual dates, bibliographies, reported/retrieved totals separately; never sum counters across databases or equate missing with zero.

Review every returned citing title/abstract, then plausible equivalents using permitted sources. An equivalent numerically reuses the same review's fixed outcome-specific network and target, omits every whole trial with all arms, and refits the remaining NMA for target effect/CI dependence. Different software/thresholds do not distinguish it. Updated/overlapping reviews, other outcomes, alternative models, bias-restricted subsets, sequential accumulation and nonnumerical commentary are not automatically equivalent; adjudicate published methods. For M=2 also check the original supplement and later exact-network work for the proposed contrast.

An established equivalent fails. Successful searches finding none mean "no equivalent identified", not proof of absence. Both indexes must return usable search/citation responses, including a verified zero if applicable; wholly failed index = UNRESOLVED. A successful lookup with no indexed record is a disclosed coverage limitation. Partial citation coverage alone does not block F2, unchanged from v1. An unresolved plausible exact equivalent prevents selection; a required adjudication source behind a bot check is blocked/NOT FEASIBLE. Coverage runs through the actual screen date; the discovery date window stays fixed.

The script's optional --openalex-cites W_ID helper remains citation retrieval only and shares the draft/release lock. It cannot decide equivalence or replace mandatory Europe PMC review. It writes a separate novelty_P04_openalex_<W_ID>.json and preserves partial results, returning nonzero when incomplete.

**G4 - powerful criteria.** Require P>=1 and L>=1, based on published features and verified external profile/context. P=3: assigned target journal; P=2: this exact review is substantively cited in a readable clinical guideline (not a snippet); P=1: timestamped OpenAlex cited_by_count >=100; P=0: none established. Take the highest applicable route. Missing counters are unknown; another verified route may qualify. The review citing a guideline is not the guideline citing the review.

L=2: original explicitly identifies unresolved controversy or a practice-changing claim for the fixed target; L=1: original documents ongoing trials or an explicitly unresolved comparative-treatment decision; L=0: no published support. Record the non-row passage/location and prospective question. Stable outcomes remain valid; never score a recalculated magnitude, direction, significance or ordering.

**G5 - effort and screen caps.** E<=4 analytical hours for one outcome from one review, including input preparation/checking, original reproduction, one focused whole-trial omission analysis, one figure and short letter. Estimate each component in 0.25-hour increments from source format/complexity. Independent extraction, adjudication and required human verification time are additional and retained in planning. A conditional estimate cannot clear an unresolved source gate. Missing E is unknown, not zero. No author contact or primary-report reconstruction can rescue over-cap effort.

Maximum screening time is 60 minutes per visited disposition, separately from E; unresolved mandatory gates at expiry are NOT CLEARED and consume the slot. Log coverage and times; do not extend a preferred candidate's cap.

**No gate was loosened:** same scope, OA/licence, complete readable inputs, supported dependence, 5-60 outcome-specific k, connected indirect-only target, M/L/P thresholds, equivalence definition/coverage rule, four-hour E, 60-minute screen cap, source restrictions, endpoint lock, ranking and five-disposition stop. Changes proposed are earlier application of those same requirements, conservative expansion of exclusions, explicit A/B frame choice and the new seed for B. No numerical candidate calculation, app upload, R fit, digitisation or extraction may inform any selection.

## 6. Selection, reporting and the renewed stop

Among complete passers only, rank lexicographically: higher M, then higher L, then higher P, then lower E, then earlier chosen seeded order, then canonical DOI for a hash tie. The second passer is fallback. No recalculated effect informs this ordering.

**If nothing passes, stop and report the v2 feasibility failure. No v3 will follow without a new explicit decision by Mahmood and a new prospective registration/release.** No switching to the unused A/B option, new seed, query, endpoint or sixth candidate is automatic. Exactly one passer means a provisional primary and "no cleared fallback"; no fictitious pair or automatic extension. Any later single-primary route requires an explicit decision and its own candidate-specific specification; this draft does not approve it.

The screen log must record every visited DOI, original/new frame order and hash, timestamps, locked outcome/population/follow-up/target, aggregate k and locator, licence, source locators/headers/completeness, all G1-G5 statuses/reasons, access blocks, exact novelty requests/coverage/equivalence, M/L/P/E evidence and component estimates, screen minutes and final disposition. Use PASS, FAIL, UNRESOLVED or NOT ASSESSED with reasons; unresolved mandatory gates cannot pass. Preserve metadata exclusions, original frame, untouched records and any deviations. Keep trial-level rows out.

## 7. Approval, release, executable handoff and later pipeline

This approved copy sets DRAFT=False and APPROVED_OPTION="A" in the script. It still does not authorize execution until the public P04-screen-v2 release exists: without the release arguments and matching frozen hashes the script stops before network access or runtime output creation. Offline query printing, generated SYNTHETIC fixtures and an offline metadata check of the archived frame (540 records retained from rank 22 after the 21 triaged exclusions; nothing screened) are the only checks run at finalization. No v2 candidate was screened, fetched, scored or selected; no real-data analysis or release occurred.

Mahmood approved a further screen on 2026-10-30 and chose A (decision quoted in the header). This approved successor of the draft bytes sets DRAFT=False and APPROVED_OPTION="A" and updates the document status; both files are frozen together at a new paper-specific public GitHub screening release, P04-screen-v2. The draft is retained as history. Record document/script SHA-256 and server-side release UTC time. Zenodo DOI is recorded when minted (PENDING allowed for the screening release, unchanged from v1). The v1 release cannot authorize v2. Approval alone is not a release.

Future pc2 command template, only for the approved released successor (Option A):
~~~text
python out/screen_P04_v2.py --screen-release-url https://github.com/mahmood726-cyber/usecase-preregistrations/releases/tag/P04-screen-v2 --screen-release-doi <ZENODO_DOI_URL_OR_PENDING> --prereg-sha256 <APPROVED_DOCUMENT_SHA256> --script-sha256 <APPROVED_SCRIPT_SHA256> --v1-frame <ARCHIVED_frame_P04.jsonl> --output-dir out/v2_run_01
~~~
The archived frame must hash to Appendix C's fef70cafb5a84c329c62b8b8122d2c634e5a43301455c1c5065a7bbe4053063f. The former option-B form (without --v1-frame) is withdrawn; B was not chosen. Local filename PREREG_P04_screen_v2_DRAFT.md is the script's expected document; this approved successor preserves it as a historical basename. The option cannot be changed by command-line choice. The script verifies local hashes/identifier syntax, not remote existence or release time; pc2 must verify the actual new release, archived bytes and server timestamp first. No credentials or login. A retrieval failure is reported, never rescued by another option; any allowed retry must use unchanged frozen rules and a fresh audit directory.

A selected pair then enters the same pipeline: candidate-specific **v4 F1-F6 freeze criteria**, REDTEAM2, resolve F1-F6 failures, use-case freeze and separate public GitHub/Zenodo release, then authorized extraction. Screening release alone never authorizes extraction.

F1: independently FEASIBLE/FEASIBLE-IMAGE inputs. F2: equivalence check with disclosed limitations. F3: exactly one original reproduction configuration fixed in advance, including documented defaults for unstated choices; no model search. F4: outcome, estimand, original/app/R settings, conversions, numeric agreement/printed-number tolerances, new/robust definitions and fallback triggers all fixed before extraction. F6: actual pinned app capability evidenced by file/function/hash; unsupported operations labelled R-only. Repeated whole-trial omission orchestration is external to individual app fits; arm-to-contrast conversion requires a source-supported contract. Prior static code review is not runtime validation.

F5 is copied from MAHMOOD_DECISIONS.md item 4:
> Human verification: humans check headline rows, a seeded 5% of the other rows (at least 1), and only the fields still disputed after a third-model adjudication plus a fourth AI re-check (agy, different family). If the sample error is over 2%: a full AI re-extraction plus a human re-check of the headline rows. Packets are about 30 minutes or less; at most one per person per week across all papers (COAUTHOR_LOAD.md); Mahmood is in the rota; a packet not returned in 7 days is reassigned.

As specified by [FREEZE_CRITERIA.md](../../S2_P04_SCREENPREREG/FREEZE_CRITERIA.md), synthetic code validation, synthetic app/R parity, browser dependency closure, kit synchronization and packet assignments are mandatory post-release/pre-analysis conditions, not additional screening-freeze blockers. Pc2 uses R 4.6.0/netmeta 3.7.0; no R ran here. No analysis of real data before synthetic validation passes. Reproduce the original within pre-frozen tolerances before new analysis; primary then independently cleared fallback then stop. Report stable results and failures. Preserve the 150-250-word, one-figure plan, no clinical recommendations, no priority/treatment-ranking claims, no altered original numbers and no allegation that any publication contains an error.

The decision is recorded above; remaining limitations are in BLOCKERS_P04_screen_v2.md. Execution remains outside the finalization job and waits for the public release.


## Appendix A. All 21 title-screened v1 DOIs excluded under both options

Together with the five pre-v1 DOIs in section 1, these are the complete 26-record exclusion set. No previous title, endpoint, access change or new database order revokes an exclusion.

| v1 rank | DOI | Historical status | A / B |
|---|---|---|---|
| 1 | 10.1007/s40123-026-01377-2 | Title exclusion | Exclude / Exclude |
| 2 | 10.1186/s13613-025-01471-x | Full-screen FAIL | Exclude / Exclude |
| 3 | 10.1186/s12962-020-00208-w | Title exclusion | Exclude / Exclude |
| 4 | 10.1038/s41598-024-63316-0 | Title exclusion | Exclude / Exclude |
| 5 | 10.3389/fendo.2026.1891173 | Full-screen FAIL | Exclude / Exclude |
| 6 | 10.1038/s41598-021-89620-7 | Full-screen FAIL | Exclude / Exclude |
| 7 | 10.1186/s13098-026-02226-9 | Full-screen FAIL | Exclude / Exclude |
| 8 | 10.3389/fpubh.2023.1201818 | Title exclusion | Exclude / Exclude |
| 9 | 10.1007/s40123-025-01247-3 | Full-screen FAIL | Exclude / Exclude |
| 10 | 10.3389/fpubh.2022.959073 | Title exclusion | Exclude / Exclude |
| 11 | 10.7759/cureus.100927 | Title-screened referral; never full-screened | Exclude / Exclude |
| 12 | 10.1186/s13643-022-01986-5 | Title exclusion | Exclude / Exclude |
| 13 | 10.1097/md.0000000000031823 | Title exclusion | Exclude / Exclude |
| 14 | 10.3389/fendo.2023.1282584 | Title-screened referral; never full-screened | Exclude / Exclude |
| 15 | 10.3389/fphar.2023.1226778 | Title exclusion | Exclude / Exclude |
| 16 | 10.1186/s12912-025-04065-x | Title exclusion | Exclude / Exclude |
| 17 | 10.3389/fphar.2021.751496 | Title-screened referral; never full-screened | Exclude / Exclude |
| 18 | 10.3389/fmed.2025.1721311 | Title-screened referral; never full-screened | Exclude / Exclude |
| 19 | 10.1111/jdi.13603 | Title-screened referral; never full-screened | Exclude / Exclude |
| 20 | 10.1007/s40122-025-00789-5 | Title-screened referral; never full-screened | Exclude / Exclude |
| 21 | 10.1007/s13300-023-01459-5 | Title-screened referral; never full-screened | Exclude / Exclude |

## Appendix B. Exhaustive DOI inventory of v1-frame records never full-screened

556 records, in original stored order. E = excluded under A and B because already title-screened (16 records); U = untouched (540 records), retained in old order under A and eligible for metadata inclusion under B only if independently returned by the complete fresh query. U does not mean clinically eligible. No new screening or scoring was performed to produce this list.

| v1 rank | DOI | Treatment code |
|---|---|---|
| 1 | 10.1007/s40123-026-01377-2 | E |
| 3 | 10.1186/s12962-020-00208-w | E |
| 4 | 10.1038/s41598-024-63316-0 | E |
| 8 | 10.3389/fpubh.2023.1201818 | E |
| 10 | 10.3389/fpubh.2022.959073 | E |
| 11 | 10.7759/cureus.100927 | E |
| 12 | 10.1186/s13643-022-01986-5 | E |
| 13 | 10.1097/md.0000000000031823 | E |
| 14 | 10.3389/fendo.2023.1282584 | E |
| 15 | 10.3389/fphar.2023.1226778 | E |
| 16 | 10.1186/s12912-025-04065-x | E |
| 17 | 10.3389/fphar.2021.751496 | E |
| 18 | 10.3389/fmed.2025.1721311 | E |
| 19 | 10.1111/jdi.13603 | E |
| 20 | 10.1007/s40122-025-00789-5 | E |
| 21 | 10.1007/s13300-023-01459-5 | E |
| 22 | 10.1007/s40123-026-01434-w | U |
| 23 | 10.3389/fendo.2022.895458 | U |
| 24 | 10.3389/fendo.2025.1462104 | U |
| 25 | 10.1097/md.0000000000028365 | U |
| 26 | 10.1111/dom.70742 | U |
| 27 | 10.1111/dom.70748 | U |
| 28 | 10.3389/fendo.2023.1134297 | U |
| 29 | 10.3389/fpubh.2026.1818686 | U |
| 30 | 10.3389/fendo.2026.1843370 | U |
| 31 | 10.1007/s41669-023-00465-4 | U |
| 32 | 10.1371/journal.pone.0297488 | U |
| 33 | 10.1097/sla.0000000000006398 | U |
| 34 | 10.1111/dom.14202 | U |
| 35 | 10.1371/journal.pone.0187537 | U |
| 36 | 10.1186/s40199-017-0189-6 | U |
| 37 | 10.1186/s13643-026-03153-6 | U |
| 38 | 10.1155/2020/6062478 | U |
| 39 | 10.1016/j.jacadv.2026.102633 | U |
| 40 | 10.3389/fphar.2025.1613610 | U |
| 41 | 10.1007/s13300-019-0630-6 | U |
| 42 | 10.1136/bmjopen-2019-034680 | U |
| 43 | 10.3389/fcvm.2022.929020 | U |
| 44 | 10.1186/s13098-023-01248-x | U |
| 45 | 10.1371/journal.pone.0306336 | U |
| 46 | 10.3803/enm.2020.912 | U |
| 47 | 10.1038/s41433-025-03641-4 | U |
| 48 | 10.1002/dmrr.3670 | U |
| 49 | 10.3389/fnut.2026.1853598 | U |
| 50 | 10.4239/wjd.v14.i3.313 | U |
| 51 | 10.1159/000543353 | U |
| 52 | 10.3389/fendo.2023.1096105 | U |
| 53 | 10.3310/skht8119 | U |
| 54 | 10.3389/fendo.2020.00553 | U |
| 55 | 10.3389/fphar.2022.998816 | U |
| 56 | 10.12659/aot.933588 | U |
| 57 | 10.1007/s40273-018-0612-y | U |
| 58 | 10.1016/j.tjpad.2025.100111 | U |
| 59 | 10.1186/s13098-024-01266-3 | U |
| 60 | 10.3389/fphar.2021.709501 | U |
| 61 | 10.1097/md.0000000000022755 | U |
| 62 | 10.3389/fendo.2024.1410883 | U |
| 63 | 10.2196/45178 | U |
| 64 | 10.3389/fendo.2022.897776 | U |
| 65 | 10.3389/fendo.2025.1614597 | U |
| 66 | 10.1016/j.jhepr.2025.101661 | U |
| 67 | 10.1007/s13300-018-0397-1 | U |
| 68 | 10.1016/j.eclinm.2025.103506 | U |
| 69 | 10.1186/s12903-019-0829-y | U |
| 70 | 10.3389/fendo.2026.1777151 | U |
| 71 | 10.1007/s13300-016-0217-4 | U |
| 72 | 10.1016/j.eclinm.2022.101463 | U |
| 73 | 10.3389/fphar.2021.759262 | U |
| 74 | 10.1007/s13300-018-0482-5 | U |
| 75 | 10.1097/md.0000000000007939 | U |
| 76 | 10.3390/medsci14010153 | U |
| 77 | 10.1136/bmj-2025-084159 | U |
| 78 | 10.1111/jdi.70293 | U |
| 79 | 10.1186/s13098-022-00929-3 | U |
| 80 | 10.1186/s40662-021-00261-3 | U |
| 81 | 10.3389/fendo.2026.1832624 | U |
| 82 | 10.3389/fendo.2022.923376 | U |
| 83 | 10.3390/ijms27062619 | U |
| 84 | 10.1080/0886022x.2024.2431141 | U |
| 85 | 10.3389/fendo.2019.00455 | U |
| 86 | 10.1007/s40123-026-01440-y | U |
| 87 | 10.1186/s40842-025-00248-2 | U |
| 88 | 10.1186/s13098-024-01492-9 | U |
| 89 | 10.3389/fendo.2023.1256548 | U |
| 90 | 10.1007/s40123-025-01098-y | U |
| 91 | 10.1136/bmjopen-2019-034481 | U |
| 92 | 10.21203/rs.3.rs-2674982/v1 | U |
| 93 | 10.1186/s12884-026-09920-6 | U |
| 94 | 10.1136/bmj.n1537 | U |
| 95 | 10.1136/bmj-2021-068882 | U |
| 96 | 10.1016/j.xkme.2024.100943 | U |
| 97 | 10.1007/s13300-021-01142-7 | U |
| 98 | 10.1136/bmjopen-2018-023458 | U |
| 99 | 10.1097/md.0000000000021568 | U |
| 100 | 10.1007/s00592-025-02534-y | U |
| 101 | 10.2337/dc22-2491 | U |
| 102 | 10.1186/s13098-022-00801-4 | U |
| 103 | 10.1097/md.0000000000014400 | U |
| 104 | 10.1136/bmj-2022-074068 | U |
| 105 | 10.1136/bmjopen-2022-066491 | U |
| 106 | 10.1007/s13300-021-01034-w | U |
| 107 | 10.4239/wjd.v14.i9.1422 | U |
| 108 | 10.1097/md.0000000000018198 | U |
| 109 | 10.1002/hsr2.73020 | U |
| 110 | 10.1016/j.eclinm.2026.104026 | U |
| 111 | 10.3390/jcm10122713 | U |
| 112 | 10.7759/cureus.114008 | U |
| 113 | 10.1186/s40001-024-01954-w | U |
| 114 | 10.3389/fphar.2022.825417 | U |
| 115 | 10.1186/s13098-024-01297-w | U |
| 116 | 10.1007/s13300-017-0312-1 | U |
| 117 | 10.1177/14791641221106866 | U |
| 118 | 10.7705/biomedica.4684 | U |
| 119 | 10.1002/sim.8383 | U |
| 120 | 10.7759/cureus.103029 | U |
| 121 | 10.3389/fphar.2023.1102792 | U |
| 122 | 10.1002/14651858.cd015952 | U |
| 123 | 10.3389/fphar.2026.1693378 | U |
| 124 | 10.1007/s10072-026-08929-1 | U |
| 125 | 10.1093/bjsopen/zrad077 | U |
| 126 | 10.1186/s40001-026-03986-w | U |
| 127 | 10.1016/j.metop.2025.100382 | U |
| 128 | 10.12998/wjcc.v8.i21.5235 | U |
| 129 | 10.1177/01410768251395877 | U |
| 130 | 10.3389/fendo.2023.1068254 | U |
| 131 | 10.3389/fphar.2025.1517272 | U |
| 132 | 10.1007/s12325-023-02675-y | U |
| 133 | 10.3389/fimmu.2020.00457 | U |
| 134 | 10.1186/s12893-026-03882-4 | U |
| 135 | 10.3389/fendo.2022.1078686 | U |
| 136 | 10.1186/s12933-026-03236-7 | U |
| 137 | 10.1097/md.0000000000029126 | U |
| 138 | 10.1186/s13561-023-00466-3 | U |
| 139 | 10.3389/fendo.2026.1772351 | U |
| 140 | 10.1007/s13300-021-01040-y | U |
| 141 | 10.3389/fpubh.2026.1880248 | U |
| 142 | 10.7759/cureus.96162 | U |
| 143 | 10.1136/bmjopen-2017-017644 | U |
| 144 | 10.1080/07853890.2024.2428432 | U |
| 145 | 10.1002/edm2.70222 | U |
| 146 | 10.3389/fimmu.2026.1825473 | U |
| 147 | 10.1038/s41598-025-09807-0 | U |
| 148 | 10.1016/j.heliyon.2024.e24533 | U |
| 149 | 10.1371/journal.pone.0282143 | U |
| 150 | 10.3390/jcm15093388 | U |
| 151 | 10.1007/s13300-018-0542-x | U |
| 152 | 10.3389/fendo.2021.649018 | U |
| 153 | 10.1001/jamanetworkopen.2022.44652 | U |
| 154 | 10.1136/bmjopen-2024-093342 | U |
| 155 | 10.1111/jcmm.13096 | U |
| 156 | 10.1136/bmjophth-2024-001702 | U |
| 157 | 10.1097/md.0000000000028946 | U |
| 158 | 10.1186/s12916-025-04018-w | U |
| 159 | 10.1371/journal.pone.0267854 | U |
| 160 | 10.1016/j.jscai.2024.101859 | U |
| 161 | 10.3389/fnut.2024.1325894 | U |
| 162 | 10.1001/jama.2024.27402 | U |
| 163 | 10.1136/bmjopen-2019-034741 | U |
| 164 | 10.3389/fphar.2026.1846714 | U |
| 165 | 10.1186/s12933-022-01474-z | U |
| 166 | 10.1002/14651858.cd016351 | U |
| 167 | 10.1007/s13300-019-0566-x | U |
| 168 | 10.1136/bmjopen-2016-015284 | U |
| 169 | 10.3389/fpubh.2023.1271706 | U |
| 170 | 10.3389/fendo.2023.1244432 | U |
| 171 | 10.3389/fendo.2025.1495131 | U |
| 172 | 10.3389/fcvm.2026.1799254 | U |
| 173 | 10.1186/s13643-018-0706-9 | U |
| 174 | 10.1007/s13300-019-00706-y | U |
| 175 | 10.1016/j.metop.2025.100414 | U |
| 176 | 10.1101/2024.06.23.24309242 | U |
| 177 | 10.3389/fendo.2026.1907358 | U |
| 178 | 10.1186/s13643-023-02349-4 | U |
| 179 | 10.1136/bmjopen-2018-023206 | U |
| 180 | 10.1097/md.0000000000020461 | U |
| 181 | 10.3389/fendo.2023.1216160 | U |
| 182 | 10.3389/fcvm.2023.1126110 | U |
| 183 | 10.1097/md.0000000000017353 | U |
| 184 | 10.1371/journal.pone.0168582 | U |
| 185 | 10.3390/ph18091337 | U |
| 186 | 10.1038/s41433-025-04015-6 | U |
| 187 | 10.3389/fneur.2026.1904967 | U |
| 188 | 10.1007/s13300-022-01336-7 | U |
| 189 | 10.7759/cureus.69711 | U |
| 190 | 10.3389/fendo.2025.1742128 | U |
| 191 | 10.1136/bmjopen-2020-048259 | U |
| 192 | 10.3389/fendo.2026.1947147 | U |
| 193 | 10.3389/fendo.2026.1941999 | U |
| 194 | 10.1186/s13195-024-01645-y | U |
| 195 | 10.3390/ph15080953 | U |
| 196 | 10.3389/fendo.2021.735824 | U |
| 197 | 10.1016/j.ijcrp.2025.200569 | U |
| 198 | 10.1016/j.jscai.2024.102432 | U |
| 199 | 10.1136/bmjopen-2019-030919 | U |
| 200 | 10.3389/fmed.2025.1653147 | U |
| 201 | 10.1002/sim.10253 | U |
| 202 | 10.1161/jaha.120.019184 | U |
| 203 | 10.1097/md.0000000000024967 | U |
| 204 | 10.1007/s12325-025-03288-3 | U |
| 205 | 10.1371/journal.pone.0177646 | U |
| 206 | 10.1016/j.bj.2026.100985 | U |
| 207 | 10.3390/nu11061373 | U |
| 208 | 10.1007/s13300-017-0321-0 | U |
| 209 | 10.3389/fphar.2022.876386 | U |
| 210 | 10.3389/fphar.2023.1028257 | U |
| 211 | 10.1038/s41366-025-01859-6 | U |
| 212 | 10.3389/fphar.2024.1360633 | U |
| 213 | 10.3389/fnut.2025.1653449 | U |
| 214 | 10.14336/ad.2019.0303 | U |
| 215 | 10.1002/edm2.70313 | U |
| 216 | 10.1136/bmjopen-2024-088687 | U |
| 217 | 10.1016/j.ebiom.2023.104856 | U |
| 218 | 10.1136/bmjopen-2021-058034 | U |
| 219 | 10.3390/ijerph19031622 | U |
| 220 | 10.3389/fcvm.2026.1785694 | U |
| 221 | 10.3389/fpubh.2025.1566101 | U |
| 222 | 10.7759/cureus.90335 | U |
| 223 | 10.3389/fendo.2024.1452192 | U |
| 224 | 10.1186/s12886-018-1006-9 | U |
| 225 | 10.1186/s12872-025-04745-1 | U |
| 226 | 10.5114/aoms/209000 | U |
| 227 | 10.1007/s40265-020-01290-3 | U |
| 228 | 10.3310/pcgv5709 | U |
| 229 | 10.1111/1753-0407.70044 | U |
| 230 | 10.3389/fendo.2024.1403606 | U |
| 231 | 10.3389/fphys.2026.1867073 | U |
| 232 | 10.1016/j.jacadv.2026.103298 | U |
| 233 | 10.1111/dme.14264 | U |
| 234 | 10.1371/journal.pone.0267025 | U |
| 235 | 10.1007/s13300-025-01728-5 | U |
| 236 | 10.18632/oncotarget.20282 | U |
| 237 | 10.3310/krwp1264 | U |
| 238 | 10.3389/fphar.2018.01393 | U |
| 239 | 10.2147/dmso.s502743 | U |
| 240 | 10.1155/2018/8620682 | U |
| 241 | 10.1186/s13098-023-01240-5 | U |
| 242 | 10.1155/2020/3987065 | U |
| 243 | 10.1186/s40001-025-02368-y | U |
| 244 | 10.3389/fendo.2020.00288 | U |
| 245 | 10.1002/edm2.70275 | U |
| 246 | 10.2147/dmso.s392952 | U |
| 247 | 10.1186/s13643-021-01864-6 | U |
| 248 | 10.3390/biomedicines12091943 | U |
| 249 | 10.1097/md.0000000000016038 | U |
| 250 | 10.3310/gjst1327 | U |
| 251 | 10.1002/oby.70100 | U |
| 252 | 10.3389/fendo.2023.1168755 | U |
| 253 | 10.1016/j.aed.2025.08.007 | U |
| 254 | 10.1097/md.0000000000029154 | U |
| 255 | 10.4097/kjae.2017.70.6.591 | U |
| 256 | 10.1186/s13048-026-02078-x | U |
| 257 | 10.1159/000552388 | U |
| 258 | 10.1007/s13300-017-0245-8 | U |
| 259 | 10.1007/s11695-025-08451-x | U |
| 260 | 10.3389/fendo.2026.1734108 | U |
| 261 | 10.3389/fendo.2026.1842847 | U |
| 262 | 10.1097/md.0000000000028086 | U |
| 263 | 10.1111/dom.16360 | U |
| 264 | 10.1016/j.eclinm.2024.103011 | U |
| 265 | 10.3389/fphar.2022.939488 | U |
| 266 | 10.4239/wjd.v12.i9.1576 | U |
| 267 | 10.3389/fphar.2026.1812118 | U |
| 268 | 10.1111/obr.13030 | U |
| 269 | 10.1007/s12325-026-03523-5 | U |
| 270 | 10.1136/bmjdrc-2023-003836 | U |
| 271 | 10.1002/dmrr.70202 | U |
| 272 | 10.1002/edm2.70248 | U |
| 273 | 10.3389/fendo.2025.1513641 | U |
| 274 | 10.3390/nu15143156 | U |
| 275 | 10.1186/s12933-020-01197-z | U |
| 276 | 10.1186/s12933-019-0853-x | U |
| 277 | 10.3947/ic.2020.0136 | U |
| 278 | 10.3389/fnut.2023.1184337 | U |
| 279 | 10.3390/healthcare14162593 | U |
| 280 | 10.1136/bmjmed-2026-003026 | U |
| 281 | 10.3389/fendo.2026.1780676 | U |
| 282 | 10.1186/s12902-025-02043-7 | U |
| 283 | 10.7717/peerj.19809 | U |
| 284 | 10.1007/s13300-018-0456-7 | U |
| 285 | 10.1097/md.0000000000029152 | U |
| 286 | 10.1007/s11695-021-05643-z | U |
| 287 | 10.7759/cureus.102204 | U |
| 288 | 10.1186/s12916-026-04705-2 | U |
| 289 | 10.1186/s12891-025-09022-y | U |
| 290 | 10.1111/dme.14180 | U |
| 291 | 10.3389/fendo.2026.1859725 | U |
| 292 | 10.3390/antiox11040621 | U |
| 293 | 10.1186/s12984-025-01614-y | U |
| 294 | 10.1186/s12874-025-02499-0 | U |
| 295 | 10.1007/s12272-025-01552-2 | U |
| 296 | 10.1080/0886022x.2023.2222847 | U |
| 297 | 10.5500/wjt.v11.i10.432 | U |
| 298 | 10.1155/jdr/1548984 | U |
| 299 | 10.3389/fcvm.2022.876795 | U |
| 300 | 10.1371/journal.pone.0217701 | U |
| 301 | 10.3389/fendo.2022.818537 | U |
| 302 | 10.3389/fphar.2023.1303694 | U |
| 303 | 10.1155/2019/8083417 | U |
| 304 | 10.3389/fphar.2022.1060956 | U |
| 305 | 10.1002/edm2.70285 | U |
| 306 | 10.3389/fendo.2026.1780580 | U |
| 307 | 10.2174/0115733998320667240805045742 | U |
| 308 | 10.3389/fendo.2024.1308959 | U |
| 309 | 10.1186/s13045-026-01788-5 | U |
| 310 | 10.1097/md.0000000000025788 | U |
| 311 | 10.1186/s12913-018-3274-8 | U |
| 312 | 10.1089/jicm.2021.0392 | U |
| 313 | 10.1007/s13300-023-01408-2 | U |
| 314 | 10.1097/md.0000000000025615 | U |
| 315 | 10.1136/bmjopen-2023-072960 | U |
| 316 | 10.3390/nu14235139 | U |
| 317 | 10.1016/j.conctc.2022.100944 | U |
| 318 | 10.2196/63209 | U |
| 319 | 10.2147/dmso.s539822 | U |
| 320 | 10.1155/2022/4251022 | U |
| 321 | 10.5662/wjm.v12.i3.164 | U |
| 322 | 10.1371/journal.pone.0263336 | U |
| 323 | 10.1001/jamanetworkopen.2022.2092 | U |
| 324 | 10.1186/s12933-018-0773-1 | U |
| 325 | 10.1136/bmjopen-2018-028430 | U |
| 326 | 10.3390/biom11040520 | U |
| 327 | 10.3389/fendo.2023.1170881 | U |
| 328 | 10.1007/s40120-025-00759-1 | U |
| 329 | 10.1007/s40520-025-03017-4 | U |
| 330 | 10.2147/dmso.s450994 | U |
| 331 | 10.3389/fendo.2026.1750615 | U |
| 332 | 10.1186/s12966-018-0703-3 | U |
| 333 | 10.3389/fphar.2022.986186 | U |
| 334 | 10.3389/fendo.2024.1333624 | U |
| 335 | 10.3390/jcm10163490 | U |
| 336 | 10.1002/ehf2.13822 | U |
| 337 | 10.1007/s12325-021-01637-6 | U |
| 338 | 10.3389/fendo.2025.1659740 | U |
| 339 | 10.1097/md.0000000000047994 | U |
| 340 | 10.1007/s12325-017-0484-0 | U |
| 341 | 10.1007/s41669-019-0171-y | U |
| 342 | 10.7759/cureus.44314 | U |
| 343 | 10.1080/13880209.2024.2422084 | U |
| 344 | 10.3310/hta21020 | U |
| 345 | 10.3389/fphar.2023.1145587 | U |
| 346 | 10.1186/s12916-025-04495-z | U |
| 347 | 10.1136/bmjopen-2023-074317 | U |
| 348 | 10.3389/fendo.2024.1286827 | U |
| 349 | 10.1038/s41591-025-03978-z | U |
| 350 | 10.1155/2022/5849995 | U |
| 351 | 10.1371/journal.pmed.1004553 | U |
| 352 | 10.1097/ms9.0000000000004669 | U |
| 353 | 10.3390/biomedicines12102328 | U |
| 354 | 10.1161/jaha.123.031805 | U |
| 355 | 10.1097/md.0000000000034122 | U |
| 356 | 10.3389/fimmu.2026.1615875 | U |
| 357 | 10.1136/bmjopen-2018-022271 | U |
| 358 | 10.15420/ecr.2020.15.1.po17 | U |
| 359 | 10.1002/osp4.70181 | U |
| 360 | 10.1016/j.metop.2023.100236 | U |
| 361 | 10.1136/bmjopen-2016-015557 | U |
| 362 | 10.1186/s12933-024-02301-3 | U |
| 363 | 10.3389/fendo.2026.1846553 | U |
| 364 | 10.1097/md.0000000000026431 | U |
| 365 | 10.1016/j.ijcrp.2026.200597 | U |
| 366 | 10.1007/s13300-016-0219-2 | U |
| 367 | 10.31083/rcm26154 | U |
| 368 | 10.1016/j.metop.2024.100284 | U |
| 369 | 10.2340/aos.v84.43344 | U |
| 370 | 10.3389/fendo.2026.1749651 | U |
| 371 | 10.1136/bmjopen-2023-075783 | U |
| 372 | 10.1177/20420188261437346 | U |
| 373 | 10.2196/47833 | U |
| 374 | 10.18502/ijph.v53i12.17302 | U |
| 375 | 10.1016/s0140-6736(21)01920-6 | U |
| 376 | 10.1136/bmjopen-2025-103539 | U |
| 377 | 10.1007/s10654-017-0352-x | U |
| 378 | 10.1016/s2213-8587(22)00172-3 | U |
| 379 | 10.3389/fphar.2022.957483 | U |
| 380 | 10.1016/j.eclinm.2025.103190 | U |
| 381 | 10.1007/s13300-018-0424-2 | U |
| 382 | 10.3389/fendo.2026.1888494 | U |
| 383 | 10.1136/bmjopen-2024-098205 | U |
| 384 | 10.3390/nu13072284 | U |
| 385 | 10.4239/wjd.v16.i10.110174 | U |
| 386 | 10.1007/s13300-023-01410-8 | U |
| 387 | 10.3310/kgfa8471 | U |
| 388 | 10.3390/healthcare12010027 | U |
| 389 | 10.21203/rs.3.rs-2305051/v1 | U |
| 390 | 10.1186/s12902-024-01805-z | U |
| 391 | 10.1016/j.advnut.2024.100330 | U |
| 392 | 10.1136/bmjopen-2022-065287 | U |
| 393 | 10.1155/jdr/1853763 | U |
| 394 | 10.1097/md.0000000000043796 | U |
| 395 | 10.1136/bmjdrc-2019-001150 | U |
| 396 | 10.3389/fendo.2026.1811595 | U |
| 397 | 10.1186/s40001-026-03933-9 | U |
| 398 | 10.1007/s13300-022-01359-0 | U |
| 399 | 10.1136/bmj.o109 | U |
| 400 | 10.1007/s13300-020-00975-y | U |
| 401 | 10.1097/md.0000000000024593 | U |
| 402 | 10.1007/s40123-026-01439-5 | U |
| 403 | 10.1186/s13102-026-01921-4 | U |
| 404 | 10.3389/fmed.2026.1852029 | U |
| 405 | 10.1097/md.0000000000028386 | U |
| 406 | 10.1007/s10741-020-09954-8 | U |
| 407 | 10.1186/s13643-023-02384-1 | U |
| 408 | 10.1097/md.0000000000024812 | U |
| 409 | 10.1111/iwj.14663 | U |
| 410 | 10.3389/fphar.2021.713007 | U |
| 411 | 10.1038/s41366-024-01467-w | U |
| 412 | 10.1186/s12933-022-01676-5 | U |
| 413 | 10.1186/s12916-025-04201-z | U |
| 414 | 10.3389/fimmu.2026.1798732 | U |
| 415 | 10.1007/s42000-023-00493-z | U |
| 416 | 10.7717/peerj.8575 | U |
| 417 | 10.1186/s12933-023-01993-3 | U |
| 418 | 10.1136/bmjopen-2022-061807 | U |
| 419 | 10.1097/md.0000000000028283 | U |
| 420 | 10.3389/fphar.2025.1543275 | U |
| 421 | 10.1007/s13300-026-01847-7 | U |
| 422 | 10.3389/fendo.2023.1098165 | U |
| 423 | 10.3389/fnins.2022.946879 | U |
| 424 | 10.3390/life16050843 | U |
| 425 | 10.1016/j.jdsr.2023.06.001 | U |
| 426 | 10.1007/s13300-020-00857-3 | U |
| 427 | 10.1111/jdi.13935 | U |
| 428 | 10.3389/fendo.2026.1902260 | U |
| 429 | 10.3389/fendo.2026.1902802 | U |
| 430 | 10.1186/s13643-026-03122-z | U |
| 431 | 10.3389/fendo.2025.1518871 | U |
| 432 | 10.7189/jogh.16.04187 | U |
| 433 | 10.7717/peerj.19571 | U |
| 434 | 10.3389/fimmu.2021.690082 | U |
| 435 | 10.2147/dmso.s116810 | U |
| 436 | 10.1186/s12933-026-03113-3 | U |
| 437 | 10.1038/s41598-017-16101-1 | U |
| 438 | 10.3390/ijms27020608 | U |
| 439 | 10.1016/j.eclinm.2022.101412 | U |
| 440 | 10.1186/s12916-023-03129-6 | U |
| 441 | 10.3390/nu14122383 | U |
| 442 | 10.3389/fendo.2026.1877008 | U |
| 443 | 10.1186/s12889-026-26256-0 | U |
| 444 | 10.1016/j.eclinm.2023.102181 | U |
| 445 | 10.3389/fendo.2025.1658739 | U |
| 446 | 10.1186/s13643-024-02558-5 | U |
| 447 | 10.3390/pharmaceutics15051361 | U |
| 448 | 10.1186/s12911-021-01470-5 | U |
| 449 | 10.1186/s12933-020-0987-x | U |
| 450 | 10.4239/wjd.v16.i7.106890 | U |
| 451 | 10.4330/wjc.v17.i7.107510 | U |
| 452 | 10.1002/pds.70087 | U |
| 453 | 10.1097/md.0000000000022564 | U |
| 454 | 10.1136/bmjopen-2025-113896 | U |
| 455 | 10.1055/a-2892-8092 | U |
| 456 | 10.1186/s13098-025-01841-2 | U |
| 457 | 10.3389/fendo.2024.1429261 | U |
| 458 | 10.1097/md.0000000000035290 | U |
| 459 | 10.1186/s12933-018-0722-z | U |
| 460 | 10.4103/picr.picr_218_23 | U |
| 461 | 10.1007/s13300-023-01466-6 | U |
| 462 | 10.3310/mjyp6578 | U |
| 463 | 10.1007/s40618-026-03006-y | U |
| 464 | 10.3390/nu11010048 | U |
| 465 | 10.1136/bmj.m4573 | U |
| 466 | 10.1136/bmjdrc-2019-000728 | U |
| 467 | 10.3389/fendo.2025.1512493 | U |
| 468 | 10.14740/cr2254 | U |
| 469 | 10.1111/1753-0407.13445 | U |
| 470 | 10.1186/s12933-019-0916-z | U |
| 471 | 10.1136/bmjdrc-2026-006026 | U |
| 472 | 10.1007/s12325-026-03553-z | U |
| 473 | 10.3310/hta24280 | U |
| 474 | 10.1111/dme.14831 | U |
| 475 | 10.1177/20420986251335214 | U |
| 476 | 10.15171/jcvtr.2019.43 | U |
| 477 | 10.3389/fendo.2023.1238399 | U |
| 478 | 10.1111/obr.70189 | U |
| 479 | 10.1097/md.0000000000023963 | U |
| 480 | 10.1186/s41043-025-00818-1 | U |
| 481 | 10.3389/fendo.2023.1144290 | U |
| 482 | 10.1111/dom.71046 | U |
| 483 | 10.3389/fendo.2024.1453067 | U |
| 484 | 10.1017/rsm.2026.10071 | U |
| 485 | 10.1371/journal.pone.0293183 | U |
| 486 | 10.3389/fendo.2025.1562815 | U |
| 487 | 10.3389/fendo.2025.1596924 | U |
| 488 | 10.3389/fphar.2018.00339 | U |
| 489 | 10.4239/wjd.v9.i11.180 | U |
| 490 | 10.1002/edm2.70187 | U |
| 491 | 10.1186/s12933-020-01070-z | U |
| 492 | 10.1007/s12325-020-01298-x | U |
| 493 | 10.4093/dmj.2024.0660 | U |
| 494 | 10.1371/journal.pone.0304283 | U |
| 495 | 10.3389/fphar.2021.637667 | U |
| 496 | 10.7759/cureus.102018 | U |
| 497 | 10.1186/s12872-023-03324-6 | U |
| 498 | 10.1186/s12902-026-02267-1 | U |
| 499 | 10.4239/wjd.v16.i11.111280 | U |
| 500 | 10.1186/s12882-025-04557-7 | U |
| 501 | 10.3390/jcm13061748 | U |
| 502 | 10.1097/ms9.0000000000003658 | U |
| 503 | 10.1038/s41598-018-22443-1 | U |
| 504 | 10.3389/fphar.2024.1472419 | U |
| 505 | 10.1007/s13300-018-0371-y | U |
| 506 | 10.1186/s12902-026-02193-2 | U |
| 507 | 10.1002/edm2.70247 | U |
| 508 | 10.1002/wjs.70406 | U |
| 509 | 10.1371/journal.pone.0329397 | U |
| 510 | 10.1136/bmjopen-2023-078100 | U |
| 511 | 10.1186/s12902-021-00846-y | U |
| 512 | 10.1136/bmj-2021-067731 | U |
| 513 | 10.3389/fendo.2022.1003263 | U |
| 514 | 10.1503/cmaj.250369 | U |
| 515 | 10.1186/s12889-025-24807-5 | U |
| 516 | 10.1136/bmj-2024-082071 | U |
| 517 | 10.1007/s12325-021-01979-1 | U |
| 518 | 10.15420/ecr.2026.03 | U |
| 519 | 10.1186/s13098-026-02162-8 | U |
| 520 | 10.3389/fmed.2025.1610141 | U |
| 521 | 10.4093/dmj.2022.0421 | U |
| 522 | 10.1016/j.ajmo.2025.100115 | U |
| 523 | 10.1186/s12903-019-0789-2 | U |
| 524 | 10.1002/cam4.71434 | U |
| 525 | 10.1186/s12882-026-04977-z | U |
| 526 | 10.1186/s12902-021-00865-9 | U |
| 527 | 10.1007/s13300-018-0428-y | U |
| 528 | 10.1136/bmjopen-2019-029073 | U |
| 529 | 10.1186/s12874-023-01925-5 | U |
| 530 | 10.3389/fendo.2022.802992 | U |
| 531 | 10.3389/fcvm.2021.791311 | U |
| 532 | 10.1136/bmjopen-2020-038970 | U |
| 533 | 10.1186/s13643-017-0455-1 | U |
| 534 | 10.1111/cob.70012 | U |
| 535 | 10.1371/journal.pone.0354259 | U |
| 536 | 10.3389/fphys.2021.700055 | U |
| 537 | 10.3389/fphar.2022.967317 | U |
| 538 | 10.1371/journal.pone.0202563 | U |
| 539 | 10.3389/fphar.2022.1096064 | U |
| 540 | 10.1111/dom.14702 | U |
| 541 | 10.3389/fnut.2025.1608634 | U |
| 542 | 10.1097/md.0000000000042431 | U |
| 543 | 10.1007/s13300-017-0250-y | U |
| 544 | 10.3389/fendo.2023.1182037 | U |
| 545 | 10.3389/fcvm.2022.1041200 | U |
| 546 | 10.1038/s41598-017-12987-z | U |
| 547 | 10.1111/1753-0407.13381 | U |
| 548 | 10.1016/j.cjco.2026.02.008 | U |
| 549 | 10.1038/s41598-020-75896-8 | U |
| 550 | 10.1101/2023.03.13.23287105 | U |
| 551 | 10.1159/000546855 | U |
| 552 | 10.4103/jfmpc.jfmpc_1319_21 | U |
| 553 | 10.1111/dom.70224 | U |
| 554 | 10.3389/fphar.2025.1626681 | U |
| 555 | 10.1111/1753-0407.13405 | U |
| 556 | 10.3389/fmed.2023.1016381 | U |
| 557 | 10.1186/s12986-025-00968-3 | U |
| 558 | 10.1111/dom.71128 | U |
| 559 | 10.1007/s12325-024-02831-y | U |
| 560 | 10.1097/md.0000000000035050 | U |
| 561 | 10.3389/fphar.2024.1462965 | U |

## Appendix C. Local provenance fingerprints

Fingerprints document source bytes, not new release evidence. All reads used Python. No candidate article or supplement was read in this drafting job.

| Source | SHA-256 |
|---|---|
| P04_screen/PREREG_P04_screen.md | 7681079c5ad884f301f1403a60d68109477978754c44dbac3b6df2e27c02c3a9 |
| P04_screen/screen_P04.py | 38edd6e943daf2f5bc7dfb1eb12ccf719bfdd34e3056baa5e344c1a146e846d7 |
| P04_screen/FREEZE.json | 6042fb367a98d5340fc3de35ddc31c1fec1f784d1eb2a99c8b822fd11e409486 |
| C1_P04_FULLSCREEN/out/FULLSCREEN_P04.jsonl | b00b442d9e1f5490f05f2b11f85a16351be99f7a17cdf573eee80c42e8809d6b |
| C1_P04_FULLSCREEN/out/SCREEN_NOTES_P04.md | 9c44be0d86afbb68f982ae9891a6edd098bd172a431107fefda08a4ce194e134 |
| worker archive ucjobs/T_P04_TRIAGE/frame_P04.jsonl | fef70cafb5a84c329c62b8b8122d2c634e5a43301455c1c5065a7bbe4053063f |
| worker archive ucjobs/T_P04_TRIAGE/out/TRIAGE_P04.jsonl | 6741b0afd2a02a42b4fce44d47e791131bdfc4c24bdc9d6f7cd9f7d93d197e15 |
| worker archive ucjobs/T_P04_TRIAGE/out/TO_FULL_TEXT_P04.json | 7c85a5f8d26a43d48391141a15134c0d879bec4d08dc3a3bebd9dc97ae9cedc8 |
| worker archive ucjobs/T_P04_TRIAGE/out/TRIAGE_P04_AUDIT.json | 0fa37490f98abcde5d951fc8b4a6db1a1fdc1d252adaf3894b8d0bab1f83d971 |

## Appendix D. Exact Europe PMC first-page URL

Applicable only to Option B, which was not chosen; Option A reuses the archive. Remaining pages change cursorMark only.

~~~text
epmc-01
https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28TITLE_ABS%3A%22network%20meta-analysis%22%20OR%20TITLE_ABS%3A%22network%20meta-analyses%22%20OR%20TITLE_ABS%3A%22network%20meta%20analysis%22%20OR%20TITLE_ABS%3A%22network%20metaanalysis%22%20OR%20TITLE_ABS%3A%22mixed%20treatment%20comparison%22%20OR%20TITLE_ABS%3A%22mixed-treatment%20comparison%22%29%20AND%20%28TITLE_ABS%3Adiabet%2A%20OR%20TITLE_ABS%3Aantidiabet%2A%20OR%20TITLE_ABS%3Aantihyperglyc%2A%29%20AND%20FIRST_PDATE%3A%5B2016-10-28%20TO%202026-10-28%5D%20AND%20OPEN_ACCESS%3AY&format=json&resultType=lite&pageSize=1000&cursorMark=%2A
~~~
