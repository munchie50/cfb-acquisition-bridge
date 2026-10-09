# Friday five-game source re-quote — Test Routine v6

Status: research QA PASS; not executable sportsbook validation or a production Hot Sheet.

Source: https://www.espn.com/college-football/odds, Firecrawl fresh scrape maxAge=0 during continuation. Linked DraftKings side spreads and American prices extracted from each exact ESPN game block (first two linked spread quotes, away/home), not the distinct Open column. Parent evidence: CFB_WEEK6_OCT08_FRIDAY_ESPN_DK_BENCHMARK_CANDIDATE.md and BYU_PRICE_EXTRACTION_CORRECTION.md.

| Game | ESPN game ID | Kickoff UTC | Away DK linked spread | Home DK linked spread | Exact prior/corrected quote match |
|---|---|---|---|---|---|
| Florida State @ Louisville | 401858254 | 2026-10-09T23:00Z | FSU +3.5 (-108) | Louisville -3.5 (-112) | PASS |
| Iowa @ Washington | 401858487 | 2026-10-10T01:00Z | Iowa +3 (-115) | Washington -3 (-105) | PASS |
| Washington State @ Utah State | 401860922 | 2026-10-10T01:00Z | WSU +5.5 (-112) | Utah State -5.5 (-108) | PASS |
| Wyoming @ San Jose State | 401864519 | 2026-10-10T01:00Z | Wyoming +4.5 (-108) | San Jose State -4.5 (-112) | PASS |
| Iowa State @ BYU | 401856826 | 2026-10-10T02:15Z | Iowa State +10.5 (-112) | BYU -10.5 (-108) | PASS against separate correction |

Result: 5/5 unique games; 10/10 side spread-and-price pairs match preserved reference; no missing price. UTC conversions correspond to frozen Friday kickoff CT 18:00, 20:00, 20:00, 20:00, 21:15, respectively (America/Chicago UTC-5). Quote recency is scrape recency, NOT independently timestamped executable sportsbook offer. No Caesars validation, final decision cutoff approval, BET NOW, wager, or terminal production closure inferred. Champion and FIRST_FROZEN unchanged.
