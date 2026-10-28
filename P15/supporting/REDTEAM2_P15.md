# REDTEAM2 P15 — review of the v6 freeze candidate

Date: 2026-10-28. Candidate: F_P15_V6/out/, as required by the current JOB.md (superseding REDTEAM2.md's generic v4 target).

**Verdict: FREEZE_OK. No P0 identified for the primary route.** The deterministic Eq. (3) rule is fully specified and implementable from the printed S2 column types. It leaves no choice of scale based on pooled results. This is a freeze judgment, not permission to extract before release or evidence that the actual rows will pass. The fallback remains unavailable.

There is one P1 documentary correction and two P2 handoff improvements below. None opens a scientific choice or fails F1–F6 for the primary. The P1 must be corrected before the source-check statement is reused or the fallback is activated.

Candidate references below are relative to F_P15_V6/out/. Review output links refer to this out/ directory.

## 1. Findings and exact replacement text

1. **RT2B-P15-01 — P1: separate the two printed fallback domain-Q locations.**

   Evidence: supporting/SOURCE_CHECK_P15.md:93 joins fulltext sec033 and S4 Appendix as support for Q = 26.732. Main-text sec033 prints that number and p < .001. However, the supplied S4 Appendix, sole table, “Moderator: Domain” row, prints **27.666** and **<.001**. Its medical subgroup summary does match g = -0.267, CI [-0.430, -0.105], k = 15. These are published pooled/model summaries, not study rows.

   The main-text value was also verified on the [publisher Results page](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0216566). S4 is the [publisher-listed supplement](https://doi.org/10.1371/journal.pone.0216566.s004); its local bytes match the candidate evidence copy, SHA-256 446943c616263527b6eda7232e1b92435d396c5f07d058e1e6844a30d8147db9.

   This finding concerns the registration's source attribution. Neither printed number is altered and no publication is labelled as containing an error. Prereg sections 3 and 6 already fix the main-text target, so the disagreement does not create a post-data choice. The fallback is independently blocked by its unresolved aggregation construction.

   Replace SOURCE_CHECK line 93 with:

   > | Domain-only comparison | Fulltext sec033 fixes the registered target Q = 26.732, p < .001. S4 Appendix, sole table, “Moderator: Domain”, separately prints Q = 27.666, p < .001; it does not corroborate the main-text Q. S4 headers are blank label, k, g, CI, Q, p. | The unaggregated medical summary agrees across these locations: g = -0.267, CI endpoints -0.430 and -0.105, k = 15 (S4 uses square brackets). Preserve both printed Q values. Use only the already registered main-text Q = 26.732 with tolerance 0.0005; never substitute S4's value after seeing a reproduction. This is distinct from Table 1/sec034's simultaneous model. |

   Add immediately after the domain-Q sentence in prereg section 6:

   > The domain-Q target is exclusively the main-text sec033 value 26.732. S4 Appendix separately prints 27.666; retain it as source context, never as an alternative gate target. Failure against 26.732 invokes the unchanged stop rule.

   The archived prior REDTEAM2 report's blanket statement that sec033/S4 both match this Q should be annotated by this review, not silently rewritten as historical evidence.

2. **RT2B-P15-02 — P2: make the comparison-to-v3 evidence limit explicit.**

   Evidence: the actual B_P15_V3, C_P15_V4 and F_P15_V5 preregistration files are not present in the supplied package or the expected adjacent directories on this node. The embedded historical REDTEAM2 report records a direct v3/v4 comparison and v3 SHA-256 4e8446d6c0502757086e777979179af5484c432b0a920110d87025aa6862a05d. V6 notes:72/98 claim v5 section retention. Those are attributable records, not independently repeatable byte comparisons here. Current thresholds agree with the historical report, and no weakening is apparent; an exact direct v3-to-v6 comparison is **UNVERIFIABLE on this node**.

   Add after V5_NOTES_P15.md:72:

   > Historical comparison provenance: the archived REDTEAM2 report records its direct v3/v4 comparison; the v6 validation record reports its v5/v6 comparison. The predecessor preregistration files are not included in this portable package. A reviewer with this package can compare the recorded specifications, but cannot independently repeat the claimed byte-for-byte section comparisons. Preserve or link the exact predecessor preregistrations and hashes when available; until then retain this limitation.

   This is an evidence-packaging improvement, not an additional freeze criterion or a reason to invent a new gate.

3. **RT2B-P15-03 — P2: point packet allocation explicitly to the live shared ledger.**

   Evidence: prereg:67 labels a link to supporting/evidence/COAUTHOR_LOAD.md as the shared ledger. That archived file still has an empty ledger, whereas the supplied job-level COAUTHOR_LOAD.md contains a planned P11 assignment. No participant/study details are reproduced here. V6 notes:87 already correctly says the evidence ledger is only a snapshot. Manifest integrity passes; this is ordinary administrative drift, not corrupted evidence.

   Replace prereg:67 with:

   > Budget approximately 25 minutes per ten-row packet, including instructions; split larger assignments. No co-author receives more than one packet weekly across papers. Coordinate assignments through the live pipeline/COAUTHOR_LOAD.md shared with P14/P06, including Mahmood in the rota. The bundled supporting/evidence/COAUTHOR_LOAD.md is a historical snapshot and must not be used to determine current availability. Reassign packets after seven days, never skip them. Corrections require rerunning gates and diagnostics until newly driving rows are checked.

   No assignment or message was sent by this review.

## 2. F1–F6 decision

| Criterion | Judgment | Evidence and limits |
|---|---|---|
| F1 — feasible chosen candidate | **PASS under the binding item-9/header-only decision** | S2's first structural row prints Study*, NT, NC, d, se. Caption and sec006 establish NC/control-before and NT/impact-after. Eq. (3)'s MathML and unchanged image contain the specified radical. SCALE_CHECK:33–79 fixes the future classification and stop paths. This does not certify completeness or a common scale for unseen observations. The current decision explicitly permits that prospective check. |
| F2 — novelty | **PASS with disclosed coverage/provenance limits** | Europe PMC/OpenAlex logs, the paged file and coordinator dispositions are portable and hash-verified. Primary paged file has 343 records and 343 unique IDs. Prereg:132–145 discloses the Scholar substitution, old cursor failure, truncated PubMed queries, index coverage and absent detailed title adjudications. No fresh comprehensive novelty search or independent methods-level adjudication is claimed. |
| F3 — original model fixed | **PASS** | Prereg:71–86 fixes one primary DL/z attempt, metafor 5.2.1/R 4.6.0, GEN/intercept/weighted/default controls, no alternative scales/models/weights/subsets, and primary → independently cleared fallback → stop. DL is stated; global z inference is explicitly an assumption. The fallback has no permission to proceed with an unspecified aggregation rule. |
| F4 — complete analysis/outcomes | **PASS** | Sections 4, 7, 8 and SCALE_CHECK fix scale arithmetic, thresholds, cluster identities, formulas, reference indicators, rho/grid, CORR moment heterogeneity, CR2/Satterthwaite, R-only HTZ/deletion, 1e-9 agreement and new/robust/indeterminate categories. Exact zero, interval boundaries, df<4 and failed diagnostics are covered. The inactive fallback has a single fixed domain-Q target despite the P1 citation correction. |
| F5 — verification | **PASS** | Prereg:53 is an exact match to current MAHMOOD_DECISIONS item 4, checked programmatically. Sections 5/8 provide the detailed blind double extraction, family checks, adjudication/fourth pass, headline-row rules, seeded 5% sampling, >2% escalation, packet caps and reassignment. Raw NC/NT/d/se strings are required fields. |
| F6 — static app capability | **PASS, static only** | All 12 APP_AUDIT file hashes match both the supplied pinned snapshot and archived copies. Functions and settings inspected below implement the registered app analysis. All ten direct dependencies exist. Scale checking, original reproduction, HTZ, deletion, classification, sampling/logging and figure remain R-only. |

**Post-release classification is appropriate.** Operational code implementation, synthetic execution, app/R runtime parity, browser dependency closure, extraction-kit synchronization and packet assignment are expressly post-release/pre-analysis conditions in FREEZE_CRITERIA. V6 retains those obligations and requires synthetic validation before real-data reproduction. Missing operational code is not itself an F4 failure when its scientific choices are already fixed.

The previous unresolved-scale blocker is replaced by a binding, fully specified rule; it has not merely been renamed an optional later condition. Failure stops the primary before pooling. Fallback aggregation is an honestly disclosed inactive-route limitation expressly allowed by FREEZE_CRITERIA. No other F1–F6 failure was found hidden among later conditions.

## 3. Adversarial review of the Eq. (3) rule

**Source availability.** Python read only the first structural row of the primary S2 observation table and its external caption/notes. The exact header sequence is:

Study*; Country; Mitigation categorya; Study designb; Taxonc; Taxon or Species; Total study duration; Were data collected during construction of mitigation?; Road typed; Fence length; Was road-kill monitored beyond fence-ends?; NT; NC; d; se.

NT and NC are actual printed columns; the check does not require reconstructing sizes from other sources. The table has one table container. Presence is not a claim about every observation's valid sizes. No S2 observation values or counts were extracted for this review.

**Formula.** XML sec006, disp-formula pone.0166941.e005, label (3), has msqrt encompassing both terms. The unchanged JPEG was read through Python and visually inspected; it agrees:

A = sqrt[(n1+n2)/(n1*n2) + d²/{2(n1+n2)}], B = A².

Fixing n1=NC and n2=NT agrees with the caption and method; the formula is symmetric. The source's variance wording and S2 Fig's standard-error wording remain disclosed. Neither wording is used to select a scale in advance or override later classification.

**Precision and boundaries.** With p mantissa decimal places and exponent e, t = 0.5 × 10^(e−p); ordinary decimals have e=0. At three decimals t=0.0005. Trailing zeros count, integers give t=0.5, and indeterminate formatting stops. The rule fixes use of printed n and d without propagating their rounding or rounding the computed forms.

For positive s and C=(n1+n2)/(n1*n2)+d²/[2(n1+n2)], the proposed exact comparisons are valid:

- SE match iff max(0,s−t)² ≤ C ≤ (s+t)².
- VAR match iff |s−C| ≤ t.

These use only rational arithmetic on finite printed decimals; no exact irrational square-root implementation is required. Both inclusive endpoints, both matches, neither match, invalid inputs and empty data are determined. A and B cannot be made equal by premature rounding.

**Dataset decision.** All SE → every vi=s²; all VAR → every vi=s. Any mixed/ambiguous/none/missing/invalid set → STOP. No majority rule, nearest-scale rule, exclusions, imputation or pooled-target input exists. The app receives a single validated vi column, preventing its se-header conversion from choosing a second scientific mapping. Mapping is logged before the single reproduction; failure cannot cause a second mapping attempt.

**Independent synthetic probe.** [synthetic_scale_probe.py](synthetic_scale_probe.py) generates invented fixtures in memory; its first line marks “SYNTHETIC - not data”. [synthetic_scale_probe.txt](synthetic_scale_probe.txt) records **63 passing synthetic assertions**. Coverage includes SE/VAR/both/neither, missing/nonfinite/nonpositive inputs, mixed/empty sets, exponent/trailing-zero precision, exact inclusive boundaries and values immediately outside, the lower-bound clamp, and prevention of an alternative mapping after a stub gate fails.

This is evidence that the written rule is mathematically executable, not a result about the candidate. It neither runs nor validates the future R implementation, the real extraction, a fitted model or app/R parity. It uses no source rows and no candidate values. The rule may stop on rounded inputs even when a different rounding treatment would match; v6 deliberately fixes that conservative outcome and forbids relaxation.

## 4. Published-number and source audit

Web search and publisher/PubMed checks ran on 2026-10-28. Exact source text was additionally checked in the supplied XML/DOCX files using Python. Printed pooled summaries are reproduced below without alteration; synthesis counts are never substituted for independently verified cluster counts. No numerical I² is quoted in the v6 preregistration, so there is no I² claim to audit. Seeds, rho, gate tolerances, classification cutoffs and installed package pins are prospective specifications, not original-paper results.

| Preregistered original-paper claim | Status | Location / URL |
|---|---|---|
| Primary full citation, DOI 10.1371/journal.pone.0166941; 2016; 11(11):e0166941 | MATCH | Local article metadata; [publisher citation](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0166941); [PubMed](https://pubmed.ncbi.nlm.nih.gov/27870889/). The e-number is an article identifier, not a page range. |
| Primary 50 studies, complete n = 99, aggregated n = 67 | MATCH | Abstract/sec009 and sec007; S1 Text Methods. [Publisher Methods/Results](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0166941). The source's “synthetic” aggregation is real-study analysis, not a permitted test fixture. |
| Primary 0.75 (95% CI: 0.50, 1.00) | MATCH | sec010; [publisher Global analysis](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0166941). |
| Primary Hedges' d; positive indicates reduced road-kill | MATCH | sec006 and [publisher Methods](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0166941). |
| Primary random-effects DL; R 3.0.3/metafor 1.9–4 named specifically for meta-regression | MATCH | sec007 and [publisher Data analysis](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0166941). Global CI method/separately scoped global software version are not stated there. |
| Primary CC BY 4.0 | MATCH | XML permissions and [publisher licence link](https://creativecommons.org/licenses/by/4.0/). |
| Fallback citation, DOI 10.1371/journal.pone.0216566; 2019; 14(5):e0216566 | MATCH | [Publisher citation](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0216566), [PubMed](https://pubmed.ncbi.nlm.nih.gov/31067283/), local metadata. |
| Fallback overall k = 49, g = 0.009, CI (-0.092, 0.109) | MATCH | sec032; [publisher Results](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0216566). |
| Fallback unaggregated k = 78 | MATCH, scope-qualified | Printed in sec034 for all-moderator meta-regression; [publisher Meta-regression](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0216566). It is not a verified independent-study count or a count derived here from S2. |
| Domain-only Q = 26.732, p < .001 | MATCH to main text; MISMATCH to the asserted S4 corroboration | sec033/[publisher Moderator analyses](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0216566). S4 prints 27.666. See RT2B-P15-01; the fixed gate remains 26.732. |
| Medical unaggregated g = -0.267, CI (-0.430, -0.105), k = 15 | MATCH | sec033 and S4 Medical row under Moderator: Domain. S4 uses brackets around the same endpoints. These are pooled effects, not independent-cluster counts. |
| Fallback random-effect overall, mixed-effect moderators, R/metafor family, within-study aggregation for overall only | MATCH | sec029/sec030 and [publisher Methods](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0216566). Reference 61 identifies metafor; the quoted “metaphor” spelling is retained. |
| Fallback Attribution licence; displayed local statement lacks a version | MATCH | Local permissions text and [publisher licence statement](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0216566). The underlying link identifies CC BY 4.0; the qualified display-text statement is not a denial of that link. |

The [metafor maintainer reference](https://wviechtb.github.io/metafor/reference/rma.uni.html) documents the named defaults, including GEN, REML, weighted=TRUE, intercept=TRUE and test="z". It supports the single prospective fallback/default configuration, not a historical claim about unspecified settings. The package versions actually required for later execution remain those in R_ENV.txt. R-only joint-test use is consistent with the [clubSandwich maintainer documentation](https://jepusto.github.io/clubSandwich/reference/Wald_test.html); no runtime check was performed.

### Complete SOURCE_CHECK claim coverage

Line references are to the candidate's supporting/SOURCE_CHECK_P15.md.

| Lines / claim group | Independent assessment |
|---|---|
| 3–14: scope, access, licences, verdicts | Local evidence containers are readable and hash-consistent; version histories remain attributed. Primary feasibility follows the binding prospective rule, not known row classification. Fallback unavailability is correctly disclosed. No claim of freshly downloading every attachment is made by this review. |
| 18–30: primary locations, identity, headers, counts | MATCH for sole S2 table, all named headers, the S1-reference footnote, S1 Text Methods/Results/Table A/Fig A, and sec006/007/009/010 locators. The corrected 50-study locator is accurate. Independence is not inferred. |
| 23–24, 89 and retained-review statements: numerical text/display claims | The prior-review attribution is present and verifiable. Actual observation-by-observation three-decimal formatting is UNVERIFIABLE in this header-only review; no numerical observation cells were inspected. V6 expressly uses each row's actual printed precision, so the inherited display statement does not control the classifier. |
| 34–43: authority and Eq. (3) | MATCH. Current item 9 and V6_JOB specify the rule; MathML and original JPEG show the radical. Equation-image SHA-256 matches ab6746b845b0dfe18016d8a170d1ee8120ab1a517a223c5830b01789ec6a1d16. |
| 44–62: captions and conflicting wording | MATCH after whitespace normalization: both S2 Fig sentences, the complete DOCX caption, the incomplete “The sampling variance of is given by:” sentence, and NC/NT/G1/G2 meanings. No missing word was supplied. |
| 64–66: rule and stop paths | MATCH to SCALE_CHECK and the current binding decision; exact boundary mathematics is valid. All decisions precede pooling. |
| 70–82: primary model quotations/direction | All three quoted sentences at lines 72, 76, 78 MATCH their respective source sections programmatically after whitespace normalization. DL/REML scopes are separated correctly. Positive direction and use of already corrected printed d match. Historical unstated global CI settings remain an acknowledged assumption. |
| 88–91, 96: fallback sources/headers/codebook | MATCH: S1 is the study list; S2 is the unaggregated table; S3 is the codebook. Headers and Financial/Interpersonal/Medical-Safety coding definitions are readable. No per-study moderator rows were copied. |
| 92: fallback overall target | MATCH to sec032 and S4 Main Effects/All studies. |
| 93: fallback domain-only target | PARTIAL MISMATCH: location/model distinction and medical summary match; S4 does not print the registered Q. Exact correction is RT2B-P15-01. |
| 94, 108–112: aggregation prerequisite | SUPPORTED AS OPEN CONDITION. sec030 names shifting-unit aggregation without an executable mean/variance/covariance construction. Readable unaggregated S2, S3 definitions and S4 summaries do not establish an overall gate input set. This is not a claim that every possible source was searched. |
| 98–112: six fallback model quotations | All six quoted sentences at lines 100, 102, 104, 106, 108, 110 MATCH sec029/sec030 programmatically after whitespace normalization. Reference 61 names metafor. Missing estimator/CI/version/aggregation details remain appropriately unstated. |
| 114–116: gates | MATCH to fixed decimal precision and prereg: primary 0.005; fallback endpoints and domain Q 0.0005. No widened tolerance or alternative target is allowed. |
| 118: novelty | Metadata counts, raw-log hashes and coordinator-note wording MATCH. The seven-title disposition remains attributed. No independent per-title methods adjudication or mapping from the earlier eight flagged entries is supplied. |
| 120: status and later conditions | Consistent with the primary F1–F6 assessment and fallback-stop route, subject to the documentary corrections above. Code/runtime/extraction/release readiness is not claimed. |

Fallback S2 header sequence, checked without observation values: Author; Year; Study; Domain; Frame; Recipient; Design; Outcome; Publication; N (total); g; Variance. S3 headers are Moderator; Code; Definition. S4 headers are blank label; k; g; CI; Q; p.

## 5. Protocol compliance and historical comparison

- **Fixed selection and outcome:** one complete primary synthesis, ecological/policy question within the target journal, selected using published relevance and dependence. No inference is made that clustering will reverse a result. The original dependence sensitivity is acknowledged.
- **Eligibility/effort:** at most 60 independent study clusters and four hours; reported study/effect counts are distinguished. Unresolved identity/overlap prevents eligibility. No data-dependent subset or primary-study reconstruction is authorized.
- **Fallback/stop:** own outcome, source, target and method are named; triggers include source/scale failure, equivalent re-analysis and reproduction failure. It activates only after independent clearance and a prospective aggregation specification. Otherwise stop, with all failures reported.
- **Reproduction:** same fixed pooled targets, both CI endpoints, 0.005/0.0005 tolerances and fixed main-text domain Q; no ratio transformation, estimator search or scale retry.
- **Analysis:** same cluster rules, intercept-only primary/domain-only fallback formulas, indicator order, centring off, rho=0.8 and grid {0,0.2,0.4,0.6,0.8,1}; CR2, Satterthwaite, two-sided Student-t intervals; independent R packages agree with manuscript context. The use-case's 1e-9 finite-result agreement is not relaxed to the software manuscript's separate undefined-output convention.
- **New/robust:** absolute 0.10 shifts, width-ratio band [0.80,1.25], all-rho reporting, exact-zero definitions and df<4/undefined/failed-agreement indeterminacy remain explicit. Primary robustness requires strictly positive CIs. Failure cannot be relabelled a substantive finding.
- **Verification:** item 4 is exact; headline checks include all rows in flagged clusters, ≥0.10 coefficient shifts, ≥10% width changes and ≥10% weight share. Remainder sample is SHA-256 ordered using the specified UTF-8 row key and seed 2026102815; minimum one when a remainder exists; escalation is >2%, not ≥2%. Blind independent AI extraction, third-model adjudication and different-family fourth pass precede unresolved-field human review. Human initials/date, ≤30-minute packets, one per week and seven-day reassignment are retained. Later diagnostic-driven verification is expressly required before reporting; SCALE_CHECK:33 makes that sequencing clear.
- **Honesty/write-up:** rows stay within their source synthesis; both outcomes are reported; 150–250 words plus figure, existing use case retained, Mahmood's final paragraph, no clinical advice or priority claims. Historical source quotations do not authorize prohibited claims.
- **Release:** GitHub release, archive/DOI conditions, hashes/time and prospective deviation logging remain mandatory before extraction. The short original writing-length aim was superseded by later package development; v6's length is not an F1–F6 failure.

The archived review documents unchanged v3/v4 gates, detailed verification and numeric categories. V6 agrees with those documented specifications; current item-4 equality is directly checked. The known change is the expressly authorized deterministic scale rule plus stricter serialization/provenance. Direct predecessor byte comparison remains unavailable (RT2B-P15-02); no assertion of an independently verified v3-to-v6 diff is made.

## 6. Static app and evidence integrity

Pin: 14dc545bcba87a02158b2f445c28450e7eaf6b89, supplied ALLMETA snapshot.

| File / functions | Verified implementation | SHA-256 |
|---|---|---|
| rve-meta/index.html — run:386, runSensitivity:465, exportAction:501 | Exact parser route, centring/rho controls, CORR fit, fixed sensitivity grid, full-precision exports | 88d1494a0128ef5bd18e33e6b35ac0d13ae516044efd99354034ec1e953632eb |
| shared/rve.js — fitCORR:369, clusterWeights:433, summary:602 | CORR weights, HTJ moment tau² truncated at zero, CR2/Satterthwaite, two-sided t and 95% intervals | 75f9b201c6fd7f245a91e1712499044d519ab3dcb49bb7d49cef311d1ea6af0e |
| shared/rve-extras.js — parseStudies:120, rhoSensitivity:253, toRScript:335, buildResult:407 | se squaring versus vi import, extra-column predictors, ID coercion, exports/count semantics and partial R export | a66b55741c7c538aa69d45ef003ee452f52835db7d8d7ef7f1f639169f06041b |
| shared/rve-eigen.js — loadSync:298, loadAsync:314, eigen:394 | Embedded WebAssembly eigen dependency | a2a687c5127f6b5989d3b37e39fe4ae92849195dc6e1cbfe7befdd17352e239a |
| shared/stats-qt.js — pt:87, qt:97 | Student-t dependency used by summary | fb4110ba8e4b2e784193fde258ac37086713dc8d75a3295f84272d6fbdba8efb |

All 12 app hashes match the archived audit and original snapshot. Eight direct script imports and two stylesheets resolve, including both hub files. No JS, browser, R or real-data model was executed. The older build stamp and automatic fit/restored-input hazards are disclosed by v6 and still need controlled synthetic runtime checks.

All 36 evidence-manifest entries match their recorded sizes/hashes. Of 31 entries with counterparts directly available on this node, 30 are byte-identical; the only difference is the current administrative COAUTHOR_LOAD ledger versus its historical snapshot, as described in RT2B-P15-03. This does not invalidate the archived manifest. All original primary/fallback source copies, all app files and all three raw novelty logs match. All 128 current-document relative links resolve.

Candidate prereg SHA-256: 239f98983381c51f9eaa5ec34aa23bd43be7afac19c79f7c513269262c3f0e4f.
Candidate SCALE_CHECK SHA-256: 668c20f7d4e2fc20c57548f842dd3d130468affdac48ea546fdb1523085ead9b.
Synthetic probe SHA-256: 81c7ce672ed4d3e54ab06597bcb7628a4886d9d512d6c4fa4989e3897c175554.
Synthetic log SHA-256: 951cab067d06edadd833ad80e865996c4c9370666112f3a0048446e99323b0cc.

## 7. Open problems and review limitations

1. Correct the fallback Q attribution (P1); preserve both printed numbers and the existing main-text gate. Resolve the P2 historical-comparison disclosure and live-ledger pointer.
2. Actual primary NC/NT completeness, se display precision, row classifications and a uniform mapping are unknown. Execute the fixed check only after release, extraction and required verification, before reproduction; failure stops the primary.
3. Fallback aggregation/variance/covariance construction remains unresolved. Its independent feasibility/novelty and prospective complete reproduction clearance are required before activation; otherwise it remains unavailable.
4. Full operational R code and hashes remain absent. Implement and validate exact arithmetic, imports/identity checks, models, gates, grid, classification, deletion and verification logic on marked generated synthetic fixtures. This review's Python probe does not discharge that obligation. Post-release code changes must be dated and independent of real results.
5. App/R parity at the stated tolerances, every rho including endpoints, WebAssembly/browser loading, parser/refusal behaviour and full-precision exports remain untested. Prevent bundled/restored data from automatically fitting.
6. Synchronize extraction/verification kits and NC/NT/raw-string fields; allocate packets against the live shared ledger; complete independent model-family checks, adjudication, human checks and later newly-driving-row rechecks.
7. Freeze/release hashes and UTC time, GitHub release and Zenodo archive/DOI remain undone. Cluster independence/overlap and effort eligibility, original reproduction, app/R comparison and classification remain unperformed.
8. Novelty coverage remains bounded; the seven-title methods dispositions and their mapping to eight older flagged entries are not documented individually. Scholar's historical block was not bypassed or retried. First-round REDTEAM/APP_CHECK outputs and predecessor preregistration files remain unavailable here; review them if delivered.

**Review-process exception:** while reading static app code, an overbroad index.html range unintentionally displayed pre-existing bundled example rows in the tool transcript. This departed from the intended header/method-only read discipline. They were not used, fitted, treated as synthetic fixtures, copied into review artifacts or used to choose any specification. No candidate S2 observation rows were extracted. The transcript cannot be redacted through the available tools; this limitation is recorded rather than claiming that no numerical rows were ever displayed.

All actual file reads/writes used Python. The only analytical code executed was the independently generated synthetic probe. Web work was read-only, with no contact, login or barrier bypass. No upstream source, candidate document, app or decision file was changed. The verdict file contains exactly FREEZE_OK on one line.

Written files: REDTEAM2_P15.md; VERDICT_P15.txt; synthetic_scale_probe.py; synthetic_scale_probe.txt.
