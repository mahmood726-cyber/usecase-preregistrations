# JOB F_P15_V5
Paper: P15
Type: V5
Node: baseimage
ALLMETA: allmeta@14dc545/

Job-type file: V5.md. Paper: P15. SOURCES: sources/P15_primary and sources/P15_fallback. COORDINATOR DECISION (pc2, Claude, before any data extraction): RT2-P15-01 (the S2 `se` column scale). Proposed resolution, which you must verify against the sources:
- The S2 Table column is headed `se`. Eq. (3), fulltext.xml sec006, pone.0166941.e005, defines `se` with a square root, i.e. as a STANDARD ERROR of d. The S2 Fig caption also describes a standard-error axis. The S2 Table caption's word "variance" is the single conflicting statement.
- Prespecify, now and before extraction: the S2 `se` column is the standard error defined by Eq. (3); import vi = se^2. Record the caption conflict verbatim as a disclosed source inconsistency.
- NO alternative mapping is ever tried. If the reproduction gate fails under this mapping, follow the stop rule: primary failure, then the fallback only if independently cleared, otherwise stop. Never switch to the variance mapping.
- If the sources contradict this reading (for example, if Eq. (3) does not define the same `se` that the S2 column reports, or the column values are described elsewhere as variances), do NOT apply it and keep the blocker.
RT2-P15-02: put the paged OpenAlex JSON and the coordinator novelty note into supporting/evidence/ as byte copies with sha256, and cite them relatively. The coordinator's novelty note text: "OpenAlex 343/343 citing works retrieved via page-based paging (cursor paging returned HTTP 401 after 200). pc2 reviewed the 7 flagged titles: none applies RVE or dependence modelling to the Rytwinski 2016 dataset."
RT2-P15-03: apply the replacement text exactly.
