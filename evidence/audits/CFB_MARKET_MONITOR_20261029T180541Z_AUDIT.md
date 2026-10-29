# CFB Market Monitor cycle audit — 2026-10-29 afternoon CT

- Cycle: `CFB_MARKET_MONITOR_20261029T180541Z`
- Audit boundary: `2026-10-29T18:08:29.097574Z`
- Recovered authority: `evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md` (`d73040c7c308340277e7ff0c4fa178812c093e1f`) and football-week cadence v1.247 (`2a41f5cee71152c9f0a84cc3ee2f634020819dc2`)
- RUN_STARTED readback: `evidence/run_receipts/CFB_MARKET_MONITOR_20261029T180541Z_RUN_STARTED.md` (`09696b8d2ebc6d6f2b532d838b8db147fb1aca4f`)
- Runtime: `SUPPORTED_GIT_RUNTIME_VERIFIED`; helper blob `b13930cb714eb87c8dce6136ffab6fbceeb44898`; pinned worktree commit `84cd4e8e2f52168b3ff1ee0e0b33c4004a96f3ea`; full non-shallow clone; all 28 retained immutable review refs verified.

## Source and budget

- Fresh complete CBS Week 9 response: `evidence/operational/CFB_CBS_WEEK9_TEXT_TABLE_CAPTURE_20261029T180541Z.md` (`26d756d441c4b50fcf85e5bdb76b44af6f6de21d`), provider scrape id `01a188d7-dd69-712c-ae31-193526f6b35a`, recovered-by upper bound `2026-10-29T18:07:07.398Z`.
- Qualified coverage: 56 governed games / 112 team rows; 52 future and 4 elapsed; zero missing game identities. Final/Open columns were quarantined from current-offer use.
- Market class: identified mixed-book fallback. Multi-book consensus was not independently qualified (`CONSENSUS_UNAVAILABLE`); actual Caesars execution offers were not independently verified (`UNVERIFIED`).
- Firecrawl period: `2026-10-27T17:16:35.203Z` through `2026-11-27T17:16:35.203Z`; plan 1000; release through cycle-day bucket 3/31 = 96; observed pre-request use 5; one-credit serial request; post-request remaining 994. No concurrent or unsettled acquisition was observed.
- Supplemental material review used official James Madison, North Texas and UCF preview/schedule pages. No qualified current player-status report was recovered; absence was not treated as player clearance.

## Full evaluation and decisions

- Revalidation: `evidence/operational/CFB_MARKET_MONITOR_20261029T180541Z_REVALIDATION.json` (`552ddfe779b2b7dcc14e9eb36f73bd7cf53d4afa`).
- Price-change audit: `evidence/operational/CFB_MARKET_MONITOR_20261029T180541Z_PRICE_CHANGE.json` (`98df1a42a4714cba00dde610a02acd0ceb090fd6`).
- Readiness audit: `evidence/operational/CFB_MARKET_MONITOR_20261029T180541Z_READINESS.json` (`570bd9ce15b89a92aba9fa7e102ed33d7e5e5031`).
- Every future predicted game was reweighed across favorite spread, underdog spread, both moneylines, over and under. Alternate lines and team totals were unavailable in the qualified packet. Plausible parlay review ended `NO_PREFERRED_PARLAY`; no joint price, probability, EV, payout or stake was invented.
- Result: 50 `PASS`, 2 historical closed `CONDITIONAL`, 4 `EXPIRED_UNPUBLISHED`; zero active recommendations and zero `INCONCLUSIVE`. No expired review was revived and no cutoff was extended.
- Price display changed on 50 games (46 future); the prospective decision set did not change. No established execution or newly settled wager was found, so execution and scorecard surfaces remained unchanged.

## Canonical publication readbacks

- Market state: `evidence/operational/CFB_MARKET_MONITOR_STATE.md` (`60405482a311c8649fe9f798c4c47fddce193ac0`).
- Decision ledger: `evidence/operational/CFB_DECISION_WAIT_LEDGER.md` (`7575796f0681720d4efff2f880d229576a28e1a9`).
- Execution ledger unchanged/read back: `1a938f42e9f03e723bd50348f8a78dbd8b7098e9`.
- Postgame FIRST_FROZEN scorecard unchanged/read back: `fd6529a4ab27ac12d74ace4441005535c605cadb`.
- Hot Sheet: `evidence/operational/CFB_WEEK9_HOT_SHEET_2026-10-29_1308CT.md` (`6cb08167225b27ccf1325210081319cb45bfb6b0`).
- Publication gate: `PASS_CONDITIONAL_CANONICAL_PRESENTATION_ONLY`, exactly 56 games.
- Original archive invariant: PASS, artifact SHA-256 `772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf`, 56 targets / 45 predictions / 11 exclusions / 135 numeric frozen fields unchanged.

Recovery-frontier validation, selected-publication CI and two-phase terminal closure are recorded separately after their independent readbacks.
