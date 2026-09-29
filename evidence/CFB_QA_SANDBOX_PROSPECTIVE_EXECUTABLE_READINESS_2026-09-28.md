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


## Source-context companion implementation review — v0 QUARANTINED
Reviewed implementation: `scripts/cfb_qa_s2_k1_source_context_companion_2026_09_28.py`
Observed source blob: `a72406f927c0466a659e909493319c25ba88f22f`
Frozen historical generator blob used for comparison: `40447984a58dbc530cbe942bc1176f0c5bcbe9b2`.

Pre-execution semantic review found two material mismatches, so the implementation is **QUARANTINED / NOT EXECUTED / NOT ACCEPTED**:

1. The companion's `side_state` currently makes context availability effectively all-17-features/all-denominators. Frozen S2 is paired-feature-specific: each mapped feature obtains its own paired baseline/context; zero-history context contributes residual zero when its paired baseline exists; positive-history context is skipped according to frozen completion-safe state and paired raw availability. One unrelated unavailable denominator must not suppress every mapped feature.

2. The companion exports cumulative target/opponent-history numerators and denominators. Frozen population baselines are pooled from completion-safe **per-game primitive rows across the season population before the calendar-day-normalized cutoff**. Cumulative team-history components are not a valid substitute for that primitive population surface.

Disposition:
- Do not create an execution workflow for this v0 script.
- Do not use its outputs for S2.
- Preserve it as rejected QA evidence; do not delete history.
- Recover/reuse the accepted v1.172-style per-game mechanical/derived primitive construction semantics, adapted only to the already-qualified 2026 R/P source boundary, or expose equivalent per-game primitive rows directly from the same R/P inputs.
- Keep target-side v1.246 acceptance unchanged.

This is an implementation correction only. Frozen S2_K1 science, mapping, chronology, k=1, production/Champion state, protected 2025 TEST, and no-outcome/no-market constraints remain unchanged.


## S2_K1 source-context synthetic semantic gate — PASS
Workflow run `36508003233`, job `109213689953`, head `9f7c6e760bbc78522836c5f7a3d4ff9c0bf65ea5`, conclusion SUCCESS.

Observed marker:
`S2_K1_SOURCE_CONTEXT_SYNTHETIC_SEMANTIC_PASS`

The bounded synthetic gate proved:
- calendar-day-normalized cutoff excludes same-date primitive rows;
- pooled numerator/denominator baseline behavior;
- incomplete primitive rows excluded from population baselines;
- zero-history opponent context contributes residual zero when baseline exists;
- positive-history context with either history-complete flag false is unavailable;
- positive-history non-finite paired raw context is unavailable;
- feature-specific context invalidity does not suppress unrelated mapped features;
- k=1 S1 residual arithmetic;
- strict source-before-target chronology.

Classification: **SYNTHETIC SEMANTIC RULES PASS / COMPANION IMPLEMENTATION NOT YET ACCEPTED.**

This run contains no live 2026 outcome evaluation and does not validate the v1 companion against real executable R/P inputs. The next authorized dependency is implementation-structure/static equivalence followed by bounded executable structural QA. No S2 prediction generation is authorized.


## Exact 2026 raw-source replay recovery closure
Pinned-source preflight run `36508651547`, job `109215690292`, head `315d61ee7ad82ba32e77df6db773bde7f8fb961f` failed closed at the accepted schedule-byte boundary:
- immutable target preflight artifact `10897001956`: PASS, ZIP SHA `4dc70419b9aa3afdfa2570861490598da69b2bccfed878e438dc17b69a9a7ea8`;
- current schedule URL no longer matches accepted SHA `5b2ff52996862b06b67309f1ebc27742e55c279ff4785c7a942915cdf820f1b1`;
- PBP hash check was not reached in that run.

A broader workflow-definition recovery sweep covered v1.204, v1.206, v1.209, v1.211, v1.213, v1.214 and v1.217 lineage. Workflows that downloaded 2026 raw schedule/PBP inputs uploaded only their derived `out/` directories. No reviewed workflow retained its `raw/` directory in an Actions artifact. The repository recursive tree likewise contains no frozen 2026 schedule parquet or PBP RDS raw snapshot.

Classification: **EXACT ACCEPTED 2026 RAW-BYTE REPLAY UNAVAILABLE / RAW-SOURCE RETENTION DEFECT DEMONSTRATED.**

This does not invalidate the accepted v1.206 freeze, its derived artifacts, the v1.246 frozen-feature-boundary proof, or the S2_K1 synthetic/static semantic gates. It means the S2 source-context companion cannot receive a real-data executable-equivalence PASS against the original accepted source bytes.

Required forward correction: any new prospective source acquisition used for S2_K1 QA must freeze and retain the exact raw schedule/PBP bytes (or an immutable byte-addressed package) together with hashes before downstream execution. Current mutable upstream bytes must not be substituted and described as historical replay.


## Prospective raw-source freeze acceptance
QA raw-source freeze run `36563040022`, job `109388231240`, head `90492e218a86df4e5bd28c43d7ebb9f3d2b0ace9`: SUCCESS.

Artifact `11031055060`, `cfb-qa-2026-raw-source-freeze`, retained the raw schedule and PBP bytes plus target projection, preflight metadata, source checksum file and manifest. GitHub artifact ZIP digest and independent downloaded-byte SHA agree exactly:
`1495f453e5d9f262baddfa2b7ad21d2d9e8d5f8c2436f058f88fcb6ebc6d8d68`.

Independent extraction/readback recalculated and matched every manifest hash:
- schedule: `9847952ba52279318018a259c07197df23392086f03bd6a308fd2cf60e83cd2c`;
- PBP: `eab0562fb2f9dd9c65cf1457c469d656d9247212694370cac10c789e673a2ddb`;
- target projection: `9303d7137ca19b5ccbdaf657d7d2f80746a82274ea4ced56dcb3d1509765307f`;
- preflight JSON: `351f20a80d452c4ec8311a41b950ca618e30b589514744b0642267bbb1c5f2d2`;
- raw checksum file: `6a45de9d226a65bf4d6f4188c2945392c2e2425a02ee58bef9a7adcadfb0148a`.

Preflight cutoff `2026-09-29T11:39:08.824054+00:00`; qualified relevant-FBS rows 888; future targets 557. Manifest remains `QA_RAW_SOURCE_FROZEN_NOT_EXECUTED`, with S2 predictions, target-outcome join and market join all false.

Classification: **PROSPECTIVE QA RAW-SOURCE FREEZE ACCEPTED AS IMMUTABLE EXECUTABLE INPUT BOUNDARY.**

Downstream S2 source-context structural QA must consume artifact `11031055060` and verify the ZIP and internal source hashes before execution; it must not reacquire mutable upstream URLs.
