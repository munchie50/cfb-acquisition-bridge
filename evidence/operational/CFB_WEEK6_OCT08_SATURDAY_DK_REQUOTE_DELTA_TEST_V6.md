# Saturday linked DraftKings quote recheck — Test Routine v6

Status: QA research recheck; no executable sportsbook verification and no production Market Monitor closure.

Source: https://www.espn.com/college-football/odds, fresh Firecrawl scrape with maxAge=0 in continuation session. Baseline: evidence/operational/CFB_WEEK6_OCT08_SATURDAY_FROZEN_MARKET_DISCREPANCY_TRIAGE.md (38 rows), matched to ESPN game URL slug from evidence/operational/CFB_WEEK6_OCT08_SATURDAY_EXACT_IDENTITY_RECONCILIATION.md.

Method: isolate each ESPN game block from kickoff/game ID header to next game header; extract first two *linked DraftKings spread* quotes in displayed away/home order; compare exact signed line and American price against persisted baseline. Source page has no independent bookmaker quote timestamp; scrape recency is not an executable offer guarantee. Final game block may contain other games after it, so take the first two linked spread quotes only.

- Unique frozen games checked: 38/38
- Exact baseline spread-and-price matches: 37
- Quote changes: 1
- Unmatched/ambiguous: 0

## Changed game
Syracuse @ Virginia (Saturday 18:30 CT): prior Syracuse +10 (-110) / Virginia -10 (-110); current displayed Syracuse +10 (-112) / Virginia -10 (-108). Spread unchanged; away price worsened by 2 cents, home price improved by 2 cents. No frozen prediction changed (Virginia -10.1). No bet implied.

## Unchanged
All 37 other Saturday frozen-game linked DraftKings away/home spread-and-price pairs match the Oct 8 stored research snapshot exactly.

## Gate
Do not promote linked DraftKings research into executable Caesars quotes. No decision or practical price cutoff validated; no canonical market ledger/Hot Sheet changed; no production RUN_PASS or scheduler fix claimed. Preserve baseline and this append-only delta as separate evidence.
