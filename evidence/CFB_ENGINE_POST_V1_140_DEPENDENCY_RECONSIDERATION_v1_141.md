# CFB Engine — Post-v1.140 Dependency Reconsideration v1.141

Status: NEXT-STAGE BOUNDARY IDENTIFIED / NO TEST OR PROMOTION AUTHORIZED
Date: 2026-09-25
Parent: v1.140 accepted first Challenger-A TRAIN/VALIDATION fit.

## Authority review
The recovered Phase-4 authority states the mission is an independently estimated, market-blind fair model that later supports disciplined positive-EV betting decisions. Production v1 remains champion/fallback; v2 remains challenger/shadow.

v1.126 explicitly requires market/external ratings to remain absent until blind fair predictions are frozen, after which they may be used only as post-freeze diagnostics. v1.140 accepts the first Challenger-A validation evidence but does not itself authorize a market join, TEST exposure, or promotion.

Library recovery state was also rechecked. The latest full integrated Library ZIP remains v1.100 and is stale relative to repository v1.140; v1.134 is only a handoff pointer. That is material integration debt at this stage boundary.

## Global dependency order after v1.140
1. Preserve and integrate the accepted v1.140 state so clean-room recovery no longer depends on a stale v1.100 ZIP plus a newer pointer.
2. Freeze the exact post-validation evidence plan before any new evidence source is joined or 2025 is exposed.
3. Only after that prospective contract may a post-freeze diagnostic market comparison be considered; market data must never feed back into Challenger A fair predictions.
4. 2025 TEST remains a separate holdout gate and is not opened by v1.140.
5. Production promotion remains later and requires explicit promotion evidence/checkpoint and authorization.

## Immediate authorized work
Integration/recovery packaging is safe, independent, and high-value. It does not alter the model or expose new performance evidence.

Create a new integrated Library recovery package containing the current authoritative checkpoints through v1.141, current v1.131 dataset-builder/workflow identities, v1.136 fitter/workflow identities, v1.139 sentinel QA identities, and an authority/supersession manifest. Include the accepted fit artifact identity and hashes as evidence references; do not silently treat ephemeral Actions storage as durable Library integration.

After package persistence/readback proof, freeze a prospective next-stage evidence contract. Do not fetch or join market data and do not expose 2025 before that contract is frozen.

## Locks
- production v1 unchanged;
- Challenger A remains shadow/challenger;
- 2023–2024 evidence spent for Challenger A;
- 2025 TEST protected;
- no post-hoc Challenger-A redesign;
- no market-informed fair-model fitting;
- no production promotion.
