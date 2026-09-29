# CFB QA S2_K1 — v4 Source-Context Acceptance — 2026-09-29

Status: **ACCEPTED QA SOURCE-CONTEXT SUBSTRATE / CAPABILITY ONLY**
Parent: evidence/CFB_QA_SANDBOX_S2_K1_SOURCE_CONTEXT_CONTRACT_2026-09-28.md
Audit basis: repository main at b9a526cdbfec6b5cd06cb680d06a24def7c933ff; exhaustive recursive tree (348 entries, truncated=false), direct authority readback, retained artifact downloads, recovered executable ancestry, and independent numeric reconciliation.
This is infrastructure acceptance, not S2_K1 scientific acceptance, prospective prediction acceptance, promotion, or production use.

## Exact execution and retained identities
- Producer: scripts/cfb_qa_s2_k1_source_context_companion_v4_2026_09_29.py
- Creation commit: 5b44f96d626f6db8923b626eab71cfeab3317ddc
- Git blob: abc843e7f86779b3f55f16bd3c75bbc4e450e094
- File-byte SHA-256: 8500b5365ccc374105156106501f2335be80de4bde7d97bb82fe3c47cc92c1f0
- Corrected static run/job: 36637684023 / 109642221487; head 48b87caeb9449166eda78542892c3af8aeabcba8; SUCCESS. Exact marker S2_K1_SOURCE_CONTEXT_V4_STATIC_PASS followed by the file-byte SHA above.
- Real run/job: 36637810698 / 109642643453; head b9a526cdbfec6b5cd06cb680d06a24def7c933ff; SUCCESS.
- Artifact: 11065575217, cfb-qa-s2-k1-source-context-v4-real
- Downloaded ZIP SHA-256: f1104a7fc509f2ef9ee1825698e0210bfd232c9acfafb34635bbd75f93567c8f; exactly matches GitHub digest and job logs.
- Cutoff: 2026-09-29T11:39:08.824054+00:00

| File | Rows | SHA-256 |
|---|---:|---|
| mechanical_primitives.csv | 662 | 9324b82fb7664cb7659cd9bb5fa56615cec7e6eef64cab34ef066e9097cbb563 |
| derived_primitives.csv | 662 | c0925c5f199d94bc72671d3c07bc782bac7d374c37b6bc453fdeddcad3683930 |
| source_context.csv | 4,355 | 12fdc0ab7b32f136a8b4898a0db0a980162b908fed3d883d6fe953a96d2cdc60 |

All CSV hashes match manifest. Manifest remains immutable EXECUTED_NOT_ACCEPTED; this separate post-run acceptance record supplies the disposition. Exact flags: s2_predictions_produced=false, target_outcomes_joined=false, market_joined=false, accepted_target_side_crosscheck=true. Primitive ancestry blob: 37c05aba201d3c2935b5d2b646437552949766fd.

## Input ancestry and locks
Consumed retained raw artifact 11031055060, ZIP 1495f453e5d9f262baddfa2b7ad21d2d9e8d5f8c2436f058f88fcb6ebc6d8d68.
Schedule 9847952ba52279318018a259c07197df23392086f03bd6a308fd2cf60e83cd2c.
PBP eab0562fb2f9dd9c65cf1457c469d656d9247212694370cac10c789e673a2ddb.
Raw ZIP and every internal manifest hash independently reproduced. No upstream reacquisition.
Same-cutoff S0 target-side artifact 11064541770, ZIP 78b58979a7a1a81bd3af0473c65fb760a94b73421e0ee97aa51adce1a540a259, substrate eb2ea9a24831fbb485070c038118aedd11934951f28d02484d30654b0e067e75.
See CFB_QA_V1_246_REAL_TARGET_SIDE_ACCEPTANCE_2026-09-29.md.

## Independent semantic reconciliation
- All 1,114 target-side rows reconciled to all 557 projected targets and original home/away identities. Six zero-history sides were explicitly checked as zero-context cases. Exact prior source-game ID sets and counts match for every target side, not merely rows appearing in context.
- Target kickoff is future at cutoff. All primitive rows are season 2026 and strictly before cutoff; all 331 source games are completed. No source primitive game ID intersects a target ID.
- Zero duplicate target/team/source identities and zero source-before-target chronology violations. Opponent and source kickoffs match exactly; opponents are the other original schedule team.
- All opponent counts are finite, integer, nonnegative and independently reproduce strict-prior histories. 1,510 context rows have zero opponent history.
- All 43,550 paired raw values, all 43,550 population baseline values and all 43,550 feature-specific availability flags independently reproduced at rtol=0/atol=1e-12, allowing matching unavailable NaNs.
- Every history completion flag independently reproduced from prior PBP availability and applicable primitive completeness. Real context contains zero incomplete mechanical/derived history rows. Synthetic acceptance remains necessary evidence for unavailable/incomplete edge cases; do not claim this real sample exercises them.
- Each of ten mapped features has 4,245 valid context rows and 110 unavailable baseline/context rows. Unavailable context remains unavailable; no residual imputation or predictions were performed.
- Mechanical/derived numeric primitives exactly reproduce the actual recovered v1.172 producer block using schedule-filtered retained PBP, including established aliases, event zero-fill and source-order drive starts.

## Explicit equivalence points
1. The entire BASE2017 membership/canonicalization block through relevant-FBS filtering is byte-identical to accepted v1.246. The historical universe is restricted to season 2026 before any team-only grouping, so season is not lost by grouping.
2. Canonicalized names are membership filters only. Original home_team/away_team/team strings are history and opponent identities, exactly matching v1.246. No alias-based history merge is introduced.
3. v1.172 filters PBP to schedule IDs before aggregation; v4 aggregates supplied PBP then left-merges on schedule-derived game/team identities. Group operations never cross game ID, so off-schedule PBP cannot enter retained primitive/history rows. This is both structurally established and demonstrated by exact primitive reproduction from the schedule-filtered v1.172 builder.
4. Frozen MAP and component numerator/denominator tables equal the accepted historical generator. Baselines use UTC calendar-day-normalized cutoff, strict earlier-day rows, completion-safe primitive pools and pooled numerators/denominators. All same-day games are excluded. No simple average of feature rates, cumulative-history pool substitution or recursion is used.
5. Zero-history context validity requires its paired baseline; positive-history validity additionally requires BOTH history-complete flags and finite paired raw value. No unrelated-feature global availability gate exists.
6. rest_days baseline remains the mean of strict-prior side intervals before the normalized cutoff; it is not one of the ten S2 paired corrections. This branch was reviewed against frozen code; real artifact has no rest_days baseline column and no S2 consumer was executed.
7. Source scores are authorized strictly prior primitive components, not target outcomes. Primitive CSVs retain unused historical schedule metadata, including home_winner/away_winner and ranks. Therefore this acceptance does NOT claim the primitive files contain no outcome-bearing source columns. Every such row is restricted to prior source games; winner/rank fields are unused. No market, odds, spread, wager, execution, prediction or target-outcome field exists on any emitted CSV. A future consumer must whitelist the frozen primitive/context fields and never consume unused schedule metadata.

## Limitations and non-effects
Historical original first-freeze raw RDS replay remains unavailable and is not reclassified. These retained 2026 bytes form a separate immutable structural-QA boundary.
No S2 predictions, target-outcome joins, market joins, 2025 TEST access, refit, recalibration or scientific design change occurred. Champion v1.193 coefficients/scaling and FIRST_FROZEN are unchanged.
This acceptance closes source-context infrastructure only. The consumer/freeze remains unexecuted.

## Reproducible audit evidence and attempts
Evidence/audits contains the reconciliation script, S0 check script and machine-readable report. Reproduce in a scratch directory with audit/raw, audit/v4, audit/s0 extracted from the three exact ZIPs and recovered/scripts containing exact repository source bytes at the audited head; place the audit scripts at audit/reconcile.py and audit/s0_check.py. Dependencies: pandas, numpy, pyarrow, pyreadr. Do not generate predictions to reproduce this audit.
Primary report SHA-256: d9c81717272978b624d510cad773b195374928606b47fe0746d9f5616d8c483d.
Audit-script SHA-256: 91cc517c5a95e103915ff04d07baf2288d4b82f876f095d6c40759a8c1d1c209.
S0-check script SHA-256: 18746ceb634589297ee235ada220cb227d5b2e5d05812ae209d52999accdd160.
A first local audit attempt stopped at source SHA because patch staging added a trailing newline. Exact connector content bytes were then restored; SHA-256 and all four Git blobs reproduced. This was an audit staging defect, not v4 source drift; no repository executable changed. Initial sandbox dependency installation failed due network restriction; approved installation succeeded. Both failed attempts remain recorded here.

## Dependency reconsideration and stop
Contracts directly reread: prospective S2_K1 continuation, v1.216 weekly lineage, v1.218 no-op disposition.
First accepted freeze cutoff was 2026-09-26T03:47:37.497112+00:00; v1.218 minutes-later preflight was NOOP. Current date 2026-09-29 remains within that weekly cycle. The 2026-09-29 raw-source/substrate runs are structural QA and do not supply a cadence exception or accepted operational prospective refresh.
Disposition: CADENCE WAIT / NO NEW PROSPECTIVE FREEZE AUTHORIZED NOW. No current mutable-source acquisition or extra snapshot was manufactured.
At the next governed weekly refresh point, run fresh preflight and retain exact qualified raw bytes; if NOOP, stop. Consumer construction/generation may advance only after this cadence/preflight decision under the user continuation boundary. Use same-cutoff accepted S0 and source-context substrates, exact k=1 semantics, separate S2 artifacts and frozen DEPTH_1_2/DEPTH_3_4/DEPTH_5_PLUS. Outcome scoring needs separate authority.
Independent-work sweep during this wait closed the real S0 substrate acceptance and integrated readiness/checkpoint/attempt history. Re-running successful gates, refitting, extra refreshes and outcome scoring have no authorized material value.
Learning trigger installed and demonstrated: when a run materially outruns recovery/readiness prose, reconcile terminal artifacts and then update all recovery pointers in one serialized evidence commit before yielding. This prevents stale NEXT instructions from reopening accepted dependencies.
