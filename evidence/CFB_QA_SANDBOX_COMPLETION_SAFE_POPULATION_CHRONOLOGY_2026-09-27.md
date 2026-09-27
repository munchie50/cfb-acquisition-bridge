# CFB QA Sandbox — Completion-Safe Population Chronology Clarification — 2026-09-27

Status: PRE-EXECUTION CLARIFICATION / FROZEN BEFORE CANDIDATE PREDICTION OR OUTCOME JOIN

## Reason
The frozen S1/S2 transform requires population-baseline source information to be complete before the applicable cutoff. Accepted historical team-history features are proven strict by same-team kickoff ordering, but the new pooled cross-team population baseline creates overlapping-game risk.

The accepted v1.157 schedule producer filtered the upstream cfbfastR schedule on historical `completed`, but the historical `cfbd_game_info` schema exposes scheduled `start_date` plus completion state and does not expose a completion timestamp. The accepted projected schedules therefore cannot prove that a different team's earlier-kickoff game had completed by a later target kickoff.

A diagnostic over the 6,246 accepted Sandbox rows showed that cross-team overlap is material: 61.5% of targets have at least one population kickoff in the preceding hour, 70.3% in two hours, and 75.5% in six hours. No fixed game-duration lag is therefore invented.

## Completion-safe cutoff
For any target/source instant T, define the population-baseline cutoff as 00:00:00 UTC on T's UTC calendar date.

A population game is eligible for B_F(T) only when:
- same season as T;
- its kickoff is strictly earlier than that UTC-date cutoff;
- the applicable primitive is complete/valid under the accepted v1.172 substrate.

This intentionally discards all same-UTC-date games. It does not infer venue timezone, local date, game duration, or completion time.

## Coverage proof
Applied to the accepted v1.179 Sandbox population:
- eligible target games: 6,246;
- target games with a usable completion-safe population baseline: 6,246;
- target games with zero completion-safe population baseline: 0;
- minimum qualifying prior population games: 23.

No 2025 row was accessed.

## S2 handling
The frozen S2 rule remains one-step and uses only valid source-game opponent residuals. The same completion-safe cutoff applies when forming the opponent population baseline at each source game's kickoff.

Pre-execution audit:
- accepted target team-sides: 12,492;
- target sides with at least one valid completion-safe S2 source context: 12,480;
- target sides with prior team history but zero valid completion-safe S2 context: 12;
- every one of those 12 has exactly one prior team game.

For those 12 sides, S2 fails closed. No opponent residual is imputed and no S1 value is silently relabeled as S2.

## Locks unchanged
- S0 remains exact Champion control.
- k grid remains {1,2,4,8}.
- frozen S2 feature mapping/sign remains unchanged.
- no recursive S2.
- target game, later games, outcomes, market, wagers, and execution state remain forbidden construction inputs.
- 2025 TEST remains forbidden.
- Champion v1.193 and FIRST_FROZEN remain unchanged.
- no promotion or production mutation is authorized.
- candidate predictions must still be hashed/frozen before any outcome join.

This clarification narrows source eligibility to satisfy the already-frozen completion requirement; it does not relax that requirement or introduce a result-driven choice.
