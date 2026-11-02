# CFB Market Monitor — stage trace CFBMM-SCHED5-20261102T190247151Z

Observed UTC: 2026-11-02T19:05:42.104Z
Trigger: scheduled automation turn 5; task 6ae766e788d881919726d0eeb44450dd; invocation ID unavailable.

| Stage | Disposition | Verified evidence / exact error |
| --- | --- | --- |
| CONNECTOR_ATTEMPT | PASS | GitHub create_file on munchie50/cfb-acquisition-bridge main; startup commit 25f9170981abbc63566131e65d7ee6ff1a7e11a2. |
| RUN_STARTED READBACK | PASS | evidence/run_receipts/CFB_MARKET_MONITOR_TRACE_20261102T190247151Z_6ae766e7.md exact blob 120f5b9b25f41e7b15baee2bd4a8dcd8e973fb59, complete content independently matched. |
| MONDAY RUN DISCOVERY | PASS with route correction | First GitHub fetch on /actions/workflows/<workflow-file>/runs?per_page=10 rejected INVALID_ARGUMENT HTTPError 400 URL not allowed. Did not retry same URL; supported /actions/runs endpoint succeeded. |
| MONDAY ACTUAL JOB/ARTIFACT | PASS_PUSH_QA_NOT_SCHEDULE | Replacement workflow run 41475977584, event push, job 125381535252 success; artifact 13156509024, ZIP SHA256 d6867c2799be28c1a9de2d5b7940448e1eb2c9a39c09e6edfc97dd486bb99556, all member hashes independently matched. Original Monday cron retired in current main. No natural Monday run evidenced. |
| AUTHORITY RECOVERY | PASS_BOUNDED | Fresh main tree latest recovery doorway v1.248 blob 0f3a3a605507cdf6f5bfe0e51c870946550c76fd; v1.246 blob 6b25766c90e3ae212efd529dc2b545c226e6abc7; mandatory v1.245 exact tree blob 57327859afb17ca42451189d3661f4c16fae4f90 (4,230,705 bytes) recovered with fetch_blob and independent GitHub API git/blobs/<sha> route: both 4,230,445 text characters and matching beginning/end. Active v1.247 cadence, v1.236 Hot Sheet, v1.133 controls and original task backup blob fb81b86d0b438fb9e84ce34b618c2c6919ededcd recovered. Canonical market and decision tree blobs unchanged 69caf5b1184eedccc90be7562e4a3bd7cb8b7375 / bb5a9cc83b6a1425dc2972ca84b33aa2bbbf8fa9; not used for production decisions without full runtime. |
| SOURCE PREFLIGHT | PASS_SOURCE_ONLY | cutoff 2026-11-02T15:53:28.240972Z, PASS_REFRESH_SOURCE_PREFLIGHT, 266 future games; schedule SHA256 b5b65c65b725e5657f8eb18fd00b5d7f0974e3d49b9a8665314c55e87a9a55be, PBP SHA256 12e23f7acf84a8aef8d249f99e9953cb687af7a94deaf75e77aefe8341f57e57. See independent operational audit blob ecb017ac8a6d545aeb36c622474720984c3f7779. |
| TUESDAY PREP | PASS_FIT_ONLY | Current Tuesday workflow blob a6f11072af8339abf92fd963589ce173d5fa5868, scheduled Tue 15:00 UTC (09:00 CST). Frozen fit artifact 10895838069 downloaded, exact ZIP SHA256 3a2cabfcd37e0bcf0cae85efc77eaa6755ffb12734d1e48c4c582ed1de375587, selected_coefficients.csv present. No new S0 candidate, no acceptance. |
| COMPUTATION RUNTIME | BLOCKED | Current container GIT_TERMINAL_PROMPT=0 git ls-remote https://github.com/munchie50/cfb-acquisition-bridge.git returned fatal: unable to access HTTPS GitHub: Could not resolve host: github.com. No supported full clone/worktree available here. Runtime checkout helper not executed; cannot claim runtime or compiler acceptance. |
| CURRENT SIX-MARKET DECISIONS | WAIT | Last accepted source pointer Oct27; no Week10 independently accepted FIRST_FROZEN S0. R93 378 WAIT / zero certified. No current executable operator/venue/offer quotes, no official current-game material clearance. |
| HOT SHEET / INTEGRATION | NOT ATTEMPTED | Producer gate blocked by missing accepted snapshot, current offer evidence and runtime; prior accepted Week9 publication preserved. |
| CLOSURE | PENDING | Separate terminal candidate and independently verified RUN_CLOSURE to follow. |

No secret material, speculative root cause, task schedule, model, Champion, wager, money or canonical production mutations. No chargeable Firecrawl calls or repeated green market-gate CI.
