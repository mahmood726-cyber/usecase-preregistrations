# P13 source check — screening only

Date: 2026-10-28. Stage: pre-release. No study-level rows were transcribed, tabulated, paraphrased or analysed. Python read the supplied files; forest images were screened for headers, legibility and precision. Archives were inspected in memory with zipfile; no _unzipped directory was created.

**Verdicts: primary FEASIBLE-IMAGE; fallback FEASIBLE-IMAGE.** Both overall forests print readable integer numerators and denominators and verification estimates/CIs. Image feasibility does not establish an executable original-model specification, independent contributions, successful reproduction or permission to extract. The original models still block freeze.

## 1. Sources and access

Source roots: C:/Users/User/ucsources/P13_primary/ and C:/Users/User/ucsources/P13_fallback/. The supplied C:/Users/User/ucsources/FETCH_LOG.json records HTTP 200 / OK for every P13 item below. **No P13 item is recorded as BLOCKED.** Earlier retrieval failures are superseded by available local files. No access restriction was bypassed, and neither candidate needs another paper's blocked file. SHA-256 checks of all six logged P13 downloads matched FETCH_LOG.json.

| Candidate | Available file(s), relative to source root | Public locator |
|---|---|---|
| Primary | fulltext.xml | [Europe PMC XML, PMC13070644](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13070644/fullTextXML) |
| Primary | rkag034.pdf, final published article | [Published PDF](https://eprints.whiterose.ac.uk/id/eprint/238347/19/rkag034.pdf) |
| Primary | supplementary.zip; supp/rkag034f1.jpg; supp/rkag034_supplementary_data.zip | [Supplementary bundle](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13070644/supplementaryFiles) |
| Primary | Nested member RHEUMAP-2025-196.R2._ Supplementary Materials.docx; companion PRISMA checklist | Same bundle; inspected in memory |
| Primary | Supplementary_Materials_ACCEPTED.pdf | [Accepted supplement](https://eprints.whiterose.ac.uk/id/eprint/238347/6/Supplementary%20Materials%20ACCEPTED.pdf) |
| Fallback | fulltext.xml | [Europe PMC XML, PMC10597538](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10597538/fullTextXML) |
| Fallback | supplementary.zip; supp/rkad084f2.jpg; supp/rkad084_supplementary_data.docx | [Supplementary bundle](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10597538/supplementaryFiles) |

Canonical hierarchy: final published overall forest for contribution list, order, counts and estimates/CIs; final article/table and associated final supplement for assessment and identity context. The accepted primary supplement is corroboration only. Its **Supplementary Figure 2, PDF page 20 (internal page 19)** is an overall forest; the final DOCX's **Supplementary Figure 2** concerns subjective methods only. Do not interchange those locators or mix versions without a prospective, documented correspondence.

## 2. Primary: Almutairi, Greenwood and Sivan

DOI 10.1093/rap/rkag034; *Rheumatology Advances in Practice* 2026;10(2):rkag034; CC BY 4.0. Target: overall dysautonomia prevalence in chronic musculoskeletal pain, excluding healthy-control ratios and subgroups.

| Required input | Exact location / printed header | Readability / precision |
|---|---|---|
| Label and order | Final Figure 1, printed/PDF page 5; supp/rkag034f1.jpg; **Study** | Readable image; no label list recorded |
| Denominator n | Same figure; **Total** | Directly printed integers, zero decimals |
| Case count x | Same figure; **Number with Dysautonomia** | Directly printed integers, zero decimals |
| Prevalence and both CI endpoints | Same figure; **Prevalence % [95% CI]** | Image; integer percentages, zero decimals |
| Assessment, condition and identity context | Final Table 1, PDF page 4; XML table rkag034-T1 | Machine-readable headers: **Study (author, year)**, **Medical diagnosis**, **Sample size, n**, **Method used**, with **Subjective** / **Objective** subheaders |
| Selection / overlap policy | XML Methods sec9, Eligibility criteria; sec13, Data synthesis and prevalence estimation | Machine-readable Methods text |

Use the forest's matched Total, not a substituted Table 1 sample size. Published **k = 17**; the overall forest presents 17 contributions. Figure 1's numerical content is raster: the PDF has selectable caption/body text but an embedded forest image. The supplied JPEG is readable (742 × 587 pixels). Counts require independent image reading after release; do not infer them from rounded percentages.

Published pooled target: **64% (95% CI 51, 76; I² = 93%)**. The forest displays **64 [51, 76]** under the percentage header. Tolerance: **0.5 percentage points separately** for the pooled estimate and each endpoint. I² is reported, not an added gate endpoint.

Methods sec13 states:

> Quantitative data on the prevalence of autonomic dysfunction were pooled using random effects meta-analysis using the Freeman–Tukey transformed proportion to restrict estimates and confidence limits to a range of 0–100% [21].

> In cases where different autonomic domains or testing methods were reported separately rather than in combination, the most sensitive testing methods or outcome for detecting dysautonomia was selected for inclusion in the overall prevalence estimate.

Figure 1 caption states:

> Forest plot shows overall pooled prevalence estimates of dysautonomia in all included musculoskeletal conditions using validated objective and subjective methods

Eligibility criteria state that where participants overlapped another publication, the more recent publication was selected. That is a published policy, not independent certification of the final contributions. Preserve the forest's chosen assessment/denominator pairing; do not repeat the outcome-selection exercise.

## 3. Fallback: Tang, Singh and Fong

DOI 10.1093/rap/rkad084; *Rheumatology Advances in Practice* 2023;7(3):rkad084; CC BY-NC 4.0. Target: overall fatigue prevalence in axial spondyloarthritis, excluding predictors and subtype contrasts.

| Required input | Exact location / printed header | Readability / precision |
|---|---|---|
| Label and order | Final Figure 2; XML figure rkad084-F2; supp/rkad084f2.jpg; **Study** | Readable image; no local article PDF, so no PDF page assigned |
| Case count x | Same figure; **Fatigued** | Directly printed integers, zero decimals |
| Denominator n | Same figure; **Total** | Directly printed integers, zero decimals |
| Prevalence and both endpoints | Same figure; **Proportion**, **95%-CI** | Image; two decimals for proportions/endpoints |
| Weight, not required input | Same figure; **Weight** | One decimal in percent; never used to reconstruct variances |
| Assessment, definition, population and identity context | supp/rkad084_supplementary_data.docx; Supplementary Table S1, Characteristics of the studies; Table S2, Fatigue characteristics | Machine-readable tables |
| Selection / overlap policy | XML Methods, Study selection and Statistical analysis | Machine-readable text |

S1 includes **Study**, **Sample**. S2 headers are **Study**, **Fatigue Tool**, **Fatigue as Primary Objective**, **Fatigue Definition**, **AxSpA**, **r-AxSpA/AS**, **nr-AxSpA**, **Classification Criteria**, **HLA-B27 Positivity (%)**. Supporting entries were not copied.

Published **k = 30**; the overall forest presents 30 contributions. The numerical forest columns are image-only in supplied sources; the JPEG is readable (780 × 813 pixels). The DOCX provides context, not permission to replace the forest's selected counts.

Methods exclude repeated papers on the same cohort, prefer the overall combined axSpA estimate when available, and specify an instrument hierarchy: FACIT-F, Fatigue Severity Scale, SF-36, BASDAI fatigue question. Preserve the selected forest contribution rather than reselecting an instrument, subtype or timepoint.

Published abstract target: **0.56 (95% CI: 0.49, 0.63; I² = 94.6%)**. The forest displays **0.56 [0.49; 0.63]** and a more coarsely rounded **I² = 95%**. Retain both presentations as printed; the fixed estimate/CI gate is unchanged. Tolerance: **0.005 separately** for each component.

Statistical analysis states:

> All analyses were performed by H.T. using RStudio statistical software, v.2022.12.0.

> We calculated the prevalence and 95% CI to estimate the prevalence of fatigue in patients with axSpA.

> A random-effects model was used for the pooled estimate of fatigue because significant between-study heterogeneity was expected.

Figure 2 caption states:

> Pooled prevalence of fatigue in patients with axial spondyloarthritis

The pooled-model label is **Random effects model**. Its label and visual style do not identify a statistical package, function, tau² estimator or CI algorithm.

## 4. Original-model ledger and default-only gate

This ledger covers the inspected article Methods, overall captions and supplied supplements. NOT STATED is not replaced by an inferred method or by the registered new-analysis settings.

| Item | Primary | Fallback |
|---|---|---|
| Model class | Random effects | Random effects |
| Specific pooling estimator / weighting | NOT STATED | NOT STATED |
| Tau² estimator | NOT STATED | NOT STATED |
| Pooled CI: z/Wald or HK | NOT STATED; 95% level stated | NOT STATED; 95% level stated |
| Transformation | Freeman–Tukey stated | NOT STATED |
| Effect/variance formula; normalization | NOT STATED | NOT STATED |
| Inverse; any inverse sample-size parameter | NOT STATED | NOT STATED; identity cannot be assumed |
| Zero/all-event handling; continuity correction | NOT STATED | NOT STATED |
| Software / version | NOT STATED | RStudio v.2022.12.0; R version, statistical package/version and function NOT STATED |
| Reported effect scale | Prevalence percentage | Prevalence proportion |
| Natural versus log ratio pooling | NOT APPLICABLE to selected outcome | NOT APPLICABLE to selected outcome |

The primary's healthy-control ratio and fallback's predictor ratios are outside this registration. No claim about their pooling scale is made. CI symmetry does not resolve the selected outcome's missing transformation.

**V3 default rule:** for an unstated setting, prospectively fix the stated statistical software/function/version's documented defaults and try that one configuration after release. Label these as assumptions, not as statements about the paper. Do not search across estimators, transforms, CIs, inverses or versions for a match.

**Current limitation:** the primary names no statistical software/function; RStudio's version alone does not identify the fallback's statistical function or its defaults. Neither currently supplies a uniquely defined default configuration. Choosing meta::metaprop, metafor, DL/z or an inverse from plot appearance would be arbitrary. Before freeze, permitted published evidence must anchor one executable configuration, including variance and inverse conventions. If that cannot be done, model eligibility fails at the freeze decision: primary → fallback → stop. No real-data reproduction gate ran; no numerical failure is asserted.

## 5. Selection and limits

**Conditional selection: primary.** Both candidates pass the printed-input screen and the supplied novelty screen identifies no equivalent re-analysis. Neither currently passes full freeze eligibility. A failure of primary eligibility at the freeze decision invokes the fixed fallback, whose current model gap prevents automatic execution. No candidate is authorized for extraction.

Unique identity/assessment/denominator mapping and independent-contribution feasibility still need a documented resolution without pre-release row transcription. Published exclusion policies do not certify independence. After release, uncertain overlap, a missing field, conflicting sources or an unmappable contribution fails that candidate; never infer, omit or merge rows or hunt primary-study data.

All remaining freeze conditions are in [BLOCKERS_P13.md](BLOCKERS_P13.md). Image feasibility and rounded printed precision are recorded risks, not findings from a new analysis.
