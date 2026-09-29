# CFB QA Sandbox — Prospective S2_K1 Executable Readiness — 2026-09-28

Status: **READINESS GAP CONFIRMED / IMPLEMENTATION MAY PROCEED OUTCOME-BLIND**

The prospective continuation contract is frozen, and the existing v1.217 refresh preflight can qualify a future source/cutoff snapshot. However, no dedicated 2026 S2_K1 companion producer currently exists. Deeper interface recovery also found that v1.206 is a first-freeze producer hard-coded to the original 622-target identity, while v1.217 is source-preflight only. There is not yet an accepted generalized REFRESH_SNAPSHOT prediction producer.

This is implementation debt, not scientific authority to change S2_K1.

## Required implementation
Create a separate QA Sandbox producer that:
- consumes a qualified 2026 refresh source snapshot and target projection;
- reproduces S0 using unchanged v1.193 coefficients/scaling;
- applies exactly frozen S2_K1 semantics (k=1 only);
- emits home/away qualified_prior_games and the predeclared DEPTH_1_2 / DEPTH_3_4 / DEPTH_5_PLUS label;
- preserves exclusions/fail-closed chronology;
- forbids target outcomes, market, wager, execution and 2025 inputs;
- writes separate QA artifacts and never mutates S0 FIRST_FROZEN/REFRESH_SNAPSHOT authority.

## Execution boundary
Implementation, syntax checks, identity observation and synthetic/structural tests may occur now.
No live 2026 S2_K1 prediction freeze should occur before the next qualified v1.216 weekly refresh cadence.
No outcome scoring is authorized.


## Dependency-order correction
Do not implement an independent S2_K1 live producer ahead of the ordinary refresh producer. That would duplicate 2026 source/feature construction and create avoidable semantic drift.

Required order:
1. create a generalized S0 REFRESH_SNAPSHOT producer from frozen v1.206/v1.216 semantics, without mutating v1.206;
2. prove S0 model/feature/chronology identity and append-only lineage behavior;
3. expose the same pre-cutoff team-side source/feature substrate needed by QA;
4. build S2_K1 as a separate companion transform over that frozen substrate;
5. observe/pin identities and structurally validate before the next live freeze.

No live refresh is triggered by this finding.


## v1.246 shared pre-cutoff team-side substrate — ACCEPTED
Accepted QA run: `36506258474`
Head: `e4e50da38a67f16e2dc6e5c5b1c0c30c187a4ab3`
Job: `109208262604`
Producer source SHA observed by gate: `62784e62d49e92b11a069792f8c8c14def0e9e7bc9eb7a00b4793b95f1a8ebfd`
Output-harness SHA: `cdc1ff1bd0807e4b0311be7e2a78e737413a3c6e`

Markers:
- `V1_246_SUBSTRATE_EXPORT_STATIC_PASS`
- `V1_246_OUTPUT_PLUMBING_PASS 3 2 1`
- `V1_246_SUBSTRATE_EXPORT_DYNAMIC_PASS 6 599493d47151ca029b577e442d4642ababfce6d5477a2813425be57c04b4a814`

The new `challenger_b_2026_refresh_team_side_substrate_v1_246.csv` is a direct export of the already-computed in-memory `L` ledger. The gate proves no new feature construction or ledger mutation in the export region. On executable synthetic state it is byte-for-byte identical to the existing feature-eligibility ledger; both have SHA-256 `599493d47151ca029b577e442d4642ababfce6d5477a2813425be57c04b4a814`.

The frozen fit ZIP checksum `3a2cabfcd37e0bcf0cae85efc77eaa6755ffb12734d1e48c4c582ed1de375587` passed. Six-file manifest integrity passed, including the substrate hash. Existing generalized output-plumbing assertions also passed.

Classification: **SHARED PRE-CUTOFF TEAM-SIDE SUBSTRATE ACCEPTED FOR QA DEPENDENCY USE.**

Scope:
- This is an exported boundary, not a second feature engine.
- S0 calculations/chronology remain the accepted v1.246 path.
- No S2 transform has been applied by this acceptance.
- No outcome, market, wager, or 2025 protected TEST information is introduced.
- No Champion/production mutation or promotion.
- Historical raw-PBP byte replay limitation remains unchanged.

Dependency order may advance to a separate S2_K1 consumer using this accepted shared boundary and the already-frozen S1/S2 transform/mapping semantics. The S2 consumer must not reconstruct or fork S0 feature chronology.


## S2_K1 exact-interface recovery — dependency correction
A full read of the frozen historical generator `scripts/cfb_qa_sandbox_candidate_generator_2026_09_27.py` confirms that the accepted v1.246 target-side substrate is necessary but not by itself sufficient to reproduce frozen S2_K1.

Frozen S2_K1 requires, for each mapped target-side feature and each qualified source game:
1. exact source-game identity and kickoff;
2. source team's opponent identity;
3. that opponent's pregame 17-feature state at the source kickoff;
4. opponent `qualified_prior_games`;
5. completion-safe mechanical/derived history status for positive-history opponent states;
6. the frozen season-local population baseline for the paired feature at the source kickoff, using calendar-day-normalized cutoff and pooled primitive numerators/denominators (rest_days uses mean strict-prior side state);
7. one-step opponent S1 residual only; no S2 recursion.

The exact frozen correction remains `target_S1 - mean(valid paired opponent S1 residuals)`. Zero-history opponent context contributes residual 0 when a completion-safe baseline exists. Unavailable baseline/context is skipped exactly as frozen; a mapped target feature fails only when no valid completion-safe S2 context remains.

Therefore the next dependency is **not** an S2 prediction consumer yet. First expose a separate source-context/baseline companion substrate from the same qualified pre-cutoff source state used by v1.246. This companion must not reconstruct S0 target features, alter v1.246 outputs, change chronology, or approximate pooled baselines with simple feature means.

Classification: **TARGET-SIDE SUBSTRATE ACCEPTED; SOURCE-CONTEXT/BASELINE SUBSTRATE STILL REQUIRED BEFORE S2_K1 IMPLEMENTATION.**

No S2 predictions, outcomes, market/wager data, 2025 TEST access, Champion mutation, or production promotion are authorized by this correction.
