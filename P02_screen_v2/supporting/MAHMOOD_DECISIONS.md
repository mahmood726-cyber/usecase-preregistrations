# Binding decisions from Mahmood (relayed 2026-10-28)

1. The list of 7 primaries and fallbacks in USECASES_SINGLE_PROGRESS.md is approved.
2. Downloading open-access supplements is approved for screening and checking only. Nothing is transcribed before the release.
   - Bot-blocked files (the Ayesh Wiley supinfo, the Li CDC PDF and the Veltkamp PMC check) are NOT bypassed. Mahmood fetches them by hand; they are listed in pipeline/MANUAL_DOWNLOADS.md.
   - If a fallback can be completed without a blocked file, proceed by the fallback route and note it.
3. Europe PMC and OpenAlex replace Google Scholar for the novelty check. Record this in each pre-registration as a deviation from the protocol. The reason is that Google Scholar showed a bot check ("unusual traffic") on 2026-10-28, and it was not bypassed.
4. Human verification: humans check headline rows, a seeded 5% of the other rows (at least 1), and only the fields still disputed after a third-model adjudication plus a fourth AI re-check (agy, different family). If the sample error is over 2%: a full AI re-extraction plus a human re-check of the headline rows. Packets are about 30 minutes or less; at most one per person per week across all papers (COAUTHOR_LOAD.md); Mahmood is in the rota; a packet not returned in 7 days is reassigned.
5. Each paper is released separately, as soon as its blockers clear. Extraction starts only after that paper's GitHub release exists.
6. No "first" claims; never change the original numbers; a row from MA X is used only for X; no author contact; no paywall workarounds.

## Decisions of 2026-10-28 evening (Mahmood: "as you suggest")
7. **Unstated software or package (F3).** When the original paper names no statistical package, the prereg fixes ONE configuration in advance: metafor with REML τ² and z-based CIs, plus the transformation the paper states, if any. The stop rule applies if the reproduction gate fails: primary, then the independently cleared fallback, then stop. No model search. This applies to P08 and P13.
8. **P02.** Pre-register the screening of the next 5 candidates under the same rules (published features only; seeded, pre-registered order), then run it.
9. **P15.** Pre-register a deterministic scale-check rule. After release, recompute Eq. (3) from the printed group sizes and d for every row:
   - if the printed `se` matches the square-root form, it is an SE and vi = se²;
   - if it matches the squared form, it is a variance and vi = se;
   - if the rows are mixed, or n is missing, stop.
10. **P11 non-analytic text fields.** The 34 fields still unresolved after the fourth pass go through a logged span-precedence rule, not to co-authors. This is recorded as a deviation.
11. **Zenodo** is enabled for all repos. P11 and P12 are re-released under new tags from the same frozen commits, so that Zenodo mints DOIs. P12 extraction starts only after its DOI exists and extraction_gate.py says ALLOWED.
12. **P04 source route,** in order:
    - (a) an open-access copy via Unpaywall/OpenAlex (PMC or Europe PMC author manuscript, institutional repository, preprint, or the authors' own repository);
    - (b) trial-level HbA1c inputs printed in the main text, so the supplement is not needed;
    - (c) otherwise, screen new P04 candidates (diabetes NMA, open access, per-study data printed) under the same rules, with a pre-registered selection order.

    No bot-check bypass at any step.
14. **P04 (Mahmood, 2026-10-28 evening: "leave Wiley in that case and use the other way you suggested").**
    - Ayesh et al. 2024 (doi:10.1111/dom.15725) is DROPPED ENTIRELY because its source was inaccessible. The supplement is bot-blocked at Wiley, no open-access copy exists, and the Wiley route is not pursued. **This was decided before any data were seen.**
    - Chen 2023 also stays excluded (NOT FEASIBLE).
    - Go straight to route (c): screen new P04 candidates. They must be diabetes network meta-analyses, open access, with per-study data printed, and k ≥ 5, under the same rules.
    - The selection order is pre-registered before screening. Choose the strongest candidate by the protocol's criteria, and name the runner-up as the fallback.
13. **APP-F1 (P11).** Option A: the registered workflow's exact k and row-identity check counts as rejecting silent inventory loss, so P11 proceeds. Fixing the app in allmeta is a separate task.
