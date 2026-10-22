# CFB production recovery audit — October 22, 2026

- recovery_cycle: CFB_PRODUCTION_RECOVERY_20261022T181612Z
- manual_primary_producer_cycle: CFB_MARKET_MONITOR_20261022T182720Z
- observed_audit_clock_utc: 2026-10-22T18:35:58Z
- method: candidate Test Routine v6; Production Routine v5 unchanged
- classification: PARTIAL_PROSPECTIVE_RECOVERY / FULL_FOOTBALL_REVIEW_INCOMPLETE

## Starting state and correction

Main 4cfabd19a6e22d1241e6cd82e99de9dcadc3568b had no Week8 market/decision packet or sheet. Repeated natural runs failed because initial bootstrap required every target to remain future after four Tuesday/Wednesday identities had elapsed. The selected display was still October17 Week7. User directed production catch-up using the test routine.

PR3 c45f01eab20e6640bbcd9d97573a7a65a8eb9c72 implements the explicitly bound October22 prospective disposition. The ordinary path still rejects initial elapsed targets. The bounded recovery preserves all56 identities and four immutable HISTORICAL_GAP records; it cannot create a pre-event PASS/recommendation, erase gaps, enlarge the gap set or convert later missed future decisions. Compiler, full-history validation, renderer and readiness agree on the gap semantics. Existing full CI39831164274/job120007357948 passed before live operational use.

The actual primary-producer proposal was compiled at18:29:11Z using genuinely retained complete CBS response recovered by18:20:28Z. Source freshness bracket was under15minutes at proposal. Quote roles remain mixed-book fallback; opaque icons do not certify operators, consensus or venue execution. Final/Open columns remain quarantined. No old capture was relabeled current.

## Expected versus independently recovered actual

| Boundary | Expected | Actual |
|---|---|---|
| Identity union | 56 exactly once in every market/decision packet and rendered sheet | PASS |
| Original model | 49 predictions, seven exclusions, 147 unchanged numeric fields | PASS against independently hashed original archive |
| Permanent missing history | Four actual missed Tuesday/Wednesday targets, no retrospective decisions | Four HISTORICAL_GAP; immutable and outside pregame work |
| Future population | 52, including exclusions and no-bet-for-now rows | 52 review-required; queue is not proof of research |
| Current decisions | Honest current earned scope | Seven original-exclusion PASS; two Thursday no-bet-for-now PASS; 43 INCONCLUSIVE |
| Canonical history | Exact Week7 prefix and authentic retained first observations | PASS, prior bytes preserved |
| Current view | One selected Week8 source-derived sheet | PASS current navigation/decision binding and whole-render audit |
| Full research/Top10 | Substantive all-style/material review, timely qualified recommendations | INCOMPLETE; no qualified ranking or recommendation claimed |

Nine PASS does not mean nine completed no-edge judgments. Seven are binding original-model exclusions. The two eligible Thursday rows record administrative no-bet-for-now because recommendation qualification, especially an independently established practical execution cutoff, is incomplete. AppState points and Memphis spread warrant continued prospective review; no stake, acceptable number or actual wager is created. Liberty remains originally excluded. Remaining43 eligible future rows are explicitly unfinished. Standard-board source inspection does not establish alternate/team-total availability elsewhere. No preferred parlay is earned.

## Persistence and readback

- market: 9a3984a83a6475222e5758543beeaea4df599d19; accepted commit bb1e69328e75c79574c9fa72bcb456cbf9d68558; immediate main identity and complete independent blob readback matched proposal.
- decision: 54936676d43466dc03ff4925424c1f7a5a6b7217; commit664a65599a4c767fbbb9c8624e89c87412a4cd6d; independent complete main readback matched.
- sheet: evidence/operational/CFB_WEEK8_HOT_SHEET_2026-10-22_1330CT.md; c34489568e920df6f65fb1005f2cebfa39b2be3b; independent complete readback matched.
- first selecting index: 250d1b636dc3bfb34f62a110bc109f48d540fa3e atdf2cf557e4b2b03e52ec9790a429d43a7094bc3d; complete independent readback matched;48consumer pointers independently verified. Later navigation may link this audit without changing operational state.
- market append101811bytes; decision append43408bytes; planned metadata proved prior-byte preservation before writes.
- execution75caee4052e02ea7d2453d1d37fd3866e13ecc07, money3aebcbdcc535479c29c31f18073cba09f59aab01, accepted-prediction pointer467e21006cc51fcc46b9577d7f98f301f9e63f84 unchanged. Scorecard c9203836e0be102593a8eb7d508f7d8bd4c05bd2 unchanged in this work.

## Structural failure discovered after real advancement

Workflow39832296476/job120011289062 failed at the historical Week8 fixture after the canonical append. historical() compared an absolute requested path against Git's repository-relative object names. The unchanged-current-file shortcut had hidden this defect. Existing accepted history was present; no data reacquisition, model regeneration or gate weakening was needed.

PR4 dd573447bdd831347b0988ac5b6ce0ca3d04a622 normalizes the repository root/path for both history query and exact blob/path comparison. Four regressions cover advanced absolute and relative canonical paths, wrong-path rejection and a different process working directory. Three valid recovery cases failed before correction. Afterward136affected publication checks and all642local tests pass using independently authenticated original/refresh archives. Full independent post-correction CI39832712036 and final selected-state CI must be separately reconciled in terminal closure; a local PASS does not certify them. Original failed workflow remains failed.

Other preserved local failures: an exclusion-reason table separator was rejected before any canonical write and replaced by ordinary prose without changing the original model exclusion; early downstream checks found no proposal because that compile had stopped. An initial broad test attempt lacked the refresh archive; after authentic download/hash verification its24adapter checks passed and the final complete642test suite passed. These are not source/model changes or reasons to upgrade earlier natural incomplete runs.

## Learning and remaining work

Benefit: manual prospective delivery is no longer blocked by four irrecoverable earlier decisions; actual current56-row output and original field integrity demonstrated. Cost: bounded recovery-specific handling plus continued manual rescue;43eligible games still lack substantive research and no Top10 has been earned. Net: helpful for recoverability/display; betting usefulness and unattended reliability remain UNPROVED. Keep the bounded correction; stop and correct if a gap becomes actionable, history changes, identities disappear or later missed decisions are concealed. Correcting canonical path normalization removes a real advanced-state failure rather than pinning fixtures to current live bytes.

Next highest-value work is prospective all-game/all-style football review, with immediate remaining Thursday reevaluation when genuine practical timing and required sources are established, followed by Friday and Saturday windows. Preserve all original limits/cutoffs if subsequently earned. No invented planning cutoff, price threshold, probability, EV, wager, settlement or capital allocation. Natural next existing Monitor/Evening/Health/WeeklyQA must consume the typed Week8 state in their existing ownership roles; no new task or schedule was created or changed. Keep all historical incomplete cycles and the21missed Week7 final windows open. Champion/FIRST_FROZEN/REFRESH governance and BigNine state unchanged.
