# P11 v4 notes — freeze-candidate reassessment

2026-10-28. Governing precedence: JOB.md/JOB_RULES.md and V4.md, FREEZE_CRITERIA.md, MAHMOOD_DECISIONS.md and COAUTHOR_LOAD.md. The older TASK_COMMON no-file/final-only and v3 pre-freeze runtime requirements are superseded by this job. Only out/ was written.

**BLOCKERS verdict: NONE.** All F1–F6 criteria are satisfied for the selected primary. This is a freeze candidate, not a completed release or permission for real-data work.

## Every v3 blocker

| V3 blocker | Reassessment and disposition |
|---|---|
| B1 — Missing analysis code and pinned-environment validation | The exact v3 source transformations, single primary ML/normal configuration, single fallback fixed-MH/normal configuration, optimizer calls and parity contract are retained in supporting/SOURCE_CHECK_P11.md. F3/F4 are specified prospectively; no model search is permitted. Independent implementation, installed API/version checks, sessionInfo and synthetic validation move to **Mandatory post-release, pre-analysis conditions**. Code must pass synthetic validation before any real-data reproduction gate. No executable R code or runtime pass is claimed. |
| B2 — Incomplete app dependencies and unverified runtime | Rechecked the supplied pin including hub/. All nine formerly missing scripts and all 26 direct script/stylesheet references now exist; all 16 PIN hashes match. F6 implementation is evidenced by files/functions/SHA-256. The identified optional webR bundle entry and package manifest are absent. Dependency closure, full browser workflow and independent R parity remain mandatory after release and before real-data analysis. Static presence is not a runtime pass. |
| B3 — Extraction kit still targets v2 | Move synchronization and meaningful synthetic kit checks into **Mandatory post-release, pre-analysis conditions**, with synchronization additionally required before extraction. Preserve normalized four-digit keys/raw labels, retained/lost versus derived totals, correction provenance, fixed-MH fallback and separate classification/contribution language. The stale builder must not regenerate v2 instructions. No kit files were supplied in the v3 package or validated here. |
| B4 — Fallback prior-analysis eligibility unresolved | Preserve its FEASIBLE-IMAGE status and uncleared novelty status. Text now fixes the permitted contingency: fallback can activate only after its own source/novelty checks clear, before fallback extraction/diagnostics; otherwise primary failure ends the study without replacement. Its original vague sensitivity statement and 35 undispositioned PubMed IDs remain open. Under FREEZE_CRITERIA's fallback provision, this does not block the primary freeze. |
| B5 — Cross-paper verification capacity unconfirmed | COAUTHOR_LOAD.md is now supplied, with P11 eligibility MA, MAY, NA, AO, AW and an empty ledger. The missing-ledger claim is resolved. Actual cross-paper capacity/slot reservation and packet assignment remain mandatory post-release work: ≤30 minutes, one per person per ISO week, Mahmood included, planned row before sending and seven-day reassignment. No packet was assigned or sent. |

## F1–F6 decision

| Criterion | Evidence and decision |
|---|---|
| F1 — Feasible primary | PASS. V3 SOURCE_CHECK says FEASIBLE for Appendix D's four readable analytical count columns and Figure 2 cross-checks. All seven source hashes were rechecked and match. V4 did not re-extract rows. Fallback remains FEASIBLE-IMAGE with its transcription risk preserved. |
| F2 — Novelty | PASS for primary on the supplied Europe PMC/OpenAlex screens: no equivalent prior re-analysis identified. Scholar substitution and coverage limits are explicit. Retrieval counts and original queries are preserved in the main document and hashed P11-only log excerpts. No new independent literature screen is claimed. Fallback remains conditional. |
| F3 — Original model fixed | PASS. Exactly one prospectively declared default configuration per candidate; all NOT STATED items remain labeled. Primary ML/log-RR/normal; fallback panel-specific fixed-MH/normal, with Methods/panel distinction disclosed. Absolute tolerance 0.005 on each target component, exact k and direction, primary → eligible fallback → stop. |
| F4 — Analysis/outcomes specified | PASS. Counts-only mapping, normal REML diagnostics, all deletions, optimizer defaults/controls, full comparison list, normalized 1e-6/1e-9 tolerances and exact identity/flag/CI/S decisions retained. Numeric sensitivity and robustness definitions are unchanged; new/additional requires sensitivity plus prior-report clearance. |
| F5 — Verification | PASS after text repair. Main §4 contains MAHMOOD_DECISIONS item 4 verbatim, followed by the preserved operational rules. No burden, sample, escalation or packet rule weakened. |
| F6 — Static capability | PASS. supporting/APP_EVIDENCE_P11.md cites functions and hashes; supporting/APP_DEPENDENCIES_P11.json records all checked paths. Original gates, transformations, classification and verification procedures are explicitly R-only/procedural. |

## Mandatory post-release, pre-analysis conditions

Main §12 is the controlling action list. Independent R implementation and installed-version checks; generated marked synthetic code/kit tests; complete browser dependencies/workflow; full app/R parity; extraction-kit synchronization; and coordinated co-author packets are outstanding. Stop before real-data reproduction if synthetic validation fails. Every post-release code change must be a dated deviation independent of real-data results. No post-release item has been silently waived.

Fallback clearance is an additional conditional requirement before its activation. No replacement candidate, outcome switching, model search or tolerance adjustment is permitted.

## Other disclosed limitations and future gates

- Original unstated software versions, CI/variance/zero-cell and optimizer details remain assumptions fixed by the single configuration, not reconstructed facts. Current online meta documentation identifies 9.0-0; pc2 must check the specified installed 8.5.0 API on synthetic fixtures.
- Novelty is based on supplied index screens, not proof of universal absence; no individual fallback PubMed dispositions were invented. The Europe PMC primary cited_by 16 versus retrieved/hitcount 18 distinction is preserved.
- Fallback image transcription and source-to-forest mapping require post-release double extraction/verification.
- The target journal is supplied by TASK_PAPER/screening; manuscript submission destination remains unconfirmed.
- App commit provenance is supplied by JOB_RULES/PIN; hashes were verified, but Git provenance was not independently checked.
- No GitHub release, server timestamp, freeze digest record or Zenodo DOI was created. No extraction, reproduction, diagnostics, human verification or result classification has occurred. Those release/real-data gates remain mandatory.

## Validation and scope

Read instructions, previous package, logs and app files with Python only. Seven source hashes and all 16 PIN entries matched; 26 direct browser references are present. Identified lazy dependencies were inspected statically, with two absent webR entry/manifest files recorded explicitly. No supplied corpus was run. No synthetic runtime test is claimed. Official package documentation was read only to check declared defaults; no study-level rows were transcribed.

The final document checks verify the exact decision-item text, preserved numerical rules and code-call specification, local links, manifest consistency, absence of obsolete freeze blockers and the main 3,000-word cap. All outputs are under out/; original files remain unchanged.

Final checks passed: **2295 whitespace-delimited words** in PREREG_P11_usecase.md; BLOCKERS is exactly NONE; item 4 is verbatim; the entire original-model/diagnostic call contract is preserved; local Markdown links resolve; manifest and novelty subsets match their source hashes; all governing/v3 inputs remain unchanged. These are document/static checks, not statistical validation.

Written files: BLOCKERS_P11.md, PREREG_P11_usecase.md, V4_NOTES_P11.md, supporting/APP_DEPENDENCIES_P11.json, supporting/APP_EVIDENCE_P11.md, supporting/NOVELTY_P11.json, supporting/SOURCE_CHECK_P11.md.
