# CFB Market Monitor audit — 2026-10-23 morning

- Cycle: `CFB_MARKET_MONITOR_20261023T115519Z`
- Audit boundary: `2026-10-23T12:10:50Z`
- Recovered authority: `CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md` blob `a4613c9ecb8a624c8452ccf22d34d26358e0e124`; football-week cadence v1.247 blob `2a41f5cee71152c9f0a84cc3ee2f634020819dc2`; persistence blob `f6143dfddc8cc7cdcb6925d8b096cc9e2d80bc66`; terminal-closure blob `9a2f158beddcde783c25fbecfa6d8d66dd8b2ca8`; neutral-publication blob `33df7ebe6ffe91a520d01eed5e1610e1e7a8c351`; Week 8 profile blob `4ee81ba5ea052364ec81109e0bea4877f7312af8`; CBS-capture procedure blob `ab554daa0446c3fccd27b7026a74700d65bc6daf`.
- RUN_STARTED: `evidence/run_receipts/CFB_MARKET_MONITOR_20261023T115519Z_RUN_STARTED.md`, blob `e7730e6c08db9f4972571fc6520bc897f65a5eb5`, independently read back before external research or canonical mutation.

## Fresh source and qualification

- One complete CBS Week 8 FBS response was recovered by `2026-10-23T11:57:47Z`, mechanically retained as `evidence/operational/CFB_CBS_WEEK8_TEXT_TABLE_CAPTURE_20261023T115747Z.md`, blob `a3b57f1719595bff9c89153e7894ec002f4f14a9`, SHA-256 `82d1d8fa753dc3f597a660fcbe5c6f3bf298216da9d89037a1cd0a15682a7a65`.
- Source URL: https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-8/
- The capture reconciled all 56 accepted Week 8 identities and 112 team rows. Forty-nine games remained future; seven were past/final. No identity was missing.
- Book-icon operators were not independently qualified. Every current quote is therefore `UNIDENTIFIED_FIELD_LEVEL_MIXED_BOOK_FALLBACK_ONLY`; `CONSENSUS_UNAVAILABLE`, Caesars `UNVERIFIED`, and execution `UNVERIFIED` remain binding. Final/Open cells were quarantined from market use.
- Firecrawl retrieval was unavailable because the connected account reported insufficient credits. The complete direct public response was retained instead; this was not treated as a qualified operator-pair consensus or Caesars offer.

## Runtime, lineage and publication validation

- Python 3.12 runtime was proved in this invocation.
- `scripts/cfb_week8_publication.py` ran in normal advance mode with the actual cycle, `as_of=2026-10-23T12:00:35Z`, and honest source recovery bound.
- Accepted original census remained exactly 56 targets / 49 predictions / 7 exclusions. The independent original-archive field invariant passed all 147 frozen numeric fields against the retained archive SHA-256 `772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf`. No REFRESH value substituted for original FIRST_FROZEN.
- Readiness passed with 56 games, 0 open `INCONCLUSIVE`, 47 `PASS`, 5 `CONDITIONAL`, 4 historical gaps, no elapsed current-quote IDs, and no overdue open-decision IDs. `CONDITIONAL_V3_SUPPORTED_WAIT_ADAPTER_OPEN` remains the renderer boundary.
- The neutral publication gate and saved whole-view audit passed. These code/integrity passes were used only with the genuinely fresh source and retained canonical decisions; they were not treated as source acquisition or recommendation evidence.

## Full-slate decision result

Every accepted game was reconciled exactly once across the deterministic day sections. Spread sides, both moneylines, over and under are displayed or explicitly withheld under the saved decision reason. Alternate lines and team totals were not present in the retained qualified response and were not evaluated. No quoted joint parlay price was available; `NO_PREFERRED_PARLAY` is retained because dependence, fragility and duplicated single-game exposure cannot be responsibly priced.

Five existing immutable `CONDITIONAL` reviews remained supported after the fresh board and targeted material check, without a new review, cutoff extension, or threshold relaxation:

| Game | Existing conditional | Fresh fallback display | Venue state |
|---|---|---|---|
| Air Force @ Wyoming | Air Force -5.5, max -105 | -5.5 (-105) | confirmation pending |
| LSU @ Auburn | Auburn +7, max -108 | +7 (-108) | confirmation pending |
| West Virginia @ TCU | West Virginia +10.5, max -105 | +10.5 (-105) | confirmation pending |
| Texas Tech @ Cincinnati | Cincinnati +11.5, max -112 | +11.5 (-111) | confirmation pending |
| Bowling Green @ Buffalo | Buffalo -3, max -112 | -3 (-112) | confirmation pending |

These numerical threshold matches are observations only, not executable offers, instructions to bet, or established tickets. Air Force running back Rocco Conti and Wyoming tight end Gage Brook were reported questionable while Wyoming running back Samuel Harris was reported available; that uncertainty is retained rather than silently cleared. LSU/Auburn absences were also rechecked. No core availability reversal invalidated an existing conditional at this boundary.

The 47 PASS rows were revalidated against the fresh full board and their saved review histories. Missing new game-specific material research remains visible debt rather than proof of no value; no PASS was silently reopened. The card was not padded to ten opportunities.

## Canonical persistence and outcome handling

- Market state: blob `4a3cc373207d6cabf4b7b5d81994a072d1590571`, independently read back.
- Decision ledger: blob `0f2d71d4db499539637379d4de8c289a54d95dc2`, independently read back.
- Current Hot Sheet: `evidence/operational/CFB_WEEK8_HOT_SHEET_2026-10-23_0700CT.md`, blob `2259605a21a257165091b1880010a54e481f8570`, independently read back.
- Exactly-once section counts: Tuesday 3; Wednesday 1; Thursday 3; Friday 5; Saturday morning 9; Saturday afternoon 21; Saturday evening/night 14; unresolved kickoff 0; union 56.
- Scorecard: blob `d210d8c51106ef393a23a4fb69c6fcdb219e3f16`, independently read back after official Thursday finals were joined. East Carolina @ Memphis and James Madison @ Appalachian State were scored only against genuine original FIRST_FROZEN rows. Liberty @ Kennesaw State remained an unscored original exclusion.
- Execution ledger remained blob `75caee4052e02ea7d2453d1d37fd3866e13ecc07`; no new established production or $20 sandbox ticket existed, so no settlement was created.

The first large market-state transfer was accepted by GitHub with truncated bytes. Independent blob readback caught the mismatch before downstream canonical writes. The file was immediately re-fetched and repaired with smaller line-safe chunks to the exact validated blob above. No downstream surface was treated as updated before its own exact readback.

## Earned disposition

All required current canonical surfaces, the sole primary Hot Sheet, fresh source capture, runtime validations, original-lineage invariant and applicable official finals read back successfully. No Champion, FIRST_FROZEN, REFRESH, task, schedule, wager or execution state was mutated outside its governed surface. Terminal-candidate and separate closure remain required after this audit readback.

RUN_PASS_CANDIDATE
