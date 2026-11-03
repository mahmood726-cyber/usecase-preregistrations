# P04 screening v3 (P04-screen-v3): approved for freeze and release; not yet released

> **Status: approved for freeze and release; not yet released.** Drafted 2026-11-02 under Mahmood's authorization to draft v3 (relayed via dispatch). Every open item was settled the same day by dispatch, under Mahmood's delegation (`supporting/DECISION_v3_2026-11-02.md`). No candidate has been screened. Until a public **P04-screen-v3** GitHub release exists, nothing may be queried, screened, scored, selected, extracted or analysed under this text.

## 0. Authority and what v3 changes

- **Predecessor.** P04-screen-v2 was released publicly: tag `P04-screen-v2`, commit `8435ff9`, Zenodo DOI 10.5281/zenodo.23883314, **verified** by the coordinator (doi.org resolves to the Zenodo record; title and version match the tag). The v2 run receipt `release_receipt_P04_v2.json` keeps `PENDING`, the historical value used when the v2 frame was built. Released bytes: prereg sha256 `414a84ef1b39fcda426a925e0f877de22df52a5b9e91be5f9394116a09c7c71a`, script `a1bc0d4f146bbdbd7c4c210cbe71de50b76f525953515e0f68e8c2b6b586617b`. Byte-identical copies are in `supporting/v2_archive/`.
- **v2 outcome.** The v2 run correctly ended in a pre-registered feasibility failure. v2_screen_order 1-5 (v1 ranks 22-26) all failed. Three failed on scope: a plain-language summary of an excluded review, a non-drug network, and a protocol. Two failed on k: an NMA made up mostly of observational studies, and a composite ranking index with no trial k. Under v2 section 6, no v3 follows without a new decision. **This text is the product of that new decision, not a continuation of v2.**
- **Mahmood's three authorized changes (dispatch):**
  1. **A larger candidate pool** (section 2).
  2. **Feasibility judged only from** headers (title, abstract, keywords, bibliographic metadata), the Methods section and the licence statement. Results, Discussion, tables, figures and supplements are never read for the feasibility judgement (sections 3-4).
  3. **Every gate's operational rules fixed in this text before any screening**, so that no judgement call is left to the screener (sections 4-6).
- **Everything else** is unchanged from v2 or tighter. `supporting/CHANGES_v2_to_v3.md` gives every change and its reason. `supporting/DECISION_v3_2026-11-02.md` records the settling decisions.
- **Binding sources:**
  - `supporting/FIELD_USE_CASE_PROTOCOL.md`, sha256 `4f6e05206d46059cdbb9bcc6c8a34ac47ebad6e7bb7483e5a5398b6037ce9bac`. This is the approved field-use-case protocol. v3 relies on it for the "powerful" criteria, k <= 60, the effort cap, no author contact and the honesty rules. The released v2 text did not cite it directly; v3 does, so a byte-identical copy is included.
  - `supporting/MAHMOOD_DECISIONS.md`, sha256 `571469f9c90265398f479ac322ea426977674ee14806ee14fd9f90abeac8028f`. Relevant items: 2, 3, 4, 6, 12 and 14.
  - `supporting/DECISION_v3_2026-11-02.md`: dispatch, under Mahmood's delegation, 2026-11-02.

## 1. The v2 dispositions that motivate the operational rules

| v2 / v1 rank | DOI | v2 terminal gate | Ambiguity the v2 screener flagged | v3 rule that now decides it |
|---|---|---|---|---|
| 1 / 22 | 10.1007/s40123-026-01434-w | scope: Summary of Research of the excluded 10.1007/s40123-025-01247-3 | Derivative of an excluded DOI; visited and consumed a slot | Section 2.3 (offline derivative and non-original rules) plus F2 (visit-time derivative rule). Now excluded as a v2 disposition. |
| 2 / 23 | 10.3389/fendo.2022.895458 | k: 41 observational studies + 1 RCT; NMA of 18 "studies" | Do observational studies count as "independent trials"? | F7: the NMA must be RCT-only according to Methods. Here Methods admit observational designs, so **F-FAIL at F7**. |
| 3 / 24 | 10.3389/fendo.2025.1462104 | scope: exercise/acupuncture network | - | F6: fewer than two active pharmacological nodes, so **F-FAIL**. |
| 4 / 25 | 10.1097/md.0000000000028365 | scope: protocol | - | Removed offline by the protocol title rule (2.3). At a visit it would be F2 FAIL. |
| 5 / 26 | 10.1111/dom.70742 | k: designated primary CEI is a SUCRA-derived index | CEI as one outcome, or as "several" (which would fall back to HbA1c)? | F8 rule C2: a sole designated derived index fails. **No component substitution.** **F-FAIL at F8.** |
| process | - | - | Gate order: the brief said k first, v2 section 4 said scope first | Sections 3-5 fix one inspection order. The first non-PASS step is terminal. |

All five v2 decisions above are the same under v3. v3 records them as rules instead of stricter readings applied case by case.

## 2. Candidate pool: larger, with no new seed and no re-retrieval

### 2.1 Frame and order
- **Default pool:** the unvisited remainder of the archived seeded order, **v2_screen_order 6-540** (535 records) of `supporting/v2_archive/frame_P04.jsonl`.
  - That file has sha256 `3563a7efe93c2f74d6a2718fef647ec5a0132cfc21e32870f0fe69fda7277d1d` and 540 rows. It was derived from `supporting/v1_archive/frame_P04.jsonl` (sha256 `fef70cafb5a84c329c62b8b8122d2c634e5a43301455c1c5065a7bbe4053063f`, 561 rows, seed **2026102804**).
  - The order is that seed's order: ascending sha256("2026102804|P04|screen|" + canonical DOI), then DOI. **No new seed. No new retrieval.** Metadata is not refreshed.
- **The script verifies before building:**
  - both hashes and row counts;
  - that the v1 rows are in seed-hash order with contiguous ranks and are unannotated;
  - that the v2 frame is exactly the v1 frame minus the 26 v1-era exclusions, field for field, with contiguous v2 orders;
  - that v2 orders 1-5 are the five v2-visited DOIs.
  Any mismatch stops the build. There is no substitute source.
- **The v3 queue:** v2 rows 6-540 in archived order, after the exclusions in 2.2-2.3. Each row keeps its v1 rank, v2 order and seed hash and gains a contiguous `v3_queue_order`.

### 2.2 Prior-disposition exclusions (31 DOIs; Appendix A)
- Every DOI with any v1 or v2 disposition is excluded:
  - the 5 pre-v1 exclusions;
  - the 21 v1 title-triaged records, including the 7 referrals that were never full-screened;
  - the 5 v2-visited records.
- No title, endpoint, access change or new database revokes an exclusion.

### 2.3 Declared filter stage: metadata rules applied offline, before any visit (implemented in `screen_P04_v3.py`)
This is a **declared filter stage**, separate from screening. Its rules read only the archived frame's title, DOI and record source ID. They never read abstracts or full text. A removed row is **not a visit** and uses no Stage F slot. The build audit reports the filter separately (`declared_filter`): rows in, distinct rows removed, rows kept, and an item count for each rule (an item matching several rules is counted under each). Every removed row is listed by DOI with its reasons in the audit and in Appendix E.

**Title normalisation.** Strip markup, unescape HTML entities, apply Unicode NFKC, casefold, turn every run of non-[0-9a-z] characters into one space, and trim.

**(a) Non-original title markers.**
- *Raw title* (punctuation matters) starts with one of these, followed by an optional to/for/on/of and then a colon, or a dash followed by whitespace:
  - correction, corrigendum, corrigenda, erratum, errata;
  - retraction (note/notice), retracted (article), withdrawn, withdrawal;
  - expression of concern;
  - comment, commentary, reply, response, letter, editorial.
- *Normalised title* contains one of these:
  - "summary of research" or "plain language summary/summaries";
  - starts with "correction/corrigendum/erratum to";
  - starts with "retraction of/note/notice";
  - "expression of concern";
  - "comment on", "commentary on", "reply to", "in reply to", "letter to the editor", "authors reply";
  - "protocol for (a|an|the)? (systematic|network|meta|bayesian|living|updated|umbrella|review)...";
  - "(a|an|study|review|research) protocol";
  - ends with "protocol".
- Negative controls in the tests: "Correction of ... hyperglycaemia", "... titration protocols compared", "Glycaemic response to ...", and "Commentary-free ...". All are retained.

**(b) Preprints.**
- DOI prefix is one of: 10.21203/ (Research Square), 10.1101/ (bioRxiv/medRxiv), 10.20944/ (Preprints.org), 10.2139/ (SSRN), 10.31219/ (OSF), 10.22541/ (Authorea), 10.48550/ (arXiv), 10.31234/ (PsyArXiv), 10.31222/ (MetaArXiv);
- or a Europe PMC record ID starts with `PPR:`.

**(c) Derivative or version of an excluded DOI (exact rule).**
- A record is removed if its normalised title *contains* the full normalised title of any excluded record and its DOI differs.
- The excluded record's normalised title must be at least 40 characters.
- This catches summaries, errata, letters, replies and republished versions that reproduce the excluded title. It also catches a same-title "update". That makes the rule conservative, which is tighter, not looser.
- Titles are available in the archive for 26 of the 31 excluded DOIs. The 5 pre-v1 exclusions are not in the frame, so their derivatives are caught offline only by rule (a), and otherwise at the visit by F2(iii).

**(d) Exact-title duplicate groups.** If two or more queue-eligible rows share an identical normalised title, **every member of the group is removed** (rule `exact_title_duplicate_group`). Archived hash order cannot tell an original from a same-title correction notice, and no keep-rule or screener choice is allowed (stricter reading, DECISION_v3 OD-6).

**Offline dry build (scratch folder outside the package; no network):**
- Rows in: 535. Distinct rows removed: **57**. **Rows kept (queued): 478.** The 40th queue position is v2 order 51.
- Item counts per rule:
  - non-original title, protocol: 46;
  - non-original title, comment/reply/letter: 4;
  - non-original title, erratum/correction: 2;
  - derivative or version of an excluded DOI: 2 (a letter and a reply about 10.1007/s40123-025-01247-3);
  - preprint DOI prefix: 4; preprint record source: 4 (the same 4 rows);
  - exact-title duplicate group: 4 (two pairs).
- The queue is rebuilt deterministically by `--build` after release, and the run records its sha256. The dry-build queue sha256 is in `supporting/synthetic_validation_P04_screen_v3.md`.

### 2.4 Re-retrieval: not forced, not proposed
- Nothing in this text needs a new retrieval or seed. The 480 queued records are 12 times the Stage F budget.
- Re-retrieval with a new query, window or seed is **not** part of v3 (DECISION_v3 OD-10). If the queue is ever exhausted, the stop rule in section 6 applies.

## 3. Two stages with fixed numbers

| Quantity | Value | Status |
|---|---|---|
| Stage F budget N_F | **40** feasibility dispositions, or queue exhaustion | fixed (dispatch 2026-11-02) |
| Stage F cap | **20 min** per disposition | fixed (dispatch 2026-11-02) |
| Stage S budget N_S | **5** full screens: the first 5 F-PASS records in v3 queue order (field protocol: "Screen up to 5 candidates") | fixed (dispatch 2026-11-02) |
| Stage S cap | **60 min** per full screen | unchanged from v2 |
| k window | **5 <= k <= 60** independent randomised trials, outcome-specific | unchanged |
| Effort | **E <= 4.0 h** (section 5, S12 formula) | unchanged threshold |
| M, L, P | **M >= 1, L >= 1, P >= 1** | unchanged |

**Sequence.**
1. Stage F visits the queue strictly in order, one row at a time. Every visited row uses one Stage F slot, whatever its disposition (F-PASS, F-FAIL or F-UNRESOLVED). There is no skip, replacement or 41st visit. Stage F never stops early, whatever the number of passers; all 40 dispositions are completed unless the queue is exhausted (DECISION_v3 OD-8).
2. When Stage F ends, the complete F log is validated by `validate_stage_f_log`, hashed and recorded. Only then may Stage S start. A validator error stops the run; it is reported, not repaired by re-screening.
3. Stage S runs on `stage_s_queue`, the first <= 5 F-PASS records in queue order. Every one is screened. An S failure is not replaced by the 6th F-passer.
4. Selection and the stop rule follow (section 6).

**Which gates are decided where.**

| Requirement (v2 name) | Stage F (headers + Methods + licence) | Stage S (full source) |
|---|---|---|
| Original NMA / non-original / derivative (scope) | decided: F2 | - |
| Retraction | decided: F3 | re-checked: S1 (and before selection) |
| Licence of the article | decided: F4 | sources used for inputs: S5 |
| Diabetes population / separable subgroup | decided: F5 | - |
| Pharmacological drug nodes | decided: F6 | - |
| Independent trials = RCT-only network | decided from Methods: F7 | re-checked against Results/tables: S2 |
| Outcome (and population) lock | decided: F8 | not re-opened |
| Outcome-specific k (G2) | only if printed in headers/Methods (F9), else DEFERRED | **decided: S3 (usually needs Results)** |
| Follow-up | locked if Methods fix it (F10), else DEFERRED | **decided: S4 (may need Results)** |
| Complete inputs (G1) | never (needs tables/figures/supplements) | **decided: S6** |
| Connected indirect target and M (G2) | never (needs the network plot/Results) | **decided: S7, S8** |
| P, L (G4) | P evidence may be recorded, not decided | **decided: S9, S10** |
| Novelty (G3) | never | **decided: S11** |
| Effort (G5) | never | **decided: S12** |

## 4. Stage F: allowed sources and the fixed step order

**Allowed sections (exhaustive):**
- title, abstract (the whole abstract, including any Results subsection, used for printed counts and designs only; never for effect estimates), keywords;
- bibliographic metadata: Europe PMC core record fields, OpenAlex work record fields, and the fixed retraction-query responses;
- the Methods section;
- the article's printed licence statement.

**Never read in Stage F:** Introduction, Results, Discussion, Conclusions (other than inside the abstract), tables, figures (including any inside Methods), supplements, data-availability statements (read only at S6), funding/declarations, reference lists, protocol registrations and external documents.

**Methods section.**
- The top-level body section(s) whose `sec-type` contains "method", or whose title matches "Methods", "Method", "Materials and methods", "Methods and materials", "Methodology", "Patients and methods", "Subjects and methods" or "Research design and methods". Numbering is optional.
- All nested subsections are included. Tables, figures and supplementary-material elements are always removed.

**Mechanical enforcement.**
- When PMC JATS is available (Europe PMC `fullTextXML`), the screener reads only the output of `extract_stage_f_sections`.
- Otherwise the screener reads the version-of-record HTML or PDF limited to the same sections.
- The F log records `sections_read`. Any value outside {title, abstract, keywords, bibliographic_metadata, methods, licence_statement} invalidates the log.
- If no Methods section can be identified by this rule, the record is F-UNRESOLVED. A required source behind a bot check is also F-UNRESOLVED (reason "blocked"); there is no bypass or mirror cycling.

**Fixed step order.** Steps run in this order. The first step that is not PASS (or not an allowed DEFERRED) is terminal. Every later step is `NOT ASSESSED`. The disposition is F-FAIL for a terminal FAIL, and F-UNRESOLVED for a terminal UNRESOLVED or an expired 20-minute cap. Only F-PASS proceeds.

**F1 Identity and queue.** The visited row is the next unvisited `v3_queue_order`. Its DOI resolves to the article read.

**F2 Article type, non-original items and derivatives.** FAIL if any of the following holds:
- (i) The headers state the item is a protocol, plain-language summary or summary of research, erratum or correction, retraction notice, expression of concern, comment or commentary, letter, reply or response, editorial, conference abstract or preprint.
- (ii) The headers and Methods describe no network meta-analysis conducted by the authors. Examples: a narrative review; an overview or umbrella review of published NMAs; a methods or simulation paper without its own clinical NMA; an economic model that uses another publication's NMA outputs without conducting one; a primary trial.
- (iii) The headers identify an excluded DOI (Appendix A), or its PMID/PMCID, as the work the item summarises, corrects, comments on or replies to.
- Otherwise PASS. IPD and model-based NMAs conducted by the authors PASS here; their inputs are judged at S6.

**F3 Retraction (fixed sources and queries).** Three GET requests are made with the DOI URL-encoded (exact templates in Appendix B):
- (1) Europe PMC search for the DOI, with resultType=core;
- (2) the OpenAlex work record for the DOI;
- (3) Crossref update notices for the DOI (`works?filter=updates:` the DOI, rows=1000).

Verdict (`retraction_verdict`):
- **FAIL** if, on any Europe PMC record whose DOI matches:
  - `pubTypeList` contains "Retracted Publication", "Retraction of Publication" or "retracted-article"; or
  - `commentCorrectionList` contains "Retraction in" or "Partial retraction in"; or
  - the title starts with "Withdrawn" or "Retracted".
- **FAIL** if OpenAlex returns `is_retracted: true`.
- **FAIL** if any Crossref item has an `update-to` entry for this DOI of type retraction, partial_retraction, withdrawal or removal. **UNRESOLVED** if the type is expression_of_concern. Other types (for example correction or erratum) are passed to Stage S as flags.
- **UNRESOLVED (cannot pass)** if:
  - there is an "Expression of concern in" entry;
  - Europe PMC returns no record with this DOI or an unusable response;
  - OpenAlex returns any status other than 200 or 404, or a 200 response without a boolean `is_retracted`;
  - Crossref returns anything other than 200 with a `message.items` list.
- **OpenAlex 404** (DOI not indexed) is a disclosed coverage limitation, not a failure.
- "Erratum in", "Correction in", "Corrected and republished in", "Update in" and "Republished in" are passed to Stage S as flags (S1/S6).
- HTTP retries follow v2 section 3: 5xx only, at 1, 2, 4 and 8 seconds, with a 45-second timeout. There are no credentials.
- The check is repeated at S1 and immediately before selection.

**F4 Licence (exact list).**
- **Accepted:** **CC BY** (any version or jurisdiction port) and **CC0 1.0** only (dispatch 2026-11-02).
- **Rejected:**
  - CC BY-SA, CC BY-NC, CC BY-ND, CC BY-NC-ND and CC BY-NC-SA;
  - publisher-specific licences (for example Elsevier user licence, Wiley terms, "free access" or "open archive");
  - author-manuscript public-access terms, "all rights reserved", or no printed licence;
  - more than one conflicting licence.
- **Source.** The licence must be printed in the article: the JATS license element or ali:license_ref element, or the licence statement on the version-of-record page or PDF. The licence URL governs. Text is used only if no URL is printed (`licence_verdict`).
- Europe PMC or OpenAlex metadata alone never passes F4. If the article's own statement cannot be read, the result is UNRESOLVED.

**F5 Population.**
- PASS if the eligibility criteria in Methods limit the NMA to people with diabetes mellitus of any type (type 1, type 2, gestational, or other specified). This includes diabetes complications in which every participant has diabetes, for example diabetic kidney disease, retinopathy or macular oedema, neuropathy and diabetic foot.
- A mixed population (for example obesity with or without diabetes) PASSes only if Methods pre-specify a separate diabetes-only network or subgroup NMA.
- Prediabetes, impaired glucose tolerance, obesity-only and "at risk of diabetes" populations FAIL.
- The **population lock**:
  - If Methods define more than one diabetes-type network (for example T2D and T1D), lock the one Methods designate as primary. If none is designated, **F5 FAIL** (DECISION_v3 OD-11).
  - Otherwise lock the diabetes population as Methods define it.
  - For a mixed review, lock the Methods-specified diabetes subgroup. If Methods specify more than one diabetes subgroup and designate none as primary, F5 FAIL.

**F6 Drug-node scope (in/out lists).** Each node, as Methods define it, is put in one category.
- **IN (active pharmacological):** a drug named by INN or proposed INN; a drug class made up of such drugs; combinations of such drugs; such a drug plus a non-drug co-intervention.
- **CONTROL:** placebo, no treatment, usual care, background or standard care.
- **OUT:**
  - exercise, diet, behavioural or education, psychological;
  - surgery or procedure (bariatric surgery, laser, vitrectomy);
  - devices, including insulin pumps, CGM and closed-loop systems as delivery systems;
  - acupuncture; herbal or traditional (including Chinese patent medicine) preparations;
  - supplements, vitamins, minerals, probiotics, nutraceuticals, foods or extracts;
  - cell, gene and tissue therapies;
  - investigational products identified only by a sponsor code with no INN or proposed INN (DECISION_v3 OD-16);
  - any other non-drug intervention.
- **PASS** if the network for the locked outcome (or, when Methods define nodes once for all outcomes, the network as defined) has **at least two IN nodes**. Otherwise FAIL (`network_scope_verdict`). Mixed networks with at least two IN nodes PASS.

**F7 Independent trials: the RCT-only rule.** A *trial* is a randomised controlled trial: parallel, factorial, crossover or cluster-randomised. A cluster trial counts once. Quasi-randomised (alternation, date of birth, record number), non-randomised controlled, cohort, case-control, cross-sectional, single-arm, registry and real-world studies are **not** trials and never count toward k. Decision (`design_verdict`):
- PASS if the eligible designs in Methods are RCTs only;
- PASS if Methods explicitly state that the NMA was restricted to RCTs, even where other designs were eligible for some other analysis;
- FAIL if Methods let any non-randomised design into the NMA;
- UNRESOLVED if Methods state no design criterion.

A mixed-design primary NMA is never rescued by switching to an RCT-only sensitivity analysis.

**F8 Outcome lock (designated primary, composites and ranking indices).**
- **Designated primary:** the outcome that Methods (or, if Methods are silent, the abstract) call "primary outcome", "primary endpoint" or "main outcome". If they conflict, Methods prevail. Protocol registrations are not read.
- **Two kinds of outcome:**
  - *participant-level*: measured on participants within each trial, so each trial contributes an effect. This includes participant-level clinical composites such as MACE, kidney composites, or "HbA1c < 7% without hypoglycaemia".
  - *derived index*: computed from pooled NMA outputs or rankings, such as SUCRA, P-scores, mean rank, rank probabilities, the cardiometabolic efficacy index (CEI), benefit-risk or MCDA scores, or clustered rankings.
- **Rules** (`lock_outcome`):
  - **C1.** A single designated participant-level primary, including a composite, is locked. Its components are never used instead, even if the composite later fails k or inputs.
  - **C2.** A single designated derived index, or several designated primaries that are all derived indices, means **F-FAIL**. No component substitution.
  - **C3.** Several designated primaries: drop the derived indices, then apply the hierarchy among the remaining participant-level primaries.
  - **C4.** No designated primary: apply the hierarchy over all participant-level outcomes that Methods list as analysed by NMA for the locked population. A component of a composite can be chosen only if Methods list it as a separately analysed NMA outcome, and only by its own hierarchy position. If there is no such outcome, F-FAIL.
  - **C5.** After the lock there is no substitution, for any reason.
- **Hierarchy (as v2):**
  1. all-cause mortality;
  2. cardiovascular mortality;
  3. MACE;
  4. heart-failure admission;
  5. kidney composite;
  6. HbA1c;
  7. body-weight change;
  8. severe hypoglycaemia;
  9. then the remaining labels, alphabetically by normalised printed label.
- **Synonyms:** Appendix C. Matching rules:
  - A label that matches two tiers belongs to neither.
  - A label with an attainment marker (target, proportion, achiev-, responder, "at least", "percentage of") is not in the HbA1c or weight tiers.
  - "Mortality" or "death" alone means all-cause.
- **Follow-up and population** are locked at the same time: the population by F5, the follow-up by F10.

**F9 k pre-check.**
- Outcome-specific k for the locked outcome and population counts only if printed in the headers or Methods (abstract Results included), under the S3 counting rules. If printed, it must lie within 5-60, otherwise FAIL.
- If a review-wide total of trials, RCTs or studies is printed and is below 5, FAIL, because outcome k cannot exceed it.
- Otherwise DEFERRED to S3. A review-wide total above 60 is not a failure.

**F10 Follow-up pre-check.**
- If Methods fix the time point or time rule for the locked outcome (a time point, a window, or a per-trial rule such as "longest available follow-up"), it is locked: PASS.
- Otherwise DEFERRED to S4.

**Recorded but not decided in Stage F:** journal (for P = 3), OpenAlex `cited_by_count` with its timestamp, and the title/objective sentence naming any comparison of interest (used by S7).

## 5. Stage S: full gates, fixed order

**Allowed sources.** Stage S may read the whole article, tables, figures, the published supplements and a permitted OA copy (MAHMOOD item 12(a)), under v2's source restrictions:
- no login, paywall workaround, bot-check bypass or author contact;
- no primary-trial hunting;
- no digitising, extraction, effect calculation or trial inventory.

Only source locations, headers, captions and qualitative completeness are recorded. Pooled results and aggregate k may be recorded exactly as printed, after the lock.

**Order.** The gates run in this order. The first non-PASS is terminal and later gates are NOT ASSESSED. An S record PASSes only if all twelve PASS within 60 minutes. A Stage F PASS never protects a record in Stage S.

**S1 Retraction re-check.** Same queries and verdict as F3. FAIL and UNRESOLVED are terminal.

**S2 Design re-check.** FAIL if any study contributing to the locked network is described anywhere (Results, tables, supplements) as non-randomised or quasi-randomised.

**S3 Outcome-specific k (counting rule; `k_verdict`).**
- k is the **printed number** of trials, RCTs or studies (studies count as trials only because S2 holds) for the **locked outcome, locked population and locked time point**, printed in text, a table, a caption or a network-plot annotation.
- Counts of articles, reports, publications, comparisons, contrasts, arms, participants or data points are **not** k.
- k is never obtained by counting forest-plot rows or network edges (DECISION_v3 OD-9).
- The original's listing is not split or merged by hunting primary reports.
- If several different values are printed for the same network, **every** one must lie within 5-60. The largest is used for E.
- No printed outcome-specific k (for example only overall-population k when the lock is a subgroup, or only the review total) means **FAIL**.

**S4 Follow-up.**
- If not locked at F10: lock the designated primary time point. If none, the longest outcome-level analysis time that the original reports for the locked outcome network (for example the 52-week network when 12, 24 and 52 weeks are printed). Otherwise the original's printed per-trial rule.
- No printed time rule at all means FAIL.
- No trial-row inventory may supply a time point.

**S5 Licence of every input source.**
- Every file that S6 relies on must be covered by an F4-accepted licence.
- Supplements published with the article are covered by the article licence unless the article or the supplement states otherwise. Any other stated licence must itself be on the list.
- A permitted OA copy carries its own printed licence and must be on the list.
- "Erratum/Correction in" flags: the correction notice is read, and the corrected version governs. If the correction changes the locked network's inputs and the corrected inputs are not printed in full, S6 fails.

**S6 Complete inputs (v2 G1, operational).** For every trial counted in k, at the locked outcome, population and time point, one complete input set is printed in a licence-covered source:
- (a) per-trial contrast effects with a labelled SE or 95% CI for every trial comparison; or
- (b) per-arm mean, SD or SE, and analysed n (continuous outcomes); or
- (c) per-arm events and analysed denominators (binary outcomes); or
- (d) per-trial log HR with SE or CI (time-to-event outcomes).

Requirements on every set:
- Each value is attributable to a trial label and to the original's node labels: whole-trial/report, treatment/control and shared-arm mapping.
- Multi-arm trials supply all arms, or all contrasts plus the information needed for the shared-arm covariance. Invented covariance means FAIL.
- Numerals inside images are acceptable (FEASIBLE-IMAGE) only if printed as numerals. Reading values off graphical marker positions is digitising and is not allowed.

Any of the following means **FAIL**:
- a trial with missing inputs, or inputs that are uncertain or illegible;
- inputs available only on request or non-public;
- inputs only reconstructable by imputation, incidence-rate reconstruction or inversion of pooled outputs;
- league tables or treatment-level results alone.

**S7 Connected indirect target (`choose_target`).**
- Nodes and direct edges come from the printed network plot or an explicit statement for the locked network. An unlabelled or unreadable network means UNRESOLVED.
- A qualifying pair has both nodes **IN** (F6), **no direct edge**, and lies in the same connected component (connections through control nodes count).
- If the title or objective sentence names qualifying pairs (both nodes, or both nodes' classes when the nodes are classes), the alphabetically earliest of those is the target. Otherwise the alphabetically earliest qualifying pair is the target. "Alphabetical" means casefolded printed labels within the pair, then across pairs.
- Nodes and doses are not merged.
- If the original reports the locked network as disconnected, FAIL. If there is no qualifying pair, FAIL.
- The target is recorded before its pooled estimate is looked at.

**S8 Method addition M (v2 definitions).**
- **M = 2:** the original prints no numerical estimate for the target pair anywhere (main text, league table, forest plot or supplement), and performs no whole-trial omission for the target.
- **M = 1:** the target estimate is printed, the original does not perform whole-trial omission for it, and the original's text contains a sentence that names a target node (or its comparisons) and states that the evidence is sparse, from few trials, from a single trial, or has high heterogeneity or inconsistency for that node or comparison.
- **M = 0:** anything else, including an equivalent omission already in the original. M = 0 means FAIL.

**S9 Profile P (v2 routes, fixed sources).**
- **P = 3:** the journal is *Diabetes, Obesity and Metabolism*, ISSN 1462-8902 or 1463-1326, from the Europe PMC journal metadata.
- **P = 2:** a readable clinical guideline (a citing work in the S11 OpenAlex or Europe PMC citation lists, of guideline, consensus or standards-of-care type) cites this review in its body text, not only in the reference list.
- **P = 1:** OpenAlex `cited_by_count` >= 100 at the S9 timestamp.
- **P = 0:** none of these. The highest route applies. A missing counter is unknown, not zero. P = 0 means FAIL.

**S10 Live question L (fixed lexicon).**
- **L = 2:** a sentence anywhere in the original names a target node, or the target comparison, and contains one of: controvers-, conflicting, debate-, uncertain-, unclear, unresolved, inconsistent, "no consensus", "practice-changing", "change practice".
- **L = 1:** a sentence names a target node and mentions ongoing, registered or underway trials, or says that head-to-head trials are lacking or needed.
- **L = 0:** neither. L = 0 means FAIL.
- The passage and its location are recorded. L is never scored from any recalculated magnitude, direction, significance or ranking.

**S11 Novelty (v2 G3, unchanged).** Europe PMC and OpenAlex citing works, with the v2 templates (Appendix B), the v2 pagination and coverage rules, and the v2 equivalence definition and adjudication. Partial coverage is disclosed. A wholly failed index is UNRESOLVED. An established equivalent, or an unresolved plausible exact equivalent, means FAIL.

**S12 Effort G5 (deterministic formula; `effort_hours`).**
- E in hours:
  - E = 2.50 (reproduction 1.00 + whole-trial omission 0.50 + figure 0.50 + letter 0.50)
  - + k x (0.02 text/table inputs, or 0.04 image-only inputs)
  - + k x 0.01 checking
  - + 0.25 each for: multi-arm trials present; arm-to-contrast conversion needed; inputs split over two or more files.
- Rounded **up** to 0.25 h.
- PASS if E <= 4.0.
- Independent extraction, adjudication and human verification are excluded, as in v2.
- The formula and constants were accepted as drafted (dispatch 2026-11-02).
- **Calibration disclosure:** the constants were set so that a 50-trial network with text inputs and no complications sits exactly at the 4.0 h cap. That calibration rests on a single human estimate (4.0 h). It has not been validated against timed runs, so E is a fixed rule, not a measured effort.

## 6. Selection, reporting and the stop rule (as v2)

**Selection.** Among the Stage S passers only, rank lexicographically:
1. higher M;
2. higher L;
3. higher P;
4. lower E;
5. earlier v3 queue order;
6. DOI.

The first is the provisional primary and the second is the fallback (`select_passers`). The retraction check is re-run on both just before selection. One passer means a provisional primary and "no cleared fallback".

**If nothing passes, stop and report the v3 feasibility failure.** No v4, new seed, new query, re-retrieval, 41st F visit, 6th S screen or endpoint switch follows without a new explicit decision by Mahmood and a new registration and release.

**Logs.** These are separate from any analysis:
- the F log (one JSON record per visit: order, DOI, every F step's status, reason and location, `sections_read`, minutes, cap flag, disposition);
- its sha256;
- the S log (all twelve gates, plus k, M, L, P and E with components, minutes and disposition);
- novelty and retraction request records;
- the selection.

Statuses are PASS, FAIL, UNRESOLVED, NOT ASSESSED and DEFERRED (F9/F10 only). No trial-level rows are recorded.

## 7. Executable handoff and later pipeline

**The script.** `screen_P04_v3.py` is frozen with this text (`DRAFT = False`). It makes no network calls.
- `--build` (the Stage F queue) and `--stage-f-extract` (given one JATS file, it writes the Stage F sections of that article) run only if `check_release` passes:
  - the release URL is exactly the `P04-screen-v3` tag (the v1 and v2 tags are rejected);
  - the DOI is a doi.org URL or `PENDING`;
  - the local prereg and script bytes match the supplied sha256 values.
  Otherwise the script stops before reading any file.
- Outputs go only to a child of the script's directory and are never overwritten.
- `--print-constants` and `--dry-build` (to a folder outside the package) are offline checks and never produce a screening queue.
- The script verifies local hashes and syntax only. pc2 must first verify the public release, its server timestamp and the archived bytes.

**Command template for pc2.** The three `RELEASE-TIME-FIELD` values are filled from the public release and its FREEZE.json. They are the only unfilled values in this text.
~~~text
python screen_P04_v3.py --build --screen-release-url https://github.com/mahmood726-cyber/usecase-preregistrations/releases/tag/P04-screen-v3 --screen-release-doi RELEASE-TIME-FIELD:zenodo-doi-url-or-PENDING --prereg-sha256 RELEASE-TIME-FIELD:prereg-sha256-from-FREEZE.json --script-sha256 RELEASE-TIME-FIELD:script-sha256-from-FREEZE.json --v1-frame supporting/v1_archive/frame_P04.jsonl --v2-frame supporting/v2_archive/frame_P04.jsonl --output-dir out/v3_run_01
~~~

**Testing.** `supporting/synthetic_test_screen_P04_v3.py` holds 31 synthetic tests. Every behaviour change was written as a failing test first. The first draft started from a stub (28 tests, 0 passing). Applying the 2026-11-02 decisions gave 31 tests with 15 failing before the code changed. All 31 pass on the final bytes. Planted defects each turn the suite red: Results allowed in Stage F; v2-visited DOIs not excluded; CC BY-NC-SA accepted; CC BY-SA accepted; N_S = 10; Crossref retractions ignored; duplicate groups kept; the v2 tag accepted as a v3 release.

**Later pipeline (unchanged from v2 section 7).** A selected pair enters candidate-specific v4 F1-F6 freeze criteria, REDTEAM2, use-case freeze and a separate GitHub/Zenodo release before any extraction. F5 human verification follows MAHMOOD_DECISIONS item 4. No real-data analysis happens before synthetic validation passes. There are no clinical recommendations, ranking or "first" claims, no changes to original numbers, and no allegation of error.

## Appendix A. The 31 excluded DOIs

| Group | DOI |
|---|---|
| pre-v1 | 10.1111/dom.15725; 10.1186/s12933-023-02035-8; 10.1007/s00125-024-06144-1; 10.1136/bmj-2023-076410; 10.1111/1753-0407.70192 |
| v1 title-triaged (21; v1 ranks 1-21) | 10.1007/s40123-026-01377-2; 10.1186/s13613-025-01471-x; 10.1186/s12962-020-00208-w; 10.1038/s41598-024-63316-0; 10.3389/fendo.2026.1891173; 10.1038/s41598-021-89620-7; 10.1186/s13098-026-02226-9; 10.3389/fpubh.2023.1201818; 10.1007/s40123-025-01247-3; 10.3389/fpubh.2022.959073; 10.7759/cureus.100927; 10.1186/s13643-022-01986-5; 10.1097/md.0000000000031823; 10.3389/fendo.2023.1282584; 10.3389/fphar.2023.1226778; 10.1186/s12912-025-04065-x; 10.3389/fphar.2021.751496; 10.3389/fmed.2025.1721311; 10.1111/jdi.13603; 10.1007/s40122-025-00789-5; 10.1007/s13300-023-01459-5 |
| v2-visited (v2 orders 1-5) | 10.1007/s40123-026-01434-w; 10.3389/fendo.2022.895458; 10.3389/fendo.2025.1462104; 10.1097/md.0000000000028365; 10.1111/dom.70742 |

## Appendix B. Fixed request templates

`{DOI}` and the other names in braces are filled per candidate at screening time, with URL-encoding. They are runtime substitution fields, not unfinished text. The forms are unchanged from v2, except that the retraction query uses resultType=core and Crossref is added.

~~~text
F3/S1 retraction (all three required):
https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%22{DOI}%22&format=json&resultType=core&pageSize=1000&cursorMark=%2A
https://api.openalex.org/works/https://doi.org/{DOI}
https://api.crossref.org/works?filter=updates%3A{DOI}&rows=1000
S11 novelty (v2 G3):
https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%22{DOI}%22&format=json&resultType=lite&pageSize=1000&cursorMark=%2A
https://www.ebi.ac.uk/europepmc/webservices/rest/{SOURCE}/{ID}/citations?format=json&page=1&pageSize=1000
https://api.openalex.org/works/https://doi.org/{DOI}
https://api.openalex.org/works?filter=cites%3A{OPENALEX_W_ID}&per-page=100&page=1
Stage F full text (read only through extract_stage_f_sections):
https://www.ebi.ac.uk/europepmc/webservices/rest/{PMCID}/fullTextXML
~~~

## Appendix C. Outcome hierarchy synonyms (normalised, whole-phrase match)

| Tier | Phrases |
|---|---|
| 1 all-cause mortality | all cause mortality; all cause death; death from any cause; overall mortality; total mortality; label exactly "mortality" or "death" |
| 2 cardiovascular mortality | cardiovascular mortality; cardiovascular death; cv death; cv mortality; death from cardiovascular causes |
| 3 MACE | mace; major adverse cardiovascular event(s); 3 point mace; 3p mace; 4 point mace |
| 4 heart-failure admission | hospitalization/hospitalisation for heart failure; heart failure hospitalization/hospitalisation; hhf; heart failure admission; hospital admission for heart failure |
| 5 kidney composite | kidney composite; renal composite; composite kidney/renal outcome; composite kidney/renal endpoint |
| 6 HbA1c | hba1c; hb a1c; a1c; glycated haemoglobin/hemoglobin; glycosylated haemoglobin/hemoglobin |
| 7 body weight | body weight; weight change; weight loss; change in weight |
| 8 severe hypoglycaemia | severe hypoglycaemia/hypoglycemia; level 3 hypoglycaemia/hypoglycemia |

## Appendix D. Fingerprints of inherited inputs (local bytes; the release FREEZE.json covers every package file)

| File | sha256 |
|---|---|
| supporting/FIELD_USE_CASE_PROTOCOL.md | 4f6e05206d46059cdbb9bcc6c8a34ac47ebad6e7bb7483e5a5398b6037ce9bac |
| supporting/MAHMOOD_DECISIONS.md | 571469f9c90265398f479ac322ea426977674ee14806ee14fd9f90abeac8028f |
| supporting/v1_archive/frame_P04.jsonl | fef70cafb5a84c329c62b8b8122d2c634e5a43301455c1c5065a7bbe4053063f |
| supporting/v2_archive/frame_P04.jsonl | 3563a7efe93c2f74d6a2718fef647ec5a0132cfc21e32870f0fe69fda7277d1d |
| supporting/v2_archive/PREREG_P04_screen_v2_DRAFT.md (released v2 text) | 414a84ef1b39fcda426a925e0f877de22df52a5b9e91be5f9394116a09c7c71a |
| supporting/v2_archive/screen_P04_v2.py (released) | a1bc0d4f146bbdbd7c4c210cbe71de50b76f525953515e0f68e8c2b6b586617b |
| supporting/v2_archive/FULLSCREEN_P04_v2.jsonl | ee16a950f6305d4402b077e4a6cf2cf39afeb502d5ce3c698692f68d2a879508 |
| supporting/v2_archive/SCREEN_NOTES_P04_v2.md | 4c90388b082767a077c4c64b490c187f9b9614979e9f9760b2b8228074496f97 |
| supporting/v2_archive/SELECTION_P04_v2.json | b7b453d519fd77dcdbcc696f76ec821e18f3c8e5722ff5b9a342023a0e1735b4 |
| supporting/v2_archive/release_receipt_P04_v2.json | e65fa2c7b9823728aa80d56d5a1d372bce72f183713be8ce697149be644f0813 |

## Appendix E. The 57 rows removed by the declared filter stage (section 2.3; offline dry build)

The list was produced mechanically by `screen_P04_v3.py`. It is a metadata classification, not a screening judgement. The drafter checked it for false positives against titles only: all 46 protocol hits are protocols. The exact-title duplicate rule removes both members of each pair (stricter reading, DECISION_v3 OD-6).

| v2 order | v1 rank | DOI | Rules |
|---|---|---|---|
| 11 | 32 | 10.1371/journal.pone.0297488 | protocol |
| 16 | 37 | 10.1186/s13643-026-03153-6 | protocol |
| 21 | 42 | 10.1136/bmjopen-2019-034680 | protocol |
| 24 | 45 | 10.1371/journal.pone.0306336 | protocol |
| 40 | 61 | 10.1097/md.0000000000022755 | protocol |
| 42 | 63 | 10.2196/45178 | protocol |
| 65 | 86 | 10.1007/s40123-026-01440-y | derivative_or_version_of_excluded:10.1007/s40123-025-01247-3; comment_reply_letter |
| 70 | 91 | 10.1136/bmjopen-2019-034481 | protocol |
| 71 | 92 | 10.21203/rs.3.rs-2674982/v1 | preprint_doi_prefix; preprint_record_source |
| 78 | 99 | 10.1097/md.0000000000021568 | protocol |
| 80 | 101 | 10.2337/dc22-2491 | comment_reply_letter |
| 84 | 105 | 10.1136/bmjopen-2022-066491 | protocol |
| 87 | 108 | 10.1097/md.0000000000018198 | protocol |
| 122 | 143 | 10.1136/bmjopen-2017-017644 | protocol |
| 133 | 154 | 10.1136/bmjopen-2024-093342 | protocol |
| 136 | 157 | 10.1097/md.0000000000028946 | protocol |
| 152 | 173 | 10.1186/s13643-018-0706-9 | protocol |
| 155 | 176 | 10.1101/2024.06.23.24309242 | preprint_doi_prefix; preprint_record_source |
| 158 | 179 | 10.1136/bmjopen-2018-023206 | protocol |
| 159 | 180 | 10.1097/md.0000000000020461 | protocol |
| 162 | 183 | 10.1097/md.0000000000017353 | protocol |
| 170 | 191 | 10.1136/bmjopen-2020-048259 | protocol |
| 182 | 203 | 10.1097/md.0000000000024967 | protocol |
| 198 | 219 | 10.3390/ijerph19031622 | protocol |
| 218 | 239 | 10.2147/dmso.s502743 | erratum_correction |
| 228 | 249 | 10.1097/md.0000000000016038 | protocol |
| 233 | 254 | 10.1097/md.0000000000029154 | protocol |
| 241 | 262 | 10.1097/md.0000000000028086 | protocol |
| 264 | 285 | 10.1097/md.0000000000029152 | protocol |
| 289 | 310 | 10.1097/md.0000000000025788 | protocol |
| 293 | 314 | 10.1097/md.0000000000025615 | protocol |
| 294 | 315 | 10.1136/bmjopen-2023-072960 | protocol |
| 304 | 325 | 10.1136/bmjopen-2018-028430 | protocol |
| 336 | 357 | 10.1136/bmjopen-2018-022271 | protocol |
| 344 | 365 | 10.1016/j.ijcrp.2026.200597 | comment_reply_letter |
| 350 | 371 | 10.1136/bmjopen-2023-075783 | protocol |
| 362 | 383 | 10.1136/bmjopen-2024-098205 | protocol |
| 368 | 389 | 10.21203/rs.3.rs-2305051/v1 | exact_title_duplicate_group; protocol; preprint_doi_prefix; preprint_record_source |
| 371 | 392 | 10.1136/bmjopen-2022-065287 | protocol |
| 378 | 399 | 10.1136/bmj.o109 | exact_title_duplicate_group |
| 381 | 402 | 10.1007/s40123-026-01439-5 | derivative_or_version_of_excluded:10.1007/s40123-025-01247-3; comment_reply_letter |
| 384 | 405 | 10.1097/md.0000000000028386 | protocol |
| 387 | 408 | 10.1097/md.0000000000024812 | protocol |
| 398 | 419 | 10.1097/md.0000000000028283 | protocol |
| 425 | 446 | 10.1186/s13643-024-02558-5 | exact_title_duplicate_group; protocol |
| 432 | 453 | 10.1097/md.0000000000022564 | protocol |
| 433 | 454 | 10.1136/bmjopen-2025-113896 | protocol |
| 444 | 465 | 10.1136/bmj.m4573 | exact_title_duplicate_group |
| 458 | 479 | 10.1097/md.0000000000023963 | protocol |
| 489 | 510 | 10.1136/bmjopen-2023-078100 | protocol |
| 499 | 520 | 10.3389/fmed.2025.1610141 | protocol |
| 507 | 528 | 10.1136/bmjopen-2019-029073 | protocol |
| 511 | 532 | 10.1136/bmjopen-2020-038970 | protocol |
| 512 | 533 | 10.1186/s13643-017-0455-1 | protocol |
| 514 | 535 | 10.1371/journal.pone.0354259 | protocol |
| 529 | 550 | 10.1101/2023.03.13.23287105 | preprint_doi_prefix; preprint_record_source |
| 538 | 559 | 10.1007/s12325-024-02831-y | erratum_correction |
