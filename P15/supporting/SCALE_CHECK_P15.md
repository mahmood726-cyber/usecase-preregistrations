# P15 v6 deterministic S2 scale-check specification

Date: 2026-10-28. Prospective specification only; NOT EXECUTED on source rows. This is R-only preprocessing for pc2's future operational scripts, not a browser feature.

Authority: [MAHMOOD_DECISIONS item 9](evidence/MAHMOOD_DECISIONS.md), expanded by the binding [v6 job](evidence/V6_JOB_P15.md). It supersedes RT2-P15-01's requirement for a documentary scale resolution before freeze and the rejected v5 proposal to assume SE. It does not change any original number, reproduction tolerance, model, verification rule or outcome definition.

## Header-only prerequisite and source interpretation

Python inspected only the first structural table row in word/document.xml of [S2 Table](evidence/primary/pone.0166941.s003.docx). It prints `NT`, `NC`, `d`, `se` and `Study*`. No observation cell, row count, row precision or row completeness was examined.

The caption identifies NT as impact sites/after monitoring and NC as control sites/before monitoring. [Methods sec006](evidence/primary/fulltext.xml) defines G1 as control/before and G2 as impact/after. Fix n1=NC and n2=NT. Equation (3) is symmetric in these two sizes. Both required group-size columns therefore exist; this is not a claim that every later extracted row has complete valid sizes.

Supporting source wording and mathematics:

> Relationship between effect sizes (d) and standard error to assess publication bias.

This is the S2 Fig caption. Equation (3), XML disp-formula pone.0166941.e005, contains MathML msqrt; its unchanged [image](evidence/primary/pone.0166941.e005.jpg) confirms the radical:

`se = sqrt[(n_G1+n_G2)/(n_G1*n_G2) + d^2/(2*(n_G1+n_G2))]`

Conflicting source wording, retained exactly:

> effect sizes (d), and variances for d (se).

This is the S2 Table caption ending. The sentence immediately introducing Eq. (3) says:

> The sampling variance of is given by:

The absent object after "of" is left unchanged. Neither statement is silently reconciled by assuming a scale. The binding decision registers a deterministic comparison against both interpretations and a stop rule. The source supports availability of the needed headers and the specified radical; no source establishes in advance which classification the rows will receive.

## Execution order and complete inputs

No scale computation is authorized before release. After P15 release/archive prerequisites, independent extraction, adjudication/fourth pass and required verification, run this rule on every S2 observation in physical-source order, excluding only structural headers. Preserve all physical row keys under prereg section 5. Complete code and synthetic validation before this real-data check and before any reproduction gate. Later diagnostic-driven verification remains mandatory before reporting.

Retain the exact printed strings for NC, NT, d and se, including trailing zeros and any exponent, alongside independently verified numeric interpretations. These are now required extraction/verification fields. Never derive missing n from other columns, sources, totals or pooled fits. Do not replace the printed d with a reconstructed effect. Do not replace printed se with computed A or B.

Missing n stops the primary. Missing/unreadable/nonfinite d or se, nonfinite/nonpositive n, or nonpositive se also stop under the existing complete-valid-input requirement. Record the reason; do not silently discard, impute, floor or repair values to achieve a class. An empty observation set cannot pass. Source-grounded extraction corrections retain their audit trail and repeat verification and this same rule before downstream work; results cannot motivate alternative assumptions.

## Exact tolerance and row classes

For each valid row let s be its printed se, n1 its printed NC, n2 its printed NT, and d its printed effect. Compute:

`A = sqrt[(n1+n2)/(n1*n2) + d^2/(2*(n1+n2))]`

`B = A^2`

If the printed se has p digits after its decimal point, its last-place unit is 10^(-p) and the tolerance is exactly:

`t = (1/2)*10^(-p)`

Thus a three-decimal display has unit 0.001 and half-unit tolerance 0.5*0.001 = 0.0005. This is arithmetic on a display convention, not a study value. Keep trailing zeros when determining p. For scientific notation with exponent e, use the mantissa's p and t=(1/2)*10^(e-p); a plain integer has p=0, e=0, hence t=0.5. Use actual printed precision separately for each row. Indeterminate numeric formatting stops eligibility rather than inviting a guessed precision.

Define two independent booleans with inclusive endpoints:

- SE match: abs(s-A) <= t.
- VAR match: abs(s-B) <= t.

| SE match | VAR match | Row class |
|---|---|---|
| true | false | SE |
| false | true | VAR |
| true | true | AMBIGUOUS |
| false | false | NONE |

Never round A or B to displayed precision before comparing. Do not add floating-point slack, widen t, propagate uncertainty from rounding n/d, use a relative tolerance or choose the nearer form.

For exact boundary decisions, parse finite printed decimals as rational numbers. Let C=(n1+n2)/(n1*n2)+d^2/(2*(n1+n2)), so A=sqrt(C) and B=C exactly. With valid s>0 and C>0, the SE inequality is exactly equivalent to max(0,s-t)^2 <= C <= (s+t)^2; VAR is abs(s-C)<=t. These rational comparisons avoid numerical square-root boundary error without changing the rule. Approximate A may be displayed in the audit log; rounded display values must never determine classification. This arithmetic is an implementation requirement for the future R-only checker, not an assertion that such code already exists.

## One dataset mapping, or stop

All observations must have one unambiguous common class:

- If all are SE, set every vi=s^2 from printed se.
- If all are VAR, set every vi=s from printed se.
- Any AMBIGUOUS, NONE, missing n, invalid required input, empty set or mixture of SE and VAR: STOP the primary before any pooled calculation.

No row-specific mixture, subset or majority decision is allowed. Keep the primary yi equal to printed d. Write the uniform decision and computed vi to a separate derived record; leave source fields unchanged. The app receives only cluster,yi,vi, with `vi` as the header. Never pass a raw se header to allow the parser to determine the scientific mapping.

The checker has no pooled estimate, CI, reproduction target or fit result among its inputs. Freeze the decision log before the original DL/z reproduction. Neither a scale-check stop nor a reproduction failure permits testing the other mapping. The only continuation is the independently cleared fallback under its unchanged feasibility, novelty and reproduction requirements; it is currently unavailable, so otherwise stop and report the disposition.

## Required audit and future validation

Record source/evidence hash, code hash/version, physical row key, unchanged input strings, p/e/unit/t, A and B with their exact C representation, both match booleans, row class or invalid-input reason, and the dataset decision. Record the check time before the gate and retain the complete row inventory. No log or real extraction table has been generated now.

The future scripts must be hashed and tested by pc2 on generated `synthetic_*` fixtures marked "SYNTHETIC - not data" in their first line or column. Cover SE-only, VAR-only, both, neither, mixed datasets, missing n, invalid fields, empty input, trailing zeros/exponents, inclusive exact boundaries and immediately outside them. Confirm stops prevent pooled fitting and no alternate mapping follows gate failure. These are mandatory operational conditions, not completed tests or new freeze criteria.
