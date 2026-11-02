# P04 screen v2: full-screen notes (Option A)

**Result: v2 feasibility failure.** All 5 of 5 dispositions are FAIL. There are zero complete passers, so there is no primary and no fallback. Under section 6 the screen STOPS here. No v3, Option B, new seed, new query, new endpoint or sixth candidate follows without a new explicit decision by Mahmood and a new registration and release. Trial rows recorded: **0**. Novelty requests: **0**, because no record reached G3. Effect data were not extracted or analysed.

## Authority and preflight
- Protocol: `PREREG_P04_screen_v2_DRAFT.md`, the released frozen text. sha256 414a84ef1b39fcda426a925e0f877de22df52a5b9e91be5f9394116a09c7c71a matches `release_receipt_P04_v2.json`. Script sha a1bc0d4f... also matches.
- Frame: `v2_run_01/frame_P04.jsonl`, sha256 3563a7efe93c2f74d6a2718fef647ec5a0132cfc21e32870f0fe69fda7277d1d. It holds 540 UNSCREENED rows. Visits followed `v2_screen_order` 1 to 5 strictly, which is v1 ranks 22 to 26.
- Sources: only the Europe PMC REST API was used (search with resultType=core, and PMC fullTextXML). Every request is logged with URL, HTTP status, UTC time, bytes and sha256 in `screening_events.jsonl`. A polite User-Agent was sent. There were no blocks, logins, mirrors or bot checks. No supplements were fetched. The publisher's own pages were not needed.
- Times are wall-clock UTC, taken from the `disposition_start` and `disposition_end` events. No disposition came near the 60-minute cap.

## Ordered dispositions
| v2 / v1 rank | DOI | Locked outcome / population | Terminal gate | Evidence location | Minutes |
|---|---|---|---|---|---|
| 1 / 22 | 10.1007/s40123-026-01434-w | not locked | SCOPE FAIL. This is a plain-language "Summary of Research" of 10.1007/s40123-025-01247-3, which is v1 FAIL rank 9 and an excluded DOI. It is not an original NMA. | EPMC abstractText sentence 1; fulltext.xml sec "Summary of Research"; ref ext-link | 0.58 |
| 2 / 23 | 10.3389/fendo.2022.895458 | mortality (designated primary, s2_4) / diabetes with COVID-19 | k FAIL. The NMA has 18 "studies" (s3_4). The review is 41 observational studies and 1 RCT (s3_1), and that RCT (ref 53) is outside NMA refs 12-29. Independent-trial k is below 5. | s3_4 P1; s3_1 P1; s4 limitations | 0.90 |
| 3 / 24 | 10.3389/fendo.2025.1462104 | not locked | SCOPE FAIL. The network is nonpharmacological only: exercise modalities and acupuncture versus control. | s3_2 P1; s4_3_1 P2 | 0.37 |
| 4 / 25 | 10.1097/md.0000000000028365 | not locked | SCOPE FAIL. It is a protocol with no results, and its planned network is exercise only. | EPMC title and abstractText | 0.29 |
| 5 / 26 | 10.1111/dom.70742 | CEI (designated primary, sec-0005) / T2D subgroup (Table 1C, Fig S5) | k FAIL. CEI is a composite built from SUCRA rankings across seven endpoint NMAs. It has no outcome-specific trial network and no printed k. | sec-0005 P1; sec-0007 P2; Table 1 note; sec-0010 P1 | 0.91 |

Gates after the terminal gate are recorded as NOT ASSESSED with a reason. Licences seen in passing are recorded only as metadata, not as G1 verdicts: #1 CC BY-NC, #2, #3 and #5 CC BY 4.0, #4 cc by.

## Ambiguities flagged (the stricter reading was applied each time)
1. **#1 derivative summary.** It has a distinct DOI that is not among the 26 exclusions, so it was visited and consumed a slot (section 4). It was scored as a scope FAIL, not as an exclusion.
2. **#2 observational studies as "trials".** Section 3 and G2 count k as "independent trials", and the protocol does not say whether non-randomised studies count. The article's Fig 4 caption calls its edges "trials". Stricter reading: observational studies are not trials, so k fails. Under the looser reading (k=18), the screen would have moved on to follow-up, which was not assessed.
3. **#5 composite primary.** Section 4 uses the fallback hierarchy only when primaries are "several or absent". CEI could be read as several endpoints, which would make HbA1c in T2D the locked outcome. That reading favours the candidate and was not applied. No supplement was fetched and the HbA1c path was not explored.
4. **Process: the gate order in the task brief versus section 4.** The brief lists k first. Section 4 puts bibliographic/scope confirmation and the outcome lock before k. Scope was therefore checked first. This changes only the order of inspection, not any gate.
5. **Process: timing.** Each disposition took under one minute of wall clock, because every failure was established from the abstract and methods text. The times are true wall-clock values from the event log and were not padded.

## Coverage
Five dispositions were completed, so the cap was reached. The frame was not exhausted: v2_screen_order 6 to 540 remain UNSCREENED. Nothing outside `screening_v2/` was written.
