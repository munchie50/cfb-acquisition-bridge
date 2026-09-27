# CFB QA Sandbox S1/S2 Transform Specification — 2026-09-27

Status: FROZEN BEFORE CANDIDATE SCORING
Parent: CFB_QA_SANDBOX_OPPONENT_STRENGTH_STABILIZATION_CONTRACT_2026-09-27
Prerequisite: CFB_QA_SANDBOX_S0_EQUIVALENCE_PROOF_2026-09-27 — PASS
Prerequisite: CFB_QA_SANDBOX_S2_PROVENANCE_READINESS_AUDIT_2026-09-27 — PASS
Production effect: NONE
Champion effect: NONE

## Fixed candidate grid
k in {1, 2, 4, 8}. No expansion after results.

## S0
Exact accepted Champion feature vector, TRAIN scaling, and frozen coefficients.

## Strict-prior population baseline
For a feature F and a target team-side at kickoff T, B_F(T) is the pooled mean of eligible team-side pregame/raw feature observations whose underlying source information was complete before T. No target-game result, later game, market field, user wager, or 2025 record may contribute.

Where a rate is generated from cumulative component counts, the baseline is formed from the corresponding completed strict-prior component totals rather than averaging future/full-season rates.

## S1
For each raw team feature F with n qualified prior games:
S1_F(k) = [n/(n+k)] * Raw_F + [k/(n+k)] * B_F(T).

Opening/no-prior sides remain governed by the accepted eligibility/exclusion rules; the Sandbox does not manufacture eligibility.

## S2 one-step opponent-context correction
S2 begins from S1.

For every qualified source game g contributing to a target side, identify opponent o(g). For feature F, use only opponent o(g)'s pregame strict-prior state at kickoff of g.

Define the opponent-context residual for source game g as the opponent's pregame stabilized state relative to the population baseline available before g:
R_F(o,g,k) = S1_F(o,g,k) - B_F(g).

For rate families where higher opponent offensive strength makes an observed defensive result more difficult, or higher opponent defensive strength makes an observed offensive result more difficult, apply the residual in the direction that normalizes the observed team statistic toward population-opponent context. For lower-is-better defensive/risk measures, direction is reversed consistently with feature semantics.

The target-side one-step context term is the simple mean of valid source-game opponent residuals. No recursion is permitted: opponent context is read from the opponent's S1 pregame state only; S2 values are never fed back into another opponent calculation.

S2_F(k) = S1_F(k) + signed_mean_opponent_context_residual_F(k).

Features without a defensible same-domain opponent-context mapping remain S1-only rather than receiving an invented cross-domain adjustment.

## Frozen mapping discipline
Mappings must be mechanical and semantic:
- team offensive production/rate features map to opponent defensive same-domain pregame context;
- team defensive allowance/rate features map to opponent offensive same-domain pregame context;
- play-selection rates map only where the opposite-side same-domain context exists;
- rest_days and average_starting_yards_to_goal receive no S2 opponent correction unless an accepted same-domain counterpart exists in the recovered schema.

The implementation must persist the exact mapping table before scoring.

## Chronology and leakage locks
- source kickoff < target kickoff;
- opponent context timestamp < source kickoff;
- target game ID excluded;
- 2025 forbidden;
- target/outcome columns forbidden from transform inputs;
- market/betting/wager columns forbidden;
- S2 recursion forbidden.

## Negative controls
1. S0 numerical equivalence remains mandatory.
2. A deliberately injected future timestamp must be rejected.
3. Candidate-input column scan for target/outcome/market/wager terms must return zero.
4. Every S2 context row must resolve to a source game and an opponent pregame state.
5. Any missing or ambiguous required mapping fails closed for that correction; it is not imputed from outcomes.

## Evaluation isolation
Candidate feature artifacts/configuration and candidate predictions must be hashed/frozen before outcome metrics are computed. 2023-2024 remains spent/corroborative. 2025 remains protected.

Scientific effect at specification freeze: none.
