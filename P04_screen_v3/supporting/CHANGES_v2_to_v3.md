# P04 screening: v2 to v3 changes (approved for freeze and release; not yet released)

**Rule:** no gate is loosened relative to the released v2 text (sha256 414a84ef...c7c71a). Every change is classified as one of:
- **AUTH-1/2/3**: one of Mahmood's three authorized changes (larger pool; feasibility from headers, Methods and licence only; every gate's rules fixed in the text);
- **DISPATCH**: fixed by the dispatch decision of 2026-11-02 (under Mahmood's delegation; supporting/DECISION_v3_2026-11-02.md);
- **TIGHTER**: fewer records can pass;
- **NEUTRAL**: the same records pass; only the wording or procedure changes.

| # | Area | v2 | v3 | Class | Reason |
|---|---|---|---|---|---|
| 1 | Pool | v1 order from rank 22, minus 26 DOIs (540 rows); 5 dispositions | v2_screen_order 6-540 (535 rows) of the same archived order; 478 queued after the declared filter; 40 Stage F + at most 5 Stage S | AUTH-1 / DISPATCH | Larger pool without a new seed or re-retrieval |
| 2 | Seed and retrieval | seed 2026102804; no re-query (Option A) | same seed and order; no re-query; no new seed; no re-retrieval option | NEUTRAL / TIGHTER | Avoids seed-shopping and index drift |
| 3 | Prior-disposition exclusions | 26 DOIs | 31 DOIs (+ the 5 v2-visited) | TIGHTER | Every v1/v2 disposition is excluded |
| 4 | Derivative of an excluded DOI | not defined; the v2 #1 summary was visited and used a slot | Exact title-containment rule offline (2.3c) plus the visit-time rule F2(iii); same-title updates are also removed | TIGHTER | Closes v2 ambiguity 1 |
| 5 | Non-original items | failed at the visit and used a slot | Removed by a **declared filter stage** with counts per rule; not visits; no Stage F slot | DISPATCH (NEUTRAL in what can pass) | These items could never pass section 3 scope |
| 6 | Preprints | not addressed | Excluded by DOI prefix or Europe PMC `PPR:` source | TIGHTER | Only the peer-reviewed version of record is eligible |
| 7 | Exact-title duplicates | both visited | every member of a duplicate group is removed by the declared filter | TIGHTER | No keep-rule and no screener choice between an original and a same-title notice |
| 8 | Stage structure | one stage, 5 dispositions, 60 min each | Stage F (40 x 20 min, no early stop) then Stage S (<= 5 x 60 min); the F log is validated and hashed before S | AUTH-1/AUTH-2 / DISPATCH | N_S = 5 matches the field protocol's "Screen up to 5 candidates" |
| 9 | Sections read for feasibility | anything | Stage F: headers, Methods and licence statement only (abstract Results for counts/designs only; no data-availability statement); enforced by the extractor and the validator | AUTH-2 | As authorized |
| 10 | Stage F time cap | none (only the 60 min overall) | 20 min; an expired cap means F-UNRESOLVED | TIGHTER | Bounds screening effort |
| 11 | Check order | "proposed" sequence; the brief listed k first | Fixed F1-F10 and S1-S12; the first non-PASS is terminal | NEUTRAL / AUTH-3 | Closes v2 ambiguity 4 |
| 12 | Slot rule | every visited record uses a slot | same, in Stage F | NEUTRAL | - |
| 13 | Independent trials | design undefined | RCT only; the network must be RCT-only according to Methods (F7) and Results (S2); no switch to a sensitivity analysis | TIGHTER | Closes v2 ambiguity 2 |
| 14 | Outcome lock | designated primary, else hierarchy if "several or absent" | Rules C1-C5: a derived index alone fails; no component substitution; synonym table | NEUTRAL / AUTH-3 | Closes v2 ambiguity 3 with the strict reading |
| 15 | k counting | "published summary material" | Printed number only, for the locked outcome, population and time; non-trial units excluded; every printed value within 5-60; never by counting rows or edges | TIGHTER / AUTH-3 | Removes judgement |
| 16 | Population | diabetes or "explicitly separable diabetes subgroup" | Subgroup pre-specified in Methods; prediabetes excluded; multiple diabetes-type networks with none designated primary = FAIL | TIGHTER | Methods-only and no ordering choice |
| 17 | Licence | printed compatible licence, e.g. CC BY, CC BY-SA, CC0, CC BY-NC | **CC BY or CC0 only**; everything else FAILs; the URL governs | TIGHTER / DISPATCH | Consistency and reuse |
| 18 | Retraction | no check | New gate F3/S1, re-run before selection: Europe PMC + OpenAlex + Crossref update notices, all required | TIGHTER | - |
| 19 | Drug-node scope | "nonpharmacological-only networks" excluded | IN/CONTROL/OUT lists; INN or proposed INN required (sponsor-code-only nodes OUT); at least 2 IN nodes; both target nodes IN | TIGHTER | Matches the field protocol's "drugs never compared head-to-head" |
| 20 | Follow-up | designated primary time or longest reported time | same, plus "no printed time rule = FAIL" and a multi-time-point rule | NEUTRAL / AUTH-3 | - |
| 21 | Complete inputs (G1) | complete printed inputs, dependence, mapping | same, enumerated as input sets (a)-(d); numerals inside images only; digitising = FAIL | NEUTRAL / AUTH-3 | - |
| 22 | Target pair | motivated pair, else alphabetical; no direct edge | same, plus both nodes IN, same connected component, disconnected locked network = FAIL | TIGHTER / AUTH-3 | - |
| 23 | M | M=2/1/0 definitions | same; the M=1 limitation is a fixed statement type naming a target node | AUTH-3 | Removes judgement |
| 24 | P | routes 3/2/1 | same routes with fixed sources | NEUTRAL / AUTH-3 | - |
| 25 | L | 2/1/0 by published passage | fixed lexicon; the sentence must name a target node | AUTH-3 | Removes judgement |
| 26 | G3 novelty | v2 templates and coverage rules | unchanged | NEUTRAL | - |
| 27 | G5 effort | screener's component estimate, <= 4 h | deterministic formula, <= 4 h; calibration disclosed as resting on a single human estimate (4.0 h) | AUTH-3 / DISPATCH | Removes judgement |
| 28 | Selection | M, L, P, E, order, DOI | unchanged (order = v3 queue order) | NEUTRAL | - |
| 29 | Stop rule | stop on zero passers | same; no 41st F visit or 6th S screen | NEUTRAL | - |
| 30 | Field protocol | not cited directly | cited by sha256; a byte-identical copy is in supporting/ | NEUTRAL | - |
| 31 | Release checks | v2 `check_release` | same pattern; only the P04-screen-v3 tag is accepted | NEUTRAL | - |

**Draft-time rule revisions (disclosed).**
- The first draft had an exact-title de-duplication rule that kept the earlier row in hash order. The dry build showed it would drop the original 10.1136/bmj.m4573 in favour of a same-title later item, so that rule was removed.
- On 2026-11-02 the stricter reading replaced it with removal of whole duplicate groups (row 7).
- None of the affected rows falls within the first 40 queue positions.
