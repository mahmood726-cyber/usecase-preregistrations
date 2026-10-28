# P15 v6 app capability and browser dependencies

Date: 2026-10-28. V6 reverified all 12 archived file hashes against the supplied v5 audit and original pinned snapshot. Python-only static inspection; no JavaScript, browser, R or statistical model was run. Unchanged snapshot files are under [evidence/app](evidence/app/rve-meta/index.html); the [byte-copy manifest](EVIDENCE_SHA256.md) records every hash. Supplied commit: `14dc545bcba87a02158b2f445c28450e7eaf6b89`. File hashes below identify the inspected bytes; no live deployment is substituted.

## Registered capability (F6)

| File | Function / line | Evidence and registered use |
|---|---|---|
| `rve-meta/index.html` | `run()`, 386; `runSensitivity()`, 465 | Parses input, honours rho and centring controls, calls CORR fit/summary; sensitivity calls the fixed grid. Centring remains off. |
| `rve-meta/index.html` | `whenEigenReady()`, 379; `exportAction()`, 501 | Waits for the eigen backend; JSON and coefficient/rho CSV export paths retain numerical values. |
| `shared/rve-extras.js` | `parseStudies()`, 120; `typeClusters()`, 100 | Recognises cluster/yi/vi; all extra columns become predictors. A header `se` squares the number (lines 177-180), whereas `vi` retains variance. Numeric/logical-only cluster labels can be coerced, hence the fixed `P15|` prefix and separate identity map. |
| `shared/rve.js` | `fitCORR()`, 369; nested `clusterWeights()`, 433 | CORR per-effect weight 1/[cluster size * (cluster mean variance + tau-squared)]. HTJ moment tau-squared at lines 443-480, truncated at zero by the estimator; no override registered. |
| `shared/rve.js` | `fitCORR()`, 507-569 | CR2 adjustment/sandwich and coefficient-specific Satterthwaite df. Default method is CR2 (373); CR1 is available but not registered. |
| `shared/rve.js` | `summary()`, 602 | Two-sided t p-values and estimate +/- qt(.975, df)*SE; requires the Student-t dependency. |
| `shared/rve-extras.js` | `rhoSensitivity()`, 253 | Refits grid [0, 0.2, 0.4, 0.6, 0.8, 1]; captures refused fits. Its display flags do not implement the prereg's full new/robust/indeterminate definition. |
| `shared/rve-extras.js` | `buildResult()`, 407; `toRhoSensitivityCSV()`, 275 | Explicit effect/cluster counts, settings, coefficients and model metadata; compare full-precision exports, never rounded display text. |
| `shared/rve-extras.js` | `toRScript()`, 335 | Exports robu(CORR, small=TRUE) and coef_test(CR2, Satterthwaite); does not implement the complete P15 workflow. |
| `shared/rve-eigen.js` | `loadSync()`, 298; `loadAsync()`, 314; `eigen()`, 394 | Embedded base64 WebAssembly payloads compiled/instantiated locally. No external .wasm download is required by this file. |
| `shared/stats-qt.js` | `pt()`, 87; `qt()`, 97 | Student-t probabilities/quantiles for engine inference. |

R-only: the [deterministic S2 scale check](SCALE_CHECK_P15.md), original-model reproduction, fallback joint HTZ test, cluster-deletion diagnostics, full classification, verification sampling/logging and comparison figure. The browser sensitivity banner is not an inferential gate.

## Browser dependency recheck

The entry page has **eight script imports and two stylesheets**. All ten resolve to existing files in this snapshot, including both hub imports. Python parsed the HTML tags, resolved their relative paths and hashed their bytes. Loaded JavaScript and CSS were inspected for further imports, fetches, script injection and CSS URLs. No additional mandatory external runtime asset was identified on the registered fitting/export path. The CommonJS require of rve-eigen.js is the nonbrowser path, not another browser resource.

The continuation links open other apps only on user action and are outside this registered analysis. Navigation anchors do not constitute fitting dependencies. The optional bus/toast globals are guarded. Browser APIs, WebAssembly support, local storage behaviour and export operation still need runtime checks; static availability is not a claim of operational dependency closure.

The page calls `whenEigenReady(run)` at line 531 and can restore an autosaved draft at line 563. Before any synthetic browser validation, arrange for a generated marked synthetic fixture to replace the bundled textarea before the automatic initial fit, and use a clean storage context. Do not run bundled examples as synthetic evidence or let a restored dataset change the inputs.

`shared/build-info.js` contains embedded sha `42a94da2110a02200d0b5bff4c56f636b9cbffa9`, version `v1.8.0`, timestamp `2026-10-20T20:32:27Z`. This older build stamp must not be represented as the supplied snapshot commit. Preserve raw exports and accompany them with the pin and file hashes below. No source edit is needed for the registered analysis.

## Mandatory post-release, pre-analysis conditions

pc2 must demonstrate dependency loading/WebAssembly readiness, fit/export operation and app/R agreement using only generated `synthetic_*` fixtures marked "SYNTHETIC - not data" in their first line or column. Include both model formulas, every rho, parser variance mapping, refusal/invalid-input handling and indeterminate cases. Use Windows R 4.6.0, metafor 5.2.1, robumeta 2.1, clubSandwich 0.7.0 and LC_COLLATE=C. Apply the unchanged 1e-9 comparison rules. No passing result is claimed here. Primary F1 is cleared under the binding v6 rule, whose real-data execution remains strictly after release, extraction and verification, before reproduction. The scale checker is not implemented by this app: its parser squares a column named se but cannot choose the scientifically registered mapping. Only the single uniform vi vector approved by the R-only scale check may enter the browser. Synthetic parser checks do not resolve source meaning.

The full P15 operational code and first-round REDTEAM/APP_CHECK reports were not supplied. The [second-round review](evidence/REDTEAM2_P15.md) is included. Review first-round reports if delivered; code delivery, version hashes and synthetic validation precede any real-data reproduction gate. Every post-release code change requires a dated deviation independent of real-data results.

## File hashes

SHA-256 values computed from local bytes. Rows tagged direct dependency are the complete import list for this page; README is contextual, not loaded by the browser.

| Snapshot-relative file | Role | SHA-256 |
|---|---|---|
| [rve-meta/index.html](evidence/app/rve-meta/index.html) | entry page | `88d1494a0128ef5bd18e33e6b35ac0d13ae516044efd99354034ec1e953632eb` |
| [rve-meta/README.md](evidence/app/rve-meta/README.md) | context | `6e8b4f38994b8a061206661481adb44ded93179c18f907085a3331af0bf95fd7` |
| [shared/forced-colors.css](evidence/app/shared/forced-colors.css) | direct dependency | `a967581cb9dfe03bcd6158264353dd8c3fff386d2919143587aa507a24e0c39c` |
| [hub/app-style.css](evidence/app/hub/app-style.css) | direct dependency | `475254903d40eebe241574975f1ddff13808c8ad478c17137fda449a3952361f` |
| [shared/stats-qt.js](evidence/app/shared/stats-qt.js) | direct dependency | `fb4110ba8e4b2e784193fde258ac37086713dc8d75a3295f84272d6fbdba8efb` |
| [shared/rve-eigen.js](evidence/app/shared/rve-eigen.js) | direct dependency | `a2a687c5127f6b5989d3b37e39fe4ae92849195dc6e1cbfe7befdd17352e239a` |
| [shared/rve.js](evidence/app/shared/rve.js) | direct dependency | `75f9b201c6fd7f245a91e1712499044d519ab3dcb49bb7d49cef311d1ea6af0e` |
| [shared/rve-extras.js](evidence/app/shared/rve-extras.js) | direct dependency | `a66b55741c7c538aa69d45ef003ee452f52835db7d8d7ef7f1f639169f06041b` |
| [shared/build-info.js](evidence/app/shared/build-info.js) | direct dependency | `44c8a7d1e2cdad4d4b1c4806cffdd4f9817dc39161cd0de5374761a71bd19177` |
| [shared/app-flow.js](evidence/app/shared/app-flow.js) | direct dependency | `2b8e366dbdbf5aebffc70f0b25b1ac7a49d65cc4ecfd7c0807113b3b5556162e` |
| [shared/autosave.js](evidence/app/shared/autosave.js) | direct dependency | `18bcc6c10f6177482b2f8453bede3f92887d7e6729413862cc903891405d23e8` |
| [hub/shared/a11y-landmarks.js](evidence/app/hub/shared/a11y-landmarks.js) | direct dependency | `a9b35c71c500b0fe4e5a080f23c9dbb11c5462663a0d44e4557f782149e5f8ea` |
