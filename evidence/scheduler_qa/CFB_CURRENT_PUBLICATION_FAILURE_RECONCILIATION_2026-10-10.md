# Current publication failure reconciliation — October10 Test Routine v6

Run: CFB_CURRENT_PUBLICATION_QA_20261010T195627Z
Scope: bounded independent QA of natural scheduled 13:03CT monitor output. Production Routine v5 remains authoritative; v6 remains candidate.

## Trigger, expected and actual behavior
Original GitHub run38074632661/job114278918420 at commitcac1efd07399d049e9d6dca92eb7f88f170d9e0f failed. Expected: current navigation selects one exact current sheet and decision binding; failures stop immediately; accepted frozen values and qualified totals/retention validate independently. Actual: an18:12Z checkpoint existed by the18:09Z validation boundary; future-clock guard correctly rejected it, but tee hid exit status and an empty selection JSON failed later. Natural producer's original RUN_PASS receipts remain historical assertions, not substituted independent validation.
At today's later independent boundary, the future timestamp no longer blocked current selection. The exact header also includes execution identity, which the previously qualified two-reference parser rejected. Parser scope was extended precisely to an optional full40hex execution reference; decision/current-pointer checks retained. No artifact rewrite was needed.
After these repairs, full CI reached the previously unqualified afternoon totals schema and correctly stopped. This newly exposed boundary was qualified separately, rather than bypassing the gate.

## Corrections and proof
- Optional execution-header parser:19 assertions passed, including malformed/duplicate/unknown sources and stale decision rejection; unchanged current sheet binding replay passed.
- Workflow failure propagation: direct JSON redirection replaces tee; controlled bash-e exit37 stops before downstream marker; success emits123. Existing future/reversed-clock guard unchanged; replay at18:09:27Z still rejects original future timestamp.
- Producer authoring instruction: use freshly observed actual UTC for new navigation boundaries, never anticipated completion/title clocks. Installed in active sectioning/output control already recovered by existing tasks. Natural next producer demonstration PENDING; no task mutations.
- Exact afternoon profile:38 modeled Saturday total endpoint displays =28 fresh source-block matches +10 retained morning matches.14 rejection tests passed for endpoint loss, wrong/stale numbers, fresh/retained mislabelling, source/cycle identity, duplicate/omitted game and unsupported Nebraska numeric claims. Nebraska withheld quote is explicit and not counted as a numeric match. Earlier11weekday rows are outside this scoped total comparison.
- Real GitHub push path: run38081980577/job114300612317, commit0d1f5890abaea63b55c6d6ab328d234daa79264c, SUCCESS. All required steps passed, including old regression profiles,19 source-binding checks,14 new afternoon assertions, section counts1/2/3/5/7/17/14, current exact FIRST_FROZEN archive hash772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf,49 rows/147 values/49 favorite directions, and38 afternoon total displays. This is real producer-to-consumer QA execution on existing authentic inputs, not a fresh monitor run.
- Intermediate runs38081840329/38081838421/38081837128 remain failed after exposing totals profile gap. No rerun or changed historical receipt.

## Independently persisted correction identities
- scripts/cfb_hot_sheet_current_decision_binding_gate.py — a42662a37ad83c2eb94f5862c8ed5b8ac5032b91
- scripts/test_cfb_hot_sheet_current_decision_binding_gate.py — 4522ab31278b459e0f3af4c667ba18e501262632
- scripts/cfb_week6_market_total_display_gate.py — ec4824c045dd112c8b48299d40b8ccc68e7e9ef7
- scripts/test_cfb_week6_afternoon_total_display_gate.py — 9a4b89a1680a0bde2aba810bfaa5046ec21a45d5
- .github/workflows/cfb_qa_hot_sheet_kickoff_section_static_gate.yml — 0d7a80957444f8feb943c610125a2346c6fb9412
- evidence/CFB_HOT_SHEET_DETERMINISTIC_KICKOFF_SECTIONING_CONTRACT_2026-09-30.md — bd567cf40d0c7e1f031430a988505d42d682c764

## Preserved state and remaining debt
Current HotSheet unchanged blob1d64f2bc69414ea9816a08eb8fef22edd47decc3; market d25896f5eb476b2c70dae292d7e099627f0f528c; decision8e4ef9544c52cbf0d8b3ce5d0d99fbc6249ff623; execution3e165dec97d2ebe4e595f2109d12c1f7e2d86f4e; scorecard6ae881224fa18b65a4408fa807a2582aebccf6fd. Four enabled production tasks,24 prompt/title/schedule/enabled/timing/timezone comparisons,zero changes. User add-$20 money instruction remains pending classification; no new debit/credit, outcome or wager.
Current binding/section/frozen/total-composition corrections are PERSISTED / READ_BACK / EXECUTED / INDEPENDENTLY_RECONCILED. Overall scheduler/persistence failure class remains OPEN; natural future clock authoring remains DEMONSTRATION_PENDING. Original morning WeeklyQA failure, opaque rejection cause and source-qualified consensus/Caesars availability remain unresolved. Numeric checks do not certify injury/weather/source truth/spread/price/ML/execution availability, calibrated betting quality, settlement, or original13:09 completion. Natural next trigger: existing scheduled monitor, with Health audit preserving original exceptions. No new task, dispatch, source research or competing HotSheet.
Scientific/Champion effect:NONE. No routine promotion.
