# Job type V5: apply second-round red-team findings, then produce a freeze candidate

Inputs: the v4 package (folder `C_<PAPER>_V4`), the red-team-2 report (folder `D_<PAPER>_REDTEAM2`), FREEZE_CRITERIA.md, the sources (JOB.md), and any coordinator decision given in JOB.md.

1. For every REDTEAM2 finding, apply its exact replacement text, OR the coordinator's decision in JOB.md where one is given. Record which you applied in `out/V5_NOTES_<PAPER>.md`.
2. Where the coordinator fixes a documentary interpretation, verify it against the sources yourself:
   - quote the exact source text that supports it;
   - quote the exact source text that conflicts with it;
   - state the prespecified rule: the single mapping fixed now; NO switching on gate failure; stop rule.
   If you find the coordinator's reading contradicted by the sources, do NOT apply it. Keep the blocker and explain why.
3. Put every evidence file that the prereg cites into `out/supporting/evidence/`, as exact byte copies with sha256 recorded. Use relative citations only, never node paths.
4. Write `out/PREREG_<PAPER>_usecase.md` (v5, at most 3,000 words), `out/supporting/` (all supporting files, updated consistently), and `out/BLOCKERS_<PAPER>.md` (F1-F6 failures only, or `NONE`).
5. Do not weaken any gate, the verification spec, or the new-versus-robust definitions.
