# P15 source check v6 - 2026-10-28

Pre-release. Python inspection was restricted to S2 headers, captions, general methods/formulas, metadata and static app code. The S2 header check preceded any scale computation; no observation values were inspected or extracted. Neither the scale check nor any real-data model was run. Exact source containers are retained as evidence, not an extraction dataset. Numerical display assessments below are attributed to the supplied prior review.

## Access and verdicts

All required local documents were readable; no download, login or fresh database query occurred. [Evidence manifest](EVIDENCE_SHA256.md).

| Candidate | Verdict | Reason |
|---|---|---|
| Primary: Rytwinski et al. (2016), DOI 10.1371/journal.pone.0166941 | **FEASIBLE under the binding v6 decision** | S2 prints both group sizes, NC and NT, alongside d and se. The complete deterministic scale rule is fixed before extraction and must pass after release/verification, before reproduction. No row classification is claimed now. |
| Fallback: Batteux et al. (2019), DOI 10.1371/journal.pone.0216566 | **NOT FEASIBLE for the complete registered workflow currently** | Readable unaggregated inputs do not supply the original overall within-study aggregation/variance/covariance construction. |

Primary F1 is cleared by the supplied [decision](evidence/V6_JOB_P15.md), not by a documentary assertion that se already means SE or variance. Fallback status is unchanged; it needs independent feasibility/novelty and a prospectively fixed complete reproduction specification, otherwise stop. Both sources carry Attribution licences; the primary links version 4.0, whereas the fallback's displayed statement does not specify its version.

## Primary source locations

The relative source below is [primary fulltext.xml](evidence/primary/fulltext.xml). `supp/` in the exact review replacement denotes the original attachment locator; byte copies here are directly under `evidence/primary/`.

| Input | Exact file/location and printed header | Format/precision |
|---|---|---|
| Identity | [S2 Table](evidence/primary/pone.0166941.s003.docx), sole table, `Study*`; footnote “*Studies cited in S1 Reference List.” [S1 Reference List](evidence/primary/pone.0166941.s007.docx) | Text; preserve identity and group dependent outcomes. Independence remains a later check. |
| Effect | Same table, `d` | Text; three-decimal display documented in the supplied review. |
| Uncertainty | Same table, `se` | Text; three-decimal display documented in the supplied review. Actual precision retained per row; apply the registered deterministic check before assigning vi. |
| Provenance | Same table, `Mitigation categorya`, `Study designb`, `Taxonc`, `Taxon or Species` | Not predictors in the registered intercept-only model. |
| Scale-check group sizes | Same table, `NC` (n1), `NT` (n2) | Printed headers confirmed without observation values; required verified inputs after release. |
| Existing dependence sensitivity | [S1 Text](evidence/primary/pone.0166941.s001.docx), Methods, Results, Table A and Fig A caption | ICC aggregation to 67 evaluations; not the registered CORR/CR2 analysis. |
| Original model, pooled target and published counts | fulltext.xml: sec006 for effect definition; sec007 for global DL and complete dataset n = 99; sec010 for 0.75 (95% CI: 0.50, 1.00); abstract and sec009 Description of studies, corroborated by the S2 Fig caption, for 50 studies | Published synthesis counts; the pooled target has two decimals. No independent-cluster count has been derived. |

The final row is the exact RT2-P15-03 replacement. All S2 headers, trimming edge whitespace and rendering footnote superscripts inline: `Study*`, `Country`, `Mitigation categorya`, `Study designb`, `Taxonc`, `Taxon or Species`, `Total study duration`, `Were data collected during construction of mitigation?`, `Road typed`, `Fence length`, `Was road-kill monitored beyond fence-ends?`, `NT`, `NC`, `d`, `se`. Only the structural header was emitted during v6 inspection; no observation cells were inspected.

## RT2-P15-01: documentary verification and binding replacement

The [current item 9](evidence/MAHMOOD_DECISIONS.md) and [v6 job](evidence/V6_JOB_P15.md) replace the earlier documentary-only resolution requirement with the [deterministic scale rule](SCALE_CHECK_P15.md). The rejected fixed-SE proposal in the archived [v5 job](evidence/V5_JOB_P15.md) and the blocked [review](evidence/REDTEAM2_P15.md) remain historical evidence.

Supporting evidence, quoted without study-level data:

- The source table header is exactly `se`. It accompanies `d`; the header alone does not determine units.
- [Primary fulltext.xml](evidence/primary/fulltext.xml), sec006, `disp-formula` id `pone.0166941.e005`, printed label `(3)`, contains MathML `msqrt`. Its general equation, preserving the radical, is:

  `se = sqrt[(n_G1 + n_G2)/(n_G1*n_G2) + d^2/{2*(n_G1 + n_G2)}]`

  The unchanged [equation image](evidence/primary/pone.0166941.e005.jpg) was read with Python and displayed; it confirms the radical. SHA-256: `ab6746b845b0dfe18016d8a170d1ee8120ab1a517a223c5830b01789ec6a1d16`. This is a general formula, not a reconstructed study value.
- Fulltext XML, S2 Fig caption (`pone.0166941.s005`):

  > Relationship between effect sizes (d) and standard error to assess publication bias.

  > Dashed line is the summary mean-weighted effect size from random-effect meta-analysis across 99 effect sizes from 50 studies.

Conflicting evidence, quoted exactly (inline formatting flattened, words unchanged):

- [S2 Table DOCX](evidence/primary/pone.0166941.s003.docx), caption outside the table:

  > S2 Table. Studies included in the meta-analysis and associated countries, mitigation categories, study designs, taxa, species or lowest level taxonomic groups, total study durations (years), whether or not data were collected during construction of the mitigation measure, road types, fence lengths (m), whether or not road-kill was monitored beyond the ends of the fencing, impact (NT = impact sites or after monitoring period) and control group (NC= control sites or before monitoring period) sample sizes, effect sizes (d), and variances for d (se).

- Fulltext XML, sec006, immediately introducing that same displayed Eq. (3):

  > The sampling variance of is given by:

The source wording remains conflicting. Neither variance wording establishes a variance mapping, nor the radical establishes what every table cell instantiates. Unlike the rejected v5 proposal, v6 does not claim that only the table caption conflicts or that the units are already known.

**Header-only finding:** NC and NT are printed. Methods defines group 1 as control/before and group 2 as impact/after; the S2 caption identifies NC and NT accordingly. Set n1=NC, n2=NT. This checks availability of the columns, not completeness or validity of their unseen values.

**Prespecified rule:** after release, extraction and verification, before any reproduction gate, compute A=sqrt[(n1+n2)/(n1*n2)+d^2/(2*(n1+n2))] and B=A^2 for every S2 observation. For printed se with p decimals, t=(1/2)*10^(-p); at three decimals t=0.5*0.001=0.0005. Keep trailing zeros; exponent e gives t=(1/2)*10^(e-p). Compare abs(se-A)<=t and abs(se-B)<=t without intermediate rounding. Only the first match is SE, only the second VAR, both AMBIGUOUS, neither NONE. All SE gives vi=se^2; all VAR gives vi=se. Any AMBIGUOUS, NONE, missing n or mixed classes stops the primary. Invalid required inputs also stop; no row exclusion, imputation or alternate mapping is allowed. [Exact boundary arithmetic and audit requirements](SCALE_CHECK_P15.md) are fixed now.

Preserve printed n, d and se strings; record derived quantities separately. No pooled result enters the decision and neither mapping can be tried as an alternative on the gate. Gate failure cannot change it. Continue only to the independently cleared fallback, otherwise stop. This binding algorithm replaces RT2-P15-01 rather than claiming a successful real-data check.

## Original primary model

Fulltext XML sec006:

> We used the standardized mean difference (Hedges’ d) as our effect size measure [32, 33]:

Sec007:

> To determine whether mitigation measures reduce road-kill, we first conducted a random-effects meta-analysis using the DerSimonian-Laird method [37, 38] to determine the summary weighted-mean effect size using the complete dataset (n = 99).

> Meta-regression analysis was conducted in R 3.0.3 [41], using the ‘metafor’ package (version 1.9–4) [42].

Global DL is stated; REML pertains to separate meta-regressions. Global CI method and a separately scoped global software/version statement are **NOT STATED**. The single registered attempt is DL/z with GEN, intercept, inverse-variance weighting and pinned default controls, after eligibility clears. The z choice is a software-default assumption, not a historical claim. No search follows mismatch. The [review](evidence/REDTEAM2_P15.md) records the software-default documentary check; [R pins](evidence/R_ENV.txt) fix implementation versions.

Positive d means reduced road-kill. Printed d already contains standardization and small-sample correction. No recalculation or ratio/log transformation is registered. S1 Text's “synthetic” effects aggregate real studies; they are not permitted test fixtures.

## Fallback locations and unresolved prerequisite

| Input | Relative evidence and locator | Status |
|---|---|---|
| Identity | [S2 Appendix](evidence/fallback/pone.0216566.s002.docx), `Author`, `Year`, `Study`; [S1 Appendix](evidence/fallback/pone.0216566.s001.docx), study list | Preserve study/experiment identifiers; dependence and overlap remain later checks. |
| Effect/uncertainty | S2, `g`, `Variance` | Readable text; three-decimal display assessment retained from the review. |
| Domain | S2, `Domain`; [S3 Appendix](evidence/fallback/pone.0216566.s003.docx), `Moderator`, `Code`, `Definition` | Financial reference; Medical/Safety to medical; interpersonal indicator. |
| Provenance | S2, `Frame`, `Recipient`, `Design`, `Outcome`, `Publication`, `N (total)` | Not additional covariates. |
| Overall gate | [Fulltext XML](evidence/fallback/fulltext.xml), sec030/sec032 | k = 49, g = 0.009, CI (-0.092, 0.109). |
| Domain-only comparison | Fulltext sec033 fixes the registered target Q = 26.732, p < .001. S4 Appendix, sole table, “Moderator: Domain”, separately prints Q = 27.666, p < .001; it does not corroborate the main-text Q. S4 headers are blank label, k, g, CI, Q, p. | The unaggregated medical summary agrees across these locations: g = -0.267, CI endpoints -0.430 and -0.105, k = 15 (S4 uses square brackets). Preserve both printed Q values. Use only the already registered main-text Q = 26.732 with tolerance 0.0005; never substitute S4's value after seeing a reproduction. This is distinct from Table 1/sec034's simultaneous model. |
| Missing overall construction | Fulltext sec030 | Shifting-unit aggregation/variance/covariance rule and complete summary inputs remain unresolved. |

S2 headers: `Author`, `Year`, `Study`, `Domain`, `Frame`, `Recipient`, `Design`, `Outcome`, `Publication`, `N (total)`, `g`, `Variance`. Published moderator `k = 78` and medical `k = 15` refer to effects, not verified independent clusters. Repeated headers are structural.

Exact model quotations retained from the reviewed source, sec029/sec030:

> We then transformed all effect sizes to Hedge’s g which corrects for biases in small samples and is recommended for use in meta-analyses [56].

> All analyses were performed in R using the metaphor package [61].

> We used the random-effect model to compute the overall effect size of self-other differences rather than a fixed-effect model as the design and measures of included studies varied significantly.

> We used mixed-effect models for the moderator analyses.

> Summary effect sizes for these studies were computed using Cooper’s ‘shifting-unit-of-analysis’ method [64].

> We did not use this method in moderator analyses as studies included multiple effect sizes because these related to different moderators; it did not make sense to compute a summary effect size in such cases.

Package spelling is preserved; reference 61 identifies metafor. Estimator, CI construction, R/package versions and exact summary construction are **NOT STATED**. One REML/z attempt is specified only after permissible published material resolves aggregation through a prospective amendment. Software defaults do not supply a missing aggregation algorithm. Unaggregated pooling cannot replace the overall gate. Positive g means greater risk-taking for others; use printed g without repeating original transformations.

## Gates and disposition

Primary estimate and both CI endpoints must agree within 0.005; fallback estimate/endpoints and domain Q within 0.0005. These gates follow eligibility, required verification and the primary scale check. No gate has run. Source rounding never authorizes altered inputs, wider tolerances or a different scale mapping.

Novelty retains F2 clearance with bounded coverage: [paged metadata](evidence/NOVELTY_openalex_P15primary_paged_2026-10-28.json) has 343 distinct IDs; [v4](evidence/V4_JOB_P15.md) and [v5](evidence/V5_JOB_P15.md) notes attribute the seven-title screening to pc2. The older eight flagged entries do not supply a mapped adjudication of those seven. See the [novelty log](NOVELTY_LOG_P15.md) for queries, limits and Scholar substitution.

Primary source verdict is FEASIBLE under the current decision. [F1-F6 assessment](../V5_NOTES_P15.md) supports [BLOCKERS = NONE](../BLOCKERS_P15.md). This is a freeze candidate for the next REDTEAM2 round, not a release, classification, scale-check pass or scientific result. Fallback remains unavailable. Operational code, synthetic validation, runtime parity, browser closure, extraction-kit synchronization and packet allocation remain mandatory later conditions under [FREEZE_CRITERIA](evidence/FREEZE_CRITERIA.md).
