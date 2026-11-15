# November 15 CFB runtime and CBS collection repair

## CBS collection

Direct CBS Week 11 HTML reproduced the three November 14 collection failures. The capture SHA-256 was `1ebb2843ba90cfe3514e397bf1d0213b2c761a8c21a4a4d603c426013f1f0ac8`. CBS emitted 68 matchup tables for 67 governed games. Ole Miss at Oklahoma (governed game 401856887) had original CBS event 50028715 and rescheduled CBS event 50051570. [Oklahoma Athletics confirms the move](https://soonersports.com/news/2026/11/14/ou-ole-miss-football-game-moved-to-sunday-at-noon) from Saturday 3:15 p.m. CT to Sunday noon CT.

Collector commit `91d1d18677331ae79138f5498a322aaa6021ea5e`, independently read back at blob `c5ec94209c51f9a3addb522e48f5e77438970c81`, excludes only the confirmed obsolete CBS table when both exact event identities occur once. It preserves raw HTML and the existing normalizer guard. Direct-source replay matched 67/67 identities and 134 team rows. An unrecognized conflicting event and a triplicate still failed the identity gate. A historical original-only capture retained the original table.

[GitHub Actions run 43741920414](https://github.com/munchie50/cfb-acquisition-bridge/actions/runs/43741920414) acquired, qualified, uploaded and independently verified collection artifact 14172369234. Optional compiler preflight failed with `elapsed game requires proved prospective PASS`. Manual replay located the first failure at retained historical CONDITIONAL game 401856888. The artifact is collection evidence only. No historical decision was relabelled, no acceptance gate relaxed and no draft was published. The other retained historical CONDITIONAL is 401856858.

## Scheduled worker checkout

The unchanged connector-bound helper at blob `b13930cb714eb87c8dce6136ffab6fbceeb44898` succeeded in the interactive Work Mode runtime at pinned main `7cd98c5af3c5e3dbc827b93e8dd5ac29abab63e6`, with full ancestry and 60 retained immutable review references validated. The Sunday 07 CT scheduled task had stopped at a separate DNS precheck before invoking that helper.

Updated the existing Market Monitor task's startup instruction to run the unchanged verified helper directly, using supported connector transfer or the already accepted immutable REST byte-transfer fallback. The existing direct acquisition path can use the exact CBS projection for the Week 11 collision. Independent lookup confirmed the exact intended prompt, same enabled state, same schedule and same exposed environment assignments. The helper still relies on GitHub connectivity from the executing worker. Natural scheduled checkout and full workload proof remain open. The next scheduled Monitor slot reported at verification was November 15 13:00 CT.

No schedule, task count, Champion, frozen prediction, wager, bankroll, outcome or Hot Sheet mutation.
