# Friday Oct 30 recovery — source coverage reconciliation

Status: RESEARCH_ONLY / RECOVERY_OPEN. No full-slate acceptance.

An uncached direct retrieval of https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-9/ returned approximately 118,979 markdown characters. Counting unique game IDs matching NCAAF_2026(1029|1030|1031|1101)_AWAY@HOME yields 40 unique matchups. The accepted manual packet CFB_MARKET_MONITOR_20261030T010121Z describes 56 canonical game identities, 35 eligible future comparisons and 210 market branches.

40 CBS page matchups versus 56 canonical game identities is NOT proof that exactly 16 games are absent from all sources: date scope, page pagination, game identity aliases, and earlier games may differ. It IS proof that this single CBS retrieval is not sufficient evidence to claim 56/56 refreshed canonical coverage.

Do not overwrite the canonical game list with the 40 IDs, treat CBS as a single identified sportsbook, fabricate missing quotes, or publish RUN_PASS. Next: enumerate canonical 56 identities, map CBS IDs by date/teams, classify unmatched rows, supplement only with sourced evidence, reconcile all markets and decision cutoffs, then producer integration/CI/independent closure. No wager, model, task or money changes.

## SUPERSEDING CORRECTION — Friday direct 56-table recovery

The earlier inference that the CBS page contained only 40 games was WRONG. The 40 count came from unique `View Matchup` hyperlinks, which are absent for some game tables. A subsequent direct source retrieval parsed **56 actual CBS odds-table headers, 112 team rows**, including four earlier-week games, and mapped all **56/56** to the canonical accepted game IDs using explicit team-name aliases. All 56 displayed six primary market values. There is **no CBS source identity coverage gap** in this capture. This corrects and supersedes the earlier 40-versus-56 warning, which must not be used as a blocker.

Authoritative bounded evidence: `evidence/operational/CFB_FRIDAY_20261030_CBS_FULL_56_GAME_RESEARCH_CAPTURE.json`, independently read back blob `73c20f2f477c9808e8c4f5c0e87a12fbf7149062`; 56-case movement comparison `evidence/operational/CFB_FRIDAY_20261030_FULL_BOARD_MARKET_DELTA_RESEARCH.json`, corrected readback blob `f123088cfa647273bc63a2569ce74ee93007cf66`.

This resolves **source-table identity mapping only**. It does NOT certify live identified sportsbook quotes, actual offered prices, complete material-news clearance, fresh 35-case comparative decisions, canonical market/decision writes, a new Hot Sheet, or producer RUN_PASS. Preserve Friday scheduler failure as open.
