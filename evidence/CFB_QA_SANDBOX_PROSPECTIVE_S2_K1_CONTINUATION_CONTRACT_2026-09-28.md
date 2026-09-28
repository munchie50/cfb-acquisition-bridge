# CFB QA Sandbox — Prospective S2_K1 Continuation Contract — 2026-09-28

## Status
**PROSPECTIVELY FROZEN DESIGN / NO S2_K1 2026 OUTCOMES EVALUATED**

Production effect: NONE.
Champion effect: NONE.

## Purpose
Test whether the historical S2_K1 signal survives a genuinely prospective 2026 window without tuning after historical outcomes.

## Candidate lock
- Control: S0, unchanged Champion v1.193 fair-model semantics.
- Candidate: S2_K1 exactly as frozen in the accepted historical Sandbox experiment.
- k = 1 only.
- No S1 continuation, heavier k values, k-grid expansion, coefficient/scaling change, refit, recalibration, threshold tuning, or formula redesign is authorized.
- Historical scoring evidence may justify testing S2_K1 but may not alter its construction.

## Prospective boundary
The first accepted 2026 live-shadow freeze predates this QA disposition and MUST NOT be retrofitted with S2_K1.
The v1.218 refresh preflight was a no-op and produced no second snapshot.
Therefore the first valid S2_K1 prospective QA evidence begins only with a future weekly REFRESH_SNAPSHOT whose prediction bytes are frozen before target kickoff and before target outcomes are evaluated.

## Lineage
The existing v1.216 rolling live-shadow contract remains authoritative for production/Champion S0 lineage.
S2_K1 QA output is a separate Sandbox companion artifact. It may share the same qualified pre-cutoff source snapshot and target ledger, but it must not overwrite or alter FIRST_FROZEN or REFRESH_SNAPSHOT S0 records.

## Required pre-outcome frozen fields
For every S0/S2_K1 eligible target:
- snapshot cutoff and lineage label;
- season/game_id/start_date/home_team/away_team/venue state;
- S0 and S2_K1 predictions;
- home and away qualified_prior_games;
- deterministic history-depth slice derived only from those two counts;
- source identities/hashes;
- candidate implementation SHA-256 and Git blob;
- prediction/exclusion artifact hashes.

History-depth slices are predeclared as:
- DEPTH_1_2: minimum(home qualified prior games, away qualified prior games) in 1–2;
- DEPTH_3_4: minimum in 3–4;
- DEPTH_5_PLUS: minimum >=5.
No slice boundary may change after outcomes are visible.

## Isolation
Forbidden from candidate construction or selection:
- target outcome/PBP;
- market/spread/odds/closing data;
- user wager/execution data;
- later-game information;
- protected 2025 TEST.

Strict chronology and fail-closed source/context behavior remain unchanged.

## Evaluation
After the prospective window closes and under separate bounded outcome-scoring authority:
- compare S2_K1 with S0 only on exact common eligible games;
- margin MAE/RMSE/bias;
- total MAE/RMSE/bias;
- win Brier/log loss/winner-direction diagnostic;
- by-snapshot/by-week and predeclared history-depth slices;
- predeclared disagreement slices may use the same historical frozen thresholds: margin >=7 points, total >=7 points, win probability >=0.10.

No market comparison is required for scientific candidate acceptance and no market field may enter candidate construction.

## Advancement discipline
This contract authorizes prediction freezing only. It does not authorize outcome scoring, scientific acceptance, Challenger promotion, Champion mutation, or production use.
Time alone is not evidence; an adequate prospective sample must accumulate before interpretation.

## Next executable step
At the next v1.216 weekly refresh cadence, run current source preflight. If source state qualifies for a new REFRESH_SNAPSHOT, freeze the ordinary S0 refresh and the separate S2_K1 companion with the required history-depth metadata before outcomes. If the refresh is a no-op, do not manufacture a QA snapshot.
