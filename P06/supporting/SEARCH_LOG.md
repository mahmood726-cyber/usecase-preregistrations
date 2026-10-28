# Search and URL log

All entries below were executed or observed on **2026-10-27 (Europe/London)**. This is a local draft log. No publishing, trial-data extraction, or analysis occurred. Queries are recorded literally. Web results are snippets/landing pages, not database exports. An access error is not a zero hit count. Only the specifically labelled F14/F06/F06b result sets contribute to the count ledger.

## Methods and database syntax discovery

Web queries:

1. `site.europepmc.org REST search API OPEN_ACCESS FIRST_PDATE meta analysis query`
2. `site.metafor-project.org regtest PET PEESE Egger predictor sei vi test`

Returned landing URLs (not all opened or used as authority):

- https://wviechtb.github.io/metafor/reference/regtest.html
- https://stat.ethz.ch/CRAN/web/packages/metafor/metafor.pdf
- https://ftp.eenet.ee/pub/cran/web/packages/metafor/metafor.pdf
- https://ppw.kuleuven.be/mesrg/documents/sr2015-course-text/workshop-r/Manual-metafor.pdf
- https://www.rdocumentation.org/packages/metafor/versions/2.4-0/topics/regtest
- https://wviechtb.github.io/metafor/reference/print.regtest.rma.html
- https://zhaoboding.github.io/PyMetaAnalysis/methods/statistical-methods/
- https://www.quantargo.com/help/r/latest/packages/metafor/2.4-0/regtest
- https://r-packages.io/packages/metafor/regtest
- https://europepmc.org/docs/EBI_Europe_PMC_Web_Service_Reference.pdf
- https://github.com/alex-strobel/DPP-LabManual/blob/main/Research/Analysis/Methods/Meta-Analysis/Meta_Analysis.md
- https://dev.europepmc.org/RestfulWebService

Only the package author's documentation is cited for the method. Draft-specific thresholds and restrictions are design decisions. The production and development REST documentation pages were opened at https://europepmc.org/RestfulWebService (403) and https://dev.europepmc.org/RestfulWebService (timeout); their search snippets were available.

## Exact proposed database queries and attempts

### P14

```text
(PUB_TYPE:"Meta-Analysis" OR TITLE:"meta-analysis" OR TITLE:"meta analysis") AND (TITLE_ABS:randomized OR TITLE_ABS:randomised OR TITLE_ABS:RCT OR TITLE_ABS:RCTs) AND OPEN_ACCESS:Y AND LANG:eng AND FIRST_PDATE:[2017-01-01 TO 2025-12-31] AND (TITLE_ABS:child* OR TITLE_ABS:pediatric* OR TITLE_ABS:paediatric* OR TITLE_ABS:infant* OR TITLE_ABS:neonat* OR TITLE_ABS:adolescen*) sort_date:y
```

Exact URL submitted to web tools:

https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=(PUB_TYPE%3A%22Meta-Analysis%22%20OR%20TITLE%3A%22meta-analysis%22%20OR%20TITLE%3A%22meta%20analysis%22)%20AND%20(TITLE_ABS%3Arandomized%20OR%20TITLE_ABS%3Arandomised%20OR%20TITLE_ABS%3ARCT%20OR%20TITLE_ABS%3ARCTs)%20AND%20OPEN_ACCESS%3AY%20AND%20LANG%3Aeng%20AND%20FIRST_PDATE%3A%5B2017-01-01%20TO%202025-12-31%5D%20AND%20(TITLE_ABS%3Achild*%20OR%20TITLE_ABS%3Apediatric*%20OR%20TITLE_ABS%3Apaediatric*%20OR%20TITLE_ABS%3Ainfant*%20OR%20TITLE_ABS%3Aneonat*%20OR%20TITLE_ABS%3Aadolescen*)%20sort_date%3Ay&format=json&pageSize=25&resultType=core&cursorMark=*

The same query and parameters were attempted via Python urllib (HTTPS handler unavailable), then subprocess curl.exe (exit 35, Schannel SEC_E_NO_CREDENTIALS). Web open and the connected web-search tool both returned inaccessible-URL errors. The clients used URL-encoding with spaces as either %20 or +; parameters were query, format=json, pageSize=25, resultType=core, cursorMark=*. No response records or hitCount were obtained. Search date: 2026-10-27. No retries changed the sampling terms.

### P06

```text
(PUB_TYPE:"Meta-Analysis" OR TITLE:"meta-analysis" OR TITLE:"meta analysis") AND (TITLE_ABS:randomized OR TITLE_ABS:randomised OR TITLE_ABS:RCT OR TITLE_ABS:RCTs) AND OPEN_ACCESS:Y AND LANG:eng AND FIRST_PDATE:[2017-01-01 TO 2025-12-31] AND (TITLE_ABS:cancer* OR TITLE_ABS:oncolog* OR TITLE_ABS:neoplas* OR TITLE_ABS:tumor* OR TITLE_ABS:tumour* OR TITLE_ABS:carcinoma* OR TITLE_ABS:leukemia* OR TITLE_ABS:leukaemia* OR TITLE_ABS:lymphoma* OR TITLE_ABS:myeloma*) sort_date:y
```

Exact URL submitted to web tools:

https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=(PUB_TYPE%3A%22Meta-Analysis%22%20OR%20TITLE%3A%22meta-analysis%22%20OR%20TITLE%3A%22meta%20analysis%22)%20AND%20(TITLE_ABS%3Arandomized%20OR%20TITLE_ABS%3Arandomised%20OR%20TITLE_ABS%3ARCT%20OR%20TITLE_ABS%3ARCTs)%20AND%20OPEN_ACCESS%3AY%20AND%20LANG%3Aeng%20AND%20FIRST_PDATE%3A%5B2017-01-01%20TO%202025-12-31%5D%20AND%20(TITLE_ABS%3Acancer*%20OR%20TITLE_ABS%3Aoncolog*%20OR%20TITLE_ABS%3Aneoplas*%20OR%20TITLE_ABS%3Atumor*%20OR%20TITLE_ABS%3Atumour*%20OR%20TITLE_ABS%3Acarcinoma*%20OR%20TITLE_ABS%3Aleukemia*%20OR%20TITLE_ABS%3Aleukaemia*%20OR%20TITLE_ABS%3Alymphoma*%20OR%20TITLE_ABS%3Amyeloma*)%20sort_date%3Ay&format=json&pageSize=25&resultType=core&cursorMark=*

The same query and parameters were attempted via Python urllib (HTTPS handler unavailable), then subprocess curl.exe (exit 35, Schannel SEC_E_NO_CREDENTIALS). Web open and the connected web-search tool both returned inaccessible-URL errors. The clients used URL-encoding with spaces as either %20 or +; parameters were query, format=json, pageSize=25, resultType=core, cursorMark=*. No response records or hitCount were obtained. Search date: 2026-10-27. No retries changed the sampling terms.

## Other retrieval diagnostics, 2026-10-27

- **Initial exploratory API query**: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=OPEN_ACCESS%3AY%20AND%20TITLE%3Ameta-analysis%20AND%20TITLE_ABS%3Apediatric%20AND%20FIRST_PDATE%3A%5B2017-01-01%20TO%202025-12-31%5D&format=json&pageSize=25&resultType=core
  - Web inaccessible; not the final sampling query.
- **Public HTTP connectivity probe**: http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=cancer&format=json&pageSize=1
  - curl exit 52, empty reply; no credentials/data sent.
- **HTTPS connectivity probe**: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=cancer&format=json&pageSize=1
  - Windows curl Schannel initialization failed; Git curl OpenSSL backend initialization failed (3221225794); web inaccessible.
- **Bibliographic API probe**: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:38767595&format=json
  - Web inaccessible; no individual analysis or selection.
- **Exploratory PubMed query**: https://pubmed.ncbi.nlm.nih.gov/?term=%28pediatric+OR+paediatric+OR+children%29+AND+meta-analysis+AND+randomized&filter=dates.2017%2F1%2F1-2025%2F12%2F31&filter=simsearch2.ffrft&size=50
  - Web inaccessible.
- **Exploratory Europe PMC UI query**: https://europepmc.org/search?query=OPEN_ACCESS:Y%20AND%20TITLE:meta-analysis%20AND%20TITLE_ABS:cancer
  - Web inaccessible.
- **E-utilities count probe**: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=pediatric%20meta-analysis&rettype=count&retmode=json
  - Web inaccessible.
- **Simple PubMed probe**: https://pubmed.ncbi.nlm.nih.gov/?term=pediatric+meta-analysis
  - Web inaccessible.

## Exploratory web queries (outside count denominators)

```text
site:pmc.ncbi.nlm.nih.gov "meta-analysis" "randomized" "children" after:2016-12-31 before:2026-01-01
```

```text
site:pmc.ncbi.nlm.nih.gov "meta-analysis" "randomized" "cancer" after:2016-12-31 before:2026-01-01
```

Returned landing URLs:

- https://pmc.ncbi.nlm.nih.gov/articles/PMC13583843/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12171270/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7156752/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13643451/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11106715/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13353196/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11905918/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12379107/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6517244/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13243340/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8783568/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8799209/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10625440/pdf/CD003913.pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10992808/pdf/262_2022_Article_3349.pdf

These queries returned out-of-window items despite the date syntax. No total or field prevalence is inferred.

## Defined fallback count searches

### F14 - 2026-10-27

```text
site:pmc.ncbi.nlm.nih.gov "meta-analysis" "randomized controlled trials" (pediatric OR paediatric OR children OR infants) (2017 OR 2018 OR 2019 OR 2020 OR 2021 OR 2022 OR 2023 OR 2024 OR 2025)
```

Web search, first returned response, 14 unique records. Exact returned URLs:

- https://pmc.ncbi.nlm.nih.gov/articles/PMC12890145/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11811580/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11763852/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13113799/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10946707
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13176288/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12337541/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13371794/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13102325/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10783429/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13460936/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13516984/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10857664/pdf/UBMC_37_2301904.pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12392408/pdf/jsae036.pdf

### F06 - 2026-10-27

```text
site:pmc.ncbi.nlm.nih.gov "meta-analysis" "randomized controlled trials" (cancer OR oncology OR carcinoma OR lymphoma) (2017 OR 2018 OR 2019 OR 2020 OR 2021 OR 2022 OR 2023 OR 2024 OR 2025)
```

Web search, first returned response, 14 unique records. Exact returned URLs:

- https://pmc.ncbi.nlm.nih.gov/articles/PMC12623341/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11106715/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9372974/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11270896/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10241766/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11444977/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13102325/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12030876/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12709029/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13423770/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13266398/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13353234/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10992808/pdf/262_2022_Article_3349.pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11797173/pdf/432_2023_Article_4874.pdf

### F06b - 2026-10-27

```text
cancer "meta-analysis" "randomized controlled trials" "2020" "open access"
```

Web search, first returned response, 14 unique records. Exact returned URLs:

- https://pmc.ncbi.nlm.nih.gov/articles/PMC8799209/
- https://link.springer.com/article/10.1007/s00432-020-03290-y
- https://www.mdpi.com/2072-6694/12/12/3655
- https://www.nature.com/articles/s41416-020-01050-w
- https://link.springer.com/article/10.1186/s12885-020-06910-5
- https://doi.org/10.1016/J.ECLINM.2020.100458
- https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2020.541699/full
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7675103/
- https://www.nature.com/articles/s41416-020-0761-6
- https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2771442
- https://www.nature.com/articles/s41416-020-01060-8
- https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2020.00049/full
- https://bmccancer.biomedcentral.com/track/pdf/10.1186/s12885-020-06871-9
- https://journals.sagepub.com/doi/pdf/10.1177/1533033820967454

F06b was added as an exploratory older-publication check after the initial pages contained many apparent 2026 papers; it does not alter the primary frame. All its records, including failures, were counted. Neither a positive result nor the apparent magnitude of any clinical effect influenced this addition.

## Follow-up metadata checks on counted records

Direct opens, 2026-10-27, for publication/eligibility counting only:

- https://pmc.ncbi.nlm.nih.gov/articles/PMC11811580/ - Browser-check page; no usable full text from this open.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10946707/ - Browser-check page; no usable full text from this open.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12337541/ - Browser-check page; no usable full text from this open.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10857664/ - Browser-check page; no usable full text from this open.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12392408/ - Accessible bibliographic/method text.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9372974/ - Browser-check page; no usable full text from this open.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10241766/ - Accessible bibliographic/method text.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12030876/ - Browser-check page; no usable full text from this open.

Focused web queries, 2026-10-27:

```text
site:pmc.ncbi.nlm.nih.gov/articles/PMC9372974 "Abstract" "trials"
```

```text
site:pmc.ncbi.nlm.nih.gov/articles/PMC12337541 "Abstract" "trials"
```

```text
site:pmc.ncbi.nlm.nih.gov/articles/PMC10857664 "studies" "randomized"
```

```text
site:pmc.ncbi.nlm.nih.gov/articles/PMC12030876 "Results" "trials"
```

```text
"Social media-based interventions for patients with cancer" meta-analysis 2022 trials
```

```text
"Effect of intervention on screen time in preschoolers" 2025 trials
```

Returned landing URLs from the four path-specific queries (mostly irrelevant; not added to the denominator):

- https://pmc.ncbi.nlm.nih.gov/articles/PMC10857664/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10362939/pdf/mxac010.pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11783733/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13108917/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10753608/pdf/zrk128.pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10594594/pdf/CD014722.pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11600493/pdf/MR000011.pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13147469/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9006700/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13524355/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11196434/pdf/40200_2023_Article_1328.pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13286251/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9427100/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12652271/

Returned landing URLs from the two title-based checks (alternate manifestations are not counted twice):

- https://pmc.ncbi.nlm.nih.gov/articles/PMC12337541/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9372974/
- https://doi.org/10.1186/s12889-025-23700-5
- https://d-nb.info/1378805887/34
- https://link.springer.com/content/pdf/10.1007/s11764-022-01244-6.pdf

No trial forest-plot rows were transcribed. Existing published effect values that appeared incidentally in search snippets were not recorded in the count ledger or used to select a sample. No primary effect calculations, cumulative fits, asymmetry tests or adjustments were performed.

## Searches reserved for a future registered workflow

The per-review PubMed/Google Scholar novelty-query templates in the drafts have **not** been executed; no review is selected in this lane. The drafts' full-frame pagination, random ordering, extraction gates and app/R work are likewise future actions. The task's draft-only restriction supersedes the protocol's usual immediate release/deposit step.

LANE DONE

## Complete frame pulls from pc2, 2026-10-27 (supersedes the access-failure entries above for the two exact queries)

Executed on pc2 (this machine reaches Europe PMC; the Codex sandbox did not). Scripts: `MMA_frames_2026-10-27/pull_frames.py` and `dedup_order.py`. Endpoint `https://www.ebi.ac.uk/europepmc/webservices/rest/search`, parameters `format=json`, `resultType=core`, `pageSize=1000`, `cursorMark` followed from `*` until a page returned 0 records. Page size 1000 (the API maximum for core) instead of the feasibility page's 25 changes only pagination, not the record set. Query strings are byte-identical to the drafts (including `sort_date:y`).

### P14

- hitCount reported: **3436**; records retrieved: **3436** (equal); started 2026-10-27T19:19:11+00:00, finished 2026-10-27T19:19:41+00:00 (UTC).
- After deduplication (DOI, then PMID, then normalized title+first author+year): **3433** (3 merged; all were same-title same-year version pairs, listed in `P14_dedup_log.json`).
- Manifest with every page file, sha256, UTC time and nextCursorMark: `MMA_frames_2026-10-27/P14_pull_manifest.json` (sha256 of manifest: `91d8168b58119c63e39fd253e792fcfa0492de35c70de351e013771e052e55ca`).

| Page file | Records | sha256 | Pulled (UTC) | Request URL |
|---|---:|---|---|---|
| `P14/P14_page001.json` | 1000 | `01ca27851cb59c6be1c1686c93b6369d59be5c393939abf05b27a721b2cb39f7` | 2026-10-27T19:19:11+00:00 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28PUB_TYPE%3A%22Meta-Analysis%22%20OR%20TITLE%3A%22meta-analysis%22%20OR%20TITLE%3A%22meta%20analysis%22%29%20AND%20%28TITLE_ABS%3Arandomized%20OR%20TITLE_ABS%3Arandomised%20OR%20TITLE_ABS%3ARCT%20OR%20TITLE_ABS%3ARCTs%29%20AND%20OPEN_ACCESS%3AY%20AND%20LANG%3Aeng%20AND%20FIRST_PDATE%3A%5B2017-01-01%20TO%202025-12-31%5D%20AND%20%28TITLE_ABS%3Achild%2A%20OR%20TITLE_ABS%3Apediatric%2A%20OR%20TITLE_ABS%3Apaediatric%2A%20OR%20TITLE_ABS%3Ainfant%2A%20OR%20TITLE_ABS%3Aneonat%2A%20OR%20TITLE_ABS%3Aadolescen%2A%29%20sort_date%3Ay&format=json&resultType=core&pageSize=1000&cursorMark=%2A |
| `P14/P14_page002.json` | 1000 | `e13efb590650e944b8e34c1c0e4f5e7317b0ac4b2517f6657b830a33c12696c5` | 2026-10-27T19:19:19+00:00 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28PUB_TYPE%3A%22Meta-Analysis%22%20OR%20TITLE%3A%22meta-analysis%22%20OR%20TITLE%3A%22meta%20analysis%22%29%20AND%20%28TITLE_ABS%3Arandomized%20OR%20TITLE_ABS%3Arandomised%20OR%20TITLE_ABS%3ARCT%20OR%20TITLE_ABS%3ARCTs%29%20AND%20OPEN_ACCESS%3AY%20AND%20LANG%3Aeng%20AND%20FIRST_PDATE%3A%5B2017-01-01%20TO%202025-12-31%5D%20AND%20%28TITLE_ABS%3Achild%2A%20OR%20TITLE_ABS%3Apediatric%2A%20OR%20TITLE_ABS%3Apaediatric%2A%20OR%20TITLE_ABS%3Ainfant%2A%20OR%20TITLE_ABS%3Aneonat%2A%20OR%20TITLE_ABS%3Aadolescen%2A%29%20sort_date%3Ay&format=json&resultType=core&pageSize=1000&cursorMark=AoJwgNWIlZEDKDUxMzI0Njg2 |
| `P14/P14_page003.json` | 1000 | `47d3ef38a7bafc53b767e0d6882f6bf15a302ba47bec8f12c925944e82c6d411` | 2026-10-27T19:19:28+00:00 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28PUB_TYPE%3A%22Meta-Analysis%22%20OR%20TITLE%3A%22meta-analysis%22%20OR%20TITLE%3A%22meta%20analysis%22%29%20AND%20%28TITLE_ABS%3Arandomized%20OR%20TITLE_ABS%3Arandomised%20OR%20TITLE_ABS%3ARCT%20OR%20TITLE_ABS%3ARCTs%29%20AND%20OPEN_ACCESS%3AY%20AND%20LANG%3Aeng%20AND%20FIRST_PDATE%3A%5B2017-01-01%20TO%202025-12-31%5D%20AND%20%28TITLE_ABS%3Achild%2A%20OR%20TITLE_ABS%3Apediatric%2A%20OR%20TITLE_ABS%3Apaediatric%2A%20OR%20TITLE_ABS%3Ainfant%2A%20OR%20TITLE_ABS%3Aneonat%2A%20OR%20TITLE_ABS%3Aadolescen%2A%29%20sort_date%3Ay&format=json&resultType=core&pageSize=1000&cursorMark=AoJwwKqA%2FYEDKDQ2MzgyMzg0 |
| `P14/P14_page004.json` | 436 | `3e272cf193bd8185471238a93b77370a780a99f0c6674d9c92d18ca9b3d54858` | 2026-10-27T19:19:36+00:00 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28PUB_TYPE%3A%22Meta-Analysis%22%20OR%20TITLE%3A%22meta-analysis%22%20OR%20TITLE%3A%22meta%20analysis%22%29%20AND%20%28TITLE_ABS%3Arandomized%20OR%20TITLE_ABS%3Arandomised%20OR%20TITLE_ABS%3ARCT%20OR%20TITLE_ABS%3ARCTs%29%20AND%20OPEN_ACCESS%3AY%20AND%20LANG%3Aeng%20AND%20FIRST_PDATE%3A%5B2017-01-01%20TO%202025-12-31%5D%20AND%20%28TITLE_ABS%3Achild%2A%20OR%20TITLE_ABS%3Apediatric%2A%20OR%20TITLE_ABS%3Apaediatric%2A%20OR%20TITLE_ABS%3Ainfant%2A%20OR%20TITLE_ABS%3Aneonat%2A%20OR%20TITLE_ABS%3Aadolescen%2A%29%20sort_date%3Ay&format=json&resultType=core&pageSize=1000&cursorMark=AoJwwILYtOwCKDQwMjcxNjAw |
| `P14/P14_page005.json` | 0 | `04d9edc4957d47f61f2288a1446dbd60a6053b23b31e9b0bb9efc6abc0ff30b1` | 2026-10-27T19:19:40+00:00 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28PUB_TYPE%3A%22Meta-Analysis%22%20OR%20TITLE%3A%22meta-analysis%22%20OR%20TITLE%3A%22meta%20analysis%22%29%20AND%20%28TITLE_ABS%3Arandomized%20OR%20TITLE_ABS%3Arandomised%20OR%20TITLE_ABS%3ARCT%20OR%20TITLE_ABS%3ARCTs%29%20AND%20OPEN_ACCESS%3AY%20AND%20LANG%3Aeng%20AND%20FIRST_PDATE%3A%5B2017-01-01%20TO%202025-12-31%5D%20AND%20%28TITLE_ABS%3Achild%2A%20OR%20TITLE_ABS%3Apediatric%2A%20OR%20TITLE_ABS%3Apaediatric%2A%20OR%20TITLE_ABS%3Ainfant%2A%20OR%20TITLE_ABS%3Aneonat%2A%20OR%20TITLE_ABS%3Aadolescen%2A%29%20sort_date%3Ay&format=json&resultType=core&pageSize=1000&cursorMark=AoJwwOzUq9kCKDM2MDEzMDUw |

### P06

- hitCount reported: **5207**; records retrieved: **5207** (equal); started 2026-10-27T19:19:41+00:00, finished 2026-10-27T19:20:25+00:00 (UTC).
- After deduplication (DOI, then PMID, then normalized title+first author+year): **5205** (2 merged; all were same-title same-year version pairs, listed in `P06_dedup_log.json`).
- Manifest with every page file, sha256, UTC time and nextCursorMark: `MMA_frames_2026-10-27/P06_pull_manifest.json` (sha256 of manifest: `7fa61a46bc66b010cd72263018add5946076b2a60f4d57baddc4e97d3dd41fc6`).

| Page file | Records | sha256 | Pulled (UTC) | Request URL |
|---|---:|---|---|---|
| `P06/P06_page001.json` | 1000 | `7ae243ce504d67bf3a69a4698cce38c123d1e6fa1170efd19ef5d595fcd89c8a` | 2026-10-27T19:19:41+00:00 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28PUB_TYPE%3A%22Meta-Analysis%22%20OR%20TITLE%3A%22meta-analysis%22%20OR%20TITLE%3A%22meta%20analysis%22%29%20AND%20%28TITLE_ABS%3Arandomized%20OR%20TITLE_ABS%3Arandomised%20OR%20TITLE_ABS%3ARCT%20OR%20TITLE_ABS%3ARCTs%29%20AND%20OPEN_ACCESS%3AY%20AND%20LANG%3Aeng%20AND%20FIRST_PDATE%3A%5B2017-01-01%20TO%202025-12-31%5D%20AND%20%28TITLE_ABS%3Acancer%2A%20OR%20TITLE_ABS%3Aoncolog%2A%20OR%20TITLE_ABS%3Aneoplas%2A%20OR%20TITLE_ABS%3Atumor%2A%20OR%20TITLE_ABS%3Atumour%2A%20OR%20TITLE_ABS%3Acarcinoma%2A%20OR%20TITLE_ABS%3Aleukemia%2A%20OR%20TITLE_ABS%3Aleukaemia%2A%20OR%20TITLE_ABS%3Alymphoma%2A%20OR%20TITLE_ABS%3Amyeloma%2A%29%20sort_date%3Ay&format=json&resultType=core&pageSize=1000&cursorMark=%2A |
| `P06/P06_page002.json` | 1000 | `b169fb42cc674c2d634eb3f4125c5cfc0cd044a2aa4a1b242c7492b07c9ea530` | 2026-10-27T19:19:49+00:00 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28PUB_TYPE%3A%22Meta-Analysis%22%20OR%20TITLE%3A%22meta-analysis%22%20OR%20TITLE%3A%22meta%20analysis%22%29%20AND%20%28TITLE_ABS%3Arandomized%20OR%20TITLE_ABS%3Arandomised%20OR%20TITLE_ABS%3ARCT%20OR%20TITLE_ABS%3ARCTs%29%20AND%20OPEN_ACCESS%3AY%20AND%20LANG%3Aeng%20AND%20FIRST_PDATE%3A%5B2017-01-01%20TO%202025-12-31%5D%20AND%20%28TITLE_ABS%3Acancer%2A%20OR%20TITLE_ABS%3Aoncolog%2A%20OR%20TITLE_ABS%3Aneoplas%2A%20OR%20TITLE_ABS%3Atumor%2A%20OR%20TITLE_ABS%3Atumour%2A%20OR%20TITLE_ABS%3Acarcinoma%2A%20OR%20TITLE_ABS%3Aleukemia%2A%20OR%20TITLE_ABS%3Aleukaemia%2A%20OR%20TITLE_ABS%3Alymphoma%2A%20OR%20TITLE_ABS%3Amyeloma%2A%29%20sort_date%3Ay&format=json&resultType=core&pageSize=1000&cursorMark=AoJwwK%2FKj5QDKDUzMTkwNjcy |
| `P06/P06_page003.json` | 1000 | `4c4bb69c440ebd7c2143bb04fcef0934cb042a2b560468c8d8bdf22f200073f9` | 2026-10-27T19:19:58+00:00 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28PUB_TYPE%3A%22Meta-Analysis%22%20OR%20TITLE%3A%22meta-analysis%22%20OR%20TITLE%3A%22meta%20analysis%22%29%20AND%20%28TITLE_ABS%3Arandomized%20OR%20TITLE_ABS%3Arandomised%20OR%20TITLE_ABS%3ARCT%20OR%20TITLE_ABS%3ARCTs%29%20AND%20OPEN_ACCESS%3AY%20AND%20LANG%3Aeng%20AND%20FIRST_PDATE%3A%5B2017-01-01%20TO%202025-12-31%5D%20AND%20%28TITLE_ABS%3Acancer%2A%20OR%20TITLE_ABS%3Aoncolog%2A%20OR%20TITLE_ABS%3Aneoplas%2A%20OR%20TITLE_ABS%3Atumor%2A%20OR%20TITLE_ABS%3Atumour%2A%20OR%20TITLE_ABS%3Acarcinoma%2A%20OR%20TITLE_ABS%3Aleukemia%2A%20OR%20TITLE_ABS%3Aleukaemia%2A%20OR%20TITLE_ABS%3Alymphoma%2A%20OR%20TITLE_ABS%3Amyeloma%2A%29%20sort_date%3Ay&format=json&resultType=core&pageSize=1000&cursorMark=AoJwgJL58IkDKDQ4OTY2NDQ4 |
| `P06/P06_page004.json` | 1000 | `1e4c51f01dbf6625f5385ec738f47bbbf0d931dfd852ed899f8279a2a8c0af94` | 2026-10-27T19:20:06+00:00 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28PUB_TYPE%3A%22Meta-Analysis%22%20OR%20TITLE%3A%22meta-analysis%22%20OR%20TITLE%3A%22meta%20analysis%22%29%20AND%20%28TITLE_ABS%3Arandomized%20OR%20TITLE_ABS%3Arandomised%20OR%20TITLE_ABS%3ARCT%20OR%20TITLE_ABS%3ARCTs%29%20AND%20OPEN_ACCESS%3AY%20AND%20LANG%3Aeng%20AND%20FIRST_PDATE%3A%5B2017-01-01%20TO%202025-12-31%5D%20AND%20%28TITLE_ABS%3Acancer%2A%20OR%20TITLE_ABS%3Aoncolog%2A%20OR%20TITLE_ABS%3Aneoplas%2A%20OR%20TITLE_ABS%3Atumor%2A%20OR%20TITLE_ABS%3Atumour%2A%20OR%20TITLE_ABS%3Acarcinoma%2A%20OR%20TITLE_ABS%3Aleukemia%2A%20OR%20TITLE_ABS%3Aleukaemia%2A%20OR%20TITLE_ABS%3Alymphoma%2A%20OR%20TITLE_ABS%3Amyeloma%2A%29%20sort_date%3Ay&format=json&resultType=core&pageSize=1000&cursorMark=AoJwwP6a8f8CKDQ1OTUyMDkx |
| `P06/P06_page005.json` | 1000 | `49dd2e57dee832154433b5388aa7dbd4772c8f3954e17408e6ed10cd8828dfb1` | 2026-10-27T19:20:15+00:00 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28PUB_TYPE%3A%22Meta-Analysis%22%20OR%20TITLE%3A%22meta-analysis%22%20OR%20TITLE%3A%22meta%20analysis%22%29%20AND%20%28TITLE_ABS%3Arandomized%20OR%20TITLE_ABS%3Arandomised%20OR%20TITLE_ABS%3ARCT%20OR%20TITLE_ABS%3ARCTs%29%20AND%20OPEN_ACCESS%3AY%20AND%20LANG%3Aeng%20AND%20FIRST_PDATE%3A%5B2017-01-01%20TO%202025-12-31%5D%20AND%20%28TITLE_ABS%3Acancer%2A%20OR%20TITLE_ABS%3Aoncolog%2A%20OR%20TITLE_ABS%3Aneoplas%2A%20OR%20TITLE_ABS%3Atumor%2A%20OR%20TITLE_ABS%3Atumour%2A%20OR%20TITLE_ABS%3Acarcinoma%2A%20OR%20TITLE_ABS%3Aleukemia%2A%20OR%20TITLE_ABS%3Aleukaemia%2A%20OR%20TITLE_ABS%3Alymphoma%2A%20OR%20TITLE_ABS%3Amyeloma%2A%29%20sort_date%3Ay&format=json&resultType=core&pageSize=1000&cursorMark=AoJwgNO9o%2FQCKDQyMjYyMjUy |
| `P06/P06_page006.json` | 207 | `361fc7ef1d18c029bf3fde7b5e601b82275c77acbb97ff9a2e6ebcd3f8d6982f` | 2026-10-27T19:20:23+00:00 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28PUB_TYPE%3A%22Meta-Analysis%22%20OR%20TITLE%3A%22meta-analysis%22%20OR%20TITLE%3A%22meta%20analysis%22%29%20AND%20%28TITLE_ABS%3Arandomized%20OR%20TITLE_ABS%3Arandomised%20OR%20TITLE_ABS%3ARCT%20OR%20TITLE_ABS%3ARCTs%29%20AND%20OPEN_ACCESS%3AY%20AND%20LANG%3Aeng%20AND%20FIRST_PDATE%3A%5B2017-01-01%20TO%202025-12-31%5D%20AND%20%28TITLE_ABS%3Acancer%2A%20OR%20TITLE_ABS%3Aoncolog%2A%20OR%20TITLE_ABS%3Aneoplas%2A%20OR%20TITLE_ABS%3Atumor%2A%20OR%20TITLE_ABS%3Atumour%2A%20OR%20TITLE_ABS%3Acarcinoma%2A%20OR%20TITLE_ABS%3Aleukemia%2A%20OR%20TITLE_ABS%3Aleukaemia%2A%20OR%20TITLE_ABS%3Alymphoma%2A%20OR%20TITLE_ABS%3Amyeloma%2A%29%20sort_date%3Ay&format=json&resultType=core&pageSize=1000&cursorMark=AoJwgPDO6t4CKDM3MzcyMDUx |
| `P06/P06_page007.json` | 0 | `5237d881cfbbdce512ec212ad152943b0f7a7e4dccf7c65860c3516d11815409` | 2026-10-27T19:20:25+00:00 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28PUB_TYPE%3A%22Meta-Analysis%22%20OR%20TITLE%3A%22meta-analysis%22%20OR%20TITLE%3A%22meta%20analysis%22%29%20AND%20%28TITLE_ABS%3Arandomized%20OR%20TITLE_ABS%3Arandomised%20OR%20TITLE_ABS%3ARCT%20OR%20TITLE_ABS%3ARCTs%29%20AND%20OPEN_ACCESS%3AY%20AND%20LANG%3Aeng%20AND%20FIRST_PDATE%3A%5B2017-01-01%20TO%202025-12-31%5D%20AND%20%28TITLE_ABS%3Acancer%2A%20OR%20TITLE_ABS%3Aoncolog%2A%20OR%20TITLE_ABS%3Aneoplas%2A%20OR%20TITLE_ABS%3Atumor%2A%20OR%20TITLE_ABS%3Atumour%2A%20OR%20TITLE_ABS%3Acarcinoma%2A%20OR%20TITLE_ABS%3Aleukemia%2A%20OR%20TITLE_ABS%3Aleukaemia%2A%20OR%20TITLE_ABS%3Alymphoma%2A%20OR%20TITLE_ABS%3Amyeloma%2A%29%20sort_date%3Ay&format=json&resultType=core&pageSize=1000&cursorMark=AoJwwOzUq9kCKDM1Nzc5ODkx |

Full-text retrieval during screening used `https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML` and, for forest-plot images/supplements, `https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/supplementaryFiles?includeInlineImage=yes`; each fetch's URL, sha256 and UTC time is saved beside the file (`screening/<pilot>/ft/rNNNNN/fetch.json`, `files_fetch.json`). Europe PMC article web pages (`europepmc.org/articles/...`) returned 403 to scripted requests and were not used or worked around.
