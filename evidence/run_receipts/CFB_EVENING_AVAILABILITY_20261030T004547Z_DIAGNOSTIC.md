# CFB Evening Availability diagnostic — 2026-10-29 CT

- cycle_id: CFB_EVENING_AVAILABILITY_20261030T004547Z
- workflow: CFB Beta Production incremental Evening Availability
- observation_boundary: 2026-10-30T00:47:54.963603498Z / 2026-10-29 19:47:54 America/Chicago
- role: downstream canonical availability and wager-management integrity; not a competing Hot Sheet producer
- repository: munchie50/cfb-acquisition-bridge
- recovered_authority: evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md @ 7eb4671fdc25a37932d0b0ffd1bf69ab6de236e1
- active_cadence: evidence/CFB_ENGINE_FOOTBALL_WEEK_OPERATING_CADENCE_CONTRACT_v1_247.md @ 2a41f5cee71152c9f0a84cc3ee2f634020819dc2
- persistence_authority: evidence/CFB_GITHUB_CONTENTS_PERSISTENCE_PROCEDURE_2026-10-03.md @ 2f601ce18aa220a036fce617ddeea9a2fbfc74f5
- terminal_authority: evidence/CFB_TERMINAL_RUN_RECEIPT_CLOSURE_CONTRACT_2026-10-05.md @ 501cda05d80229402a485493f10b1a4bbb76d3b8
- consensus_caesars_authority: evidence/CFB_CONSENSUS_BENCHMARK_AND_CAESARS_EXECUTION_CONTROL_2026-10-10.md @ c8daffd209ca1575d057b8d73839fa74998ccce6
- typed_publication_authority: evidence/CFB_NEUTRAL_SOURCE_DERIVED_PUBLICATION_CONTRACT_2026-10-12.md @ 29b06d911ee9c10b4314ca296cf0e24ae161d3c7
- complete_response_authority: evidence/CFB_CBS_COMPLETE_RESPONSE_CAPTURE_PROCEDURE_2026-10-14.md @ ab554daa0446c3fccd27b7026a74700d65bc6daf
- shared_budget_authority: evidence/CFB_FIRECRAWL_CYCLE_BUDGET_CONTROL_2026-10-24.md @ d27ff9d78cf84e29a28b906ffe75e6c7895e82cb
- RUN_STARTED: evidence/run_receipts/CFB_EVENING_AVAILABILITY_20261030T004547Z_RUN_STARTED.md @ 96a8edd466f71c538078e2a157527ef9bd5838f5; independent readback PASS

## Runtime repair and authority proof

- independently observed main after RUN_STARTED: 8e86867b2f11da5f18ea6efa7509d781ecdceb96
- current runtime helper: scripts/cfb_runtime_checkout.py @ b13930cb714eb87c8dce6136ffab6fbceeb44898; exact bytes independently matched before execution
- helper result: SUPPORTED_GIT_RUNTIME_VERIFIED
- checkout: full public HTTPS clone, non-shallow, HEAD exactly 8e86867b2f11da5f18ea6efa7509d781ecdceb96
- Python: 3.12.14
- immutable review loader: 30 retained canonical review references verified unchanged
- required compiler/readiness scripts: present
- runtime itself is not the blocker for this cycle

## Fresh complete source capture

A genuinely fresh complete CBS Week9 response was recovered after runtime preparation. The governed table-only response was extracted from that response, then normalized by the current repository normalizer with the accepted Week9 lineage.

- source: https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-9/
- response recovered by: 2026-10-30T00:47:54.963603498Z
- retained complete table surface: evidence/operational/CFB_CBS_WEEK9_TABLES_20261030T004754Z.md @ 55986fa04bb17faf4edfb655ab37a78878b2eb31; independent readback PASS
- normalized packet: evidence/operational/CFB_CBS_WEEK9_CAPTURE_20261030T004754Z.json @ 76d75519f32a80068957a198d3f4d59ba004bb13; independent readback PASS
- table SHA-256: 5463cd0723d827ea0a015d57b763d9b20ccd0b4eb62e82c8fe37ca806fb09d48
- governed games / matched games: 56 / 56
- team rows: 112
- future games / future team rows: 50 / 100
- started-or-past games: 6
- missing identities: none
- Final and Open columns: quarantined
- qualification: UNIDENTIFIED_FIELD_LEVEL_MIXED_BOOK_FALLBACK_ONLY
- consensus: CONSENSUS_UNAVAILABLE
- actual Caesars: UNVERIFIED
- executability: UNVERIFIED
- book update clocks: UNKNOWN

The response proves display completeness and current fallback cells only. Opaque per-cell book icons are not qualified constituent identities, and mixed-book cells are not a consensus pair.

## Current canonical/readiness boundary

Independently read-back canonical surfaces remained unchanged:

- market: evidence/operational/CFB_MARKET_MONITOR_STATE.md @ c6d552a407dafbd2a11c3ac9a1502d459c82c320
- decision: evidence/operational/CFB_DECISION_WAIT_LEDGER.md @ f96ac4add18c2e28a823cefb3a2c5e9670c21064
- execution: evidence/operational/CFB_EXECUTION_LEDGER.md @ 1a938f42e9f03e723bd50348f8a78dbd8b7098e9
- scorecard: evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md @ fd6529a4ab27ac12d74ace4441005535c605cadb
- inherited primary Hot Sheet: evidence/operational/CFB_WEEK9_HOT_SHEET_2026-10-29_1741CT.md @ 026f7298f7f80a546bbb509765c95333948304f0; Evening did not mutate it
- canonical cycle / boundary: CFB_MARKET_MONITOR_20261029T222851Z / 2026-10-29T22:41:03.230751+00:00
- canonical states: 48 PASS, 4 CONDITIONAL, 4 EXPIRED_UNPUBLISHED_REVIEW
- actual audit clock open games: zero; saved conditional windows are closed history, not active opportunities
- elapsed current-quote identity: 401869963 (Troy @ James Madison)
- overdue open decision identities: none
- readiness review_required_game_ids: 49
- packet evaluation coverage: 11 ORIGINAL_EXCLUSION, 4 CONDITIONAL_REVIEW_REFERENCE, 4 EXPIRED_UNPUBLISHED_REVIEW, 37 NOT_CERTIFIED
- kickoff timing for the 37 uncertified rows: KICKOFF_REQUIRES_QUALIFICATION; readiness queue membership is not analytical-review proof

The fresh fallback still displayed UCF +2.5/-104, but its immutable recommendation cutoff was 2026-10-30T18:00:00Z, already past at this cycle. It was not revived, extended, chased, or recorded as an execution. The Troy/JMU conditional was likewise closed and the game had started. No active recommendation was claimed.

## Unfinished research carried honestly

The latest retained targeted follow-up covers seven games but does not prove a complete all-game/all-market current Evening sweep:

- bounded research PASS at capture: Marshall @ Old Dominion, Arizona State @ BYU, Florida @ Georgia
- reconsideration candidate, not issued recommendation: Illinois @ Maryland; Ohio State @ USC under inquiry
- material review pending, not confirmed PASS: Kansas State @ Colorado replacement-quarterback comparison; Missouri @ Arkansas current personnel/role comparison

Those four unfinished cases were not silently rewritten as PASS, promoted to CONDITIONAL, or treated as current recommendations. The earlier 27 bounded qualitative PASS demonstrations remain saved evidence; they do not certify all 49 current readiness rows or current injury/weather coverage. Alternates, team totals and plausible parlays remain unavailable/not fully evaluated where the saved review did not independently cover them.

## Shared Firecrawl budget

- provider plan credits: 1000
- provider observed remaining credits: 1004
- observed cycle: 2026-10-27 through 2026-11-27
- conservative cycle-day bucket: 3 of 31
- released cap: floor(1000 * 3 / 31) = 96
- confirmed/reserved unsettled prior cost retained conservatively: 41
- conservative remaining released allowance: 55
- chargeable Firecrawl calls in this cycle: none

The balance above plan reflects refund/accounting behavior and does not create a quota multiplier. With prior acquisition accounting still unsettled and no independently known upper cost for the complete remaining multi-source availability/weather review, paid work was deferred under the active budget control. The fresh CBS response used ordinary public HTTPS after the governed runtime checkout and did not consume Firecrawl credits.

## Typed downstream handoff result

- scripts/cfb_hot_sheet_readiness.py: executed from the pinned worktree at 2026-10-30T00:55:00Z; saved canonical packets validated at their own boundary
- scripts/cfb_week9_publication.py normal advance: NOT EXECUTED
- reason: all 56 independently earned current decision rows were not available; four targeted cases remained analytically unfinished, 37 packet rows were NOT_CERTIFIED, and current qualified availability/weather plus source constituent identity remained incomplete
- canonical market append: NOT WRITTEN
- canonical decision append: NOT WRITTEN
- execution append: NOT WRITTEN
- settlement append: NOT WRITTEN
- scorecard append: NOT WRITTEN
- competing Hot Sheet: NOT CREATED

Running the compiler with copied prior PASS rows would misrepresent queue membership and saved reasons as current full-slate research. Writing a prose-only tail, forcing PASS, inventing a review, or retiming an expired conditional is prohibited.

## Integrity and earned disposition

- accepted Champion/FIRST_FROZEN/REFRESH lineage: unchanged
- new production execution: none
- new separate $20 sandbox execution: none
- new settlement: none
- new casino trip: none
- invented probability/EV/confidence/stake: none
- task/schedule mutation: none
- four recurring production schedules: preserved
- sole primary Hot Sheet producer: CFB Market Monitor; unchanged

Blocker: CURRENT_FULL_SLATE_DECISION_AND_AVAILABILITY_RESEARCH_INCOMPLETE / TYPED_HANDOFF_NOT_EARNED.

Next safe action: the next prospective producer should begin from the retained fresh 56-game capture and current canonical state, first settle the shared-budget accounting/concurrency boundary, then qualify current injury/weather and source constituents, finish the four named analytical cases and remaining readiness-required rows, supply genuinely earned complete decision rows, and run the normal Week9 compiler. Do not replay this cycle, revive expired conditionals, backfill decisions, or publish an Evening Hot Sheet.

DIAGNOSTIC_ONLY
