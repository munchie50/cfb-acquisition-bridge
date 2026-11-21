# Week12 Hot Sheet rejection dimensions — second independent read-only pass

Status: COMPLETED_TEXTUAL_CENSUS / NONCANONICAL / NOT A BETTING MODEL.
Exact input: evidence/operational/CFB_WEEK12_20261120_MANUAL_RENDERED_HOT_SHEET_PREVIEW_NOT_ACCEPTED.md
Exact source blob: 00cb3eac893e34187769b56924e553d52681cb92

## Counts, mutually overlapping
- Exact 70 game rows; 68 PASS and 2 HISTORICAL CONDITIONAL WINDOW CLOSED.
- 14 original FIRST_FROZEN EXCLUDED.
- 68 rows explicitly contain CUTOFF_AUTHORITY_UNVERIFIED.
- 70/70 market cells explicitly contain CONSENSUS_UNAVAILABLE.
- 68/70 market cells explicitly contain Caesars UNVERIFIED; this is not an active Caesars requirement.
- 6/70 market cells explicitly contain CURRENT QUOTE UNAVAILABLE; all six are Tue–Thu historical games, so this is NOT a count of currently actionable Saturday quotes.
- 22/70 narrative cells contain the bounded textual regex QB|quarterback|injur|starter|personnel as whole words; only a mention count, NOT verified injury flags.
- 1/70 narrative cells match a narrow textual model/conflict phrase; not a complete model-disagreement census.
- The two historical conditional games are Eastern Michigan @ Western Michigan and Ball State @ Ohio, both expired.

## Interpretation / drift prevention
CONSENSUS_UNAVAILABLE in all 70 does not by itself prohibit action; Caesars is not required. Source text has mixed-book fallback and public aggregates but lacks separately established contemporaneous venue-qualified executable six-market quotes. Do not count 68 PASS as 68 bets, 22 personnel mentions as 22 injuries, or 1 model-conflict mention as evidence that only one model conflict exists. All categories overlap.

## Next smallest engineering delta
Produce structured, separately auditable rejection reason records from typed decision packets rather than NLP heuristics on a rendered preview. Use UNKNOWN when the typed source lacks authority. Do not modify original selector or market/decision ledger to accommodate provisional analytics. First finish original canonical selector/publication acceptance; then run latest analytics Python QA and independently certify provider/source/time before adapting market rows.

## Scope
Read-only independent second-pass check; no production ledger/pointer, Champion, task, schedule, deadline or wager modified.
