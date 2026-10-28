# P13 v5 evidence and limits

Date: 2026-10-28. Documentary screening only. No study-level rows were extracted, transcribed, assembled or analysed. Original publication files are archived as opaque byte copies, as V5 requires; their contents are not an extracted dataset. All active citations are relative. [Manifest](evidence_manifest_P13.json) records every archived file's SHA-256 and provenance.

## F1: source feasibility

The supplied [v3 source screen](evidence/history/v3_SOURCE_CHECK_P13.md) gives **FEASIBLE-IMAGE** for both candidates. Its historical F3 conclusions are superseded by [JOB.md](evidence/instructions/JOB.md), [decision 7](evidence/instructions/MAHMOOD_DECISIONS.md) and the v5 [reproduction contract](REPRODUCTION_P13.md). The current job independently checked Methods and source-file identity; it does not claim a fresh row-level image extraction.

| Candidate | Archived source and locator | Required printed columns/context |
|---|---|---|
| Primary | [Final Figure 1 image](evidence/primary/supp/rkag034f1.jpg); [final PDF](evidence/primary/rkag034.pdf), page 5 | Study; Total; Number with Dysautonomia; Prevalence % [95% CI]; integer counts and percentage/endpoints |
| Primary | [Final XML](evidence/primary/fulltext.xml), Table rkag034-T1; final PDF page 4 | Identity, assessment and denominator context; Study (author, year), Medical diagnosis, Sample size, n, Method used, Subjective/Objective |
| Primary | [Supplement bundle](evidence/primary/supplementary.zip); [nested final supplement](evidence/primary/supp/rkag034_supplementary_data.zip) | Final supplementary DOCX and PRISMA checklist; inspected in memory |
| Primary | [Accepted supplement](evidence/primary/Supplementary_Materials_ACCEPTED.pdf), PDF page 20<br><br>The authoritative locator here is physical PDF page 20. The historical source screen's additional “internal page 19” label was not independently verified and is not used to identify or extract the figure. Final published Figure 1 remains the primary data source. | Overall Supplementary Figure 2 is corroboration only; final DOCX Figure 2 is subjective-only |
| Fallback | [Final Figure 2 image](evidence/fallback/supp/rkad084f2.jpg); [final XML](evidence/fallback/fulltext.xml) | Study; Fatigued; Total; Proportion; 95%-CI; Weight. Integer counts, two-decimal proportions/endpoints; weights unused |
| Fallback | [Supplement DOCX](evidence/fallback/supp/rkad084_supplementary_data.docx), Tables S1–S2; [bundle](evidence/fallback/supplementary.zip) | Identity/population/fatigue instrument/definition; not replacement counts |

Published targets and k are retained without alteration in the registration. The six logged downloads match the supplied [FETCH_LOG](evidence/FETCH_LOG.json), HTTP 200/OK; no P13 source is recorded blocked. No access restriction was bypassed. Figure readability, image precision and overlap/identity risks remain carried into the independent post-release checks. Source Methods' overlap policies do not certify row independence.

Final forests govern contributions/order/counts; context tables support identity and selected assessments. Never mix final and accepted locators or infer counts from rounded prevalence. All ambiguity, missing fields or unresolved overlap fails that candidate.

Source-specific independence alert: the primary article's Limitations explicitly leave possible cohort overlap unresolved. Its general overlap-exclusion policy does not settle that warning. The registered independence condition must be resolved from the permitted review/supplement sources before the primary reproduction gate. If it remains unresolved, the primary fails eligibility and only the independently cleared, already specified fallback may proceed; otherwise stop. Do not assume independence from different assessment methods, matching pooled results, or legible forest columns. Do not omit or merge contributions.

## F3: source interpretation

[REPRODUCTION_P13.md](REPRODUCTION_P13.md) quotes the exact supporting passages and the RStudio wording considered as potentially contrary evidence. No contrary transformation or package declaration was found. The [source audit](source_screen_P13.json) records search scope and keyword counts, not study data. Absence of a method statement is not evidence of the authors' actual computation. V5 fixes a prospective configuration under the coordinator decision and retains the numerical gate.

## F2: supplied novelty checks and deviation

Europe PMC and OpenAlex substitute for Google Scholar under decision 3. Scholar showed “unusual traffic” on 2026-10-28 and was not bypassed. This is an explicit protocol deviation.

Equivalence means GOSH/all-subsets heterogeneity re-analysis of the same review's registered overall outcome/contributions, regardless of software, estimator, sampling or thresholds. Confirmed equivalence invokes primary → independently cleared fallback → stop; an unresolved potentially equivalent record blocks that candidate.

The exact supplied [Europe PMC/PubMed log](evidence/novelty/NOVELTY_pc2_2026-10-28.json) and [OpenAlex log](evidence/novelty/NOVELTY_openalex_2026-10-28.json) are archived without filtering or rewriting.

| Candidate/index, 2026-10-28 | Supplied record counts | Reported screen |
|---|---|---|
| Primary Europe PMC, PMID 41978692 | cited_by=0; retrieved=0; hitcount=0 | Empty flagged list |
| Primary OpenAlex, W7138950171 | cited_by_count=1; retrieved=1; complete=true; error=null | Empty flagged list |
| Fallback Europe PMC, PMID 37881507 | cited_by=14; retrieved=15; hitcount=15 | Empty flagged list |
| Fallback OpenAlex, W4387524331 | cited_by_count=18; retrieved=18; complete=true; error=null | Empty flagged list |

Do not reconcile 14 with 15 by changing a source number or sum cross-index counts. These supplied screens report no equivalent; this job does not claim an independent record-level rereview.

Supplemental PubMed queries in the supplied log:

- Primary: `(GOSH OR combinatorial OR heterogeneity OR reanalysis OR re-analysis) AND ("The prevalence of dysautonomia in chronic musculoskeletal pa")`; count 1; PMID 33046102.
- Fallback: `(GOSH OR combinatorial OR heterogeneity OR reanalysis OR re-analysis) AND ("Prevalence and factors associated with fatigue in patients w")`; count 2; PMIDs 41571420, 33266287.

Earlier inaccessible searches remain not assessed: `((dysautonomia OR "autonomic dysfunction") AND "musculoskeletal pain") AND (GOSH OR "graphical display of study heterogeneity")` and `(fatigue AND "axial spondyloarthritis") AND (GOSH OR "graphical display of study heterogeneity")`. Citing-request URLs and full record-level screening lists are unavailable. Disclosure satisfies F2's coverage rule; no guarantee about unindexed work is made.

## F6: pinned app functions and actual byte hashes

Declared snapshot: **14dc545bcba87a02158b2f445c28450e7eaf6b89**, from [PIN.txt](evidence/instructions/PIN.txt). The files below match its four core GOSH hashes.

| File | Functions/lines and supported operations | SHA-256 |
|---|---|---|
| [gosh/index.html](evidence/app/gosh/index.html) | parse 186; pool 211; sampledSubsets 245; run 289; applyExact 423; __almGoshValidationRun 609; snapshot/restore 620/625: strict y/SE inputs, DL fits, fixed draw memberships, completed exact promotion and capture hooks | 6e4ca4f3002d9c2c11bd34db91dea3ff71662a0a286090008e806833e9ef73a3 |
| [gosh/exact-enum.js](evidence/app/gosh/exact-enum.js) | createEngine 63; fitOne 111; sweep 134; finishQuantiles 221; perStudy 244; summary 262; fit(mask) 281; run 287: exact nonempty enumeration, DL, grid, type-7 quartiles, inclusion means | 9d89f7c0a5aa3be070e4c10fb5e52d15710975db82ef19bcecabb9508a63527b |
| [gosh/exact-ui.js](evidence/app/gosh/exact-ui.js) | renderTables 39; renderDensity 69; finish/show 97/105; startExact 123; request 175: worker lifecycle, completion and full exact display | 8d3e99916b929325312c976ba3d0197469e73c698c69edd06a85f116ea916b2a |
| [gosh/plus.js](evidence/app/gosh/plus.js) | derive 33; capture 89; refresh 103; AlmGoshPlus.state 108: sampled occurrences, all 11 inclusion fields including medians, snapshot/restore and suspended URL writes | 5ceb7aea4c44b82c7015f3d5025d684e1299114d67c3d80cbacaf5582234f4f8 |

All 28 direct script/stylesheet dependencies are copied under evidence/app/ in their relative layout. The manifest also covers English glossary and optional PDF-export vendor. These copies support inspection, not a certified standalone runtime. Embedded worker creation uses exact-enum.js. Optional real-data replay corpora and optional webR runtimes are outside the registered native-R comparison and were not run or copied as new evidence.

The [build-info file](evidence/app/shared/build-info.js), SHA-256 **44c8a7d1e2cdad4d4b1c4806cffdd4f9817dc39161cd0de5374761a71bd19177**, embeds **42a94da2110a02200d0b5bff4c56f636b9cbffa9**, different from the declared snapshot. Both identities are preserved; Git ancestry is not certified. Runtime asset closure and provenance reconciliation remain required before real-data execution.

Original REML reproduction, PFT preprocessing/inverse, independence/input checks, subset Wald CIs, thresholds/classification, human-packet selection, comparisons and the publication figure are R-only/external. Native app outputs supply the DL subset fits, exact summaries/grid/inclusion means and sampled inclusion fields. Missing fallback global summaries are calculated externally from captured app fits and separately from R refits. Display rounding cannot establish agreement.

## Audit boundary

[VALIDATION_P13.json](VALIDATION_P13.json) reports document/byte checks only. [audit_p13.py](audit_p13.py) checks hashes, relative links, source-method search scope, word count, exact decision-4 wording, preserved analysis/verification text and Python syntax. It never fits models or transcribes study rows. R scripts are handoffs for pc2; no runtime pass is claimed.

Historical files under evidence/history/ are exact copies and can contain obsolete conclusions, node paths or links. They serve provenance only; active v5 documents govern. No REDTEAM2 report was provided; [JOB.md](evidence/instructions/JOB.md) explicitly places that round after this job.
