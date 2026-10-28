# Stage D — per-study source check (forest plot image or supplement)

`target.json` names the review's designated synthesis (outcome, comparison, time point) and where the
full-text screen said its per-study data are (`per_study_location`). Attached images are the review's
figures named there (or all figures if none matched); `supp/` may hold supplementary files.

**Do not record any number from the plot or supplement** (no estimates, CIs, weights, counts, p, I², and
no pooled result or its direction). Do not let any result influence your answers. Only record:
- `source_found`: yes if you can see the per-study display for the designated synthesis (the right
  outcome/comparison), else no.
- `per_study_printed`: yes if every trial row prints its estimate with a 95% CI (or SE), or arm-level
  numbers sufficient to compute it, as legible numbers; no if only graphical markers/bars; unclear if illegible.
- `trial_rows`: number of independent trial rows contributing to the designated pooled result (count
  rows, do not read their values; a trial appearing twice counts once — then say so in note). null if not countable.
- `plot_model_label`: the model label as printed (e.g. "IV, Random, 95% CI", "M-H, Fixed"), or "" if none.
- `plot_weighting`: inverse_variance / mantel_haenszel / peto / unstated, from that label only.
- `plot_fixed_random`: fixed / random / unstated, from that label only.
- `note`: ≤40 words (which figure/file you used; any problem).
