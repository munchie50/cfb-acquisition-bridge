# CFB Engine — Challenger B 2025 Descriptive Holdout Diagnostics v1.201

Status: **PASS — DESCRIPTIVE READBACK ACCEPTED / NOT A TUNING OR PROMOTION INPUT**
Parents: v1.198, v1.199
Diagnostic run: **36215718892**
Artifact: **10897725841**
ZIP digest: `sha256:8e9c8acfdb9d03d250ab602da1af3b3c840f672e541037343b4519b82429d79f`

The readback consumed only the already accepted v1.196 scoring artifact and reported the prospectively generated stability slices. It did not refit, recalibrate, redesign, select thresholds, join markets, or alter predictions.

## Venue
HOME n=734:
- margin MAE 14.144373; bias -1.481964
- total MAE 12.657847; bias +0.394442
- win Brier 0.198336; logloss 0.578880

NEUTRAL n=59:
- margin MAE 12.344622; bias -1.615563
- total MAE 14.220881; bias +4.053374
- win Brier 0.224403; logloss 0.639485

## Population class
FBS_VS_FBS n=761:
- margin MAE 13.786414; bias -0.925448
- total MAE 12.765905; bias +0.835977
- win Brier 0.204392; logloss 0.593625

FBS_VS_NONFBS n=32:
- margin MAE 19.338797; bias -14.962944
- total MAE 12.969944; bias -3.359657
- win Brier 0.102389; logloss 0.339965

## Competition class
CONFERENCE_CHAMPIONSHIP n=9:
- margin MAE 11.683534; bias -0.913859
- total MAE 12.248241; bias +12.097831
- win Brier 0.240255; logloss 0.664682

POSTSEASON n=46:
- margin MAE 12.330404; bias -2.427480
- total MAE 15.344350; bias +2.668002
- win Brier 0.223572; logloss 0.637221

REGULAR n=738:
- margin MAE 14.143567; bias -1.440639
- total MAE 12.620349; bias +0.402522
- win Brier 0.198336; logloss 0.579043

## Bounded observations
The largest descriptive signal is the FBS-vs-nonFBS margin slice (n=32), with materially larger margin error and strongly negative prediction-minus-actual bias. Neutral-site total and conference-championship total slices also show positive bias, but their samples are only 59 and 9 respectively. Postseason total error is higher than regular-season total error on 46 games.

These observations are hypothesis-generating only. No feature/model change may be selected from these 2025 results while treating 2025 as fresh holdout evidence.

Production v1 remains champion/fallback. Challenger B remains challenger/shadow.
