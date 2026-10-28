# P14 and P06 preregistrations: what changed and why (2026-10-27 to 2026-10-28)

No trial data have been extracted and no analysis has been run. Every number below traces to a saved file.

## Status

| Step | State |
|---|---|
| Frames pulled, deduplicated, seeded | Done (P14 3433, P06 5205; manifests and sha256 in SEARCH_LOG.md) |
| Screening + AM-S7 + **AM-S8 second pass** | Done; yields below |
| P14 reserve frame (AM-P14-R) | Pulled and screened: **5 eligible of 730** |
| PR mahmood726-cyber/allmeta#278 | **Merged**: 0dd16ee6, 2026-10-28T08:12:36Z, after all CI passed |
| metafor 5.2-1 | Installed. P06 app-vs-R and the P14 41-case check re-run: identical, all pass |
| Freeze / secret scan / push | See the final report |
| **GitHub release + Zenodo DOI** | **Blocked: Zenodo is not enabled for `usecase-preregistrations`** (no Zenodo webhook on the repo) |
| Extraction | **Not started.** `MMA_extraction/extract.py` refuses to run until a release carries the frozen FREEZE.json |

## Feasibility (at least 10 eligible) — established at screening for both pilots

| | Frame | Screened | Eligible | Yield, Wilson 95% CI | Selection |
|---|---:|---:|---:|---|---|
| **P14** | 3433 | 3433 (exhausted) | **18** | 0.52% (0.33-0.83%) | all 18 |
| **P14 reserve** | 730 | 730 (exhausted) | **5** | 0.68% (0.29-1.59%) | used only if fewer than 10 of the main 18 pass all gates |
| **P06** | 5205 | 3300 | **36** | 1.09% (0.79-1.51%); ~57 projected (41-78) | first 30; stopping rank **2769** (was 3265) |

UNRESOLVED records still count as not eligible: P14 152, P06 67.

Sources:
- `screening/YIELD_SUMMARY.json`
- `screening/SELECTION_P14.json`
- `screening/SELECTION_P06.json`
- `reserve_P14/screening/RESERVE_ORDER_P14.json`

## What changed since the last report

1. **AM-S6b.** The P14 0-17 age rule is kept. The draft records that accepting ages up to 18 was considered after the yield was seen, and was declined.
2. **AM-S8 second pass**, written into both drafts before it ran. It covers the UNRESOLVED records coded "independence unclear".
   - Codex transcribed only forest-plot row labels. A deterministic rule decided independence: any repeated author-year label, or a shared/split-control note, means not independent.
   - A 2026-10-28 clarification, made while the pass ran: independence counts as met only with one label per designated trial. It was added because one record (P14 rank 506) had 8 labels for k = 12; it is applied to every record and disclosed.
   - **Result:**
     - P14: 18 eligible (was 14).
     - P06: 36 eligible, so its first 30 now end at rank 2769, and the reviews at ranks 2805-3265 are displaced in seeded order.
3. **AM-P14-R: reserve and fallback.** The requested 2012-2016 window breaks the "within ten years" rule, so the nearest compliant window was used instead: 2016-10-27 to 2016-12-31 plus 2026-01-01 to 2026-10-27. It was pulled and screened identically, with byte-identical code and seed 2026102714.
   - Reserve reviews are added in seeded order only if fewer than 10 of the main 18 pass all gates, and they are reported as reserve-sourced.
   - Final fallback: an insufficient-yield report, with the paper using **Kuitunen et al. 2025, Eur J Pediatr 184:34, DOI 10.1007/s00431-024-05839-2** (video laryngoscopy; first-attempt success).
4. **AM-H2: capped human verification**, replacing AM-H1's scope in both drafts.
   - Humans check all rows of headline reviews, plus a seeded 5% sample (at least 1 row per review).
   - Adjudicated discrepancies go to a fourth AI pass (agy on GPT-OSS 120B). Only fields the AIs still dispute reach humans.
   - Escalation means a full AI re-extraction plus a human check of headline rows.
   - Packets are capped at about 30 minutes (~20 rows), one per co-author per week, round-robin with Mahmood included. An unreturned packet is reassigned after 7 days.
5. **P14 pin.** Merge commit 0dd16ee6; `index.html` sha256 6ff010e0...; the R reference is regenerated under metafor 5.2-1, numerically identical, 32/32 tests pass, and the independent rule re-derivation finds 0 mismatches. One flaky pixels test in an unrelated app (limit-ma) failed once and passed on rerun.
6. **P06 pin.** App-vs-R re-run under metafor 5.2-1: maximum difference 4.4e-15, PEESE branch agrees, R values identical to the 5.0.1 run.

## Expected human load under AM-H2 (`screening/HUMAN_LOAD_ESTIMATE.json`)

The headline share is unknown until the analysis has run, so it is shown as scenarios. Headline reviews are assumed to be the largest-k reviews, a conservative upper bound. The estimate assumes 1.5 minutes per row, about 20 rows per packet, and excludes the few fields still disputed after the fourth AI pass.

| Pilot | Headline share | Human rows | Packets | Packets per co-author (4 / 6 checkers) | Weeks at 1 packet/week (4 / 6) |
|---|---|---:|---:|---|---|
| P14 (18 reviews, 234 rows) | none | 19 | 1 | 0.25 / 0.17 | 1 / 1 |
| | 25% | 85 | 5 | 1.25 / 0.83 | 2 / 1 |
| | 50% | 144 | 8 | 2.0 / 1.33 | 2 / 2 |
| | all | 234 | 12 | 3.0 / 2.0 | 3 / 2 |
| P06 (30 reviews, 404 rows) | none | 31 | 2 | 0.5 / 0.33 | 1 / 1 |
| | 25% | 163 | 9 | 2.25 / 1.5 | 3 / 2 |
| | 50% | 253 | 13 | 3.25 / 2.17 | 4 / 3 |
| | all | 404 | 21 | 5.25 / 3.5 | 6 / 4 |

Co-author lists are not yet confirmed: the claim sheet has no "Yes" entries. The sheet's own rule gives 4-6 authors per paper, including MA and AW, hence the 4 and 6 checker scenarios. The **same candidate co-authors appear on both papers**. If the same people check both, the one-packet-per-week cap applies to their combined load. At a 50% headline share that is 21 packets: about 6 weeks with 4 checkers, 4 weeks with 6.

## Extraction pipeline (built and tested on a synthetic control only)

`pipeline/MMA_extraction/` contains:
- `extract.py`: the release-gated dispatcher. It runs Codex on the desktop and on baseimage alongside agy, with the title-echo guard.
- `verify.py`: compare, Claude adjudication, the fourth AI pass, AM-H2 packets and the scheduler.
- `reproduce.R`: gate 2.

Self-test on `__control_selftest`, a synthetic review:
- The three extractors agreed on all 152 compared fields.
- The reproduction gate passed.
- A planted-discrepancy test of the adjudicator passed: it chose the source value with a citation for both plants.

Defects found and fixed by the self-test:
- Codex's `-i` flag is variadic and swallowed the prompt.
- agy's transcript truncates messages above about 4 KB, so agy now writes its output to a file.
- Two workers shared output filenames, which masked a failure.

**Not yet verified:**
- agy running GPT-OSS headless for the fourth pass. AM-H2 sends those fields to humans until it is shown to work.
- The laptop worker is unreachable (SSH timeout).
- The baseimage Codex CLI was upgraded to 0.153.4 and is called by full path, because the Codex desktop app's older 0.142.3 comes first on its PATH.
- The desktop Codex seat hit rate limits (HTTP 429) under heavy load. Retries at lower concurrency cleared every record, so the extraction concurrency must be set below that level.

## For Mahmood

1. **Enable Zenodo for `mahmood726-cyber/usecase-preregistrations`** (zenodo.org → GitHub → toggle the repo on). Then I create the release, which Zenodo archives with a DOI. A release made before enabling would get no DOI.
2. Confirm co-author lists per paper. Packets are sized for 4-6 checkers each.
