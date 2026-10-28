# P12 v4 evidence: sources, novelty, capabilities and dependencies

Date: 2026-10-28. This is screening/static evidence, not an extraction dataset, reproduction pass or runtime certification. All local reads used Python. No per-study rows were transcribed or analysed. No browser or R code was executed, no web search was rerun, and no blocked endpoint was bypassed.

The v3 inputs are `B_P12_V3/out/PREREG_P12_usecase.md`, `SOURCE_CHECK_P12.md`, `CHANGELOG_P12.md` and `BLOCKERS_P12.md`. Their hashes and the governing instruction/novelty-log hashes are recorded in [DEPENDENCIES_P12.json](DEPENDENCIES_P12.json). V4 carries forward source readability from that screening and verifies that all six source files remain byte-identical. It does not claim a new image-reading pass.

## 1. F1: fixed sources and source risk

| Candidate | Screening verdict | Authoritative numerical source and required fields |
|---|---|---|
| Cheema primary | FEASIBLE-IMAGE | Figure 3, `P12_primary/supp/nutrients-14-01600-g003.jpg`; `Study or Subgroup`, numerical `Risk Ratio / IV, Random, 95% CI`; exact label/order and printed effect/lower/upper endpoints. Panel `Cheema2022_Fig3_VAP`. |
| MacKinnon fallback | FEASIBLE-IMAGE | Figure S8, PDF/printed page 36 of `P12_fallback/supp/cc9-6-e1140-s001.pdf`; `Study or Subgroup`, numerical `Std. Mean Difference / IV, Random, 95% CI`; exact label/order and printed effect/lower/upper endpoints. Panel `MacKinnon2024_FigS8_hospitalLOS`. |

V3 inspected the primary 774 x 393 JPEG and the fallback's 1696 x 571 embedded forest image. Both have readable numerical endpoints printed to two decimals; neither has a direct SE column. The primary's earlier publisher-PDF locator is page 8; the image file itself is authoritative. Fallback Figure S8 is the single observational hospital-LOS forest on page 36, with no A/B panel choice. Main tables are identity/context checks only, never substitute numerical inputs.

The primary pooled target is RR 0.68 [0.55, 0.84], k = 18; the fallback target is SMD -0.19 [-0.36, -0.03], k = 11. These are published pooled summaries, not extracted rows. The normal/log CI-to-SE conventions, no-reconstruction rule, unique source-order IDs and stop rules are frozen in the preregistration and contract.

V3's source check records ordinary Europe PMC HTTP 200 / OK downloads for full text and supplements, with CC BY 4.0 (primary) and CC BY-NC-ND 4.0 (fallback). It reports no required P12 manual download. Earlier blocked publisher/browser attempts remain historical blocked attempts. The primary's nested extra supplement is unnecessary for Figure 3 and was not unpacked.

Permitted source provenance:
- Primary [full-text XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9031795/fullTextXML) and [supplementary archive](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9031795/supplementaryFiles).
- Fallback [full-text XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11338257/fullTextXML) and [supplementary archive](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11338257/supplementaryFiles).

Measured SHA-256, paths relative to `C:/Users/User/ucsources`:

| File | SHA-256 | Matches v3 |
|---|---|---|
| P12_primary/fulltext.xml | `3786bd746ba8bc01fda37f2119a6c0ef57550d3e5d0e6116321993cfe5f6c3ad` | Yes |
| P12_primary/supplementary.zip | `952c094067f4e273624a8656642eb9a1c3a6f83377e1e135960478bfa00c06f0` | Yes |
| P12_primary/supp/nutrients-14-01600-g003.jpg | `b0e03517d09e80a12e11aa98a116bd069338ae5cbe96a7087536219c47fba07c` | Yes |
| P12_fallback/fulltext.xml | `08c3846719737d3253d086b3a5175ff73ecf737576c7f54a1432eeace86ed148` | Yes |
| P12_fallback/supplementary.zip | `81b8af8341d6d567f33a568f3f9ad4f26ed447911d4cc268a32e604fb5fccf44` | Yes |
| P12_fallback/supp/cc9-6-e1140-s001.pdf | `ade2ff6ed53fec6ee10cd2fb42fa2745618de863ebe069f4b6eadb751e709098` | Yes |

Image reading remains a risk carried into independent double extraction and human verification. Two-decimal rounding may prevent the unchanged 0.005 reproduction gate from passing. Readability does not establish source-row independence, correct contrast mapping or numerical reproduction. Those checks remain prospective and cannot justify prerelease extraction.

## 2. F3: statements, missing details and one fixed default attempt

The unchanged v3 SOURCE_CHECK records these source model statements:

Primary, Methods 2.6: "We used DerSimonian and Laird random-effects model to perform meta-analyses." It names Review Manager (RevMan, Version 5.4). Figure 3 states IV, Random, 95% CI and prints an overall Z test. Jamovi 1.8 / MAJOR is separately named for asymmetry, not the pooling calculation.

Fallback, Data Synthesis and Analysis: "We used the DerSimonian and Laird (23) inverse-variance method to estimate effect sizes for each outcome using a random-effects model." It names RevMan 5.4, Stata/MP 15.1 and RStudio 1.4.1106; the latter is an IDE version, not a package/R version. Figure S8 states IV, Random, 95% CI and prints an overall Z test.

The exact CI algorithm, explicit log-RR pooling statement, fallback forest-to-software assignment, original R/package versions, detailed zero-cell convention and fallback SMD variant remain NOT STATED. Do not relabel them source-confirmed. V3's default rationale cited [Cochrane, Statistical algorithms in Review Manager 5](https://training.cochrane.org/handbook/current/statistical-methods-revman5), PDF page 8, for log-ratio pooling and normal CIs; this is inherited documentary support, not a fresh retrieval.

F3 permits exactly one prospective configuration based on the stated RevMan 5 software/defaults. V4 keeps IV DL, log RR/unchanged SMD, classic normal 95% CI and printed effect/CI inputs, without reconstruction, new continuity correction or alternative method/software search. Remaining choices are fixed in CONTRACT sections 2, 3, 6 and 8. Gate failure means primary, cleared fallback, stop. The fallback's other named programs do not supply alternative attempts.

## 3. F2: approved novelty checks and their coverage

The supplied logs dated 2026-10-28 are the evidence for this review; their P12 records are copied structurally, without modification, into DEPENDENCIES_P12.json. The binding deviation replaces Scholar with Europe PMC/OpenAlex because Scholar returned "unusual traffic" on 2026-10-28; no bypass was attempted.

| Candidate | Europe PMC citation lookup | OpenAlex citation lookup | Additional logged PubMed query |
|---|---|---|---|
| Cheema | MED/35458162; cited_by 28; hitcount 31; retrieved 31; flagged titles 0 | W4223940454; cited_by_count 45; retrieved 44; complete true; error null; flagged 0 | 7 records |
| MacKinnon | MED/39162653; cited_by 4; hitcount 4; retrieved 4; flagged titles 0 | W4401716073; cited_by_count 3; retrieved 3; complete true; error null; flagged 0 | 0 records |

Literal PubMed queries:
- Primary: `(limit meta-analysis OR small-study OR publication bias OR reanalysis OR re-analysis) AND ("Probiotics for the Prevention of Ventilator-Associated Pneum")`
- Fallback: `(limit meta-analysis OR small-study OR publication bias OR reanalysis OR re-analysis) AND ("Impact of Rounding Checklists on the Outcomes of Patients Ad")`

The seven primary PubMed IDs are retained in the JSON evidence. No equivalent beta0 application to the same fixed outcome and included synthesis was identified in the approved checks. This is not proof of absence or an independent full-text citation audit. Different methods, subsets and updated syntheses are distinct from the registered equivalence definition.

Counts describe different metadata/retrieval fields; preserve the differences and do not sum overlapping indexes. In particular, complete=true does not turn 44 retrieved into 45. Full citing-record inventories and full request URLs are not supplied and are not reconstructed. V3 also reports earlier blocked v2 PubMed/Scholar attempts; those remain unsuccessful historical attempts, not zero-hit searches. Their original v2/REDTEAM records are not in this workspace. These disclosed coverage limitations are not F2 failures under FREEZE_CRITERIA. Confirmed future overlap still activates the prospective exclusion/clearance rule.

## 4. F6: measured file/function evidence

App root: `C:/Users/User/ucjobs/allmeta_14dc545`. Supplied commit: `14dc545bcba87a02158b2f445c28450e7eaf6b89`. Line numbers below refer to Python-read source lines in that snapshot. SHA-256 identifies the exact bytes; no app files were changed.

| File | Functions / source lines | Registered capability or boundary | SHA-256 |
|---|---|---|---|
| limit-ma/index.html | parse (208), pool (240), dl (250), radialReg (272), limitMA (300), run (358), drawFunnel (432), AlmLimitEngine.fit (680) | Strict finite positive-SE input; IV DL, beta0, normal CIs, diagnostics and funnel/curve. run auto-executes at 766–773; do not launch with real examples. | `5d5f1a705d5228014f684dd77eb98a950ed582a8175321835a8bed90792866d3` |
| limit-ma/plus.js | compute (78), chisqSF (31), tp (29) | DL comparison, authoritative full-fit internal-REML status; Q tests, Egger t/df/p, shift and G2. Other automatically computed methods are outside inference. | `91097a304ac7e82dcbcc7b57fb4659cb87b5abb8ac2fe796f15580d65968975e` |
| limit-ma/plus-opt.js | AlmLimitPlusMLStart (32) | Fixed internal REML convergence check on shrunken estimates; preserve refusals and original controls. | `869e65ce474846c4d483d9451f3b7e41478f7e7b36fd17cba4ebad2d7c765b8e` |
| limit-ma/plus-ui.js | current (80), run (91), AlmLimitPlusUI.snapshot (99) | Strict current-input parsing, comparison execution and raw state/results capture; exceptions clear comparison state. | `7576d7b450257e1d37d908265bc7150c1f39d756551ba4803dcf78217ad14f26` |
| limit-ma/loo-limit.js | check (7), deletion (10), compute (27), csv (41), invalidate (48) | Every deletion refits beta0 with REML check, SE/CI, ordinary point estimate, tau2 and status/reason; validated k domain 4–200. Ordinary deletion SE/CIs are absent from its export. | `27c45750a00443e059a1ca01af51e1be99512a13e659ea4eb8951c9ac9032c98` |
| shared/ma-core.js | tau2DL (34), pool (404) | Independent pinned JavaScript ordinary-deletion mu/SE/tau2 capture is available. Explicit DL/no-HK settings; normal endpoints use the contract's exact z constant. | `fef6ab267ec7fd5582e3431381f090daee11267010effc0858834d9e5fc44bc8` |
| hub/shared/results-export.js | _csvEscape (20), _flatKVs (26), _toCSV (41), init (107) | Numeric String and JSON.stringify preserve numeric precision; arrays serialize as JSON, CSV nulls are empty. Actual download fidelity is untested. | `16ffa76bc74275565214c2e142d7f0d0847a5a8eded2614efb04aa172acd71f4` |
| hub/shared/plot-export.js | loadPdf (10), _prepareSvg (57), _serialize (65), _download (69) | SVG/plot export exists. PDF lazily loads script-relative vendor/jspdf.min.js; publication inset/composition is R-only. | `7533db659c89b328f20252fc2deaa1272d8473d00052d7b91a9732c24ee382cc` |
| limit-ma/validate/generate-plus.R | metagen/limitmeta (22–24), Q tests (29–30), metabias (42) | Read-only R reference for field mapping and original oracle settings; not run and not the complete v4 capture contract. | `07f9174d428ba0b8d7af3f95997e5283b0ead8044ecdfd29606e8688d2bc680d` |
| limit-ma/validate/loo/generate.R | deletion metagen/limitmeta (24–27) | Read-only reference confirms independent refitting; older manifest lacks required ordinary-deletion uncertainty. Not executed. | `5597fd7d2a6837f553622d8be833613a0c50b1e82762c031449f5fcd895ea2ac` |

The page's main closed-form fit does not run the internal REML convergence check performed by the comparison and deletion paths. This difference remains explicit: main finite output never overrides comparison/R refusal. Matching refusals are agreement on failure, not a finite sensitivity estimate. Preserve main, comparison, deletion and R statuses independently.

The app does not implement source extraction, CI-to-SE/log transformations, design/contrast verification, release receipts, numeric new/robust classification, verification sampling/history/packets, or the requested publication inset/composition. Computational preparation, classification/weights and verification orchestration are **R-only** under CONTRACT section 8; human/model source review is not a browser capability. Apply derived comparisons separately to captured app and R values. Ordinary deletion SE capture uses an existing pinned JavaScript function; the missing capture plumbing remains mandatory implementation work.

The complete F4 manifest and normalized 1e-9 tolerance supersede smaller historical oracle manifests, not the numerical app implementation. R reference scripts were read only; corpus inputs/outputs were hashed as opaque bytes and never replayed. No historical check count is presented as current runtime proof.

## 5. Browser dependencies rechecked, including hub/

Python's HTML parser found **32 direct resources: 30 scripts and two stylesheets**. All exist; all applicable PIN.txt comparisons match. The entry page plus every direct resource has a SHA-256 and byte count in DEPENDENCIES_P12.json. This includes `hub/app-style.css` and all nine directly linked `hub/shared/` scripts previously missing in earlier work.

Named dynamic targets were read from the loader code rather than assuming one relative-path base:

| Loader and path | Current finding | Role |
|---|---|---|
| index.html:782 / tooltips.js:_loadAndRefresh -> hub/shared/glossary.json | Present and hashed | Default English tooltips; translation variants/runtime requests are not certified |
| plot-export.js:loadPdf -> hub/shared/vendor/jspdf.min.js | Present and hashed | Lazy PDF export, script-relative; chosen figure route uses SVG |
| alm-validate.js:runner -> shared/webr-runner.js | Present and hashed | Optional browser-R loader |
| webr-runner.js -> r-shiny/shinylive/webr/webr.mjs | Missing | Optional WebR runtime, outside required desktop-R route |
| webr-runner.js -> r-shiny/shinylive/webr/repo/manifest.json | Missing | Optional WebR package manifest, outside required route |
| adapter.js / plus-pins.js -> four archived corpus/reference JSON files | Present, hashes checked as bytes only | Excluded archived replay; do not execute |

Both linked stylesheets contain no active external imports/URL dependencies in the inspected source. The comparison validation code also clones linked stylesheets. These observations establish static availability only; they do not certify dynamic request completion, optional language variants, browser execution, export round trips or app/R parity.

The embedded build-info commit is `42a94da2110a02200d0b5bff4c56f636b9cbffa9`, different from the job pin; no .git ancestry is present. Preserve this discrepancy beside the job-supplied identity and measured file hashes. The missing optional WebR files must not be represented as a working browser-R route or replaced with another runtime.

A fresh controlled browser context must prevent restored/default examples from executing: index.html runs on load and hero loading can click Run. Use only marked synthetic fixtures for validation; no archived corpus or real-data example runs. Confirm actual closure for the chosen route after release and before real analysis. `audit_P12.py` is the historical static-inventory generator for the original V4 job directory. It requires that directory's B_P12_V3 inputs, PIN.txt and novelty logs, together with the configured app/source roots; these dependencies are not all included in this package. It also rewrites DEPENDENCIES_P12.json. It is not a standalone verifier of a frozen release. Preserve the released inventory unchanged, record any regenerated inventory separately, and compare actual file hashes with the frozen inventory before relying on the result. Runtime validation remains a separate mandatory condition. *(Text replaced pre-freeze per REDTEAM2 P2-01, 2026-10-28.)*
