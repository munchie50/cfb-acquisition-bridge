# CFB Engine — Challenger B Post-Fit Evidence Boundary & 2025 Preparation Contract v1.185

Status: **PROSPECTIVELY FROZEN / 2025 OUTCOMES STILL PROTECTED**
Parents: v1.143, v1.149, v1.173, v1.178, v1.180, v1.184
Candidate: accepted Challenger B v1.183/v1.184
Production v1 remains champion/fallback.

## Reconciliation
v1.184 accepts the corrected-population Challenger-B fit and 2023–2024 spent/corroborative evaluation. It does not open TEST, market, or promotion.

The sequencing safeguards in v1.143 remain governing, but its Challenger-A candidate identity is superseded for this branch by the accepted Challenger-B identity.

The old 762-game 2025 FBS-vs-FBS count remains a source-reacquisition diagnostic only. v1.149 correctly established that it is not the Phase-4 full relevant-FBS holdout population.

## Frozen Challenger-B identity entering future evidence
- accepted corrected dataset: artifact 10896565577;
- accepted fit artifact: 10895838069, digest sha256:3a2cabfcd37e0bcf0cae85efc77eaa6755ffb12734d1e48c4c582ed1de375587;
- 34 numeric side-specific predictors + venue state;
- selected lambdas: margin 10, total 100, win 10;
- scaling/coefficients exactly as persisted in v1.183 artifact;
- no recalibration;
- no market/external-rating inputs;
- no feature/model/population redesign based on 2023–2024 results.

## 2025 current blocker
There is no accepted Challenger-B 2025 outcome-blind full-relevant-FBS schedule/feature/prediction artifact.

The accepted v1.172 corrected feature substrate ends at 2024. Therefore 2025 cannot be scored and cannot yet receive fair predictions by merely filtering an existing artifact.

## Authorized safe preparation
Without opening outcomes, future work may:
1. reacquire/source-qualify 2025 schedule metadata;
2. quarantine raw source bytes if they contain outcomes;
3. project an outcome-blind schedule containing only identity, kickoff, home/away, neutral-site and population metadata;
4. apply v1.124/v1.151 full relevant-FBS population semantics, including qualified FBS-vs-non-FBS and postseason;
5. build 2025 same-season features using unchanged v1.159/v1.172 semantics with strict source kickoff < target kickoff;
6. ensure target-game own PBP and later PBP are inaccessible to its prediction features;
7. apply the already-frozen v1.183 scaling/coefficients without refitting;
8. durably freeze all eligible 2025 fair predictions and exclusions;
9. independently audit candidate identity, chronology, population, leakage and hashes.

## Outcome isolation
Prediction machinery must not receive:
- home/away points, score, winner or postgame result/status;
- market/odds/line fields;
- any target-derived or outcome-derived field.

If raw historical schedule/PBP sources necessarily contain results, the prediction path must use an isolated pregame projection and chronology gate. Raw outcome-bearing bytes are source evidence only.

## Opening gate
After the full 2025 fair-prediction artifact is frozen and independently accepted, **a separate explicit user authorization is required before 2025 outcomes are joined or scored.**

No individual 2025 game may be inspected for model correction before that freeze.

## Market boundary
Historical market diagnostics remain source-semantic blocked by v1.144 unless a separately qualified market contract/source is frozen. Market data must not enter 2025 fair-prediction construction.

## Promotion boundary
No favorable corroborative, TEST, market, or shadow result automatically promotes Challenger B. Promotion remains a separate evidence/rollback/operational-readiness checkpoint with explicit authorization.

## Immediate next technical gate
Recover and prospectively freeze the corrected 2025 full-relevant-FBS outcome-blind schedule qualification procedure before retrieval/execution.

Locks: 2025 outcomes unscored; no market join; no refit/redesign; no promotion.
