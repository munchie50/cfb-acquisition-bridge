# CFB_MARKET_MONITOR_20261028T120024Z terminal candidate

Recorded UTC: 2026-10-28T12:17:00Z
Final terminal state: RUN_INCOMPLETE

Prospective start:
- path: evidence/run_receipts/CFB_MARKET_MONITOR_20261028T120024Z_RUN_STARTED.md
- commit: 12da49afd6f230d286987575f4ba06dfb02f5a54
- blob: d5b1fdd1bc335b4135685cad675262ae5d0bbbf0
- independent readback: PASS

Authority:
- current recovery index: evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md
- recovered index blob: 356b5920ab9cba100baa5669588995161585e48b
- cadence: v1.247
- original Week 9 lineage: 56 targets / 45 predictions / 11 exclusions; frozen fields unchanged

Fresh evidence:
- complete source: evidence/operational/CFB_CBS_WEEK9_TEXT_TABLE_CAPTURE_20261028T120000Z.md
- source commit: d6dc2a3d26ce0d20d7684e65cb622c8f2748bbff
- source blob: b55854c08e51602c2e36b92f405f83394cccc0b8
- response recovered by: 2026-10-28T12:04:37.444Z
- coverage: 56 games / 112 team rows
- qualification: MIXED_BOOK_FALLBACK; CONSENSUS_UNAVAILABLE; CAESARS_UNVERIFIED; EXECUTION_UNVERIFIED
- no chargeable Firecrawl request; plan/remaining 1000/1000; cycle day 1/31; released cap 32; observed consumption 0

Decision result:
- NO_MATERIAL_DECISION_CHANGE
- Pittsburgh conditional limit -6.5 or better at -115 or better; fresh fallback -7.5 -108 fails line cap
- Boston College conditional limit +7.5 or better at -115 or better; fresh fallback +7.5 -124 fails price cap
- official ACC Wednesday availability reports not yet posted at review boundary
- original noon CT reconciliation / 1:00 PM CT hard cutoff unchanged
- all sides, both moneylines and totals rechecked; no new earned state
- alternates/team totals unavailable or not evaluated; NO_PREFERRED_PARLAY
- no execution, money movement, settlement, model or Champion mutation

Durable diagnostic evidence:
- diagnostic: evidence/run_receipts/CFB_MARKET_MONITOR_20261028T120024Z_DIAGNOSTIC.md
- diagnostic commit: ca130974705eb2744bb64c7d38ff9dc0d73816fc
- diagnostic blob: 9671ee8ad294d55307d2c4f4a38fac62f5ff622a
- candidate full-board view: evidence/operational/CFB_WEEK9_HOT_SHEET_2026-10-28_0700CT.md
- candidate blob: a73692ca20b141ffb830d6b5c17ce8b85df6294e
- candidate status: UNSELECTED_DIAGNOSTIC_ONLY
- exactly-once candidate assertion: PASS, 56 unique identities, section total 56

Canonical integrity:
- market restored/read back exact blob: 2110b9167e823b3169335ffd12e6780b4067f1de
- decision restored/read back exact blob: 8b43d28b71a0e70b12a4cbda3d14e886f13fa110
- execution read back unchanged blob: 1a938f42e9f03e723bd50348f8a78dbd8b7098e9
- scorecard read back unchanged blob: 1e8e0a9c3cd34c163c32f6782cdfccf30b9e13d8
- prior selected sheet retained: evidence/operational/CFB_WEEK9_HOT_SHEET_2026-10-27_2050CT.md
- prior selected sheet blob: a11e571c9f2eab663b68cc4e0d25283a7da33092

Blocker:
- classification: IMMUTABLE_REVIEW_ANCESTRY_UNAVAILABLE
- actual Python runtime: 3.12.14
- current Week 9 compiler and readiness both failed closed while attempting required git merge-base --is-ancestor validation
- connected GitHub contents access did not provide a supported local repository checkout/HEAD containing accepted immutable review commits
- no ancestry fabricated; no gate bypassed
- compiler proposal, readiness result, publication gate, selected publication, recovery-index handoff/preflight, and selected CI integration remain incomplete

Next safe action:
Use a supported authenticated repository checkout whose HEAD contains the accepted review commits, then run the normal Week 9 compiler/readiness/publication route with a genuinely fresh source before any prospective cutoff. Do not reconstruct or retime this run and do not select its diagnostic candidate.

No task, schedule, ownership, billing, model, wager or automation mutation occurred.

RUN_INCOMPLETE