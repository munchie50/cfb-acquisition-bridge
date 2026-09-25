# CFB Engine V36 Shadow-Addition Precision Comparison — v1.86
Date: 2026-09-25
Status: bounded precision diagnostic; no V37 and no semantic/model/source/gate/production promotion.

## Test-routine action
Continued v5 from verified/read-back v1.85. Compared conservative-shadow-only events in residual overcount team-games against shadow-only events in team-games where the conservative shadow improved official reconciliation.

## Populations
Shadow-only events are conservative_shadow_events not present in the frozen baseline events_unique.

Within official-control team-games:
- 38 shadow-only events occur in residual overcount team-games.
- 61 shadow-only events occur in team-games whose absolute fumbles_lost error improved versus baseline.
- remaining shadow-only events occur in unchanged/exact/other-control contexts and are not used to manufacture a precision rule.

## Play-type comparison
Overcount shadow-only events:
- overwhelmingly Fumble Return Touchdown
- small residual special-teams / explicit-text edge classes

Improvement shadow-only events:
- also overwhelmingly Fumble Return Touchdown
- same core occurrence family that produced the largest V36 gain

Recovery/evidence structure overlaps materially between the two groups. No clean play_type-only or broad recovery-presence split separates the false-positive-associated additions from the beneficial additions.

## Key result
The principal V36-added occurrence class is both useful and imperfect. The residual overcount additions are not a clearly separable junk subtype that can be removed with a simple play_type exclusion without also discarding beneficial recoveries.

Therefore a V37 precision rule cannot safely be based on:
- excluding all Fumble Return Touchdown additions,
- excluding all shadow-only explicit-text additions,
- or a broad recovery-present / recovery-absent switch.

A narrower discriminator would need event identity / team-side semantics, duplicate representation, no-play context, or another independently evidenced feature.

## Consequence
No evidence-backed V37 rule emerges from the shadow-addition precision comparison. This materially lowers expected value of further broad turnover-rule iteration.

Global dependency reconsideration should now favor either:
1. event-identity/duplicate audit of the overcount additions if executable evidence supports it, or
2. shifting the active branch back toward another unresolved Primitive Historical Coverage dependency rather than overfitting V36.

RAW_TURNOVER_RATE remains OPEN.

## Governance
V36 frozen inputs/artifact remain the evidence substrate. v1.85 readback verified before this checkpoint.
Latest integrated Library ZIP remains v1.73; v1.74-v1.86 are bounded repository evidence checkpoints.
Production/master routine v4; active test routine v5.
Production v1 untouched; v2 challenger/shadow; 2025 TEST protected.
Primitive Historical Coverage Gate OPEN. Prediction cutoff UNKNOWN/fail-closed. Second-order lineage evidence boundary preserved.
No fitting/tuning/source/model/production promotion.
