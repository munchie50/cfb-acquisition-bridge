# CFB Engine — Phase 4 Challenger-A Conservative 2022 Temporal Exclusion Contract v1.127

Status: FROZEN PROSPECTIVELY — FAIL-CLOSED TRAIN POPULATION CONTROL
Scope: Challenger A only
Production effect: NONE
2025 TEST: PROTECTED / UNTOUCHED
Fitting: NOT AUTHORIZED

## Evidence boundary

v1.24 proves bounded 2022 primitive corrections for five team-games:
Auburn 77→76; Mississippi State 67→66; Georgia Tech 68→66; South Carolina 68→65; Washington 77→76.

v1.25 proves those corrections propagate through direct same-team chronology to exactly 43 later 2022 TRAIN target-team rows:
Auburn 9; Mississippi State 8; Georgia Tech 9; South Carolina 8; Washington 9.

v1.52–v1.54 prove authoritative prediction cutoffs for that bounded population were not recovered and schedule start may not substitute. The original serialized 43-row key ledger has not been recovered from surviving authority.

## Source-game anchors

The preserved 2022 control chronology identifies the relevant Week-3 team-games:
- Auburn — Penn State: game_id 401403882
- Mississippi State — LSU: game_id 401403885
- Georgia Tech — Ole Miss: game_id 401403886
- South Carolina — Georgia: game_id 401403888
- Washington — Michigan State: game_id 401403994

These IDs are chronology anchors for the conservative rule, not a claim that the lost v1.25 serialized target-row ledger was recovered.

## Frozen conservative rule

For Challenger-A TRAIN construction only:

For each affected team, exclude that team's target-side observation for every 2022 game strictly later in authoritative schedule chronology than its source-game anchor.

Do not exclude the source game merely because it is the source anchor: history-derived features for that target are based only on completed prior games.

When a target game contains one affected side, the game-level Challenger-A row fails closed because Challenger A requires complete qualified inputs for both sides.

If both sides are affected, count the game once at game level while retaining both team-side exclusion reasons in the eligibility ledger.

No schedule kickoff timestamp is treated as a prediction cutoff. Chronology is used only to define 'strictly later than the source game' for this conservative population exclusion.

## Verification requirements

Before dataset freeze:
1. enumerate excluded team-side keys deterministically from accepted 2022 chronology;
2. verify counts against v1.25: 9/8/9/8/9 = 43;
3. report unique game-level exclusions separately;
4. retain source anchor, team, reason and authority references per exclusion;
5. prove no 2023–2024 VALIDATION row is excluded by this 2022-only rule;
6. prove no 2025 row is present anywhere in the development matrix.

If the deterministic chronology rule does not reproduce the v1.25 counts exactly, STOP and do not broaden or shrink exclusions ad hoc.

## Gate effect

This contract resolves how Challenger A handles the known 2022 temporal-qualification uncertainty without inventing prediction cutoffs or falsely labeling reconstructed target IDs as recovered historical evidence.

The next executable step is to apply this rule to the accepted v1.109 + v1.115 feature join, attach authoritative targets, verify the 43 team-side count and unique game exclusions, then freeze/hash the exact dataset/config and run the final leakage/market-blind audit.

No fitting is authorized by this checkpoint.
