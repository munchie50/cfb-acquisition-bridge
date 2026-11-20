# Week12 Nov20 CBS raw board — exact governed lineage identity preflight

**Status: EXACT_DIRECTED_IDENTITY_PREFLIGHT_PASS / PYTHON_NORMALIZER_NOT_EXECUTED / NO PUBLICATION**

## Independent readback and checks
- Read raw source: evidence/operational/CFB_WEEK12_CBS_FULL_BOARD_20261120_MANUAL_0700_CATCHUP.md.
- Read governed baseline: evidence/audits/CFB_WEEK12_CBS_ORIGINAL_LINEAGE_PREFLIGHT_20261115.json (70 rows; authoritative Week12 lineage blob named by cfb_cbs_full_board_normalizer.py).
- Read both alias layers used by normalizer: scripts/cfb_week7_accepted_s0_ancestry_audit.py ALIASES plus Week12 lineage JSON aliases.
- Extracted directed CBS team names from each of 70 raw game table headers and their two team rows; normalized by those two established alias layers; joined exact (away_team,home_team) pair to original governed game_id.
- **70/70** directed pairs matched; **70/70** unique governed game IDs; **0** unknown or reversed directed pairs; **0** unmatched original baseline identities.
- Previously 68/70 matched with only Week12 aliases. Two remaining were UL-Monroe @ App State and Hawaii @ Nevada. Existing shared ALIASES resolves UL-Monroe to UL Monroe and Hawaii to Hawai'i. This is not a new alias/model change.
- Prior structural preflight: 140 team rows, 420 field positions, 4 legitimately UNAVAILABLE moneyline cells (Chattanooga/Alabama and Samford/Auburn).

## Remaining unverified acceptance boundaries
- This is a JavaScript exact-pair identity and market-shape preflight using the existing Python alias contract, **not an execution of Python cfb_cbs_full_board_normalizer.py**. Git blob lineage hash, local source clock, exact source timestamp, and source kickoff status still require governed runtime verification.
- Week12 source_board() enforces 900-second recovered-by-to-proposal freshness. A morning capture cannot qualify a later proposal.
- Source is mixed-book fallback; no venue executable quote, wager or CONDITIONAL promotion.
- Production selector and frozen model are unchanged.
