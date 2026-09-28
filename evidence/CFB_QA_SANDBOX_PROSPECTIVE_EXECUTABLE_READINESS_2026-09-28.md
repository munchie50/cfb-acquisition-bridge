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
