SYNTHETIC - not data

# Offline amended frame-builder and novelty-helper validation

Tests run: 51; failures: 0; errors: 0.
API responses and hypothetical candidate metadata are SYNTHETIC - not data.
Real exclusion DOIs and frozen query strings are checked only as unchanged configuration.
No live API, candidate screening or statistical engine ran; a socket audit hook forbids network access.
Fake output streams stayed in memory; no real frame_P04.jsonl was generated.
This validates Europe PMC-only discovery, bounded 5xx retries, failure/zero separation, page-based
OpenAlex novelty limits, metadata ordering and preserved rules. It does not validate live API availability, query semantics,
a public release, candidate feasibility/novelty, or app/R parity.

~~~text
test_date_boundaries_and_missing_date (__main__.FrameTests.test_date_boundaries_and_missing_date) ... ok
test_earliest_conflicting_date_determines_eligibility (__main__.FrameTests.test_earliest_conflicting_date_determines_eligibility) ... ok
test_hash_collision_tie_break (__main__.FrameTests.test_hash_collision_tie_break) ... ok
test_invalid_doi_is_audited (__main__.FrameTests.test_invalid_doi_is_audited) ... ok
test_no_five_hit_truncation (__main__.FrameTests.test_no_five_hit_truncation) ... ok
test_oa_conflicts_retained_and_flagged (__main__.FrameTests.test_oa_conflicts_retained_and_flagged) ... ok
test_preserves_significant_suffix (__main__.FrameTests.test_preserves_significant_suffix) ... ok
test_previously_screened_exclusion_survives_aliases (__main__.FrameTests.test_previously_screened_exclusion_survives_aliases) ... ok
test_resolver_and_case_deduplication (__main__.FrameTests.test_resolver_and_case_deduplication) ... ok
test_seed_order_is_independent_of_input_order (__main__.FrameTests.test_seed_order_is_independent_of_input_order) ... ok
test_exhausted_503_never_writes_a_zero_frame (__main__.HandoffTests.test_exhausted_503_never_writes_a_zero_frame) ... ok
test_incomplete_fetch_writes_audit_only_in_memory (__main__.HandoffTests.test_incomplete_fetch_writes_audit_only_in_memory) ... ok
test_missing_release_stops_before_network (__main__.HandoffTests.test_missing_release_stops_before_network) ... ok
test_mixed_cli_modes_are_rejected (__main__.HandoffTests.test_mixed_cli_modes_are_rejected) ... ok
test_novelty_failure_is_recorded_and_nonzero (__main__.HandoffTests.test_novelty_failure_is_recorded_and_nonzero) ... ok
test_novelty_missing_release_stops_before_network (__main__.HandoffTests.test_novelty_missing_release_stops_before_network) ... ok
test_novelty_mode_does_not_build_a_frame (__main__.HandoffTests.test_novelty_mode_does_not_build_a_frame) ... ok
test_novelty_output_guards (__main__.HandoffTests.test_novelty_output_guards) ... ok
test_offline_query_display_never_fetches (__main__.HandoffTests.test_offline_query_display_never_fetches) ... ok
test_output_path_cannot_escape_out (__main__.HandoffTests.test_output_path_cannot_escape_out) ... ok
test_prior_frame_or_audit_not_overwritten (__main__.HandoffTests.test_prior_frame_or_audit_not_overwritten) ... ok
test_success_emits_unscreened_frame_and_hash_in_memory (__main__.HandoffTests.test_success_emits_unscreened_frame_and_hash_in_memory) ... ok
test_synthetic_release_hash_guard (__main__.HandoffTests.test_synthetic_release_hash_guard) ... ok
test_verified_empty_discovery_is_distinct_from_failure (__main__.HandoffTests.test_verified_empty_discovery_is_distinct_from_failure) ... ok
test_9900_can_observe_empty_page_100 (__main__.OpenAlexNoveltyTests.test_9900_can_observe_empty_page_100) ... ok
test_citation_cap_and_exact_cap_do_not_claim_empty_termination (__main__.OpenAlexNoveltyTests.test_citation_cap_and_exact_cap_do_not_claim_empty_termination) ... ok
test_later_failure_preserves_partial_bibliography (__main__.OpenAlexNoveltyTests.test_later_failure_preserves_partial_bibliography) ... ok
test_mismatch_duplicate_and_changing_totals_are_incomplete (__main__.OpenAlexNoveltyTests.test_mismatch_duplicate_and_changing_totals_are_incomplete) ... ok
test_numbered_pages_continue_after_short_page_until_empty (__main__.OpenAlexNoveltyTests.test_numbered_pages_continue_after_short_page_until_empty) ... ok
test_work_id_and_page_validation (__main__.OpenAlexNoveltyTests.test_work_id_and_page_validation) ... ok
test_zero_requires_successful_empty_response (__main__.OpenAlexNoveltyTests.test_zero_requires_successful_empty_response) ... ok
test_changing_count_stops (__main__.PaginationTests.test_changing_count_stops) ... ok
test_discovery_is_epmc_only_and_harvests_every_page (__main__.PaginationTests.test_discovery_is_epmc_only_and_harvests_every_page) ... ok
test_duplicate_source_ids_do_not_satisfy_total (__main__.PaginationTests.test_duplicate_source_ids_do_not_satisfy_total) ... ok
test_empty_intermediate_page_stops (__main__.PaginationTests.test_empty_intermediate_page_stops) ... ok
test_epmc_complete_cursor_walk (__main__.PaginationTests.test_epmc_complete_cursor_walk) ... ok
test_missing_cursor_cannot_certify_partial_frame (__main__.PaginationTests.test_missing_cursor_cannot_certify_partial_frame) ... ok
test_missing_identity_stops (__main__.PaginationTests.test_missing_identity_stops) ... ok
test_oversized_result_stops (__main__.PaginationTests.test_oversized_result_stops) ... ok
test_partial_pages_retained_in_failed_audit (__main__.PaginationTests.test_partial_pages_retained_in_failed_audit) ... ok
test_repeating_cursor_stops (__main__.PaginationTests.test_repeating_cursor_stops) ... ok
test_true_empty_query_completes (__main__.PaginationTests.test_true_empty_query_completes) ... ok
test_unexpected_schema_and_invalid_count_stop (__main__.PaginationTests.test_unexpected_schema_and_invalid_count_stop) ... ok
test_printed_discovery_url_matches_script_and_excludes_openalex_search (__main__.PreservedSpecificationTests.test_printed_discovery_url_matches_script_and_excludes_openalex_search) ... ok
test_selection_gates_and_rules_unchanged (__main__.PreservedSpecificationTests.test_selection_gates_and_rules_unchanged) ... ok
test_5xx_retries_are_bounded (__main__.RetryTests.test_5xx_retries_are_bounded) ... ok
test_auth_bot_rate_limit_and_other_4xx_never_retry (__main__.RetryTests.test_auth_bot_rate_limit_and_other_4xx_never_retry) ... ok
test_epmc_503_recovers_same_url_and_logs_each_attempt (__main__.RetryTests.test_epmc_503_recovers_same_url_and_logs_each_attempt) ... ok
test_later_cursor_page_retries_without_duplicating_first_page (__main__.RetryTests.test_later_cursor_page_retries_without_duplicating_first_page) ... ok
test_non_json_schema_and_transport_failures_never_retry (__main__.RetryTests.test_non_json_schema_and_transport_failures_never_retry) ... ok
test_openalex_5xx_does_not_gain_epmc_retry_policy (__main__.RetryTests.test_openalex_5xx_does_not_gain_epmc_retry_policy) ... ok

----------------------------------------------------------------------
Ran 51 tests in 0.089s

OK
~~~

## Files to freeze (SHA-256 of current local bytes)

- PREREG_P04_screen.md: 7681079c5ad884f301f1403a60d68109477978754c44dbac3b6df2e27c02c3a9
- screen_P04.py: 38edd6e943daf2f5bc7dfb1eb12ccf719bfdd34e3056baa5e344c1a146e846d7
- synthetic_test_screen_P04.py: 32bf6613e6903d98f4c5a258612ba9f3d4e03a53333760ea2558423b0de0521e
- BLOCKERS_P04_screen.md: 4c735ee4dffa08f9eb254284050ca480467649d887bf446345dfc48cf6318b45
