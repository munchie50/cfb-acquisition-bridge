# CFB Engine Health audit — 2026-10-25

## Result

`RUN_INCOMPLETE`.

Task ownership and schedules remain healthy, all newly due producer/QA invocations have durable start/candidate/closure evidence, and the saved Week9 canonical market/decision packets parse at their own boundary. Current publication integration is not healthy: the newest recovery frontier names market/decision blobs that do not match independent repository readback, exact-frontier CI failed at recovery binding, and the current selected sheet cannot be certified against the saved canonical bytes. Both Sunday Market Monitor cycles and the Sunday Weekly QA cycle also retained their own `RUN_INCOMPLETE` results. Health made no market, decision, execution, scorecard, money, model, Hot Sheet, task or schedule change.

## Authority and observability

- cycle: `CFB_ENGINE_HEALTH_20261025T214139Z`
- audit clock: `2026-10-25T21:44:40Z` / `2026-10-25 16:44:40 America/Chicago`
- recovered repository head before start: `38364f876ea660461a25b5496e217dac0a964078`
- newest accepted index: `evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md` @ `6e011a3fef38ec775e3f0464af6775806ad4bd79`
- cadence v1.247 @ `2a41f5cee71152c9f0a84cc3ee2f634020819dc2`
- persistence procedure @ `27e6500d0e4f001d8f71449e15f813e6fb83bedf`
- terminal closure contract @ `501cda05d80229402a485493f10b1a4bbb76d3b8`
- consensus/Caesars control @ `c8daffd209ca1575d057b8d73839fa74998ccce6`
- neutral publication contract @ `29b06d911ee9c10b4314ca296cf0e24ae161d3c7`
- Week9 profile @ `67b519927f6526cccbb57aec94349de83633c29d`
- coverage/correction authority @ `d17ecae007e6b84413ebe34ec7aaae726eb2e052`
- Firecrawl budget control @ `d27ff9d78cf84e29a28b906ffe75e6c7895e82cb`
- `RUN_STARTED` persisted/read back at `evidence/run_receipts/CFB_ENGINE_HEALTH_20261025T214139Z_RUN_STARTED.md` @ `5b1a18422e3c42c593e6f0168beb9734d0166908` before Health mutation.

No paid research was attempted. The provider balance was already recorded as zero; Health used saved repository, CI and task state only.

## Output ownership and task topology

Independent task readback found exactly four enabled recurring CFB production tasks and one intentionally open task slot:

1. Market Monitor `6ab42966…`: enabled, sole primary Hot Sheet producer, exact 07:00/13:00 CT Sunday–Saturday cadence.
2. Weekly Engine QA `6ab42974…`: enabled, downstream integrity/learning, exact 09:00 CT Saturday/Sunday cadence.
3. Engine Health `6ab4296b…`: enabled, integrity/closure audit, flexible daily 16:30 CT cadence.
4. Evening Availability `6ab4296f…`: enabled, downstream typed handoff, flexible Wednesday/Thursday/Friday 19:30 CT cadence.

Disabled diagnostic tasks remain disabled. No competing Hot Sheet producer, ownership drift or cadence drift was found; no enabled-state restoration or lifecycle mutation was needed. Big Nine remains paused and out of scope.

## Expected-cycle completion since the prior Health audit

The proved prior Health boundary is `CFB_ENGINE_HEALTH_20261024T215052Z`, which itself durably ended `RUN_INCOMPLETE`. Scheduler completion was not used as engine proof.

| Expected cycle | Durable evidence | Original result | Present disposition |
|---|---|---|---|
| Market Monitor 2026-10-25 07:00 CT, `CFB_MARKET_MONITOR_20261025T120550Z` | start `9688a288…`; candidate `3c6acb40…`; closure `574b9f2c…` | `RUN_INCOMPLETE` | Week8 results/scorecard/established-ticket grades and prior frontier closed; Week9 opening research and current Week9 sheet were not earned. Do not replay. |
| Weekly QA 2026-10-25 09:00 CT, `CFB_WEEKLY_QA_20261025T140321Z` | start `292f4169…`; candidate `7e0d6fb7…`; closure `a6d94a44…` | `RUN_INCOMPLETE` | Week8 review and Week5 baseline persisted. Later weekly-selector repair and manual baseline completion are separate remediation and do not upgrade this cycle. |
| Market Monitor 2026-10-25 13:00 CT, `CFB_MARKET_MONITOR_20261025T180321Z` | start `432d7de6…`; candidate `c4e3a546…`; closure `e65abebe…` | `RUN_INCOMPLETE` | Fresh 56-game fallback, canonical packets and sole 13:08 CT sheet persisted; all 56 reviews remained unserved and integration was unproved. Exact CI later completed `failure`, confirming the frontier defect below. |
| Evening Availability | no new cycle due after the prior Health boundary | N/A | Friday cycle remains carried below; next applicable Evening natural proof is not yet due. |

## Current canonical and publication integrity

Independent current readback:

- market actual blob `b96411026e2dc71918c323fc31b48c467fbdc28d`
- decision actual blob `b1b50bb4920cb8e7f543cd5f19b6f979b94f95e4`
- execution `1a938f42e9f03e723bd50348f8a78dbd8b7098e9`
- postgame FIRST_FROZEN scorecard `1e8e0a9c3cd34c163c32f6782cdfccf30b9e13d8`
- money `fc24ea6274160eebfef2ba22fe060deabfe81f9f`
- selected Week9 sheet `evidence/operational/CFB_WEEK9_HOT_SHEET_2026-10-25_1308CT.md` @ `c5c7d2d42a1bb2d56bd60b655d63709057088da3`

The newest recovery frontier instead binds market `3fe4dff0f2057a196f5af3ada2741c6b84e87fd5` and decision `014db27bb226b48681d570029d0fcd8be476d3fd`; neither object exists in current repository history. Current saved-file recovery preflight fails closed at `stale recovery pointer: evidence/operational/CFB_MARKET_MONITOR_STATE.md`. GitHub selected-publication workflow [40220062835](https://github.com/munchie50/cfb-acquisition-bridge/actions/runs/40220062835), job `121249492363`, completed `failure` at step `Validate complete current recovery consumer bindings` for exact frontier commit `452d687e4ee09c11312975c7e2cdafa9d3bb8d12`. Live Week9 gate separately rejects changed prior-week parent bytes; saved-publication ancestry recovery cannot locate the sheet-bound canonical source objects. Therefore the current sheet may be read as a retained saved view, but current canonical binding/readback and selected-publication integration are not certified.

The read-only readiness audit does validate the saved market/decision packets at their own `2026-10-25T18:08:00Z` boundary: 56 games, 56 open INCONCLUSIVE, 45 `NOT_CERTIFIED` original-prediction rows, 11 original exclusions, zero conditional/actionable entries, zero elapsed current-quote identities and zero overdue decisions at 21:44:40Z. Every game still lacks material/rule/market-reference/limits/cutoff review. This is an unserved review queue, not research or football PASS. Consensus remains unavailable and Caesars remains unverified; neither was invented. Nebraska remains in the selected view. Frozen Champion/FIRST_FROZEN/accepted REFRESH lineage was not mutated.

Execution and accounting remain separated: 32 actual tickets / $123.50 historical stake are retained; the completed October23 Week8 batch is score-derived 5–3, $36 stake, $43.75 printed return, +$7.75 result net. Sportsbook adjudication/payment/redemption, available cash and production-versus-sandbox assignment remain unverified. The separate sandbox remains $20 available / $0 assigned; no Week9 execution or overlapping experimental exposure was created. The Week8 scorecard retains 49/49 genuine pre-event original joins and seven exclusions; no outcome-informed reconstruction occurred.

## Evening disposition and carried closure debt

Friday Evening `CFB_EVENING_AVAILABILITY_20261024T012553Z` retains its original `RUN_INCOMPLETE` closure (`c5501406…`). Its closed-conditional compiler defect is not current: PR5 merged, repair closure `CFB_EVENING_REPAIR_20261024T022139Z` exists at `5dc3e574…`, and both Saturday Monitor cycles naturally adopted the repair. Do not request that repair again. Evening-specific natural adoption and sustained reliability remain unproved until a future applicable Evening cycle.

Historical debt remains carried without reconstruction or watermark advancement: Market Monitor Oct9 start-only; Oct12 incomplete; Oct13 readback/navigation unverified; Oct14 normalization incomplete; Oct15 untyped tail; Oct17 afternoon incomplete; Oct18–22 incomplete per receipts; Oct23 morning reported PASS without contemporaneous integration proof; Evening Oct8 closure gap, Oct10 PASS/WAIT conflict, Oct22 incomplete and Oct24 Friday incomplete; Health Oct8 coverage unverified and Oct23/Oct24 incomplete; Weekly QA Oct11 R1 semantic defect. Later successes, repairs or manual work do not close those cycle-specific records.

## Learning follow-through

The fold-in checkpoint and action register now establish the latest boundary; Health did not rerun the baseline:

- `CFB_QA_LEARNING_FOLLOW_THROUGH_20261023`: Weeks4–8 finite numerical baseline complete, 249 unique original predictions, 153/249 direction, margin MAE 14.006623340516, total MAE 13.190502012127, Brier 0.239225353872. Week9 extension is `NOT_YET_DUE` until completion.
- `CFB_QA_QUALIFICATION_LIMITS_REVIEW_20261023`: `KEEP CURRENT LIMITS / PROSPECTIVE DELIVERY PROOF OPEN`. PR10 demonstrated useful classification in one natural Weekly consumer; timely complete producer research remains unproved. The Week8 reconciliation is 38 saved analytical PASS records, two partial reviews, seven exclusions and four permanent gaps—not 40 unreviewed games.
- `CFB_QA_S2_K1_PROMOTION_TRACKING_20261023`: first 44-game prospective cohort scored under separate bounded authority; S2 losses were worse overall than S0 despite one additional margin-direction correct game. Continue in QA/observe; no promotion, threshold change or claimed edge.

The action register was minimally appended and independently read back at blob `6da9726f442db49dc7f535382bc2de35ceede2cd`. Benefit is improved evidence fidelity and an honest negative challenger result; current delivery/integration remains incomplete and predictive/financial benefit remains unknown.

## Blocker and next safe action

Current blocker: `CURRENT_RECOVERY_FRONTIER_AND_SELECTED_PUBLICATION_BINDING_FAILED`, plus `FULL_WEEK9_REVIEW_UNSERVED`.

The next existing Market Monitor should first re-fetch current canonical bytes and make the smallest append-only recovery-frontier correction binding the actual market/decision/sheet blobs; independently rerun complete saved-byte recovery and publication checks and require selected-publication CI success. It must then complete prospective material, all-market, timing and practical-cutoff reviews within the existing decision cadence using released budget or qualified no-charge sources. Do not retime evidence, force PASS, replay failed cycles, extend cutoffs, alter frozen predictions, request the already-completed Evening compiler repair, or change the four-task topology.

`RUN_INCOMPLETE`
