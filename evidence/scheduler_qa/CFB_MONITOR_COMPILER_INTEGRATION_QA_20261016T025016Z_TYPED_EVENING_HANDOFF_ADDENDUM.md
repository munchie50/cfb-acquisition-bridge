# Typed Evening handoff integration addendum

Cycle: CFB_MONITOR_COMPILER_INTEGRATION_QA_20261016T025016Z
Scope extension: prevent the EXISTING downstream Evening producer from reintroducing an untyped canonical tail after the verified Monitor repair.

## Bounded implementation

V2 cycle allowlist now additionally accepts actual CFB_EVENING_AVAILABILITY_<UTC> identities. V1 remains Monitor-only. Unknown producer families remain rejected. No quote/decision/frozen/source/execution validation is weakened. Existing normal compiler can therefore consume complete typed current canonical records, a fresh complete source response and all independently earned decision rows under an Evening identity, then the next Monitor can consume that typed packet under its own identity. Generic arbitrary legacy/untyped-tail interpretation remains unsupported and fails closed. This closes the future known producer format gap by preventing the tail, not by discarding an existing tail.

Exact installed/read-back:
- scripts/cfb_neutral_publication_gate.py @3f85e1b2fb65500c0c52c93131582b56a0554f7c
- scripts/test_cfb_neutral_weekly_reconciliation.py @d5c5b6c35b948686d21f1d0399d5e539beebf25a
- unchanged normal compiler @5fe98c5a05e6ecee92f659823fe28eece9398d9c
- active contract @a75e5eb3e2e6e66aaa081c4ce186f04fd3356b48

Three new tests cover own-identity Evening-to-next-Monitor packet chaining, V1 rejection of Evening identity, and unknown-family rejection. All73 local current/new tests PASS; original12legacy and25full-board fixtures remain in existing CI. Independent complete CI for final installation is recorded in terminal closure.

## Existing task integration

Preserved the entire existing Evening Availability prompt and appended this exact typed handoff/runtime instruction:

> TYPED DOWNSTREAM HANDOFF — USER-DIRECTED QA INTEGRATION: Recover evidence/CFB_NEUTRAL_SOURCE_DERIVED_PUBLICATION_CONTRACT_2026-10-12.md including the qualified V2 Evening-to-Monitor handoff and evidence/CFB_CBS_COMPLETE_RESPONSE_CAPTURE_PROCEDURE_2026-10-14.md, or accepted superseding controls. After authority recovery persist/read back the actual cycle RUN_STARTED before operational mutation. Verify a supported computation runtime in THIS invocation before canonical publication mutations; if unavailable report COMPUTATION_RUNTIME_UNAVAILABLE / RUN_INCOMPLETE with truthful permitted terminal closure, never simulated execution or untyped substitute updates. When current neutral weekly V2 scope applies, consume the latest complete typed Monitor/canonical state; retrieve and retain a genuinely fresh complete source response, supply all governed independently earned decision rows including material availability/provenance, and execute scripts/cfb_neutral_weekly_reconciliation.py normal advance with the ACTUAL CFB_EVENING_AVAILABILITY_<UTC> cycle, actual as_of and honest recovered-by bound. Inspect complete proposal validation before serial SHA-guarded market/decision writes and independent readbacks. End each applicable append with the validated typed boundary; do not leave a prose-only tail for the next Monitor to repair. Never use --bootstrap-saved, disguise this run as a Monitor, discard an existing untyped tail, force PASS, extend deadlines automatically or downgrade richer facts to fit neutral scope. A pre-existing unsupported tail/phase requires qualified reconciliation or RUN_INCOMPLETE. Preserve all source, consensus/Caesars, cutoff, execution/settlement and scientific boundaries. Do not create, select or publish a competing Hot Sheet: canonical typed packets are the downstream handoff, and the next scheduled Monitor remains sole primary sheet producer. Scoped Evening completion does not upgrade an earlier sheet or Monitor failure. Natural runtime/handoff adoption must be demonstrated, not inferred from installed instructions.

Both actual-invocation computation and genuine fresh source recovery remain required; source/cutoff/execution/decision qualification remains separate. If unavailable or unsupported, honest RUN_INCOMPLETE, never a prose substitute or fabricated Monitor identity. Evening must persist typed canonical updates only and never create/select/publish a competing Hot Sheet. Monitor retains sole primary publication ownership. Prior material availability/reasons must be retained in applicable canonical fields.

Independent task readback after BOTH integrations: all11 identities preserved, exactly4enabled recurring tasks, every title/schedule/timezone/timing/enabled field unchanged. Only Market Monitor and Evening Availability prompt suffixes changed. All original prompt bytes retained as exact prefixes; Health/Weekly and disabled diagnostic prompts unchanged. No new task, dispatch, schedule/ownership change or sign-in action.

Current market2daa4415d1c2877fa27af207d1678c41863f5b06, decisiond09c1cbdb17111fcfa67c0f01df6c2e2bf0d9e46 and primary sheet7089e9253ce6bca81210f3227e7b0d1e748f78ad are unchanged by this integration. No prediction/model/Champion/FIRST_FROZEN/REFRESH/wager/scorecard/money mutation.

This is installed protocol and task guidance. Scheduled runtime availability and natural typed Evening-to-Monitor adoption remain UNPROVED until real existing invocations demonstrate them. First due Monitor remains FridayOctober16 07:00CT; Friday Evening remains its existing flexible19:30CT cadence.
