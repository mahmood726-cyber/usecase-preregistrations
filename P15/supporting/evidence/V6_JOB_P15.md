# JOB F_P15_V6
Paper: P15
Type: V5
Node: baseimage
ALLMETA: allmeta@14dc545/

Job-type file: V5.md. Paper: P15. Previous packages here: F_P15_V5, D_P15_REDTEAM2. SOURCES: sources/P15_primary and sources/P15_fallback. DECISION (binding, before any data extraction): MAHMOOD_DECISIONS.md item 9 applies. Replace the unresolved-scale blocker (RT2-P15-01) with a pre-registered deterministic scale-check rule, executed after release, after extraction and verification, and BEFORE the reproduction gate. For every S2 row:
1. Compute A = sqrt[(n1+n2)/(n1*n2) + d^2/(2*(n1+n2))] from that row's printed n1, n2 and d (Eq. 3 with its radical).
2. Compute B = A^2.
3. Classify the row as SE if |printed se - A| <= half a unit in the last printed decimal of se, or VAR if |printed se - B| <= the same tolerance. State the tolerance arithmetic exactly. A row that matches both is AMBIGUOUS; a row that matches neither is NONE.
4. If all rows are SE: vi = se^2. If all rows are VAR: vi = se. Otherwise (any AMBIGUOUS, NONE, missing n, or mixed classes) STOP the primary under the stop rule.
The rule never looks at pooled results and never tries both mappings on the gate.

First check, from the S2 Table headers only (no row values), whether n1 and n2 are printed. If they are not, the rule cannot run, so keep the blocker and say so.

Apply this to the v5 package F_P15_V5: write v6 with BLOCKERS = NONE only if F1-F6 all hold. Fallback status is unchanged. The REDTEAM2 round follows this job.
