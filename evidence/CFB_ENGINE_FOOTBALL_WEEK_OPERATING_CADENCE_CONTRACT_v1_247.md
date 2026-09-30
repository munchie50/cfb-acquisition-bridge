# CFB Engine — Football-Week Operating Cadence Contract v1.247

Status: PROSPECTIVELY ACTIVE FOR THE NEXT QUALIFIED WEEKLY CYCLE
Date: 2026-09-29
Supersedes: v1.216 cadence timing only. All v1.216 lineage, chronology, immutability, source, model, and evaluation rules remain active unless explicitly changed here.
Production/Champion effect: NONE.
Scientific S2_K1 effect: NONE.

## Purpose
Align the CFB Engine operating clock with the actual college-football week instead of the seven-day anniversary of FIRST_FROZEN. This is an operational timing correction, not a model or evidence-rule change.

## Prospective timing rule
Beginning with the next qualified weekly cycle, use an early-week prediction/data cycle rather than waiting until Friday night/Saturday.

Planning windows are America/Chicago:
1. SUNDAY — postgame closure and recovery. Score only already-frozen predictions under existing outcome authority; close prior-week operational evidence. Sunday market/early-board observations remain downstream market evidence and never model inputs.
2. MONDAY — source readiness and schedule recovery. Requalify current schedule/PBP source state and identify the coming relevant-FBS slate. If required source state is not ready, WAIT and retry within the early-week readiness window; do not manufacture a snapshot.
3. TUESDAY — preferred weekly immutable model freeze. Once source preflight qualifies, capture one immutable cutoff, retain exact raw bytes/hashes, run the ordinary S0 REFRESH_SNAPSHOT and same-cutoff S2_K1 QA companion when authorized by its frozen contract, and independently reconcile outputs before acceptance.
4. WEDNESDAY — bounded fallback for source/operational delay. If Tuesday could not qualify for a documented source/operational reason, Wednesday is the normal fallback. Preserve the actual cutoff and reason. Do not move later merely to obtain more favorable information.
5. THURSDAY–SATURDAY — market monitoring, decision maturation, and execution windows operate downstream from the frozen fair-model predictions. No ordinary weekly model refresh during this period. A separately documented operational/source failure exception is required for any later model snapshot.

No exact clock hour is imposed by this contract. The immutable execution cutoff is the actual UTC time at which the qualified snapshot is frozen. All target games must remain strictly future at that cutoff.

## Relationship to FIRST_FROZEN and v1.216
- FIRST_FROZEN remains immutable and primary prospective evidence.
- This contract does not retroactively change any September 2026 snapshot.
- The old seven-day anniversary is no longer the operating dispatch rule after this prospective correction.
- v1.216 REFRESH_SNAPSHOT lineage remains unchanged.
- A weekly no-op still means no manufactured snapshot.
- Do not rerun because upstream bytes change later in the same weekly cycle.
- The next cycle must recover current authority and pass fresh preflight before any freeze.

## S2_K1 QA
The prospective S2_K1 continuation contract remains frozen scientifically:
- k=1 only;
- exact frozen S1/S2 semantics;
- separate QA companion;
- same accepted cutoff/source boundary as the week's S0 refresh;
- DEPTH_1_2, DEPTH_3_4, DEPTH_5_PLUS frozen pre-outcome;
- no target outcomes, market, odds, wagers, execution evidence, protected 2025 TEST, refit, recalibration, redesign, or promotion.
Changing the operating weekday does not create scientific acceptance or outcome-scoring authority.

## Market and execution coordination
Market/odds observations remain strictly downstream and separate from model construction.
The existing Sunday Early Board may continue as the first market view of the coming slate. After the Tuesday/Wednesday model freeze, subsequent market passes compare current executable markets with the accepted frozen model snapshot under the existing decision/WAIT governance.

Execution planning should batch actionable wagers into practical weekly windows rather than requiring daily trips. The normal operating objective is 1–2 execution trips per week; a third requires a compelling documented reason. Exact trip timing is decision-layer work and does not alter the model freeze.

## Available schedule plumbing
Existing September 29 QA workflows are retained evidence runners with pinned inputs; they are not converted into the recurring scheduler by this contract.
Next-cycle plumbing must:
- acquire and retain newly qualified raw bytes and exact cutoff;
- retain complete S0 prediction/exclusion/chronology/target/feature artifacts, not only the side substrate;
- execute fresh same-cutoff source context;
- independently accept new output bytes;
- only then execute/freeze the exact S2_K1 consumer when its contract permits.

## Governance
This prospective timing correction is authorized operationally. It does not weaken chronology, contamination, acceptance, or evidence-retention gates.
Workflow green is not acceptance.
Prior failed attempts and accepted boundaries remain preserved.
Any future cadence change must again be prospective and documented.

## Immediate frontier
The previous CADENCE WAIT tied to the September 26 seven-day anniversary is superseded as an operating-time constraint by this contract.
Do not create an extra September 29 snapshot merely because this contract exists. The next target is the next normal early-week cycle after the current Week 5 slate, beginning with Sunday postgame closure / Monday source readiness and a preferred Tuesday qualified freeze.
