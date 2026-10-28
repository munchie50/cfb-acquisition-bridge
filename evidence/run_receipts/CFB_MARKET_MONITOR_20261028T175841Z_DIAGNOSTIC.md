# CFB Market Monitor diagnostic — CFB_MARKET_MONITOR_20261028T175841Z

Recorded UTC: 2026-10-28T18:04:00Z
Run status earned: RUN_INCOMPLETE

## Authority and observability

- Recovered accepted authority: `evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md`, blob `356b5920ab9cba100baa5669588995161585e48b`; active cadence v1.247.
- RUN_STARTED persisted/read back: `evidence/run_receipts/CFB_MARKET_MONITOR_20261028T175841Z_RUN_STARTED.md`; commit `de473e3ceb307a13e1c9e0d528beec503e26ea58`; blob `162778c2fef2bababd13be08d85aae69cac17180`.
- Prior scheduled cycle `CFB_MARKET_MONITOR_20261028T120024Z` remains RUN_INCOMPLETE.
- Unresolved independent STARTED records `CFB_GIT_RUNTIME_REPAIR_20261028T122659Z` and `CFB_MARKET_MONITOR_20261028T124125Z` were observed. No completion was inferred and no code-repair work was overlapped.

## Fresh market and deadline result

- Complete source capture: `evidence/operational/CFB_CBS_WEEK9_TEXT_TABLE_CAPTURE_20261028T180009Z.md`; commit `13911165a231ca86106de729f684d87dde99a829`; blob `8ca38dd69fd9ce1d3c9e80a0291c68fba32ffc04`.
- Coverage: 56 games / 112 team rows. Mixed-book fallback with unidentified constituents; `CONSENSUS_UNAVAILABLE`; `CAESARS_UNVERIFIED`; execution `UNVERIFIED`.
- Complete response recovery finished `2026-10-28T18:00:09.255Z`, nine seconds after the `18:00:00Z` hard cutoff. It is post-cutoff evidence and cannot create, revive or execute a recommendation.
- Pittsburgh post-cutoff fallback `-7.5 -108` failed the original `-6.5 or better / -115 or better` line cap. Review expired history-only; no chase.
- Boston College post-cutoff fallback `+7.5 -114` met the saved numerical threshold only after the hard cutoff. Review expired history-only; no late recommendation or execution.
- The applicable official ACC availability report was not recovered before cutoff. The ACC policy requires reporting beginning three nights before conference football games, but absence of timely recovered evidence is not treated as clearance.
- All 56 identities remained exactly once in the diagnostic view. All future rows retained current descriptive sides, both moneylines and totals. Alternates/team totals were unavailable/not evaluated; `NO_PREFERRED_PARLAY`.
- Post-cutoff diagnostic Hot Sheet: `evidence/operational/CFB_WEEK9_HOT_SHEET_2026-10-28_1300CT.md`; commit `0c311d6e42b2916890d0c5bdc72b56c1c4ef3d79`; blob `e0335ec0addf3c55b0e811c8b7ced574f8a56520`; explicitly UNSELECTED.
- Current user decision: zero active recommendations and zero established Week 9 executions.

## Settlement and scorecard

- Authoritative Tuesday finals were independently recovered from both teams' official athletics sources:
  - Delaware 35, Western Kentucky 21.
  - Sam Houston 3, Missouri State 24.
- Result evidence: `evidence/operational/CFB_WEEK9_TUESDAY_RESULTS_CAPTURE_20261028T180300Z.md`; commit `78d12ad7db1c21b50b5fe5c6170872b4966c09b6`; blob `1f6d0ca4bab568db83582f272de2905b910b43cb`.
- FIRST_FROZEN scorecard append persisted/read back at `fd6529a4ab27ac12d74ace4441005535c605cadb`; commit `3690c3d418e81a29b914adf614affc293657416e`.
- Week 9 Tuesday result: SU `1/2`; margin MAE `20.83`; total MAE `13.89`. Frozen predictions were unchanged.
- No established Week 9 wager existed for either game; execution ledger remains unchanged at `1a938f42e9f03e723bd50348f8a78dbd8b7098e9`.

## Publication blocker

- Actual Python runtime: `3.12.14`.
- Supported local Git checkout: unavailable (`NO_SUPPORTED_GIT_CHECKOUT`).
- Current `scripts/cfb_week9_publication.py` and `scripts/cfb_hot_sheet_readiness.py --profile WEEK9` both failed closed at required immutable-review ancestry validation:
  `git -C <repository-root> merge-base --is-ancestor 37f0e3edf5b09afdc4f05e14e5a70b6d4fa91ab3 HEAD`.
- Classification: `IMMUTABLE_REVIEW_ANCESTRY_UNAVAILABLE`.
- Canonical market and decision streams were not mutated and independently remain at valid typed blobs `2110b9167e823b3169335ffd12e6780b4067f1de` and `8b43d28b71a0e70b12a4cbda3d14e886f13fa110`.
- Because normal compiler/readiness validation did not pass, no governed current Hot Sheet selection, recovery-index transfer/preflight, or selected-publication CI integration was earned.

## Shared Firecrawl budget

Provider balance re-read: remaining/plan `1000/1000`; billing cycle `2026-10-27T17:16:35.203Z/2026-11-27T17:16:35.203Z`; cycle day `1/31`; cumulative release `32`; observed consumption `0`. Unsettled independent recovery work was present and a known upper request cost was unavailable, so no chargeable Firecrawl request was issued. The permitted direct CBS browser fallback supplied the complete board.

## Next safe action

Allow the separately authorized runtime repair to finish and close durably. A later prospective Monitor run must recover its accepted result, use a supported authenticated repository ancestry, acquire a genuinely fresh source, and run the ordinary Week 9 compiler/readiness/publication/index/CI route. Do not reconstruct this missed cutoff, retime the post-cutoff source, revive either expired review or select this diagnostic sheet.

No task, schedule, ownership, billing, model, wager or automation mutation was made.
