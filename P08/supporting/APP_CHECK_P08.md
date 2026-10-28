# P08 v4 static app and code audit — 2026-10-28

This is V4's own replacement static review. Earlier REDTEAM/APP/CODE jobs did not complete; their absence is not represented as a pass. Source inspection, specification review and package checks here address those gaps. R and JavaScript were not executed.

## Pin and launch path

Snapshot: `C:/Users/User/ucjobs/allmeta_14dc545/`; supplied commit **14dc545bcba87a02158b2f445c28450e7eaf6b89**. Serve that root; entry path `meta-regression/index.html`. Old `app/meta-regression/` is an alias in prior prose, not a folder under this snapshot. Preserve sibling `shared/` and `hub/` paths.

| File | Function / lines | Static capability | SHA-256 |
|---|---|---|---|
| meta-regression/plus-engine.js | prepare 21; fit 44; compute 81 | ML inverse-variance mixed-effects fits, z inference, full/reduced LRT, held-moderator predictions | 9b002c0594ab787c403ebb606a83f6d58d1492d091b1a68c9d5b117e719723b3 |
| meta-regression/plus-ui.js | parse 9; run 66; exportPayload 70 | Strict numeric CSV, moderator order, interaction flag, full-precision JSON | d56667f6ba8f6ea0781f852cd9c0d9958b5ade8fb501c7da38a888d0ea35156f |
| meta-regression/index.html | parseStudies 189; fitPM 251; hksj 277; tTwoSidedP 355; render 489; __almResults 817 | Single-moderator PM, floored HK, t(k−2), browser fit/SE/CI cache | 263d040ca4bd53d7125181b00687c78be3630efb41ba4573da0d8b95c81ed067 |
| meta-regression/validate/reference.R | plus_reference 2; fit 14 | Independent metafor ML/z reference and same model comparison | 1db73c17a432c35d858f3d4bad971babd9f809f5799e1d0dda41a6e0404271b8 |

Python recomputes these hashes and checks PIN.txt. [FILE_HASHES_P08.json](FILE_HASHES_P08.json) records every inspected dependency separately; this report's function/line/hash combination supplies F6 evidence.

## Registered primary path

Enter `yi,vi,D,S` in the multiple-moderator panel, interaction unchecked. `compute` builds intercept,D,S; its reduced model is intercept,D, so input order is material. The UI does not automatically code factors: S must already be numeric 0/1, following source provenance. No PM/HK option exists in this panel.

`fit` profiles ML with starting tau² from the unweighted residual estimate, nonnegative tau², fixed scoring convergence controls, scaled design calculations and rank refusal. Coefficient CIs use 1.959963984540054 and normal tests. Model outputs include k, p, beta, SE, z/p, CI endpoints, tau², log likelihood, AIC/BIC. `compute` clamps LRT at zero, uses the coefficient-count difference and chi-square tail, and exports the plot at 41 points with S held at its arithmetic mean.

The desktop reference uses metafor's same pinned ML controls: threshold 1e-12*max(1,var(yi)), stepadj .5, maxiter 10000. This static correspondence does not assert numerical agreement at the stricter P08 tolerance. Existing bundled validation tolerances are not substituted for P08's 1e-8 scaled numeric / 1e-6 p tolerances.

## Registered fallback path

`fitPM` solves weighted RSS=k−2 with bisection, taking tau²=0 at the boundary. `hksj` fixes q=max(1,RSS/(k−2)); `tQuantile975` and `tTwoSidedP` supply the t inference. This corresponds to metafor PM/test="adhoc"; use tol=1e-12 in R. PM reproduction is not registered: Liu reproduction is R-only DL/z.

`parseStudies` uses parseFloat, may skip malformed rows, and tolerates a leading nonnumeric header. Validate all numeric tokens before loading; compare accepted labels, numeric values and order against all ten intended rows and reject unexplained warnings. An app row count alone cannot prove correct parsing.

`__almResults()` returns unrounded intercept/slope, SEs/CIs, tau², q/df and ancillary quantities, but no slope p-value. The included `capture_app_P08.js` reads the cached browser fit and computes the same unrounded t-tail using verbatim `lnGamma`, `betaCF`, `betaInc`, `tTwoSidedP` source from the pinned page. It neither refits in R nor reads rounded cards. Its provenance is testable by the static audit script; runtime validation remains pending.

The app automatically calculates a permutation p-value via `AlmPermTest`. It is outside registered inference/comparison/classification. Location-scale stays disabled. Additional automatic descriptive outputs do not choose models. Both registered coefficient vectors, their SEs/CIs, tau² and the specified tests are comparison targets; fallback comparisons additionally check q and df. Primary also compares log likelihood, AIC/BIC and LRT. Nonfinite outputs or term/count/row/classification mismatches fail.

## Browser dependencies, including hub/

Static audit parses every script src and stylesheet href from index.html and hashes the resolved local paths. All direct files are present, including:

- `../hub/app-style.css` and hub/shared CSV upload, axes, results export, URL state, undo, tooltips, plot export, lifecycle and accessibility scripts;
- shared numerical, metadata, dataset/example, citation, autosave, validation and flow scripts;
- plus.css, plus-engine.js, plus-ui.js, validation contract/pins/adapter.

Dynamic resources manually traced and hashed: hub/shared glossary.json and ar/es/zh variants; hub/shared/vendor/jspdf.min.js for optional PDF export; shared/webr-runner.js; the four JSON files named in plus-pins.js and desktop reference documentation.

**Limit:** shared/webr-runner.js requests `r-shiny/shinylive/webr/webr.mjs` and `r-shiny/shinylive/webr/repo/manifest.json`; both are absent. The optional live-R button therefore lacks its bundle. Do not describe the whole browser app as dependency-closed. The registered browser fit plus separate desktop R does not use live webR; do not enable it or claim it as the independent run.

The app's in-page validation corpus and built-in examples are not certified synthetic P08 fixtures. Do not execute them in this pre-release job or use them as the post-release synthetic validation. Opening an unchanged page can auto-fit its defaults: plus-ui.js line 78 invokes run(). Before executing scripts in the validation harness, replace both panels' default inputs with marked synthetic values, clear URL/autosave state and suppress automatic example restoration. Keep original numerical script bytes pinned; record/hash any fixture-loader instrumentation. Use no clinical demo button.

Static asset presence is established. Actual same-origin serving, request failures, dynamic-loading/CSP behavior, export behavior and numerical runtime parity remain mandatory post-release checks. Navigation/documentation URLs are not numerical engine dependencies.

## R-only work and release code

Original-summary reproduction, source/independence eligibility, HR-before-OR selection, complete-case selection, deletion diagnostics and headline membership are not implemented as P08 workflows in the app. They are **R-only or extraction/verification workflow**, not promised browser features.

[reference_P08.R](reference_P08.R) supplies fixed model/gate/classification functions; [VERIFICATION_P08.md](VERIFICATION_P08.md) fixes the kit and diagnostic contract. No earlier missing implementation is claimed to exist. The R file is a reference component, not a certified complete orchestration/verification harness. The pc2 release runner still must connect verified extraction, deletion diagnostics, the browser capture, classification/row comparison and verification logs, then pass synthetic validation before any real-data gate. This is explicitly a post-release condition under F4/FREEZE_CRITERIA, not an invitation to choose methods later.

Meaningful synthetic validation must exercise both reproduction paths; tau²=0 and nonzero; full/rank-deficient designs; exact k/category boundaries; missing/invalid inputs; primary bR threshold/sign/50%/20% classifications; fallback CI zero boundaries; parser skipping/permissiveness; rounding-gate failures; p capture; all headline/sample/escalation rules. Mark outputs “SYNTHETIC - not data”; they are never use-case results. Any post-release code change is a dated, result-independent deviation and requires synthetic revalidation.
