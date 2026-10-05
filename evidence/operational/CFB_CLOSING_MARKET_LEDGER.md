# CFB Closing Market Ledger

Status: ACTIVE APPEND-ONLY OPERATIONAL SURFACE
Initialized: 2026-10-05
Authority: CFB_ENGINE_PROSPECTIVE_BETTING_EVIDENCE_LAYER_CONTRACT_v1_226.md; CFB_ENGINE_BETA_LEARNING_CLOSURE_CONTRACT_v1_231.md.
Scientific effect: NONE.
Champion effect: NONE.

## Purpose
Durable prospective surface for separately qualified closing-market observations. This ledger does not replace FIRST_OBSERVED or INTERMEDIATE market history, Engine decision state, or actual execution state.

## Required fields for a qualified CLOSE observation
- game and market identity;
- closing source / sportsbook or qualified benchmark;
- observation timestamp and timestamp semantics;
- spread/total/moneyline number as applicable;
- associated price/odds where available;
- provenance/evidence reference;
- relationship to any established execution may be evaluated only after both records independently exist.

## Invariants
- Append only. Never overwrite an earlier observation.
- CLOSE is market evidence only and never mutates Champion prediction, frozen fair line, features, scaling, coefficients, or prior decision.
- A later source may not be used to manufacture an earlier close.
- A single sportsbook quote is not silently generalized to the whole market.
- Preserve number and price separately.
- Outcome knowledge never creates or alters a close observation.
- Actual execution evidence remains in CFB_EXECUTION_LEDGER.md, not here.
- If a qualified closing benchmark was not captured prospectively, CLV remains UNVERIFIED.

## Historical initialization
No Week 5 closing observations are backfilled by this initialization. Existing Week 5 market observations remain in CFB_MARKET_MONITOR_STATE.md with their original timestamp/source semantics. Missing Week 5 qualified closes are explicitly UNVERIFIED rather than reconstructed after outcomes.

## Prospective operating rule
Beginning with the next qualified pre-kickoff closing observation, append it here with source/time/number/price/provenance. Downstream QA may compare an independently established execution to an independently qualified close, but no CLV claim is permitted when either side is missing or ambiguous.

Current entries: NONE ESTABLISHED AT INITIALIZATION.
