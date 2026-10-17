# Hot Sheet recommendation / venue decoupling — Test Routine audit

Cycle: CFB_HOT_SHEET_READINESS_QA_20261016T235756Z
Scope: downstream controls, read-only diagnostics and code-QA boundary correction. No new operational source, recommendation, wager or primary Hot Sheet.
Status: INSTALLED_READ_BACK_AND_MANUALLY_DEMONSTRATED; natural scheduled adoption of THESE additions remains pending.

## Recovered versus changed
- Current main at recovery: 3c2f30d2bd254ece83cbeda10e9a75add907dbcf.
- Both October16 Monitor cycles have separate RUN_PASS closures. This demonstrates earlier compiler/runtime integration, NOT these new additions.
- Current saved13:01CT sheet/canonical state:62games,52INCONCLUSIVE+10PASS. Nine of the52open games have original frozen exclusions;43 have original frozen predictions but full recommendation reviews are not established by neutral packets.
- Earlier CFB_RECOMMENDATION_DECOUPLING_QA_20261016T032450Z remains STARTED-only. It is not retroactively closed or described as installed work.

## Installed and read back
1. Active consensus control now explicitly removes a Caesars quote as a prerequisite for recommendation formation/display/ranking. Venue confirmation is separate. Actual offer verification/execution evidence, original limits, maturity, market/material evidence and deadlines remain protected. Missing venue/practical trip alone must not hide observation/experimental lean.
2. scripts/cfb_hot_sheet_readiness.py reports exact per-game missing/unreviewed prerequisites from canonical packets, preserving closed PASS and avoiding guesses from boilerplate prose. assess() proves venue verification does not change prerequisite completeness. EARNED remains a caller assertion requiring independently qualified evidence, not acceptance.
3. scripts/cfb_consensus_reference.py formats caller-qualified non-Caesars constituents, deduplicates supplied operator identities, rejects conflicting observations, preserves paired prices and clocks, and calculates descriptive median points/dispersion only. Unknown/out-of-window updates remain explicitly unavailable. No price averaging, derived executable offer, moneyline probability, bet rule or source acquisition.
4. All four existing enabled task prompts received the bounded decoupling/diagnostic instruction. Independent post-update inventory:11identities preserved, exactly4enabled; all existing prompt prefixes retained; titles, schedules, timezones, timing modes, enabled states and disabled-task prompts unchanged. No new task or dispatch.
5. Existing static workflow executes the new tests. No recurring workflow/schedule added.

## Actual read-only census
Recover evidence/scheduler_qa/CFB_HOT_SHEET_READINESS_QA_20261016T235756Z_READINESS.json @7158c485b4fb5e2775fa123ae4659f3fae70f93a.
Actual audit boundary2026-10-17T00:02:19.831293+00:00, canonical boundary2026-10-16T18:01:27Z:
-52 market-reference records missing a qualified consensus; fallback retained.
-52 line/price limits absent,52 practical cutoffs unverified.
-52 material and decision-rule reviews UNREVIEWED in this bounded profile; this is not proof no review exists anywhere.
-9 model exclusions;43 model reviews unreviewed, not automatically accepted from having numbers.
-3 elapsed current Friday quotes;0overdue open decisions at that audit clock. Saturday-morning13deadline remains00:30Z/19:30CT, unchanged.
-Caesars is NOT a recommendation blocker.

## Reproduction and producer correction
The first actual-clock CLI diagnostic rejected the older packet after Friday kickoff. Root cause: the strict LIVE publication guard was being reused to audit saved-view integrity at a later clock.
Readiness now validates packets at their own immutable saved boundary, then separately reports actual-clock elapsed/overdue exceptions.
Independent existing CI38984414775/job117252421643 reproduced the same failure in the previously installed whole-view QA step, after all new tests/frozen checks passed. Preserved original failure; no rerun upgrade.
New scripts/cfb_saved_publication_audit.py checks unique nonfuture saved boundary, authentic bootstrap, exact source digests and entire render at that boundary; separately reports actual-clock exceptions and always current_operational_acceptance=NOT_CERTIFIED.
Only the static saved-view audit uses that wrapper. Live compiler/renderer/gate stay strict;5tests prove stale live rejection, stale/overdue reporting, boundary/source/view tamper rejection. No clock or source was retimed.

## Verification and proof limits
- Initial broad local invocation failed because accepted archive fixtures/env were absent (4failures,5errors across453tests); no semantic acceptance was inferred. Exact configured GitHub artifacts10897612260/11423386216 were recovered and hashes independently matched772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf /674501a82f6eb207b58b30c483910304c881b3ce29ba2506258152455cb6047b.
- Full local suite with those actual archives:532tests PASS.22new readiness/consensus tests plus5saved-view tests; future test clocks are synthetic QA only.
- Independent existing CI38984594630/job117252990769 at a8df228155a7c557ae537625924b392d41324bc1 SUCCESS. Decoded logs independently read: new9/13/5test groups pass; PASS_SAVED_PUBLICATION_INTEGRITY_ONLY reports ELAPSED_CURRENT_QUOTES and NOT_CERTIFIED.
- All code/contracts/workflow and report independently fetched and matched after writes. Canonical marketf96df574ef69a6d1e21139c9c721bd1804295501, decision579ee3d16c76663428b3a00e49d4861a8ed512f1 and selected sheet441ec2a74dae91804b602ae8f6cfb1942f6545c7 remain unchanged.

## Remaining actual bottlenecks / next evidence
Qualified multi-book acquisition and current operator/source freshness are still OPEN; formatter tests do not acquire a consensus. Original line/price limits and material/decision-rule review need genuinely earned prospective records, not retroactive guesses. The neutral publisher still lacks a qualified richer recommendation/WAIT profile; this audit does not claim to implement it. Natural next scheduled Evening must reconcile the13Saturday-morning decisions by the preserved deadline and use these installed controls; missing actual runtime/source/decision evidence earns truthful incomplete status, not forced picks or extended clocks. Monitor remains sole primary publisher. Current sheet integrity is not full betting readiness.
Scientific/Champion/FIRST_FROZEN/REFRESH/execution/scorecard/money effect: NONE.
