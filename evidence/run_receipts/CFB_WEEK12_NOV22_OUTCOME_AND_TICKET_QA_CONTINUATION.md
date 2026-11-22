# Week12 Nov22 outcome and real-money ticket recovery — bounded continuation

Status: CANDIDATES_PERSISTED_AND_READBACK_VERIFIED / FULL_70_OFFICIAL_VERIFICATION_OPEN / NO_CANONICAL_ACCEPTANCE.

## Durable candidate identities
- 70-game final candidate: evidence/audits/CFB_WEEK12_CBS_FINAL_CANDIDATE_20261122_RESEARCH_ONLY.json, blob 7b5bc9f5bf85ef35839add8e08b22007b786c5a7, created commit 535f5c690ed3b9732d4b671e4cbed799a4f83835.
- 56 modeled / 14 excluded FIRST_FROZEN scoring candidate: evidence/audits/CFB_WEEK12_FIRST_FROZEN_SCORE_CANDIDATE_20261122_QA_ONLY.json, blob 76235eccc30b32a6ad0eccbf5dff87d28f536000, commit c2ef1eae3473ae1d3fbe488c64697f179a515ade. Provisional 44/56 winner direction, margin MAE 13.468254103895376, total MAE 11.627854203068864, Brier 0.18722209345053917.
- 13 real-money ticket arithmetic candidate: evidence/audits/CFB_WEEK12_NOV21_13_TICKET_GRADE_CANDIDATE_20261122_QA_ONLY.json, blob 6222cb59711bec86f95356f02b3200ae22f528cf, commit 5ff92d6a733ea1979ab7061799f05facb642f735. 13 tickets, $75 stakes, 5 candidate WIN / 8 candidate LOSS / 0 PUSH. No sportsbook settlement, cash movement or model input.

## Evidence quality and unresolved boundaries
- Final score candidate was manually transcribed into the pre-existing exact 70-game original-ID roster. Structural join 70/70 is verified, but the candidate DOES NOT yet contain independently authenticated per-game CBS final citations or full 70-game score cross-check. Do not call it official final cohort, accepted scorecard or production PASS.
- Two individual results have independently corroborated final scores: Ohio State 28 at Nebraska 31, conference and Ohio State official box scores https://bigten.org/boxscore.aspx?id=JcLFfL9RUu0H5ystoOMbjQ7A58QMysWHEEqi7hufVoQwy9YzDltjQ8EtWEiHoRWTsoB9veqy6%2Byh%2Bddv1bsaQNIG5cdwPNDIZ%2BNJoPzmbBS%2BmkX0uj9iVL73uqPuA%2B7%2Fe%2FRgRpPR4GTMT2%2FsWFtV4Uth75f2PrvARljyJjMpgO970oDJEMHQJz2QzzcQKSgl ; Wisconsin 42 at Purdue 10, conference and Wisconsin official box scores https://uwbadgers.com/sports/football/stats/2026/purdue/boxscore/17151. These two matches do not qualify the other 68.
- Ticket candidate joins exact recorded selections and handicaps to candidate scores. All outcomes are conditional on verified scores. Printed event/issue clocks, live-versus-pregame status and book adjudication remain separate.
- Full original 70-game lineage is retained at evidence/audits/CFB_WEEK12_CBS_ORIGINAL_LINEAGE_PREFLIGHT_20261115.json; original frozen predictions and exclusions were not altered.
- Original Nov20 paired market/decision packets structurally join 70/70 but canonical main still points to Nov19. Do not append historical packets, rewrite accepted pointers, revive expired decisions, or reopen DNS/checkout work.

## First unfinished action
Independently verify each of the remaining 68 score lines against qualified final sources, preferably CBS final scoreboard with individual game identifiers, recording source URL, retrieval timestamp, exact home/away score and any conflicts. Quarantine any discrepancy and invalidate/recompute only affected derived rows. Then execute governed scoring QA against frozen originals, append accepted scorecard with SHA-guarded readback only when authority conditions are satisfied. Separately reconcile each ticket result to final scores and actual book settlement; no automatic cash postings.

Four production tasks, champion, canonical market/decision ledgers, existing scorecard, and money ledger unchanged.


## Nov22 full CBS scoreboard reconciliation — supersedes earlier candidate blob identities
- Fresh CBS FBS 2026 regular Week12 scoreboard parsed as 70 FINAL game blocks; each has two team rows and event-specific CBS boxscore path. Matched 68 directly to original CBS event keys plus two explicit event alias changes (USF@FLAATL -> SFLA@FAU; OREGON@MSU -> OREG@MICHST), 70/70 unique original game IDs. Source https://www.cbssports.com/college-football/scoreboard/FBS/2026/regular/12/.
- Two discrepancies versus previous candidate: Old Dominion @ UConn CBS 20-29 (reverts an erroneous earlier NCAA spotcheck correction to 21); Arizona @ Kansas State CBS 35-28 (prior candidate incorrectly reversed scores). The previous earlier spotcheck assertion was not sufficient; the direct CBS full scoreboard is the present source boundary. Keep discrepancies explicit.
- Corrected 70-game source candidate blob 5ff4559fee54abf86a109288514a7f4713824b96 commit a112905483a6c32c6bdb54a704321277022005b2. Each row has CBS event-specific provenance in cbs_final_provenance.
- Recomputed FIRST_FROZEN candidate blob 21a7d2a5e8398373375b7de159480aa85607a375 commit 3c653ad3717067fc3f24e78e7facbce27fc742b4: 56 scored, 14 excluded, 43/56 winner direction, margin MAE 13.718254103895376, total MAE 11.627854203068864, Brier 0.19718225044930882. Supersedes earlier 44/56 claim.
- Rebound and recomputed all 13 ticket arithmetic rows, blob c551600602d4bbac8ec8b5284f355b36ef591108 commit b7debf6fed036a46b055d947cf075596e7b9782f. Kansas State +10 remains WIN despite Arizona winning outright by 7: Kansas State cover cushion +3. Aggregate remains 5 WIN, 8 LOSS, 0 PUSH, $75 stake. No book settlement or money movement inferred.
- All three changed files independently fetched and byte-compared after SHA-guarded writes. Canonical scorecard, market and decision ledgers, Champion and four scheduled tasks unchanged.
- Next: run independent CBS event-by-event verification and governed scorecard acceptance checks against original immutable FIRST_FROZEN, confirm final-status provenance, then separately adjudicate sportsbook tickets. Do not promote research-only derived grades into official or book-settled states without acceptance.
