# Week 11 Friday review and Market Monitor fallback checkpoint

November 11, 2026, morning CT. Continuation of verified manual recovery de930dd28b4b417299d7dae7befbec0a8cea408e.

## Production worker checkout diagnostic

Fresh authenticated main de930dd28b4b417299d7dae7befbec0a8cea408e, scripts/cfb_runtime_checkout.py. The Work Mode connector returned complete base64 and the documented shell accepted those bytes in the same call. Strict decode and roundtrip, 3780 bytes, binary write/readback, Git blob b13930cb714eb87c8dce6136ffab6fbceeb44898, and equality with the verified worktree all passed. Reused the verified worktree; no second clone or helper execution. This isolates byte transport from helper execution. The unchanged helper itself runs ordinary Git against github.com, so successful transfer can still be followed by clone DNS failure in the scheduled worker. Scheduled-worker fallback availability, verified transfer and clone outcome are separate boundaries. The active production prompt already specifies that ordering and limits. Use the next existing natural invocation to capture those outcomes; no task changes.

## Friday review at the saved 07:32 CT source boundary

CBS source evidence/operational/CFB_WEEK11_CBS_FBS_CAPTURE_20261111T133238Z.md, blob b01695f86fd5fc9aa48d450f18b8303a5bfd3df2. Figures below are displayed mixed-book observations. Retain all three prior PASS decisions and original cutoff fields.

| Game ID / fixture | Reviewed spread, moneyline, total | Disposition |
|---|---|---|
| 401858293 Florida State at Pitt | FSU +3.5/-112, Pitt -3.5/-105; +142/-160; o53.5/-111, u54.5/-120 | Pitt gets a modest price improvement versus the saved -108, with the same spread. Neither moneyline offers enough to reopen the prior QB/run-front assessment. Split total numbers leave competing cases, and the Pitt personnel uncertainty recorded in the post-report reassessment remains applicable pending a newer official update. PASS retained. |
| 401858526 Illinois at UCLA | Illinois +10/-108, UCLA -9.5/-120; +310/-385; o47.5/-110, u47.5/-105 | Illinois gets modest price improvement at the same +10 versus the prior named benchmark. UCLA's official preview corroborates kickoff at 8 PM CT. The retained replacement-QB and UCLA run-defense concerns still constrain Illinois and the over. UCLA lay juice is higher despite the shorter spread, and neither ML nor total clears the prior assessment. PASS retained. |
| 401856860 Houston at Colorado | Houston -9.5/-112, Colorado +10/-114; -370/+310; o51.5/-102, u51.5/-114 | Houston gives one point less than the older screening, at higher juice. This is a reassessment trigger if confirmed in a paired named-book offer with materially supportive matchup evidence. Current source has asymmetric spreads, and ML/total observations supply no independent basis to qualify a change. PASS retained. |

Official sources: https://seminoles.com/game-center/16682 ; https://uclabruins.com/news/2026/11/10/no-4-ucla-hosts-illinois-at-rose-bowl-friday-night ; https://cubuffs.com/game-center/17950 . Saturday checks: https://byucougars.com/news/2026/11/9/byu-football-game-week-2026-baylor ; https://jaxstatesports.com/game-center/8717 ; https://georgiadogs.com/news/2026/11/9/football-returns-home-to-host-missouri-on-saturday ; https://goutsa.com/news/2026/11/02/utsanorth-texas-game-selected-for-espnu-broadcast . These official matchup sources provide schedule or preview corroboration; latest personnel, weather and qualified paired prices remain due within their governing windows. No renewal of the five Saturday conditional reviews or new live sheet publication from this checkpoint.
