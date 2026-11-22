# Week 12 frozen lineage and real-money ticket arithmetic QA — Nov 22

Status: QA_PASS_ON_FROZEN_NUMERIC_LINEAGE_AND_PRINTED_TICKET_ARITHMETIC / NO_BOOK_SETTLEMENT / CANONICAL_SCORECARD_NOT_PROMOTED.

## Pinned input blobs
- Original frozen lineage: evidence/audits/CFB_WEEK12_CBS_ORIGINAL_LINEAGE_PREFLIGHT_20261115.json (original source retains 70 original game IDs and numeric strings).
- CBS 70/70 scoreboard-matched final candidate: evidence/audits/CFB_WEEK12_CBS_FINAL_CANDIDATE_20261122_RESEARCH_ONLY.json, blob 5ff4559fee54abf86a109288514a7f4713824b96.
- Derived scoring candidate: evidence/audits/CFB_WEEK12_FIRST_FROZEN_SCORE_CANDIDATE_20261122_QA_ONLY.json, blob 21a7d2a5e8398373375b7de159480aa85607a375.
- Ticket arithmetic candidate: evidence/audits/CFB_WEEK12_NOV21_13_TICKET_GRADE_CANDIDATE_20261122_QA_ONLY.json, blob c551600602d4bbac8ec8b5284f355b36ef591108.
- Canonical actual ticket terms: evidence/operational/CFB_EXECUTION_LEDGER.md.

## Executed independent lineage assertions
- All 70 derived game IDs match original lineage with identical prediction/exclusion status; no extra games.
- 56 modeled original numeric strings pred_margin, pred_total and pred_win match the derived candidate exactly as JS Number representations. No frozen projection changed.
- All 56 modeled signed margin errors equal realized home margin minus original frozen home margin. 14 original exclusions remain unscored.
- CBS scoreboard direct extraction had 70 final blocks, 70 unique matched original IDs, 68 original event codes plus two explicit CBS aliases; conflicts were corrected and retained in source candidate.
- Current provisional metrics: 43/56 winner direction, margin MAE 13.718254103895376, total MAE 11.627854203068864, Brier 0.19718225044930882.

## Ticket conditional arithmetic and printed receipt payout
- 13 original real-money straight tickets, $75 total stake, conditional 5 WIN / 8 LOSS / 0 PUSH. Individual game IDs, teams, side and spread are retained in the ticket candidate.
- Winning printed payouts from canonical ticket intake (not unrounded American-odds estimates):
  - CFB_NOV21-01 Kansas State +10: $9.40, conditional WIN, Arizona 35 Kansas State 28, cushion +3.
  - CFB_NOV21-02 Georgia -15: $9.65, conditional WIN, Georgia 34 South Carolina 6.
  - CFB_NOV21-05 Tennessee +1: $19.10, conditional WIN, LSU 13 Tennessee 27.
  - CFB_NOV21-06 Michigan +3.5: $9.55, conditional WIN, UCLA 16 Michigan 18.
  - CFB_NOV21-12 Wisconsin -4.5: $9.45, conditional WIN, Wisconsin 42 Purdue 10.
- Printed conditional gross return = $57.15; conditional net = -$17.85 on $75 stakes. Unrounded odds calculations differ slightly because receipt printed payout rounding is authoritative for potential payouts.
- These are NOT verified cash receipts, sportsbook adjudications, payout vouchers or money-ledger entries. All 13 settlement states remain UNVERIFIED. Ticket data are downstream execution evidence only, not training or calibration inputs.

## Outstanding acceptance checks
- Verify source independence / status for full 70-game finals where required by established scorecard acceptance governance, especially CBS vs NCAA conflicts. Do not use earlier erroneous Old Dominion 21 score as accepted; full CBS scoreboard states Old Dominion 20 UConn 29.
- Review original frozen pre-event timestamps and scoring-run chronology acceptance contract before canonical append; do not infer acceptance solely from arithmetic PASS.
- Only then consider SHA-guarded append/readback to canonical postgame scorecard; separately seek book settlement evidence before any money-ledger update.
- Canonical Champion, market/decision ledgers, scorecard, money ledger and exactly four production tasks unchanged.
