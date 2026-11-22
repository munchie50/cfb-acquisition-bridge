# Week12 corrected outcome candidate — effective-source metadata drift fixed

Status: QA_METADATA_DRIFT_FIXED / NUMERIC_OUTCOMES_UNCHANGED / CANONICAL_HOLD

## Defect
Two downstream QA artifacts had retained CBS-only status labels after the NCAA official game 6604217 superseded the erroneous CBS scoreboard/header Old Dominion 20 at UConn 29 with official 21 at 29. Their append-only corrections contain historical opposite-direction transitions, so consumers must not treat the last CBS correction or a stale status as effective source authority.

## Fix executed and read back
- Scoring QA evidence/audits/CFB_WEEK12_FIRST_FROZEN_SCORE_CANDIDATE_20261122_QA_ONLY.json: status CBS_69_PLUS_NCAA_1_FINAL_QA_ONLY_NOT_CANONICAL; added effective_final_source_policy default CBS game-specific final with explicit NCAA official 401861968 override. Git blob 50e9f78c56be186e8a760190e463aa3272047d03, commit 906f8a7a3b4794ccd6d7f5a2f8d00f65ec0a42ec.
- Tickets QA evidence/audits/CFB_WEEK12_NOV21_13_TICKET_GRADE_CANDIDATE_20261122_QA_ONLY.json: status CBS_69_PLUS_NCAA_1_CONDITIONAL_TICKET_GRADES_NO_BOOK_SETTLEMENT; same effective_final_source_policy. Git blob 251c07d3f34452f066a4bcf73b603cc9c7458233, commit f2a4e5a1429cacf5be91cf07175c7ef2000febc2.
- Both SHA-guarded updates were independently fetched and exact content compared. No row/score/grade/money changes.
- Current 70-game final candidate blob remains 548b1a19f337e00a0a18b8ee8fa45345cd959ce3. Week12 scoring 56 modeled/14 excluded, 43/56 winner direction, margin MAE 13.736111246752518, total MAE 11.611958254609505, Brier 0.19718225044930882; 13 conditional tickets 5-8, $75 staked.

## Next
- Independently corroborate remaining finals against ESPN/NCAA/school and pin source retrieval time and stable game IDs. ESPN Week12 page discovered, but Firecrawl credits exhausted before full 70-row comparison; don't repeat failed credit-consuming call.
- Profile activation and governed canonical scorecard acceptance remain separate pending gates. Do not touch production or bankroll.
