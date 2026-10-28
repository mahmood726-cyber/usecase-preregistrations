# P08 v4 verification implementation and kit audit

This supplements prereg section 4 without changing MAHMOOD_DECISIONS item 4. It is incorporated at freeze. Actual extraction, kit execution and packet allocation remain post-release work.

## Identity, independence and sampling

The row key is compact UTF-8 JSON serialization of [DOI, figure, one-based source-order position, exact printed study label], preserving Unicode with no whitespace between elements. Source order is panels top-to-bottom, then rows top-to-bottom. Do not renumber after exclusions. Retain the independently sourced cohort/arm/assessment mapping; a unique row key is not evidence of independence.

Primary reproduction preserves separate HR and OR panel membership. Primary regression uses one estimate per independent cohort, HR preferred; source-unresolved same-type ties fail, without averaging/reconstructing effects. Record raw fields and derivations separately. Setting unknown is missing; known cardiovascular-surgery category is 1, other known categories 0. All overlapping/shared-control ambiguities require source resolution. No reconstruction from arm counts.

Compute headline membership from the union of every prereg trigger. Target SE is the full-fit adjusted-D SE for primary and duration SE for fallback. Use full/reduced primary fitted weights, with ≥10% in either sufficient. Use all D and S extrema ties; **every primary row is a binary S extremum**. An empty nonspecial pool has no sample/error rate; never invent a denominator. For fallback retain all duration extrema ties.

Sign means negative/zero/positive; zero is distinct. CI exclusion is strict lower>0 or upper<0; touching zero does not exclude it. Delete one row, refit the same fixed models/variance rules without reapplying original k/category gates, and compare target slope, CI exclusion and section 7 class. Full-fit SE remains the reference. A fitting failure/nonfinite result marks that row for human checking.

Order non-headline rows by lowercase SHA-256 of UTF-8 `2026102808|P08|<row key>`, then key; take max(1,ceil(0.05*n)) when n>0. Preserve membership by verification round. Any source mismatch in a required field or identity/outcome mapping makes the sampled row erroneous. >2% row error triggers both independent AI extractions again, third/fourth passes, and human headline re-check. It does not trigger a blanket human audit. Still-disputed fields, including excluded-row/publication/mapping fields, still go to humans.

The initial two AI passes are mutually blinded. Record exact model identifiers and families: agy differs from Codex; the fourth agy pass differs from the adjudicator. Do not substitute model names inferred from task labels. Humans check headline rows, the seeded sample and only still-disputed fields after both adjudication passes.

## Log and packet contract

The release kit's VERIFICATION_LOG.csv must support paper, candidate DOI, round, immutable row key, source/file/panel location, field, both extraction values, third-model decision, fourth-model check, unresolved flag, headline reasons, sample membership, human decision/correction, initials/date and packet ID. Preserve model identity logs, excluded-row disputes, denominator and escalation history.

At most five rows per packet, five minutes setup plus five minutes per row; split further when actual image/mapping complexity exceeds 30 minutes. All-primary-row verification can require many packets; do not cap the human scope to save time. Schedule without promising completion in a week.

Eligible P08 rota: MA, SMA, QFH, HK, AW. Check the shared cross-paper COAUTHOR_LOAD ledger before assignment; reserve a planned row before sending, at most one packet per ISO week per person. Mahmood participates under the same cap. Reassign after seven days to the next eligible person, log it, never skip. No ledger assignment or message was sent in V4.

## Replacement for the missing earlier KIT check

The sibling A_P08_KIT/out files are present but are historical inputs, not an aligned or validated v4 kit. Their hashes are retained in FILE_HASHES_P08.json. Static inspection found:

- Primary codebook requires identification of original pooling details without defaults. Replace that execution instruction with v4's single natural-scale REML/z configuration. Keep “NOT STATED” in source-reporting fields; never fill them with our assumed settings.
- Fallback codebook requires confirming a fixed-effect forest label and FE reproduction. Replace those instructions with Figure 4A's random-effects label, DL/z reproduction and the strict 0.005 gate.
- Keep the existing explicit treatment-duration/assessment distinction, months-as-printed rule, independence gates and all-ten-study requirement.
- Headline helper's full/reduced weight union, binary extrema/all ties, immutable keys, hash seed and deletion mechanics are preserved.
- Schemas/prompts/log must separate reported source methods from prespecified reproduction assumptions; no raw values are fabricated to satisfy a schema.

Before any extraction, make a release-aligned copy and validate it on marked synthetic fixtures: wrong/unknown labels; missing duration; overlap/ties; invalid CI/variance; extrema ties including binary S; exact 10% and 0.5-SE boundaries; CI touching zero; all-headline/empty sample; seeded sampling; exactly 2% versus >2% error; excluded-row unresolved fields; packet caps and seven-day reassignment. The absent earlier synthetic_kit_checks.py is not a v4 pass. The synchronization and runtime validation are mandatory post-release, pre-analysis conditions under FREEZE_CRITERIA, not failures of F1–F6.
