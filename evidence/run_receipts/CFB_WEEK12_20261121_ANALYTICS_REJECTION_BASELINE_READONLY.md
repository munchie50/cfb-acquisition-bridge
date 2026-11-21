# Week12 analytics rejection baseline — read-only exact-source census

Status: OBSERVED_READ_ONLY_CENSUS / NOT_ACCEPTED_ANALYTICS / NO_BET.
Source: evidence/operational/CFB_WEEK12_20261120_MANUAL_RENDERED_HOT_SHEET_PREVIEW_NOT_ACCEPTED.md
Source Git blob: 00cb3eac893e34187769b56924e553d52681cb92
As-of: Nov21 2026 recovery continuation. Counts are historical sheet rows, NOT fresh Saturday quote checks.

## Exact rendered-row census
- 70 game rows, broken down Tuesday 3, Wednesday 2, Thursday 1, Friday 6, Saturday 58.
- Decision labels: 68 PASS; 2 HISTORICAL CONDITIONAL — WINDOW CLOSED; 0 INCONCLUSIVE.
- 14 rows retain FIRST_FROZEN EXCLUDED, including 12 Saturday exclusions. Never count these as prediction-backed betting opportunities.
- 6 rows explicitly contain CURRENT QUOTE UNAVAILABLE in the market column. This is a minimum explicit-text count, not a count of venue-qualified quotes.
- 68 rows have CUTOFF_AUTHORITY_UNVERIFIED in the deadline column; the two closed conditional histories have review-evidenced cutoffs. Neither is proof of prospective executable eligibility.
- Primary section is NONE. No accepted fresh book offer or new wager can be inferred from PASS.

## Analytical classification defect
Current PASS combines game review/no-bet decisions with unresolved offer, cutoff, personnel and model/market issues. A numerical ranking of PASS rows would silently conflate missing evidence with rejected EV. Existing frozen point margins and public mixed-book lines do not independently establish calibrated cover probabilities, comparable sportsbook odds or qualified offers.

## Bounded next steps — preserve original selector and Champion
1. Preserve original row labels. Add an independent, NONCANONICAL rejection-reason classification with separate dimensions: original frozen eligibility; decision authority; named-book offer freshness/venue; personnel; model disagreement; value/price; elapsed deadline; canonical publication.
2. Require reason evidence and exact source path/hash per classified row; allow UNKNOWN, never fill missing fields with inference. Independently reconcile counts and overlapping categories against all 70 source rows.
3. Analytics v1: run exact current source and optimization-safe QA in genuine Python; collect exit, stdout, code hashes and readback. Its latest source and identity verifier are BUILT, not production-accepted.
4. Do not certify provisional Markdown as point-in-time market JSONL. Obtain authoritative provider/time/content capture receipts before adapter certification. Keep book, market, side, price unit and quote type isolated.
5. Keep selector/publication recovery as the production critical path. This audit is nonblocking and cannot promote preview, change cutoff, or authorize wagers.

## Drift controls
Do not repeat successful CBS normalization, market hash reconstruction, old DNS checkout or initial compiler. Do not treat historical 68 PASS as 68 picks; 58 Saturday rows as 58 prediction-backed picks; GitHub commit as executed QA; or source-identity hash as quote authenticity. No production task or schedule modified.
