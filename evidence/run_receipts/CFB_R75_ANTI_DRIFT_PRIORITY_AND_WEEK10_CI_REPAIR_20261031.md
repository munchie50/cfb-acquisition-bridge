# CFB R75 — anti-drift priority correction and verified Week10 CI repair

## Drift admitted and bounded
Repeated Week9 outcome polls and exploratory R67–R74 diagnostics displaced the earliest recoverable production dependency. Those records are valid bounded evidence, but they are **not** evidence that the governed full-slate Hot Sheet recovered. Week9 R60 remains RUN_INCOMPLETE; elapsed pregame decision cutoffs must never be repaired retroactively.

## Mandatory continuation priority gate (established routine)
1. Fresh-read authoritative main index/contracts, active production workflow, latest failed execution and CI evidence before selecting work.
2. Rank by **earliest blocking dependency for the next actionable pregame slate**, not by easiest receipt to produce. With Week9 decision windows elapsed, prioritize Week10 acquisition/validation and production execution readiness; capture Week9 outcomes when new finals actually exist.
3. Last-good -> first-bad -> smallest bounded change; KISS first, targeted layered provenance if ambiguous. No new framework or duplicate monitor.
4. Write -> independent readback -> execution/test -> independent CI verification -> acceptance only on green evidence. An unchanged status poll is not a progress checkpoint.
5. Explicitly label BUILT / EXECUTED / VERIFIED / ACCEPTED / PRODUCTION. Never equate shadow quotes, source discovery, or a green unrelated test with an executable sportsbook offer or published Hot Sheet.
6. Four standing production tasks only; no fifth, no model promotion, no hindsight wager authorization.

## Actual CI failure and fix
- Failed Week10 validation run `41243394686`, job `124661743117`, step `Reconcile five captured BetSharp market tables`.
- Exact traceback: assertion that six-game snapshot had 12 displayed and 24 missing branches failed.
- Root cause in `scripts/cfb_betsharp_week10_five_game_reconcile.py`: hardcoded `30-sum(available.values())` used for both five- and six-game snapshots. Six games have 36 possible branches.
- Smallest repair: `expected_games * 6 - sum(available.values())`.
- Code commit `c100f381c52ff35f1b2023cc96cf5eaf3cceae0b`, independently read back.
- New independent GitHub Actions validation run `41248917491`: **completed / success**, same code commit.
- Market evidence remains SHADOW ONLY: six games 12 displayed Kalshi-linked moneylines, 24 missing; five games 10 displayed, 20 missing. No executable sportsbook offers or authorized bets established.

## Next blocker
Week10 canonical 63-game six-branch coverage remains incomplete: 17 CBS-covered games, 46 unpriced games and 276 missing branches in the earlier frozen inventory. Re-read current inventory before claiming exact current counts. Prioritize genuine sportsbook spread/total and moneyline acquisition with provenance, identity, timestamps and user-venue executability checks. Do not run repeated Kalshi-only BetSharp discovery as a substitute.

**Acceptance boundary:** Week10 bounded CI repair is VERIFIED. Week10 production Hot Sheet is NOT thereby ACCEPTED or COMPLETE.
