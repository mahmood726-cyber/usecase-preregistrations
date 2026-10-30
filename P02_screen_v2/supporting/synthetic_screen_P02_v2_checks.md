# SYNTHETIC - not data

Offline draft-code checks on generated bibliographic fixtures and mocked HTTP only.
No live requests, real candidate frames, screening, scoring or analysis were run.
All test frames/manifests/receipts were held in memory; no approval receipt was issued.

Tests: 20; failures: 0; errors: 0.

Validates DOI/date handling, exclusions, seeded ordering, original-frame reconciliation, A/B separation, draft/receipt locks, pagination, failure manifests, access refusal and output guards.

Limitations: no live API compatibility, real inventory completeness, source eligibility, novelty, candidate selection, statistical validation or app/R parity is established.

```text
test_403_and_transport_are_not_retried (__main__.SyntheticTests.test_403_and_transport_are_not_retried) ... ok
test_5xx_retry_budget_and_no_bot_retry (__main__.SyntheticTests.test_5xx_retry_budget_and_no_bot_retry) ... ok
test_approved_copy_receipt_contract_using_only_synthetic_bytes (__main__.SyntheticTests.test_approved_copy_receipt_contract_using_only_synthetic_bytes) ... ok
test_archive_byte_hash_mismatch (__main__.SyntheticTests.test_archive_byte_hash_mismatch) ... ok
test_archive_mismatch_missing_duplicate_rank_hash_and_order_fail (__main__.SyntheticTests.test_archive_mismatch_missing_duplicate_rank_hash_and_order_fail) ... ok
test_date_edges_dedup_conflicts_and_exclusions (__main__.SyntheticTests.test_date_edges_dedup_conflicts_and_exclusions) ... ok
test_doi_normalization_and_suffix (__main__.SyntheticTests.test_doi_normalization_and_suffix) ... ok
test_draft_lock_prevents_read_or_network (__main__.SyntheticTests.test_draft_lock_prevents_read_or_network) ... ok
test_failure_manifest_never_becomes_zero_frame (__main__.SyntheticTests.test_failure_manifest_never_becomes_zero_frame) ... ok
test_final_copy_fixes_option_A_and_refuses_B_before_file_access (__main__.SyntheticTests.test_final_copy_fixes_option_A_and_refuses_B_before_file_access) ... ok
test_full_pagination_and_true_zero (__main__.SyntheticTests.test_full_pagination_and_true_zero) ... ok
test_incomplete_and_drift_duplicate_bad_schema_fail (__main__.SyntheticTests.test_incomplete_and_drift_duplicate_bad_schema_fail) ... ok
test_offline_queries_and_cli_refusal (__main__.SyntheticTests.test_offline_queries_and_cli_refusal) ... ok
test_option_A_execution_makes_no_query (__main__.SyntheticTests.test_option_A_execution_makes_no_query) ... ok
test_option_B_excludes_entire_v1_including_deferred (__main__.SyntheticTests.test_option_B_excludes_entire_v1_including_deferred) ... ok
test_original_archive_validation_and_option_A (__main__.SyntheticTests.test_original_archive_validation_and_option_A) ... ok
test_output_containment_and_overwrite_refusal (__main__.SyntheticTests.test_output_containment_and_overwrite_refusal) ... ok
test_receipt_rejects_v1_wrong_option_unreconciled_and_wrong_hash (__main__.SyntheticTests.test_receipt_rejects_v1_wrong_option_unreconciled_and_wrong_hash) ... ok
test_schema_projection_discards_abstract_and_data (__main__.SyntheticTests.test_schema_projection_discards_abstract_and_data) ... ok
test_seed_order_is_deterministic_and_no_scores (__main__.SyntheticTests.test_seed_order_is_deterministic_and_no_scores) ... ok

----------------------------------------------------------------------
Ran 20 tests in 0.227s

OK
```

## Finalization checks (2026-10-30; Option A approved)

Re-run on the finalized bytes: 20 tests, 0 failures, 0 errors (19 draft tests plus one new lock test). Changes to the suite: the draft-lock test now patches `DRAFT_ONLY=True` explicitly and still requires refusal before file access; a new test requires `DRAFT_ONLY=False`, `APPROVED_OPTION="A"`, the v1 seed 2026102802, and refusal of option B before file access; the receipt-contract and receipt-mutation tests now use option A (the mutation set gained `frame_option="B"` and a wrong `ordering_seed`, so each mutation is still a real rejection rather than a refusal caused by option B). A planted defect (option-B guard removed) made the suite fail, so the new lock test can fail.

Offline metadata check of the recovered v1 archive (no network, nothing screened): the complete `frame_P02.jsonl` (1,798 rows, SHA-256 c2aad90c...a1a04) is REFUSED by the script's archive check, which requires exactly the 16 triaged rows; its first 16 rows match the inventory, and all 1,798 order hashes equal the v1-seed hashes. See BLOCKERS item B2-S.
