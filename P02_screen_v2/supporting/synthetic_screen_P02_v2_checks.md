# SYNTHETIC - not data

Offline draft-code checks on generated bibliographic fixtures and mocked HTTP only.
No live requests, real candidate frames, screening, scoring or analysis were run.
All test frames/manifests/receipts were held in memory; no approval receipt was issued.

Tests: 23; failures: 0; errors: 0.

Validates DOI/date handling, exclusions, seeded ordering, original-frame reconciliation, A/B separation, draft/receipt locks, pagination, failure manifests, access refusal and output guards.

Limitations: no live API compatibility, real inventory completeness, source eligibility, novelty, candidate selection, statistical validation or app/R parity is established.

```text
test_403_and_transport_are_not_retried (__main__.SyntheticTests.test_403_and_transport_are_not_retried) ... ok
test_5xx_retry_budget_and_no_bot_retry (__main__.SyntheticTests.test_5xx_retry_budget_and_no_bot_retry) ... ok
test_approved_copy_receipt_contract_using_only_synthetic_bytes (__main__.SyntheticTests.test_approved_copy_receipt_contract_using_only_synthetic_bytes) ... ok
test_archive_byte_hash_mismatch (__main__.SyntheticTests.test_archive_byte_hash_mismatch) ... ok
test_archive_mismatch_missing_duplicate_rank_hash_and_order_fail (__main__.SyntheticTests.test_archive_mismatch_missing_duplicate_rank_hash_and_order_fail) ... ok
test_complete_frame_shaped_archive_is_accepted_for_option_A (__main__.SyntheticTests.test_complete_frame_shaped_archive_is_accepted_for_option_A) ... ok
test_date_edges_dedup_conflicts_and_exclusions (__main__.SyntheticTests.test_date_edges_dedup_conflicts_and_exclusions) ... ok
test_doi_normalization_and_suffix (__main__.SyntheticTests.test_doi_normalization_and_suffix) ... ok
test_draft_lock_prevents_read_or_network (__main__.SyntheticTests.test_draft_lock_prevents_read_or_network) ... ok
test_failure_manifest_never_becomes_zero_frame (__main__.SyntheticTests.test_failure_manifest_never_becomes_zero_frame) ... ok
test_final_copy_fixes_option_A_and_refuses_B_before_file_access (__main__.SyntheticTests.test_final_copy_fixes_option_A_and_refuses_B_before_file_access) ... ok
test_full_pagination_and_true_zero (__main__.SyntheticTests.test_full_pagination_and_true_zero) ... ok
test_incomplete_and_drift_duplicate_bad_schema_fail (__main__.SyntheticTests.test_incomplete_and_drift_duplicate_bad_schema_fail) ... ok
test_offline_queries_and_cli_refusal (__main__.SyntheticTests.test_offline_queries_and_cli_refusal) ... ok
test_option_A_execution_makes_no_query (__main__.SyntheticTests.test_option_A_execution_makes_no_query) ... ok
test_option_A_never_labels_untriaged_rows_as_terminal_screens (__main__.SyntheticTests.test_option_A_never_labels_untriaged_rows_as_terminal_screens) ... ok
test_option_B_excludes_entire_v1_including_deferred (__main__.SyntheticTests.test_option_B_excludes_entire_v1_including_deferred) ... ok
test_original_archive_validation_and_option_A (__main__.SyntheticTests.test_original_archive_validation_and_option_A) ... ok
test_output_containment_and_overwrite_refusal (__main__.SyntheticTests.test_output_containment_and_overwrite_refusal) ... ok
test_receipt_rejects_v1_wrong_option_unreconciled_and_wrong_hash (__main__.SyntheticTests.test_receipt_rejects_v1_wrong_option_unreconciled_and_wrong_hash) ... ok
test_schema_projection_discards_abstract_and_data (__main__.SyntheticTests.test_schema_projection_discards_abstract_and_data) ... ok
test_seed_order_is_deterministic_and_no_scores (__main__.SyntheticTests.test_seed_order_is_deterministic_and_no_scores) ... ok
test_sixteen_row_cut_and_bad_untriaged_rows_are_refused (__main__.SyntheticTests.test_sixteen_row_cut_and_bad_untriaged_rows_are_refused) ... ok

----------------------------------------------------------------------
Ran 23 tests in 0.100s

OK
```

## Finalization checks (2026-10-30; Option A approved; B2-S corrected)

Re-run on the finalized bytes: **23 tests, 0 failures, 0 errors**: 19 draft tests, 1 option-lock test and 3 B2-S tests.

Changes to the suite:
- The draft-lock test patches `DRAFT_ONLY=True` explicitly.
- A new test requires `APPROVED_OPTION="A"` and the v1 seed, and refuses option B before file access.
- The receipt tests use option A, with two added mutations.
- The fixture takes an optional count of never-triaged rows (`extra`), and patches `V1_FRAME_RECORD_COUNT`.
- B2-S tests, written first:
  - a complete-frame-shaped archive (16 triaged rows plus 8 never-triaged) is accepted, and gives the seven deferred rows with five inside the batch;
  - a 16-row cut, a missing row, and a bad hash, rank, order or duplicate in the never-triaged ranks are all refused;
  - Option A never labels never-triaged rows as terminal screens.

Before the fix, these three tests failed (1 failure, 2 errors) and the other 20 passed. After the fix, all 23 pass. Planted defects (option-B guard removed; option set to B) also turn the suite red.

Offline check of the real recovered v1 archive (no receipt, no network, nothing screened or written):
- `load_v1_frame` accepts the complete `frame_P02.jsonl` (1,798 rows, SHA-256 c2aad90c...a1a04).
- The continuation queue is v1 ranks 8, 9, 10, 12 and 13 inside the five-slot batch, with 14 and 16 outside it.
- A 16-row cut, a missing last row and a wrong receipt hash are refused.
- Option A's exclusion log would label 1,782 never-triaged rows as `v1_never_triaged_outside_option_A_queue` and 9 rows as `v1_terminal_screen`.
