# CFB Engine V36 Residual Overcount Classification — v1.85
Date: 2026-09-25
Status: bounded precision-audit checkpoint; no V37 and no semantic/model/source/gate/production promotion.

## Test-routine action
Continued v5 from verified/read-back v1.84. Global dependency reconsideration selected residual overcount audit before another undercount expansion because precision protection is required before considering any new occurrence rule.

## Population
Conservative-shadow fumbles_lost overcounts: 57 team-games.
Overcount depth:
- replay exceeds official by 1: 49 team-games
- by 2: 4
- by 3: 4

The 57 overcount team-games contain 118 conservative-shadow fumble-loss events.

## Event-origin structure
Reconciled conservative_shadow_events to the frozen baseline events_unique:
- 80 / 118 overcount-team-game events already existed in the baseline event set.
- 38 / 118 are conservative-shadow-only additions from the explicit-text / implicit-return-TD expansion.

At team-game level:
- 29 / 57 overcount team-games contain at least one shadow-only added event.
- 28 / 57 contain only baseline-existing loss events.

Therefore the residual overcount problem cannot be attributed solely to the V36 occurrence expansion. Roughly half of overcount team-games are already overcounted using baseline-existing event semantics.

## Precision implication
A future V37 cannot be evaluated only on recovered undercounts. It must preserve or improve precision across two distinct overcount sources:
1. baseline-existing loss classifications, and
2. shadow-added occurrence classifications.

Blindly adding more occurrence classes risks increasing the 29 expansion-exposed overcount team-games, while doing nothing for the 28 baseline-only overcounts.

## Consequence
Before any V37 semantic change, candidate rules need event-level precision auditing against both groups. The highest-value next turnover diagnostic is to classify the 38 shadow-only events inside overcount team-games by play_type/recovery evidence and compare them with shadow-only events that improved undercount/exact reconciliation. This can identify whether the V36 gain contains a separable false-positive subtype.

RAW_TURNOVER_RATE remains OPEN.

## Governance
V36 frozen inputs/artifact remain the evidence substrate. v1.84 readback verified before this checkpoint.
Latest integrated Library ZIP remains v1.73; v1.74-v1.85 are bounded repository evidence checkpoints.
Production/master routine v4; active test routine v5.
Production v1 untouched; v2 challenger/shadow; 2025 TEST protected.
Primitive Historical Coverage Gate OPEN. Prediction cutoff UNKNOWN/fail-closed. Second-order lineage evidence boundary preserved.
No fitting/tuning/source/model/production promotion.
