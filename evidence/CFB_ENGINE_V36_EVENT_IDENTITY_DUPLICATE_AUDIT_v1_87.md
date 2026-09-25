# CFB Engine V36 Event-Identity / Duplicate Audit — v1.87
Date: 2026-09-25
Status: bounded precision diagnostic; no V37 and no semantic/model/source/gate/production promotion.

## Test-routine action
Continued v5 from verified/read-back v1.86. Global dependency reconsideration allowed one bounded event-identity/duplicate audit because V36 preserves exact event identity (game_id, id_play, team, stat) and this test can reject a duplicate-representation hypothesis without semantic invention.

## Frozen identity contract
V36 event identity is game_id + id_play + team + stat with exact deduplication before team-game aggregation.

## Audit
Checked conservative-shadow fumble-loss events in residual overcount team-games for:
1. exact duplicate event identities,
2. multiple fumble-loss events assigned to the same team on the same id_play,
3. shadow-only additions colliding with baseline-existing events under the frozen identity key.

Result:
- no exact duplicate event identities survive the frozen deduplication;
- no evidence that the residual overcount is explained by simple duplicate rows under the authoritative V36 identity contract;
- shadow-only additions are distinct event identities rather than duplicate copies of baseline events.

## Interpretation
The duplicate-representation hypothesis does not explain the residual overcount at the level V36 actually aggregates. A broader notion of "same football occurrence represented by multiple distinct play IDs" would require a new cross-play equivalence rule and cannot be inferred merely because text is similar or events are adjacent.

Do not collapse distinct play IDs into one event without independent evidence establishing that they represent the same physical fumble.

## Consequence
The cheap, evidence-backed duplicate audit is exhausted and negative. Combined with v1.83-v1.86:
- possession-change expansion rejected;
- broad explicit-text expansion mostly already harvested;
- overcount is split between baseline and shadow additions;
- beneficial and false-positive-associated shadow additions overlap semantically;
- exact event duplication does not explain residual overcount.

Marginal value of further broad V36 rule hunting is now low. Global dependency reconsideration should shift the active rebuild branch away from speculative turnover semantics unless a genuinely new authentic discriminator appears. RAW_TURNOVER_RATE remains OPEN as a bounded unresolved feature, not a license to fit control totals.

Next work should re-enter the highest-value executable Primitive Historical Coverage dependency under the same v5 ancestry/evidence-loss gates.

## Governance
V36 frozen inputs/artifact remain the evidence substrate. v1.86 readback verified before this checkpoint.
Latest integrated Library ZIP remains v1.73; v1.74-v1.87 are bounded repository evidence checkpoints.
Production/master routine v4; active test routine v5.
Production v1 untouched; v2 challenger/shadow; 2025 TEST protected.
Prediction cutoff UNKNOWN/fail-closed. Second-order lineage evidence boundary preserved.
No fitting/tuning/source/model/production promotion.
