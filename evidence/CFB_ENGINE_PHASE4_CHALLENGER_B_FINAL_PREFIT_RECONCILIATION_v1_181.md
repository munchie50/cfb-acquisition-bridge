# CFB Engine — Challenger B Final Pre-Fitting Reconciliation v1.181

Status: **TECHNICALLY READY / EXPLICIT FITTING AUTHORIZATION REQUIRED**
Parents: v1.173, v1.178, v1.180
No Challenger-B fitting/scoring, 2025 access, or market join occurred.

## Reconciliation result
No unresolved technical pre-fit blocker remains.

### Input and population authority — PASS
- corrected population authority: 7,701 games / 15,402 team-sides;
- accepted corrected feature substrate: v1.172 via v1.173;
- accepted corrected dataset artifact: v1.179 via v1.180;
- dataset artifact 10896565577, digest sha256:8eeb67f5da87df4a75f2f785838553679928e370eefeea3945f2b2e688e69780;
- 6,246 model-eligible rows + 1,455 explicit exclusions = 7,701 target games;
- population/competition-class accounting reconciles.

### Prospective model authority — PASS
v1.178 prospectively inherits v1.123/v1.126/v1.130/v1.135 mechanics:
- 34 side-preserving numeric predictors + venue state;
- Gaussian ridge for margin/total; ridge logistic for home win;
- lambda {0,0.0001,0.001,0.01,0.1,1,10,100};
- TRAIN-only centering/scaling, venue dummy unstandardized;
- unpenalized intercept; non-intercept coefficients penalized;
- complete-case/no model-stage imputation;
- raw logistic probabilities;
- no post-hoc calibration or adaptive search.

### Numerical convention — PASS
Carry v1.135 unchanged:
- HOME=0, NEUTRAL=1;
- population standard deviation for scaling;
- zero-variance numeric columns fail closed;
- fold-specific prior-season scaling;
- 2017–2022 forward-chain evaluation folds using strictly earlier TRAIN seasons;
- tie at 12-decimal reported precision chooses larger lambda;
- final refit on all eligible 2016–2022 TRAIN rows;
- 2023–2024 may then be evaluated only as SPENT/CORROBORATIVE evidence.

### Evidence locks — PASS
- 2025 TEST remains protected and absent from accepted dataset;
- 2023–2024 is not fresh validation and cannot drive same-lineage redesign;
- no market/external-rating predictors;
- no market join before blind candidate predictions are frozen;
- production v1 remains champion/fallback;
- no production promotion authority exists.

## Authorization boundary
The precedent at v1.135 is explicit: technical readiness did not itself authorize fitting; the user separately authorized Challenger-A fitting.

The same governance boundary applies here.

**Required next event: explicit user authorization to fit Challenger B.**

If authorized, execution is limited to:
1. TRAIN 2016–2022 forward-chain lambda selection under the frozen rules;
2. refit selected candidates on all eligible TRAIN rows;
3. evaluate 2023–2024 strictly as spent/corroborative evidence;
4. persist all fold/lambda results, coefficients, scaling, predictions, metrics, exclusions and hashes;
5. independently audit artifacts before any interpretation or downstream decision.

Authorization would NOT include:
- 2025 TEST access/evaluation;
- market join;
- feature/model redesign;
- calibration;
- production promotion;
- champion replacement.

## Current state
**READY TO FIT, NOT AUTHORIZED TO FIT.**
