# Friday Oct 30 recovery — source coverage reconciliation

Status: RESEARCH_ONLY / RECOVERY_OPEN. No full-slate acceptance.

An uncached direct retrieval of https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-9/ returned approximately 118,979 markdown characters. Counting unique game IDs matching NCAAF_2026(1029|1030|1031|1101)_AWAY@HOME yields 40 unique matchups. The accepted manual packet CFB_MARKET_MONITOR_20261030T010121Z describes 56 canonical game identities, 35 eligible future comparisons and 210 market branches.

40 CBS page matchups versus 56 canonical game identities is NOT proof that exactly 16 games are absent from all sources: date scope, page pagination, game identity aliases, and earlier games may differ. It IS proof that this single CBS retrieval is not sufficient evidence to claim 56/56 refreshed canonical coverage.

Do not overwrite the canonical game list with the 40 IDs, treat CBS as a single identified sportsbook, fabricate missing quotes, or publish RUN_PASS. Next: enumerate canonical 56 identities, map CBS IDs by date/teams, classify unmatched rows, supplement only with sourced evidence, reconcile all markets and decision cutoffs, then producer integration/CI/independent closure. No wager, model, task or money changes.
