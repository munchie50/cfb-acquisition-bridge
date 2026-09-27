# CFB Decision and WAIT Ledger

Status: ACTIVE APPEND-ONLY OPERATIONAL SURFACE
Initialized: 2026-09-27

## Recovery semantics
Canonical durable ledger for prospective BET EARLY / BET NOW / WAIT / PASS / INCONCLUSIVE decisions. Decisions are preserved before outcomes and never rewritten.

## Required decision fields
- decision timestamp CT
- game/market
- linked Champion snapshot
- qualified market observation reference
- decision state
- minimum acceptable line/price where supported
- rationale and maturity
- realistic next execution window

## Additional WAIT fields
- awaited information
- why it matters
- current opportunity/price at risk
- next trigger/review point
- latest useful decision point where supportable
- later disposition: HELPED / HURT / NEUTRAL / UNRESOLVED

## Initial state
No missing historical decision or WAIT state is inferred. Earlier unpersisted states remain UNRECOVERABLE unless separate genuinely pre-event evidence establishes them.

## Write-path validation — 2026-09-27 13:03 CT
- Purpose: controlled repair validation for canonical existing-file mutation.
- Governance effect: none; no decision, execution, settlement, prediction, score, or outcome state created.
- Method: SHA-guarded existing-file update followed by direct repository readback.


## Prospective decisions — 2026-09-27 13:08 CT
Champion snapshot: v1.208 FIRST_FROZEN / v1.193 accepted Beta Champion. Market observation: CFB_MARKET_MONITOR_STATE 2026-09-27 13:08 CT capture. Maturity: OBSERVATION ONLY / betting-layer calibration not yet sufficient to convert raw fair-line disagreement into invented EV or automatic wager authority.

- Alabama at Mississippi State — INCONCLUSIVE. Large Champion/market side disagreement (Champion Mississippi State by 9.865 vs market Alabama -5.5). Await: independent qualified market confirmation plus football/injury/source review sufficient to determine whether disagreement reflects information outside frozen Champion inputs. Opportunity at risk: Mississippi State +5.5. Next review: next governed market-monitor pass; do not chase if the number moves beyond any later-established acceptable threshold.
- Ohio State at Iowa — INCONCLUSIVE. Very large Champion/market side disagreement (Champion Iowa by 6.290 vs FanDuel Ohio State -14.5). Await: independent qualified market confirmation and matchup/injury/source review before any controlled-Beta expression. Opportunity at risk: Iowa +14.5 (-122) at observed source. Next review: next governed market-monitor pass.
- Maryland at Nebraska — WAIT. Champion Nebraska by 10.521 versus market Nebraska -12.5; raw side disagreement is modest and does not itself establish a bet. Await: cross-book confirmation and next information cycle. Current opportunity: Maryland +12.5 (-110); total 52.5 versus Champion 56.012. Next review: next governed monitor pass. Nebraska inclusion preserved regardless of Hot Sheet cutoff.
- Vanderbilt at Georgia — WAIT. Side is near Champion/market alignment; total differs by about 4.06 points (Champion 57.560 vs market 53.5). Await: cross-book total confirmation and matchup/injury review. Current opportunity: total 53.5 (-110). Next review: next governed monitor pass.
