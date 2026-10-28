# Two-reviewer screening check: adjudication log

Reviewers: Codex (gpt-6-astra, OpenAI) = primary screener; agy (Gemini 3.x Pro via agentapi driver, Google) =
second reviewer. agy was blind to Codex's answers and saw the same rules and source text. Samples were
pre-specified in `agy_review.py`: seeded SHA-256 order of `<seed>|<pilot>|agycheck|<key>`, fixed at first
draw in `<pilot>/agy/sample.json`. Full-text agreement is judged at the text level: the same `decide.py`
applied to each reviewer's facts, with "passes all text criteria" (PENDING_D or ELIGIBLE) counted as one
category. Stage D (the forest-plot image check) was single-reviewer (Codex).
The adjudicator is the coordinating Claude session (Anthropic, a third family). It checked only the
disputed eligibility fact against the source and never recorded or used results.

## Harness defects found during the check (fixed before scoring)
- agy driver returns at the first quiet gap between tool calls, so 6/11 full-text answers came back with no
  JSON. Fix: keep tailing the conversation, with up to two in-conversation "reply with the JSON" nudges.
- **Wrong-document answer:** agy's answer for P06 rank 191 (ICI haematological AEs) described a different
  paper (acupuncture/pain intensity, k=11) and was identical to its rank-525 answer. Fix: agy must echo the
  paper TITLE; answers whose title does not match `record.json` are discarded. All earlier agy full-text
  answers were re-run under this guard (old outputs kept as `agy_ft_attempt*_*.jsonl`, not scored).

## Adjudicated disagreements
| Pilot | Rank | Stage | Codex | agy | Source check | Adjudicated | Final status changed? |
|---|---|---|---|---|---|---|---|
| P06 | 458 | Title/abstract | FULLTEXT | EXCLUDE K_LT_10 | Abstract: "11 studies ... (3 RCTs and 8 NRCTs)" | agy correct under the TA rule (fewer than 10 RCTs stated) | No: excluded at full text for DESIGN (mixed RCT/NRCT) either way |

## Wrong-document audit of the primary screener (Codex)
Each Codex full-text answer's designated-outcome words were checked against its own `paper.txt`. 498 records were checked (P14 259, P06 239), and each has the outcome tokens in its own paper. The only low-overlap cases are 3 P14 records (ranks 379, 544, 669) whose outcome field reads "not determinable", meaning there is no outcome text to match. No Codex wrong-document answer was found. Each Codex run is a fresh process confined to one record folder.
| P06 | 401 | Title/abstract | FULLTEXT | EXCLUDE DESIGN | Abstract states "21 studies" and that "further randomized controlled trials ... are required"; design not stated explicitly | Codex correct under the TA rule (exclude only when explicit); full text confirmed nonrandomized | No: excluded at full text for DESIGN |
| P06 | 571 | Title/abstract | EXCLUDE DESIGN | FULLTEXT | Title/abstract: PFS as a surrogate for OS, correlated across 26 RCTs | Codex correct: surrogacy analyses are excluded by the draft | No |

## P06 results (sample fixed in `P06/agy/sample.json`)
- **Full text:** 11 sampled. agy produced a title-verified answer for 10 (rank 401: none after retries and transcript harvest). **10/10 agree** at the text-level category. Where both gave k (9 pairs), the trial counts are identical. Rank 55: both exclude, with different first-failing reasons (Codex DESIGN, agy K_OUT_OF_RANGE).
- **Title/abstract:** 50 sampled, 50 answered, **47/50 agree**. The 3 disagreements were adjudicated above. In no case did the final disposition change.
- Late agy answers were recovered by `agy_harvest.py`. It attributes a conversation only by the working directory named in its own first prompt, and keeps only title-verified answers.

## P14 adjudicated disagreements
| Pilot | Rank | Stage | Codex | agy | Source check | Adjudicated | Final status changed? |
|---|---|---|---|---|---|---|---|
| P14 | 994 | Full text | EXCLUDE CHRONOLOGY (earliest year "not determinable") | passes text (years 2000-2018) | Table 1: 26 included studies dated 2000-2018; the designated synthesis has 22, so at least one is from 2011 or earlier and at least one from 2016 or later | agy correct: the 5-year span is established by bounds | **Yes**: no longer excluded for chronology; proceeds to stage D (model label) |
| P14 | 679 | Full text | EXCLUDE CHRONOLOGY (earliest year "not determinable") | passes text (years 1997-2016) | Table 1: trials 1972-2016 | agy correct | **Yes**: proceeds to stage D (model choice was heterogeneity-conditional) |
| P14 | 249 | Title/abstract | FULLTEXT | EXCLUDE DESIGN | Abstract: case-control/cohort dietary exposures, randomized trials mentioned | Either acceptable (Codex chose FULLTEXT when in doubt) | No: excluded at full text for DESIGN |
| P14 | 280 | Title/abstract | EXCLUDE DESIGN | FULLTEXT | Abstract: RCTs plus non-randomized studies; pooled single-drug egg-reduction/cure rates | Codex correct: single-arm/proportion and mixed-design synthesis | No |
| P14 | 793 | Title/abstract | FULLTEXT | EXCLUDE POPULATION | Abstract: before-after and controlled studies; ages to be checked | Either acceptable | No: excluded at full text for DESIGN |
| P14 | 1162 | Title/abstract | FULLTEXT | EXCLUDE POPULATION | Abstract: children and adults, primary outcome synthesized by age group | agy's reading is defensible; Codex's referral is allowed by "when in doubt" | No: excluded at full text for POPULATION |

**Systematic defect found by the check and fixed:** Codex recorded trial years as "not determinable" when it could not map trials to the forest plot. That turned 8 of 9 P14 CHRONOLOGY exclusions into possible false negatives (ranks 101, 615, 679, 754, 805, 994, 1061, 1064). Fix: stage C2 (`RULES_C2.md`). Where the C screen left years missing, Codex lists the report years from the included-studies table. `screen.c2_span` then decides deterministically: individual years if the trials can be mapped; otherwise the span is established only if every window of k_designated consecutive sorted years spans at least 5. This is a screening-procedure correction, not a rule change: the draft's chronology rule still applies in full at extraction.

## P14 results (sample fixed in `P14/agy/sample.json`)
- **Full text:** 8 sampled; agy title-verified answers for all 8 (4 harvested from transcripts). **6/8 agree** at the text level. The 2 disagreements (994, 679) were adjudicated in agy's favour and traced to the systematic defect above. Trial counts were identical in every pair where both gave k.
- **Title/abstract:** 50 sampled, 50 answered, **46/50 agree**. In none of the 4 disagreements did the final disposition change.
