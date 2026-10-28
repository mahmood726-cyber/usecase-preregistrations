# P08 v4 source and novelty audit — 2026-10-28

Pre-release screening only. No study-level rows are transcribed into this package and no clinical dataset or fitted results were produced. Files were read using Python. Forest images were read as bytes in Python and viewed at native resolution; ZIP/PDF structure and text were inspected in memory. This document supersedes the selection/model verdict in v3 SOURCE_CHECK, without changing original published numbers.

## F1 and source availability

**Veltkamp: FEASIBLE-IMAGE.** Figure 2 prints readable HR/OR estimates and confidence limits; Table 1 contains the AKI-group DM percentage and setting fields. The exact required fields are present in permitted supplied open sources. Image-reading/rounding risk goes into independent double extraction and verification. Actual independent complete-case k, missingness, variation and row mapping are not calculated before release.

**Liu: FEASIBLE-IMAGE for numeric access, conditional for activation.** Figure 4A prints the CRP SMDs/CIs; Table 1 contains follow-up values. Whether each value is treatment duration at the plotted CRP assessment, plus independent study/arm mapping, remains unresolved. Do not replace the registered duration estimand. Its own novelty and profile decisions must also clear before activation; otherwise stop.

Source roots are `C:/Users/User/ucsources/P08_primary/` and `P08_fallback/`. Both XMLs and supplementary archives are present. The primary nested archive contains `C.Figures_Supplements_S1_to_S6_20022025.pdf` (13 pages) and `C.Tables_Supplements_S1_to_S3_20022025.pdf` (11 pages). Figures S6A–C concern CKD incidence or kidney failure and do not specify the added joint model. The tables file covers search/exclusions/risk of bias. Liu's `Data_Sheet_1.docx` supplies search/risk-of-bias material, not new CRP inputs.

V3 records a timeout for the earlier primary supplementary fetch despite the current local archive being present. This job makes no claim about the undocumented later acquisition date/route. Mahmood's historical PMC block and the Scholar challenge were not bypassed or revisited. Current local readability supersedes an “unavailable supplement” claim, not the historical access log.

## Direct verification of permitted numbers and statements

| Registered fact | Direct source | Finding |
|---|---|---|
| HR 2.38 (95%CI 1.93–2.84) | Primary XML, Results sec4-3, and Figure 2 HR summary | Verified; unchanged |
| OR 2.92 (95%CI 2.64–3.20) | Same section and Figure 2 OR summary | Verified; unchanged |
| V3 “40 cohorts” | V3 SOURCE_CHECK/PREREG | Not independently located as a printed outcome-specific cohort count in the inspected text/image captions; not carried forward as a verified k |
| SMD: −0.34; 95% CI: −0.62, −0.07 | Fallback XML, sec24, and Figure 4A total | Verified; unchanged |
| Ten studies | Fallback XML, sec24 | Verified; not a computed completeness/independence result |
| I² = 37% | Fallback XML, sec24; Figure 4A | Verified; does not override the frozen figure-label precedence |
| Primary random effects; R 4.3.2/RStudio v.2023.09.1+494 | Primary Methods, sec3-5 | Verified; no statistical package, tau² estimator or pooling transformation identified |
| HR preference over OR for regression | Primary Methods sec3-5 and Figure 6 caption | Verified |
| Fallback RevMan 5.4; generic I² >50% rule | Fallback Methods sec13 | Verified |
| IV, Random, 95% CI; Z overall-effect test | Fallback Figure 4A | Verified from image |

The unsupported v3 count is a limitation of the earlier package, not a claimed discrepancy in a publication. Do not count forest lines as independent cohorts or alter a published number. Retain k=10–60, ≥5 per setting and every completeness/independence gate for primary regression.

## F3: single configuration, not model identification by fitting

The primary's original scale, SE construction, estimator and CI method remain **NOT STATED**. F3 explicitly permits fixing one reproduction configuration before data. The selected implementation is R/metafor, using its REML/z defaults; the article names R but does not name metafor. This implementation choice is ours. Natural ratio scale is fixed explicitly because the published pooled CIs appear approximately symmetric on that scale; this is an inference, not a confirmed author method.

The primary is therefore not rejected for unspecified original model details. Separate HR/OR panels use printed ratios, natural CI-width variances, inverse-variance weights, intercept-only REML/z and the exact controls in the prereg/R reference. No log-scale alternative, model search or variance reconstruction is permitted. Both point/CI triples must pass 0.005; otherwise primary → cleared fallback → stop.

The fallback's outcome-specific forest specifies random effects while generic Methods describe a heterogeneity threshold. Record both neutrally. Use the outcome-specific label, DL/z, identity SMD and printed CI-width variances. The added regression remains PM/floored HK, a different prespecified task.

Documentation checked in V4:
- [metafor rma.uni reference](https://wviechtb.github.io/metafor/reference/rma.uni.html): function signature gives REML, z, weighted/intercept models and level 95 defaults. This supports implementation defaults, not attribution to Veltkamp.
- [Cochrane Review Manager 5 algorithms](https://training.cochrane.org/handbook/current/statistical-methods-revman5): inverse-variance random-effects synthesis, DL heterogeneity and normal intervals. This supports the declared Liu default assumptions.

All tuning choices beyond estimator/inference are explicitly frozen in the R reference or the pinned package defaults, not chosen for agreement. Rounded printed inputs may prevent reproduction; that risk is retained.

## F2: supplied novelty evidence and bounded conclusion

The successful pc2 checks from 2026-10-28 found no equivalent application. We rely on that screening summary with disclosed limits; no new comprehensive search or independent full-text clearance is claimed. The two supplied JSON files contain counts and flagged records, not all citing records/dispositions or exact citation API request strings.

| Index / candidate | Exact query or retrieval identifier | Supplied result |
|---|---|---|
| Europe PMC / Veltkamp | MED / 40424522; DOI 10.1093/ndt/gfaf093 | cited_by 31; citations_retrieved 33; citations_hitcount 33 |
| Europe PMC / Liu | MED / 39166132; DOI 10.3389/fnut.2024.1434613 | 37; 37; 37 |
| OpenAlex / Veltkamp | W4410765724 citing works | cited_by_count 45; retrieved 45; complete true; error null |
| OpenAlex / Liu | W4401368310 citing works | 46; 46; complete true; error null |
| PubMed / Veltkamp | (meta-regression OR reanalysis OR re-analysis OR moderator) AND ("Long-term risks of adverse kidney outcomes after acute kidne") | 0 |
| PubMed / Liu | (meta-regression OR reanalysis OR re-analysis OR duration) AND ("Efficacy of probiotics/synbiotics supplementation in patient") | 2; 41102471, 35070839 |
| Scholar / Veltkamp, historical | (Veltkamp AND "acute kidney injury") AND ("meta-regression" OR reanalysis OR "re-analysis") | blocked; no negative-search inference |
| Scholar / Liu, historical | (Liu AND probiotics AND kidney) AND ("meta-regression" OR reanalysis OR "re-analysis") | blocked; no negative-search inference |

Primary flags: MED 41637990 / W7127111770, RIPK3 dose-response report; W7221515842, childhood-AKI reply. Titles alone are not a demonstrated equivalent study-level joint diabetes-plus-setting re-analysis. Fallback flag: MED 39758318 / W4405654446, Ruszkowski–Dębska-Ślizień commentary. V3's accessible-content assessment found no continuous-duration regression there; V4 does not adopt criticisms of a named publication. Source supplement captions do not identify either added model.

V3's additional direct PubMed access found 41102471 blocked, and no usable record content for 35070839/41637990. These are historical unsuccessful checks, not V4 independent clearances. Liu's two query hits remain an activation condition. Any subsequently confirmed equivalent excludes its candidate.

Binding deviation: Europe PMC and OpenAlex replace Google Scholar because its unusual-traffic bot check on 2026-10-28 was not bypassed. Missing full citing lists/dispositions is an F2 coverage/audit limitation disclosed in the prereg, not an automatic freeze failure.

## Provenance and limits

[FILE_HASHES_P08.json](FILE_HASHES_P08.json) records every supplied source file's SHA-256, source/job inputs and app assets. Primary XML: `6103b90bd8a9c2fe4b9f040bac284db31d5d0a6cfd99a067b85e2c1ed960e7e0`. Fallback XML: `b2ba7938c00f06a4a2a9c5c5a20863d09f12c84d246ffcd590b191df22e6814f`.

Primary target-journal placement supplies profile eligibility. Liu remains outside that journal; counts of 37 Europe PMC / 46 OpenAlex citations are evidence, not an invented “widely cited” threshold. A documented eligibility decision or dated protocol deviation is required before fallback activation. No primary-study lookup, contact, login, paywall workaround or blocked-route bypass was used.
