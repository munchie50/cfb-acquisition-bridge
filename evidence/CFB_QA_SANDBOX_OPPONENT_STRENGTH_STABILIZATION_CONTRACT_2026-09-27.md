# CFB QA Sandbox Experiment Contract — Early-Season Opponent-Strength Stabilization — 2026-09-27

Status: PROSPECTIVE SANDBOX DESIGN — NO EXECUTION RESULTS SEEN
Parent evidence: CFB_QA_WEEK4_FULL_SLATE_MARKET_CONTROL_2026-09-27
Production effect: NONE
Champion effect: NONE

## Question
Can a strictly pre-kickoff opponent-strength / small-sample stabilization layer reduce the early-season failure mode identified by QA without market inputs, user-wager inputs, target outcomes, or postgame information?

## Recovered mechanism
The accepted 2026 prediction producer constructs each team side from cumulative 2026 strict-prior games and PBP only. It does not opponent-adjust the 17 raw history-derived features. Week 4 therefore usually represents three prior games per team.

## Experiment isolation
This is a Sandbox counterfactual only. Champion v1.193 coefficients, lambdas, TRAIN scaling, FIRST_FROZEN predictions, operational market state, decisions, executions, and exclusions remain immutable.

Market lines are evaluation diagnostics only after candidate predictions are frozen. They are prohibited from feature construction, fitting, parameter selection, and stabilization weights.

## Candidate family
Test only transparent shrinkage/opponent-context transforms. No new fitted model family is authorized by this contract.

Candidate S0: exact Champion feature vector and frozen coefficients (control).

Candidate S1: small-sample shrinkage of each team raw rate toward a strictly-prior population baseline. Weight is deterministic from qualified prior-game count n: adjusted = n/(n+k)*team_raw + k/(n+k)*prior_population_baseline.

Candidate S2: S1 plus one-step opponent-context correction using only opponents' strictly-prior pregame baselines available before each source game. No recursive use of target-game outcome or later opponent information.

Pre-freeze k grid: {1, 2, 4, 8}. No expansion after results.

## Chronology
For every target game and every source game used:
- source kickoff must precede target kickoff;
- population baseline must be calculated only from games completed before the target/source cutoff applicable to that feature;
- opponent context must itself be based only on information available before the source game;
- target game ID is forbidden from all feature inputs;
- later 2026 games are forbidden from earlier predictions.

## Evaluation order
1. Implement and hash candidate transform/config before target outcomes are joined.
2. Generate candidate predictions for a historical replay using chronology locks.
3. Freeze candidate predictions.
4. Only then join outcomes and compute margin MAE/RMSE/bias, total MAE/RMSE/bias, win Brier/log loss and winner-direction diagnostics.
5. Report early-season/history-depth slices and large-disagreement QA slices.
6. Market comparison may be appended only after candidate predictions are frozen.

## Selection discipline
Week 4 findings motivated the experiment, so Week 4 cannot be treated as pristine unseen evidence. Any Week 4 improvement is diagnostic/corroborative only.
Primary candidate selection must rely on pre-2026 time-respecting historical evidence or a separately preserved future prospective window. No candidate may be selected solely because it repairs the known Week 4 misses.
2025 TEST remains protected unless a separate authority explicitly permits use.

## Acceptance bar for continued Sandbox study
A candidate may advance only if:
- chronology/leakage audits pass;
- improvement is broad rather than concentrated in the known outliers;
- margin improvement does not create material total/win degradation;
- performance is stable across multiple seasons/history-depth slices;
- no market/user-wager/outcome field entered construction;
- all artifacts/hashes/readbacks persist.

Advancement means Sandbox continuation only. It does not authorize Champion mutation or Challenger promotion.

## Negative controls
- exact S0 reproduction must match frozen Champion predictions within numerical tolerance;
- deliberate future-information sentinel must fail the candidate-input audit;
- target outcome and market-column name scans must return zero candidate inputs.

## Stop conditions
Fail closed on ambiguous chronology, missing opponent pregame context, unreproducible baseline, S0 mismatch, or any target/outcome/market leakage.

## Next executable step
Recover/freeze the historical strict-prior source substrate needed to compute S1/S2 without 2025 access, then implement an outcome-blind candidate feature producer and S0 equivalence test.

Scientific effect: none.
