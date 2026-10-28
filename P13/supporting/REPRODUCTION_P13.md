# P13 v5 normative reproduction contract

Fixed on 2026-10-28, before extraction or any real-data calculation. Authority: [JOB.md](evidence/instructions/JOB.md) and [Mahmood decision 7](evidence/instructions/MAHMOOD_DECISIONS.md). This contract and [original_gate_P13.R](original_gate_P13.R) fix exactly one configuration for each candidate. They do not identify the authors' historical implementation. The REML reproduction gate is R-only and precedes the unchanged DL/PFT GOSH analysis.

## Documentary decision and contrary evidence

Primary, [final article XML](evidence/primary/fulltext.xml), Methods sec13, “Data synthesis and prevalence estimation”:

> Quantitative data on the prevalence of autonomic dysfunction were pooled using random effects meta-analysis using the Freeman–Tukey transformed proportion to restrict estimates and confidence limits to a range of 0–100% [21].

This supports random effects and Freeman–Tukey. It does not specify the normalization, inverse sample-size convention, tau² estimator, test or package. The final PDF, accepted supplementary PDF and both DOCX members of the final supplementary ZIP were also screened for method/package language; none states a statistical package. The PRISMA checklist's generic software-reporting instruction does not identify one used.

**Conflicting primary source text: none found.** In particular, the quoted range restriction is respected by the named inverse; the source does not prescribe a different inverse. There is no exact contrary passage to quote. The half-angle normalization and harmonic-mean inverse are prospective assumptions fixed by the job, not quoted author choices.

Tang, [final article XML](evidence/fallback/fulltext.xml), Methods, “Statistical analysis”, first three sentences:

> All analyses were performed by H.T. using RStudio statistical software, v.2022.12.0.

> We calculated the prevalence and 95% CI to estimate the prevalence of fatigue in patients with axSpA.

> A random-effects model was used for the pooled estimate of fatigue because significant between-study heterogeneity was expected.

The first sentence would contradict a claim that Tang names no software. The coordinator's actual premise is **no statistical package**, which this sentence does not contradict: RStudio does not identify a pooling package or function. No source states metafor, REML, or z intervals as Tang's historical implementation.

**Conflicting Tang transformation/package text: none found.** The complete article XML and supplied supplementary DOCX contain no Freeman, Tukey, transform, arcsin, logit, logarithm, metafor or metaprop match. Methods, captions, supplementary headings and figure/table scope were checked; the supplementary DOCX consists of contextual tables and contains no embedded drawing. The available source screen gives raw “Proportion” forest headers, not a transformation declaration. Thus **transformation NOT STATED** is the documentary finding; **measure="PR"** is the single prospective choice required by JOB.md. Do not equate silence with proof of the authors' raw-proportion implementation.

No conflicting passage has been suppressed or invented. If a later source supplies a conflicting method, stop eligibility for that candidate and record a prospective amendment before any extraction; do not use numerical gate results to choose a mapping.

## Fixed numerical choices

| Choice | Primary | Tang fallback |
|---|---|---|
| Input inventory | All 17 final overall-forest contributions | All 30 final overall-forest contributions |
| Counts | Direct printed integer events x and matched n; no imputation/reconstruction | Same |
| R/package/function | R 4.6.0; metafor 5.2.1; escalc then rma | Same |
| Measure | PFT; half-Freeman–Tukey double arcsine, radians | PR; p=x/n |
| Sampling variance | 1/(4n+2) | vtype="LS", p(1−p)/n |
| Correction | add=0, to="none", drop00=FALSE; no added counts | Same |
| Boundary rows | Retain x=0 and x=n with finite positive PFT variance | No correction; v=0 fails the candidate before fitting |
| Model | Intercept only, independent contributions, weighted=TRUE, inverse-variance weights 1/(v+tau²) | Same |
| Heterogeneity | method="REML"; nonnegative tau², estimated once; no supplied fixed tau² | Same |
| Pooled uncertainty | test="z", level=95; unrounded coefficient and Wald CI endpoints; no HK, t, bootstrap or prediction interval | Same |
| Inverse | **transf.ipft.hm using the harmonic mean of n**, targs=list(ni=n) | Identity |
| Harmonic mean | h=k/sum(1/n), over all included forest denominators; same h for point, lower and upper limits | Not applicable |
| Final scale | Apply the inverse separately to estimate/CI limits, then multiply by 100 | Proportion; no ×100 |
| Boundary output | Keep pinned transf.ipft.hm behavior, including its own boundary handling; no external clipping/reordering | Do not clip the raw Wald interval to [0,1] |
| Omission/dependence | Missing/nonfinite values, noninteger counts, invalid n/x, wrong k, unresolved identity/overlap fail; na.action="na.fail" | Same |
| Optimization | Package HE initialization (tau2.init=NULL), tau2.min=0, threshold=1e−5, maxiter=100, stepadj=1 | Same |
| Extra settings | No moderators, custom weights, subset selection, scaling covariates, robust variance, alternate optimizer, parallel fitting, seed or retry; all other internal numerical controls pinned to metafor 5.2.1 defaults | Same |

PFT definition: y=0.5×{asin(sqrt(x/(n+1)))+asin(sqrt((x+1)/(n+1)))}. The half-angle and 1/(4n+2) convention must remain paired. Passing the full n vector to transf.ipft.hm makes it compute the harmonic mean; do not substitute arithmetic mean n, pooled n, effective n, asin inverse, or a different normalization.

The executable module validates formulas against escalc on synthetic fixtures. Warnings, errors, nonconvergence, wrong versions, nonfinite outputs, reversed CI ordering, or silently changed inventory stop execution without rerunning a different setting. Built-in numerical steps within the pinned fit are not a model search. R/sessionInfo, platform and package versions must be archived by pc2. API documentation was consulted to check function signatures; no local R execution or installed-package verification is claimed.

## Gate and stop rule

The published targets remain **64% (95% CI 51, 76; I² = 93%)** and **0.56 (95% CI: 0.49, 0.63; I² = 94.6%)**. Compare the unrounded point estimate and both endpoints separately with inclusive tolerances **0.5 percentage points** and **0.005 proportion units**, respectively. All three must pass; no rounding, epsilon widening, endpoint omission, I² gate or target editing. The executable interval check target−tolerance ≤ observed ≤ target+tolerance implements the inclusive bound.

**NO switching within a candidate on gate failure. No model search.** Stop the primary; activate Tang only if its own feasibility, novelty, inventory/mapping and fixed-model eligibility independently clear. Run Tang's one fixed gate; if it fails or cannot clear, stop. Report failures and conduct no new analysis for failed candidates. A successful reproduction is required before GOSH; a completed valid sensitivity/robustness result never licenses switching candidates.

No real-data invocation is permitted before GitHub release, Zenodo DOI, synchronized extraction/verification kit, and the mandatory synthetic/browser validation conditions. The supplied R module and synthetic test script are unexecuted handoff files, not a claim that those conditions passed.
