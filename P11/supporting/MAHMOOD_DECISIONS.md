# Binding decisions from Mahmood (relayed 2026-10-28)

1. The list of 7 primaries and fallbacks in USECASES_SINGLE_PROGRESS.md is approved.
2. Downloading open-access supplements is approved for screening and checking only. Nothing is transcribed before the release.
   - Bot-blocked files (the Ayesh Wiley supinfo, the Li CDC PDF and the Veltkamp PMC check) are NOT bypassed. Mahmood fetches them by hand; they are listed in pipeline/MANUAL_DOWNLOADS.md.
   - If a fallback can be completed without a blocked file, proceed by the fallback route and note it.
3. Europe PMC and OpenAlex replace Google Scholar for the novelty check. Record this in each pre-registration as a deviation from the protocol. The reason is that Google Scholar showed a bot check ("unusual traffic") on 2026-10-28, and it was not bypassed.
4. Human verification: humans check headline rows, a seeded 5% of the other rows (at least 1), and only the fields still disputed after a third-model adjudication plus a fourth AI re-check (agy, different family). If the sample error is over 2%: a full AI re-extraction plus a human re-check of the headline rows. Packets are about 30 minutes or less; at most one per person per week across all papers (COAUTHOR_LOAD.md); Mahmood is in the rota; a packet not returned in 7 days is reassigned.
5. Each paper is released separately, as soon as its blockers clear. Extraction starts only after that paper's GitHub release exists.
6. No "first" claims; never change the original numbers; a row from MA X is used only for X; no author contact; no paywall workarounds.
