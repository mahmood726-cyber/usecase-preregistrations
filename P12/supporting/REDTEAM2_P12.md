# REDTEAM2_P12: adversarial review of the v4 freeze candidate

Date: 2026-10-28. **Verdict: FREEZE_OK. No P0 or P1 findings; one P2 documentation finding.**

This verdict concerns F1–F6 under FREEZE_CRITERIA.md. It does not certify executable readiness, authorize extraction before release, or waive the mandatory post-release conditions.

Reviewed package: `C_P12_V4/out/`. The main preregistration, normative CONTRACT, EVIDENCE, DEPENDENCIES, V4_NOTES and BLOCKERS were read with Python. V4 has no separately named SOURCE_CHECK file: EVIDENCE §§1–2 explicitly incorporates v3's `SOURCE_CHECK_P12.md`. I located that file and the actual v3 preregistration/blockers in `../B_P12_V3/out/`; the source verification below covers the incorporated check, rather than treating v4's assertion as independent evidence.

All local reads used Python. The primary JPEG and the fallback PDF's embedded image were inspected in memory; no image, study-level row, extraction dataset or real-data calculation was written. No R/browser analysis, archived-corpus replay, author contact, login, release or external write occurred.

**1. P2-01 — Document the audit generator's original-workspace dependencies and write behavior.**

Evidence: `supporting/audit_P12.py:12` derives WORK from its location; lines 66–67 require `WORK/B_P12_V3/out/SOURCE_CHECK_P12.md`; later reads require PIN and the original novelty logs. Those files are absent beneath the supplied `C_P12_V4/` package. Lines 101–103 rewrite `out/supporting/DEPENDENCIES_P12.json`. Consequently the script is a historical inventory generator, not a self-contained, read-only validator of a released package. EVIDENCE §5's final sentence and V4_NOTES' file description should make this distinction explicit. I did not execute the generator or overwrite its evidence.

This is not an F6 failure: the capability map and inventory are present, and independent Python reads confirmed their code/source hashes. No analysis choice depends on this documentation correction.

**Exact replacement text** for EVIDENCE §5's final sentence:

> `audit_P12.py` is the historical static-inventory generator for the original V4 job directory. It requires that directory's B_P12_V3 inputs, PIN.txt and novelty logs, together with the configured app/source roots; these dependencies are not all included in this package. It also rewrites DEPENDENCIES_P12.json. It is not a standalone verifier of a frozen release. Preserve the released inventory unchanged, record any regenerated inventory separately, and compare actual file hashes with the frozen inventory before relying on the result. Runtime validation remains a separate mandatory condition.

**Exact replacement text** for its V4_NOTES file-list entry:

> supporting/audit_P12.py — historical Python inventory generator requiring the original V4 job layout; it rewrites its inventory and is not a standalone release verifier.

No statistical, verification or source-number replacement is proposed.

**F1–F6 assessment**

| Criterion | Judgment and independently checked evidence |
|---|---|
| F1 — feasible chosen candidate | **PASS, FEASIBLE-IMAGE.** Primary Figure 3 supplies readable labels and numerical RR/CI fields; the published synthesis has k = 18. Fallback Figure S8 on PDF/printed page 36 supplies readable SMD/CI fields for k = 11. Image reading and rounding risks remain explicit. All six source hashes match v3/v4. These are feasibility findings, not reproduction results. |
| F2 — novelty | **PASS under the approved screening rule.** The two supplied novelty logs' P12 records exactly equal those embedded in DEPENDENCIES. Main §8 discloses the Scholar substitution, incomplete inventories and primary citation-count differences. Neither log identifies an equivalent application. F2 explicitly permits these disclosed coverage limitations; it does not require a new exhaustive citation audit. |
| F3 — original model fixed | **PASS.** Source model statements were verified. CONTRACT §§2–3, 5–6 and 8 fix IV DL, log RR/unchanged printed SMD, normal 95% CIs, CI-derived SEs, and a single RevMan-default configuration. Unstated source details are not relabelled as confirmed. There is no alternative estimator, software, continuity-correction or reconstruction search. |
| F4 — analysis/outcomes fully specified | **PASS.** Main §§2–7 plus normative CONTRACT §§2–8 specify sources, transformations, versions/calls/options, gate ordering, capture manifest, statuses, full/deletion fits, 0.005 reproduction tolerance, normalized 1e-9 app/R tolerance, numeric classification and verification rules. Untouched internal package defaults are explicitly fixed; incompatibility stops execution. Deferred implementation must implement this contract, not choose an analysis after results. |
| F5 — exact verification specification | **PASS.** Python string comparison confirmed that main §4 contains the entire text of MAHMOOD_DECISIONS item 4 verbatim, apart from the item's list number. The independent extractors, different-family fourth pass, seeded sampling, escalation, packet limits and reassignment operational details remain in the contract. |
| F6 — static app capability | **PASS.** The pinned functions below implement the registered statistical/browser operations. All inspected hashes match EVIDENCE/DEPENDENCIES. Input transformations, classification, weights, verification orchestration and publication composition are explicitly R-only. Ordinary deletion uncertainty uses an existing pinned JS pooling function; capture plumbing and runtime evidence remain prospective. |

`BLOCKERS_P12.md` containing `NONE` is consistent with these findings.

**Independent source and numerical-claim audit**

Sources are under `C:/Users/User/ucsources/`. MATCH means the cited evidence supports the claim. UNVERIFIABLE below refers to the specified online route, not to a contradiction in an available local source. No numerical MISMATCH was found.

| Claim in v4/incorporated SOURCE_CHECK | Result, locator and URL |
|---|---|
| Cheema title/authorship, DOI 10.3390/nu14081600, 2022, Nutrients 14(8):1600, CC BY 4.0 | **MATCH.** Local XML article metadata/licence; publisher PDF p.1 supports citation/date/licence, and the publisher article path identifies issue 8. 1600 is the article identifier, not a page range. [Publisher PDF](https://www.mdpi.com/2072-6643/14/8/1600/pdf?version=1649759175). |
| Primary RR 0.68 [0.55, 0.84], k = 18, I² = 61%, Egger p = 0.012 | **MATCH.** Read the published overall summary only: local Figure 3, XML Results and Table 2; publisher PDF pp.7–8. The asymmetry p-value belongs to VAP. [Publisher PDF](https://www.mdpi.com/2072-6643/14/8/1600/pdf?version=1649759175). |
| Primary source location, image size, headers, direction and precision | **MATCH.** `P12_primary/supp/nutrients-14-01600-g003.jpg`, 774 × 393; XML figure ID `nutrients-14-01600-f003`; publisher PDF p.8. Visual inspection confirms `Study or Subgroup`, Probiotics/Control Events and Total, Weight, and `Risk Ratio / IV, Random, 95% CI` over the numerical and graphical columns. Required numerical fields are readable to two decimals; no SE column; lower ratios favour probiotics. [Publisher PDF](https://www.mdpi.com/2072-6643/14/8/1600/pdf?version=1649759175). |
| Primary model sentence and named software | **MATCH.** Both the v4 quotation and incorporated SOURCE_CHECK quotation exactly match local XML Methods 2.6 after XML text flattening/whitespace normalization. RevMan 5.4 is named for synthesis; Jamovi 1.8/MAJOR is separately named for asymmetry. IV/random/95% CI and the overall Z test are visible in Figure 3. [Publisher Methods, PDF p.3](https://www.mdpi.com/2072-6643/14/8/1600/pdf?version=1649759175). |
| Primary caption, identity-table header and unused nested supplement | **MATCH.** XML caption matches SOURCE_CHECK line 44; Table 1 ID and its `Study ID (First Author, Year)` header match. Python listed the nested ZIP member `nutrients-1670561-supplementary.pdf` without unpacking it. Table 1 is context only; Figure 3 remains the sole numerical route. [Supplied XML provenance](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9031795/fullTextXML). |
| MacKinnon authors/title, DOI 10.1097/CCE.0000000000001140, 2024, Critical Care Explorations 6(8):e1140 | **MATCH.** Local XML and current PubMed record; e1140 is an article identifier. [PubMed](https://pubmed.ncbi.nlm.nih.gov/39162653/). |
| Fallback CC BY-NC-ND 4.0 | **MATCH locally** in XML permissions and the indexed original full text. Fresh publisher/full-text access was blocked, so that route is **UNVERIFIABLE** in this audit. [Original full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11338257/); [supplied XML provenance](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11338257/fullTextXML). |
| Fallback SMD -0.19 [-0.36, -0.03], k = 11, observational hospital LOS | **MATCH locally** in Figure S8, XML Results and Table 3. PubMed independently confirms 11 observational studies for hospital LOS; it does not print the SMD and limits. Publisher confirmation of those three numbers is **UNVERIFIABLE: blocked**. The earlier screen's I² = 95% also matches the supplied published summary. [PubMed](https://pubmed.ncbi.nlm.nih.gov/39162653/); [publisher](https://journals.lww.com/ccejournal/fulltext/2024/08000/impact_of_rounding_checklists_on_the_outcomes_of.11.aspx). |
| Fallback source location, image, headers, direction and precision | **MATCH.** `P12_fallback/supp/cc9-6-e1140-s001.pdf` has 42 pages. Page index 35 is printed page 36 and carries Figure S8, one hospital-LOS forest without A/B alternatives. Its embedded image is 1696 × 571. Visual inspection confirms `Study or Subgroup`, Checklist/No Checklist Mean, SD and Total, Weight, and `Std. Mean Difference / IV, Random, 95% CI`. Effects/endpoints are readable to two decimals; no SE column; negative favours checklist. [Supplied archive provenance](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11338257/supplementaryFiles). |
| Fallback title, context Table S4 and model quotation | **MATCH locally.** Figure S8 title exactly matches SOURCE_CHECK line 64. Table S4's hospital-LOS title is on printed/PDF p.14; its rows were not transcribed. The Data Synthesis and Analysis sentence quoted in v4 EVIDENCE line 43 and v3 SOURCE_CHECK line 108 matches the XML exactly after whitespace normalization. The section names RevMan 5.4, Stata/MP 15.1 and RStudio 1.4.1106; RStudio is correctly treated as an IDE version. [Supplied XML provenance](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11338257/fullTextXML). |
| Fallback hospital-LOS asymmetry rationale | **MATCH locally** in Reporting Biases and Certainty of Evidence and in the indexed original text. No mortality-specific asymmetry test is transferred to this endpoint. Fresh direct full-text route: **UNVERIFIABLE, blocked**. [Original full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11338257/). |
| Exact CI algorithm/log pooling/forest-specific software and SMD variant are NOT STATED | **Supported as a distinction between explicit documentation and inference.** Neither quoted methods passage specifies all those details. The selected defaults are documented prospectively. Cochrane's official RevMan 5 algorithms, PDF p.8, specify DL inverse-variance pooling, log ratio effects and normal CIs, with exponentiation continuing onto p.9. [Official algorithms](https://training.cochrane.org/handbook/current/statistical-methods-revman5). |
| Source access, licence and six-source continuity claims | **MATCH.** P12 FETCH_LOG entries record HTTP 200/OK for both XML files and both supplementary archives. All six current hashes equal both source-check generations, as listed below. No required local P12 source is missing or marked blocked. This does not erase blocked web endpoints. |
| Historical AWMF guideline connection | **UNVERIFIABLE independently here.** The earlier candidate screen supplies the exact appendix URL and records an indexed match plus blocked direct retrieval. V4 appropriately does not claim an inspected recommendation or endorsement. This is a disclosed profile limitation, not newly verified source evidence. [Recorded appendix](https://register.awmf.org/assets/guidelines/001_Anaesthesiologie_und_Intensivmedizin/001-021e5_S3_Invasive-Beatmung-Einsatz-extrakorporaler-Verfahren-akute-respiratorische-Insuffizienz_2025-08.pdf). |

All nine block quotations in the incorporated SOURCE_CHECK were checked programmatically against the corresponding XML or the PDF page-36 title: **9/9 MATCH**. This includes the primary RR/software/model sentences and fallback SMD/software/model/summary-estimate sentences. No per-study numerical text was copied into this report.

| Source file | Independently measured SHA-256 |
|---|---|
| P12_primary/fulltext.xml | `3786bd746ba8bc01fda37f2119a6c0ef57550d3e5d0e6116321993cfe5f6c3ad` |
| P12_primary/supplementary.zip | `952c094067f4e273624a8656642eb9a1c3a6f83377e1e135960478bfa00c06f0` |
| P12_primary/supp/nutrients-14-01600-g003.jpg | `b0e03517d09e80a12e11aa98a116bd069338ae5cbe96a7087536219c47fba07c` |
| P12_fallback/fulltext.xml | `08c3846719737d3253d086b3a5175ff73ecf737576c7f54a1432eeace86ed148` |
| P12_fallback/supplementary.zip | `81b8af8341d6d567f33a568f3f9ad4f26ed447911d4cc268a32e604fb5fccf44` |
| P12_fallback/supp/cc9-6-e1140-s001.pdf | `ade2ff6ed53fec6ee10cd2fb42fa2745618de863ebe069f4b6eadb751e709098` |

**Web-check access record**

Web searches were used for both original articles, their numeric/model claims and official methods documentation on 2026-10-28. For example, the searches included `site.mdpi.com 10.3390/nu14081600 Probiotics Prevention Ventilator Associated Pneumonia 0.68 0.55`, `site.pubmed.ncbi.nlm.nih.gov 39162653 Impact Rounding Checklists`, `"Impact of Rounding Checklists" "0.19" "11"`, and `"Impact of Rounding Checklists" "DerSimonian" "15.1"`. Irrelevant hits were not treated as verification or novelty clearance.

The primary publisher PDF and official Cochrane PDF were readable. The primary publisher HTML returned 429 (**blocked**); its PubMed route returned only an HHS footer, so its article content was **unverifiable via that route**. Fallback PubMed was readable; fallback PMC direct retrieval returned a browser/reCAPTCHA check (**blocked**), the publisher page returned 402 (**blocked**), and the PubMed-linked Ovid route returned cache miss (**unverifiable**). No challenge, paywall or access control was bypassed. Accessible supplied Europe PMC downloads supported local verification where the fresh publisher route failed.

**Novelty-log cross-check**

| Candidate | Europe PMC: metadata / hitcount / retrieved | OpenAlex: metadata / retrieved | PubMed supplementary query count |
|---|---|---|---|
| Primary | 28 / 31 / 31 | 45 / 44, logged complete=true | 7 |
| Fallback | 4 / 4 / 4 | 3 / 3, logged complete=true | 0 |

Both indexes' supplied flagged lists are empty. These values match the supplied JSON records exactly; complete=true is not evidence that 45 records were retrieved. This audit does not convert the summary logs into a full-text citing-work inventory.

**V3-to-v4 comparison and deferred-condition audit**

Python section-by-section comparison of the actual v3 preregistration against v4's normative CONTRACT found:

| Area | Change assessment |
|---|---|
| Contract §2 | Only the governing-rule reference changes from V3 to FREEZE_CRITERIA F3 and the evidence link changes to EVIDENCE. Targets, scales, model and estimand remain fixed. |
| Contract §§3–6 | Text is identical to v3: source/input rules, detailed verification, ordered reproduction gate and full app/R contract are preserved. |
| Contract §7 | Only trailing whitespace differs; numeric New/Robust/indeterminate definitions are identical. |
| Main §4 | Adds Mahmood item 4 verbatim while retaining operational details. This strengthens documentary compliance. |
| Contract §8 | Makes R-only boundaries and fixed remaining settings explicit, including independently captured ordinary-deletion SE/CIs, clean R settings and unchanged internal defaults. |
| V3 B1 | Key serialization, source IDs, sampling history, headline union, field manifest, correction ordering and ordinary-deletion uncertainty are already fixed in the normative text. Coding/alignment/packaging are deferred; no statistical choice is delegated to future results. |
| V3 B2 | Synthetic execution, parity, browser closure and export/figure checks move to post-release/pre-analysis. FREEZE_CRITERIA expressly permits this timing. An unresolved discrepancy still prohibits real-data reproduction/analysis. |

**No F1–F6 failure was concealed as a post-release condition. No gate, verification rule or classification definition was weakened.** In particular, both 0.005 endpoint gates and normalized 1e-9 comparisons remain; the fourth pass, >2% escalation, one-packet/ISO-week cap and seven-day reassignment remain; the 20% classification boundary and indeterminate cases remain. V4's absent executable bundle is not treated as a completed implementation.

**Static implementation audit**

App root: `C:/Users/User/ucjobs/allmeta_14dc545`; supplied pin `14dc545bcba87a02158b2f445c28450e7eaf6b89`. Each hash below was recomputed from the supplied bytes, and the cited implementation was read.

| File and functions | Capability/boundary verified | SHA-256 |
|---|---|---|
| limit-ma/index.html: parse, pool, dl, radialReg, limitMA, run, drawFunnel, AlmLimitEngine.fit | Strict finite positive-SE input; DL and beta0; normal CIs; diagnostics/funnel; main fit lacks the comparison-path REML refusal check. | `5d5f1a705d5228014f684dd77eb98a950ed582a8175321835a8bed90792866d3` |
| limit-ma/plus.js: compute, chisqSF, tp | Comparison status, Q tests, shift/G², Egger t/df/p. Unselected automatic methods cannot become optional inference. | `91097a304ac7e82dcbcc7b57fb4659cb87b5abb8ac2fe796f15580d65968975e` |
| limit-ma/plus-opt.js: AlmLimitPlusMLStart | The fixed internal REML check called by comparison and deletion paths. | `869e65ce474846c4d483d9451f3b7e41478f7e7b36fd17cba4ebad2d7c765b8e` |
| limit-ma/plus-ui.js: current, run, snapshot | Strict input, raw comparison capture, exception clearing. | `7576d7b450257e1d37d908265bc7150c1f39d756551ba4803dcf78217ad14f26` |
| limit-ma/loo-limit.js: deletion, compute, csv, invalidate | Refitted deletions and refusal handling; separate CSV; main reruns invalidate deletion state. Its export omits ordinary deletion SE/CIs. | `27c45750a00443e059a1ca01af51e1be99512a13e659ea4eb8951c9ac9032c98` |
| shared/ma-core.js: tau2DL, pool | Existing JS ordinary-fit mu/SE/tau² supports the explicitly specified deletion uncertainty capture; exact-z CIs are formed separately as registered. | `fef6ab267ec7fd5582e3431381f090daee11267010effc0858834d9e5fc44bc8` |
| hub/shared/results-export.js: _csvEscape, _flatKVs, _toCSV, init | Number/String and JSON serialization; CSV null handling. Actual downloads remain untested. | `16ffa76bc74275565214c2e142d7f0d0847a5a8eded2614efb04aa172acd71f4` |
| hub/shared/plot-export.js: _prepareSvg, _serialize, loadPdf | SVG export and lazy PDF dependency; no claimed native CI inset. | `7533db659c89b328f20252fc2deaa1272d8473d00052d7b91a9732c24ee382cc` |

I checked all 32 direct-resource inventory entries, nine dynamic/excluded entries, three entry/R-reference entries and six source entries against their recorded existence/hashes: no mismatch. Archived corpus files were hashed only, never parsed as observations or run. The R reference scripts confirm the documented field mapping/refitting route; they do not substitute for the pending full-manifest implementation. The maintainer's [metasens 1.5-3 manual](https://guido-s.r-universe.dev/metasens/doc/manual.html) supports the registered limitmeta arguments and beta0 estimand.

F6 is static evidence only. Missing optional WebR files remain outside the desktop-R route. Main/comparison/R statuses stay distinct; a finite main-panel result cannot override an authoritative refusal.

**TASK_COMMON/protocol compliance and researcher-choice check**

| Requirement | Assessment |
|---|---|
| Fixed approved candidate and mandatory fallback; one outcome per candidate; k within effort cap | PASS. The full source panels and k = 18/11 are fixed; no result-based subset selection. Four analyst hours cover both candidates, excluding verification waiting. |
| Selection on published features only | PASS. Clinical uncertainty, published asymmetry/heterogeneity and outcome-specific k justify method fit. The guideline-profile limitation and fallback target-journal relevance are disclosed. No computed SE distribution or adjusted effect informed selection; attenuation is not assumed. |
| Exact sources, input conventions and row provenance | PASS. Labels/order and effect/CI inputs are fixed. No count/mean reconstruction, alternate time point, imputation, design repair or borrowed review rows. Mapping/dependence problems trigger the fixed stop procedure. |
| Independent double extraction and verification | PASS. Codex/agy independence, logged different family, third-model adjudication, fourth different-family recheck and unresolved-field escalation are explicit. |
| Numeric headline/sampling/escalation rules | PASS. Weight >=10%, tied SE extrema, deletion change >=0.10/sign/CI/classification/refusal triggers; seed 2026102812; compact JSON/NFC SHA-256 key; ceil(5%) minimum one when n > 0; retained sample/error history and headline union; >2% full AI re-extraction with headline human recheck. |
| Human workload | PASS. Five minutes per row plus five administration, at most five rows per packet, eligible coauthors/Mahmood, one packet per ISO week across papers, planned ledger slot and seven-day reassignment. Assignment itself properly remains prospective. |
| Reproduction and candidate transitions | PASS. Each point/CI endpoint within 0.005 on the printed scale, exact k/direction/null category; one documented transcription correction and unchanged rerun; primary → cleared fallback → stop; no switching after sensitivity results. |
| Exact app/R runs and tolerances | PASS as specification. Pinned settings, arguments, complete manifest, statuses, capture order and independent app-derived/R-derived quantities are fixed. Execution is not certified. |
| New versus robust | PASS. Sign/CI-category change or relative change >=0.20 is New; same categories and <0.20 is Robust; zero denominator and undefined/disagreement cases have explicit handling. No tolerance epsilon or outcome switching. |
| Novelty log and approved deviation | PASS with disclosed limits. Successful supplied checks are distinguished from blocked historical attempts; equivalence is fixed to beta0 on the same outcome/synthesis. |
| Write-up, release and amendments | PASS. Existing example retained; 150–250 words and one figure; both implementations and indeterminate outcomes; no clinical advice, priority/ranking claims or publication-error allegation; GitHub server timestamp/hashes and Zenodo DOI precede extraction. |

No remaining data-dependent analytic choice was identified. Prospective mapping checks, convergence/refusal handling and the time cap have specified consequences; they are not invitations to tune the model. Mandatory synthetic validation, kit alignment and browser closure are implementation obligations under the new freeze criteria.

**Every remaining open problem/condition**

- P2-01 remains a proposed documentation correction; no v4 input was edited.
- The aligned, versioned CODE/KIT bundle and its hashes remain outstanding: JSON/NFC keys, stable identities, retained sampling/headline history, independent ordinary-deletion uncertainty capture, full manifest and ordered safeguards must be implemented. Earlier CODE/KIT inputs are discoverable in `../B_P12_V3/A_P12_CODE/out/` and `../B_P12_V3/A_P12_KIT/out/`; their availability here does not certify alignment or change the supplied v4 package.
- Actual pinned-version R/browser synthetic parity, refusal/boundary tests, capture/export round trips, state invalidation, funnel/inset production and browser dependency closure remain unproved. No real-data gate may run first. Prevent default/restored examples and corpus replay from executing. All later code changes require dated deviations independent of real results.
- Optional WebR runtime/package files are missing; desktop R remains required. The embedded build commit differs from the supplied pin, and Git ancestry is unavailable; retain measured hashes and the disclosure.
- Novelty coverage remains limited by summary-only citing inventories/request records and the disclosed count differences. Current direct publisher/PMC access failures and historical AWMF/Scholar blocks remain recorded; they were not bypassed. The supplied readable sources meet F1 despite these web-route limits.
- Critical Care Explorations is task-specified; the software manuscript does not independently confirm the target journal. The AWMF recommendation/profile evidence remains uninspected beyond the historical indexed claim.
- Source-specific CI/transformation/software/SMD details remain NOT STATED, handled by the fixed single configuration. Rounded-input reproduction, source-row mapping/dependence, candidate-specific parity and final finite/indeterminate outcomes remain unknown until the authorized post-release workflow. The fallback must still be cleared when activated.
- Public GitHub release URL/server UTC timestamp, frozen hashes and Zenodo DOI do not yet exist in this job. Post-release extractor identities, verified extraction, cross-paper packet assignments, human signatures and correction checks remain outstanding. Final results, both implementations' outputs, publication figure, Mahmood's paragraph and the archive remain prospective.

Reviewed main preregistration SHA-256: `4dc35cca8c965ea783f99533a169ce98758760e2566a90c852517b366feab4be`.
Normative CONTRACT SHA-256: `04a244185437452e29c6dbd60dd4aefb25a5b5e96da827f9eb2006fc446d9ece`.
EVIDENCE SHA-256: `34889647e1048eae62c383cb1c21d1938e9d7ef1122208add37873ec66188741`.
DEPENDENCIES SHA-256: `84f3b5c02418b676ca431c8168f73a68d9c28d21f3da55ae35aa9306eef0140b`.

Required one-line verdict is in `VERDICT_P12.txt`: `FREEZE_OK`.
