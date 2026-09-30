# CFB QA — Weekly Source-State No-Op Regression Guard — 2026-09-30

Status: INSTALLED / STATIC READBACK VERIFIED / RUNTIME DEMONSTRATION PENDING
Scope: regression prevention for the recurring Tuesday no-op control only.

## Routine finding
After the accepted-source no-op correction, global dependency reconsideration identified a remaining operational risk: the scheduler fix had no dedicated regression guard. A later workflow edit could remove the source-state comparison or conditional execution without an explicit QA failure.

## Installed guard
Added:
- `scripts/cfb_qa_weekly_source_state_noop_static_gate.py`
- `.github/workflows/cfb_qa_weekly_source_state_noop_static_gate.yml`

The static gate verifies:
1. the accepted-source pointer exists with required identity/governance fields and SHA-256-shaped source identities;
2. the Tuesday workflow still reads that pointer and compares current schedule/PBP hashes against it;
3. candidate eligibility still requires both future targets and changed source state;
4. the Champion-fit fetch, S0 producer, v4 source-context producer, candidate packaging, and artifact upload all remain guarded by `candidate_needed == true`;
5. the accepted-source pointer retains its rule that workflow success alone cannot advance it.

The QA workflow triggers on changes to the Tuesday workflow, pointer, static script, or QA workflow itself.

## Verification
Repository readback after writes:
- static script blob: a8c7b3d26693396ac0054f531cf43b04f0a031f6
- static workflow blob: ea0e2f7244e73d0809d2fc6e3fa2e28927148e68
- accepted-source pointer blob remains: 2fde1a1e14c040fc9a7b348f8f2f09555b1e8d65
- Tuesday workflow blob remains: 45b8a1690526737a8501b4b42c832d3295a8ec52

Direct readback confirms the required tokens/guards are present. The available connector run helper reports only pull-request-triggered runs and therefore returned no run for the push commit; runtime PASS is deliberately not claimed from absence of evidence.

## Classification
Operational QA hardening only. No weekly source acquisition was performed, no scheduler/candidate workflow was manually dispatched, no S0/S2 prediction generated, no outcome/market/wager data joined, no protected 2025 TEST accessed, and no Champion/scientific authority changed.

Frontier remains CADENCE WAIT. Runtime demonstration of this regression guard and the real no-op/change branch remains naturally pending scheduled execution.
