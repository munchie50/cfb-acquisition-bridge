# Week 6 Friday — BYU source price extraction correction

Status: research evidence correction; no executable market approval.

During Test Routine v6 readback, the October 8 Friday benchmark candidate recorded BYU -10.5 with price 'not extracted'. Re-fetched ESPN NCAAF odds (https://www.espn.com/college-football/odds) using live maxAge=0 and inspected Iowa State @ BYU game block (ESPN game ID 401856826). Source linked DraftKings spread quotes:
- Iowa State +10.5 (-112)
- BYU -10.5 (-108)
- Total 46.5: over -108, under -112.

This closes an *extraction omission*, not the underlying market-executability gate. No Caesars price or sportsbook quote timestamp verified. Frozen BYU -11.8 prediction unchanged. No BET NOW/BET EARLY decision, no canonical ledger update and no production completion inferred.

Source parent: evidence/operational/CFB_WEEK6_OCT08_FRIDAY_ESPN_DK_BENCHMARK_CANDIDATE.md. Preserve original candidate and this correction as separate append-only evidence.
