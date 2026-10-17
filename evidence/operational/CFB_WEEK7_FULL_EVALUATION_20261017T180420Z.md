# CFB Week 7 Standing Full-Evaluation Audit — 2026-10-17 13:04 CT

Cycle: CFB_MARKET_MONITOR_20261017T175803Z
Status: PUBLICATION_BLOCKED / RUN_INCOMPLETE
Audit boundary: 2026-10-17T18:04:20Z
Fresh source bounds:
- Complete CBS response persisted/read back: evidence/operational/CFB_CBS_FULL_BOARD_TABLES_20261017T180000Z.md; response recovered by 2026-10-17T17:59:40.809Z; 62 governed games; 35 future at capture.
- Complete ESPN board persisted/read back: evidence/operational/CFB_ESPN_DRAFTKINGS_BOARD_20261017T180100Z.md; response recovered by 2026-10-17T18:01:30.034Z; explicitly identified DraftKings pairs; offer-update clocks unknown; actual execution unverified.
- CBS field-level books remain unidentified mixed-book fallback; CONSENSUS_UNAVAILABLE. Caesars was not independently verified; venue confirmation remains pending and is not, by itself, a recommendation blocker.

## Deadline and publication finding

The five earlier CONDITIONAL rows all reached their immutable 2026-10-17T18:00:00Z reconciliation boundary before this audit completed. The accepted V3 renderer rejects CONDITIONAL after that boundary, while the accepted neutral publisher still does not support the richer BET NOW / governed WAIT state needed for three rows whose identified paired prices still met their preserved limits. Downgrading those earned states to PASS merely to fit the schema is prohibited. Therefore no canonical market/decision mutation and no replacement Hot Sheet were published.

Two rows earned prospective PASS / NO CHASE:
- Georgia Tech @ Virginia Tech — preserved limit Virginia Tech -8.5 at -110 or better; fresh identified DraftKings was Virginia Tech -9.5 -110. Do not chase.
- Nebraska @ Oregon — preserved limit Nebraska +6.5 at -110 or better; fresh identified DraftKings was Nebraska +7 -118. The point improved but the price failed the preserved -110 floor. Do not chase.

Three rows require a richer supported decision state rather than forced PASS:
- Penn State @ Michigan — preserved Penn State +6 at -110 or better; fresh identified DraftKings +6 -110.
- UNLV @ Air Force — preserved Air Force moneyline -115 or better; fresh identified DraftKings +102.
- Oklahoma State @ Houston — preserved Houston -4.5 at -110 or better; fresh identified DraftKings -4 -110.

These are evidence-backed transition candidates, not placed bets. No execution, stake, ticket, calibrated EV, or consensus is claimed.

## Exactly-once future-slate evaluation

All 35 future-at-capture governed games were rechecked across spread, total, and moneyline. “PASS” means the continuing prior PASS justification was revalidated against the fresh complete boards; it is not a claim that missing research proves no value.

| Game | Spread | Total | Moneyline | Disposition |
|---|---|---|---|---|
| Auburn @ Georgia | PASS | PASS | PASS | Revalidated |
| Akron @ Miami (OH) | PASS | PASS | PASS | Revalidated |
| Alabama @ Tennessee | PASS | PASS | PASS | Revalidated |
| Georgia Tech @ Virginia Tech | PASS | PASS | PASS | New no-chase PASS |
| Missouri @ Ole Miss | PASS | PASS | PASS | Revalidated |
| Arizona State @ Texas Tech | PASS | PASS | PASS | Revalidated |
| UNLV @ Air Force | PASS | PASS | STATE BLOCKED | Air Force ML met limit; richer transition unsupported |
| Northern Illinois @ Wyoming | PASS | PASS | PASS | Revalidated |
| Toledo @ Eastern Michigan | PASS | PASS | PASS | Revalidated |
| Penn State @ Michigan | STATE BLOCKED | PASS | PASS | Penn State +6 met limit; richer transition unsupported |
| North Carolina @ Duke | PASS | PASS | PASS | Revalidated |
| Tulsa @ Rice | PASS | PASS | PASS | Revalidated |
| Troy @ Louisiana | PASS | PASS | PASS | Revalidated |
| Washington State @ Oregon State | PASS | PASS | PASS | Revalidated |
| Florida State @ Miami | PASS | PASS | PASS | Revalidated |
| Arkansas @ Vanderbilt | PASS | PASS | PASS | Revalidated |
| Arkansas State @ Southern Miss | PASS | PASS | PASS | Revalidated |
| Nevada @ North Dakota State | PASS | PASS | PASS | Revalidated |
| TCU @ Baylor | PASS | PASS | PASS | Revalidated |
| Kent State @ South Florida | PASS | PASS | PASS | Revalidated |
| Kentucky @ Oklahoma | PASS | PASS | PASS | Revalidated |
| Oklahoma State @ Houston | STATE BLOCKED | PASS | PASS | Houston -4 met limit; richer transition unsupported |
| Louisville @ Syracuse | PASS | PASS | PASS | Revalidated |
| Notre Dame @ BYU | PASS | PASS | PASS | Revalidated |
| Wisconsin @ UCLA | PASS | PASS | PASS | Revalidated |
| Elon @ Stanford | PASS | PASS | PASS | Revalidated |
| Louisiana Tech @ UL Monroe | PASS | PASS | PASS | Revalidated |
| Navy @ UTSA | PASS | PASS | PASS | Revalidated |
| San José State @ UTEP | PASS | PASS | PASS | Revalidated |
| Ohio @ Sacramento State | PASS | PASS | PASS | Revalidated |
| Utah @ Colorado | PASS | PASS | PASS | Revalidated |
| New Mexico @ Hawai'i | PASS | PASS | PASS | Revalidated |
| Fresno State @ San Diego State | PASS | PASS | PASS | Revalidated |
| Wake Forest @ California | PASS | PASS | PASS | Revalidated |
| Nebraska @ Oregon | PASS | PASS | PASS | New no-chase PASS |

Exactly-once assertion: 35 unique future game identities; no duplicates; union equals the normalized future-at-capture slate. The remaining 27 governed games had started by the fresh-source boundary and were not outcome-reconstructed.

## Cross-market and parlay disposition

- Totals: 35 assessed; 35 PASS. No total earned a defensible preference over the surviving single-market cases.
- Moneylines: Air Force was the only current price that still met its preserved qualitative limit, but its required post-deadline actionable state is unsupported by the accepted publisher. All other moneylines PASS.
- Plausible parlays: NO_PREFERRED_PARLAY. No qualified quoted joint price was acquired, and correlation, fragility, and duplicate exposure could not be responsibly shown to improve on singles. No joint probability, EV, payout, or stake was invented.
- Earlier analysis: 30 PASS rows were revalidated after the fresh-board material check; Virginia Tech and Nebraska were newly assessed as no-chase PASS; Penn State, Air Force, and Houston were revalidated as price-qualified but publication-state blocked.

## Integrity boundaries

Engine Prediction (Frozen), FIRST_FROZEN lineage, execution ledger, and scorecard were not changed. No ticket or wager was inferred from user intent. No settlement was due from the still-live slate. The stale earlier Hot Sheet remains historical evidence only and was not falsely refreshed or selected as current.

Blocker: POST_RECONCILIATION_ACTIONABLE_STATE_UNSUPPORTED.
Next safe action: qualify and accept a governed richer-state publication profile, or allow the next prospective cycle to use only states supported by accepted authority without extending expired deadlines or relaxing saved limits.

RUN_INCOMPLETE