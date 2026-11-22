# Week12 independent ESPN scoreboard corroboration — source discovery and bounded interruption

Status: INDEPENDENT_SOURCE_DISCOVERED / FULL_70_SCORE_RECONCILIATION_NOT_EXECUTED / NO_CANONICAL_PROMOTION

- Independently discovered ESPN 2026 Week12 FBS scoreboard https://www.espn.com/college-football/scoreboard/_/week/12/year/2026/seasontype/2.
- One live Firecrawl scrape succeeded, returning 66,445 Markdown characters and 138 occurrences of ESPN gameId URLs (Gamecast/Box Score duplication); visible examples: Oregon 45 at Michigan State 7, ESPN game 401858529; BYU 31 at Kansas 29, game 401856866; Wake Forest 50 at Georgia Tech 29, game 401858310. This is a promising exact original game-ID join source, NOT yet a validated 70/70 result.
- Follow-up combined ESPN scoreboard scrape plus GitHub readback to parse all 70 was rejected BEFORE execution: Firecrawl connected-app credits exhausted. Do not retry Firecrawl until reset or credits are available. No additional games are claimed corroborated by this failed call.
- Prior official NCAA Old Dominion game 6604217 independently establishes Old Dominion 21 @ UConn 29; source correction already applied to QA candidates. ESPN search independently reported same 21-29.
- Current QA source blob 548b1a19f337e00a0a18b8ee8fa45345cd959ce3 and scoring blob 148e06da9a1cdcbe45cefd5af43843f7c3deb473 remain unchanged. 56 modeled, 14 excluded, 43/56 winner direction, margin MAE 13.736111246752518, total MAE 11.611958254609505, Brier 0.19718225044930882.
- Bounded next action: retrieve the ESPN Week12 scoreboard once from an available non-credit-exhausted source, parse 70 original ESPN game IDs and final-score pairs, compare against all 70 CBS/NCAA QA rows, quarantine any discrepancies, persist per-game independent source URLs/retrieval clock and readback. ESPN alone is independent secondary corroboration, not necessarily the NCAA/official-school source demanded by Week11 acceptance; distinguish tiers.
- Week12 original archive identity matches accepted Week11 producer artifact; Week12 profile activation still pending. No scorecard, market, decision, bankroll, or task mutation.
