# CFB Week 9 R43 — complete official Big Ten Friday-summary versus archive cross-view reconciliation

**RUN_INCOMPLETE. This is material personnel-source reconciliation, not certified betting decisions or model changes.** Prepared 2026-10-31T05:48:35.869Z UTC. Source retrieval clocks below are observation times only, not official report issuance or sportsbook operator update times.

## Authority and verified continuation
Fresh main before write `0276da03e503b2900bdd4f09a976d2f5b2dde7ea`, R42 independent receipt blob `c7af3464e3d9dbb8f9c067593a7cccad6478b921`; R41 independently verified `077270dce72e72350fa84f70c131e25dbf94d050`; R14 accepted case frontier `757811e4a6a5028e2d274edaf417706f79cac46a`; R24 manual-producer correction `01ef94397d3d38d6a3592700d424ab687df312af`; accepted Oct27 S0 source and original frozen values unchanged. Last-good is Oct29 governed manual comparative-review publication; first-bad remains lack of current 56 qualified six-market decisions and 35 certified prospective packets, executable venue evidence and fresh full-slate source. No selector, QA, historical CBS normalization or historical review replay performed.

## Systematic source delta (independent targeted read)
- **Official Friday 10/30 summary** https://bigten.org/fb/availability-reports/ live scrape `01a19080-5cda-747a-8c02-d09d82bfcd7f`; **official linked archive** https://app.hdintelligence.com/?conf=B10&source=B10&sport=Football&type=archive live scrape `01a19080-5cd8-7322-a484-83e8e6d9bbb8`; both retrieved by **2026-10-31T05:48:14.273Z**.
- Deterministic read-only parsing of labeled Friday team/status/player groups produced **169 player rows**; archive contained **170 October31 rows**; **165 exact team/player matches**, **20 different Friday-status vs archive Update1-status values**. Four unmatched names were Jo'Ziah Edmond, Joey Kopec, Messiah Hampton, Alex McLaughlin; do **not** infer their status change from this crosswalk. Archive Update2 and Game Day columns still blank for compared rows.
- This is **cross-view discrepancy evidence**, not 20 verified chronological changes, not final game-day clearance and not a calibrated model-impact update. The live official Friday summary is explicitly labeled **FRIDAY REPORT 10/30/26**; the archive's Update1 entries can lag. Use explicit view and status, never silently overwrite one with the other.

| Team | Player | Official Friday 10/30 summary | Official archive Update1 | Week9 review implication |
|---|---|---|---|---|
| Wisconsin | Barrett Nelson | OUT | Doubtful | Wisconsin @ Iowa: OL availability |
| Iowa | Cody Haddad | OUT | Doubtful | Wisconsin @ Iowa: DB availability |
| Iowa | Brevin Doll | OUT | Doubtful | Wisconsin @ Iowa: RB availability |
| Iowa | Emmanuel Olagbaju | OUT | Doubtful | Wisconsin @ Iowa: DL availability |
| Illinois | Katin Houser | QUESTIONABLE | Doubtful | Illinois @ Maryland: QB uncertainty; already considered original Houser injury |
| Maryland | Sean Williams | OUT | Doubtful | Illinois @ Maryland: WR downgrade |
| Maryland | Trevor Szymanski | OUT | Doubtful | Illinois @ Maryland: OL downgrade |
| Maryland | Ryan Manning | PROBABLE | Questionable | Illinois @ Maryland: WR improvement |
| Rutgers | KJ Duff | QUESTIONABLE | Doubtful | Other Week9 game; do not invent 35-case qualification |
| Minnesota | Garrison Monroe | OUT | Questionable | Other Week9 game |
| Minnesota | Pierce Walsh | OUT | Doubtful | Other Week9 game |
| Northwestern | Brendan Flakes | OUT | Doubtful | Other Week9 game |
| Northwestern | Robby Preckel | PROBABLE | Questionable | Other Week9 game |
| Purdue | Jaden Mangham | DOUBTFUL | Questionable | Purdue @ Penn State: DB downgrade |
| Purdue | De'Nylon Morrissette | DOUBTFUL | Questionable | Purdue @ Penn State: WR downgrade |
| Penn State | Alijah Carnell | OUT | Doubtful | Purdue @ Penn State: DT downgrade |
| Penn State | Koby Howard | DOUBTFUL | Questionable | Purdue @ Penn State: WR downgrade |
| Ohio State | Jay Timmons | DOUBTFUL | Questionable | Ohio State @ USC: CB downgrade, does not establish U51.5 edge |
| Washington | Trey Cooley | PROBABLE | Questionable | Washington @ Nebraska: RB improvement |
| Nebraska | Vincent Shavers Jr. | PROBABLE | Questionable | Washington @ Nebraska: LB improvement |

## Case-level decision-gate implications (existing manual review, no duplicated numerical preflight)
- **Maryland +2.5** (ID 401858503) **NOT APPROVED**; original **2026-10-31T14:00Z / 09:00 CT** cutoff immutable. Official Friday Houser QUESTIONABLE versus archived DOUBTFUL is now source-labeled; Maryland Williams and Szymanski Friday OUT, Ryan Manning PROBABLE. Original frozen Maryland home margin +6.678 vs accepted Oct27 -3.246 remains a 9.924-point reversal. These official player changes cannot be converted into an invented calibrated Champion probability or automatic +2.5 approval. User venue executable quote/limit absent.
- **Wisconsin @ Iowa** (401858502) remains NOT_CERTIFIED across all six branches. Four Friday OUT vs archived DOUBTFUL statuses affect both sides. Prior frozen/Oct27 raw totals ~47 vs public 36.5 do not by themselves earn an over.
- **Purdue @ Penn State** (401858506) remains NOT_CERTIFIED across all six branches. Four Friday status discrepancies (two Purdue, two Penn State) increase material personnel-review need; prior home-margin shift +20.646 to +8.797 is not a calibrated cover edge.
- **Ohio State @ USC Under51.5** (401858509) **NOT APPROVED**; original **2026-10-31T20:00Z / 15:00 CT** cutoff immutable. Ohio State Jay Timmons Friday DOUBTFUL vs archive QUESTIONABLE; QB Sayin OUT and other material absences previously established. Frozen total 58.139, Oct27 56.417: both exceed proposed under51.5; no certified under advantage or executable venue quote/limit.
- **Washington @ Nebraska** (401858504) remains NOT_CERTIFIED; two probable vs questionable cross-view differences. Washington QB Demond Williams Jr. remains PROBABLE, not independently starter-certified. No raw-model-to-bet shortcut.
- **UConn @ Air Force** (401861966) remains NOT_CERTIFIED; Medders OUT, Johnson/Fisher replacement unresolved; this Big Ten source audit does not close Air Force QB.

## Attempt ledger / next eligible work
| Action | Outcome | Precise blocker | Next |
|---|---|---|---|
| Parse Friday official source and archive as separate views | 169 Friday, 170 archive, 165 exact matches, **20 cross-view differences**, 4 unmatched | Archive update1 lag; final game-day columns blank; names unmatched | Carry explicit status and source into affected existing manual reviews; do not infer chronological publication timestamps |
| Apply to relevant five outstanding games | Maryland, Wisconsin/Iowa, Purdue/PSU, OSU/USC, Washington/Nebraska material review flags refined | No calibrated personnel-adjusted Champion six-market decisions or executable venue quotes/limits | Prioritize original cutoffs, actual venue proof and source-qualified final reports |
| Preserve unaffected other cases | R37 35 cases/192 preflight branches and R39/R40 16 material saved-drift reconciliations unchanged | 0/56 qualified current rows, 0/35 packets | Do not redo prior verified preflights |
| Guarded publication and selected CI | NOT ATTEMPTED | Contract gates, 900s CBS source, venue and authentic 56 decisions absent | Serial publish only when genuinely qualified |

**All 20 discrepancies are source-evidence updates, zero betting certifications, zero approved bets.** Canonical market/decision/Hot Sheet/index/prediction pointer not modified. Four standing schedules and existing temporary rescue task not modified. **Next entry:** Maryland before 14:00Z, earliest 16:00Z cases, Air Force QB, Ohio State-USC before 20:00Z, then remaining prospective cases; no retrospective approvals. Disable temporary rescue when no useful authorized Week9 work remains. **RUN_INCOMPLETE.**
