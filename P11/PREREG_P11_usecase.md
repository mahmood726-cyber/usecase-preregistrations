# P11 pre-registration v4: single-study influence in digital-health evidence

**DRAFT for freeze; no extraction or analysis has been performed**

2026-10-28. P11, influence-diagnostics app. Target: *Journal of Medical Systems* (TASK_PAPER/screening; manuscript.txt does not confirm submission destination). **Primary selected; F1–F6 satisfied: freeze candidate.** [BLOCKERS_P11.md](BLOCKERS_P11.md) contains NONE. This is not a release or authorization to extract.

## 1. Chosen meta-analysis and fallback

**Primary:** Cevasco KE, Morrison Brown RE, Woldeselassie R, Kaplan S. Patient Engagement with Conversational Agents in Health Applications 2016–2022: A Systematic Review and Meta-Analysis. *Journal of Medical Systems*. 2024;48:40. [DOI](https://doi.org/10.1007/s10916-024-02059-x). CC BY 4.0.

Target-journal placement, the engagement question and published I² **64.3%** justify influence diagnostics prospectively. Published **k=14** meets the 5–60 limit; heterogeneity does not establish influence.

**Fallback:** Zhu Y, Gu X, Xu C. Effectiveness of telemedicine systems for adults with heart failure: a meta-analysis of randomized controlled trials. *Heart Failure Reviews*. 2020;25:231–243; online 2019. [DOI](https://doi.org/10.1007/s10741-019-09801-5). CC BY 4.0. The screening record's dated publisher citation metric supports profile; mortality and I² **49%** support relevance. Existing sensitivity work limits incremental contribution and requires scope clearance.

Retain the primary unless source, model/input or equivalent-prior-analysis eligibility fails. The fallback is FEASIBLE-IMAGE but its prior-analysis eligibility is **not cleared**. Primary source/input/reproduction or prior-analysis ineligibility may activate it only after its own feasibility and novelty checks clear, **before fallback extraction or diagnostics**. If it cannot clear those checks, stop without replacement; if its reproduction gate fails, stop. The primary route may freeze while fallback clearance is pending. Once diagnostics begin, sensitivity, robustness, workload or app/R disagreement cannot trigger switching. Log active analyst time against **four hours total across both candidates**, excluding queues; no reset. Exhaustion means incomplete work, not another candidate.

## 2. Fixed outcome and estimand

| Item | Primary | Fallback |
|---|---|---|
| Outcome/comparison | End-of-study retention, chatbot versus published controls, overall Figure 2 | All-cause mortality, telemonitoring versus usual care, Figure 2e follow-up |
| Diagnostic scale | Log-RR | Log-OR |
| Published target | **0.99 (95% CI 0.95–1.03)** | **OR 0.75, 95% CI 0.62–0.90** |
| Published k | **14** | **15** |
| Original reproduction | Random effects, ML, metafor/R | Fixed MH per panel; RevMan 5.2 |

Fallback Methods describes random effects, but Figure 2e explicitly prints **M-H, Fixed, 95% CI**. Prospectively prioritize that outcome-specific label; never search across models. [SOURCE_CHECK_P11.md](supporting/SOURCE_CHECK_P11.md), §§2–5, supplies verbatim evidence, all NOT STATED items and the single software-default attempt, including normal CIs and zero-cell rules. It is normative and must accompany the release; no release has occurred. Primary pooling is explicitly log-RR; fallback MH uses counts with default log-OR inference, not arithmetic natural-ratio averaging.

## 3. Sources and analytical inputs

Primary **FEASIBLE**: 10916_2024_2059_MOESM1_ESM.docx, Appendix D: Author, Control arm type, Chat Retain, Chat Loss, Control Retain, Control Loss. Use retained/lost counts directly; totals are derived sums, without repeating administrative adjustments. Figure 2 supplies Author(s) and Year, RR [95% CI], Weight cross-checks.

Fallback **FEASIBLE-IMAGE**: 10741_2019_9801_Fig2b_HTML.jpg, middle panel **e**: Study or Subgroup; Experimental/Control Events and Total; Odds Ratio, M-H, Fixed, 95% CI; Weight. Table 1 supplies follow-up/comparison context.

Use counts exclusively for the complete published synthesis, one independent contrast per trial. No CI-derived variances, alternate follow-ups, new arm combinations, coordinate digitization or selective row removal. Missing inputs, dependence or contradictory mapping fail the candidate. Rows serve only their source meta-analysis. Source hashes/readability/precision are in SOURCE_CHECK. No author contact, login, paywall workaround or bot-check bypass.

## 4. Extraction and verification

**MAHMOOD_DECISIONS.md item 4, verbatim:**

Human verification: humans check headline rows, a seeded 5% of the other rows (at least 1), and only the fields still disputed after a third-model adjudication plus a fourth AI re-check (agy, different family). If the sample error is over 2%: a full AI re-extraction plus a human re-check of the headline rows. Packets are about 30 minutes or less; at most one per person per week across all papers (COAUTHOR_LOAD.md); Mahmood is in the rota; a packet not returned in 7 days is reassigned.

**Operational implementation (unchanged burden):**

After release, Codex and agy independently extract identical source versions, blind to each other. Agy uses a different model family from Codex; read back and record its actual model-family log line.

For every discrepancy:

1. A third model adjudicates against the source, recording location.
2. A fourth AI pass, agy using a family different from the adjudicator's, checks each adjudicated field against the source.
3. Only fields still disputed go to humans.

P11 co-authors and/or Mahmood record initials, date, source location and decision in VERIFICATION_LOG.csv. They check:

- Every headline-driving row: any deletion changing CI null-category; standardized change ≥0.5; every app-flagged row; and maxima of absolute DFFITS, Cook's distance, weight share or standardized change, **including all ties**.
- A seeded 5% sample of remaining rows, minimum one if any remain. Seed **2026102811**. Ascending lowercase SHA-256 of UTF-8 “2026102811|P11|<row key>”; take max(1,ceil(0.05×n)); lexical row-key tie-break.
- Fields unresolved after the fourth AI pass.

Row key: selected meta-analysis DOI, four-digit one-based forest study-row position (top-to-bottom across subgroups, excluding headings/pooled rows), and printed label normalized to NFC, trimmed, internal whitespace collapsed; join with “|”, retaining case/punctuation. Preserve raw labels separately. Freeze mapping at reconciled extraction; preserve the original sample and error history after corrections.

An erroneous sampled row has any required value or identity/arm/outcome/time mapping inconsistent with source. If erroneous/sample rows **exceeds 2%**, both extractors repeat the complete extraction under the same rules, followed by human re-checking of headline rows only, plus separately required unresolved fields. No universal human check. Corrections rerun reproduction, diagnostics and headline identification; verify newly qualifying headline rows.

Allow five minutes per checked row plus five administration: at most five rows per **≤30-minute packet**, splitting complex cases. Maximum one packet per person weekly across papers; use the supplied COAUTHOR_LOAD.md rules and shared ledger across P14/P06 and every other paper, include Mahmood, and reassign after **seven days**, never skip.

## 5. Original-result gate

Use SOURCE_CHECK §5's fixed R-only calls. For each candidate require exact k/direction and **absolute difference ≤0.005 separately** for pooled ratio and both CI endpoints. No display-rounding allowance. Unstated original settings get one declared software-default attempt, not model searches. Primary's apparently symmetric displayed ratio CI does not justify natural-scale pooling.

Only verified transcription corrections permit identical-model reruns. A failed primary can activate only a fallback cleared under §1; unavailable/ineligible fallback or its failed gate ends analysis. Never try another model.

## 6. App and independent R analysis

SOURCE_CHECK §5 and its v4 execution boundaries fix all count transformations, correction rules, functions, defaults and optimizer arguments now. Independent executable code is still missing; implementation and synthetic validation are mandatory post-release, pre-analysis conditions (§12), not additional freeze criteria.

Use pinned influence/index.html: paste effect=yi, SE=sqrt(vi), administrative label mapped bijectively to the row key; enable additional columns, retain all studies. Fresh browser state, no restored/example inputs, no log-axis conversion, null=0 and automatic plot limits. Export unrounded JSON, per-study CSV, R script and leave-one-out SVG. Intercept-only inverse-variance **REML**, two-sided normal 95% CIs; every single deletion re-estimates tau². No collective deletion or moderators.

Independent R **4.6.0**, metafor **5.2.1**: rma(method="REML",test="z",level=95), leave1out and stats::influence. Scalar-root tolerance **1e-14**, 1,000 iterations; optimizer threshold **1e-12×max(1,start)**, 10,000 iterations, stepadj=1; exact deletion code2 in SOURCE_CHECK. Run independently authored calculations before exported-script comparison.

Report both outputs. Compare every specified full/deletion/diagnostic quantity using unrounded exports: normalized difference **≤1e-6**, Q/Q p-value **≤1e-9**; identities, counts, flags and exclusion states exact. Require identical CI/S classifications. Non-convergence, nonfinite output or unresolved disagreement prevents classification; no numerical rescue or candidate switch.

## 7. New versus robust

CI categories: wholly below, including/touching, wholly above null (0 log-scale; 1 ratio-scale). S_i=|mu_deleted−mu_full|/SE(mu_full).

**Sensitive:** any deletion changes category or S_i≥0.5. **Robust:** every category unchanged and every S_i<0.5. Both reportable. **New/additional sensitivity finding:** sensitive by those numeric criteria plus prior-report clearance. Already-reported sensitivity remains reportable as sensitive, without an additional-finding claim. Late discovery of equivalent work is disclosed without novelty claim or replacement candidate. Technical/verification failure is unresolved, not robust. Flags alone do not change classification. Original-model versus full-REML differences are estimator sensitivity; neither null inclusion nor robustness establishes equivalence.

## 8. Novelty-check log

**Deviation, binding decision:** Europe PMC and OpenAlex replace Google Scholar because Scholar showed a bot check (“unusual traffic”) on **2026-10-28**; it was not bypassed.

Supplied pc2 logs, same date:

| Index/candidate | Query or record | Result |
|---|---|---|
| Europe PMC primary | MED/38594411 citing-record traversal | cited_by 16; 18 retrieved / hitcount 18 |
| Europe PMC fallback | MED/31197564 citing-record traversal | 108 retrieved / hitcount 108 |
| OpenAlex primary | W4394686921 | 34 citing records; 34 retrieved; complete |
| OpenAlex fallback | W2952943844 | 171 citing records; 171 retrieved; complete |
| PubMed primary | (influence OR leave-one-out OR reanalysis OR re-analysis) AND ("Patient Engagement with Conversational Agents in Health Appl") | 0 |
| PubMed fallback | (influence OR leave-one-out OR reanalysis OR re-analysis) AND ("Effectiveness of telemedicine systems for adults with heart ") | 35; IDs logged |

[NOVELTY_P11.json](supporting/NOVELTY_P11.json) preserves the P11 records verbatim with hashes of both supplied JSON logs; archive those full logs at release. Their citation screens identified none applying the same method to the same meta-analysis; no flagged titles. These are index-specific citing-record/title screens, not universal absence or an independently repeated full-text review. Coverage can miss nonciting or unindexed work; the complete flags describe retrieval only. Do not sum counts across indexes. Historical blocked requests are not zero hits.

Equivalent prior re-analysis means single-study deletion or influence diagnostics applied to the fixed outcome/comparison and included evidence, in the original or elsewhere; a different estimator alone does not distinguish it. Primary remains selected. Fallback's unspecified original sensitivity analysis and undocumented PubMed dispositions remain open.

## 9. App implementation

Pin **14dc545bcba87a02158b2f445c28450e7eaf6b89**. [APP_EVIDENCE_P11.md](supporting/APP_EVIDENCE_P11.md) cites files, functions, lines and SHA-256 for the implemented REML/deletion diagnostics and exports. [APP_DEPENDENCIES_P11.json](supporting/APP_DEPENDENCIES_P11.json) records hashes: all 26 direct dependencies and all nine formerly absent hub/shared scripts are present; all 16 PIN hashes match. The optional browser-R bundle is absent. Runtime closure/parity remains untested; global app REML and R initialization differ. Original ML/MH gates, effect construction, classification and verification selection are **R-only/procedural**.

## 10. Write-up and archive

Produce **150–250 words plus one figure** showing full REML and every deletion CI, null and flags; report original reproduction separately. Frame as “a re-analysis illustrating …”; retain P11's existing example. Primary claims concern trial retention only, not adherence or efficacy; fallback claims concern the fixed mortality synthesis. State the precise contribution, including robustness. No clinical recommendations, priority or ranking claims. Mahmood dictates the final paragraph.

Archive reconciled extraction, source map, verification log, preregistration, independent/exported scripts, outputs and amendments in a new paper-archive version.

## 11. Amendments

| Date | Amendment | Reason |
|---|---|---|
| 2026-10-28 | Source/default contracts and fixed-MH fallback gate | Readable local sources; V3 default policy; panel-specific model label |
| 2026-10-28 | Europe PMC/OpenAlex substitution | Binding Scholar bot-check decision |
| 2026-10-28 | Verification identity, reporting and switching clarified | V3 REDTEAM integration retained |
| 2026-10-28 | V4 freeze reassessment; exact item-4 verification text; updated dependency hashes; conditional fallback; later-work separation | FREEZE_CRITERIA.md; V4_NOTES_P11.md maps B1–B5 |

## 12. Mandatory post-release, pre-analysis conditions

These are mandatory holds on the indicated next step, **not F1–F6 freeze failures**:

1. **Implement and validate code on pc2 before any real-data reproduction gate.** Independently implement the frozen source/model contract; assert R 4.6.0, metafor 5.2.1 and meta 8.5.0 APIs/defaults and archive sessionInfo(). Generate fixtures named synthetic_* with “SYNTHETIC - not data” in the first line or column. Cover ordinary/zero cells, exclusions changing fixed k, malformed/mis-mapped inputs, null and S=0.5 boundaries, tied headline maxima, numerical/nonfinite failures and verification escalation. No real rows or supplied example/corpus data may substitute for generated fixtures.
2. **Demonstrate browser/R parity on those fixtures.** Verify full fits, every deletion, every diagnostic/flag, exact identities/exclusions/classifications, import precision and unrounded exports at the unchanged tolerances. Global REML versus R initialization disagreement must fail validation. No runtime pass is claimed.
3. **Close browser dependencies.** Complete the manifest and prove the required workflow loads and exports. Resolve or explicitly document the absent optional webR bundle and demonstrate its absence cannot enter the required external-pc2 workflow; do not claim built-in live R works. Browser dependency closure is still open.
4. **Synchronize the extraction kit before extraction.** Update schemas, codebooks, identical blind-extractor prompts, adjudication/fourth-pass instructions and helpers to v4: normalized four-digit row keys/raw labels, retained/lost versus derived totals, declared corrections, fixed-MH fallback and separate numerical/contribution classifications. Prevent the stale v2 builder regenerating old rules; revalidate only on marked synthetic fixtures.
5. **Coordinate verification packets.** Use the single cross-paper COAUTHOR_LOAD.md ledger; eligible P11 initials are MA, MAY, NA, AO, AW. Reserve an eligible weekly slot as planned before sending; ≤30 minutes, ≤one packet per person per ISO week across all papers, Mahmood included, reassign after seven days. Slots and capacity are unassigned. Close applicable human verification before classifying/reporting results.
6. **Conditional fallback clearance.** Before activating/extracting fallback, resolve the original nonspecific sensitivity statement and plausible matches among its 35 PubMed IDs with evidence-based dispositions under §8, without contact or bypass. Confirm its own source/novelty eligibility. If uncleared, stop after primary failure; do not substitute another candidate.

After release, every code change is logged as a dated deviation and never depends on real-data results. Synthetic failure keeps real-data gates closed; no tolerance, verification or new/robust rule is relaxed.

## 13. Freeze

F1–F6 clear for the primary; mandatory later conditions remain. Commit P11's document and all incorporated supporting files to mahmood726-cyber/usecase-preregistrations; create its GitHub release, record commit, server-side timestamp, document SHA-256 and Zenodo DOI. Extraction starts only after P11's GitHub release exists and its extraction kit is synchronized. Before any real-data reproduction gate, code must pass synthetic validation and all applicable §12 conditions. Every code change after release is a dated deviation independent of real-data results; no retrospective model, eligibility, tolerance or outcome changes. No release occurred here.

**sha256 and UTC freeze time recorded at release**
