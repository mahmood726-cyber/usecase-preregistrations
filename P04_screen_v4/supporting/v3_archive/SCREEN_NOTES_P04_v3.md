# P04-screen-v3: screening notes (run 2026-11-02)

**Outcome: v3 feasibility failure.** None of the five Stage S records passed, so `select_passers` returns (None, None) and the section 6 stop rule applies. This run makes no claim about clinical effects and records no effect data.

## Authority and inputs
- **Release.** Tag `P04-screen-v3`, commit c6a3c938, published 2026-11-02T19:03:10Z. The Zenodo DOI is PENDING. The coordinator receipt is `out/release_receipt_P04_v3.json`.
- **Local bytes match FREEZE.json:**
  - prereg 5e2f5f03…25e2;
  - script 91161f79…c6e5;
  - queue 2a885702…b03f (478 rows).
- **Package.** Nothing in `pkg\` was edited. The only writes inside it are the frozen script's own `--stage-f-extract` outputs, in `pkg/out/v3_run_01/stage_f_extracts/`. Byte copies of those outputs are in `extracts/`.

## Stage F (N_F = 40, queue positions 1-40, cap 20 min)
- **Totals:** 9 F-PASS, 31 F-FAIL, 0 F-UNRESOLVED. No disposition took more than 1.1 min of wall-clock time.
- **F-FAIL by terminal step:**

  | Terminal step | Count |
  |---|---|
  | F4 licence | 10 |
  | F6 drug nodes | 8 |
  | F2 article type | 5 |
  | F5 population | 4 |
  | F7 design | 2 |
  | F8 outcome lock | 1 |
  | F9 k | 1 |

- **F-PASS queue positions:** 4, 9, 12, 22, 24, 25, 32, 37, 40.
- **Validator.** The F log was validated (`validate_stage_f_log(final=True)` returned []) and hashed (547574a4…4807) before Stage S started.
- **Reading restriction.** Each source was fetched by `tools/http_get.py`, which prints only status, byte count and sha256. Stage F material came only from the frozen `--stage-f-extract`, plus selected Europe PMC core, OpenAlex and Crossref metadata fields (`tools/show_f.py`).
  - No raw XML was printed, read or grepped.
  - Methods were often printed only in part (eligibility or keyword windows). Each record's `sections_read` and `notes` say which.

## Stage S (first five F-passers: queue positions 4, 9, 12, 22, 24; cap 60 min)
| Queue | DOI | Result | Terminal gate | Min | Key evidence |
|---|---|---|---|---|---|
| 4 | 10.3389/fendo.2026.1843370 | FAIL | S4 | 1.9 | HbA1c network k=48 printed (S3 PASS). No designated, outcome-level or per-trial time rule anywhere, including the supplement (DataSheet1.docx). The trial durations in Table 1 are an inventory and cannot supply a time point. |
| 9 | 10.1186/s40199-017-0189-6 | FAIL | S4 | 0.5 | HbA1c k=32 printed. "Change from baseline" has no time rule. The Table 1 "Weeks" column is an inventory. |
| 12 | 10.3389/fphar.2025.1613610 | FAIL | S3 | 2.5 | The locked outcome (constipation, from the C4 alphabetical rule) has no printed k. There is only a citation list; Figure 5E has no numbers; the supplement holds search strategies only. |
| 22 | 10.3389/fendo.2023.1096105 | FAIL | S6 | 2.3 | CMT k = 8 and 12 (12 at the locked 12 months). In Table 1 the per-arm dispersion (±) is unlabelled (SD or SE) and n is "Total eyes", not an analysed n. |
| 24 | 10.3389/fendo.2020.00553 | UNRESOLVED | S3 | 3.8 | Only the review total (23) is printed. The HbA1c network figure was blocked (Cloudflare, HTTP 403) and the supplement request timed out twice. |

- **Validator.** `validate_stage_s_log(final=True)` returned []. The S log sha256 is b0f430c2…c0b.
- **No replacements.** The 6th to 9th F-passers (queue positions 25, 32, 37 and 40) were not screened, because there is no 6th S screen.

## Ambiguities: the stricter reading was applied, and each is flagged in the logs
1. **q02 F6: TCM + "conventional Western medicine" nodes.** The lumped CWM was treated as background (CONTROL), so every node is herbal → FAIL.
2. **q08 F9.** The review admits only fracture-reporting trials, so "75 RCTs" was treated as the k for the locked bone-fracture outcome → FAIL (above 60). The same reading was applied consistently at q32 and q37, where it gave PASS.
3. **q18 and q33 F6: growth-factor nodes not named by INN** (rhPDGF, rhEGF, and so on) → OUT → FAIL. Under the looser reading ("the substance has an INN": becaplermin, nepidermin) both would pass F6. **This reading needs coordinator review:** q18 would otherwise have been a candidate F-passer before q22.
4. **Licence URL printed inside the licence text, not as xlink:href (q01, q18, q37).**
   - The frozen extractor reads only the href attribute. The protocol rule "the licence URL governs" was applied by passing the printed URL to the frozen `licence_verdict`.
   - The protocol rule decides q18's F4 (PASS). It does not change q01 (CC BY-NC: FAIL either way) or q37 (PASS either way).
   - For q37, the frozen text-only call labels the licence "CC0", because the article's CC0 *data* waiver is matched first. The article licence is CC BY.
5. **q12 F7.** The RCT restriction is stated as the purpose of the search. **q12 F8:** the C4 alphabetical rule locks "constipation".
6. **q22 F8 (C3).** The tie-break depends on the printed label: the full phrases lock CMT, while the abbreviations alone would lock BCVA. **q22 F10:** two time points with none designated → DEFERRED. **q22 S3:** the k sentence in the CMT subsection says "BCVA", read as a typo. **q22 S6:** unlabelled ± and "Total eyes" → FAIL.
7. **q24 F10.** "Baseline to endpoint" was read as a per-trial time rule.
8. **q27 F2.** A methods paper that refits another NMA's dataset → FAIL.
9. **q30 F8.** Methods never state which outcomes entered the NMA → C4 "no such outcome" → FAIL.
10. **q37 F6.** SRP+antibiotic and SRP+aPDT+doxycycline were classed as IN under the literal "drug plus a non-drug co-intervention" rule. This has no effect on Stage S, because q37 is the 8th passer.
11. **q24 S3.** Recorded as UNRESOLVED rather than FAIL because the decisive sources were inaccessible. Both outcomes are terminal.

## Exposure events
- **No forbidden Stage F material was seen.**
- **Disclosures:**
  1. q24's Methods prose (delivered by the frozen extractor; not a figure element) describes the lines of Figure 2. This was logged as `exposure_note`; it was not used.
  2. The Stage F abstracts include Results subsections with effect estimates. Reading them is allowed; they were used only for counts and designs.
  3. When the queue was first inspected, archived titles for queue positions 1-45 were printed. This is bibliographic metadata only; positions 41-45 were never visited.
  4. One connectivity-probe request was made before logging began: the Crossref F3 URL for q01, with status and length only. It is recorded in `request_log.jsonl` with a null sha.

## Access events
- **q24, Cloudflare bot check.** https://europepmc.org/articles/PMC7466678/bin/fendo-11-00553-g0002.jpg returned HTTP 403 "Just a moment...". It was not bypassed, and no mirror was tried.
- **Europe PMC REST supplementaryFiles timeouts.**
  - q12: timed out once; one retry succeeded.
  - q24: timed out twice; stopped.
- **Retraction checks.** All 120 F3 requests and 15 S1 requests returned HTTP 200. Crossref "correction" flags appeared only on q13 and q27, both F-FAIL.

## Files (all in this folder)
- **Logs:**
  - `STAGE_F_LOG_P04_v3.jsonl`;
  - `STAGE_S_LOG_P04_v3.jsonl`;
  - `screening_events.jsonl`;
  - `request_log.jsonl` (every URL, status, bytes and sha256).
- **Results:**
  - `stage_s_queue_P04_v3.json`;
  - `SELECTION_P04_v3.json`.
- **Source material:**
  - `extracts/` (Stage F extracts);
  - `sources/` (raw responses, JATS and supplements).
- **Tooling and integrity:**
  - `tools/` (the fetch, display, logging and validation helpers used);
  - `MANIFEST_SHA256_P04_v3.txt`.
