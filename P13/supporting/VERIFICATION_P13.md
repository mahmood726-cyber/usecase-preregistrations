# P13 v5 normative verification specification

The exact binding item 4 is copied in the main registration. The operational details below preserve v3 verification; threshold references to section 7 mean the main registration and analysis supplement.

## 4. Extraction and verification

After release:

- Codex and agy independently extract, blind to each other. Pin agy to a model family different from Codex's and read back the actual family/version from its log line.
- A third model adjudicates every discrepant field against the source. A fourth AI pass, agy using a family different from the adjudicator's, re-checks every adjudicated field. Only disagreements remaining after that pass go to humans.
- Co-authors of P13 and/or Mahmood verify headline-driving rows, the random sample below, and unresolved fields. Record source, finding, checker initials and date in VERIFICATION_LOG.csv.

A headline-driving row is any row meeting either §7 threshold, plus every row attaining the maximum absolute estimate contrast or maximum absolute I² contrast, including ties. Check all required fields. If app/R tied maxima differ within the numerical tolerance, include their union in human checking.

For remaining rows, seed **2026102813-HV**, paper **P13**. DOI means the selected review's lowercase DOI without URL prefix. Index is one-based, three decimal digits. Normalize the printed label to Unicode NFC, strip outer whitespace and replace internal whitespace runs with one ASCII space, preserving case/punctuation. The row key is the compact JSON array [review DOI, index string, normalized label], with literal Unicode and no separator spaces. Hash UTF-8 **"<seed>|<paper>|<row key>"**, without BOM or trailing newline. Sort lowercase SHA-256 digests ascending, ties by row key; take **max(1, ceil(0.05 × n))** if n > 0.

Select the sample once from non-headline rows of the first provisional post-release analysis. Retain it through corrections; add newly headline-driving rows. A sampled row is erroneous if any required field or identity mapping disagrees with the source. Preserve the initial numerator/denominator before correction. If erroneous sampled rows/sample size **exceeds 2%**, repeat full AI double extraction with the same adjudication rules, plus human re-checking of headline rows only. Do not escalate to universal human checking or restart sampling to reset the error rate. Remaining disputed fields still follow the fourth-pass rule. Corrections repeat affected gates and analyses; withhold final classification until checks finish.

Budget approximately three minutes per row plus five administration: eight routine rows ≈29 minutes. Include navigation and difficult unresolved fields; split any packet expected to exceed 30 minutes and split unfinished work at that limit. At most one packet per person per ISO week across all papers, and also at most one in any rolling seven-day period (the retained v3 restriction), coordinated in the shared COAUTHOR_LOAD.md ledger with P14/P06. Mahmood is in the rota. Reassign packets outstanding after seven days to an eligible checker; never skip them.


## Assignment eligibility and ledger

P13 eligible rota from COAUTHOR_LOAD.md: MA (Mahmood), AKi (Agnes Kindiki), IMM (Idah Mokeira Mirera), FA (Fiyinfoluwa Adekunte), AO (Arun Oyewole), AW (Andrew Woo). ID/DI (Izataku David / David Izataku) remains unassignable while the recorded authorship decision is pending; treat both name orders as one person for cross-paper caps if cleared.

Reserve the ledger row with status planned before sending; earlier rows win slot collisions. Record sent/due dates, estimated minutes, status and every reassignment. No packet was assigned or sent by this job. Check the shared ledger across all lanes, including P14/P06, before assigning.

The minimum-one sample applies when non-headline rows exist. If none remain, all rows already receive headline verification; record sample size zero and no invented sample/error denominator. If corrections alter headline membership, retain the initial sample and error numerator/denominator, add newly headline-driving rows, and repeat affected gates and analyses. Final classification waits for complete required verification.
