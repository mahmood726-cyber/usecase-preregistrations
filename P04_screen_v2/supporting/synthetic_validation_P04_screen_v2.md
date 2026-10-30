SYNTHETIC - not data

# Offline P04 v2 draft software validation

Invented bibliographic fixtures only. No candidate was fetched, screened, ranked or scored; no network call was made. This is not a clinical result or release certification. Fixtures ran in memory; outputs are confined to out/.

~~~text
test_bounded_5xx_and_no_auth_retry (__main__.Tests.test_bounded_5xx_and_no_auth_retry) ... ok
test_citations_require_empty_terminal_page (__main__.Tests.test_citations_require_empty_terminal_page) ... ok
test_complete_pages_and_true_zero (__main__.Tests.test_complete_pages_and_true_zero) ... ok
test_continuation_preserves_original_order_and_rejects_wrong_bytes (__main__.Tests.test_continuation_preserves_original_order_and_rejects_wrong_bytes) ... ok
test_draft_stops_before_network_and_outputs (__main__.Tests.test_draft_stops_before_network_and_outputs) ... ok
test_exact_ten_thousand_without_terminal_empty_is_incomplete (__main__.Tests.test_exact_ten_thousand_without_terminal_empty_is_incomplete) ... ok
test_final_copy_is_option_A_and_stops_without_release (__main__.Tests.test_final_copy_is_option_A_and_stops_without_release) ... ok
test_incomplete_duplicate_and_changed_count_rejected (__main__.Tests.test_incomplete_duplicate_and_changed_count_rejected) ... ok
test_new_seed_order_dedup_and_exclusions (__main__.Tests.test_new_seed_order_dedup_and_exclusions) ... ok
test_normalization_and_date_boundaries (__main__.Tests.test_normalization_and_date_boundaries) ... ok
test_output_path_cannot_escape_out (__main__.Tests.test_output_path_cannot_escape_out) ... ok
test_v1_release_cannot_activate_v2 (__main__.Tests.test_v1_release_cannot_activate_v2) ... ok

----------------------------------------------------------------------
Ran 12 tests in 0.075s

OK
~~~

Live API availability, remote release existence, actual candidate feasibility and app/R runtime parity remain untested.

## Finalization checks (2026-10-30; Option A approved)

Re-run on the finalized bytes: 12 tests, 0 failures, 0 errors (11 draft tests plus one new lock test). The draft-lock test now patches `DRAFT=True` and `APPROVED_OPTION=None` explicitly and still requires a stop before network/output; a new test requires `DRAFT=False`, `APPROVED_OPTION="A"`, the v1 seed 2026102804, and a stop before network, output or frame construction when release arguments are absent. A planted defect (`APPROVED_OPTION="B"`) made the suite fail.

Offline metadata check of the archived v1 frame (no network, nothing screened): `continuation_frame` on `frame_P04.jsonl` (561 rows, SHA-256 fef70caf...3063f) retains 540 rows starting at original rank 22 and excludes the 21 triaged DOIs. All 556 Appendix B entries and the 21 Appendix A exclusions are unchanged from the draft, which checked them against the archive. The five v1 FREEZE.json digests in Appendix C are unchanged.
