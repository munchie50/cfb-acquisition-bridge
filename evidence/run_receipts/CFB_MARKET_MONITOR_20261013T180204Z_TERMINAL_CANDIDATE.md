# CFB Market Monitor terminal candidate — 2026-10-13 13:00 CT

- cycle_id: CFB_MARKET_MONITOR_20261013T180204Z
- workflow: CFB Beta Production Market Monitor
- terminal_candidate_at: 2026-10-13T18:08:00Z
- recovered_authority: evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md with active v1.247 football-week cadence and accepted persistence, deterministic kickoff sectioning, terminal closure, neutral publication, and consensus/Caesars controls
- RUN_STARTED: evidence/run_receipts/CFB_MARKET_MONITOR_20261013T180204Z_RUN_STARTED.md
- RUN_STARTED_blob: e434c7b3591ef4dc9a5394f734de3feb7fc86686
- observability_order: PASS — authority recovered before RUN_STARTED; RUN_STARTED persisted/read back before external market research or governed operational mutation

## Persisted and independently read-back governed surfaces

- market: evidence/operational/CFB_MARKET_MONITOR_STATE.md
- market_blob: 242b039554458293ac90172beb8c16ee62a04f0e
- market_result: appended 2026-10-13T18:03:00Z full 62-game CBS board recheck; all earlier qualified observations retained
- decision: evidence/operational/CFB_DECISION_WAIT_LEDGER.md
- decision_blob: 6a05a6f7a58fe8f26606cab70bf7ffaac6cbfdc8
- decision_result: Delaware at Middle Tennessee and Florida International at Jacksonville State prospectively transitioned INCONCLUSIVE to PASS at the governed Tuesday reconciliation boundary
- execution: evidence/operational/CFB_EXECUTION_LEDGER.md
- execution_blob: 75caee4052e02ea7d2453d1d37fd3866e13ecc07
- execution_result: read back; no new established execution, production exposure $0, separate $20 sandbox exposure $0
- scorecard: evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md
- scorecard_blob: 6f7650d340bf63f8f93a2b825e35f8b8e41fa80b
- scorecard_result: read back; no newly final established wager or eligible pre-event FIRST_FROZEN settlement due
- Hot Sheet: evidence/operational/CFB_WEEK7_HOT_SHEET_2026-10-13_1304CT.md
- Hot Sheet_blob: 8649313f2a33be8dca4586b2910df90b8f7247af
- Hot Sheet_result: created and independently read back exact proposed bytes

## Market and decision result

- qualified multi-book consensus: CONSENSUS_UNAVAILABLE
- independently verified actual Caesars execution offer: UNVERIFIED
- fallback: CBS Sports multi-book display with unidentified constituents; explicitly labelled mixed-book fallback, never consensus
- Tuesday Delaware at Middle Tennessee fallback: Delaware -1 (-111), ML -114; Middle Tennessee +1.5 (-114), ML -104; over 47.5 (-114), under 47.5 (-105)
- Tuesday Florida International at Jacksonville State fallback: FIU +3 (-110), ML +128; Jacksonville State -2.5 (-124), ML -148; over 43.5 (-110), under 43.5 (-108)
- Delaware at Middle Tennessee: PASS — no qualified consensus, verified Caesars execution offer, or established acceptable threshold; Delaware QB Nick Minicucci availability remains decision-relevant
- Florida International at Jacksonville State: PASS — frozen Jacksonville State -4.5 versus fallback -2.5 is an investigation flag, not calibrated EV; no qualified consensus, verified Caesars offer, or acceptable threshold
- actionable production wagers: 0
- actionable sandbox wagers: 0
- casino trip: NONE
- settlements: NONE

## Hot Sheet exactly-once assertion

- governed slate cardinality: 62
- unique game identities: 62
- duplicates: 0
- union equals governed slate: PASS
- section counts: TUESDAY 2; WEDNESDAY 2; THURSDAY 3; FRIDAY 3; SATURDAY MORNING 13; SATURDAY AFTERNOON 17; SATURDAY EVENING/NIGHT 22; UNRESOLVED KICKOFF 0
- count sum: 62
- decision-state count: 60 INCONCLUSIVE; 2 PASS
- earliest still-active section: WEDNESDAY
- Nebraska included: PASS — Nebraska at Oregon displayed
- each populated section contains actual game rows: PASS
- required row fields present: PASS

## Integrity and closure gate

- FIRST_FROZEN preserved: PASS — 51 predictions and 11 exclusions; no frozen prediction changed
- accepted REFRESH lineage preserved separately: PASS — no substitution
- earliest qualified observations preserved: PASS
- downstream market, availability, execution, and outcome evidence kept separate from Champion: PASS
- no invented EV, probability, confidence, or price: PASS
- no automatic Champion mutation, Challenger promotion, or scientific acceptance: PASS
- task/schedule mutation: NONE
- canonical market readback: PASS
- canonical decision readback: PASS
- execution readback: PASS
- scorecard readback: PASS
- Hot Sheet persistence/readback: PASS
- terminal blocker: NONE
- next safe action: retain PASS/no-bet for both Tuesday games; the next prospective monitor reconciles the earliest active Wednesday section using new qualified source, availability, consensus, and independently verified Caesars evidence if available
- historical incomplete cycles: unchanged; this cycle does not reconstruct or upgrade them

RUN_PASS