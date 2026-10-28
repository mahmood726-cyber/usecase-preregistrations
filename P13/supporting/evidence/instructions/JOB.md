# JOB F_P13_V5
Paper: P13
Type: V5
Node: baseimage
ALLMETA: allmeta@14dc545/

Job-type file: V5.md. Paper: P13. Previous packages here: C_P13_V4, B_P13_V3. SOURCES: sources/P13_primary and sources/P13_fallback. DECISION (binding, before any data extraction): MAHMOOD_DECISIONS.md item 7 applies to P13. The original papers state random effects (Almutairi also states the Freeman-Tukey transformation) but no statistical package. Fix exactly ONE reproduction configuration now, before any data:
- metafor 5.2.1;
- escalc(measure="PFT") on the printed events/n (the Freeman-Tukey double arcsine, as the paper states);
- rma(method="REML", test="z", level=95);
- back-transformation with transf.ipft.hm using the harmonic mean of n (name it exactly).

For Tang, the transformation is NOT STATED. Use measure="PR" (raw proportions) only if no transformation is stated anywhere in the sources; otherwise use the stated one. Decide this from the sources now and record the evidence.

State every remaining choice explicitly. No model search. Stop rule if the gate fails: primary, then the fallback only if independently cleared, otherwise stop. Remove the F3 blocker only if the sources support this; write BLOCKERS = NONE only if F1-F6 all hold. The REDTEAM2 round follows this job.
