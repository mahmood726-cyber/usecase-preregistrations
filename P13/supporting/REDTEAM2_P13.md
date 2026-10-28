# REDTEAM2 P13 — review of F_P13_V5

Date: 2026-10-28. Reviewed candidate: `F_P13_V5/out/`, as explicitly required by this job's binding JOB.md; the generic REDTEAM2 v4 reference is superseded. Main preregistration SHA-256: `c1125c9823b2e7fbc1cd38b0bdde698e029288280804621770dc5cdf33ce9a99`.

**Verdict: FREEZE_OK. P0 findings: none.** This means F1–F6 satisfy the supplied freeze definition. It does not certify release, extraction eligibility, independence, remaining effort, executable-pipeline completion, or statistical validation. P1 items below must be addressed before the affected downstream work. P2 is a prospective implementation clarification. Proposed replacements have not been applied to the candidate.

Local evidence was read with Python only. Forests were inspected visually for headers, readable printed fields, contribution count and pooled footer only; no study-level dataset was transcribed or assembled. No original-paper numbers were recomputed, no statistical analysis was executed, and no source/app/prior-package files were changed. All review outputs are under this job's `out/`.

## F1–F6 decisions and evidence

Paths in this table are relative to `F_P13_V5/out/`; line numbers refer to the reviewed bytes.

| Criterion | Decision | Evidence and limit |
|---|---|---|
| F1 — feasible printed inputs | MET, FEASIBLE-IMAGE | Preregistration lines 35–45; EVIDENCE lines 5–20; independently inspected final primary Figure 1 and fallback Figure 2, article/context-table headers and supplements. Both print the required matched event/denominator fields and verification intervals legibly. Final sources, source hierarchy and image-reading risk are explicit. This criterion does not require completed row extraction or independence certification. The affirmative overlap warning requires RT2-01 and the existing fail-closed eligibility check. |
| F2 — novelty | MET under the specified supplied-screen/coverage rule | Preregistration lines 93–101; EVIDENCE lines 26–48; exact supplied Europe PMC/OpenAlex logs for both candidates. Their flagged lists are empty. Scholar substitution, failed earlier searches, missing request/record-level audit trail and the fallback 14/15 discrepancy are disclosed. No independent full citing-record rereview or guarantee of absence is asserted. |
| F3 — one original reproduction configuration | MET under binding Mahmood item 7 and the archived v5 JOB.md | Preregistration lines 57–67; REPRODUCTION lines 29–59; original_gate_P13.R lines 34–74. One REML/z configuration is fixed per candidate. Primary uses PFT and transf.ipft.hm with harmonic mean n; fallback uses PR/LS and identity inverse because no transformation declaration was found. All three published-target components retain their original tolerances. Source statements and prospective assumptions remain distinct. |
| F4 — fixed analysis, options and outcome definitions | MET | Normative ANALYSIS_CONTRACT lines 7–52 fixes transformation/variance, serialized input, DL/z, singleton normalization, all 131,071 primary subsets, 50,000 fallback draws with exact generator/state, membership/duplicate rules, summary scope, medians, grid, numerical agreement and failure rules. Preregistration lines 87–91 fix inclusive 0.10-radian/10-percentage-point flags and both outcomes. Missing integration and runtime tests are implementation obligations, not unresolved scientific choices. RT2-03 makes the pinned grid arithmetic literal. |
| F5 — exact verification specification | MET | Preregistration line 51 is an exact copy of MAHMOOD_DECISIONS item 4. VERIFICATION lines 9–19 and 24–28 specify independent different-family extraction, adjudication, fourth-pass family difference, headline rows/ties, UTF-8 SHA-256 seeded 5% selection, minimum one when eligible rows exist, fixed error denominator, >2% escalation, ≤30-minute packets, both weekly caps, Mahmood and seven-day reassignment. |
| F6 — static implemented app capability | MET | EVIDENCE lines 50–65 names files/functions/hashes. All four core GOSH hashes match PIN.txt and the supplied ALLMETA snapshot; all 31 inventoried app assets match archived and snapshot bytes. Static inspection confirms the registered native operations. Original reproduction/PFT/inverse, independence checks, subset intervals, thresholds, comparison, human sampling and combined figure are explicitly R-only/external. Runtime parity and provenance remain unverified. |

The incomplete R/browser pipeline is not being treated as validated. The review distinguishes static F6 evidence from runtime conditions exactly as FREEZE_CRITERIA requires. The supplied original gate R module was inspected, not run. Official [metafor transformation documentation](https://wviechtb.github.io/metafor/reference/transf.ztor.html) supports the named harmonic-mean inverse API, and [GOSH documentation](https://wviechtb.github.io/metafor/reference/gosh.html) supports membership-based enumeration; these pages do not certify the installed 5.2.1 runtime.

## Numbered findings and exact replacements

1. **RT2-01 — P1: disclose the source-specific overlap uncertainty and the existing sensitivity checks.**

   Evidence: the primary source XML, Discussion → Limitations (`sec27`), explicitly leaves possible cohort overlap unresolved and describes leave-one-out sensitivity checks. This was checked against the [publisher's article](https://academic.oup.com/rheumap/article/10/2/rkag034/8528302). V5 preregistration lines 43–45 and EVIDENCE lines 18–20 give generic independence cautions but omit this affirmative source warning; ANALYSIS_CONTRACT line 56 describes the contribution only relative to pooled/subgroup summaries. This is a limitation of the package's disclosure, not a finding about the correctness of a publication. No affected study identity, row value, or sensitivity result is reproduced here.

   F1 still meets its expressly defined printed-input/readability test. The existing rule already rejects unresolved overlap, so this omission does not create permission to analyse dependent contributions or a new F1–F6 failure. Resolve the eligibility question before any real-data gate; image legibility and a matching pooled estimate cannot resolve it.

   Exact addition after preregistration §3's final paragraph, also to EVIDENCE §F1:

   > Source-specific independence alert: the primary article's Limitations explicitly leave possible cohort overlap unresolved. Its general overlap-exclusion policy does not settle that warning. The registered independence condition must be resolved from the permitted review/supplement sources before the primary reproduction gate. If it remains unresolved, the primary fails eligibility and only the independently cleared, already specified fallback may proceed; otherwise stop. Do not assume independence from different assessment methods, matching pooled results, or legible forest columns. Do not omit or merge contributions.

   Exact replacement for ANALYSIS_CONTRACT's final sentence at line 56:

   > The primary article already describes leave-one-out sensitivity checks. The added output is the registered exhaustive joint-subset and inclusion-contrast analysis beyond those checks and the published pooled/subgroup summaries.

2. **RT2-02 — P1: the retained effort cap has no usable opening balance.**

   Evidence: preregistration line 18 and V5_NOTES line 59 retain four active hours from the v3 handoff but explicitly say historical active time is unavailable. V3 preregistration line 17 started this same cap; v4/v5 did not reset it. No time/duration ledger was identified in the supplied v3/v4/v5 packages. The cap is a protocol obligation, not one of F1–F6; absence of a ledger does not prove the cap was exceeded. It does prevent certifying that further active work fits the remaining allowance.

   Exact replacement for the last two sentences of preregistration §1's effort paragraph:

   > Historical active time is not established. Before further implementation or extraction work, recover a documented conservative upper bound for active time since the v3 handoff, including both candidate routes, and subtract it from the original four-hour allowance. If no defensible remaining allowance can be established, stop under the effort cap; do not assign a new four-hour budget or treat missing time as zero. Log subsequent start/stop durations. Wu remains outside this plan.

3. **RT2-03 — P2: make the density-grid evaluation order match the pinned engine literally.**

   Evidence: ANALYSIS_CONTRACT line 42 writes `floor((estimate−x0)×100/(x1−x0))`; pinned `gosh/exact-enum.js` line 86 first computes `gxScale=GX/(x1-x0)`, and lines 161–163 multiply by that scale before flooring. The expressions are mathematically equivalent, but different floating-point evaluation orders can disagree at a cell boundary. No such failure on real data, synthetic data, R, or a browser is claimed. This is an implementation clarification of an already fixed grid, not a reason to widen its exact-count acceptance rule.

   Exact replacement for ANALYSIS_CONTRACT's grid paragraph:

   > Primary grid: set x0=min(y), x1=max(y); if equal, expand to y−0.5 and y+0.5. Match the pinned engine's evaluation order: first compute gxScale=100/(x1−x0) and gyScale=100/100; then ix=floor((estimate−x0)×gxScale) and iy=floor(I²×gyScale). Clamp each index to 0…99 and flatten as iy×100+ix. Compare all 10,000 cells exactly, their total and dimensions, and the continuous bounds. These are unpadded density bounds, distinct from display limits. Include boundary-adjacent synthetic checks. Never repair a discrepancy by moving bins, introducing an epsilon, or widening acceptance.

4. **RT2-04 — P2: the inherited internal-page label is unverified.**

   Evidence: inherited SOURCE_CHECK line 21 calls the accepted supplement locator “PDF page 20 (internal page 19)”. Python confirms the overall Figure 2 caption on physical PDF page 20, but finds no internal “19” in that page's selectable text and no PDF PageLabels dictionary. The reader's physical page label is 20. The active v5 preregistration and EVIDENCE already use the correct physical locator, so F1 is unaffected; do not promote the inherited internal label to independently verified fact.

   Exact addition to active EVIDENCE after the accepted-supplement locator:

   > The authoritative locator here is physical PDF page 20. The historical source screen's additional “internal page 19” label was not independently verified and is not used to identify or extract the figure. Final published Figure 1 remains the primary data source.

## Independent verification of the inherited SOURCE_CHECK

V5 has no new file named SOURCE_CHECK. EVIDENCE explicitly incorporates `supporting/evidence/history/v3_SOURCE_CHECK_P13.md`; its bytes match `../B_P13_V3/out/SOURCE_CHECK_P13.md`. The historical missing-model blocker is explicitly superseded by the binding v5 configuration. Every factual claim group in that incorporated source check was checked; obsolete eligibility judgments were not treated as current instructions.

The source roots are `C:/Users/User/ucsources/P13_primary/` and `C:/Users/User/ucsources/P13_fallback/`. No study label inventory or per-study number appears in this report.

| Source-check claim / lines | Status | Independent evidence |
|---|---|---|
| Both sources permitted and readable; lines 5–19 | MATCH | Local XML, PDFs, image files and ZIP/DOCX bundles exist and are readable. All six P13 FETCH_LOG items record HTTP 200/OK and match SHA-256 against original local files. This verifies the historical log, not six new HTTP requests. No P13 item is logged blocked. |
| Primary public locators; lines 13–17 | MATCH | [Europe PMC XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13070644/fullTextXML), [published repository PDF](https://eprints.whiterose.ac.uk/id/eprint/238347/19/rkag034.pdf), [supplement bundle](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13070644/supplementaryFiles), [accepted supplement](https://eprints.whiterose.ac.uk/id/eprint/238347/6/Supplementary%20Materials%20ACCEPTED.pdf); URLs agree with the supplied fetch log. |
| Fallback public locators; lines 18–19 | MATCH | [Europe PMC XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10597538/fullTextXML) and [supplement bundle](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10597538/supplementaryFiles); local files match the logged downloads. |
| Primary final overall Figure 1, PDF/printed p.5, rkag034f1.jpg; lines 29–36 | MATCH | Python PDF inspection locates Figure 1/caption on PDF p.5 and an embedded forest image. Direct JPEG inspection confirms “Study”, “Total”, “Number with Dysautonomia”, “Prevalence % [95% CI]”; integer printed counts and percentage/CI precision; 17 contributions; 742 × 587 pixels. No row values recorded. |
| Primary Table 1, PDF p.4/XML rkag034-T1; line 33 | MATCH | PDF page location and XML table ID match; requested context headers are “Study (author, year)”, “Medical diagnosis”, “Sample size, n”, “Method used”, with “Subjective”/“Objective”. These are selected relevant headers, not a claim that the table has no other columns. |
| Primary pooled target/k; lines 36–38 | MATCH | Published article/abstract: k=17 and 64% (95% CI 51, 76; I² = 93%). Forest pooled footer: 64 [51, 76]. No calculation performed. |
| Primary model, selection sentence and caption; lines 40–50 | MATCH, with RT2-01 disclosure omission | The model quotation and sensitive-method/outcome-selection sentence match Methods sec13; caption matches rkag034-F1; overlap-exclusion policy matches sec9. The additional sec27 overlap warning must accompany the policy. No inference that the policy proves independence is justified. |
| Accepted versus final supplementary Figure 2; line 21 | MATCH physical locator; UNVERIFIABLE internal p.19 label (RT2-04) | Accepted physical PDF p.20 locates the overall Supplementary Figure 2; the claimed internal p.19 marker was not independently verified. Nested final DOCX labels its Figure 2 subjective-only. The nested archive contains the named Supplementary Materials DOCX and PRISMA checklist. Final Figure 1 remains authoritative. |
| Fallback overall Figure 2/rkad084-F2/rkad084f2.jpg; lines 58–68 | MATCH | JPEG shows “Study”, “Fatigued”, “Total”, “Proportion”, “95%-CI”, “Weight”; 30 contributions; 780 × 813 pixels. Counts are integers, prevalence/CI values have two decimals, weights one decimal in percent. No fallback article PDF was supplied; no PDF page is invented. |
| Fallback S1/S2 titles and headers; lines 63–66 | MATCH | Python read DOCX XML headers: S1 “Characteristics of the studies” includes Study/Sample; S2 “Fatigue characteristics” includes Study, Fatigue Tool, Fatigue as Primary Objective, Fatigue Definition, AxSpA, r-AxSpA/AS, nr-AxSpA, Classification Criteria, HLA-B27 Positivity (%). No study entries transcribed. |
| Fallback selection and instrument hierarchy; line 70 | MATCH | Article Methods → Study selection excludes repeated cohorts; Statistical analysis prefers combined axSpA when reported and states the FACIT-F → Fatigue Severity Scale → SF-36 → BASDAI fatigue-question hierarchy. These are source selection rules, not instructions to reselect contributions. |
| Fallback pooled target/k and forest rounding; lines 68–72 | MATCH | Article: k=30, 0.56 (95% CI: 0.49, 0.63; I² = 94.6%). Forest: 0.56 [0.49; 0.63], I² = 95%. Preserve distinct printed presentations; no numerical reconciliation attempted. |
| Fallback software/model quotations and caption; lines 74–86 | MATCH | First three Statistical analysis sentences agree with the quoted RStudio v.2022.12.0, prevalence/95% CI and random-effects statements. Figure 2 caption and “Random effects model” label match. RStudio does not identify a pooling package. |
| Original-method ledger; lines 88–106 | MATCH as a bounded documentary finding | Primary states random effects/Freeman–Tukey, fallback random effects/RStudio. The inspected sources do not name the remaining estimator, interval, normalization/inverse or boundary conventions. Tang article and entire supplementary DOCX contain no transformation declaration; the DOCX has no embedded media. Source absence does not identify historical author settings. |
| Original default-only limitation; lines 108–114 | SUPERSEDED, not a current mismatch | V5 JOB.md and Mahmood item 7 deliberately authorize a single prospective metafor configuration. It is not chosen from numerical gate results. Historical source-check statements that model eligibility currently blocks freeze must not be read as the active verdict. |
| Mapping, independence and limits; lines 116–118 | UNVERIFIABLE before extraction at row level | No independent row mapping or overlap certification was attempted. These remain mandatory eligibility checks, with RT2-01's affirmative source alert. FEASIBLE-IMAGE is not a certificate of independence. |

## Checks against v3 and v4; deferred conditions

The actual adjacent `B_P13_V3/out/` package was read, rather than relying only on v5's self-audit. Archived v4 preregistration, notes, analysis and verification files match the adjacent C_P13_V4 bytes.

- **Gate retained:** v3 §5 and v5 §5 both check the point and each CI endpoint separately, inclusively at 0.5 percentage points / 0.005 proportion units; I² remains descriptive. No threshold widening, rounded-value pass or model search was introduced.
- **F3 change authorized:** the missing-software/default anchor in v3/v4 is replaced by the explicitly binding REML/z decision; this is a documented prospective model choice, not a weaker reproduction gate or a historical-method claim.
- **Analysis/outcomes retained:** v3 §6 matches the normative v5 contract except the local entry-path citation. V3 §7 is identical to the v5 sensitivity/robustness section. No medians, individual fits, cells, duplicate occurrences, singleton coverage or failures were dropped.
- **Verification retained/strengthened:** exact decision 4 is included; v3 operational extraction, headline, sample and correction rules remain. V4 adds the ISO-week rule while retaining the rolling-seven-day restriction; v5 verification is identical to v4 apart from its heading.
- **V3 B2 → downstream mapping:** no missing printed inputs were found; F1 does not demand pre-release row certification. Moving full mapping/independence checks after release is consistent with the no-extraction rule, but the affirmative source warning still needs RT2-01 and cannot be cleared by runtime parity.
- **V3 B3/B5 → downstream runtime:** dependency closure and synthetic execution/parity are expressly post-release conditions in FREEZE_CRITERIA. Their movement is legitimate. All 28 direct assets now exist; differing declared/embedded build identities remain disclosed.
- **V3 B4 → downstream implementation:** the normative choices are fixed; only implementation/integration remains. All enumerated v4 obligations are retained in V5_NOTES lines 37–50. No actual F3 choice is deferred: original_gate_P13.R and REPRODUCTION now specify it.
- **Fallback remains conditional:** its own source, novelty, mapping, independence and fixed-model checks must clear before activation; no automatic fallback pass is claimed.

**No demonstrated F1–F6 failure was hidden in the post-release list.** Do not promote the incomplete pipeline, future verification, or a successful gate into evidence that independence or the effort cap has been satisfied.

## Documentary validation and every remaining problem

Independent Python checks: 57 evidence hashes match; 31 app asset hashes match both the archived copy and ALLMETA; 28 are direct page dependencies; 10 archived source files match the original source roots; all six logged source hashes match; four historical v4 copies and the v3 source check match their adjacent packages. These are file/document checks, not statistical results. Details are in [documentary_audit_P13.json](documentary_audit_P13.json), reproducible with `python -B out/documentary_audit_P13.py` from this job root using [the documentary audit script](documentary_audit_P13.py).

Open matters:

- RT2-01 source-specific overlap/previous-sensitivity disclosure and unresolved independence; RT2-02 missing active-time accounting; RT2-03 literal grid evaluation order; RT2-04 unverified inherited internal-page label.
- No public GitHub release, server-side freeze record or Zenodo DOI is evidenced in this package; extraction waits for both release and DOI.
- Full app/R pipeline integration, code hashing, exact R/package/browser/Playwright environment checks, labelled synthetic tests at both complete workloads, gate/endpoint/boundary/refusal tests, runtime parity and browser dependency closure remain undone.
- Declared snapshot `14dc545bcba87a02158b2f445c28450e7eaf6b89` differs from embedded `42a94da2110a02200d0b5bff4c56f636b9cbffa9`; byte equality is established, Git ancestry and runtime provenance are not.
- Extraction-kit/log/identity-map synchronization, independent extraction and family-log checks, adjudication/fourth pass, human verification and packet assignment remain future gated work. Izataku eligibility is unresolved; shared live ledger slots must be checked.
- Final contribution mapping, selected-assessment/denominator pairing, source conflicts, missing fields and independence must be resolved; otherwise use the registered failure order. Actual primary/fallback reproduction, app/R analysis, figure, write-up and archive remain unperformed.
- Novelty citing-request URLs and full record-level screening lists are absent; fallback Europe PMC metadata 14 versus retrieved/hitcount 15 remains unresolved as an audit discrepancy, not silently corrected.
- Direct PubMed opens during this review returned only a footer, so that route was UNVERIFIABLE; publisher results supplied the required verification. No bot check, login or paywall was bypassed. Historical Google Scholar remains blocked as recorded, and was not retried.

R execution is unavailable on this node and was not attempted. No statistical fixture or bundled real-data corpus was executed.
