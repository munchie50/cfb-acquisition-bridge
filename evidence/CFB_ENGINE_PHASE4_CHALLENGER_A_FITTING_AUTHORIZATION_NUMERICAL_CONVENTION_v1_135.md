# CFB Engine — Challenger A Fitting Authorization & Numerical Convention v1.135

Status: AUTHORIZED / FROZEN BEFORE PERFORMANCE
Date: 2026-09-25
Scope: first Challenger A TRAIN/VALIDATION fit only
2025 TEST: NOT AUTHORIZED / MUST REMAIN UNEXPOSED
Production promotion: NOT AUTHORIZED

## Authorization
The user explicitly authorized Challenger A fitting after v1.134 established no remaining technical pre-fit blocker.

Authorization permits TRAIN 2016–2022 fitting/forward-chain selection and VALIDATION 2023–2024 evaluation under frozen v1.126 rules. It does not authorize 2025 TEST access, market joining, redesign from observed performance, or production promotion.

## Numerical convention frozen before performance
To remove implementation ambiguity without changing the model family:

- one game row; predictors are the frozen 34 numeric side-specific columns plus one venue dummy;
- venue encoding: HOME = 0 reference, NEUTRAL = 1; unknown values fail closed;
- numeric columns are centered and scaled with fitting-sample mean and population standard deviation; zero-variance numeric columns fail closed;
- the venue dummy is not standardized;
- intercept is unpenalized;
- Gaussian margin/total objective: mean squared error / 2 + lambda * ||beta||^2 / 2;
- logistic win objective: mean Bernoulli negative log likelihood + lambda * ||beta||^2 / 2;
- penalty applies to all non-intercept coefficients, including the venue dummy;
- lambda grid remains exactly {0,0.0001,0.001,0.01,0.1,1,10,100};
- forward-chain folds evaluate seasons 2017–2022 using every strictly earlier TRAIN season available in the frozen dataset; 2016 is seed training history and is not itself an evaluation fold;
- each fold recomputes numeric centering/scaling from that fold's prior-season fitting rows only;
- lambda selection remains mean fold MAE for margin/total and mean fold Brier for win; exact ties at reported 12-decimal precision choose larger lambda;
- after lambda selection, refit on all 2016–2022 TRAIN rows with TRAIN-only scaling, then evaluate unchanged on 2023–2024 VALIDATION;
- raw logistic probabilities only; no recalibration;
- retain all lambda/fold results and selected-model coefficients/scaling;
- 2025 presence anywhere in input is a hard failure;
- market/external-rating-like predictor names are a hard failure.

This convention is prospective and must not be changed in response to the resulting TRAIN/VALIDATION performance. Any redesign is a separately versioned challenger.

No performance was viewed before this checkpoint was persisted.
