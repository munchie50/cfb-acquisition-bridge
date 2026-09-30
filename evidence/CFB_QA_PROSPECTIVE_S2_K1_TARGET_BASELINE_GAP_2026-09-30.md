# CFB QA — Prospective S2_K1 Target-Baseline Substrate Gap — 2026-09-30

Status: EXECUTABLE READINESS BLOCKER IDENTIFIED / CONSUMER CONSTRUCTION DEFERRED
Scope: prospective S2_K1 plumbing only. No scientific/model change.

## Routine finding
Field-level reconciliation of the accepted v1.246 S0 target-side substrate, accepted v4 source-context substrate, and frozen prospective S2_K1 consumer specification found one missing input.

v1.246 supplies each target side's:
- 17 raw frozen features;
- qualified_prior_games;
- target identity/kickoff/cutoff.

v4 supplies, for each qualified source game:
- paired opponent raw pregame state;
- paired population baseline at the source-game cutoff;
- context validity/completion/chronology identities.

That is sufficient for the one-step S2 opponent residual, but NOT for target-side S1:
S1_F(target,1) = n/(n+1) * Raw_F(target) + 1/(n+1) * B_F(target cutoff).

Neither accepted surface persists B_F at the target cutoff for all 17 target features. Reusing a source-game baseline is wrong because its cutoff differs. Reconstructing target baselines inside the prediction consumer would collapse substrate construction and prediction into one executable and weaken independent reconciliation.

## Corrective design
Do not alter accepted v4 and do not manufacture a baseline in the consumer.

Add a separate QA-only same-cutoff target-baseline companion at the next implementation step. It must:
1. consume the exact same retained raw schedule/PBP bytes and immutable cutoff as v1.246/v4;
2. use the exact frozen pooled-baseline rules from CFB_QA_SANDBOX_POOLED_BASELINE_MAPPING_FREEZE_2026-09-27 and accepted historical generator;
3. emit one row per accepted target side with target identity, cutoff, qualified_prior_games, and all 17 B_F(target cutoff) values plus per-feature availability;
4. preserve season-local 2026, strict cutoff-local semantics and UTC calendar-day normalization where frozen historical baseline semantics require it;
5. never consume target outcomes, target PBP, markets, wagers, protected 2025 TEST or later source state;
6. be independently reconciled/accepted before the S2_K1 consumer can execute.

The consumer input contract therefore becomes:
accepted weekly S0 target-side + accepted same-cutoff target-baseline companion + accepted same-cutoff v4 source context + frozen Champion fit.

## Why this is not a science change
The missing values are already required by the frozen S1 equation and historical pooled-baseline specification. This correction exposes those required inputs as a separately auditable substrate rather than inventing a new formula, mapping, k, eligibility rule or prediction mechanic.

## Stop condition
Prospective S2_K1 consumer construction is deferred until this target-baseline substrate has an executable, static gate, real/synthetic structural acceptance as appropriate, and a same-cutoff integration contract. No prediction consumer should independently reconstruct B_F(target cutoff).

Frontier remains CADENCE WAIT. No live source acquisition, prediction, outcome evaluation, 2025 TEST access or Champion change occurred.
