# Week12 two-surface isolated tree staging and publication-path boundary

Status: STAGING_TREE_PASS / ORIGINAL_SELECTOR_NOT_EXECUTED / NOT_CANONICAL_ACCEPTANCE.

Main at staging start: `978afd5fca49b9bb7f92edf0e660e25f30e158e8`; base Git tree `972bddbc874870e315f41219fea1564fb0e142e5`.
Isolated candidate Git tree `b618ce07f87d53e87e2352072261f97bc8d38e3b` created via GitHub create_tree and independently read back with exact entries:

- `evidence/operational/CFB_DECISION_WAIT_LEDGER.md` => `98941e228072e6941b1c33e42d4d8dba570f7182` (exact reconstructed ledger)
- `evidence/operational/CFB_WEEK12_HOT_SHEET_2026-11-20_1450CT.md` => `00cb3eac893e34187769b56924e553d52681cb92` (identical bytes to explicit **NONCANONICAL MANUAL RECOVERY PREVIEW — NOT ACCEPTED PRODUCTION**).

The candidate Hot Sheet path matches the existing selector path pattern; this is a path compatibility check, NOT a promotion or claim that a 14:50 CT publication actually occurred. Its filename timestamp is a staging identifier only and must not be used as evidence of deadline compliance. The content remains unaccepted, including no qualified venue offers and no authorized wagers. No main branch ref moved. No current recovery index pointer was changed. The current index still selects Nov19 and old decision blob.

The original selector's publication() requires a freshly parsed index with exactly one CURRENT_HOT_SHEET pointer, the exact reconstructed decision pointer, the exact sheet blob, and audit() of the sheet against the full ledger. A non-main candidate tree cannot by itself satisfy these conditions. Before any production promotion, execute original QA and governance/atomic pointer transaction; never manufacture a past publication time or rewrite accepted history.
