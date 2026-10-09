# Week 6 — October 8 evening manual source reconciliation candidate

Status: RESEARCH / NOT ACCEPTED AS EXECUTABLE HOT SHEET OR RUN_PASS

## Recovery
Accepted Champion v1.193, FIRST_FROZEN v1.208 unchanged; 49 modeled games from the existing Oct 7 research candidate. No retrospective decisions or bets.

## Source comparison
1. CBS live fetch https://www.cbssports.com/college-football/odds/ALL/2026/regular/week-6/ (maxAge 0; scrape 01a11e25-58ec-704a-8a42-60546bcb2fa9): 199129 extracted characters. Page contains Thursday Oct 8 and future Friday Oct 9 matchups with 'Final' in status column. Do not use its status as authoritative or its quotes as verified Caesars execution prices.
2. ESPN live fetch https://www.espn.com/college-football/schedule (maxAge 0): 80780 extracted characters; Thursday Oct 8 entries show LIVE, Friday/Saturday remain scheduled. This independently demonstrates CBS status inconsistency.
3. ESPN search https://www.espn.com/college-football/odds and schedule: Friday October 9 DraftKings-labelled benchmark shows Louisville -3.5, Washington -3, BYU -10; totals 59.5, 41.5, 46.5 respectively. These are source-displayed benchmarks, not established Caesars prices or actionable recommendations. Independent quote timestamps and complete Friday/Saturday coverage not proven.

## Test routine findings
- SOURCE_STATUS_CONFLICT: do not ingest CBS 'Final' for future games as actual outcomes.
- MARKET_SOURCE_BOUNDARY: book-labelled public quotes are benchmark observations only until independently timestamped and executable conditions established.
- Scope remains 49 modeled games; Saturday 7 morning, 17 afternoon, 14 evening; Friday 5; historical Tue/Wed 3, Thu 3. No row membership changes authorized by this candidate.
- No BET NOW/BET EARLY established; no fabricated line cutoffs or EV.

## Next safe work
- Resolve source clock/status mismatch and qualify independent Friday/Saturday full-slate quotes.
- Reconcile kickoff section membership and per-game deadlines; do not backfill Thursday decisions.
- Apply governed prospective append-only canonical market and decision updates only for qualified observations; produce/readback complete Hot Sheet; persist terminal candidate and separate RUN_CLOSURE.

Champion, task topology, wagers, and canonical operational ledgers unchanged by this research candidate.
