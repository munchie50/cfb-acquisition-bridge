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
