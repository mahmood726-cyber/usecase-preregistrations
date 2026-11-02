SYNTHETIC - not data

# Offline P04-screen-v3 software validation (approved for freeze; not yet released)

Invented bibliographic fixtures only. No candidate was fetched, screened, ranked or scored; no network call was made. This is not a clinical result or a release certification.

~~~text
test_check_release (__main__.Locks.test_check_release) ... ok
test_draft_flag_still_locks (__main__.Locks.test_draft_flag_still_locks) ... ok
test_dry_build_cannot_write_into_package_or_overwrite (__main__.Locks.test_dry_build_cannot_write_into_package_or_overwrite) ... ok
test_final_copy_stops_before_reading_without_release (__main__.Locks.test_final_copy_stops_before_reading_without_release) ... ok
test_frozen_numbers_and_exclusion_composition (__main__.Locks.test_frozen_numbers_and_exclusion_composition) ... ok
test_release_build_end_to_end_and_no_overwrite (__main__.Locks.test_release_build_end_to_end_and_no_overwrite) ... ok
test_annotated_or_reordered_v2_rejected (__main__.Queue.test_annotated_or_reordered_v2_rejected) ... ok
test_prior_disposition_in_tail_is_excluded (__main__.Queue.test_prior_disposition_in_tail_is_excluded) ... ok
test_queue_starts_after_v2_visits_and_preserves_order (__main__.Queue.test_queue_starts_after_v2_visits_and_preserves_order) ... ok
test_v2_frame_must_be_exact_continuation_of_v1 (__main__.Queue.test_v2_frame_must_be_exact_continuation_of_v1) ... ok
test_wrong_bytes_rejected (__main__.Queue.test_wrong_bytes_rejected) ... ok
test_derivative_and_duplicate_rules_in_build (__main__.Rules.test_derivative_and_duplicate_rules_in_build) ... ok
test_design_rule_independent_trials (__main__.Rules.test_design_rule_independent_trials) ... ok
test_drug_node_scope (__main__.Rules.test_drug_node_scope) ... ok
test_effort_formula (__main__.Rules.test_effort_formula) ... ok
test_k_rules (__main__.Rules.test_k_rules) ... ok
test_licence_list_is_exact (__main__.Rules.test_licence_list_is_exact) ... ok
test_non_original_title_markers (__main__.Rules.test_non_original_title_markers) ... ok
test_outcome_lock_rules (__main__.Rules.test_outcome_lock_rules) ... ok
test_preprints_excluded_by_prefix_or_source (__main__.Rules.test_preprints_excluded_by_prefix_or_source) ... ok
test_retraction_urls_are_fixed (__main__.Rules.test_retraction_urls_are_fixed) ... ok
test_retraction_verdicts (__main__.Rules.test_retraction_verdicts) ... ok
test_target_choice (__main__.Rules.test_target_choice) ... ok
test_exhaustion_allows_short_log (__main__.Stages.test_exhaustion_allows_short_log) ... ok
test_selection_tiebreaks (__main__.Stages.test_selection_tiebreaks) ... ok
test_stage_f_violations (__main__.Stages.test_stage_f_violations) ... ok
test_stage_s_queue_is_first_five_passers_in_order (__main__.Stages.test_stage_s_queue_is_first_five_passers_in_order) ... ok
test_stage_s_validation_and_selection (__main__.Stages.test_stage_s_validation_and_selection) ... ok
test_valid_stage_f_log (__main__.Stages.test_valid_stage_f_log) ... ok
test_methods_by_title_and_missing_methods (__main__.StageFSections.test_methods_by_title_and_missing_methods) ... ok
test_only_headers_methods_and_licence_survive (__main__.StageFSections.test_only_headers_methods_and_licence_survive) ... ok

----------------------------------------------------------------------
Ran 31 tests in 1.548s

OK
~~~

Live API behaviour, remote release existence, real candidate feasibility and app/R parity remain untested.

## Test-first record

- **First draft (2026-11-02).**
  - Against a stub (`DRAFT = True` only): 28 tests, 0 passing, 59 errors (subtests included).
  - Against the implementation: 28/28 pass.
  - Planted defects, each red: Results allowed in Stage F; v2-visited DOIs not excluded; CC BY-NC-SA accepted.
- **Finalization (2026-11-02, dispatch decisions applied).**
  - Tests were changed first: 31 tests, 15 failing (8 failures + 7 errors) before the code changed.
  - After the code changes: 31/31 pass.
  - Planted defects, each red: CC BY-SA accepted (3 failures); N_S = 10 (3 failures); Crossref retractions ignored (1); duplicate groups kept (1); v2 tag accepted as a v3 release (1).
- **Report file.** The suite writes this report only with `--write-report`, so running it on frozen package bytes never changes a package file.
- **Offline dry build** (final script, scratch folder outside the package, no network):
  - declared filter: 535 rows in, 57 distinct rows removed, 478 kept;
  - item counts per rule: protocol 46, comment/reply/letter 4, erratum/correction 2, derivative of an excluded DOI 2, preprint DOI prefix 4, preprint record source 4, exact-title duplicate group 4;
  - queue sha256: 2a88570287edd5f180861075f7c7833bed8017163be75ff22f213c0b8ce6b03f.
