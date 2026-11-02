# P02 screening v3 (P02-screen-v3): two-stage screen

**Approved for freeze and release; not yet released.** Drafted and finalized 2026-11-02. Every item that was open in the draft (D1-D14) was decided on 2026-11-02 by dispatch, under Mahmood's delegation; the decisions are quoted in `supporting/DECISION_v3_2026-11-02.md`, and the text below cites them as "decision Dn". Nothing may be retrieved, screened, scored, selected or extracted before the public **P02-screen-v3** GitHub release exists (section 10.3). The file keeps its working basename, `PREREG_P02_screen_v3_DRAFT.md`, because the script and the release receipt check that exact file name (as v2 did). In this approved copy the script's `DRAFT_ONLY` is False; `--run` still refuses without a matching release receipt.

Paper P02; target journal *Observational Studies*; field: human observational epidemiology and nutrition dose-response meta-analysis, including behavioural and occupational exposures. Use case: a dose-unit plausibility audit with a linear-only re-analysis question. No candidate data or anticipated numerical finding may inform selection.

## 0. Status, authority and binding documents

- **Drafting authorized** by Mahmood (relayed via dispatch, after the P02-screen-v2 STOP) with three requirements: (1) a larger candidate pool; (2) feasibility judged only from headers (title, abstract, keywords, bibliographic metadata), the Methods section and the licence statement, never from Results, Discussion, tables, figures or supplements; (3) every gate's operational rules fixed in this text before any screening, so that no judgement call is left to the screener.
- **Decisions (2026-11-02).** Dispatch, under Mahmood's delegation, decided N_F, N_S, the caps, the declared metadata filter, the licence rule, the effort formula and the recency rule, and directed that every other open item be settled by the stricter reading. The record is `supporting/DECISION_v3_2026-11-02.md`. The public release is the screening precondition.
- **Binding documents, cited by hash:**

| Document | Location in the v3 package | SHA-256 |
|---|---|---|
| Field use-case protocol (Mahmood, 27 Oct 2026) | `supporting/FIELD_USE_CASE_PROTOCOL.md` (byte-identical copy of `pipeline/FIELD_USE_CASE_PROTOCOL.md`) | `4f6e05206d46059cdbb9bcc6c8a34ac47ebad6e7bb7483e5a5398b6037ce9bac` |
| Archived complete v1 frame, 1,798 rows, seed 2026102802 | released in P02-screen-v2 as `P02_screen_v2/supporting/v1_archive/frame_P02.jsonl`; byte-identical copy in this package at `supporting/v1_archive/frame_P02.jsonl` (decision D13) | `c2aad90cf12b746b9de40dd5a88113ab43eccddb23c406f33008e53a7eff1a04` |
| P02-screen-v2 protocol (released) | tag `P02-screen-v2`, commit `8435ff98731e2b5384d94c65027a4c36bd7ea7b4`, DOI 10.5281/zenodo.23883100 | `754d83f8cc16f472673fcd8cc695882ff07731acddf01d63f8211409062f734d` |
| P02-screen-v2 script (released) | same tag | `dad7dde624b2d64eff0b8e3ce6af880b8c4807a7590d2b345ae1f5f048c4137e` |

The v2 text called the field protocol binding for G4 but linked to a path absent from the release (v2 ambiguity A4). v3 carries the byte-identical copy above; the script refuses a copy with any other hash (`verify_field_protocol`).

## 1. What v1 and v2 established

**V2 ended correctly in STOP / feasibility failure:** 5 of 5 FAIL at G1, 0 passes, no primary, no fallback. V1 ranks 14 and 16 were left NOT SCREENED.

| v2 order | v1 rank | DOI | Recorded G1 failure (v2 ledger) |
|---:|---:|---|---|
| 1 | 8 | 10.1186/s12889-018-5041-5 | Methods-designated comparison is highest-versus-lowest; dose-response is secondary (A1). |
| 2 | 9 | 10.1186/s12884-020-03036-1 | Designated synthesis k = 4, cubic spline; field doubtful (A2, A3). |
| 3 | 10 | 10.3389/fphys.2022.955702 | Primary cohort study with an appended non-dose-response pooled OR (A3). |
| 4 | 12 | 10.1002/fsn3.72357 | RCT-only. |
| 5 | 13 | 10.1016/j.eclinm.2026.103847 | RCT-only; restricted cubic splines. |

Together with v1 (5 full screens, 0 passes) and the five pre-v1 screens (Liang, Li, Hackshaw, Descatha, Suksatan; none cleared), **15 full screens have produced no pass.** Most failures were decided by design, target or field facts that the Methods state. A structural check of the v2 sources (section 11) found that the decisive v2 G1 locators lay inside the Stage F view defined below for four of the five; the fifth (v1 rank 9) failed on k and model statements printed in Results, and under v3 it fails earlier on the field rule (A3). v3 is built on that observation: a cheap, Methods-only feasibility stage over many records, then full screens only for the survivors.

## 2. What changes and what does not

The three authorized changes are: a larger pool (section 3), a two-stage design with a Methods-only feasibility stage (section 4), and fully operational gate rules (sections 5-6). Every other change is listed with its reason in `supporting/CHANGES_v2_to_v3.md`; each is tighter than v2 or neutral. **No v2 gate is loosened.** In particular: the date window, the k range 5-60, the observational-only design rule, the complete-printed-input rule, the linear-only rule, all three powerful criteria, the four-hour effort cap, the 60-minute per-candidate cap, the G3 novelty procedure and equivalence definition, the selection order, the single fallback, the stop rule, and the subsequent freeze/extraction pipeline are retained.

## 3. Pool, exclusions and queue (no new seed, no retrieval)

### 3.1 Source

The pool is drawn from the **archived complete v1 frame** in its original seeded order (ascending SHA-256 of `2026102802|P02|screen|<doi>`, then DOI). **No new seed and no new API retrieval.** The script verifies the frame's bytes against `c2aad90c...a1a04`, the 1,798-row count, every row's rank, order hash and strict order, and ranks 1-16 against the v1 triage inventory (the unchanged v2 B2-S contract).

No protocol-text reason prevents reuse of the archived frame: v1 and v2 both require the first complete frame to be frozen and never resampled; the v2 Option B fresh frame was not chosen and was never run; and the registered window (2016-10-28 to 2026-10-28) is unchanged. Recency (decision D9): the registered window is kept exactly as drafted and is not widened. Every pool record is dated 2016-11-03 or later, so all satisfy the field protocol's "recent (<=10 years)" on 2026-11-02, the scheduled Stage F date; the earliest record in the Stage F window is dated 2016-12-02, so the window stays within ten years for any Stage F run completed before 2026-12-02.

### 3.2 Pool definition

**Pool = v1 frame ranks 17-1,798 (1,782 records never triaged), in v1 seeded order.** Ranks 1-16 are outside the pool: 14 have a v1 or v2 disposition; ranks 14 and 16 were triaged TO_FULL_TEXT in v1, left outside the v2 batch, and **remain NOT SCREENED** (decision D2).

### 3.3 Declared metadata filter stage (counted and reported)

This is a **declared, named stage of the protocol** (decision D6), executed by the script before any screening. It applies the five rules below, in this order (first match), identically to every pool record. **It is counted and reported:** the run manifest's `declared_filter_stage` field states the stage's input count, the number removed by each rule, the total removed and the number remaining; every removed record is listed by DOI and v1 rank with its rule in the exclusions file; and section 3.5 reports the dry-build values. It is therefore **not** the "second uncounted title/abstract filter" that v2 section 3 prohibits: that prohibition is aimed at an unlogged screener triage that silently shrinks the denominator, whereas this stage is fixed in advance, mechanical, counted and published. It removes only items that could not pass G1 (prior dispositions and their duplicates, retraction-flagged items, non-original items); it never admits or rescues a record. Removed records do not consume a Stage F disposition; the Stage F denominator is the first 40 queue records that remain after the stage.

1. **`prior_disposition`**: the DOI has any v1 or v2 disposition. The 19 DOIs:
   - pre-v1: 10.1186/s13643-025-02800-8, 10.1016/j.envint.2020.105739, 10.1136/bmj.j5855, 10.1016/j.envint.2020.105746, 10.3390/nu14010174;
   - v1 full screens: 10.1016/j.eclinm.2023.102308, 10.7717/peerj.20570, 10.1038/s41598-019-38723-3, 10.1093/ajcn/nqz178, 10.1038/s41598-020-76306-9;
   - v1 terminal title triage: 10.1136/bmjopen-2026-117508, 10.1136/bmjopen-2018-026232, 10.7762/cnr.2024.13.3.186, 10.1007/s40279-023-01966-2;
   - v2 full screens: 10.1186/s12889-018-5041-5, 10.1186/s12884-020-03036-1, 10.3389/fphys.2022.955702, 10.1002/fsn3.72357, 10.1016/j.eclinm.2026.103847.
2. **`duplicate_title_of_dispositioned`**: the record's title key equals the title key of a dispositioned record. Title key = HTML-unescape twice, remove tags, Unicode NFKD, drop combining marks, casefold, keep only `[a-z0-9]`. Reference titles: the frame titles of the 14 dispositioned v1/v2 rows, and the verified titles of Liang, Li and Hackshaw (`CANDIDATES_P02.md`). Descatha and Suksatan have no locally verified title and are matched by DOI only; any other version of them found during Stage F fails as F-G0-DUPLICATE (section 5).
3. **`metadata_reports_retracted`**: the Europe PMC pubType contains `retracted publication`, `retraction of publication` or `retraction notice`. (V1's frame builder read only `isRetracted`-style keys and missed these; this applies v2's existing "explicit retraction metadata" exclusion.)
4. **`non_original_pubtype`**: the pubType contains any of `published erratum`, `correction`, `protocol`, `clinical trial protocol`, `letter`, `comment`, `reply`, `editorial`, `news`, `preprint` (decision D6, with the stricter readings: `letter` and `preprint` are both removed).
5. **`non_original_title`**: the title matches one of these case-insensitive patterns (fixed verbatim in `screen_P02_v3.py`):
   - correction notice: begins with optional "author/publisher", then correction, corrigendum, erratum, errata or addendum, followed by ":", "to", "for" or end;
   - retraction notice: begins with retraction, retracted, "notice of retraction", "withdrawn:" or "expression of concern";
   - protocol: contains "study protocol"; or "protocol for a/an" followed by systematic, scoping, umbrella, updated, living, network or meta-analysis; or "review protocol", "meta-analysis protocol", "research protocol"; or ends with ": a" or ": an", then at most four words, then "protocol";
   - plain-language summary: contains "plain language summary" or "plain-language summary";
   - letter/reply: begins with "re:", "reply to", "in reply", "response to", "comment on", "commentary on" or "letter to".

A word such as "protocol" in an exercise-protocol title does not match (synthetic test). A non-original item that escapes these rules fails in Stage F as F-G0-NONORIGINAL and consumes a disposition, as in v2.

### 3.4 Duplicates inside the pool

Records whose title key equals that of an earlier queue record are **kept in the queue and flagged** (`title_duplicate_of_queue_pos`). If reached, the flagged record receives **F_FAIL F-G0-DUPLICATE without opening any source** and consumes a disposition (v2: "a duplicate-review determination during screening consumes a slot"). The script refuses a Stage F ledger that gives such a record any other disposition.

### 3.5 Offline dry build (not a run)

Built offline from the archived frame into a scratch folder; no network request; nothing screened:

| Count | Value |
|---|---:|
| Frame rows | 1,798 |
| Ranks 1-16 outside the pool (14 dispositioned, 2 NOT SCREENED) | 16 |
| Pool before exclusions (ranks 17-1,798) | 1,782 |
| `prior_disposition` / `duplicate_title_of_dispositioned` | 0 / 0 |
| `metadata_reports_retracted` | 9 |
| `non_original_pubtype` | 36 |
| `non_original_title` (all 27 inspected: every one is a review protocol) | 27 |
| **Stage F queue (pool after exclusions)** | **1,710** |
| Stage F window (queue positions 1-40) | v1 ranks 17-58 |
| Title-duplicate flags in the queue / in the window | 0 / 0 |
| **Declared filter stage, as reported in `declared_filter_stage`** | input 1,782; removed: prior_disposition 0, duplicate_title_of_dispositioned 0, metadata_reports_retracted 9, non_original_pubtype 36, non_original_title 27 (total 72); remaining 1,710 |
| Queue records without a PMCID (no fixed Stage F source) | 0 |

The queue file is deterministic (no timestamps). Its SHA-256 is **`d5dba663e5247cf834ef3a3978b49db5d4406642d546410e6f06a5756d98fd58`**; the exclusions file is `8a267854ac0598ade386e73c8ff4d335dcccc5341be3185de4caa9b571db7f8a`. **The authorized run must reproduce the identical queue hash; any difference is a STOP** (decision D13).

## 4. Two-stage design

### 4.1 Sequence (all numbers fixed here)

1. Public P02-screen-v3 release exists (section 10). Nothing before it.
2. **Stage F (feasibility).** Visit queue positions 1, 2, 3, ... in order. Each visited record receives exactly one disposition, **F_PASS** or **F_FAIL** with its registered code. **Stop at the first N_F = 40 dispositions (decision D3)** (positions 1-40), or at queue exhaustion. No skipping, no reordering, no early stop for a promising pass, no 41st record.
3. **Lock Stage F.** Write the Stage F ledger, record its SHA-256 and the UTC time, and run `derive_stage_s_queue` (which refuses a ledger with skips, reordering, early stop, overrun, unregistered codes, or a flagged duplicate that did not fail). No Stage S work starts before the lock.
4. **Stage S (full gates).** Take the F_PASS records in Stage F order. Full-screen **at most N_S = 5 (decision D4)**, in that order, each to a final PASS or FAIL. Do not stop early for a pass. F_PASS records beyond the fifth stay **F_PASS - NOT SCREENED**; they are never activated, including after a later primary or fallback failure.
5. **Selection (section 7), then the stop rule (section 8).**

### 4.2 Stage F evidence: what may be read

The Stage F screener reads **only**:

- the record's frame metadata (DOI, title, journal, pubType, dates, PMCID);
- the two retraction responses (G0-R below);
- the **Stage F view** produced by `screen_P02_v3.py --stage-f-view` from the fixed source. The view contains: article title, journal, publisher, article type, identifiers, publication dates, subject labels, abstract(s) (graphical, teaser and table-of-contents abstracts removed), keywords, the licence/permissions statement, and the **Methods** section.

**Fixed Stage F source:** the Europe PMC full text `https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML` for the frame's PMCID (decision D12). HTTP policy is v2's: 60-second timeout; up to five attempts at the identical URL for HTTP 5xx with 1, 2, 4, 8-second backoff; no retry of a bot check, 401/403, other non-5xx, non-XML or transport failure; every attempt logged with UTC times, status and response SHA-256. The full XML is saved with its hash for Stage S; **the Stage F screener does not open it**, only the view.

**Methods section, as the script identifies it (no judgement):** (i) every top-level body section whose `sec-type` contains "method", or whose title, after removing a leading section number, is one of: materials and methods, method(s), methods and materials/analysis/design, methodology, patients/subjects/participants and methods, study/research design and methods. (ii) If none, every top-level section positioned before the first section titled results, findings, discussion, conclusion(s) or summary, excluding sections titled introduction, background, rationale, aim(s), objective(s) or purpose. (iii) If neither yields a section, `methods_found = false`. Within the kept sections, **every figure, table, supplementary-material, graphic and media element is removed, including floats inside a paragraph**; reference lists and back matter are never included.

**Never read in Stage F:** Introduction/Background, Results, Discussion, Conclusions, any table, figure or supplement, references, the publisher's page, any other article, guideline, registry or web search. A fact visible only there is **PENDING_S** and cannot fail or pass a record in Stage F.

### 4.3 Stage F outcome rules

- Items are checked in the fixed order of section 5 (G0, source, G1, G4 linear/audit, G2 licence/input type). The **first failing item ends the record** with its code; later items are recorded `NOT ASSESSED - TERMINAL FAILURE`.
- **F_PASS** requires every F-decidable item to pass and lists every PENDING_S item for Stage S. A pending item is never a pass.
- **F_FAIL codes** (registered in the script): F-G0-RETRACTION, F-G0-NONORIGINAL, F-G0-DUPLICATE, F-SRC-UNAVAILABLE, F-SRC-NO-METHODS, F-G1-NOT-MA, F-G1-TARGET, F-G1-FIELD, F-G1-DESIGN, F-G1-K, F-G4-NONLINEAR, F-G4-AUDIT, F-G2-LICENCE, F-G2-INPUT-TYPE, F-TIMEOUT.
- **Stage F timer:** at most **20 elapsed minutes per disposition (decision D5)**, starting before the first request for that record. Unresolved at the cap: F-TIMEOUT. Pause only for a documented external interruption.

### 4.4 Stage S evidence and timer

Stage S may read the full article (all sections, tables, figures), its own supplements, erratum notices, and the section 6 novelty sources, under v2's G2 source rules (the review's own main text, numbered figures/forests or published supplement, via the publisher, Europe PMC/PMC or an openly licensed repository copy of that review; no login, payment, bypass, OCR dataset, reconstruction or author contact). **Combined cap: 60 elapsed minutes per candidate including its Stage F time (decision D5)**, so a candidate whose Stage F took 14 minutes has 46 Stage S minutes. Unresolved gates at the cap fail. **Stage S may not change the Stage F target, revisit a Stage F failure, or reopen Stage F.**

### 4.5 Gate map: which stage decides what

| Gate component | Decided in | Evidence | Stage F can FAIL? | Stage F can PASS? |
|---|---|---|---|---|
| G0-R retraction | F | two fixed metadata queries | yes | yes (CLEAR) |
| G0-N non-original / duplicate | build, then F | metadata, headers, Methods | yes | yes |
| Source available, Methods locatable | F | fixed source, view | yes | yes |
| G1-M original aggregate meta-analysis | F | headers, Methods | yes | yes |
| G1-T target identification | **F (final)** | Methods (title only as the stated tie rule) | yes | yes |
| G1-DR target is a dose-response synthesis | F | Methods | yes | yes |
| G1-F field scope | F | title, abstract, keywords, Methods | yes | yes |
| G1-D design | F (eligibility), **S confirms the designated synthesis's study list** | Methods; S: tables/forests/supplement | yes | only when eligibility is observational-only or separation is stated; otherwise PENDING_S |
| G1-K k of the designated synthesis | **S** (needs Results/tables/forest) | printed k | only if headers/Methods print that synthesis's k outside 5-60 | no |
| G4-L linear-only | F preliminary, **S confirms** | Methods; S: Results, figures, tables, supplement | yes (unconditional nonlinear statement) | preliminary only |
| G4-A audit fit and score | F | Methods (S only for the conversion-factor rule) | yes | yes |
| G2-L article licence | F | licence statement | yes | yes |
| G2-I input type | F | Methods | yes | PENDING_S otherwise |
| G2-C complete printed inputs, supplement licences | **S** (needs tables/figures/supplements) | permitted sources | no | no |
| G4-T threshold plausible | S | Introduction, Methods, Discussion | no | no |
| G4-P high profile | S | journal metadata, section 6 citation lists, OpenAlex count | no | no |
| G4-Q live question | S | Introduction, Discussion, Conclusions | no | no |
| G5 effort | S | formula inputs | no | no |
| G3 novelty | S (last) | section 6 procedure | no | no |

## 5. Operational definitions of every gate

Each rule below is applied as written. In request templates, `<doi>`, `<DOI>`, `<PMCID>`, `<W_ID>`, `<source>/<id>` and `<TITLE>` are per-record substitution variables (as in v2), not unfilled values. Quotations recorded in a ledger are at most 25 words, with a locator (section id / paragraph id from the view or the full XML). No study-level number is copied, paraphrased, calculated or tested at any stage of screening; printed aggregate counts, model wording and licence text may be recorded exactly.

### G0-R. Retraction status (closes A5)

At the start of each Stage F turn (after the timer starts), make exactly these two requests with the record's normalized, URL-encoded DOI:

1. Europe PMC: `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%22<doi>%22&format=json&resultType=core&pageSize=25`
2. OpenAlex: `https://api.openalex.org/works/https://doi.org/<doi>`

The status is computed by `retraction_status()`:

- **CLEAR** only if both return a record whose DOI equals the queried DOI; OpenAlex `is_retracted` is boolean `false`; the Europe PMC `pubTypeList` is present and contains none of `retracted publication`, `retraction of publication`, `retraction notice`; and no `commentCorrectionList` entry has a type beginning "Retraction in" or containing "Expression of concern". If Europe PMC returns several records with that DOI, a flag on any of them counts.
- **RETRACTED** (any retraction flag), **CONCERN** (expression of concern) or **UNVERIFIED** (missing record, DOI mismatch, missing pubTypeList, non-boolean OpenAlex flag, or a failed request after the HTTP policy) all give **F_FAIL F-G0-RETRACTION** (decision D8).
- "Erratum in" / "Correction in" entries are recorded; in Stage S, each erratum notice joins the source inventory and its corrections govern.
- The same two requests are repeated for the selected primary and fallback immediately before selection is reported; a status other than CLEAR then fails that candidate.

### G0-N. Non-original items and duplicates

- **F-G0-NONORIGINAL** if the metadata or Stage F view shows the item is a protocol or registration of a planned review, a plain-language summary, an erratum or correction, a letter, comment, reply or editorial, a conference abstract, or a preprint version.
- **F-G0-DUPLICATE** if the record is flagged under section 3.4; or the view states that it is a republication, translation or secondary version of another article of the same synthesis; or it is another version (preprint, accepted manuscript, translation) of a record already visited or dispositioned. An **update** (a new search and a new synthesis) is not a duplicate.

### Source checks

- **F-SRC-UNAVAILABLE**: no PMCID in the frame; or the fixed source returns non-200, non-XML, a non-JATS document or a bot check (`stage_f_view` refuses these). Never bypass; no alternative route in Stage F.
- **F-SRC-NO-METHODS**: `methods_found = false`.

### G1-M. Original aggregate meta-analysis

Pass if the headers or Methods state that the authors searched for studies and quantitatively pooled estimates from at least two studies. **F-G1-NOT-MA** if the first analysis the Methods describe is of the authors' own participant data (a primary study, even with an appended meta-analysis: v2 rank 3); a modelling, simulation or projection study; an umbrella review that pools only published meta-analytic estimates without its own study-level input set; or an individual-participant-data pooling (not an aggregate synthesis).

### G1-T. Primary target identification (closes A1 and A2)

Applied only to the Stage F view; the target fixed here is final.

1. **Designation.** In the Methods, in document order, find the first sentence containing any of: "primary outcome", "primary end point", "primary endpoint", "main outcome", "primary exposure", "main exposure", "primary analysis", "main analysis", "primary aim", "primary objective", "main objective". The outcome and exposure it names form the designated pair. If it lists several outcomes or exposures, **the first listed is designated (Methods order resolves co-primary items)**. If it names an outcome only, the exposure is the first exposure named in the article title. **The abstract and title never override Methods order.**
2. **No designating sentence.** The designated pair is the first exposure-outcome pair for which the Methods' statistical-analysis text describes a pooled analysis. If that text covers outcomes collectively ("for each outcome"), take the first outcome listed in the Methods' eligibility/outcome text; likewise for the exposure. If the Methods list none, take the first exposure and the first outcome named in the article title.
3. **Granularity.** If the designated exposure is a group (for example "dairy products") and the Methods describe pooled analyses only for its components, the target exposure is the first component named in the Methods' description of the target comparison. Population: the overall population if the Methods describe an overall analysis, otherwise the first stratum named. Design strata: if the Methods state separate pools by design, the first-described observational pool.
4. **Comparison (unnamed comparisons).** The target comparison is **the first analysis the Methods describe for the designated pair**; word order inside a sentence counts as document order. If that first analysis is highest-versus-lowest, extreme-category, any-versus-none, ever-versus-never or above-versus-below a cut-off, **F-G1-TARGET**. If the Methods label the pair's dose-response analysis secondary, additional, subgroup, sensitivity or exploratory, **F-G1-TARGET**, even if it is described first.
5. **Not locatable.** If no pair can be fixed by steps 1-4, F-G1-TARGET (ambiguous target). No secondary outcome, other exposure or larger synthesis is substituted.

### G1-DR. What counts as a dose-response synthesis

A pooled synthesis, by the review's authors across at least two studies, of the relation between a **quantitative** exposure level (amount, frequency, duration, concentration or cumulative dose in physical or count units) and the outcome, using study-specific trend estimates or at least three exposure levels per study including the reference: for example Greenland-Longnecker/Orsini generalized least squares, one- or two-stage dose-response meta-analysis, variance-weighted least-squares trend, or pooled per-unit estimates. **Not dose-response:** highest-versus-lowest, any-versus-none, ever-versus-never, above-versus-below a cut-off, separate pooling of each category against the reference without a trend across levels, meta-regression of study-level mean exposure on effect, and any dose-response analysis of a single study. If the target comparison is not a dose-response synthesis: **F-G1-TARGET**.

### G1-F. Field scope (closes A3)

Classify the designated exposure and outcome **as named in the Methods** (title and abstract only to complete a name). **The OUT list prevails over the IN list; anything not on the IN list is OUT (decision D11).**

**IN exposures**
- E1 Diet and nutrition: foods, food groups, beverages (including alcohol, coffee, tea, sugar-sweetened drinks), nutrients and dietary components, dietary patterns or indices, dietary supplements as habitually consumed by free-living people, and biomarkers of intake measured in blood, urine or tissue (not anthropometry).
- E2 Behaviour measured in free-living people: physical activity, fitness, sedentary time, screen time, sleep, tobacco and nicotine use, cannabis and other recreational substance use.
- E3 Occupation: working hours, shift or night work, occupational physical load, occupational exposure to a chemical, physical or biological agent.
- E4 Environment: ambient or indoor air pollutants, noise, heat or temperature, non-therapeutic radiation, environmental chemicals and metals (water, soil, food contaminants), greenness or built-environment measures.

**OUT exposures:** physiological or anthropometric characteristics (body mass index, waist, weight change, height, birth weight, blood pressure, heart rate, and circulating non-intake biomarkers such as lipids, glucose or uric acid) and socioeconomic or psychosocial characteristics (decision D11, stricter reading); medicinal products and vaccines (dose, duration or adherence, even when studied observationally); medical, surgical, obstetric or anaesthetic procedures and their timing, frequency or volume (for example the gestational week of an elective caesarean section); therapeutic radiation; delivered interventions or programmes (exercise or training prescriptions, behavioural programmes, acupuncture or device parameters); health-service characteristics (hospital or surgeon volume, staffing, waiting time); genetic variants; non-human exposures.

**OUT outcomes:** O1 perioperative, postoperative or post-procedural outcomes or complications (post-surgical prognosis); O2 efficacy, response or adverse effects of a medical treatment; O3 diagnostic or prognostic test accuracy; O4 pharmacokinetic, laboratory-method or non-human outcomes. All other human health outcomes (incidence, prevalence, mortality, disease course, continuous health measures) are IN.

**F-G1-FIELD** if the exposure or the outcome is OUT, or the population is not human.

### G1-D. Observational versus RCT design

An observational study is one in which the exposure was not assigned by the investigators: prospective or retrospective cohort, case-cohort, nested case-control, case-control or cross-sectional. **The review's own design label governs; the screener never relabels** (a trial population counts as observational only where the review labels the study a cohort). Mendelian randomization estimates are not observational exposure studies for this protocol.

Stage F, from the Methods eligibility criteria:
- only randomized/controlled trials, interventional, experimental or Mendelian randomization designs eligible: **F-G1-DESIGN**;
- only observational designs eligible: passes Stage F;
- both eligible, and the Methods state that the designated synthesis is restricted to observational studies or that designs are pooled separately: passes Stage F (the target is the observational pool, G1-T step 3);
- both eligible and the Methods state that designs are pooled together for the target: **F-G1-DESIGN**;
- both eligible and the Methods are silent on pooling, or the Methods state no eligible designs: **PENDING_S**.

Stage S: every study contributing to the designated synthesis (its forest, table or supplement listing) must carry an observational design label from the review. Any study labelled RCT, trial, intervention or quasi-experimental: **FAIL G1** (inseparable mixture). Any contributing study without a design label: **FAIL G1** (unverifiable).

### G1-K. k of the designated synthesis

k is the number of independent studies or cohorts contributing to the designated dose-response synthesis, **as printed by the original** for that synthesis; never counted from rows. Required: 5 <= k <= 60.

- **Stage F** fails (**F-G1-K**) only if the abstract or Methods print a count in the same sentence as the designated dose-response analysis (named as dose-response, per-unit, linear trend or the target pair with one of those words) and that count is outside 5-60. A review-wide count is never a designated-synthesis k and neither passes nor fails a record. Otherwise **PENDING_S**: k usually needs Results, a table or a forest plot, which Stage F never reads.
- **Stage S**: a printed k for the designated synthesis within 5-60 passes. No printed k, conflicting printed values for that same synthesis, a printed count of reports where the review states that some reports contribute several cohorts without printing the cohort count, or a value outside 5-60: **FAIL G1**.

### G4-L. Linear versus nonlinear (linear-only requirement)

- **Linear:** each study's log relative risk modelled with a single slope in dose in the reported unit, and a pooled slope or per-unit estimate.
- **Nonlinear:** any model allowing curvature or a change of slope: restricted cubic or other splines, fractional polynomials, quadratic or polynomial terms, piecewise, segmented or threshold models, non-parametric categorical curves, any transformation of dose (for example log dose), and any test of nonlinearity or "P for nonlinearity", whatever its result.
- **Stage F:** if the Methods or abstract state, for the target or for all/each exposure-outcome pairs without excluding the target, that a nonlinear model was fitted or nonlinearity was tested: **F-G4-NONLINEAR**. A conditional statement ("if nonlinearity was detected", "where data were sufficient") or silence on model form: **PENDING_S**. A statement of a linear model only: preliminary pass.
- **Stage S:** pass only if a linear pooled estimate is reported for the designated target and **no** nonlinear model, curve, test or P value for that target appears anywhere in the article or its supplements. Otherwise **FAIL G4**.

### G4-A. Audit fit and its score (Stage F)

From the Methods (the abstract only for the unit):
1. **Dose-assignment rule:** the Methods state how a dose was assigned to each category (median, mean or midpoint) **and** how open-ended categories were handled. Either part missing: **F-G4-AUDIT**.
2. **Physical unit:** the common unit of the target exposure's dose is stated (for example g/day, servings/day with a gram equivalent, hours/week, ug/m3). Missing: **F-G4-AUDIT**.
3. **Score** (fixed in Stage F; Stage S may not raise it): **2** if the Methods state the conversion or standardization procedure for the target exposure (conversion factors, or a named standard); **1** if the Methods state one common unit and describe no conversion. If the Methods mention a conversion without its factors or a named standard: **PENDING_S**, and Stage S looks only in the supplement for those factors (found: 2; not found: **FAIL G4**).

### G2-L. Licence (article in Stage F, supplements in Stage S)

- **Article (Stage F):** pass only if the licence statement identifies **CC BY** (any version or jurisdiction port, by name or by a `creativecommons.org/licenses/by/` URL) or **CC0** (`publicdomain/zero`). **F-G2-LICENCE** for NC, ND or SA variants, publisher-specific open-access licences, "free to read" wording, no licence, or conflicting statements (decision D7).
- **Every data source used for inputs** (the article, each supplement, any repository copy of the review) must itself be CC BY or CC0 under this rule; G2-C admits no other source of inputs.
- **Each needed supplement (Stage S):** covered only if it carries its own CC BY or CC0 statement, or the article's licence or data statement extends CC BY or CC0 to supplementary or additional files or to the data made available in the article. Otherwise **FAIL G2** (unresolved reuse condition).

### G2-I and G2-C. Inputs

- **G2-I (Stage F):** **F-G2-INPUT-TYPE** if the Methods state that the target synthesis used only study-reported continuous or per-unit estimates, or that category-level cases and person-time or totals were not extracted. Otherwise PENDING_S.
- **G2-C (Stage S), unchanged from v2:** for every study in the designated synthesis, the review's own permitted sources must print category doses or bounds with the original assignment rule, physical units/denominator, the reference category, adjusted relative effects with CIs, **cases and total persons or person-time in every required category, including the reference**, and an unambiguous mapping to the designated synthesis. Any required field missing for any contributing study: **FAIL G2**. Record locations, column headers and FEASIBLE-TEXT or FEASIBLE-IMAGE only. Curve coordinates, per-increment forests and study totals do not replace category inputs. No OCR/digitization dataset, primary-study reconstruction, count imputation, author data or post hoc subset. The printed sources must support one physical exposure quantity, reference system and a source-supported unit map. A bot-blocked required source: **FAIL, blocked; NOT FEASIBLE**, never bypassed.

### G4-T. Threshold plausible (Stage S)

Pass if the Introduction, Methods or Discussion contains a sentence that (a) contains one of: threshold, plateau, saturation, ceiling, J-shaped, U-shaped, nonlinear or non-linear, curvilinear, "level off" or "levels off", optimal level/dose/intake, upper limit, safe limit, tolerable upper intake; and (b) names the target exposure (its Methods term or the title term) in the same sentence or the preceding sentence of the same paragraph. Record the quotation and locator. None: **FAIL G4**.

### G4-P. High profile (Stage S; operationalizes the field protocol's "widely cited, guideline-cited, or published in the target journal itself")

Levels as v2; highest qualifying level used; no extra credit for counts.
- **Level 3, guideline-cited:** among the citing records retrieved by the section 6 citation lists, a record whose title contains guideline(s) or recommendation(s), or whose Europe PMC pubType contains "guideline" or "practice guideline", cites the review **substantively**: the review's reference appears in a sentence citing at most three references that states a finding (direction or estimate) on the review's topic. Only open full text is read; no paywall is bypassed.
- **Level 2:** the journal title in the metadata is *Observational Studies*.
- **Level 1, widely cited:** the OpenAlex `cited_by_count` at the section 6 DOI lookup is >= 100 (record value and UTC date) **and** a substantive citation (same sentence rule) appears in a citing record whose title or pubType marks it as a guideline, consensus statement, position or scientific statement, systematic review, umbrella review, evidence review or report, technical report or health technology assessment.
- No level met: **FAIL G4**. Institutional branding alone is insufficient. **No source outside the section 6 lists is searched** (no free web or guideline search).

### G4-Q. Live question (Stage S)

From the original's Introduction, Discussion or Conclusions; highest level met; quotation and locator recorded.
- **Level 3, controversy:** a sentence containing controvers*, debate*, conflicting, inconsistent, contradictory, disagree*, unresolved, uncertain or unclear, that names the target exposure and cites at least one reference.
- **Level 2, practice-changing claim:** a Discussion or Conclusions sentence stating that the findings support or inform a change to a guideline, recommendation, dietary or public-health advice, limit or policy concerning the target exposure.
- **Level 1, ongoing trials:** the original cites at least one ongoing trial (a registration number, or the words "ongoing trial(s)" or "under way") on the target exposure.
- None: **FAIL G4**. A relevance claim is never constructed from a computed effect.

### G5. Effort (Stage S)

The four-hour cap on subsequent Codex work (extraction/checking, reproduction, app/R comparison, figure, short write-up) is applied by a **fixed formula in quarter-hours** (`effort_upper_bound()`) (decision D10):

| Component | Quarter-hours |
|---|---|
| Extraction and checking | 2 + ceil(k / 4) + 2 if any required input is image-only + 1 per distinct supplement file needed + 2 if the Methods state any unit conversion for the target |
| Reproduction | 3 |
| App/R comparison | 2 |
| Figure | 1 |
| Short write-up | 2 |

Pass if the total is <= 16 (four hours) **and** the work needs no reconstruction, imputation or author contact. The screener records the formula inputs and may not substitute its own estimate, higher or lower. Calibration: the only prior human estimate available, pre-v1 Liang (k = 12, unit conversions, one supplement), was "3.5-4 h"; the formula gives exactly 16 (4.0 h). With no add-ons the formula passes k <= 24. Independent extractor and human packet time are additional and disclosed (v2).

**Disclosure (decision D10):** the formula and its constants were accepted as drafted. Its calibration rests on a **single human estimate** (pre-v1 Liang, upper bound 4.0 h); no other estimate or measured completion time was available, so its agreement with real effort is unvalidated.

### G3. Novelty (Stage S, last)

**Unchanged from v2 section 6**, including the equivalence definition; the requests run only for Stage S candidates that have passed every other gate, within the combined 60-minute cap:

1. Europe PMC identity: `query=DOI:"<doi>"`, `format=json`, `resultType=lite`; confirm title/DOI; then `https://www.ebi.ac.uk/europepmc/webservices/rest/<source>/<id>/citations?format=json&page=1&pageSize=1000`, all pages to the reported total or a logged failure; several source IDs for one DOI: use all, deduplicate citing records by DOI, otherwise source/id.
2. OpenAlex: `https://api.openalex.org/works/https://doi.org/<doi>`; confirm DOI/title and W identifier; record `cited_by_count`. Then `https://api.openalex.org/works?filter=cites:<W_ID>&per-page=100&page=1`, page 2, 3, ... until an empty page, at most 10,000 records (100 pages). Completion requires an empty page, a stable count and no repeated records; beyond the ceiling or with a nonempty page 100, record INCOMPLETE_LIMIT; HTTP/access/schema/count/duplicate failures record FAILED_BLOCKED, never zero citations.
3. Europe PMC search with each template: `"<DOI>" AND (reanalysis OR "re-analysis" OR "dose unit" OR harmonisation OR harmonization OR plausibility)` and `"<TITLE>" AND (reanalysis OR "re-analysis" OR "dose unit" OR harmonisation OR harmonization OR plausibility)`.
4. Review every retrieved title/abstract for possible equivalence; inspect permitted full text for plausible matches; log index, exact request, UTC time, IDs, counts, pagination/error status and a reason for each possible match.

**Equivalence (v2, unchanged):** an equivalent prior re-analysis uses the same underlying synthesis, fixed outcome/comparison and substantially the same dose-unit plausibility or source-supported dose harmonisation audit with consequent re-analysis; different software or terminology does not establish a difference; a different synthesis, an ordinary exposure association or a spline analysis alone is not equivalent; an equivalent audit already reported in the original leaves no contribution. Both indexes must be attempted and at least one must give a usable result; failure of both, or an unresolved plausible equivalent, is NOT CLEARED: **FAIL G3**. Coverage gaps are disclosed, never reported as negatives.

## 6. The v2 ambiguities and how v3 closes them

| ID | v2 ambiguity | v3 decision rule | Worked example (v2 record, already dispositioned; not re-screened) |
|---|---|---|---|
| A1 | Primary aim names outcome and exposure but not the comparison scale. | G1-T step 4: the target comparison is the first analysis the Methods describe for the designated pair; highest-versus-lowest first, or dose-response labelled secondary or subgroup: F-G1-TARGET. | v1 rank 8 (dairy, hip fracture): the primary aim (Sec3/Par14), the highest-versus-lowest pooling (Sec5/Par16, Sec6/Par19) and the "subgroup and dose-response" wording are all in Methods or the abstract, so v3 gives **F_FAIL F-G1-TARGET in Stage F**. The v2 permissive reading (first dose-response synthesis) is no longer available, and the alternative G4 evidence (Results Sec14/Par32) is never read. |
| A2 | Abstract lists one primary outcome first, Methods another. | G1-T step 1: Methods order resolves co-primary items; abstract and title never override it. | v1 rank 9: neonatal death (first in Methods Sec4/Par26) is the target, not NICU admission (first in the abstract). Under v3 the record fails earlier, on A3 below. |
| A3 | Is the timing of an obstetric procedure, or perioperative prognosis, within the P02 field? | G1-F closed IN list; procedures and their timing are OUT exposures; post-procedural outcomes are OUT (O1); OUT prevails. | v1 rank 9: exposure = gestational week of elective caesarean section (title, Methods): **F-G1-FIELD**. v1 rank 10: BMI is an OUT exposure (decision D11) and postoperative oxygenation impairment after aortic surgery is an O1 outcome: **F-G1-FIELD** (it would also fail F-G1-NOT-MA: the Methods' first analysis is the authors' own 227-patient cohort, s2-6/p1). |
| A4 | The binding field protocol was cited by a path absent from the release. | Byte-identical copy in `supporting/`, cited by SHA-256 `4f6e0520...bac`; the script refuses another hash; each criterion is quoted and operationalized (section 9). | Not record-specific. |
| A5 | No independent retraction check; a frame flag of `false` is not clearance. | G0-R: two fixed queries (Europe PMC core, OpenAlex work), both required; anything but CLEAR fails in Stage F; re-checked for the selected pair. The 9 frame records whose pubType already reports retraction are excluded before screening (section 3.3). | All five v2 records carry `UNVERIFIED` in the v2 ledger; under v3 each would have been checked before any other gate. |

**Calibration of the Stage F view on the v2 sources** (structure only; locators checked, no text re-judged): `stage_f_view` located the Methods of all five v2 sources by title. The v2 decisive G1 locators inside the Stage F view: rank 8, Sec3/Par14, Sec5/Par16, Sec6/Par19 (Methods) and the abstract; rank 10, s2-6/p1 and s2-6/p2 (Methods); rank 12, sec-0005/p2-p3 (Methods) and the abstract; rank 13, sec2.1.1/p0055 and sec2.1.4/p0070 (Methods). Rank 9's k = 4 and spline statements (Sec20, Table 3/4) are in Results and are **not** visible in Stage F; only its target locator (Sec4/Par26) is.

## 7. Selection

Only Stage S candidates passing every gate (G0-G5) enter selection, after all Stage S screens are complete. Rank by this **lexicographic** order (unchanged from v2; implemented by `select()`):

1. Audit fit: 2 before 1 (G4-A score).
2. Profile: 3 (guideline-cited), 2 (target journal), 1 (widely cited).
3. Live question: 3 (controversy), 2 (practice-changing claim), 1 (ongoing trials).
4. Smaller G5 total in quarter-hours.
5. Smaller v1 seeded order hash (`order_sha256`, seed 2026102802), then DOI.

The first is the primary; the second is the **only fallback**. Fix both outcomes and source routes before any extraction. One pass: primary only, "fallback absent". No failing candidate is promoted; no third candidate is activated if the fallback later fails.

## 8. Stop rule

- **Zero F_PASS among the 40 Stage F dispositions: STOP after Stage F** and report every disposition as a feasibility failure.
- **Zero Stage S passes: STOP** and report every disposition.
- In either case **no v4 follows without a new explicit Mahmood decision.** No widened window, changed source, relaxed gate, new seed, extra Stage F record, extra Stage S screen or activation of an F_PASS - NOT SCREENED record is authorized.
- A failed retrieval never counts as a zero-candidate result. Every result, including "robust", stays reportable. No clinical recommendation, priority claim or named allegation of error follows from screening.

## 9. The binding field protocol, criterion by criterion

| Field protocol text (`supporting/FIELD_USE_CASE_PROTOCOL.md`) | Checkable v3 rule |
|---|---|
| "High profile: widely cited, guideline-cited, or published in the target journal itself." | G4-P levels 1-3, fixed procedures. |
| "Live question: a known controversy, a practice-changing claim, or ongoing trials." | G4-Q levels 3-1, fixed sentence rules. |
| "Dose-response (P02): a published linear-only analysis of an exposure where a threshold is plausible." | G1-DR + G4-L (linear-only, F then S) + G4-T (threshold plausible). |
| "selection uses only the original paper's published features" | Sections 4-5: only the original article, its supplements and the fixed metadata/citation sources; no calculation on candidate data. |
| "one meta-analysis per paper; data from the forest plot, a table or the supplement only; k <= 60; no contacting authors; about half a day of Codex time" | One designated synthesis (G1-T); G2-C permitted sources; G1-K 5-60; no contact; G5 four-hour formula. |
| "Screen up to 5 candidates on these criteria, then pick the strongest." | Conforms: at most 5 candidates are screened on these criteria in Stage S (N_S = 5, decision D4). Stage F gives feasibility dispositions only, as v1's title triage did. The field protocol text is unchanged. |
| "Recent (<=10 years), open-access (CC-BY or similar)" | Registered window unchanged and not widened (decision D9); G2-L CC BY or CC0 only (decision D7). |
| "k >= 5 is acceptable for others" (dose-response) | G1-K lower bound 5. |
| "Novelty check ... PubMed and Google Scholar" | Replaced by the already authorized Europe PMC + OpenAlex procedure (Mahmood decision 3; Google Scholar showed a bot check on 2026-10-28 and is not revisited). |
| "Pre-registration (before any run) ... GitHub release ... Zenodo" | Section 10. |
| Reproducibility-audit mode, "P02: dose-unit plausibility screen" | G4-A audit fit and score. |

## 10. Ledgers, execution and release

### 10.1 Ledgers

- **Stage F ledger** (one row per disposition, positions 1-40 in order): queue position, v1 rank, DOI, order hash, retraction requests (URLs, UTC times, statuses, response hashes) and status, source request record and XML hash, Stage F view hash, `methods_found` and rule, each Stage F item's result (PASS, FAIL, PENDING_S, or NOT ASSESSED - TERMINAL FAILURE) with locators and short quotations, the fixed target (exposure, outcome, comparison, population, design stratum), audit-fit score or pending, disposition, code, elapsed minutes and interruptions.
- **Stage S ledger:** as v2's screening ledger (every gate result and reason, novelty coverage and equivalence disposition, power scores, effort formula inputs and total, elapsed time including the Stage F minutes, final disposition, fallback rank), plus the Stage F ledger hash.
- Study-level numbers are never recorded. Published pooled statements, k and model wording may be recorded exactly, never recalculated.

### 10.2 Script (`screen_P02_v3.py`, standard library, no network in any mode)

- `--print-queries`: prints the fixed request templates.
- `--dry-build --v1-frame FRAME --out-dir FOLDER`: offline queue build labelled `DRY_BUILD_NOT_A_RUN`, reporting the declared filter stage counts; refuses to write into the package folder or to overwrite.
- `--stage-f-view XML --out JSON`: writes the Stage F view.
- `--run --release-record RECEIPT --v1-frame FRAME --out-dir FOLDER`: checks the release receipt (refused without a matching one) and writes `stage_f_queue_P02_v3.jsonl`, `stage_f_exclusions_P02_v3.jsonl`, `run_manifest_P02_v3.json`. Accept the run only if the queue hash equals section 3.5's.
- Functions used during screening: `retraction_status`, `derive_stage_s_queue`, `effort_upper_bound`, `select`.

### 10.3 Release steps

1. **Done (2026-11-02).** Decisions recorded in `supporting/DECISION_v3_2026-11-02.md` and applied to this text, the script constants and the tests (test-first where behaviour changed).
2. **Done (2026-11-02).** Package assembled with the byte-identical v1 frame copy under `supporting/v1_archive/`; `DRAFT_ONLY = False`; file names kept.
3. **Done (2026-11-02).** Synthetic suite run on the package bytes; FREEZE.json written and verified against the bytes; secret scan run.
4. **Not yet done.** Commit, push to `main` of `mahmood726-cyber/usecase-preregistrations`, create release tag `P02-screen-v3`, record the server `publishedAt`, verify released bytes against the local hashes; Zenodo DOI when minted (PENDING allowed at screening).
5. Receipt fields (`check_release`). The release-time fields `approved_at_utc`, `released_at_utc` and `zenodo_doi` are **filled only from the public release** and do not exist yet; every other field is fixed now: `paper "P02"`, `version "P02-screen-v3"`, `ordering_seed "2026102802"`, `decision_by "Mahmood"`, `decision "APPROVE_V3_TWO_STAGE_SCREEN"`, nonempty `decision_evidence`, `approved_at_utc` <= `released_at_utc`, `n_f`, `n_s`, `f_cap_minutes`, `candidate_cap_minutes` equal to the script constants, `v1_frame_sha256`, `field_protocol_sha256`, `script_sha256`, `prereg_sha256`, `github_release_url .../releases/tag/P02-screen-v3`, `zenodo_doi` (DOI or PENDING).

## 11. Validation and current limits

- `synthetic_test_screen_P02_v3.py`: 26 synthetic tests (generated fixtures, mocked network). Red before implementation (26 errors against a stub), green after (26/26); 13 planted defects each turned the suite red. Finalization (2026-11-02), test-first: the changed assertions (N_S = 5, approved-copy lock, declared filter counts) were red (3 failures, 1 error), then 26/26 (`supporting/synthetic_screen_P02_v3_checks.md`).
- Offline dry build on the real archived frame (section 3.5); offline structural check of `stage_f_view` on the five v2 sources (section 6). Neither is a screen.
- Not established: live API behaviour, actual Stage F pass rate, source feasibility, novelty, candidate scores, app/R parity or any statistical result. N_F = 40 is a fixed budget (decision D3), not a power calculation: no prior data predict the Stage F pass rate.
- No candidate was screened, no Stage F view of any pool record was produced, and no network request was made in drafting or finalization.

## 12. Subsequent pipeline (unchanged from v2 section 9)

A selected primary or fallback enters the same v4 freeze-criteria, REDTEAM2, separate analysis freeze/release and extraction pipeline (F1-F6). Selection alone does not clear extraction. Binding verification text (MAHMOOD_DECISIONS.md item 4), retained exactly:

> Human verification: humans check headline rows, a seeded 5% of the other rows (at least 1), and only the fields still disputed after a third-model adjudication plus a fourth AI re-check (agy, different family). If the sample error is over 2%: a full AI re-extraction plus a human re-check of the headline rows. Packets are about 30 minutes or less; at most one per person per week across all papers (COAUTHOR_LOAD.md); Mahmood is in the rota; a packet not returned in 7 days is reassigned.

No changed original number, author contact, outcome switching or real-data model search is allowed.
