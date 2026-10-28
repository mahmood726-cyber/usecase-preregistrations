# Rules for every wave-A job (read first)

Stage: **pre-release**. The pre-registration is not yet frozen or released, so:
- **No extraction:** do not transcribe, copy or paraphrase any per-study row (study-level effects, counts, CIs, doses, moderators) from any source. Published *pooled* results, k and model statements may be read and quoted exactly as printed.
- **No analysis of real data.** Code may be run only on SYNTHETIC fixtures you generate. Name them `synthetic_*`, mark them "SYNTHETIC - not data" in the first line or column, and never present their output as a result.
- No author contact, no login, no paywall workaround, no bypassing bot checks. If a page is blocked, record "blocked" and move on.
- Never change any number from the original papers. No "first", "novel" or ranking claims. Never name any publication as containing an error.

Environment:
- Read files with python only. Powershell, node, git and Rscript will not start inside this sandbox. Use python to run code.
- You may create files only under `./out/`. Do not modify anything else.
- The pinned app snapshot is at `ALLMETA` (path in `JOB.md`): allmeta commit 14dc545bcba87a02158b2f445c28450e7eaf6b89, app folders plus `shared/`.
- R 4.6.0 is available to pc2 only, not to you. Write R scripts that pc2 will run. Package versions: metafor 5.2.1, meta 8.5.0, metasens 1.5.3, dosresmeta 2.2.0, netmeta 3.7.0, clubSandwich 0.7.0, robumeta 2.1.

Your final message: a short summary (at most 200 words) listing each file you wrote under `./out/`, plus every open problem.
