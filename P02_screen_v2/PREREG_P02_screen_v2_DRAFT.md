# P02 screening v2 (P02-screen-v2): Option A approved

**Approved for freeze and release; not yet released.** Drafted 2026-10-30; finalized 2026-10-30 after Mahmood's decision, relayed in chat on 2026-10-30: "P02 and P04: Option A v2 approved. Proceed." That decision authorizes exactly one further five-disposition batch under **Option A** (section 2.3). **Option B was NOT CHOSEN**; it is retained below only as a record of the alternative that was considered, and it can never be executed under this registration. Nothing may be retrieved, screened, scored, selected, extracted or analysed before the public **P02-screen-v2** GitHub release exists (section 8.1). The authorized v1 use case remains ended as a pre-registered feasibility failure; v2 is a separately authorized batch, not a continuation of the v1 authorization. The file keeps its historical basename, `PREREG_P02_screen_v2_DRAFT.md`, because section 8.1 step 3 requires the filenames to be retained so the receipt checks the correct local protocol.

Paper P02; target journal *Observational Studies*; field: human observational epidemiology and nutrition dose-response meta-analysis, including behavioural and occupational exposures. The proposed use case is a dose-unit plausibility audit. No candidate data or anticipated numerical finding may inform selection.

## 1. Why this draft exists, and what v1 established

**V2 exists only because v1 found no feasible candidate.** The released **P02-screen-v1** completed five full-screen dispositions: **5 FAIL, 0 passes, no selected primary and no fallback**. Its "if nothing passes, stop and report" rule applied and ended that use case. This draft does not reopen v1, reinterpret its result or treat the remaining records as permission to keep searching.

Evidence: [v1 frozen protocol, sections 3-6](../P02_screen/PREREG_P02_screen.md), [freeze record](../P02_screen/FREEZE.json), [full-screen ledger](../C1_P02_FULLSCREEN/out/FULLSCREEN_P02.jsonl), [screen notes](../C1_P02_FULLSCREEN/out/SCREEN_NOTES_P02.md) and [validation/remainder record](../C1_P02_FULLSCREEN/out/VALIDATION_P02.json). The retained draft wording inside v1 is historical: JOB.md and the C1 notes identify it as released. The freeze records 2026-10-28T21:54:04+00:00; this is the freeze timestamp, not a newly verified public release timestamp. The protocol and script hashes match the supplied freeze record. No remote release verification was attempted.

| V1 full-screen order / frame rank | DOI | Recorded failure and evidence locator in the supplied C1 record |
|---|---|---|
| 1 / 2 | 10.1016/j.eclinm.2023.102308 | G1: RCT-only review, not observational epidemiology. P02_01/fulltext.xml, Methods sec2.1/p0060. |
| 2 / 3 | 10.7717/peerj.20570 | G1: randomized trials of mind-body exercise. P02_02/fulltext.xml, Methods sec10/p[1]. |
| 3 / 5 | 10.1038/s41598-019-38723-3 | G1: controlled intervention trials and within-group pre/post analysis. P02_03/fulltext.xml, Methods Sec3/Par10, Results Sec7/Par16, Sec5/Par13. |
| 4 / 6 | 10.1093/ajcn/nqz178 | G1: the fixed primary target is highest-versus-lowest pooling, not the required dose-response synthesis. P02_04/fulltext.xml, sec2-1-1/p[1], sec2-4/p[3], sec3-1-1/p[2]. This was not a finding of inseparable trial/cohort mixing. |
| 5 / 7 | 10.1038/s41598-020-76306-9 | G2/F1: missing complete category cases and denominators, including reference categories; independent G4 failure because a nonlinear spline analysis was already reported. P02_05/fulltext.xml, Tab1, Fig3A/B, Methods Sec10/Par22-23 and the Word supplement. Assigned-dose completeness and supplement licensing also remained unresolved. |

These are reported screening dispositions, not fresh source checks, computed reproduction failures or allegations about publications. G3 was not run for the failed C1 candidates; an empty novelty-request list is not evidence of novelty clearance.

Earlier approved Liang and Li also failed the complete-published-input/eligible-vehicle requirements. Their readable per-increment or categorical forests and study totals did not supply complete matching category inputs; the Li workload estimate also exceeded the four-hour cap. Evidence: [historical candidates](../../S_P02_SCREENPREREG/CANDIDATES_P02.md), [v3 SOURCE_CHECK, disposition/input maps](../../S_P02_SCREENPREREG/B_P02_V3/out/SOURCE_CHECK_P02.md), [v3 BLOCKERS B1-B3](../../S_P02_SCREENPREREG/B_P02_V3/out/BLOCKERS_P02.md). No separate v4 SOURCE_CHECK package is supplied; [FREEZE_CRITERIA](../../S_P02_SCREENPREREG/FREEZE_CRITERIA.md) supplies the later F1-F6 requirements. No historical gate is waived.

[Mahmood decision 8](../MAHMOOD_DECISIONS.md) authorized v1, not unlimited batches. Decision 12 concerns P04. Neither authorizes v2. The new explicit Mahmood decision of 2026-10-30 ("P02 and P04: Option A v2 approved. Proceed.") chooses Option A below; a separate screening freeze/release is still required before it is activated.

## 2. Exclusions, the uncompleted v1 records, and the decision options

### 2.1 Permanent terminal-screen exclusions under both options

Exclude all five pre-v1 screened candidates, all five v1 full-screen failures, and all four identified v1 title/metadata rejections. A newly accessible copy cannot rescue a permanently excluded DOI.

| Prior stage | Excluded DOI |
|---|---|
| Pre-v1: Liang | 10.1186/s13643-025-02800-8 |
| Pre-v1: Li | 10.1016/j.envint.2020.105739 |
| Pre-v1: Hackshaw | 10.1136/bmj.j5855 |
| Pre-v1: Descatha | 10.1016/j.envint.2020.105746 |
| Pre-v1: Suksatan | 10.3390/nu14010174 |
| V1 full screen 1 | 10.1016/j.eclinm.2023.102308 |
| V1 full screen 2 | 10.7717/peerj.20570 |
| V1 full screen 3 | 10.1038/s41598-019-38723-3 |
| V1 full screen 4 | 10.1093/ajcn/nqz178 |
| V1 full screen 5 | 10.1038/s41598-020-76306-9 |
| V1 terminal title triage, rank 1: modelling study | 10.1136/bmjopen-2026-117508 |
| V1 terminal title triage, rank 4: protocol | 10.1136/bmjopen-2018-026232 |
| V1 terminal title triage, rank 11: trial-only review | 10.7762/cnr.2024.13.3.186 |
| V1 terminal title triage, rank 15: umbrella review | 10.1007/s40279-023-01966-2 |

The four terminal triage entries are preserved in [C1 codex_stdout.log](../C1_P02_FULLSCREEN/codex_stdout.log), lines 1099, 1102, 1109 and 1113, under the printed TRIAGE_P02.jsonl block (lines 1098-1114). They were never full-screened, but remain excluded under both options. This draft does not recalculate or change the reported v1 five-full-screen denominator.

### 2.2 Seven records deferred before full screening

These seven were marked TO_FULL_TEXT at v1 title triage but were **never full-screened**. Their prior triage does not establish eligibility, feasibility, novelty or power. Their titles have already been seen historically; this is not a claim of an unseen candidate frame. The supplied C1 remainder lists them in the following order:

| Original v1 frame rank | DOI | Option A (CHOSEN) | Option B (NOT CHOSEN) |
|---|---|---|---|
| 8 | 10.1186/s12889-018-5041-5 | Continuation position 1 | Excluded from fresh frame; NOT SCREENED, not FAIL |
| 9 | 10.1186/s12884-020-03036-1 | Continuation position 2 | Excluded from fresh frame; NOT SCREENED, not FAIL |
| 10 | 10.3389/fphys.2022.955702 | Continuation position 3 | Excluded from fresh frame; NOT SCREENED, not FAIL |
| 12 | 10.1002/fsn3.72357 | Continuation position 4 | Excluded from fresh frame; NOT SCREENED, not FAIL |
| 13 | 10.1016/j.eclinm.2026.103847 | Continuation position 5 | Excluded from fresh frame; NOT SCREENED, not FAIL |
| 14 | 10.1186/s40795-025-01152-9 | Continuation position 6, outside this batch | Excluded from fresh frame; NOT SCREENED, not FAIL |
| 16 | 10.1161/jaha.124.038714 | Continuation position 7, outside this batch | Excluded from fresh frame; NOT SCREENED, not FAIL |

Together with the four terminal triage exclusions, these are all eleven identified v1-frame records that never received a full screen. The original complete frame and standalone TRIAGE/TO_FULL_TEXT files are absent from this job. Sixteen frame identities/ranks can be recovered from the retained log, but **that log is not certified as the complete original discovery frame**. The original frame, its complete-run manifest/hash and triage inventory must be reconciled before either option is released. The script refuses a different inventory instead of guessing missing dispositions or adding unseen remainder records.

### 2.3 Two mutually exclusive choices; Mahmood chose A on 2026-10-30

**A - Continue the v1 frame's seeded order (CHOSEN).** Reuse the original complete archived frame, its metadata and ordering hashes. Remove all terminal-screen exclusions; take the seven deferred records in their original order. No new discovery retrieval and no reshuffle. A maximum of the first five receive dispositions; the final two stay NOT SCREENED even if the first five all fail. V1 seed **2026102802** remains the ordering seed for this option, because changing it would not be a continuation. This is a newly authorized v2 batch, not an extension permitted by the ended v1 run.

**B - Fresh frame with a new seed (NOT CHOSEN; record of the rejected alternative only).** Rerun the unchanged Europe PMC discovery query in section 3, retrieve every page, apply the fixed metadata rules, and exclude the five pre-v1 candidates plus **every record of the reconciled v1 frame**, including all seven deferred records above. Thus no already triaged v1-frame record enters B. The known exclusion union is 21 DOIs; an inventory mismatch blocks execution and requires reconciliation before release. Deferred records stay NOT SCREENED rather than receiving an invented failure. There is no later crossover to A within this authorization.

**New seed stated now: 2026103002**, different from v1's 2026102802. B uses ascending SHA-256 of UTF-8 `2026103002|P02|screen|<normalized-doi>`, then normalized DOI ascending for a hash tie. No alternative seed was tried. A deliberately retains the old hash order; the new seed would have applied only to B, which was not chosen, so it orders nothing in this registration. It is kept as the receipt's `new_seed` field only. Do not apply the new seed to A.

**Decision: A** (Mahmood, 2026-10-30), the option this draft recommended. It uses the existing precommitted order and avoids creating a replacement sample after observing failure. This is a procedural reason, not a judgment that any remaining publication will pass; no option promises a feasible vehicle. The decision was made before any v2 discovery, source inspection, or comparison of A/B yield. B cannot be run later as a backup within this authorization.

## 3. Fixed sampling frame, queries and five-disposition ceiling

Publication dates remain **2016-10-28 through 2026-10-28 inclusive**; no rolling extension. Require open access, a valid DOI, the P02 field, a real observational aggregate dose-response synthesis, **5 <= k <= 60 independent studies/cohorts in its designated synthesis**, and the complete printed category inputs specified below. Do not use the review-wide count as dose-response k.

Retain v1 amendment A1: **Europe PMC only for discovery; OpenAlex only for per-candidate novelty/profile evidence**. This carries forward the released instrument repair rather than reinstating the generic job-type's superseded OpenAlex discovery requirement. Both services' executable request templates are specified here and in section 6. No OpenAlex free-text discovery, API key, login or alternative database is introduced.

Under the chosen Option A, no discovery request is made in v2: EPMC-1 below documents the original v1 frame definition, and the retrieval rules in this section describe how that frame was built (and how the not-chosen B would have been built).

Europe PMC EPMC-1 (unchanged):
```text
(TITLE_ABS:"dose-response" OR TITLE_ABS:"dose response") AND (TITLE_ABS:"meta-analysis" OR TITLE_ABS:"meta analysis") AND FIRST_PDATE:[2016-10-28 TO 2026-10-28] AND OPEN_ACCESS:Y
```

Copy-pasteable initial request:
```text
https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28TITLE_ABS%3A%22dose-response%22+OR+TITLE_ABS%3A%22dose+response%22%29+AND+%28TITLE_ABS%3A%22meta-analysis%22+OR+TITLE_ABS%3A%22meta+analysis%22%29+AND+FIRST_PDATE%3A%5B2016-10-28+TO+2026-10-28%5D+AND+OPEN_ACCESS%3AY&format=json&resultType=lite&pageSize=1000&cursorMark=%2A
```

For B, follow all cursorMark pages to stable hitCount matched by unique source/id records; no relevance-ranked truncation or title/abstract keyword exclusions. Missing/repeated cursors, duplicate records, count drift, malformed responses or partial retrieval fail the run. True zero means a complete valid hitCount=0 response with an empty list. For A, this query documents the original frame definition; do not rerun it to replace the archived snapshot.

Normalize DOI by stripping surrounding whitespace and a DOI URL or doi: prefix, percent-decoding once and lowercasing; retain suffix punctuation. Require `10.<4-9 digits>/<non-whitespace suffix>`. Deduplicate solely by normalized DOI, retain all bibliographic provenance/conflicts, and log invalid/missing DOI exclusions. For fresh records use the earliest exact valid YYYY-MM-DD date among duplicates; never impute month/day. Exclude missing exact dates, dates outside the window, explicit retraction metadata or no OA-positive record. Unknown retraction status is not clearance. All other eligibility decisions occur in the ordered candidate screen. A retains archived metadata exclusions; any newly discovered unresolved date/licence/eligibility conflict fails the candidate within its counted slot.

A different DOI version is not silently removed as the same review: a duplicate-review determination during screening consumes a slot. No convenience additions or hand-picked source replacements.

HTTP policy remains v1's: 60-second request timeout; one-second pacing between pages; at most five identical-URL attempts for HTTP 5xx with 1, 2, 4, 8-second backoff. Never retry explicit bot checks, 401/403, other non-5xx failures, schema/non-JSON failures or transport failures. Record request URL, UTC times, response hash/status and attempted delays. No partial frame may be used. A failed run is FAILED_BLOCKED, with no frame_count interpreted as zero. Preserve the failure manifest/log. A technical retry of the identical query in a fresh output directory is allowed only before any candidate screen, after a transient failure, and never for a bot check. Freeze the first complete frame; do not resample a successful frame.

Lock the complete frame/hash before any candidate source inspection or novelty review. **Screen in its fixed order until five completed dispositions or frame exhaustion; do not stop early for a promising pass.** An early wrong-field/design/target/input/method/licence/effort failure, duplicate review or bot block consumes one of the five. Give it a complete checklist, marking unperformed later gates NOT ASSESSED - TERMINAL FAILURE. Do not add a second uncounted title/abstract filter or replace a failed candidate with number six. Pure pre-frame metadata exclusions above do not consume slots. If fewer than five records exist, screen all and report the exact denominator, including a genuine empty frame.

## 4. Earlier failure checks; no gate loosened

**No v1 eligibility, source, novelty, powerful, effort, ranking, honesty or stop gate is loosened.** The design change is the prospective order of evidence checks, plus the explicitly chosen frame/exclusions. The full inherited gates follow in sections 5-7. No positive retrieval keyword is treated as evidence of eligibility.

| Evidence checked at the start of each counted screening turn | V1 failure it screens out before expensive later work |
|---|---|
| Fix the original target, then inspect published design/eligibility methods and target-specific k | G1 intervention/RCT-only failures in full screens 1-3. Trials are not relabelled observational. A genuinely separate observational synthesis still must satisfy the unchanged target rule. |
| Verify that the fixed target is an actual aggregate dose-response synthesis | G1 failure in full screen 4. A highest-versus-lowest target is not replaced by a secondary dose-response result or given another synthesis's k. |
| Read original model statements for the fixed exposure/target before detailed input mapping or novelty searching | G4 independent failure in full screen 5. A linear panel alongside an already reported nonlinear spline for that target is not a linear-only original analysis, even if a nonlinear test is non-significant. |
| Check the permitted-source inventory, licence, headers and required-field completeness immediately after design/method fit | G2/F1 failure in full screen 5 and the earlier Liang/Li failures: study totals, pooled curves or per-increment effects cannot substitute for category-level inputs. Missing reference counts, source-supported dose assignments or reusable supplements are not reconstructed. |
| Apply the unchanged effort/source restrictions as soon as a prohibited or over-cap route is evident | No reconstruction, contact, bypass or enlarged effort budget to rescue input failures. |

Operational sequence: timer/target -> G1 -> the G4 linear-only and threshold/audit-fit component -> G2 complete-input/access/licence map -> remaining G4 profile/live-question evidence and G5 estimate -> G3 novelty -> confirm all G1-G5 and rank only passes. Early checks can fail immediately; a preliminary positive never clears unexamined requirements. Novelty remains inside the same 60-minute cap. Later unassessed fields do not become passes. No claim is made that these checks make a candidate more likely to pass.


## 5. Fixed outcome and gates for each candidate

Before judging numerical summaries, record exactly one synthesis from the published report: the first author-designated primary outcome/exposure/comparison in Methods (Methods order resolves co-primary outcomes); if none is designated, the first overall dose-response synthesis encountered in main-text reading order, then the first panel in printed order. Use its author-designated primary population and follow-up. If multiple analyses remain indistinguishable, fail as AMBIGUOUS TARGET. Do not search secondary outcomes for an eligible k, more complete data or a larger effect.

Complete these gates using published features only. A PASS requires evidence and exact locators; unverified required information is not a pass.

**G1 - field, date, design and k.** Human observational epidemiology/nutrition, a real published aggregate dose-response meta-analysis, within the date window. Exclude protocols, primary studies, umbrella summaries without their own qualifying input set, retracted reports, and inseparable trial/observational mixtures. Require **5 <= k <= 60 independent studies/cohorts in the designated dose-response synthesis**, as supported by published aggregate k and methods. Review-wide counts, counts of reports, or highest-versus-lowest k cannot substitute. Unresolved independence or synthesis correspondence fails. Record pooled k exactly as printed; never enumerate/transcribe study rows to manufacture k.

**G2 - licence, source access and readable complete inputs (F1).** Verify the licence on the article and each needed supplement. Require CC BY, CC0, or another explicit open licence permitting the planned factual-data reuse; record licence terms and source locator. NC/ND labels do not automatically authorize adapted figures/tables. Do not redistribute or adapt restricted source content; an unresolved reuse condition fails. Recreate later analysis figures only from permitted inputs.

Use only the review's own main-text table, numbered figure/forest or published supplement via the publisher, Europe PMC/PMC or an openly licensed repository copy of that review. Require printed category-level doses or bounds plus a fully specified original assignment rule, physical units/denominator, reference category, adjusted relative effects with CIs, **cases and total persons or person-time in every required category, including reference counts**, and unambiguous mapping to the designated synthesis. Record locations/column headers, text versus image readability, and required-field availability only. A clear image is FEASIBLE-IMAGE, not a reason to invent precision. Curve coordinates, per-increment forests and study totals do not replace category inputs. No OCR/digitization dataset, primary-study reconstruction, count imputation, author data or post hoc subset.

The complete printed sources must support the same physical exposure quantity and reference system and a source-supported unit map; dimensional comparability cannot be assumed. No per-study value is copied, paraphrased, calculated or tested in screening. Mere differing unit labels are not evidence of a discrepancy.

A required candidate source that encounters a bot check is recorded **blocked; NOT FEASIBLE**, consumes a screen and is not bypassed, retried via an alternate route, or rescued by author contact. A normal alternative open repository may be used to locate an initially unavailable/publisher-paywalled source before any bot block, without login or payment. Never bypass a check.

**G3 - novelty (F2).** Use the definition and procedure in section 6. An equivalent audit excludes the candidate. An unresolved potentially equivalent record fails clearance. Report coverage limitations honestly; incomplete citation counts are not invented negatives.

**G4 - all three powerful criteria.** [FIELD_USE_CASE_PROTOCOL.md](../../S_P02_SCREENPREREG/FIELD_USE_CASE_PROTOCOL.md) remains binding. Apply the following operational rules, fixed before screening:

- High profile: published in *Observational Studies*; OR the exact review is substantively cited in a named published clinical/public-health guideline; OR widely cited, operationalized here as OpenAlex cited_by_count >= 100 **and** substantive discussion of this review in a separate published guideline, consensus statement or evidence review. A passing citation count alone is insufficient. Record the count/date and citation locator; institutional branding alone is insufficient.
- Live question: the original Introduction/Discussion documents a controversy, a practice-changing claim or ongoing trials, with its reference/locator. Do not manufacture relevance from a computed effect.
- Method-question fit: preserve the protocol's published **linear-only dose-response analysis of an exposure where a threshold is plausible**, evidenced by the original rationale or a cited published rationale. In audit mode, also require explicit unit/assignment/standardization documentation permitting a dose-unit plausibility audit with the printed complete inputs. The contribution is testing robustness to unit handling, with no assumed flag or curve change. A spline-only re-analysis is not this audit. No suspected numeric anomaly may raise a candidate's score.

**G5 - effort.** At most **four hours of subsequent Codex work** for the single designated synthesis, covering extraction/checking, reproduction, app/R comparison, figure and short write-up, assuming the common app workflow is ready. Independent extractor and human packet time are additional and disclosed, never silently included as free Codex labour. Before selection, estimate those five components in quarter-hour increments from published format, source count and required workflow, without transcribing values. If any defensible upper bound exceeds four hours, or the work needs reconstruction/contact, fail. Also cap this full screening session at **60 elapsed working minutes per candidate**, including novelty checking; unresolved gates at the cap fail. Pause the timer only for a documented external interruption, not difficult searching.

## 6. Prospective novelty procedure and equivalence

Authorized deviation: Europe PMC and OpenAlex replace Google Scholar, which displayed an "unusual traffic" bot check on 2026-10-28; it was not bypassed ([decision 3](../MAHMOOD_DECISIONS.md)). Do not revisit Scholar.

**Same equivalence definition as [v3 section 9](../../S_P02_SCREENPREREG/B_P02_V3/out/PREREG_P02_usecase.md):** an equivalent prior re-analysis uses the same underlying synthesis, fixed outcome/comparison and substantially the same dose-unit plausibility or source-supported dose harmonisation audit with consequent re-analysis. Different software or terminology does not establish a difference. A different topic synthesis, ordinary exposure association or spline analysis alone is not equivalent. An already reported equivalent audit in the original also leaves no unreported audit contribution.

After release, for each screened DOI:

1. Resolve Europe PMC identity with the REST search parameter `query=DOI:"<doi>"`, `format=json`, `resultType=lite`. Confirm title/DOI, then request `https://www.ebi.ac.uk/europepmc/webservices/rest/<source>/<id>/citations?format=json&page=1&pageSize=1000`; follow all pages to the reported total or a logged failure. If multiple source IDs map to the same DOI, use all, deduplicating citing records by DOI, otherwise source/id.
2. Resolve OpenAlex with `https://api.openalex.org/works/https://doi.org/<doi>`. Confirm the returned DOI/title and W identifier; retain cited_by_count for the unchanged profile criterion. Request `https://api.openalex.org/works?filter=cites:<W_ID>&per-page=100&page=1`, then page=2, page=3 and so on **until an empty results page**, with **at most 10,000 records (100 pages)**. No cursor, free-text search, discovery-date or OA filter is used. A short nonempty page or reaching the advertised count alone does not establish completion. Completion requires an empty page and matching stable count with no repeated records. Above 10,000, retain the retrieved prefix and record **INCOMPLETE_LIMIT** with reported/retrieved counts and the ceiling; no claim of complete coverage. If page 100 is nonempty, including at exactly 10,000 reported records, the terminal empty page is unverified: also disclose INCOMPLETE_LIMIT rather than requesting page 101 beyond the paging ceiling. HTTP/access/schema/count/duplicate failures retain partial evidence with **FAILED_BLOCKED**, not zero citations. Both types of incomplete check are coverage limitations under the unchanged F2 rule below; they do not add records to the discovery frame. Non-OA citations may identify prior work, although no paywall may be bypassed.
3. Supplement these citation lists with Europe PMC search using each of the following two exact templates, with ordinary URL encoding. TITLE is the full indexed title with double quotes replaced by spaces, DOI is normalized:
   `"<DOI>" AND (reanalysis OR "re-analysis" OR "dose unit" OR harmonisation OR harmonization OR plausibility)`
   `"<TITLE>" AND (reanalysis OR "re-analysis" OR "dose unit" OR harmonisation OR harmonization OR plausibility)`
4. Review all retrieved titles/abstracts for possible equivalence, not just keyword flags; inspect permitted full text for plausible matches. Record index, exact request, UTC time, IDs, counts retrieved/reported, pagination/error status and a reason for each possible match's disposition. No numerical study data enter the log.

At least one index must supply a usable citation/search result, and both must be attempted. An index coverage gap or partial list is disclosed under F2 and does not automatically block freeze when no equivalent is identified among the reviewed records; state the search's actual scope. Failure of both indexes, or an unresolved plausible equivalent, gives NOT CLEARED, not "none found." A bot-blocked necessary full text gives NOT FEASIBLE. No claim of universal absence.

## 7. Selection ranking, fallback and screening log

Only candidates passing every required gate enter selection. After all five dispositions (or frame exhaustion), rank passing candidates by this **lexicographic** order:

1. Audit/method fit: 2 if both original assigned-dose and conversion/standardization procedures are explicitly documented; 1 if original doses/units are complete with a fully specified assignment rule and the original explicitly uses one common unit without conversion. Otherwise fail G4. No credit for unusual values, flags or effect size.
2. Profile: 3 for the exact review substantively guideline-cited, 2 for publication in the target journal, 1 for the defined widely cited route. Use the highest qualifying level; no extra point for larger citation counts.
3. Live question: 3 for an explicitly documented ongoing clinical/public-health controversy, 2 for a practice-changing claim, 1 for ongoing trials. Use the highest documented category.
4. Smaller upper-bound total Codex effort in quarter-hour units.
5. Smaller seeded hash from section 3, then normalized DOI lexically.

These are procedural selection priorities, not publication-ranking claims. The highest-ranked pass is the primary; the next is the **only fallback**. Fix both outcomes and source routes before any extraction. If no candidate passes, **STOP and report all dispositions**. If only one passes, report "fallback absent"; the primary can enter the later freeze pipeline, but failure then stops work. Do not promote a failing candidate to manufacture a pair. With two or more passes, do not activate candidate three after the fallback fails.

The later screening ledger must include every attempted frame rank/DOI, original target label, date/field/design/k evidence, source and licence locators/status, each gate result and reason (including NOT ASSESSED), novelty coverage/equivalence disposition, power scores, effort components/upper bound, elapsed screening time, final disposition and fallback rank. Record metadata exclusions separately and report unscreened remainder. Source locators and headers are allowed; study-level numbers are not. Published pooled statements, k and model wording may be recorded exactly, never recalculated.

No calculation on any candidate's data may inform eligibility, ordering, score, primary/fallback choice or switching. No extraction dataset, fitted curve, unit-outlier calculation, sensitivity model or trial reproduction is allowed at this stage. A no-flag or robust later finding is as reportable as a change. No outcome switching, changing original numbers, author contact, named-error allegation or priority claim.

## 8. Stop rule, authorization and execution

**If nothing passes, STOP and report every disposition as a feasibility failure. No v3 will follow without a new explicit Mahmood decision.** This applies after five dispositions or frame exhaustion, including a genuine zero-record frame. No widening the date range, changing sources, relaxing gates, trying another seed, crossing to the other option or completing an extra batch is authorized. The two records outside A's five-slot batch remain NOT SCREENED. B's unused records likewise remain NOT SCREENED. An unresolved retrieval never counts as a zero-candidate feasibility result.

If one passes, primary only and "fallback absent"; if at least two pass, select the top two by section 7 and no others. A later primary failure can activate only the independently cleared fallback; fallback failure or absence ends the analysis. Every result, including a robust/no-flag result, remains reportable. No clinical recommendation, priority claim or named allegation of error follows from this screen.

### 8.1 Actions required before any v2 run

1. **Done (2026-10-30).** Mahmood authorized one further five-disposition batch and chose **Option A**, before any v2 discovery or source inspection. Evidence: his decision as relayed in chat on 2026-10-30, "P02 and P04: Option A v2 approved. Proceed." (recorded in `supporting/DECISION_v2_2026-10-30.md` of the release package).
2. **Provenance recovered and reconciled (2026-10-30).** The original complete v1 run is preserved on pc2: `frame_P02.jsonl` (SHA-256 `c2aad90cf12b746b9de40dd5a88113ab43eccddb23c406f33008e53a7eff1a04`, 1,798 records), its COMPLETE run manifest (EPMC-1 reported 1,838 = retrieved 1,838, 2 pages; 40 metadata exclusions; output hashes match), and the standalone `TRIAGE_P02.jsonl` / `TRIAGE_P02_AUDIT.json` / `TO_FULL_TEXT_P02.json` (16 records visited, 4 EXCLUDED_TA, 12 TO_FULL_TEXT, stop at rank 16). The 16 triaged ranks, DOIs and dispositions match this protocol's inventory exactly, and every archived order hash equals the v1-seed hash. Ranks 17-1,798 were never triaged; they are not part of Option A's queue. **Pre-release correction B2-S (2026-10-30, coordinator-approved, before any release):** the drafted archive check accepted only a file of exactly the 16 triaged rows, so it would have refused the complete original frame that this protocol requires. Under the rule above ("If additional records ... are found, stop and amend ... before approval/release"), the check now requires the complete 1,798-record original frame. Every row must have a unique canonical DOI, its rank, its v1-seed hash and strictly increasing seeded order. Ranks 1-16 must equal the inventory, and the deferred subsequence must equal the C1 remainder. A 16-row cut, or any other rebuilt or truncated frame, is refused. In Option A's metadata-exclusion log, never-triaged ranks are labelled `v1_never_triaged_outside_option_A_queue`, not terminal screens. No gate, exclusion, order, seed or slot count changed. Do not rebuild the original frame by rerunning the API.
3. **Done (2026-10-30).** This is the approved version; the DRAFT is retained as history. The decision status and the single option are resolved, and only in this copy is the script's `DRAFT_ONLY` set to False (with `APPROVED_OPTION = "A"`; option B is refused). The filenames below are retained so the receipt checks the correct local protocol. The labelled synthetic checks were re-run on the finalized bytes.
4. Hash the approved protocol and script, freeze them, publish the distinct public **P02-screen-v2** screening release, record its server UTC timestamp and independently verify the release bytes against local hashes. Record the Zenodo DOI when minted; PENDING is allowed at this screening stage, as in v1. The screening release does not authorize extraction.
5. Supply the release/decision receipt and reconciled original frame to pc2. The script verifies local receipt fields/hashes; it cannot establish remote release existence or authenticate Mahmood's decision. Those are coordinator checks, not assumed tool results.

The script is standard-library Python only. It has no screening/scoring/extraction routine. Its execution path requires a matching P02-screen-v2 release receipt and refuses option B; no receipt or release has been created at finalization. Its offline `--print-queries` mode prints the exact query/template strings without requesting anything.

Required future receipt fields (schema only; no receipt has been issued):
- `paper: "P02"`, `version: "P02-screen-v2"`, `frame_option: "A"` (B was not chosen and is refused);
- `new_seed: "2026103002"`; `ordering_seed: "2026102802"` (the v1 seed, for A);
- `decision_by: "Mahmood"`, `decision: "APPROVE_ONE_FIVE_SCREEN_BATCH"`, nonempty `decision_evidence`, `approved_at_utc`;
- `v1_inventory_reconciled: true`, `v1_inventory_record_count: 16`, `v1_frame_sha256` for the recovered original bytes;
- `script_sha256` for `screen_P02_v2.py` and `prereg_sha256` for `PREREG_P02_screen_v2_DRAFT.md` in the approved package;
- `github_release_url: "https://github.com/mahmood726-cyber/usecase-preregistrations/releases/tag/P02-screen-v2"`, `released_at_utc` (not earlier than approval), and `zenodo_doi` as the real screening DOI or `"PENDING"`.

Future pc2 command, **only after the release in step 4 exists** (the paths are placeholders for files the coordinator must supply):
```text
python -B out/screen_P02_v2.py --run --frame-option A --release-record out/screen_release_P02_v2.json --v1-frame out/v1_archive/frame_P02.jsonl --out-dir out/screen_run_P02_v2_A
```

A performs no retrieval. The release receipt must match option A. The former option-B command is withdrawn: B was not chosen, and the script refuses it.

Future run outputs: `frame_P02_v2.jsonl`, `metadata_exclusions_P02_v2.jsonl`, `query_log_P02_v2.jsonl` and `run_manifest_P02_v2.json`, all in a fresh subdirectory of out/. The versioned frame filename avoids confusion with v1's `frame_P02.jsonl`. Every frame row is NOT_SCREENED. A preserves v1 ranks/hashes as provenance; B records the new hashes. Only a COMPLETE manifest with matching output hashes is usable. Existing outputs are never overwritten. Even if a write failure leaves partial files, FAILED_BLOCKED makes them unusable. No partial frame or failed receipt can authorize screening.

The standalone script constructs only the metadata frame. The per-candidate Europe PMC/OpenAlex requests and substantive novelty adjudication in section 6 are a later, separately logged screening activity; `--print-queries` is not a novelty check. OpenAlex lookup and cites requests are copy-pasteable templates after replacing DOI/W_ID:
```text
https://api.openalex.org/works/https://doi.org/<doi>
https://api.openalex.org/works?filter=cites:<W_ID>&per-page=100&page=1
```
Replace DOI with its normalized, URL-encoded value and W_ID with the confirmed OpenAlex work identifier. Follow section 6's unchanged page ceiling, empty-page completion rule, limited-coverage disclosure and equivalence review. Do not use OpenAlex to expand the discovery frame.

## 9. Subsequent selected-pair pipeline and verification

Any selected primary/fallback next enters the **same v4 freeze-criteria -> REDTEAM2 -> separate analysis freeze/release -> extraction pipeline**. Selection alone does not clear extraction. Apply F1 complete permitted/readable input sources and F2 independently documented novelty; F3 one fixed original-model configuration with no search; F4 all outcomes, unit-screen/conversion rules, model settings, tolerances and numeric new/robust criteria; F5 the binding verification specification; F6 static app file/function/hash evidence with unimplemented steps labelled external or R-only. Decision 7's P08/P13 default is not a general P02 default.

Binding verification text, [MAHMOOD_DECISIONS.md item 4](../MAHMOOD_DECISIONS.md), retained exactly:

> Human verification: humans check headline rows, a seeded 5% of the other rows (at least 1), and only the fields still disputed after a third-model adjudication plus a fourth AI re-check (agy, different family). If the sample error is over 2%: a full AI re-extraction plus a human re-check of the headline rows. Packets are about 30 minutes or less; at most one per person per week across all papers (COAUTHOR_LOAD.md); Mahmood is in the rota; a packet not returned in 7 days is reassigned.

Retain independent blind double extraction, explicit operational headline/sample rules and the shared co-author ledger. The pinned app commit is `14dc545bcba87a02158b2f445c28450e7eaf6b89`; independent pc2 R is 4.6.0 with dosresmeta 2.2.0. This draft does not certify app capability or parity and does not run R. Reverify v3 helper/provenance and covariance-convergence issues, synchronized code/verification/figure workflow and package/session pins for any selected analysis.

Synthetic analysis validation, actual app/R parity, browser dependency closure, synchronized extraction kit and packet assignment are mandatory post-release, pre-analysis conditions under the supplied freeze criteria. Static capability evidence remains F6. Synthetic code must pass before real-data reproduction. Then conduct extraction/verification, fixed original pooled-estimate/CI reproduction, app/R agreement and the registered audit in that order. No changed original number, author contact, outcome switching or real-data model search is allowed.

## 10. Validation and current limits

The companion `synthetic_test_screen_P02_v2.py` and `synthetic_screen_P02_v2_checks.md` cover only generated SYNTHETIC metadata, mocked responses and refusal paths. They do not establish live API compatibility, retrieval yield, source feasibility, novelty, candidate scores, app/R parity or statistical results.

Only historical protocols, identity/disposition metadata and supplied reports were read for this draft. No remaining candidate source was opened, fetched, screened or scored; no per-study row was transcribed and no candidate data were analysed. No network requests or release actions were made.

The decision is recorded (section 8.1 step 1). The original-frame provenance is recovered and reconciled, and the archive check was corrected before release (section 8.1 step 2, B2-S). Later substantive changes require a dated amendment before release or further screening, preserving all prior dispositions; they may not loosen v1 gates or depend on candidate calculations.
