# P11 v4 static app and browser dependency evidence

2026-10-28. Supplied pin: **14dc545bcba87a02158b2f445c28450e7eaf6b89**. Root: C:/Users/User/ucjobs/allmeta_14dc545. Commit attribution comes from JOB_RULES/PIN; no Git provenance check was run. Python read and hashed files; no browser JavaScript, R, supplied corpus or real-data calculation was executed.

## Capability evidence (F6)

| File | Functions / locations | Registered capability | SHA-256 |
|---|---|---|---|
| influence/index.html | parse 216; tau2_REML 249; pool 253; run 336; repool 441; drawLOO 566 | Strict effect/SE input; inverse-variance REML full fit and all single deletions; residuals, DFFITS, Cook distance, covariance ratio, hat, weights, DFBETAS and flags; leave-one-out figure. | 48c65317a4090a7e72ea3b70cf177a1e77dbf2620a2eed1d1c5e9805c0773d25 |
| shared/ma-core.js | tau2REML 137–362; _tau2Guarded 121 | Fixed global restricted-likelihood search with boundary/interior comparison; invalid inputs/unresolved search throw. No exposed estimator tuning is registered. | fef6ab267ec7fd5582e3431381f090daee11267010effc0858834d9e5fc44bc8 |
| influence/influence-extra.js | summarize 53; pnormUpper 45; pchisqUpper 50 | Full/deletion normal 95% CIs, z/p, I²/H² and Q p-value. Z975=1.959963984540054. | 54a7c60ff2919a8a2a3b7e00738e3ada8c4fbabf84100210c925902aaddfa67c |
| influence/r-script.js | AlmInfluenceR.build 21–125 | R exporter; scalar-score initialization, per-deletion restart, numerical field/flag comparisons. Independent P11 implementation must precede exporter comparison. | f1b6a5cbeb7e490925696496e0ac3be2a083b563ca55422f7bc63197fae0e677 |
| hub/shared/results-export.js | resultsExport | Unrounded structured results export wired to index.html __almResults 762; __almInfluenceStudyRows 693 and __almInfluenceStudyCsv 702 expose full per-deletion quantities. | 16ffa76bc74275565214c2e142d7f0d0847a5a8eded2614efb04aa172acd71f4 |

The page's registered fit is intercept-only REML with normal inference. The core also contains other estimators, but the page does not expose the registered original ML/MH reproduction gates. Those gates, count-to-effect transformations, S_i/CI-category classification, headline selection and seeded verification sampling are **R-only/procedural**, not claimed complete app features. Collective exclusions, moderators, HK inference, alternative estimators and built-in example data are outside the registered analysis.

The flag rule in index.html:377–378 is the OR of abs(DFFITS)>3/sqrt(k−1), Cook's D>0.4549364231195727, hat>3/k, abs(DFBETAS)>1. Flag thresholds and the main preregistration's sensitivity thresholds remain unchanged. Additional columns change display only.

Global app REML and the fixed R scalar-score start can choose differently; static implementation is not parity evidence. The exported generic checker at r-script.js:109–115 allows paired NA. The P11 contract rejects nonfinite required values even if both are missing and requires exact row maps, exclusions and CI/S classifications in addition to every numerical/flag check.

## Direct and lazy dependencies

[APP_DEPENDENCIES_P11.json](APP_DEPENDENCIES_P11.json) records each dependency's path, parent/reference, existence, byte size and SHA-256, all 16 supplied PIN hash comparisons, seven unchanged source hashes and governing-input hashes. All **26 direct references** (24 scripts, two stylesheets) exist. All 16 PIN entries match. No files were patched or repinned.

All nine scripts absent in v3 are present:
- hub/shared/csv-upload.js: 6ce4702db911d2c193da4b775a10f8b748d4901ddcc98f0830bab7bd48db5384
- hub/shared/axis-controls.js: 1620bdc94620df10a41abe91c388de6a91f03367dd3719cb77ce2776ab553806
- hub/shared/results-export.js: 16ffa76bc74275565214c2e142d7f0d0847a5a8eded2614efb04aa172acd71f4
- hub/shared/url-state.js: a704241f6c1faffaf33544d3c2059cc3d7d196c0dab39d91a3e006e315de1aa1
- hub/shared/reset-undo.js: 0ef224c3e8a53dca6364cdbdfa8a0f24dc5e0e8805180651781106e0a2af1ee8
- hub/shared/tooltips.js: cd9fd2d82a5d5402915737de9aaef7caa0f506ca0550e0f18f078c67b3078393
- hub/shared/plot-export.js: 7533db659c89b328f20252fc2deaa1272d8473d00052d7b91a9732c24ee382cc
- hub/shared/analysis-lifecycle.js: bdae7a0d966e9093b4234e697a8474e3e1757cde804f5893a880a0f9b2b4d9f7
- hub/shared/a11y-landmarks.js: a9b35c71c500b0fe4e5a080f23c9dbb11c5462663a0d44e4557f782149e5f8ea

Identified lazy resources also present: four glossary JSONs, vendored hub/shared/vendor/jspdf.min.js, shared/webr-runner.js, and the two manifest-listed influence validation JSONs. The supplied corpus/reference were hashed only; no contents were treated as this task's synthetic fixtures or run.

**Browser dependency closure remains unverified.** In the supplied snapshot, r-shiny/shinylive/webr/webr.mjs and r-shiny/shinylive/webr/repo/manifest.json are missing. shared/webr-runner.js resolves that same-origin bundle at lines 33–36, imports it at 49, and reads the package manifest at 61. Without the manifest its package/runtime dependency graph cannot be fully enumerated or hashed. Do not label the built-in live-R route operational or substitute it for the registered independent pc2 run.

Required workflow: fresh isolated browser state; no shared-bus/example/restore inputs; paste the fixed round-trip effect, SE and administrative label lines, run once with all studies, enable additional columns, keep the analysis scale and null at zero, use automatic plot limits, then export numerical JSON, per-study CSV, R script and the leave-one-out SVG. No exclusions or estimator choices. Verify CSV upload separately on synthetic inputs because __almLoad filters invalid entries; exact inventory checks must catch any silent loss.

Mandatory post-release, pre-analysis closure: serve the pinned snapshot locally, exercise the full required workflow and all identified lazy routes on newly generated marked synthetic fixtures; record loading/console failures, import/export precision and every full/deletion comparison against independent pc2 R. Supply/hash same-pin missing bundle resources for the full-page audit, or document that an optional route is unavailable while proving it is not entered by the required external-R workflow. An unresolved failure on the required workflow stops real-data analysis. No pass is inferred from source presence or historic check counts.

The absent optional bundle is an open dependency issue under the mandatory post-release condition, not an F6 failure: the registered numerical JavaScript implementation is present and statically evidenced. R execution remains external on pc2.
