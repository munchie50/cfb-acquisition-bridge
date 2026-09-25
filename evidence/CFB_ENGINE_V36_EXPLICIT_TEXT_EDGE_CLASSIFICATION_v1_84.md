# CFB Engine V36 Explicit-Text Edge Classification — v1.84
Date: 2026-09-25
Status: bounded diagnostic checkpoint; no V37 and no semantic/model/source/gate/production promotion.

## Test-routine action
Continued v5 from verified/read-back v1.83. Reconciled the preserved V36 occurrence-expansion rows against the conservative-shadow event output to classify explicit-fumble-language detector edges.

## Preserved edge population
V36 occurrence_expansion_new_rows contains 116 rows newly found by broad explicit fumble-language occurrence expansion beyond the baseline detector.

Classification:
- 89 / 116 have an explicit resolved recovery team.
- 27 / 116 have no resolved recovery team.
- 87 / 116 are Fumble Return Touchdown rows.
- 29 / 116 are other play types.

Conservative shadow already converted the evidence-supported subset into events:
- 78 / 116 edge rows appear in conservative_shadow_events.
- 38 / 116 do not.

## Why 38 remain excluded
The excluded set is dominated by missing resolved recovery identity and/or insufficient evidence that the fumble was lost by the inferred side. Broad explicit-fumble language alone is not enough to assign a loss.

The V36 conservative rule intentionally requires stronger evidence (explicit recovery semantics, the separately bounded implicit Fumble Return Touchdown case, or existing frozen fallback semantics) rather than treating every textual fumble as a lost fumble.

## Consequence
The explicit-text edge audit does not expose a second large, mechanically safe rule comparable to the V36 implicit Fumble Return Touchdown correction. Most of the evidence-backed edge gain is already captured by the conservative shadow.

The remaining 38 excluded rows should not be bulk-promoted. Any further rule must be derived from a narrower semantic class with recoverer/loser identity evidence. This materially lowers the expected value of launching V37 from another broad occurrence expansion.

Global dependency reconsideration after this checkpoint should compare:
1. a targeted audit of the 38 excluded explicit-text rows for a small recoverable semantic subtype,
2. residual overcount analysis to protect precision,
3. or shifting effort back to the Primitive Historical Coverage Gate if the turnover branch's marginal evidence yield is now lower.

RAW_TURNOVER_RATE remains OPEN.

## Governance
V36 frozen inputs/artifact remain the evidence substrate. v1.83 readback verified before this checkpoint.
Latest integrated Library ZIP remains v1.73; v1.74-v1.84 are bounded repository evidence checkpoints.
Production/master routine v4; active test routine v5.
Production v1 untouched; v2 challenger/shadow; 2025 TEST protected.
Primitive Historical Coverage Gate OPEN. Prediction cutoff UNKNOWN/fail-closed. Second-order lineage evidence boundary preserved.
No fitting/tuning/source/model/production promotion.
