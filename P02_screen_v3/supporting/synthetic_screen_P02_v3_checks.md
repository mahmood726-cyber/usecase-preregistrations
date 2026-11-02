# SYNTHETIC - not data
# P02-screen-v3: approved for freeze and release; not yet released

Offline checks of `screen_P02_v3.py` on generated fixtures and mocked network only. No real candidate was read, screened or scored by these tests; sockets and `urlopen` are patched to fail.

## Test-first record

1. `synthetic_test_screen_P02_v3.py` was written first, against a stub `screen_P02_v3.py` that defined only `FrameError`: **26 tests, 26 errors** (red).
2. After implementation: 25 passed, 1 failed. The failure was a real defect: the section-number stripper removed the leading "I" of "Introduction", so the positional Methods rule kept the Introduction. Fixed at the source (numbers are stripped only when followed by ".", ")" or whitespace); then 26/26.
3. Hardening, test first: a planted-defect run showed that removing `supplementary-material` from the dropped elements was not caught, because the test placed it outside a paragraph. The test now puts a figure, a supplement and a table *inside* a Methods paragraph (JATS allows this); the planted defect then turns the suite red.
4. Test first: a Europe PMC core record without `pubTypeList` must give UNVERIFIED. The new assertion was red (1 failure), then green after the fix.

## Planted defects (each must turn the suite red)

All 13 were caught on the draft bytes: pool starting at rank 15; supplements kept in the view; figures kept; Introduction kept; prior-disposition DOI exclusion removed; dispositioned-title exclusion removed; early Stage F stop accepted; N_S cap removed; OpenAlex retraction flag ignored; missing pubTypeList accepted; DRAFT lock removed; looser effort cap; non-original pubType rule removed.

## Offline dry build on the real archived frame (scratch folder; not a run)

No network; nothing screened. 1,798 frame rows; 16 outside the pool; 72 excluded from ranks 17-1,798 (9 retraction pubType, 36 non-original pubType, 27 protocol titles, each inspected); queue 1,710; Stage F window = v1 ranks 17-58; 0 title-duplicate flags; 0 records without a PMCID. Two independent builds gave the same queue SHA-256 `d5dba663e5247cf834ef3a3978b49db5d4406642d546410e6f06a5756d98fd58` and exclusions SHA-256 `8a267854ac0598ade386e73c8ff4d335dcccc5341be3185de4caa9b571db7f8a`. A second build into the same folder was refused (no overwrite).

## Structural check of the Stage F view on the five v2 sources (already dispositioned)

`stage_f_view` located a titled Methods section in all five and removed every figure, table, supplement and media element. The decisive v2 G1 locators inside the view: v1 rank 8 (Sec3/Par14, Sec5/Par16, Sec6/Par19, abstract), rank 10 (s2-6/p1, s2-6/p2), rank 12 (sec-0005/p2-p3, abstract), rank 13 (sec2.1.1/p0055, sec2.1.4/p0070). Rank 9's k and spline locators (Sec20, Tables 3-4) are outside the view; only its target locator (Sec4/Par26) is inside. Only locators and section titles were compared; no text was re-judged.

## Limitations

No live API compatibility, Stage F pass rate, source feasibility, novelty, candidate selection, statistical validation or app/R parity is established.

## Finalization (2026-11-02), test-first

Decisions of 2026-11-02 (`supporting/DECISION_v3_2026-11-02.md`) changed behaviour in three places. The assertions were changed first: N_S = 5; the approved copy has `DRAFT_ONLY = False` (the draft-lock test now patches the lock explicitly); and the dry-build manifest must report the declared metadata filter stage (input, removals per rule, total, remaining). Against the unchanged script: **3 failures, 1 error** (red). After the script change: **26/26** (green). The test file also locates the script both beside it (working folder) and one level up (package `supporting/` layout).

Planted defects on the final bytes, 14 of 14 caught: the 13 above (with "N_S back to 10" in place of "N_S cap removed", and the receipt lock removed in place of the draft flag), plus a miscounted declared-filter input.

Offline dry build on the final script (scratch, not a run): declared filter stage input 1,782; removed prior_disposition 0, duplicate_title_of_dispositioned 0, metadata_reports_retracted 9, non_original_pubtype 36, non_original_title 27 (total 72); remaining 1,710; Stage F window 40 (v1 ranks 17-58). Queue SHA-256 unchanged: `d5dba663e5247cf834ef3a3978b49db5d4406642d546410e6f06a5756d98fd58`; exclusions `8a267854ac0598ade386e73c8ff4d335dcccc5341be3185de4caa9b571db7f8a`.

## Final run on these bytes

```text
test_complete_frame_accepted_and_cuts_refused (__main__.SyntheticTests.test_complete_frame_accepted_and_cuts_refused) ... ok
test_dispositioned_doi_and_title_duplicates_are_excluded (__main__.SyntheticTests.test_dispositioned_doi_and_title_duplicates_are_excluded) ... ok
test_dispositioned_set_is_the_nineteen_known_dois (__main__.SyntheticTests.test_dispositioned_set_is_the_nineteen_known_dois) ... ok
test_draft_lock_and_pinned_constants (__main__.SyntheticTests.test_draft_lock_and_pinned_constants) ... ok
test_dry_build_writes_labelled_outputs_and_refuses_overwrite (__main__.SyntheticTests.test_dry_build_writes_labelled_outputs_and_refuses_overwrite) ... ok
test_effort_formula_quarter_hours_and_cap (__main__.SyntheticTests.test_effort_formula_quarter_hours_and_cap) ... ok
test_field_protocol_copy_is_byte_identical (__main__.SyntheticTests.test_field_protocol_copy_is_byte_identical) ... ok
test_frame_byte_hash_is_checked (__main__.SyntheticTests.test_frame_byte_hash_is_checked) ... ok
test_metadata_non_original_and_retraction_exclusions (__main__.SyntheticTests.test_metadata_non_original_and_retraction_exclusions) ... ok
test_missing_pmcid_is_kept_and_flagged (__main__.SyntheticTests.test_missing_pmcid_is_kept_and_flagged) ... ok
test_offline_cli (__main__.SyntheticTests.test_offline_cli) ... ok
test_pool_is_never_triaged_ranks_in_seeded_order (__main__.SyntheticTests.test_pool_is_never_triaged_ranks_in_seeded_order) ... ok
test_ranks_14_and_16_style_deferred_rows_are_outside_pool (__main__.SyntheticTests.test_ranks_14_and_16_style_deferred_rows_are_outside_pool) ... ok
test_receipt_contract_on_synthetic_bytes (__main__.SyntheticTests.test_receipt_contract_on_synthetic_bytes) ... ok
test_retraction_status_requires_both_sources (__main__.SyntheticTests.test_retraction_status_requires_both_sources) ... ok
test_run_refused_in_draft_before_file_access (__main__.SyntheticTests.test_run_refused_in_draft_before_file_access) ... ok
test_selection_lexicographic_primary_fallback_only (__main__.SyntheticTests.test_selection_lexicographic_primary_fallback_only) ... ok
test_short_queue_needs_every_record (__main__.SyntheticTests.test_short_queue_needs_every_record) ... ok
test_stage_f_ledger_refuses_skips_reorders_early_stop_and_overrun (__main__.SyntheticTests.test_stage_f_ledger_refuses_skips_reorders_early_stop_and_overrun) ... ok
test_stage_f_view_keeps_headers_methods_and_licence_only (__main__.SyntheticTests.test_stage_f_view_keeps_headers_methods_and_licence_only) ... ok
test_stage_f_view_title_variants_and_positional_fallback (__main__.SyntheticTests.test_stage_f_view_title_variants_and_positional_fallback) ... ok
test_stage_f_view_without_methods_or_xml_fails_closed (__main__.SyntheticTests.test_stage_f_view_without_methods_or_xml_fails_closed) ... ok
test_stage_f_window_is_first_forty (__main__.SyntheticTests.test_stage_f_window_is_first_forty) ... ok
test_stage_s_queue_from_complete_f_ledger (__main__.SyntheticTests.test_stage_s_queue_from_complete_f_ledger) ... ok
test_title_duplicate_flag_forces_f_fail_duplicate (__main__.SyntheticTests.test_title_duplicate_flag_forces_f_fail_duplicate) ... ok
test_within_pool_title_duplicate_is_flagged_not_removed (__main__.SyntheticTests.test_within_pool_title_duplicate_is_flagged_not_removed) ... ok

----------------------------------------------------------------------
Ran 26 tests in 0.229s

OK
```
