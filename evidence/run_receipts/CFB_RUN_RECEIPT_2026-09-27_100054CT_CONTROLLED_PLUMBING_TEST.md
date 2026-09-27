# CFB Run Receipt — Controlled Plumbing Test

Run type: CONTROLLED_PLUMBING_TEST
Actual timestamp CT: 2026-09-27 10:00:54 CT
Repository tip observed at recovery start: c8b28fb507bdca01749e56241130456d00fbc4da

## Recovery
Selected recovery index: evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_243.md
Recovery-index direct readback: PASS
Active persistence controls directly read: v1.239 and v1.242
Beta Champion maturity/identity recovery: PASS
- CFB Beta Production Champion
- retired production-v1 confirmed non-operational
- accepted identity preserved: margin lambda 0.1; total lambda 0.1; win lambda 0.01
- coefficients SHA bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221
- scaling SHA 68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45

## Canonical operational surfaces
Direct recovery/readback:
- evidence/operational/CFB_MARKET_MONITOR_STATE.md — PASS
- evidence/operational/CFB_DECISION_WAIT_LEDGER.md — PASS
- evidence/operational/CFB_EXECUTION_LEDGER.md — PASS
- evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md — PASS

Operational disposition: NO_MATERIAL_CHANGE.
This controlled plumbing test intentionally did not manufacture market observations, decisions, WAIT states, executions, settlements, or postgame joins merely to force a write. Existing surfaces remain canonical and unchanged.

Production ledger state: no new established execution created by this test.
Sandbox ledger state: no new established experimental execution created by this test.

## Boundaries
FIRST_FROZEN state unchanged.
No Champion mutation.
No Challenger promotion.
No hindsight reconstruction.
No invented probability, EV, confidence, market state, decision, execution, close, or outcome.
No wager placement.

## Required deliverable
Conforming append-only receipt under evidence/run_receipts/: this document.

ENGINE_WORKFLOW_STATE: RUN_PASS
ARTIFACT_PERSISTENCE_STATE: PASS subject to independent receipt readback
USER_DELIVERY_STATE: PENDING at receipt creation

Blockers: none.
Next safe action: allow the regular 1:00 PM CT CFB Market Monitor to exercise the same v1.243/v1.242 persistence chain with live applicable state; require its own conforming receipt and direct surface readbacks.
