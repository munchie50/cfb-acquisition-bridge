# CFB Engine V36 Recovery / Possession Contradiction — v1.80
Date: 2026-09-25
Status: bounded diagnostic checkpoint; no V37 and no semantic/model/source/gate/production promotion.

## Test-routine action
Continued v5 from v1.79. Isolated the 46 candidate-bearing residual replay=0 / official=1 fumble-loss undercount team-games and reconciled explicit recovery identity against possession-change evidence.

## Exact candidate population
46 target team-games contain 68 detected raw fumble-candidate rows.
All 68 have explicit recovery text that resolves to the target/fumbling team itself:
- recovery_same_team: 68 / 68
- recovery_other_team: 0 / 68
- unresolved recovery token: 0 / 68

Possession-change flag on those same rows:
- coposs FALSE: 40
- coposs TRUE: 28

At target-team-game level:
- 23 targets have no candidate row with coposs TRUE
- 14 targets have all candidate rows coposs TRUE
- 9 targets have mixed coposs TRUE/FALSE candidates

Candidate play-type structure:
- Fumble Recovery (Own): 35 rows (34 coposs FALSE, 1 TRUE)
- Fumble Recovery (Opponent): 27 rows (3 FALSE, 24 TRUE)
- Kickoff Return (Offense): 2 TRUE
- Punt: 1 TRUE
- Punt Team Fumble Recovery: 2 FALSE
- Sack: 1 FALSE

## Key semantic finding
The 24 rows labeled "Fumble Recovery (Opponent)" with coposs TRUE still have explicit recovery text resolving to the target/fumbling team. Examples include text such as a Louisville fumble "recovered by Lvile", Delaware "recovered by Delaw", Houston "recovered by Houst", etc.

Therefore:
1. play_type and possession-change metadata can contradict explicit recovery identity;
2. none of these 68 rows supplies direct text evidence that the target team lost that particular fumble;
3. converting these rows to losses solely because play_type says Opponent or coposs is TRUE would override stronger explicit recovery text and is not justified.

## Classification / consequence
The 46 candidate-bearing official undercounts are not currently evidence for a simple recovery-classification bug. They are source/control contradictions: the frozen play rows explicitly show same-team recovery while the independent team box reports at least one lost fumble for the team-game.

Do not "fix" these 46 by forcing loss classification from play_type/coposs. They require locating a different lost-fumble occurrence in the game or establishing a source semantic discrepancy at the aggregate-control layer.

Next highest-value turnover diagnostic: for these 46 team-games, search all same-game plays (including other possession roles and non-target-role fumble signals) for an unassigned opponent recovery / return-TD occurrence before treating the official aggregate discrepancy as irreducible.

RAW_TURNOVER_RATE remains OPEN.

## Governance
V36 frozen inputs/artifact remain the evidence substrate.
Latest integrated Library ZIP remains v1.73; v1.74-v1.80 are bounded repository evidence checkpoints.
Production/master routine v4; active test routine v5.
Production v1 untouched; v2 challenger/shadow; 2025 TEST protected.
Primitive Historical Coverage Gate OPEN. Prediction cutoff UNKNOWN/fail-closed. Second-order lineage evidence boundary preserved.
No fitting/tuning/source/model/production promotion.
