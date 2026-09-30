# CFB QA — Wednesday Fallback Cycle-Binding Correction — 2026-09-30

Status: STRUCTURAL CONTROL CORRECTION PERSISTED / READBACK VERIFIED / RUNTIME DEMONSTRATION PENDING
Scope: recurring Wednesday fallback only. No scientific/model/Champion change.

## Trigger
Routine v5 global dependency review of the Monday→Tuesday→Wednesday chain found that Wednesday treated any successful Tuesday workflow run within the prior 36 hours as satisfying the fallback check. That could allow a manual/test run, or an unrelated recent run, to suppress the normal Wednesday fallback.

The cadence contract defines Wednesday as the bounded fallback for the preceding Tuesday weekly disposition, not for an arbitrary recent success.

## Correction
Updated `.github/workflows/cfb_weekly_wednesday_fallback.yml` so only a successful `event == schedule` Tuesday run whose UTC creation date is the immediately preceding calendar day can suppress Wednesday fallback.

If that exact scheduled Tuesday disposition is absent or unsuccessful, Wednesday dispatches the existing Tuesday candidate workflow once on main.

Manual/test Tuesday runs no longer suppress the scheduled weekly fallback.

## Regression protection
Added:
- `scripts/cfb_qa_weekly_wednesday_fallback_static_gate.py`
- `.github/workflows/cfb_qa_weekly_wednesday_fallback_static_gate.yml`

The guard requires the preceding-day + scheduled-event binding and rejects restoration of the broad 36-hour-success logic.

## Monday→Tuesday dependency classification
The chain review also confirmed that Monday readiness and Tuesday fresh acquisition are intentionally separate:
- v1.247 assigns Monday to readiness/schedule recovery;
- Tuesday must capture its own immutable execution cutoff and newly qualified same-cutoff source boundary;
- v1.216 requires current source preflight/hashes for each snapshot;
- the 2026-09-29 readiness audit explicitly requires newly qualified raw bytes and one immutable cutoff for the actual next-cycle execution.

Therefore Tuesday must not consume Monday's raw bytes as its prediction cutoff merely to avoid reacquisition. Monday is readiness evidence; Tuesday is the candidate execution boundary.

## Persistence
Wednesday correction commit: 1eb609d2bb65aa4812a08171ab280bacbc700503
Regression script commit: a89fe4a20950c7ddbe2c8c96db11f12f562b1d02
Regression workflow commit: 92b24b7c39b685ae734987cd7b1ce1c5fc90d63a

## Classification
Operational/governance hardening only. No weekly workflow was dispatched, no source reacquired, no prediction generated, no S2 consumer built, no outcome/market/wager data joined, no protected 2025 TEST accessed, and no Champion/scientific authority changed.

Frontier remains CADENCE WAIT. Runtime demonstration remains pending normal scheduled execution.
