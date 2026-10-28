# P02: preregistration of the next five candidate screens

**DRAFT FOR SCREENING FREEZE - amended 2026-10-28 before any candidate screening. Not frozen or released.**
Paper P02; target journal: *Observational Studies*; field: human observational epidemiology and nutrition dose-response meta-analysis, including behavioural and occupational exposures. The journal/field designation follows JOB.md, TASK_PAPER.md and the supplied v3 preregistration; manuscript.txt describes the dose-response app and its dosresmeta validation.

This document registers **screening only**. It selects a vehicle for a dose-unit plausibility audit, not a likely finding. No candidate-level numerical extraction, real-data calculation, new candidate source check or network query has been performed in this job. Bibliographic hashes and citation counts are not clinical-data analyses.

## 1. Authority and reason for another screen

[Mahmood decision 8](../MAHMOOD_DECISIONS.md) authorizes preregistering the next five screens in a seeded order, then executing that screen. It supersedes the old v3 prohibition on a sixth candidate; it does not relax source, power, effort or honesty gates. Decision 12 concerns P04 and grants no additional P02 source exception. JOB.md, JOB_RULES.md and SCREENPREREG.md govern this assignment over the historical TASK files' output and screening instructions.

Every previously approved P02 candidate failed the pre-specified complete-published-input gate, now F1 in [FREEZE_CRITERIA.md](../FREEZE_CRITERIA.md):

| Approved candidate | Gate and supplied evidence |
|---|---|
| Liang et al. (2025), DOI 10.1186/s13643-025-02800-8 | NOT FEASIBLE. Table 1/Figure 3 supply study descriptions/totals and per-increment effects, not all category doses, references, adjusted effects/CIs and category cases plus denominators. Figure 4 is a different synthesis. Successfully retrieved supplements do not fill the gap. |
| Li et al. (2020), DOI 10.1016/j.envint.2020.105739 | NOT FEASIBLE. Table 5/Figures 5/7/9 do not supply a complete matching dose-response input set or assigned-dose rule. The paper states dose-response statistical testing was not possible. A readable categorical forest does not establish an eligible dose-response vehicle. |

Evidence: [CANDIDATES_P02.md](../CANDIDATES_P02.md), especially feasibility and selection handoff; [v3 SOURCE_CHECK](../B_P02_V3/out/SOURCE_CHECK_P02.md), disposition and required-input maps; [v3 BLOCKERS](../B_P02_V3/out/BLOCKERS_P02.md), B1-B3. Li also had a 4-6-hour estimate above the four-hour cap. These are source-feasibility failures, not failed computed reproductions or allegations about publications. The v3 source check supersedes older uncertainty about access to those supplements. No v4 source-check/blocker package is supplied; the supplied freeze criteria govern the next use-case revision.

## 2. Fixed retrieval frame and executable queries

Publication window: **2016-10-28 through 2026-10-28, inclusive**. Require an open-access article, a DOI, and later confirmation of a permitted readable input source. No journal-only restriction: the target is the journal's field across journals. These broad bibliographic queries deliberately defer field, design, exact synthesis, k, input completeness and power assessment to the ordered full screens. They do not claim comprehensive coverage of every dose-response review.

The discovery frame is **Europe PMC ONLY**: the deduplicated output of **all pages** of the unchanged registered TITLE_ABS phrase query EPMC-1, after the metadata exclusions below. OpenAlex is **removed from discovery**, including its free-text searches and cursor traversal. It is retained only for each screened candidate's novelty check; that candidate's DOI lookup also supplies the unchanged G4 citation-count criterion. No convenience additions, citation-ranked truncation, keyword changes, date extension or replacement database.

Europe PMC REST query EPMC-1:

```text
(TITLE_ABS:"dose-response" OR TITLE_ABS:"dose response") AND (TITLE_ABS:"meta-analysis" OR TITLE_ABS:"meta analysis") AND FIRST_PDATE:[2016-10-28 TO 2026-10-28] AND OPEN_ACCESS:Y
```

Endpoint: `https://www.ebi.ac.uk/europepmc/webservices/rest/search`; parameters: query above, `format=json`, `resultType=lite`, `pageSize=1000`, `cursorMark=*`, then each returned cursor. Retrieve every page until the stable hitCount is matched by unique source/id records; missing/repeated cursors, duplicate records or count drift before completion fail the retrieval.

Copy-pasteable, URL-encoded initial request (the script follows subsequent cursors):

```text
https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28TITLE_ABS%3A%22dose-response%22+OR+TITLE_ABS%3A%22dose+response%22%29+AND+%28TITLE_ABS%3A%22meta-analysis%22+OR+TITLE_ABS%3A%22meta+analysis%22%29+AND+FIRST_PDATE%3A%5B2016-10-28+TO+2026-10-28%5D+AND+OPEN_ACCESS%3AY&format=json&resultType=lite&pageSize=1000&cursorMark=%2A
```

The script `screen_P02.py --print-queries` prints the discovery URL without network access. No API key, login or new account is required by the script. HTTP 5xx failures receive **at most five attempts at the identical URL**, with backoff **1, 2, 4, 8 seconds** (15 seconds total), a 60-second request timeout and one-second pacing between pages. Each attempt's UTC time, HTTP status, response hash and delay is logged. Explicit bot challenges, HTTP 401/403 or other non-5xx failures, non-JSON/schema failures and transport failures are not retried. No bypass or silent change to the search. The same bounded HTTP policy is available for candidate OpenAlex retrieval.

If retries are exhausted or any retrieval is incomplete, record **FAILED_BLOCKED**, preserve the failure log/manifest and **do not create or use a discovery frame or start screening**. Unknown/partial retrieval is never a zero-hit result; frame_count is absent on failure. A genuine zero requires a valid complete response with hitCount=0 and an empty result list.

**Metadata rules.** Normalize DOI by stripping surrounding whitespace, a DOI URL or `doi:` prefix, percent-decoding once, and lowercasing; retain suffix punctuation. Require the form `10.<4-9 digits>/<non-whitespace suffix>`. Deduplicate solely on that DOI; retain all bibliographic provenance and disagreements. Missing/invalid DOIs are logged and excluded, not assigned surrogate hash keys. Separate DOI versions remain separate until the ordered screen identifies a duplicate review; that terminal screen still consumes a slot.

Use the earliest exact valid YYYY-MM-DD publication date among the returned records. Log conflicts; do not impute month/day from a year. Exclude a missing exact date, an earliest date outside the window, explicit retracted status if supplied, or absence of an OA-positive record. Removal of OpenAlex discovery also removes that index's discovery metadata; no extra OpenAlex lookup is used to construct the frame. The G1 retraction check during full screening is unchanged. OA metadata is provisional: the full screen must verify actual access, licence and original publication date. A disagreement that cannot be resolved within the source/effort rules fails that candidate; do not hand-edit the frame to move it. Do not infer absence of retraction from Europe PMC's lack of a flag.

**Previously screened exclusions, applied before ordering:**

1. Liang et al. (2025), UPF/all-cause mortality: `10.1186/s13643-025-02800-8`.
2. Li et al. (2020), working hours/acquired IHD: `10.1016/j.envint.2020.105739`.
3. Hackshaw et al. (2018), smoking/CHD: `10.1136/bmj.j5855`.
4. Descatha et al. (2020), working hours/stroke: `10.1016/j.envint.2020.105746`.
5. Suksatan et al. (2021 online; 2022 issue), UPF/mortality: `10.3390/nu14010174`.

These exclusions are permanent for this screen, regardless of accessible new copies. Do not reuse incidental leads from the previous search unless the frozen queries independently retrieve them.

## 3. Seeded order and the five-screen ceiling

**Seed: 2026102802.** For each normalized DOI, calculate lowercase hexadecimal SHA-256 of the UTF-8 string:

```text
2026102802|P02|screen|<doi>
```

Sort ascending by digest, then ascending normalized DOI for a hash tie. Index relevance, citation count and arrival order do not set screening order.

Lock the first complete metadata frame and its SHA-256 before opening any new candidate's full text or conducting its novelty review. Screen in that order until **five candidates have a completed screening disposition**, or the frame is exhausted. Do not stop early because a promising candidate passes. Each of these first five receives a complete checklist/disposition; a failed gate may end source inspection, with later gates marked NOT ASSESSED - TERMINAL FAILURE. Such a rejection, bot block, wrong-field record, duplicate, unconfirmed k or effort failure **counts toward five**. It is not replaced by record six. Administrative pre-frame metadata exclusions do not consume slots; every exclusion is retained.

This operational definition of a full screen prevents selective replacement of inconvenient records. Remaining frame records stay NOT SCREENED. If fewer than five exist, screen all and report the exact denominator. If a retrieval query fails or pagination is incomplete, there is no usable frame and no screening.

## 4. Fixed outcome and gates for each candidate

Before judging numerical summaries, record exactly one synthesis from the published report: the first author-designated primary outcome/exposure/comparison in Methods (Methods order resolves co-primary outcomes); if none is designated, the first overall dose-response synthesis encountered in main-text reading order, then the first panel in printed order. Use its author-designated primary population and follow-up. If multiple analyses remain indistinguishable, fail as AMBIGUOUS TARGET. Do not search secondary outcomes for an eligible k, more complete data or a larger effect.

Complete these gates using published features only. A PASS requires evidence and exact locators; unverified required information is not a pass.

**G1 - field, date, design and k.** Human observational epidemiology/nutrition, a real published aggregate dose-response meta-analysis, within the date window. Exclude protocols, primary studies, umbrella summaries without their own qualifying input set, retracted reports, and inseparable trial/observational mixtures. Require **5 <= k <= 60 independent studies/cohorts in the designated dose-response synthesis**, as supported by published aggregate k and methods. Review-wide counts, counts of reports, or highest-versus-lowest k cannot substitute. Unresolved independence or synthesis correspondence fails. Record pooled k exactly as printed; never enumerate/transcribe study rows to manufacture k.

**G2 - licence, source access and readable complete inputs (F1).** Verify the licence on the article and each needed supplement. Require CC BY, CC0, or another explicit open licence permitting the planned factual-data reuse; record licence terms and source locator. NC/ND labels do not automatically authorize adapted figures/tables. Do not redistribute or adapt restricted source content; an unresolved reuse condition fails. Recreate later analysis figures only from permitted inputs.

Use only the review's own main-text table, numbered figure/forest or published supplement via the publisher, Europe PMC/PMC or an openly licensed repository copy of that review. Require printed category-level doses or bounds plus a fully specified original assignment rule, physical units/denominator, reference category, adjusted relative effects with CIs, **cases and total persons or person-time in every required category, including reference counts**, and unambiguous mapping to the designated synthesis. Record locations/column headers, text versus image readability, and required-field availability only. A clear image is FEASIBLE-IMAGE, not a reason to invent precision. Curve coordinates, per-increment forests and study totals do not replace category inputs. No OCR/digitization dataset, primary-study reconstruction, count imputation, author data or post hoc subset.

The complete printed sources must support the same physical exposure quantity and reference system and a source-supported unit map; dimensional comparability cannot be assumed. No per-study value is copied, paraphrased, calculated or tested in screening. Mere differing unit labels are not evidence of a discrepancy.

A required candidate source that encounters a bot check is recorded **blocked; NOT FEASIBLE**, consumes a screen and is not bypassed, retried via an alternate route, or rescued by author contact. A normal alternative open repository may be used to locate an initially unavailable/publisher-paywalled source before any bot block, without login or payment. Never bypass a check.

**G3 - novelty (F2).** Use the definition and procedure in section 5. An equivalent audit excludes the candidate. An unresolved potentially equivalent record fails clearance. Report coverage limitations honestly; incomplete citation counts are not invented negatives.

**G4 - all three powerful criteria.** [FIELD_USE_CASE_PROTOCOL.md](../FIELD_USE_CASE_PROTOCOL.md) remains binding. Apply the following operational rules, fixed before screening:

- High profile: published in *Observational Studies*; OR the exact review is substantively cited in a named published clinical/public-health guideline; OR widely cited, operationalized here as OpenAlex cited_by_count >= 100 **and** substantive discussion of this review in a separate published guideline, consensus statement or evidence review. A passing citation count alone is insufficient. Record the count/date and citation locator; institutional branding alone is insufficient.
- Live question: the original Introduction/Discussion documents a controversy, a practice-changing claim or ongoing trials, with its reference/locator. Do not manufacture relevance from a computed effect.
- Method-question fit: preserve the protocol's published **linear-only dose-response analysis of an exposure where a threshold is plausible**, evidenced by the original rationale or a cited published rationale. In audit mode, also require explicit unit/assignment/standardization documentation permitting a dose-unit plausibility audit with the printed complete inputs. The contribution is testing robustness to unit handling, with no assumed flag or curve change. A spline-only re-analysis is not this audit. No suspected numeric anomaly may raise a candidate's score.

**G5 - effort.** At most **four hours of subsequent Codex work** for the single designated synthesis, covering extraction/checking, reproduction, app/R comparison, figure and short write-up, assuming the common app workflow is ready. Independent extractor and human packet time are additional and disclosed, never silently included as free Codex labour. Before selection, estimate those five components in quarter-hour increments from published format, source count and required workflow, without transcribing values. If any defensible upper bound exceeds four hours, or the work needs reconstruction/contact, fail. Also cap this full screening session at **60 elapsed working minutes per candidate**, including novelty checking; unresolved gates at the cap fail. Pause the timer only for a documented external interruption, not difficult searching.

## 5. Prospective novelty procedure and equivalence

Authorized deviation: Europe PMC and OpenAlex replace Google Scholar, which displayed an "unusual traffic" bot check on 2026-10-28; it was not bypassed ([decision 3](../MAHMOOD_DECISIONS.md)). Do not revisit Scholar.

**Same equivalence definition as [v3 section 9](../B_P02_V3/out/PREREG_P02_usecase.md):** an equivalent prior re-analysis uses the same underlying synthesis, fixed outcome/comparison and substantially the same dose-unit plausibility or source-supported dose harmonisation audit with consequent re-analysis. Different software or terminology does not establish a difference. A different topic synthesis, ordinary exposure association or spline analysis alone is not equivalent. An already reported equivalent audit in the original also leaves no unreported audit contribution.

After release, for each screened DOI:

1. Resolve Europe PMC identity with the REST search parameter `query=DOI:"<doi>"`, `format=json`, `resultType=lite`. Confirm title/DOI, then request `https://www.ebi.ac.uk/europepmc/webservices/rest/<source>/<id>/citations?format=json&page=1&pageSize=1000`; follow all pages to the reported total or a logged failure. If multiple source IDs map to the same DOI, use all, deduplicating citing records by DOI, otherwise source/id.
2. Resolve OpenAlex with `https://api.openalex.org/works/https://doi.org/<doi>`. Confirm the returned DOI/title and W identifier; retain cited_by_count for the unchanged profile criterion. Request `https://api.openalex.org/works?filter=cites:<W_ID>&per-page=100&page=1`, then page=2, page=3 and so on **until an empty results page**, with **at most 10,000 records (100 pages)**. No cursor, free-text search, discovery-date or OA filter is used. A short nonempty page or reaching the advertised count alone does not establish completion. Completion requires an empty page and matching stable count with no repeated records. Above 10,000, retain the retrieved prefix and record **INCOMPLETE_LIMIT** with reported/retrieved counts and the ceiling; no claim of complete coverage. If page 100 is nonempty, including at exactly 10,000 reported records, the terminal empty page is unverified: also disclose INCOMPLETE_LIMIT rather than requesting page 101 beyond the paging ceiling. HTTP/access/schema/count/duplicate failures retain partial evidence with **FAILED_BLOCKED**, not zero citations. Both types of incomplete check are coverage limitations under the unchanged F2 rule below; they do not add records to the discovery frame. Non-OA citations may identify prior work, although no paywall may be bypassed.
3. Supplement these citation lists with Europe PMC search using each of the following two exact templates, with ordinary URL encoding. TITLE is the full indexed title with double quotes replaced by spaces, DOI is normalized:
   `"<DOI>" AND (reanalysis OR "re-analysis" OR "dose unit" OR harmonisation OR harmonization OR plausibility)`
   `"<TITLE>" AND (reanalysis OR "re-analysis" OR "dose unit" OR harmonisation OR harmonization OR plausibility)`
4. Review all retrieved titles/abstracts for possible equivalence, not just keyword flags; inspect permitted full text for plausible matches. Record index, exact request, UTC time, IDs, counts retrieved/reported, pagination/error status and a reason for each possible match's disposition. No numerical study data enter the log.

At least one index must supply a usable citation/search result, and both must be attempted. An index coverage gap or partial list is disclosed under F2 and does not automatically block freeze when no equivalent is identified among the reviewed records; state the search's actual scope. Failure of both indexes, or an unresolved plausible equivalent, gives NOT CLEARED, not "none found." A bot-blocked necessary full text gives NOT FEASIBLE. No claim of universal absence.

## 6. Selection ranking, fallback and screening log

Only candidates passing every required gate enter selection. After all five dispositions (or frame exhaustion), rank passing candidates by this **lexicographic** order:

1. Audit/method fit: 2 if both original assigned-dose and conversion/standardization procedures are explicitly documented; 1 if original doses/units are complete with a fully specified assignment rule and the original explicitly uses one common unit without conversion. Otherwise fail G4. No credit for unusual values, flags or effect size.
2. Profile: 3 for the exact review substantively guideline-cited, 2 for publication in the target journal, 1 for the defined widely cited route. Use the highest qualifying level; no extra point for larger citation counts.
3. Live question: 3 for an explicitly documented ongoing clinical/public-health controversy, 2 for a practice-changing claim, 1 for ongoing trials. Use the highest documented category.
4. Smaller upper-bound total Codex effort in quarter-hour units.
5. Smaller seeded hash from section 3, then normalized DOI lexically.

These are procedural selection priorities, not publication-ranking claims. The highest-ranked pass is the primary; the next is the **only fallback**. Fix both outcomes and source routes before any extraction. If no candidate passes, **STOP and report all dispositions**. If only one passes, report "fallback absent"; the primary can enter the later freeze pipeline, but failure then stops work. Do not promote a failing candidate to manufacture a pair. With two or more passes, do not activate candidate three after the fallback fails.

The later screening ledger must include every attempted frame rank/DOI, original target label, date/field/design/k evidence, source and licence locators/status, each gate result and reason (including NOT ASSESSED), novelty coverage/equivalence disposition, power scores, effort components/upper bound, elapsed screening time, final disposition and fallback rank. Record metadata exclusions separately and report unscreened remainder. Source locators and headers are allowed; study-level numbers are not. Published pooled statements, k and model wording may be recorded exactly, never recalculated.

No calculation on any candidate's data may inform eligibility, ordering, score, primary/fallback choice or switching. No extraction dataset, fitted curve, unit-outlier calculation, sensitivity model or trial reproduction is allowed at this stage. A no-flag or robust later finding is as reportable as a change. No outcome switching, changing original numbers, author contact, named-error allegation or priority claim.

## 7. Freeze, execution and subsequent pipeline

Before retrieval/screening, pc2 freezes this document and the script with SHA-256 hashes, publishes a public GitHub screening release in `mahmood726-cyber/usecase-preregistrations`, records its server UTC timestamp, and verifies that the released bytes match the frozen digests. **The public GitHub release is the precondition for retrieval and screening.** The Zenodo DOI is recorded when minted (value `PENDING` until then); it is not a precondition (pre-freeze amendment, coordinator, 2026-10-28, consistent with Mahmood's rule "no extraction or analysis before the release exists"). This draft does not assert those events have occurred. Do not run the discovery query before that screening release.

The coordinator supplies a JSON release receipt with these fields (placeholders below are not an actual receipt):

```json
{
  "script_sha256": "<SHA-256 of screen_P02.py>",
  "prereg_sha256": "<SHA-256 of PREREG_P02_screen.md>",
  "github_release_url": "https://github.com/mahmood726-cyber/usecase-preregistrations/releases/tag/<screen-tag>",
  "zenodo_doi": "<actual screening-release DOI>",
  "released_at_utc": "<server timestamp in UTC>"
}
```

From the job root, after release only:

```text
python -B out/screen_P02.py --fetch --release-record out/screen_release_P02.json
```

Default future output directory: `out/screen_run_P02/`. It will contain `frame_P02.jsonl`, `metadata_exclusions_P02.jsonl`, `query_log_P02.jsonl` and `run_manifest_P02.json`. The frame is bibliographic only; NOT_SCREENED appears on every record. The script checks receipt fields/local hashes, not remote release existence: independent coordinator verification is essential.

The Europe PMC discovery query must finish with stable reported counts and complete nonrepeating cursorMark traversal. The log records projected bibliographic metadata, exact request URLs, response hashes, counts and UTC times; abstracts/full text are not saved. Exhausted bounded 5xx retries, a blocked request, schema error, changing count or partial traversal stops the run with manifest status FAILED_BLOCKED; no partial frame is usable and the screen is blocked. Accept output only with manifest status COMPLETE and matching output hashes. Existing outputs are never overwritten. An identical retry after a transient API failure may use `--out-dir out/<new-run-directory>`, preserving the failed receipt; it is allowed only before any candidate screen. No bot-check retry. Freeze the first complete run and do not resample it. The date window remains fixed even if retrieval occurs later; index growth means this is the recorded execution snapshot, not a claimed historical index snapshot.

For the OpenAlex part of a candidate's novelty check, after the screening release and only when its seeded screening turn is reached:

```text
python -B out/screen_P02.py --fetch --release-record out/screen_release_P02.json --novelty-doi <candidate-doi> --out-dir out/screen_run_P02/<candidate-key>
```

Replace the two bracketed arguments with that candidate's actual DOI and directory key. This separate mode never runs discovery. It writes `novelty_openalex_P02.jsonl` (lookup/citation metadata and request receipts) and `novelty_openalex_P02.json` (counts, complete/incomplete status, failure/limit reason, local release receipt and log hash). It exits nonzero if citation retrieval is incomplete; partial metadata remain usable only as explicitly limited novelty evidence. It does not review equivalence, clear novelty or select candidates. Europe PMC citations, the supplementary searches and human review in section 5 remain required. All output stays under the script's out/ directory, in fresh candidate subdirectories; never overwrite prior runs.

**After selection:** prepare the selected primary/fallback use-case package under the supplied v4 freeze criteria, then REDTEAM2, resolve F1-F6 findings, freeze/release that separate analysis preregistration, and only then extract. The screening release never unlocks extraction. Candidate F1 feasibility and F2 novelty are independently documented; F3 fixes one original-model configuration with no model search; F4 fixes all outcomes, unit-screen/conversion rules, model settings, tolerances and numeric new/robust criteria; F5 preserves the binding verification spec; F6 cites pinned static app capability by file/function/hash and labels external/R-only steps. Do not carry the v3 pair's unresolved model choices into new candidates. Decision 7's specific P08/P13 default is not a blanket P02 default.

Binding F5 text, [decision 4](../MAHMOOD_DECISIONS.md), copied exactly:

> Human verification: humans check headline rows, a seeded 5% of the other rows (at least 1), and only the fields still disputed after a third-model adjudication plus a fourth AI re-check (agy, different family). If the sample error is over 2%: a full AI re-extraction plus a human re-check of the headline rows. Packets are about 30 minutes or less; at most one per person per week across all papers (COAUTHOR_LOAD.md); Mahmood is in the rota; a packet not returned in 7 days is reassigned.

The selected use-case preregistration also retains independent blind AI double extraction, exact operational headline/sample rules and the shared co-author ledger. App pin: `14dc545bcba87a02158b2f445c28450e7eaf6b89`; independent R on pc2: R 4.6.0, dosresmeta 2.2.0. A dose-unit audit is external unless implemented capability is actually evidenced; this screening package certifies no app feature.

Carry forward the v3 warnings for re-verification: app helper/provenance issues and inner covariance-convergence visibility; synchronized code/verification/figure workflow; package/session pinning. Under the newer freeze criteria, synthetic validation, actual app/R parity, browser dependency closure, extraction-kit synchronization and packet assignment are **mandatory post-release, pre-analysis conditions**, not extra reasons to refuse an otherwise F1-F6-complete analysis freeze. Static capability evidence remains F6. Synthetic validation must pass before real-data reproduction.

Then double extraction/verification, fixed original pooled-estimate/CI reproduction, app/R agreement and the registered audit proceed in that order. Primary failure activates only the independently cleared fallback; fallback failure or absence stops the analysis. Do not add a candidate after seeing results. Archive all dispositions and failures; retain original numbers and report robust findings.

## 8. Validation, amendments and outstanding execution

Local validation is synthetic metadata only, using `synthetic_test_screen_P02.py`; the first line identifies it as SYNTHETIC - not data. Its report is `synthetic_screen_P02_checks.md`. No live endpoint compatibility, retrieval yield, candidate feasibility or statistical validation is claimed.

The protocol's numerical profile threshold, scoring levels, deterministic target rule, screening timer and metadata handling are prospective operationalizations, not previously observed facts. Any later substantive query/gate/ranking change requires a dated amendment and new public screening freeze before further screening; retain the original frame, attempted records and reasons. It cannot depend on candidate calculations. Log technical fixes as dated deviations, with unchanged selection rules and no silent search substitution.

### Pre-freeze amendment A1 - discovery instrument repair, 2026-10-28

Authority/evidence: the binding [JOB.md decision](../JOB.md), reporting pc2's count-only instrument check on 2026-10-28. Only meta.count / hitCount were fetched; these are index counts, not study observations or candidate screens. The registered OpenAlex relevance searches returned fuzzy, unbounded discovery frames: **P02: 835,052 and 834,162**; **P04: 6,191 / 2,237 / 2,237 / 56,404 / 4,496 / 56,430 / 6,555 / 22,577**. OpenAlex cursor paging had returned **HTTP 401 beyond the first page without an API key** earlier that day. Europe PMC was temporarily returning **503**; its registered TITLE_ABS phrase queries and cursorMark traversal are the retained discovery route. These supplied observations were not independently rerun in this job.

Before freeze, extraction or any new candidate screening, remove OpenAlex from the discovery frame, retain the existing Europe PMC query unchanged, add bounded 5xx backoff and explicit failed/blocked handling, and use OpenAlex only for per-candidate novelty via cites filters with page-based paging at 100 records per page and the disclosed 10,000-record ceiling. This supersedes the historical SCREENPREREG.md requirement for OpenAlex discovery strings and the prior draft's cursor-based OpenAlex novelty request. The seed **2026102802**, date window, DOI normalization/deduplication, five prior exclusions, ordering, five-screen ceiling, outcome rule, gates, scores, tie-breaks, selection, fallback, equivalence definition and subsequent pipeline are unchanged. The matching script and synthetic tests implement A1.

**SHA-256, public release URL, server UTC time and DOI to be recorded at release.** Publication of the screening release, live retrieval, screening and the later analysis package are designed future process steps, not present screening-specification defects. [BLOCKERS_P02_screen.md](BLOCKERS_P02_screen.md) lists only genuine unresolved specification defects, or NONE.
