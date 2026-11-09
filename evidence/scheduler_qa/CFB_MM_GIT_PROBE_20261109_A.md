# Market Monitor Git transport diagnostic

Correlation: MM_GIT_PROBE_20261109_A
Date: 2026-11-09 CT
Scope: READ-ONLY runtime probe, no producer publication or canonical changes.

- Existing production automation run-now returned inline execution in the current Work conversation. It did not dispatch or identify a new background recurring worker. The most recent recorded automation run ID was unchanged.
- Original production prompt, schedule and enabled state were restored and independently read back after diagnostic dispatch. No extra automation.
- Authenticated connector main: 7fdc64d09f88aaf4528cd77020232c42d73ceb9c.
- Python getaddrinfo for github.com and api.github.com both returned temporary failure in name resolution.
- GIT_ROUTE_PASS in the inline Work runtime: bounded, noninteractive git ls-remote using the standard repository HTTPS URL exited 0 and returned the exact connector-observed main SHA.
- CLONE_FIRST_PASS in the same Work runtime: ordinary Git clone, commit ancestry against origin/main, pinned detached checkout, nonshallow history, and exact worktree helper identity verified. Helper blob b13930cb714eb87c8dce6136ffab6fbceeb44898, 3780 bytes. No helper API download or connector-to-shell payload transfer was needed for this probe.
- No governed review validation, live production work or publication was run by the probe. Scheduled worker Git connectivity and checkout-first production integration remain unproved.
