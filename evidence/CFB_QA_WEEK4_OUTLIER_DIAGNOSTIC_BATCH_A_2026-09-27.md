# CFB QA Outlier Diagnostic — Week 4 Batch A — 2026-09-27

Status: DIAGNOSTIC EVIDENCE — NO CHAMPION CHANGE
Parent: Weekly Beta Learning Review v1.244

## Scope
First-pass diagnosis of the five largest Week 4 absolute margin errors identified by v1.244. Frozen predictions remain immutable. Postgame evidence is used only to diagnose error after the fact, never to rewrite the prediction.

## Frozen prediction and outcome
- UCLA at Maryland: Champion Maryland by 7.251; final UCLA 54, Maryland 3; absolute margin error 58.251.
- Tulsa at Arkansas: Champion Arkansas by 12.635; final Arkansas 34, Tulsa 6; absolute margin error 40.635.
- UNLV at Akron: Champion Akron by 7.852; final UNLV 38, Akron 10; absolute margin error 35.852.
- Sam Houston at Texas Tech: Champion Texas Tech by 0.567; final Texas Tech 49, Sam Houston 14; absolute margin error 35.567.
- Boise State at Western Michigan: Champion Western Michigan by 4.895; final Boise State 32, Western Michigan 7; absolute margin error 29.895.

## Feature-snapshot observations
The frozen inputs themselves show why several Champion opinions were plausible from the model's narrow statistical view, while also exposing an early-season comparability risk.
- Sam Houston entered the snapshot with stronger raw points-against, defensive yards/play and defensive success-rate-allowed than Texas Tech; the Champion therefore treated the matchup as near-even.
- Tulsa entered with much stronger raw points-against and defensive efficiency than Arkansas, compressing Arkansas's projected advantage.
- Akron's frozen offensive success rate exceeded UNLV's despite weaker scoring, helping produce an Akron-favored prediction.
- Western Michigan's frozen defensive yards/play and Boise State's defensive explosive-play rate created support for a Western Michigan lean despite Boise's stronger scoring/offensive yards-play profile.
- UCLA/Maryland inputs were comparatively strong on both sides and did not imply the eventual 51-point UCLA win.

## Postgame game-shape observations
- Texas Tech's 49-14 margin included two interception-return touchdowns on consecutive Sam Houston throws. This is unusually high-leverage defensive scoring and is a variance component, but Texas Tech was also described as a nearly five-touchdown market favorite, so variance alone cannot explain the Champion's near-pick'em view.
- UNLV outgained Akron 493-301 and intercepted Akron three times. The miss was not merely a one-play outcome; UNLV materially controlled the game.
- Boise State led Western Michigan 32-0 before a late touchdown and held Western Michigan to 223 yards and 2-of-11 on third down. The miss reflects sustained game control rather than only late-score variance.
- Arkansas led Tulsa throughout and won 34-6. The frozen raw team statistics appear to have materially understated Arkansas relative to Tulsa.
- UCLA's 54-3 win over Maryland is too large to classify from final score alone; deeper pre-event opponent-strength/roster/context review is required.

## Classification
HYPOTHESIS OPEN — EARLY-SEASON RAW-STAT COMPARABILITY / OPPONENT-STRENGTH ADAPTATION.
Evidence from multiple large misses is consistent with the Champion giving too much authority to small-sample current-season raw efficiency without enough context for opponent quality and rapidly changing team strength. This is not yet a confirmed diagnosis.

HYPOTHESIS OPEN — HIGH-LEVERAGE TURNOVER/DEFENSIVE-SCORE VARIANCE.
Relevant to Texas Tech/Sam Houston and UNLV/Akron, but insufficient as a common explanation for the batch.

## Required next evidence
1. Compare pre-Week-4 opponent quality and game samples for both teams in each outlier.
2. Check whether the same raw-stat comparability pattern appears among correctly predicted Week 4 games; avoid selecting only failures.
3. Quantify error by number of prior 2026 games / early-season sample maturity.
4. If pattern survives controls, create a Sandbox hypothesis for opponent-strength/small-sample stabilization. Do not modify Champion directly.

Scientific effect: none.
