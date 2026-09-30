# CFB QA — Weekly Source-State No-Op Gate Correction — 2026-09-30

Status: STRUCTURAL CONTROL CORRECTION PERSISTED / READBACK VERIFIED
Scope: recurring weekly scheduler only. No scientific/model/Champion change.

## Trigger
Production Routine v5 + core controls v1.132/v1.133 were applied during cadence-wait independent work. The installed Tuesday workflow treated `future_at_cutoff > 0` as sufficient to proceed. That condition proves future targets exist but does not prove source state changed from the last independently accepted prediction boundary.

This conflicted with v1.218 and v1.247: unchanged source state is a weekly no-op and must not manufacture a prediction snapshot/candidate boundary.

## Correction
Created `evidence/operational/CFB_ACCEPTED_PREDICTION_SOURCE_STATE.json` as the fail-closed pointer to the last independently accepted prediction-source boundary. Initial authority is v1.208, with exact source identities already independently reconciled by v1.218:
- schedule SHA-256: 5b2ff52996862b06b67309f1ebc27742e55c279ff4785c7a942915cdf820f1b1
- PBP SHA-256: 81e38e7e874d249300bb108de0029a8ffb0b19c31cfea6e7aafab5507115e5da

The pointer may advance only after a later weekly prediction boundary is independently accepted and persisted. Workflow success/candidate generation alone cannot advance it.

Updated `.github/workflows/cfb_weekly_tuesday_candidate_freeze.yml` so fresh source hashes are compared to that accepted pointer after v1.217 preflight and before any model/context producer runs.

If no future targets exist OR both source hashes are unchanged:
- workflow classifies a successful weekly NOOP;
- Champion fit is not fetched;
- S0 producer is not run;
- source-context producer is not run;
- no candidate package is uploaded.

If at least one source identity changed and future targets remain, the existing NOT_ACCEPTED candidate path proceeds unchanged.

Wednesday fallback remains bounded correctly: a successful Tuesday no-op is a valid completed Tuesday disposition and must not trigger a duplicate Wednesday candidate attempt.

## Persistence/readback
Pointer creation commit: f07d8136dd9857e0ccc23c92b02288fc8c123d8f.
Tuesday correction commit: e68fcfccb5c19f75740e7320cc3416b17a72eb02.
Readback blobs:
- pointer: 2fde1a1e14c040fc9a7b348f8f2f09555b1e8d65
- Tuesday workflow: 45b8a1690526737a8501b4b42c832d3295a8ec52

Direct readback confirmed exact pointer values and conditional gating on every downstream candidate-producing/upload step.

## Classification
Operational/governance correction only. No source was reacquired during this correction, no workflow dispatched, no prediction generated, no S2 consumer built, no outcome/market/wager data joined, no 2025 TEST accessed, and no Champion/scientific authority changed.

## Learning enforcement
Observed: recurring scheduler omitted the previously demonstrated v1.218 accepted-source comparison.
Installed trigger: every Tuesday candidate decision now compares fresh raw source identities to the persisted last independently accepted prediction-source pointer before execution.
Demonstration status: structural/readback PASS; real scheduled-path demonstration remains pending the next normal Tuesday run.
