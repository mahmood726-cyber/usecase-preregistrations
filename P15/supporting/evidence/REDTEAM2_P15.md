# P15 second-round adversarial review

Date: 2026-10-28. Candidate: C_P15_V4/out/PREREG_P15_usecase.md and its five supporting Markdown files.

**Verdict: FREEZE_BLOCKED: RT2-P15-01**

The blocker concerns the preregistration's source interpretation. It is not an allegation about a publication and does not establish which uncertainty convention the source table actually uses. No study row, study-level value, dataset or real-data analysis is reproduced here.

## Numbered findings and exact replacements

1. **RT2-P15-01 - P0, F1: primary uncertainty scale not established.**

   Evidence: prereg lines 15 and 36; SOURCE_CHECK lines 11, 24, 37 and 112; V4_NOTES lines 15, 23 and 34 certify FEASIBLE and assert that the caption and Eq. (3) establish variance, so se must be copied unchanged to vi. The S2 caption does use variance terminology. However, the displayed Eq. (3) in primary fulltext.xml, sec006, is:

   se = sqrt[(n_G1 + n_G2)/(n_G1*n_G2) + d^2/{2*(n_G1 + n_G2)}]

   This is a general source formula, not a study row. Its XML element is disp-formula id="pone.0166941.e005", with an explicit MathML msqrt element. Its printed number is (3), not its filename suffix. The supplied image P15_primary/supp/pone.0166941.e005.jpg visibly confirms the radical. SHA-256: ab6746b845b0dfe18016d8a170d1ee8120ab1a517a223c5830b01789ec6a1d16. Flattening XML to text loses the radical. The displayed equation is not affirmative evidence that the column can be used unchanged as a variance. The S2 Fig caption also describes a standard-error axis. [Publisher Methods and supplement captions](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0166941).

   Consequence: readability and a label do not settle the documented scale ambiguity. F1 requires the necessary variance input to be established in a permitted source. F3's software-default allowance does not establish input units. Trying both mappings, or choosing one through pooled-result agreement, would introduce a forbidden source-dependent choice. The current mapping is explicit, but its claimed documentary justification is incomplete. This issue was inherited from v3.

   Exact replacement for prereg section 4's primary-source paragraph and SOURCE_CHECK's variance interpretation:

   > Primary S2 Table, supp/pone.0166941.s003.docx, supplies readable Study*, d and se columns. The caption calls se a variance, while the displayed Eq. (3), fulltext.xml sec006 / pone.0166941.e005, includes a square root. The supplied evidence does not establish which uncertainty convention the S2 column instantiates. Primary source feasibility is therefore NOT CLEARED: UNCERTAINTY SCALE UNRESOLVED. Resolve that convention from permitted published documentation before freeze, record the source and fix one import mapping prospectively. Preserve the printed field unchanged in the extraction record and document any justified conversion separately. Do not use study-row reconstruction, reproduction results, alternative-mapping trials or author contact to settle the convention. If it cannot be resolved, record primary source-feasibility failure; the fallback may activate only after its own feasibility, novelty and fixed reproduction specification clear, otherwise stop. No original number or reproduction tolerance changes.

   Exact replacement for the prereg status assertion, primary status in section 2 and V4_NOTES' all-pass conclusion:

   > Status: DRAFT for freeze; FREEZE_BLOCKED by RT2-P15-01 (F1). The primary uncertainty scale is unresolved. F2-F6 have the evidence described in this review, but they do not waive F1. The fallback remains unavailable for its complete mandatory reproduction workflow.

   Exact replacement for the candidate BLOCKERS_P15.md:

   > RT2-P15-01 (F1): The primary S2 uncertainty scale is unresolved. Establish its meaning from permitted published documentation and fix the import mapping before freeze; otherwise follow primary source failure, independently cleared fallback, then stop.

   These replacements record the blocker; they do not clear it. Update all corresponding FEASIBLE/variance-resolved assertions in SOURCE_CHECK and V4_NOTES consistently.

2. **RT2-P15-02 - P1: novelty evidence and JOB.md attribution are not portable in the handoff.**

   Evidence: prereg lines 130 and 136, SOURCE_CHECK line 112 and NOVELTY_LOG lines 15-19 cite a paged JSON and a coordinator statement in JOB.md. Neither is in the copied C_P15_V4 package supplied to this review. The current review's JOB.md does not contain that statement. I located both originals with Python under C:/Users/User/ucjobs/C_P15_V4/. The JSON contains 343 records with 343 distinct OpenAlex IDs; the original job note contains the attributed seven-title disposition. Both hashes match NOVELTY_LOG. Thus this is an evidence-packaging problem, not an F2 failure.

   Exact replacement for the unqualified attribution/evidence-location text in prereg section 9, SOURCE_CHECK's final disposition and NOVELTY_LOG:

   > The coordinator statement is in C:/Users/User/ucjobs/C_P15_V4/JOB.md, SHA-256 283047c869269f462a5c1f708a9c6f84e814788c4363c8a33a8dae38bf71eec9; it is not the REDTEAM2 job's JOB.md. The paged file at C:/Users/User/ucjobs/C_P15_V4/NOVELTY_openalex_P15primary_paged_2026-10-28.json has SHA-256 15c33a8c364cd305a60286d90971932e1cd4eefebdf6401ed923aa376415fcf2 and contains 343 distinct work IDs. These records support the attributed screening conclusion, not an independent full-text adjudication by this reviewer. Before release, include those exact bytes in supporting/evidence/ under V4_JOB_P15.md and NOVELTY_openalex_P15primary_paged_2026-10-28.json, together with the two original novelty logs, and update release-relative links. The older eight flagged metadata entries are not a documented mapping to the coordinator's seven reviewed titles.

3. **RT2-P15-03 - P2: incomplete primary study-count locator.**

   Evidence: SOURCE_CHECK line 27 associates the pooled target, n = 99 and 50 studies with sec006/sec007/sec010. The direct 50-study provenance is the abstract, Results sec009 and the S2 Fig caption. The number itself matches.

   Exact replacement for that source-table row:

   > | Original model, pooled target and published counts | fulltext.xml: sec006 for effect definition; sec007 for global DL and complete dataset n = 99; sec010 for 0.75 (95% CI: 0.50, 1.00); abstract and sec009 Description of studies, corroborated by the S2 Fig caption, for 50 studies | Published synthesis counts; the pooled target has two decimals. No independent-cluster count has been derived. |

4. **RT2-P15-04 - P2: specify verification row-key serialization.**

   Evidence: prereg line 55 fixes the seed and sampling fraction but describes the key as DOI, source table and physical row position without defining serialization. Delimiter, indexing and normalization choices can produce different samples. This is a verification-kit reproducibility gap; the literal item-4 specification and sampling fraction remain intact. Close it before extraction/sample selection.

   Exact replacement for the row-key sentences in the Random remainder bullet:

   > Row key is the lowercase DOI without a URL prefix, followed by "|" and the exact source DOCX filename, followed by "|table1|row" and the base-10, unpadded, one-based position of the w:tr element in the sole source table. Positions include structural header rows, although headers are never eligible observations. Hash the UTF-8 bytes of "2026102815|P15|" followed by that row key, without a BOM, newline or trailing whitespace. Sort lowercase hexadecimal SHA-256 digests ascending; break ties by bytewise ascending row key. Take max(1, ceiling(0.05*n)) eligible remainder rows when n>0, and none when n=0. Preserve physical positions through corrections.

## F1-F6 assessment

| Criterion | Judgment | Evidence |
|---|---|---|
| F1 feasible primary | **FAIL: RT2-P15-01** | Required named columns and numerical text are readable, but the documented uncertainty-scale ambiguity prevents certification of the required variance input. |
| F2 novelty | **PASS, bounded evidence; P1 handoff repair** | Recorded Europe PMC/OpenAlex checks and original v4 coordinator note support the reported screening conclusion. Paged JSON has 343 distinct IDs. Scholar substitution and index/query limits are disclosed. No independent full-text adjudication claimed. |
| F3 original model fixed | **PASS as model specification** | Prereg lines 64-79 fix one DL/z attempt, pinned R/metafor, GEN/intercept/weighted/default controls, no search and primary/eligible-fallback/stop. DL is stated; z is an acknowledged assumption. This does not cure F1. |
| F4 exact analysis/outcomes | **PASS as specified, subject to F1 eligibility** | Sections 5-8 fix clusters, formulas, indicators/reference, centring, CORR/CR2/Satterthwaite, rho/grid, R-only HTZ/deletion/classification, agreement and classification thresholds. No additional data-chosen model option identified. |
| F5 exact verification | **PASS** | Prereg line 46 equals MAHMOOD_DECISIONS item 4 exactly. The entire detailed v3 verification body is retained. P2 serialization concerns implementation of that unchanged rule. |
| F6 static app evidence | **PASS, static only** | All 12 APP_AUDIT hashes match; file/function evidence below implements the registered app analysis, with remaining work labelled R-only. No runtime success inferred. |

An unavailable fallback does not independently block a cleared primary under FREEZE_CRITERIA. Here the primary itself fails F1.

## Source and publisher verification

All local files were read with Python. DOCX archives were opened in memory. Inspection was limited to headers, captions, general methods, published synthesis summaries, reference metadata and display-format checks. No study rows were emitted/copied and no study-row or independent-cluster counts were calculated. Format checks returned only whether the effect/uncertainty fields were readable text with three decimal places. The equation image was read with Python and displayed unchanged.

Web searches and publisher/PubMed checks were run on 2026-10-28. A fresh publisher equation-thumbnail request returned a cache miss: that live-image fetch is **UNVERIFIABLE**. The supplied local image and MathML were inspected successfully. No access barrier was bypassed.

### Numbers, models and bibliographic claims in the prereg

| Claim | Status | Evidence / URL |
|---|---|---|
| Primary citation, DOI 10.1371/journal.pone.0166941, 2016, 11(11), e0166941 | MATCH | Local metadata; [publisher citation](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0166941), [PubMed](https://pubmed.ncbi.nlm.nih.gov/27870889/). e0166941 is an article identifier, not a page range. |
| Primary 50 studies; complete n = 99; aggregated n = 67 | MATCH | Abstract/sec009; sec007; S1 Text methods. [Publisher](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0166941). The 67 are source-described evaluations/aggregated effects, not generated testing fixtures. |
| Primary 0.75 (95% CI: 0.50, 1.00) | MATCH | sec010, Global analysis and publication bias. [Publisher](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0166941). |
| Primary global DL; R 3.0.3 / metafor 1.9-4 scoped to meta-regression | MATCH | sec007. Source package version uses an en dash. Global CI construction and separately scoped global software/version are NOT STATED. [Publisher Methods](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0166941). |
| Primary CC BY 4.0 | MATCH | Local XML and publisher licence link identify [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). |
| Fallback citation, DOI 10.1371/journal.pone.0216566, 2019, 14(5), e0216566 | MATCH | Local metadata; [publisher](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0216566), [PubMed](https://pubmed.ncbi.nlm.nih.gov/31067283/). |
| Fallback overall k = 49, g = 0.009, CI (-0.092, 0.109) | MATCH | sec032. [Publisher Results](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0216566). |
| Fallback moderator k = 78 | MATCH with scope | Explicitly printed for sec034's all-moderator meta-regression. Not an independently verified cluster count or a row count derived here. [Publisher Results](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0216566). |
| Domain-only Q = 26.732, p < .001; medical g = -0.267, CI (-0.430, -0.105), k = 15 | MATCH | sec033 and S4 Appendix. These are pooled/domain summaries; sec022 defines k as effects. [Publisher Results](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0216566). |
| Fallback random-effect overall, mixed-effect moderators, R/metafor family | MATCH | sec030/reference 61. Estimator, CI construction, R/package versions and exact summary construction NOT STATED there. [Publisher Methods](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0216566). |
| Fallback Attribution licence; local display lacks version | MATCH | Local permissions support that qualified statement. Publisher link currently resolves to [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), consistent with the narrower local-display claim. |

No numerical I2 value is quoted in the v4 prereg. Tolerances, seeds, rho values, decision thresholds and current package pins are prospective settings, not original-paper numbers. R_ENV/JOB_RULES support the supplied pins. The [maintainer's rma.uni reference](https://wviechtb.github.io/metafor/reference/rma.uni.html) confirms REML, z, GEN, intercept and weighted defaults; it does not establish historical use of unstated settings.

### Complete SOURCE_CHECK claim audit

Line references below are to C_P15_V4/out/supporting/SOURCE_CHECK_P15.md.

| Lines / claim group | Result and evidence |
|---|---|
| 3, review history | Retained v3 text/document lineage verified. Historical v4 execution remains its attributed record; content was independently inspected in this review. |
| 7 and 101-108, access/hashes | MATCH. FETCH_LOG records HTTP 200/OK for both XML and both ZIP files; all four hashes match local bytes. Both numerical-source DOCX hashes also match. Cached availability does not promise future network access. |
| 11-14, verdicts/licences | Primary FEASIBLE NOT ESTABLISHED, RT2-P15-01. Fallback aggregation limitation supported. Licence statements match. |
| 22, 25, 29, primary headers/identity/provenance | MATCH, trimming edge whitespace and rendering footnote letters inline. Sole S2 table, reference-list footnote and named fields readable. This is not certification of cluster independence. |
| 23-24, text/precision/scale | Text and three-decimal display MATCH. se's uncertainty convention remains UNRESOLVED; Eq. (3) justification for unchanged variance import is MISMATCH. |
| 26 and 51, S1 Text | MATCH. Methods, Results, Table A and Fig A caption exist; ICC aggregation and n = 67 evaluations are stated. Existing sensitivity is acknowledged, not represented as the registered CR2 method. |
| 27, targets/count locators | Values MATCH; 50-study locator needs RT2-P15-03. |
| 35, 41, 43, primary model quotations | All three sentences MATCH exactly after whitespace normalization, including citation numbers. Hedges' d: sec006; DL and scoped software sentence: sec007. |
| 37, caption/Eq. (3) concurrence | Caption wording MATCH. Claimed concurrence with unchanged variance import MISMATCH: MathML msqrt and local equation image establish the unresolved distinction. |
| 45-49, model/CI/direction/scale | Global DL versus separate REML meta-regressions, unstated global CI method, Fig 3 scatterplot and Figs 5-8 CI captions MATCH. Positive d means reduced road-kill. No ratio/log transformation is needed for printed d. This does not settle se. |
| 59-62, fallback files/headers/domain mapping | MATCH. S2 title/table; S1 list label; S3 headers and Financial/Interpersonal/Medical/Safety codes present. g/Variance are text with three decimals. S3 entries are coding definitions, not study rows. |
| 63-64, fallback gate/comparator | MATCH. sec032 overall target; sec033/S4 domain-only summaries; S4 headers blank label, k, g, CI, Q, p. sec034/Table 1 is the distinct simultaneous model. |
| 65, 85, 87-91, aggregation limitation | SUPPORTED AS OPEN CONDITION. sec030 names shifting-unit analysis without exact mean/variance/covariance construction; no separately identified overall gate input set is established. S2 is unaggregated, S3 definitions and S4 pooled breakdown do not supply the construction, and S5 is labelled PRISMA checklist. No universal absence claim is made. |
| 67, counts/formats | Published k = 78 and k = 15 MATCH with the scope above; repeated headers are structural. Required unaggregated numeric fields are not image-only. No data-row/independence count inferred. |
| 73, 77, 81, 83, 87, 89, fallback quotations | All six sentences MATCH exactly after whitespace normalization at sec029/sec030. Reference 61 identifies metafor. Printed package spelling retained. |
| 93, fallback direction/conversion | MATCH in sec029/Fig 2 caption. Printed g already carries source transformations and sign convention; it is not a ratio. |
| 95-99, gate/default/pins | 0.005/0.0005 are the stated half-last-decimal tolerances. Defaults and supplied pins match; no gate or statistical test run. |
| 112, novelty/primary disposition | 343 distinct IDs and attributed coordinator statement MATCH in original v4 inputs. RT2-P15-02 repairs provenance. Novelty does not clear uncertainty-scale feasibility. |
| 114, fallback disposition | MATCH to FREEZE_CRITERIA: inactive until independent checks and prospective reproduction specification clear; otherwise stop. |

Primary S2 header sequence, no data rows:

Study*; Country; Mitigation categorya; Study designb; Taxonc; Taxon or Species; Total study duration; Were data collected during construction of mitigation?; Road typed; Fence length; Was road-kill monitored beyond fence-ends?; NT; NC; d; se.

Fallback S2 header sequence, no data rows:

Author; Year; Study; Domain; Frame; Recipient; Design; Outcome; Publication; N (total); g; Variance.

Sources: [primary S2 Table](https://doi.org/10.1371/journal.pone.0166941.s003), [S1 Text](https://doi.org/10.1371/journal.pone.0166941.s001), [S1 Reference List](https://doi.org/10.1371/journal.pone.0166941.s007); [fallback S2](https://doi.org/10.1371/journal.pone.0216566.s002), [S3](https://doi.org/10.1371/journal.pone.0216566.s003), [S4](https://doi.org/10.1371/journal.pone.0216566.s004). Verification used supplied local files, not claimed fresh downloads of every attachment.

### Novelty evidence integrity

The original two logs match their recorded hashes: NOVELTY_pc2_2026-10-28.json, 54c69ad0ec27c6f16aec5e880266650c04bf62c2ca107276a474db97f94324d7; NOVELTY_openalex_2026-10-28.json, 05c3de75c25a627907fda403c1a671d4a363bcabec57b4ef58d375784e8140e2. P15 entries support Europe PMC 82/82 primary and 26/26 fallback; old OpenAlex 200/343 primary with HTTP 401 and 74/74 fallback; and zero results for each recorded title-truncated PubMed query. The original v4 paged file and job note have the hashes in finding 2. The seven-title disposition remains attributed; no per-title methods adjudication table exists in the supplied evidence. The old eight flagged metadata entries were not silently relabelled. Scholar remains recorded as blocked and was not retried.

## v3 comparison and protocol compliance

The adjacent C:/Users/User/ucjobs/B_P15_V3/out/ package was read directly. Its prereg SHA-256 is 4e8446d6c0502757086e777979179af5484c432b0a920110d87025aa6862a05d, matching the v4 lineage record.

- **Reproduction gates retained:** same outcomes/estimands/targets, each-endpoint tolerances 0.005/0.0005, fallback domain-Q check, no model/aggregation search and primary/eligible-fallback/stop.
- **Verification retained:** the entire detailed v3 section 5 body occurs verbatim in v4. Independent blind double extraction, family log check, third-model adjudication, fourth-pass family separation, operational headline definition, seeded 5% remainder/minimum one, >2% escalation, initials/date logs, approximately 25 minutes per ten-row packet, one packet weekly across papers, shared ledger, Mahmood's rota place, seven-day reassignment and newly-driving-row rechecks remain. Literal item-4 quotation is an addition.
- **New/robust definitions retained:** entire v3 section 8 body occurs verbatim. Absolute 0.10 shifts, [0.80,1.25] width band, all-rho rules, exact-zero boundaries, df<4, undefined-result and failed-agreement indeterminacy remain. Added ratio/deletion definitions reduce ambiguity.
- **Selection honesty:** same candidates selected from published relevance/dependence features, with no new calculation or predicted significance. Primary is an ecological/policy example, not a clinical-trial example. Existing ICC aggregation is acknowledged. No priority/ranking claim is made.
- **Eligibility constraints retained:** <=60 study clusters, estimated <=4 hours, one complete synthesis, no result-based subset, no primary-study reconstruction, fixed identity fields and unresolved-overlap stop. Published counts are not independently certified cluster counts.
- **Workflow/write-up rules:** rows remain confined to their own synthesis; fallback has its own fixed target/source and explicit triggers; write-up is 150-250 words plus one figure, with both outputs, indeterminate/failure reporting and Mahmood's paragraph. No clinical recommendations, extraction before release, author contact or access workaround is authorized.
- **Remaining choices:** the substantive unresolved choice is primary uncertainty meaning; do not determine it through a successful fit. Hash serialization is a minor reproducibility choice (finding 4). Fallback aggregation is inactive, not available for post-results selection.

V4 appropriately moved synthetic execution, runtime app/R parity, browser dependency closure, kit synchronization and packet assignment to mandatory post-release/pre-analysis conditions. Absent scripts may be implemented there because scientific settings are specified; subsequent code changes require dated, result-independent deviations. Fallback unavailability is expressly permitted as disclosure.

**The source-scale problem is not operational work.** V4 does not explicitly defer it: it claims it was resolved. Leaving that assertion would allow the later reproduction gate to stand in for F1. Resolve it before freeze or use the source-failure stop path. Missing runtime tests alone are not additional P0s.

## Static app evidence

Pin: 14dc545bcba87a02158b2f445c28450e7eaf6b89. Root: C:/Users/User/ucjobs/allmeta_14dc545/.

| File / functions | Capability | SHA-256 |
|---|---|---|
| rve-meta/index.html: run() 386; runSensitivity() 465; exportAction() 501 | Parser, rho/centring controls, CORR fit, grid, full-precision exports | 88d1494a0128ef5bd18e33e6b35ac0d13ae516044efd99354034ec1e953632eb |
| shared/rve.js: fitCORR() 369; clusterWeights() 433; summary() 602 | CORR weights, HTJ moment tau-squared truncated at zero, CR2, coefficient Satterthwaite df, two-sided t/95% CI | 75f9b201c6fd7f245a91e1712499044d519ab3dcb49bb7d49cef311d1ea6af0e |
| shared/rve-extras.js: parseStudies() 120; rhoSensitivity() 253; toRhoSensitivityCSV() 275; toRScript() 335; buildResult() 407 | se squared, vi retained, extras treated as predictors; fixed grid/refusals; precise exports | a66b55741c7c538aa69d45ef003ee452f52835db7d8d7ef7f1f639169f06041b |
| shared/rve-eigen.js: loadSync() 298; loadAsync() 314; eigen() 394 | Embedded WebAssembly eigensolver | a2a687c5127f6b5989d3b37e39fe4ae92849195dc6e1cbfe7befdd17352e239a |
| shared/stats-qt.js: pt() 87; qt() 97 | Student-t probabilities/quantiles | fb4110ba8e4b2e784193fde258ac37086713dc8d75a3295f84272d6fbdba8efb |

All eight script and two stylesheet imports resolve, including both hub files. All twelve APP_AUDIT hashes, including README and remaining dependencies, match. Default CR2, no registered tau override, and rho grid 0, 0.2, 0.4, 0.6, 0.8, 1 are implemented. The app R export is not the full workflow. Original reproduction, joint HTZ, deletion, classification, sampling/logging and figure are correctly R-only.

The older build-info SHA is disclosed rather than substituted for the pin. Automatic initial fitting and autosave restoration are present; synthetic validation must prevent bundled/restored inputs being fitted. Export precision does not certify runtime agreement at 1e-9. No browser, JavaScript, R or statistical model was executed.

## Open problems and handoff

- **Before freeze:** resolve RT2-P15-01 with permitted documentary evidence, fix mapping and correct source/status/blocker assertions; otherwise use source-failure/fallback/stop.
- **Document/evidence repairs:** package original novelty evidence (RT2-P15-02); repair the count locator (RT2-P15-03); fix sampling-key serialization before extraction (RT2-P15-04). The coordinator's title review remains attributed; detailed adjudications were not supplied.
- **Fallback:** exact within-study summary/variance/covariance construction remains unresolved. Full-workflow activation still requires independent feasibility/novelty clearance and a prospective reproduction specification.
- **Mandatory later work, not additional freeze blockers:** complete operational code/hashes; named and marked synthetic fixtures; pc2 synthetic validation and app/R parity; browser/WebAssembly/export closure; extraction/verification kit/logs; shared-ledger packet allocation. Review any later-delivered first-round APP_CHECK/REDTEAM reports; this second-round report now exists.
- **Release/later gates:** GitHub release, Zenodo archive/DOI, hashes and UTC freeze time are undone. Extraction, identity/overlap checks, independent-cluster/effort eligibility, human verification, original reproduction and classification have not occurred. No gate success or scientific result is claimed.

Only out/REDTEAM2_P15.md and out/VERDICT_P15.txt were written by this review. Upstream inputs and candidate files were not edited.
