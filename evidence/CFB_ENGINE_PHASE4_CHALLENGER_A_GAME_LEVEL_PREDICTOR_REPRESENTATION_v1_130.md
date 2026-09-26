# CFB Engine — Phase 4 Challenger-A Game-Level Predictor Representation Contract v1.130

Status: FROZEN PROSPECTIVELY — BEFORE MODEL PERFORMANCE
Scope: Challenger A / v2 shadow only
Production effect: NONE
2025 TEST: PROTECTED / UNTOUCHED
Fitting: NOT AUTHORIZED
Parent: v1.129

## Authority search result

Targeted recovery did not locate a higher-authority frozen Phase 4 rule specifying whether accepted team features must enter the first game-level challenger as home/away copies or engineered home-minus-away differentials. The recovered redesign/evaluation authority requires a market-blind, simple, explainable, reproducible challenger but does not freeze this representation.

Therefore this is a genuine prospective Challenger-A design decision and is frozen now, before model performance is observed.

## Frozen representation

Use SIDE-PRESERVING HOME/AWAY COPIES of the accepted team-level feature values.

For each canonical game, join exactly one schedule-designated home team row and one schedule-designated away team row.

For every accepted team-level numeric feature F, create:
- home_F = qualified value for canonical home team
- away_F = qualified value for canonical away team

Do NOT replace these with F_home - F_away, ratios, sums, averages, interactions, manually signed transforms, or other engineered matchup features in Challenger A.

Rationale:
- preserves the accepted feature values without adding an unfrozen transformation;
- lets the frozen linear/GLM family estimate side-specific coefficients transparently;
- preserves canonical schedule home/away identity required by v1.124;
- remains reconstructable and auditable;
- avoids choosing a differential transformation whose predictive effect has not been prospectively justified.

## Venue representation

The accepted team-level home_away_neutral field is not duplicated blindly as two unrelated categoricals.

The executable builder must derive one deterministic game-level venue state from authoritative schedule identity:
- HOME when canonical home team is home and game is not neutral;
- NEUTRAL when authoritative schedule marks neutral_site;
- any unresolved/inconsistent venue identity fails closed.

No market favorite/underdog identity may substitute for canonical home/away identity.

## Rest and all other side-specific features

Rest-days remains side-specific:
- home_rest_days
- away_rest_days

All accepted offensive/defensive rates, scoring, pace/volume, efficiency, interception, explosiveness, success and starting-field-position values remain side-specific home/away copies.

## Exact predictor family

Challenger A game-level predictors consist only of the two side-preserving copies of the 18 accepted v1.123 features, except that team-side home_away_neutral is represented once as the deterministic game-level venue state above.

Thus:
- 17 numeric/side-specific accepted features x 2 sides = 34 side-specific predictor columns;
- plus one deterministic categorical game-level venue state;
- no engineered differential/sum/ratio/interaction columns.

The executable config must list the exact 34 numeric column names/order and the categorical venue encoding before fitting.

## Eligibility

A game is eligible only when:
- canonical home and away identity resolve uniquely to accepted feature rows;
- all required numeric values for both sides are qualified/nonmissing under v1.126;
- venue state is qualified;
- target is available from authoritative schedule under v1.124;
- temporal qualification passes under corrected authority v1.129 / v1.127-v1.128.

If either side fails, the one game-level row fails closed.

## Decision-before-evidence lock

This representation may not be changed after viewing Challenger-A TRAIN/VALIDATION performance.

A differential, symmetric, ratio, interaction, or other representation becomes a separately versioned prospective challenger and may not be presented as the same Challenger A.

## Next gate

Build and freeze the exact schedule-authoritative game-level dataset/config; emit row-level exclusion ledger; apply 42 v1.128 temporal game exclusions; prove 2025 absence and market blindness; hash/persist/read back all artifacts; then perform final pre-fitting readiness reconciliation.

No fitting is authorized by this checkpoint.
