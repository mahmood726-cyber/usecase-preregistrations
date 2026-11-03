# Field-specific use case: protocol (approved by Mahmood, 27 Oct 2026)

Purpose: each software paper gets one extra use case drawn from the target journal's own field. It re-analyses a published, open-access meta-analysis with the app's method to show something the original did not report. The existing use case is kept.

## What makes a use case powerful (Mahmood, 27 Oct): select for impact before running, never after
Choose a candidate whose *published features* (visible in the original paper before we run anything) make the method likely to say something that matters:
- **High profile:** widely cited, guideline-cited, or published in the target journal itself.
- **Live question:** a known controversy, a practice-changing claim, or ongoing trials.
- **Method-question fit,** judged from what the original paper reported:
  - Cumulative (P14): many trials spread over years, with trials still being run. Headline type: "the evidence was conclusive by year X, yet N more trials with M participants followed" (research waste).
  - GOSH and influence (P11, P13): high reported I², or a conclusion resting on a few trials. Headline type: "the pooled effect depends on trial Z".
  - Publication bias and limit meta-analysis (P06, P12): many small trials with a wide spread in SE. Headline type: "the adjusted effect is much smaller or null".
  - Dose-response (P02): a published linear-only analysis of an exposure where a threshold is plausible. Headline type: "the benefit plateaus above dose D".
  - NMA (P04): drugs never compared head-to-head. Headline type: "an indirect comparison not previously reported".
  - Meta-regression and RVE (P08, P15): a clinically important moderator that was reported but not modelled (eGFR, dose, age). Headline type: "the effect varies with X".
- **Effort cap:** one meta-analysis per paper; data from the forest plot, a table or the supplement only; k ≤ 60; no contacting authors; about half a day of Codex time. Screen up to 5 candidates on these criteria, then pick the strongest.
- **Honesty:** selection uses only the original paper's published features. The analysis is pre-registered (GitHub release plus Zenodo DOI) before we run it. Whatever result comes out is reported; "robust" counts as a valid outcome. No outcome switching.
- **Write it to be publishable:** one clear clinical sentence as the headline, a figure that shows it at a glance, and an explicit statement of what it adds to the original. Keep it to ≤250 words, or Extended data where limits require.

## Multi-meta-analysis mode (Mahmood, 27 Oct): pilot on P14 and P06
Instead of a single example, apply the paper's method to 10–30 published meta-analyses in the journal's field and report one field-level finding.
- **Sampling frame, pre-specified (no hand-picking):**
  - Example: "all open-access meta-analyses of RCTs in paediatrics, published 2015–2025 in [journal list], with ≥5 trials spread over ≥5 years and per-study data in the forest plot or supplement".
  - The search string, date and inclusion rules all go in the pre-registration.
  - Take every eligible meta-analysis up to a cap of 30, in a random order set by a seed that is pre-registered.
- **Questions:**
  - P14 cumulative: in how many meta-analyses did the cumulative estimate become, and stay, conclusive before the final trial? How many trials and participants came after that point? Define the conclusiveness rule in advance (e.g. 95% CI excludes the null and stays excluded, at the meta-analysis's own model).
  - P06 publication bias: in how many oncology meta-analyses does the significance or direction change after small-study adjustment? Pre-specify the methods, e.g. limit meta-analysis or PET-PEESE, with Egger as a secondary test.
- **Data:**
  - Reuse harness-store trial data only where it matches that meta-analysis's own included trials and is checked against its forest plot.
  - Everything else is double-extracted from the forest plot.
  - Gate: reproduce each meta-analysis's own pooled estimate. Meta-analyses that fail the gate are excluded, and the exclusion is reported.
  - Rule: a row taken from meta-analysis X is used only to analyse X.
- **Output:** one summary figure plus 150–250 words, with every individual result listed in Extended data and the archive.
- **Honesty:** report the result whatever it is (for example "3 of 20"). Frame it as a meta-research finding. Make no clinical recommendations.

## Reproducibility-audit mode (Mahmood, 27 Oct): drawn from pipeline\ERROR_WORK_CATALOGUE.md
Each candidate use case can also be a reproducibility audit:
1. Reproduce the published estimate exactly, using the published inputs.
2. Show the app's check that detects the problem: clustering, overlap or multi-arm detection, unit plausibility, consistency, or influence.
3. Report the corrected estimate.

Shortlist:
- P15: shared-control and nested-subgroup clustering (Yu, error confirmed by the authors; Fu).
- P04: duplicated-trial overlap in heart-failure and finerenone NMAs.
- P16: consistency checks across 10–30 published NMA league tables (multi-MA).
- P11/P13: influential rows traced to extraction errors.
- P02: dose-unit plausibility screen.
- P14: equivalence band.

Naming rules:
- Name a publication only if its authors were contacted AND either replied, or 14+ days passed with no reply. Otherwise describe it anonymously.
- Include a line: "the authors were notified separately on [date]".
- Use neutral wording: report the discrepancy, not misconduct.
- Fu: report the reproduction only, never the retraction request.
- Re-check every case's status before submission.

## Steps (Codex does the work; Claude coordinates)
1. **Candidate search.**
   - Look for recent (≤10 years), open-access (CC-BY or similar) meta-analyses in the journal's field, ideally published in the target journal itself.
   - Per-study data must be extractable from the forest plot, a table or the supplement.
   - Need k ≥ 10 for GOSH, cumulative, publication-bias and meta-regression analyses; k ≥ 5 is acceptable for others.
   - List 3 candidates with the reason each fits.
2. **Novelty check.** Search PubMed and Google Scholar for an existing re-analysis that uses this method on this meta-analysis. Drop the candidate if one exists.
3. **Pre-registration (before any run).** Write PREREG_Pnn_usecase.md giving the chosen meta-analysis (DOI), the outcome, the exact analysis, and what would count as "new" versus "robust". Commit it, and record its sha256 and time. **Timestamp method (Mahmood, 27 Oct):** push it to a public GitHub repo (mahmood726-cyber/usecase-preregistrations, one folder per paper) and create a GitHub *release* tag for it. Git commit dates can be set locally, so they don't prove time; the release's server-side timestamp does. Zenodo's GitHub integration then archives the release with a DOI, which gives an independent, immutable timestamp to cite in the paper. No data extraction or analysis may start before that release exists.
4. **Extraction.**
   - Two independent extractions: Codex, and agy's Claude or Gemini.
   - An adjudicator resolves differences against the source PDF.
   - Gate: reproduce the paper's own pooled estimate within rounding before any new analysis. If it fails, stop and report.
5. **Analysis.** Run in the app and in R (same package as the paper's validation). Report both and confirm they agree.
6. **Write-up.**
   - 150–250 words plus one figure panel, or Extended data where the journal limits words or figures.
   - Frame it as "a re-analysis illustrating …". No clinical recommendations. Cite the original meta-analysis.
   - If nothing new emerges, report it as "conclusion robust to …".
   - Mahmood dictates the final paragraph from a draft.
7. **Archive.** Deposit the extraction, the pre-registration and the scripts in the paper's archive (new version) so every number traces.

## Rules
- Never change the original paper's numbers.
- No "first" or ranking claims.
- Every number must trace to the extraction or the R output.
- A row taken from meta-analysis X is used only to re-analyse X.

## Pilot
P14 (cumulative, Eur J Pediatrics) and P13 (GOSH, Rheumatology Advances in Practice). Then P04 (diabetes NMA), P06 (oncology publication bias) and P08 (nephrology meta-regression).
