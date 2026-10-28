SYNTHETIC - not data
# Offline P02 screening-script checks - amendment A1

UTC: 2026-10-28T19:14:30.308999+00:00
Python: 3.13.13
Script SHA-256: d55ef926f9ca275b2f404954094286cee012b8a42e3643473eaefd5ce58f8b3c
Prereg SHA-256: bc0d103ec22a2a8e9c904fc3cb15a77e4d0ddbad97f8bdabe59af20c776f4327

Checks: 29; failures: 0; errors: 0.
All API responses, candidate metadata and run-output fixtures were fabricated in memory.
Coverage: Europe-PMC-only discovery; bounded 5xx retries; failed/blocked versus zero;
OpenAlex page-based novelty, empty termination and 10,000-record limits; unchanged screening rules.
No network calls, candidate screens, real-data extraction or statistical fits were performed.
These checks do not certify live APIs, retrieval yield, real source feasibility or app/R parity.

```text
test_5xx_exhaustion_is_bounded_and_logged (__main__.SyntheticChecks.test_5xx_exhaustion_is_bounded_and_logged) ... ok
test_5xx_retry_backoff_and_success_receipt (__main__.SyntheticChecks.test_5xx_retry_backoff_and_success_receipt) ... ok
test_access_errors_challenges_and_transport_never_retry (__main__.SyntheticChecks.test_access_errors_challenges_and_transport_never_retry) ... ok
test_all_five_previous_dois_excluded_case_insensitively (__main__.SyntheticChecks.test_all_five_previous_dois_excluded_case_insensitively) ... ok
test_cli_is_offline_by_default_and_query_printing_is_offline (__main__.SyntheticChecks.test_cli_is_offline_by_default_and_query_printing_is_offline) ... ok
test_complete_zero_requires_successful_response (__main__.SyntheticChecks.test_complete_zero_requires_successful_response) ... ok
test_dates_oa_retraction_and_missing_doi (__main__.SyntheticChecks.test_dates_oa_retraction_and_missing_doi) ... ok
test_deduplication_retains_provenance_and_date_conflict (__main__.SyntheticChecks.test_deduplication_retains_provenance_and_date_conflict) ... ok
test_discovery_execute_only_epmc_and_complete_output (__main__.SyntheticChecks.test_discovery_execute_only_epmc_and_complete_output) ... ok
test_discovery_failed_manifest_no_frame_and_no_zero (__main__.SyntheticChecks.test_discovery_failed_manifest_no_frame_and_no_zero) ... ok
test_document_urls_exclusions_and_verification_are_synchronized (__main__.SyntheticChecks.test_document_urls_exclusions_and_verification_are_synchronized) ... ok
test_doi_normalization_and_valid_suffix_punctuation (__main__.SyntheticChecks.test_doi_normalization_and_valid_suffix_punctuation) ... ok
test_epmc_complete_zero_and_invalid_pagination (__main__.SyntheticChecks.test_epmc_complete_zero_and_invalid_pagination) ... ok
test_epmc_multi_page_complete (__main__.SyntheticChecks.test_epmc_multi_page_complete) ... ok
test_exact_frozen_query_parameters (__main__.SyntheticChecks.test_exact_frozen_query_parameters) ... ok
test_http_forbidden_and_html_are_failures (__main__.SyntheticChecks.test_http_forbidden_and_html_are_failures) ... ok
test_jsonl_output_round_trip_in_memory (__main__.SyntheticChecks.test_jsonl_output_round_trip_in_memory) ... ok
test_novelty_cli_requires_release_and_uses_separate_mode (__main__.SyntheticChecks.test_novelty_cli_requires_release_and_uses_separate_mode) ... ok
test_openalex_incomplete_partial_count_duplicate_schema_and_access (__main__.SyntheticChecks.test_openalex_incomplete_partial_count_duplicate_schema_and_access) ... ok
test_openalex_limit_and_exact_boundary_are_explicitly_incomplete (__main__.SyntheticChecks.test_openalex_limit_and_exact_boundary_are_explicitly_incomplete) ... ok
test_openalex_lookup_failure_is_recorded_not_zero (__main__.SyntheticChecks.test_openalex_lookup_failure_is_recorded_not_zero) ... ok
test_openalex_novelty_empty_zero_is_complete (__main__.SyntheticChecks.test_openalex_novelty_empty_zero_is_complete) ... ok
test_openalex_novelty_output_keeps_lookup_profile_and_does_not_clear_gate (__main__.SyntheticChecks.test_openalex_novelty_output_keeps_lookup_profile_and_does_not_clear_gate) ... ok
test_openalex_novelty_pages_until_empty_without_discovery_filters (__main__.SyntheticChecks.test_openalex_novelty_pages_until_empty_without_discovery_filters) ... ok
test_output_root_restriction_before_writes (__main__.SyntheticChecks.test_output_root_restriction_before_writes) ... ok
test_preserved_screening_rules_and_pre_freeze_amendment (__main__.SyntheticChecks.test_preserved_screening_rules_and_pre_freeze_amendment) ... ok
test_projection_omits_abstracts_and_nonbibliographic_payloads (__main__.SyntheticChecks.test_projection_omits_abstracts_and_nonbibliographic_payloads) ... ok
test_release_hash_mismatch_stops (__main__.SyntheticChecks.test_release_hash_mismatch_stops) ... ok
test_seed_hash_independent_oracle_and_order_invariance (__main__.SyntheticChecks.test_seed_hash_independent_oracle_and_order_invariance) ... ok

----------------------------------------------------------------------
Ran 29 tests in 0.163s

OK
```
