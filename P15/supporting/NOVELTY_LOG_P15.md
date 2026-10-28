# P15 v6 novelty log

Search date: 2026-10-28. This document records supplied pc2 searches and the coordinator dispositions in [V4_JOB_P15.md](evidence/V4_JOB_P15.md) and [V5_JOB_P15.md](evidence/V5_JOB_P15.md). V6 rechecked JSON structure, metadata counts, distinct work IDs and hashes with Python; it did not conduct a new database/full-text search or analyse study data.

## Decision and deviation

Europe PMC and OpenAlex replace Google Scholar by [MAHMOOD_DECISIONS.md item 3](evidence/MAHMOOD_DECISIONS.md). Scholar showed a bot check ("unusual traffic") on 2026-10-28, was recorded as blocked and was not bypassed. No login, access-control workaround or author contact was attempted.

No equivalent prior re-analysis was identified in the recorded checks. An equivalent must re-analyse the same candidate synthesis/outcome/effect set using study-cluster CORR robust variance estimation with CR2/Satterthwaite inference for the registered mean/domain question; a materially identical implementation qualifies. Citation alone, another dataset or the original ICC aggregation sensitivity does not qualify. Suspected equivalence requires methods-level confirmation before exclusion. There is no claim of priority or universal absence.

## Primary coverage closure and flagged records

The earlier OpenAlex file records W2556258011, cited_by_count=343, retrieved=200, complete=false and HTTP 401 during cursor paging. That attempt remains recorded as blocked; missing records were not counted as reviewed.

NOVELTY_openalex_P15primary_paged_2026-10-28.json records "page-based, per-page 100", cited_by_count=343 and retrieved_unique=343. V6 verified 343 metadata records with 343 distinct OpenAlex IDs. This supplied ordinary page-based retrieval closes the cursor coverage gap; V6 did not retry the blocked endpoint.

**Coordinator disposition ([v4 note](evidence/V4_JOB_P15.md)): pc2 reviewed the seven flagged titles; none applies RVE/dependence modelling to the Rytwinski 2016 dataset.** The noted topic matches include a 2021 tropical wildlife-vehicle-collision reproducibility paper, a 2025 vulnerability meta-analysis and comments. This is the supplied review conclusion, not an independently performed v6 full-text adjudication.

The paged JSON has no separate flagged-subset or per-title adjudication field. The older cursor log has eight flagged metadata entries. These are different reporting objects: do not relabel those eight entries as the seven reviewed titles or invent a one-to-one disposition list. The coordinator's supplied conclusion is attributed explicitly and retained without overstating its documentary detail.

Fallback Europe PMC/OpenAlex screening similarly identified no equivalent in retrieved records. Fallback feasibility is independently unresolved; novelty screening alone does not activate it.

## Limits and preservation

Citing lists cover their respective indexes at the recorded date, not all literature. PubMed queries below use the title truncations supplied by pc2 and are supplemental to the citation checks. Counts across indexes overlap and must not be added. New equivalent evidence would require the unchanged prospective candidate disposition, not selective redefinition of equivalence. All three supplied raw logs and both coordinator job notes are now preserved as exact byte copies. [SHA-256 manifest](EVIDENCE_SHA256.md). Primary feasibility now follows the binding [v6 deterministic rule](SCALE_CHECK_P15.md); no row check or mapping decision was performed. Novelty clearance is independent of that future check.

## Exact recorded lookups and queries

| Candidate/index | Exact key | Retrieved / indexed |
|---|---|---|
| primary / Europe PMC | MED / 27870889 citing-record lookup | 82/82 |
| fallback / Europe PMC | MED / 31067283 citing-record lookup | 26/26 |
| primary / OpenAlex, original log | https://openalex.org/W2556258011 citing-record lookup | 200/343 |
| fallback / OpenAlex, original log | https://openalex.org/W2943919874 citing-record lookup | 74/74 |
| primary / OpenAlex, paged update | W2556258011; page-based, per-page 100 | 343/343 unique |

### Primary / PubMed

```text
(robust variance OR dependent effect OR multilevel OR reanalysis OR re-analysis) AND ("How Effective Is Road Mitigation at Reducing Road-Kill? A Me")
```

Count: 0. Supplied returned ID list: empty.

### Fallback / PubMed

```text
(robust variance OR dependent effect OR multilevel OR reanalysis OR re-analysis) AND ("Do our risk preferences change when we make decisions for ot")
```

Count: 0. Supplied returned ID list: empty.

## Evidence hashes

| Supplied file | SHA-256 |
|---|---|
| [NOVELTY_pc2_2026-10-28.json](evidence/NOVELTY_pc2_2026-10-28.json) | `54c69ad0ec27c6f16aec5e880266650c04bf62c2ca107276a474db97f94324d7` |
| [NOVELTY_openalex_2026-10-28.json](evidence/NOVELTY_openalex_2026-10-28.json) | `05c3de75c25a627907fda403c1a671d4a363bcabec57b4ef58d375784e8140e2` |
| [NOVELTY_openalex_P15primary_paged_2026-10-28.json](evidence/NOVELTY_openalex_P15primary_paged_2026-10-28.json) | `15c33a8c364cd305a60286d90971932e1cd4eefebdf6401ed923aa376415fcf2` |
| [V4_JOB_P15.md](evidence/V4_JOB_P15.md) | `283047c869269f462a5c1f708a9c6f84e814788c4363c8a33a8dae38bf71eec9` |
| [MAHMOOD_DECISIONS.md](evidence/MAHMOOD_DECISIONS.md) | `6d400ca1963b4df8d3d6b0c1e10c9a28485e051f6f0f0beca07185451fc945a5` |

The archived [v5 coordinator note](evidence/V5_JOB_P15.md) states exactly:

> OpenAlex 343/343 citing works retrieved via page-based paging (cursor paging returned HTTP 401 after 200). pc2 reviewed the 7 flagged titles: none applies RVE or dependence modelling to the Rytwinski 2016 dataset.

The note is copied in full rather than re-created as a purported original. Its SHA-256 is in the manifest. No per-title methods-adjudication table is supplied.
