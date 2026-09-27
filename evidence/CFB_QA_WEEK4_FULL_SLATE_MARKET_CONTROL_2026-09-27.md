# CFB QA Week 4 Full-Slate Market Control — 2026-09-27

Status: DIAGNOSTIC EVIDENCE — NO CHAMPION CHANGE
Parent: CFB_QA_WEEK4_CONTROL_CHECK_2026-09-27

## Scope
Systematic control test using all 44 Saturday 2026-09-26 FBS-vs-FBS FIRST_FROZEN games for which the CBS Week 4 betting guide provides a consistently recoverable pregame side. Archived CBS lines are independent QA evidence only; they are not backfilled into the canonical Market Monitor.

## Coverage and outcome
- Games joined: 44/44 Saturday frozen FBS-vs-FBS games.
- Champion winner direction: 30/44 correct (68.2%), 14/44 wrong.
- CBS market favorite/underdog direction relative to final winner: 39/44 correct (88.6%).
- Champion margin MAE: 14.607 points.
- CBS line margin MAE: 10.920 points.

## Champion-versus-market separation
Champion wrong calls (n=14): mean absolute Champion/market margin separation 11.257; median 8.134.
Champion correct calls (n=30): mean separation 7.848; median 7.532.

Large disagreement buckets:
- >=7 points: 25 games; Champion wrong 9/25 (36.0%); market winner direction correct 24/25.
- >=10 points: 14 games; Champion wrong 5/14 (35.7%); market winner direction correct 14/14.
- >=14 points: 7 games; Champion wrong 4/7 (57.1%); market winner direction correct 7/7.
- >=20 points: 2 games; Champion wrong 2/2; market winner direction correct 2/2.

Largest separations included Sam Houston/Texas Tech (35.07), UNLV/Akron (21.35), Southern Miss/Tulane (17.06), Notre Dame/Purdue (16.08), Texas/Tennessee (15.97), App State/NC State (14.30), and Illinois/Ohio State (14.15).

## Sample maturity
Feature-eligibility readback shows 86 of 88 team-sides had exactly 3 qualified prior games; two sides had 4. Therefore this Saturday control set is overwhelmingly a three-game early-season sample. Within-week sample-maturity stratification is not meaningful because there is almost no variation.

## Interpretation
The earlier failure-only hypothesis survives a proper control check: Champion/market separation was materially larger among wrong winner calls than correct calls, and the highest-disagreement buckets had elevated Champion miss rates. This supports using extreme independent-market disagreement as a QA diagnostic flag.

It does NOT establish that market information belongs in the Champion, that a 14-point threshold is calibrated for betting, or that opponent-strength adaptation is the proven causal mechanism. The control set is almost uniformly three prior games, so the suspected small-sample/opponent-strength mechanism must be tested across later weeks or through a sandbox counterfactual with opponent-strength stabilization.

## Hypothesis state
SUPPORTED FOR SANDBOX TEST DESIGN — early-season raw-stat comparability / opponent-strength adaptation.
SUPPORTED AS QA FLAG — extreme Champion-versus-independent-market disagreement.
NOT AUTHORIZED — Champion change, automatic market blending, betting threshold, recalibration, or promotion.

## Next governed work
1. Design a non-production Sandbox counterfactual that adds opponent-strength/small-sample stabilization without consuming outcome or user-wager evidence.
2. Evaluate it first on frozen historical/prospective-safe partitions under existing leakage controls.
3. Continue prospective Week 5 market persistence so later QA can test whether the disagreement signal repeats without historical reconstruction.
4. Preserve Champion v1.193 unchanged until a separate evidence and authorization gate is satisfied.

Scientific effect: none.
