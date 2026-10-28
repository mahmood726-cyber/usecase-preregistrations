# Co-author verification load (shared ledger for ALL use-case lanes)

Created 2026-10-28 by the single-example lane (P02, P04, P08, P11, P12, P13, P15). **The P14/P06 lane must use this file too.**
Rule from Mahmood (28 Oct): "we can't overload coauthors".

## Rules (apply to every paper)
1. **Packet size:** each packet takes about 30 minutes or less. If the work is bigger, split it into packets.
2. **Weekly cap:** each person gets at most **one packet per ISO week across all papers**. Check the ledger below before assigning.
3. **Mahmood (MA) is in the rota.** Use him like anyone else, within the same cap.
4. **Reassign after 7 days:** a packet not returned within 7 days of being sent is reassigned to the next eligible person. It is never skipped. Log the reassignment.
5. **Who may verify:** a co-author of that paper, or Mahmood. The verifier's initials and date go into that paper's `VERIFICATION_LOG.csv`.
6. **Human scope per meta-analysis:**
   - rows that drive the headline result;
   - a seeded 5% sample of the other rows (at least 1);
   - fields still disputed after the third-model adjudication and the fourth AI re-check (agy, different model family).
   - If the sample error rate is over 2%: a full AI re-extraction plus a human re-check of the headline rows only.
7. **Claiming a slot:** add the ledger row first (status `planned`), then send. If two lanes collide on a slot, the earlier row wins.

## Eligible verifiers per paper (from manuscript author lines, 2026-10-28; placeholders excluded)
| Paper | Eligible (initials) |
|---|---|
| P02 | MA, IA (Irfan Ahmad), HK (Haris Khan), NA (Najia Ahmad), DI (David Izataku), AW (Andrew Woo) |
| P04 | MA, MAY (Mohamed Ali Yusuf), FA (Fiyinfoluwa Adekunte), AK (Ann Kalu), AW |
| P08 | MA, SMA (Syed Muhammad Ali), QFH (Qudsia Fatimah Hussain), HK, AW |
| P11 | MA, MAY, NA, AO (Arun Oyewole), AW |
| P12 | MA, SA (Sheheryaar Ahmed), GKA (Gabriel Kwaku Agbeshie), AK, AO, AW |
| P13 | MA, AKi (Agnes Kindiki), IMM (Idah Mokeira Mirera), FA, ID (Izataku David), AO, AW |
| P15 | MA, SMA, NA, CM (Christine Muhumuza), AW |
| P14, P06 | *(P14/P06 lane: add your rows)* |

Notes:
- "David Izataku" (P02) and "Izataku David" (P13) look like the same person in two name orders. Treat them as **one** person for the cap until Mahmood confirms otherwise.
- AUTHOR_CONTRIBUTIONS_CONFIRMED.md says Izataku is not on any author list and is pending Mahmood's decision. Do not assign him until that is settled.
- People shared across papers: AO (P11, P12, P13, P14?), NA (P02, P11, P15), AK (P04, P12), FA (P04, P13), MAY (P04, P11), SMA (P08, P15), HK (P02, P08). The weekly cap binds hardest on these.

## Ledger
| Packet ID | Paper / MA | Person | ISO week | Sent (date) | Due (+7 d) | Est. min | Status | Reassigned to |
|---|---|---|---|---|---|---|---|---|
| *(none yet: no extraction has started; it is gated on the prereg release)* | | | | | | | | |
