# P11 source check and method specification — v4

2026-10-28. **Pre-release screening only: no study-level transcription, dataset, effect calculation or real-data analysis.** V3 inspected local files and image bytes with Python; v4 rechecked their hashes without transcribing study rows. Only locations, headers, readability, precision, permitted k and model statements are recorded. Existing unpacked supplements were used; no out/_unzipped directory was needed.

The input/model contracts here are incorporated into ../PREREG_P11_usecase.md and must accompany its release. Source feasibility does not certify reproduction, runtime or novelty clearance.

## 1. Verdicts and provenance

| Candidate | Step-1 verdict | Basis | Selection |
|---|---|---|---|
| Cevasco et al., DOI 10.1007/s10916-024-02059-x | **FEASIBLE** | Four analytical count columns readable as DOCX text; Figure 2 supplies readable cross-checks. | **Selected primary**, F1 satisfied. |
| Zhu et al., DOI 10.1007/s10741-019-09801-5 | **FEASIBLE-IMAGE** | Figure 2e prints both arms' events/totals and OR/CI; numerical inputs are raster-only. | Prespecified fallback; prior-analysis clearance remains open. |

C:/Users/User/ucsources/FETCH_LOG.json records HTTP 200 / OK for both XMLs and supplementary ZIPs. **No needed P11 file is marked BLOCKED.** Earlier REDTEAM download/screenshot failures remain historical access failures; the supplied public Europe PMC copies now permit screening. No blocked route was bypassed. Neither candidate needs the other's files.

Source roots: C:/Users/User/ucsources/P11_primary/ (PMC11004048) and C:/Users/User/ucsources/P11_fallback/ (PMC7046570). Public retrieval: [primary XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11004048/fullTextXML), [primary supplement archive](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11004048/supplementaryFiles), [fallback XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7046570/fullTextXML), [fallback supplement archive](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7046570/supplementaryFiles).

Python SHA-256 checks match FETCH_LOG for the four logged XML/ZIP files. Individual DOCX/image hashes identify the inspected files.

| Root | Relative file | SHA-256 |
|---|---|---|
| Primary | fulltext.xml | ba6e2b2a7cfc00de298c4260ba19dcc55a5888352abb46ef0934edea240ad769 |
| Primary | supplementary.zip | f60abf9630e95f12d470f52c4fca7271c1d830f9d02a9e8686bfb11bd9b8f70a |
| Primary | supp/10916_2024_2059_MOESM1_ESM.docx | 3ea5aa4529fd4a489741ba153fc013b2b0bdb4b9a70e2519bdbf813ddfd8e2f9 |
| Primary | supp/10916_2024_2059_Fig2_HTML.jpg | 4d7f2afbf6806c3baa9ae3f461e2389c0e7a40a5a04727f435c8aa8a77483c57 |
| Fallback | fulltext.xml | 3adac89f564031af95750fdfaeda96f6f84f432b7dd8993169c91a566db2a651 |
| Fallback | supplementary.zip | 40e478d965cf1bc4c73ce9b70b17025d82005939a8c9b8dcfef14bb5535572b6 |
| Fallback | supp/10741_2019_9801_Fig2b_HTML.jpg | 98889289037b2c2d5a41756518d5510e4d1998f0635970e89caa7a89a5beae71 |

## 2. Primary input locations

DOCX **Appendix D, “Results of individual studies”**, is the second table in word/document.xml. Description: “Trial arm details with trial arm retention, loss to follow-up frequencies, and moderator variables”. It has **k=14** body rows. No study identities or values are reproduced.

| Required input | Printed location/header | Representation and precision |
|---|---|---|
| Identity | Appendix D: Author; Figure 2: Author(s) and Year | DOCX text / image; reconcile mapping after release. |
| Intervention retained / lost | Appendix D: Chat Retain; Chat Loss | All required cells readable text integers; 0 decimals. |
| Control retained / lost | Appendix D: Control Retain; Control Loss | All required cells readable text integers; 0 decimals. |
| Comparison | Appendix D: Control arm type; Figure 2 control-type headings | Text/image; complete overall synthesis. |
| Ratio / CI cross-check | Figure 2, 10916_2024_2059_Fig2_HTML.jpg: RR [95% CI] | Readable image; 2 decimals. |
| Optional weight cross-check | Same figure: Weight | Image; percentage, 2 decimals. |

Other headers are Age (mean) and Incentive; neither is an analysis input. The count table has no footnote/endnote references and no separately printed analysis-total or administrative-loss column.

**Appendix C**, the first DOCX table, is a data dictionary headed Data element, Instructions, Description. Relevant definitions, not study rows:

> Arm N: “Number of subjects randomized into this trial arm. Adjust down randomized baseline for loss for eligibility, study errors or other non-participant attrition”

> Loss to follow-up: “Number lost to follow-up at end of study.”

> Admin Loss: “Loss to follow-up due to administrative reasons not attributed to user decision to continue with a trial. Will be removed from arm size and loss to follow-up results: (N)”

**Input contract:** a=Chat Retain, b=Chat Loss, c=Control Retain, d=Control Loss. Analysis totals are derived after release as a+b and c+d, never transcribed as separately printed totals. Use the published final retained/lost table. Do not reconstruct randomized totals, infer unprinted adjustment magnitudes or subtract administrative losses again. The adjustment policy is documented; individual unprinted adjustment magnitudes are not. Any post-release mapping contradiction fails the complete candidate. No primary-trial retrieval or row repair. The endpoint is the end-of-study retention synthesis in Figure 2.

## 3. Primary original model and defaults

Locations: fulltext.xml, Sec5 (Study Context), Sec7 (Data Analysis Methods), Fig2 caption. Verbatim statements:

> “We used a random effects meta-analysis to compare LTFU attrition rates between intervention and control groups.”

> “The metafor package in R was used to perform effect size estimate calculations and display forest plots and publication bias analyses [33].”

> “Differences between chatbot and control arm LTFU rates were assessed for heterogeneity using metafor with models fit using maximum likelihood estimators.”

> “We used log relative risk as the effect size measure by comparing the chatbot arm retention against total participants of the chatbot and control.”

> “Results were adjusted after randomization for loss for study eligibility, study errors or other non-participant attrition to determine if loss can be attributed to trial arms.”

Figure 2 caption:

> “Higher study subject trial retention has a higher risk ratio. The risk ratio is shown on a log scale indicated at the bottom of the figure”

| Item | Original evidence | Gate policy |
|---|---|---|
| Model / tau² estimator | Random effects; maximum likelihood | Inverse-variance ML; no REML substitution. |
| Effect / transformation | Log relative risk; retained participants | Log-RR; exponentiate estimate and CI for comparison. |
| CI level | 95% in Figure 2 | 95%. |
| CI construction: z or HK | **NOT STATED** | One default attempt: normal/Wald, test="z"; no HK alternative. |
| Variance formula / exact weighting implementation | **NOT STATED** | Default large-sample escalc variance and inverse-variance rma.uni. |
| Zero-cell handling | **NOT STATED** | Default 0.5 added to all four cells only in zero-containing tables; drop00=FALSE. Raw extracted counts remain unchanged. |
| Software | R, metafor | Run on pc2. |
| Original software versions / optimizer settings | **NOT STATED** | Pinned R 4.6.0 / metafor 5.2.1, unchanged ML optimizer defaults; no assertion about original versions. |

F3 permits exactly one declared software-default attempt for unstated items. Defaults are assumptions, not paper quotations. [metafor model documentation](https://wviechtb.github.io/metafor/reference/rma.uni.html) supports normal inference; [effect-size documentation](https://wviechtb.github.io/metafor/reference/escalc.html) documents variance/zero-cell defaults. Online documentation does not establish the original version; pc2 must check the pinned installed API during post-release, pre-analysis synthetic validation.

Published overall target: **0.99 (95% CI 0.95–1.03)**, **k=14**, **I² 64.3%**. Displayed ratio symmetry does not override explicit log-effect methodology.

## 4. Fallback input locations and original model

**Figure 2e is the middle panel of supp/10741_2019_9801_Fig2b_HTML.jpg.** Filename suffix 2b is not the panel letter: the image contains d, e and f. Use only e, **k=15**. Numerical inputs are readable, but image transcription remains a risk. Independent reading is permitted after release. No coordinate digitization or CI-derived SE substitution.

| Required input | Exact printed header/location | Representation and precision |
|---|---|---|
| Identity | Study or Subgroup | Image text. |
| Intervention deaths / total | Experimental over Events, Total | Image; integers, 0 decimals. |
| Control deaths / total | Control over Events, Total | Image; integers, 0 decimals. |
| OR / CI cross-check | Odds Ratio over M-H, Fixed, 95% CI | Image; 2 decimals; same header over numerical and graphical columns. |
| Optional weight cross-check | Weight | Image; percentage, 1 decimal. |
| Outcome / arm meaning | fulltext.xml, Fig2 caption, e | Machine-readable text. |
| Time / comparison context | fulltext.xml, Tab1, Description of included studies | Machine-readable text; mapping only. |

Table 1 has two header rows. The top row is Author/year; Study population (spanning three columns); Population; Type of interventions; Follow-up lengths; Outcome parameters; Jadad score. The three subheaders under Study population are N, Age (year), and Female (%). Population is a separate column. No study rows copied. *(Corrected pre-freeze per REDTEAM2 R2-01, 2026-10-28.)*

Input contract: a=Experimental Events, b=Experimental Total−a, c=Control Events, d=Control Total−c. Use the follow-up represented by Figure 2e. No telephone-support pool, alternate endpoint or new arm combination.

fulltext.xml, Sec8, Statistical analysis:

> “Separate analyses were performed for each outcome’s odds ratio (OR) or weighted mean difference (WMD) using the Mantel–Haenszel method.”

> “Pairwise meta-analyses were conducted by combining studies comparing the same interventions using a random-effects model.”

> “The analyses were carried out using Comprehensive Meta-Analysis techniques in Review Manager (RevMan, version 5.2, The Cochrane Collaboration, London, England, 2012) [12].”

Figure 2 caption:

> “e Effect of telemonitoring versus usual care on all-cause mortality in patients with chronic heart failure. CI, confidence interval; M-H, Mantel–Haenszel.”

**The panel prints “M-H, Fixed, 95% CI” and an overall Z test.** Preserve both this label and the general random-effects Methods statement without alleging a publication error. The outcome-specific panel label takes precedence prospectively: reproduce fixed MH once; do not try fixed and random alternatives for agreement. This explicitly amends v2's fallback description.

| Item | Original evidence | Gate policy |
|---|---|---|
| Estimator | MH in Methods/panel; fixed in panel | Fixed/common-effect MH OR. |
| Tau² method | **NOT STATED** for generic random-effects claim | Not estimated for the selected fixed-effect gate. |
| CI method | 95% and Z printed; exact CI variance formula **NOT STATED** | RevMan-style normal CI for log MH OR, exponentiated; no HK. |
| Pooling transformation / log versus natural | **NOT STATED** explicitly | MH combines cell-count components, not an inverse-variance log-OR average or natural-OR arithmetic average. Default inference uses log OR. |
| Software / version | RevMan 5.2 | R-only reproduction using meta 8.5.0; original did not report R. |
| Zero handling | **NOT STATED** | RevMan-style 0.5 correction to four cells of zero-containing tables, method.incr="only0", MH.exact=FALSE. |

The [meta authors' manual](https://guido-s.r-universe.dev/meta/doc/manual.html) documents RevMan-style corrections and common-effect inference. Check the installed meta 8.5.0 API during post-release, pre-analysis synthetic validation. V3 attempts at guido-s.github.io/meta/reference/metabin.html and settings.meta.html were unavailable; no bypass occurred, and the authors' public r-universe manual was accessible.

Published target: **OR 0.75, 95% CI 0.62–0.90**, **k=15**, **I² 49%**. No published number changes.

## 5. Normative code/ contract

These specifications were not run. The fixed contract below must be frozen with the preregistration. Independently authored executable scripts, pinned-API checks and synthetic validation are mandatory post-release, pre-analysis conditions. No prior CODE deliverable exists. Assert versions; record sessionInfo(). Validate inventory, independence, count ranges, positive denominators and finite effects/positive variances. Contradictory mapping or default exclusion reducing fixed k fails the candidate. Keep lexical values separate from derived/corrected analysis cells.

### One original-result attempt per candidate

Primary, R 4.6.0 / metafor 5.2.1:

    dat <- metafor::escalc(measure="RR", ai=a, bi=b, ci=c, di=d,
                           add=0.5, to="only0", drop00=FALSE, vtype="LS")
    original <- metafor::rma.uni(yi=dat$yi, vi=dat$vi,
                                method="ML", test="z", level=95,
                                intercept=TRUE, weighted=TRUE, control=list())

Fallback, meta 8.5.0 in a clean process:

    meta::settings.meta("RevMan5")
    original <- meta::metabin(event.e=a, n.e=a+b, event.c=c, n.c=c+d,
      sm="OR", method="MH", common=TRUE, random=FALSE,
      incr=0.5, method.incr="only0", MH.exact=FALSE, allstudies=FALSE,
      level=0.95, level.ma=0.95, method.common.ci="classic",
      method.tau="DL", Q.Cochrane=TRUE, prediction=FALSE,
      backtransf=TRUE)

Use only exponentiated TE.common, lower.common and upper.common. DL fixes an ancillary software calculation; it is **not** the gate estimator or a claimed original tau² method. The package may calculate random-effects fields internally; do not inspect/use them to select a model. If default double-zero/double-all exclusion reduces the fixed inventory, fail rather than silently dropping the row.

Require **absolute difference ≤0.005 separately** for pooled ratio and each CI endpoint, exact k and resolved direction. No rounding to manufacture agreement. Only independently verified transcription corrections permit rerunning the identical model. No estimator, scale, correction, input-source or tolerance search.

### App / independent R diagnostics

After the gate, primary uses its count-derived log-RRs. Fallback uses the same a/b/c/d mapping with metafor::escalc(measure="OR", add=0.5, to="only0", drop00=FALSE, vtype="LS"). Both app and R use these log effects.

Independently author the R calculation before comparing the exported script, implementing the pinned scalar-score initialization:

    start_tau <- function(y, v) {
      score <- function(t) {
        w <- 1/(v+t); mu <- sum(w*y)/sum(w)
        sum(w*w*(y-mu)^2) - sum(w) + sum(w*w)/sum(w)
      }
      if (score(0) <= 0) return(0)
      hi <- max(var(y), max(v), 1e-8)
      while (score(hi) > 0) hi <- hi*2
      uniroot(score, c(0, hi), tol=1e-14, maxiter=1000)$root
    }
    ctl <- list(tau2.init=start_tau(yi, vi), maxiter=10000, stepadj=1)
    ctl$threshold <- 1e-12*max(1, ctl$tau2.init)
    res <- metafor::rma(yi, vi, slab=study, method="REML",
                       test="z", level=95, control=ctl)
    code <- "x$control$tau2.init <- start_tau(x$yi[-i], x$vi[-i]); x$control$threshold <- 1e-12*max(1, x$control$tau2.init)"
    loo <- metafor::leave1out(res, code2=code)
    inf <- stats::influence(res, code2=code)

Reset starts/thresholds and re-estimate tau² per deletion. Transfer yi and sqrt(vi) at round-trip precision in fixed row order. Record the app/exported script's SE-to-variance round trip. Use unrounded numerical exports.

Compare full/deletion estimate, SE, CI, test statistic, p-value, tau², I², H², Q/Q p-value; studentized residuals, DFFITS, Cook's D, covariance ratio, hat, weight and DFBETAS. Require abs(app−R)/max(1,abs(R)) ≤1e-6, except Q/Q p-value ≤1e-9. Row identity, k, exclusion state and flags match exactly; CI category and S_i≥0.5 classification must also agree. Nonfinite output, non-convergence or unresolved numerical/category mismatch is unresolved even if two missing values match. No optimizer/tolerance switching.


## 6. V4 execution and evidence boundaries

This companion is normative for source mapping, transformations, original-model gates and the independent REML calculation; [APP_EVIDENCE_P11.md](APP_EVIDENCE_P11.md) supplies current static capability/dependency evidence. The obsolete v3 missing-hub and pre-freeze runtime requirements are superseded. No script or runtime pass is asserted.

All unspecified analytical arguments retain the pinned package defaults in a clean R process (no user profile, restored workspace or changed options beyond the explicitly declared RevMan5 setting); no optional subset, moderator, cluster, custom weights or fixed tau². No choice may be revised after data inspection. Assert R 4.6.0, metafor 5.2.1 and meta 8.5.0 and save sessionInfo(). An API incompatibility or failed synthetic validation stops real-data work; any code change after release is a dated deviation based only on synthetic evidence.

For the original primary fit, compare exp(coef(original)), exp(original$ci.lb), exp(original$ci.ub), without rounding. For fallback use the exponentiated common-effect fields specified above. Preserve raw cells and cross-checks exactly; derived analysis counts/variances carry separate provenance. Treat the a/b/c/d mappings above as fixed, never outcome-dependent choices.

For diagnostics the independent R run uses the original count-derived vi; record separately the app/exported-R round trip (sqrt(vi))² and require the stated full parity checks against the independent result. No replacement of the independent input with browser output to manufacture agreement. Keep all effects and standard errors at round-trip precision.

Transport study labels as P11_ plus their four-digit forest position (for example P11_0001, an administrative example only), with a bijective map to the full row key and exact raw printed label. This avoids comma/newline parsing changes. Verify the map, complete fixed inventory, order and exclusions exactly at import and export. Identity comparison is of the mapped row key, never display-label similarity.

The generic exported R checker accepts matched NA values; that is insufficient here. The independent P11 validator must reject every nonfinite required quantity and additionally check all exact identity, exclusion, flag and CI/S decisions. Classification, headline selection, seeded sampling, source verification and original ML/MH gates are R-only/procedural; the influence page does not implement them as a complete workflow. Auxiliary Baujat/radial output generated by the page/exporter is not an additional registered endpoint.

The official [escalc documentation](https://wviechtb.github.io/metafor/reference/escalc.html) and [rma.uni documentation](https://wviechtb.github.io/metafor/reference/rma.uni.html), accessed 2026-10-28, support the declared effect-size defaults and normal inference. The [meta manual](https://guido-s.r-universe.dev/meta/doc/manual.html) supports the RevMan-style MH correction contract but currently identifies version 9.0-0: it is not proof of the installed 8.5.0 API. Pinned-environment checks remain mandatory before real-data gates. No original software version or unstated original choice is inferred from these current manuals.
