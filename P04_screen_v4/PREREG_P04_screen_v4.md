# P04 screening v4 (P04-screen-v4): the final P04 screen; approved for freeze and release, not yet released

> **Status: approved for freeze and release; not yet released.** Decided by Mahmood on 2026-11-03 (relayed by dispatch; `supporting/DECISION_v4_2026-11-03.md`). Until a public **P04-screen-v4** GitHub release exists, nothing may be screened, scored or selected under this text.

## 0. Authority and predecessor
- **Predecessor.** P04-screen-v3: tag `P04-screen-v3`, commit `c6a3c938d9c914b43ba030ed3866d47f71703a7a`, Zenodo DOI 10.5281/zenodo.23894254 (verified). The released v3 text and script are archived byte-identically in `supporting/v3_archive/` (prereg sha256 `5e2f5f039e53aeffaed8b28a25ecaaa0947e5b8dfbdc22de03cb3e4e04b825e2`, script `91161f79715e7eb337d761fb1a5714c6c47e0305f5b5c8df5d065845b7d1c6e5`, v3 FREEZE.json `bc6ba499e3ae865f72729be72413fe4f1584ebae894680ed73a750c6892fd16f`).
- **v3 outcome.** Stage F: 40 dispositions, 9 F-PASS, 31 F-FAIL. Stage S screened the first 5 F-passers (v3 queue orders 4, 9, 12, 22, 24). Four failed (S4, S4, S3, S6) and one was unresolved (S3, source behind a bot check). Nothing passed, so v3 stopped under its section 6. **This text is the product of a new explicit decision by Mahmood, as v3 section 6 requires.**
- **v3 run outputs archived here.** These are the inputs v4 relies on. The script refuses to run if any byte differs.

| File in `supporting/v3_archive/` | sha256 |
|---|---|
| queue_P04_v3.jsonl (478 rows) | 2a88570287edd5f180861075f7c7833bed8017163be75ff22f213c0b8ce6b03f |
| STAGE_F_LOG_P04_v3.jsonl (40 records) | 547574a44d3542c46facc5c39dc511df662cc845b94cc81e1650c6b683f34807 |
| STAGE_S_LOG_P04_v3.jsonl (5 records) | b0f430c2aed97be0cb5d011711956fc58b2808bb4e738ef4361e7ef5da7b8c0b |
| SELECTION_P04_v3.json | 2eb5e19c3028fdc230332a13dd0e54b379fb80a1bee8fca04c3486de33385a99 |
| SCREEN_NOTES_P04_v3.md | 409341905d6b89dee1455dbc248a141e8416089f4039056a98c5cd12f8231c8f |

`SELECTION_P04_v3.json` records the v3 DOI as `PENDING`, the value at the time it was written; the DOI was minted afterwards.

## 1. What v4 changes, and nothing else
**v4 screens the four v3 Stage F passers that v3's cap of 5 left unscreened.** Every rule of P04-screen-v3 applies unchanged: sections 4-6, the Stage S gate order S1-S12, the 60-minute cap per full screen, the k window 5-60, the effort formula, the selection rule and the stop rule's wording. The binding sources are those of v3: `supporting/FIELD_USE_CASE_PROTOCOL.md` (sha256 `4f6e05206d46059cdbb9bcc6c8a34ac47ebad6e7bb7483e5a5398b6037ce9bac`) and `supporting/MAHMOOD_DECISIONS.md` (`571469f9c90265398f479ac322ea426977674ee14806ee14fd9f90abeac8028f`).

- **No Stage F.** There are no new Stage F visits. Each record's v3 Stage F disposition, locks (outcome, population, follow-up) and flags carry over exactly as in the v3 F log.
- **No re-screening.** No v3 Stage F or Stage S disposition is revisited.
- **Stage S, in this fixed order.** Every one is screened; a failure is not replaced.

| v4 order | v3 queue order | DOI | Title (abridged) |
|---|---|---|---|
| 1 | 25 | 10.3389/fphar.2022.998816 | Tirzepatide in type 2 diabetes: Bayesian NMA |
| 2 | 32 | 10.3389/fendo.2022.897776 | Glucose-lowering drugs in children and adolescents with type 2 diabetes: NMA |
| 3 | 37 | 10.1186/s12903-019-0829-y | Non-surgical periodontal therapy and glycaemic control in type 2 diabetes: Bayesian NMA |
| 4 | 40 | 10.1016/j.eclinm.2022.101463 | Prophylaxis of macular oedema after cataract surgery in diabetes: Bayesian NMA |

- **N_S = 4.** This is every remaining F-passer. The v3 cap of 5 full screens is not exceeded.

## 2. #18: not added (stated before any v4 screening)
Mahmood allowed #18 (v3 queue order 18, 10.1002/dmrr.3670) to be added under the looser drug-name reading of F6 if the coordinator judged it justified, stated in advance. **The coordinator judges it not justified, and #18 is not screened.** The full reasons are in `supporting/DECISION_v4_2026-11-03.md`.
- v3 queue order 33 (10.3389/fendo.2025.1614597) failed F6 on the identical ground: generic growth factors not named by INN. The looser reading cannot be applied to #18 alone.
- Applying it to both would need 6 full screens, above the cap of 5.
- The reading would be chosen after the v3 outcomes were known.

F6 stays exactly as released in v3.

## 3. Procedure
1. pc2 verifies the public P04-screen-v4 release, its server timestamp, its archived bytes and its Zenodo DOI before step 2.
2. `screen_P04_v4.py --build` writes `stage_s_queue_P04_v4.json`. It checks the release arguments and the local hashes, verifies the v3 archive, re-runs the v3 validators on the v3 logs, and checks that the remaining F-passers are exactly orders 25, 32, 37 and 40. Any mismatch stops it.
3. Stage S under v3 section 5, one record at a time, in v4 order. Each record keeps its `v3_queue_order` field, and the log is validated with `validate_v4_stage_s_log` (the v3 Stage S validator with the v4 queue).
4. Selection under v3 section 6, with the retraction check re-run on the primary and fallback first.

Command:
~~~text
python screen_P04_v4.py --build --screen-release-url https://github.com/mahmood726-cyber/usecase-preregistrations/releases/tag/P04-screen-v4 --screen-release-doi RELEASE-TIME-FIELD:zenodo-doi-url-or-PENDING --prereg-sha256 RELEASE-TIME-FIELD:prereg-sha256-from-FREEZE.json --script-sha256 RELEASE-TIME-FIELD:script-sha256-from-FREEZE.json --output-dir out/v4_run_01
~~~

## 4. Stop rule: v4 is final
- **If no record passes Stage S**, stop and report the v4 feasibility failure. **P04's field use case is then closed** as a documented feasibility stop after v1-v4, the same way as P02. No v5, new seed, new query, re-retrieval, further Stage F visit, extra full screen or endpoint switch follows.
- **If one or more records pass**, the provisional primary and fallback are selected under v3 section 6. Nothing beyond selection happens under this text: the later pipeline of v3 section 7 (candidate-specific freeze criteria, red-team review, a use-case freeze and a separate GitHub/Zenodo release) applies before any extraction.

## 5. Testing
`supporting/synthetic_test_screen_P04_v4.py` has 12 tests, run against the archived v3 bytes. All pass on the frozen bytes. They check:
- the queue is exactly orders 25, 32, 37 and 40, in order;
- #18 and #33 are absent;
- no v3-screened record is re-queued;
- tampered v3 logs, queue or script are refused;
- a planted queue that includes #18 fails closed;
- a fifth screen, out-of-order screens, PASS records outside the v3 thresholds and over-cap screens are rejected;
- v1-v3 release tags and wrong hashes are refused;
- output must stay inside the package.
