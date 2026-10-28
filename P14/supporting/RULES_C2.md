# Stage C2 (P14 only) — chronology check when the full-text screen could not map trial years

`paper.txt` is the review; `target.json` gives the designated synthesis and its number of trials
(`k_designated`). Do not record any effect, CI, count or result.

Question: is it ESTABLISHED that the report years of the trials in the designated synthesis span at
least 5 years (latest minus earliest >= 5)?

1. If the designated synthesis' trials can be identified individually (forest-plot caption, results
   text, a table marking which studies contribute), list their report years and compute min/max.
2. Otherwise use the review's included-studies table or reference list: list the report year of every
   included trial (n_review trials). The span is established only if EVERY possible subset of
   k_designated of those trials spans >= 5 years. Equivalently: sort the years; for every window of
   k_designated consecutive years in the sorted list, last − first >= 5.
   Report the conservative bounds: earliest possible maximum and latest possible minimum.
3. If report years for the review's trials are not printed anywhere, answer `undeterminable`.

Return: `method` (individual / bound / undeterminable), `years` (the list you used), `n_review`,
`k_designated`, `span_established` (yes / no / undeterminable), `years_min`, `years_max` (for method
individual: the actual min/max; for method bound: the conservative pair that proves the span, or null),
`basis` (≤40 words, naming the table or section).
