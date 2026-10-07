# CFB QA — Weekly S0 REFRESH_SNAPSHOT Acceptance — 2026-10-07

Status: ACCEPTED / PERSISTED PENDING READBACK
Scope: exact natural Tuesday S0 REFRESH_SNAPSHOT only.

## Frozen candidate identity
- Natural workflow run: 37485273952
- Artifact: 11423386216 (`cfb-weekly-tuesday-candidate-boundary`)
- Exact artifact ZIP SHA-256: `674501a82f6eb207b58b30c483910304c881b3ce29ba2506258152455cb6047b`
- Frozen cutoff: `2026-10-06T15:11:29.838398+00:00`
- Schedule SHA-256: `b2837158c4efb357bd0c1cc89589129ef0d1a54d34c18059b9e7700dd27a2642`
- PBP SHA-256: `4ee3d9e15a271ea08a1fc4034a9c1e670b5bc356c968fa751f9cccf54f8b8b85`

## Independent acceptance audit
Existing repository auditor `scripts/cfb_qa_weekly_refresh_acceptance.py` was recovered and executed against the exact downloaded natural artifact bytes and the exact frozen fit ancestry used by the workflow.

Result: `PASS_WEEKLY_REFRESH_ACCEPTANCE`

Verified:
- 498 unique future targets;
- 495 eligible predictions + 3 explicit exclusions = 498;
- 996 team-side ledger rows;
- 993 strict-chronology audit rows;
- REFRESH_SNAPSHOT / v1.216 lineage and one immutable cutoff;
- own-game exclusion and strict-prior chronology;
- frozen coefficient and scaling byte identities;
- 108 coefficient terms, 34 scaling features, frozen lambdas;
- margin/total/win predictions independently recomputed to absolute tolerance 1e-12;
- manifest-listed output hashes reproduced;
- retained raw source identities reproduced;
- target outcomes unopened;
- market unjoined;
- no fit or optimization performed.

## Acceptance
This exact S0 weekly REFRESH_SNAPSHOT boundary is independently ACCEPTED as prospective prediction-source evidence.

This acceptance does **not**:
- promote or mutate Champion v1.193;
- accept/promote S2_K1;
- join target outcomes, market, execution, or protected TEST;
- accept the target-baseline companion by implication.

The accepted prediction-source pointer may advance only after this record is independently read back. S2_K1 target-baseline acceptance remains a separate audit.
