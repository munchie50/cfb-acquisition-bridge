# CFB Week 8 game-day pre-kickoff QA — 2026-10-24

**Cycle:** `CFB_WEEKLY_QA_20261024T140313Z`  
**Mode:** Saturday CFB game-day pre-kickoff QA  
**Audit boundary:** `2026-10-24T14:13:13Z` / `09:13:13 CT`  
**Scope:** integrity, breadth and established-ticket risk QA only; not a competing Market Monitor or Hot Sheet producer.

## Authority and observability

- Deterministic current doorway: `evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md`, starting blob `e3a7e180004b745ed2bcfefbe03d8b098a55140d`.
- Active cadence: `evidence/CFB_ENGINE_FOOTBALL_WEEK_OPERATING_CADENCE_CONTRACT_v1_247.md`, blob `2a41f5cee71152c9f0a84cc3ee2f634020819dc2`.
- Active persistence / terminal-closure / consensus-Caesars / neutral-publication / Week8-profile controls were independently recovered from current `main` before research or mutation.
- `RUN_STARTED` was created and independently read back at `evidence/run_receipts/CFB_WEEKLY_QA_20261024T140313Z_RUN_STARTED.md`, blob `1aecd6244759186d3fa75641c319a1b6b05d3b2b`.
- Latest upstream Monitor cycle `CFB_MARKET_MONITOR_20261024T120126Z` has a separate read-back terminal candidate and closure ending `RUN_PASS`; this QA does not upgrade or replace it.

## Canonical readback and saved-view integrity

| Surface | Current blob | QA result |
|---|---|---|
| `CFB_MARKET_MONITOR_STATE.md` | `9acab4ebdefa407ae862cac0193bf2c11767df47` | Week8 packet retained; current numerical boundary 07:10 CT. |
| `CFB_DECISION_WAIT_LEDGER.md` | `8e7a93341ffeb28d1751971c998e4eccbf51b638` | 47 PASS, 5 historical closed CONDITIONAL, 4 permanent historical gaps; no open/overdue decision. |
| `CFB_EXECUTION_LEDGER.md` | `a28404143930aeadef5d9d9b678ffb66ce39cc74` | Friday tickets graded 0-2 / -$8 result net; six Saturday tickets remain open for $28 stake. Book payment remains unverified. |
| `CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md` | `a22d6e45bc9f499213bb35b288da12ccc494a130` | Friday finals joined only to genuine original FIRST_FROZEN; one original exclusion retained. |
| `CFB_MONEY_LEDGER.md` | `fc24ea6274160eebfef2ba22fe060deabfe81f9f` | October23 $61.30 complete-pot baseline retained; not recomputed without sportsbook settlement/current holdings. Sandbox remains separately $20 ceiling / $0 assigned. |
| Current sole Hot Sheet | `15893bd343c6d216eeddaf8a905081f199271816` | 56 games exactly once; zero actionable opportunities; no unresolved kickoff. |

`cfb_saved_publication_audit.py --profile WEEK8` passed saved publication integrity: 56 games, exact sheet blob, no elapsed-current-quote IDs and no overdue-open-decision IDs. `cfb_recovery_consumer_preflight.py` passed 166 current pointers and selected the exact 07:10 CT sheet. The readiness audit separately reported 56 games / 47 preserved PASS / 5 historical closed conditional / 4 historical gaps / 0 open games. Queue membership is not analytical review evidence.

After full Git ancestry was recovered, 151 targeted readiness, saved-publication, renderer, closed-conditional, recovery, scope, decision-binding and execution-aware tests passed. An earlier local attempt failed because the existing clone was shallow and lacked authenticated historical commits, and because the accepted archive environment variable was not supplied; that attempt did not mutate repository state. No test result is treated as fresh source acquisition or recommendation acceptance.

## Fresh Saturday evidence and established-ticket risk

The 07:04 CT complete CBS capture remains the canonical Monitor observation. QA re-opened the current CBS Week8 page at approximately 09:05 CT for a bounded spot check. The display remains an unidentified mixed-book fallback: `CONSENSUS_UNAVAILABLE`, actual Caesars `UNVERIFIED`, operator/update clocks unknown, and executability unverified. It is not a new canonical market baseline.

| Open ticket | Accepted ticket | Fresh fallback display | QA disposition |
|---|---|---|---|
| Auburn vs LSU | Auburn +7.5 / -110 | Auburn +7.5 / -118 | Ticket retained; no new wager. Final LSU/Auburn reporting adds asymmetric personnel risk: LSU TE Trey'Dez Green and two defensive linemen were absent from the final out list, while Auburn OL Tai Buster is out. This is adverse uncertainty for the held Auburn position, not authority to reopen or hedge. |
| Cincinnati vs Texas Tech | Cincinnati +11.5 / -106 | Cincinnati +11.5 / -110 | Ticket retained; slightly better accepted price. No qualified new availability fact changed the canonical closed window. |
| West Virginia at TCU | West Virginia +10.5 / -108 | West Virginia +10.5 / -108 | Ticket retained; no change at the checked fallback. Existing competing explosive-offense/TCU-defense mechanisms remain. |
| Buffalo vs Bowling Green | Buffalo -3 / -115 | Buffalo -3 / -111 | Ticket retained; same line and a cheaper unidentified fallback price after execution do not create a second wager or CLV claim. |
| UCLA vs Michigan State | UCLA -14.5 / -112 | UCLA -16.5 / -108 | Ticket retained; accepted line is two points better than the fallback display. Official Big Ten availability reporting exists, but no independently extracted player-level change was earned in this bounded QA. |
| Texas vs Ole Miss | Texas -3 / -115 | Texas -3 / -112 | Ticket retained. Fresh reporting identifies Texas edge Colin Simmons as questionable with a high-ankle sprain and Richard Wesley out; this is adverse pass-rush uncertainty for the held Texas position, not an invented hedge or state mutation. |

Game-window weather was sunny/mostly clear at the six ticket venues in the retrieved hourly forecasts. No weather emergency or automatic total/spread change was earned. Alternate spreads, alternate totals and team totals were not available in the retained complete response. No qualified joint parlay price/dependence/exposure review exists; `NO_PREFERRED_PARLAY` remains valid.

## Breadth, timing and learning assessment

- Production delivered an exact 56-game typed view and a same-response numerical sweep across both spread sides, both moneylines, over and under for all 44 games that were future at the 07:04 CT capture.
- Production did **not** deliver fresh team-specific material research for all 44 future games. The Monitor itself labels that debt honestly. Missing research is not proof of no value, and the readiness queue does not cure it.
- The user's Friday 19:00 CT placement cap and each original conditional cutoff are closed. This QA cannot silently reopen, extend, relax or chase them. The practical consequence is zero new actionable opportunity at this boundary, not a claim that every late Saturday market was exhaustively researched.
- The four missed Tuesday/Wednesday identities remain historical gaps, not PASS. Five conditional rows remain historical/window-closed; actual tickets remain separate execution evidence.
- S2_K1 promotion tracking advances no further today: the accepted 44-game prospective study cohort is frozen pre-event and remains `OBSERVE / CONTINUE IN QA`. Target-outcome scoring is not yet authorized, and no prospective accuracy, edge, promotion date or production effect is claimed.
- Champion v1.193, original FIRST_FROZEN 49-prediction/7-exclusion Week8 lineage, accepted REFRESH, TIME-HIDDEN layers and all four task schedules remain unchanged. Big Nine remains paused and out of scope.

## QA disposition

No canonical market, decision, execution, scorecard, money, model or Hot Sheet mutation was earned. The correct user-facing state is: **no new bets, no chase, six established Saturday tickets remain open, and two held positions carry newly visible personnel risk (Auburn and Texas).**

Next safe action: the sole Market Monitor may use later genuinely qualified source/review evidence prospectively, while preserving all original limits and closed cutoffs. Sunday Weekly QA may score only authoritative finals against genuine pre-event FIRST_FROZEN and established executions; S2 scoring remains separately gated.

External evidence recovered during this QA:

- Current CBS Week8 board: https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-8/ (opened 2026-10-24 approximately 09:05 CT; lines subject to change; unidentified mixed-book fallback).
- Final LSU–Auburn availability reporting: https://www.andthevalleyshook.com/lsu-tigers-football/54682/fridays-lsu-vs-auburn-injury-report-treydez-green-still-not-listed (published/recovered 2026-10-24).
- Texas pass-rush availability context: https://www.burntorangenation.com/texas-longhorns-football/106184/texas-longhorns-pass-rush-injuries-colin-simmons (published 2026-10-23; recovered 2026-10-24).
- Official Big Ten availability-report doorway: https://bigten.org/fb/availability-reports/ (recovered 2026-10-24; player-level UCLA–Michigan State extraction unavailable in this bounded pass).

QA_RESULT: PASS_PENDING_DURABLE_TERMINAL_SEQUENCE
