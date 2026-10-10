# Dinner recovery trailing-update guard — October 9, 2026

Run CFB_DINNER_RECOVERY_TAIL_QA_20261010T005738Z; manual Test Routine v6 candidate continuation. Baseline recovery blob 3bec083b711a4bf7828c30ae818dc1d55f2e75d8. Current measured checkpoint clock 2026-10-10T00:59:33Z. Scientific/Champion effect NONE.

## Authentic reproduction

Actual baseline script blob deff4ed43059ebbca74a2ebc9861d4ca812827a5. Existing recovery reader selected explicit 2026-10-10T00:19:31Z checkpoint even though actual full index contained later 19:42:26 and 19:53:50 CT dinner changes. Reproduced locally against full independently fetched baseline bytes: selected_clock 00:19:31Z; newer_dinner_prose_present true; pointer_readback NOT_PERFORMED. This could restore obsolete unresolved/no-recommendation navigation after a complete dinner card. It is a stale-navigation selection defect, not lost canonical decisions or proof of scheduler failure.

## Correction and producer control

scripts/cfb_recovery_navigation_reader.py now refuses ANY non-whitespace trailing content after its last complete explicit checkpoint. It does not guess whether untagged text is material, derive chronology from prose, or certify claims. Horizontal fence whitespace/CRLF handling is explicit. A writer appending later state must reconcile it into a final new tagged checkpoint in the same complete append. Intervening historical prose remains preserved; schema/monotonic clock/pointer validation still applies. Missing/truncated/invalid checkpoint or trailing prose fails closed and directs full manual recovery. This optional helper does not make a task use it automatically.

Source blob b6901d80f3535ee8e218755dda830ef13d3c2869, accepted write commit 298b87940135a977801022fa6d369dd7f83c6b39; tests blob ff71c852841261838d16d3d7a9679be5c4ce37ac, commit 0ae3398dca011ecbefa193ffb1d6fe18665e667f. Both exact-commit and main readbacks match local executed contents.

## Meaningful tests and independent evidence

16 local unit tests PASS (previous ten retained plus six new cases): authentic-style later dinner prose rejected; unclocked comments/headings rejected; intervening prose followed by a newer final checkpoint accepted; harmless trailing whitespace accepted; CRLF supported with same tail rejection; navigation-only/pointer-not-read-back claims preserved. Corrected helper rejects actual baseline full index with 'uncheckpointed trailing content' as expected.

Existing GitHub workflow independently completed success at exact test commit: run38011286883/job114091654286, started 00:58:24Z/completed00:58:33Z. All exposed steps completed success, including navigation regressions, presentation, naming, total-display, frozen archive and retained sheet validation. Workflow unchanged, no dispatch/new schedule. Direct job-log retrieval was rejected INVALID_ARGUMENT; no unobserved exact log/test count or raw log contents claimed. Job-step metadata plus local exact-source execution and immutable readbacks are distinct proof classes.

https://github.com/munchie50/cfb-acquisition-bridge/actions/runs/38011286883

## Dinner-card structural audit

Current card independently fetched blob020a377974b8b04edcc607bf0180da9c0666637c and canonical decision blob6d5f70c5b8c9d0bf49dd8853f581a0357321a497. Full card identity set matches all38 retained Saturday rows, each exactly once. 76 separate side/total verdicts: three conditional Beta side recommendations,35 sidePASS,38 totalPASS; Nebraska separateUNMODELED; all38 named rationale sections exactly once; actual Caesars unverified wording retained. This is structural display/coverage verification only, not full availability verification, optimized cutoff acceptance, calibrated EV or bookmaker execution. Large source URL inventory includes navigation links; mere URL presence is not assessed evidence.

App -10 or better, UMass +4.5 or better, Fresno +7 or better, max -115 each unchanged. Full manual review separately closed RUN_INCOMPLETE at blob65e659e61907e0de77f44a28a8cd19561914e9bc because actual Caesars and final full-team availability/weather remain unverified. Prior narrow four-only result is historical, not erased or upgraded. Original ~13:02 canonical board/15:38 presentation remains historical; no new market retrieval or counter access in this QA run.

## Integration and remaining debt

Append an explicit latest navigation checkpoint to the SOLE current recovery index preserving all old bytes and independently verified current pointers. Include current full-card/decision/closure references, qualitative recommendation maturity and remaining limits. Candidate Test Routine v6 installs trailing-update reconciliation plus declared full-review scope versus actual identity/cardinality checks. Existing holistic QA map records this bounded pass. New index exact-source local execution and independent persistence proofs must be recorded before terminal closure.

CORRECTED / LOCAL_AUTHENTIC_DEFECT_REPLAY_AND_BOUNDARY_TESTS_DEMONSTRATED / EXACT_CODE_READBACK_AND_REPOSITORY_QA_VERIFIED. Natural future consumer invocation remains DEMONSTRATION_PENDING. Automatic casino-trip deadline/full-slate enforcement in existing task prompts remains OPEN; this guard only fixes stale recovery selection, and manual full-card coverage does not close that producer obligation. Production v5/Champion/FIRST_FROZEN/protected studies/task fields unchanged. No actual bet or new decision/quote. This record is evidence, not a second authority doorway.
