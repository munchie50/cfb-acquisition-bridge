# CFB Market Monitor rebuilt — scheduled stage trace

Correlation: CFBMM-SCHED2-20261101T172934245Z
Invocation ID (later scheduler read): a1e13d48-2d5c-8332-8ed7-b9de59a3b46c
Observed producer start: 2026-11-01T17:29:34.245Z
Trigger: natural scheduled automation (not a manual run-now)

| Stage | Result | Independent evidence / limitation |
| --- | --- | --- |
| STARTUP / GitHub connector | PASS | Append-only RUN_STARTED created commit e7009a0e361a0970930137b03c3dab09b836851c; exact readback blob de0eb9f0fc42ef0d7a23d928634ee08d65c145ce. |
| TREE AUTHORITY DISCOVERY | PASS | Fresh main recursive Git tree 1924 entries, not truncated; newest index v1.245 tree blob 57327859afb17ca42451189d3661f4c16fae4f90 (4,230,705 bytes). |
| LARGE-BLOB RECOVERY | PASS | Exact tree SHA fetch_blob and independent GitHub git/blobs/<sha> fetch contents matched byte-for-byte; verified exact UTF-8 byte sizes index 4,230,705, market 3,837,275, decision 1,901,065, complete first/end. Canonical market blob 69caf5b1184eedccc90be7562e4a3bd7cb8b7375, decision bb5a9cc83b6a1425dc2972ca84b33aa2bbbf8fa9. No canonical writes. |
| ACTIVE CONTRACTS / LAST-GOOD | PASS (read) | v1.247 football-week cadence, v5.2 routine, October10 consensus/Caesars control with October16 decoupling, October12 publication contract, original prompt backup, October30 manual producer closure, October31 decision-producer repair frontier and accepted prediction source state recovered. Latest accepted prediction cutoff 2026-10-27T15:38:14Z, not a certified Week10 FIRST_FROZEN. |
| FRESH CBS WEEK10 ACQUISITION | PASS (source only) | Live Firecrawl source semantic preflight 63 games. R90 full capture commit 5832053049daf1775d0fe90dde1fc07f0addc886, independently read back blob 1b9605ef579aad8e55e2a7f116f7b817f2bb988a. Retrieval 2026-11-01T17:31:23.853Z to 17:31:25.116Z; bookmaker update times unknown. |
| SIX-BRANCH DIRECTED IDENTITY JOIN | PASS (source only) | R91 commit a098969200f3c9cc5b60b44f2cad2575d3ae5baa, readback blob abe0afe3f7e435875645d029faa57b7cdc7ddec0. 63 unique exact directed CBS names to ESPN/CBS canonical IDs; 360 displayed unqualified branches / 18 unavailable; 60 games with displayed CBS rows, 3 without, compared with prior R88 17/46. No positional join. |
| MISSING SOURCE FALLBACK | PARTIAL | R92 commit 04526a7a1afab1b383de83255ad593fb8f393382, readback blob be612db7f4ac9c39c61ab8b06c75b388d529c640. UCF @ Kansas named-book retrieval-only display, Rutgers @ Wisconsin unattributed display, NIU @ SJSU unavailable. Neither quote updates nor venue executable offers certified. |
| MARKET SEMANTIC AUDIT | PASS (limitations found) | Independently checked R91/R92/R93 JSON against 63 directed identities: 378 branch states, 360 displayed/18 unavailable, 0 numeric/identity/WAIT certification violations. 13 of 60 displayed games have non-opposite spread sides; 17 have different over/under total numbers due to mixed/asymmetric source cells. Do not pair or average opposite sides. |
| EVIDENCE-CONSTRAINED WAIT | PASS (noncanonical) | R93 commit 20e919f1d97f4b0a0717922782b4f4dac7c143e8, readback blob f4e9575303f22a8e69749827a81d30b0e14f4809. 63 games x 6 markets = 378 WAIT/NOT_CERTIFIED, 0 bet authorizations. Not caller-authored decision_rows. |
| PRODUCTION DECISION PRODUCER | BLOCKED | No accepted Week10 FIRST_FROZEN game-by-game Champion join, independently authored current qualitative decision_rows, material football review, book offer clocks or executable venue confirmation. Tuesday preferred weekly model freeze under v1.247; cannot reuse Oct27/Week9 predictions or decisions. |
| HOT SHEET / CANONICAL MUTATION / SELECTED CI | NOT ATTEMPTED | Current Week10 production packet not certified; preserving prior accepted Week9 Hot Sheet and all canonical market/decision/execution/scorecard/index. No CI or RUN_PASS claim. |

Nonfatal diagnostic tool-code errors: initial TextEncoder use in JS isolate failed (ReferenceError: TextEncoder is not defined), replaced with explicit UTF-8 byte counter; initial assumption GitHub git/blobs URL returned JSON failed (SyntaxError unexpected '#'), corrected to compare returned decoded content exactly. Neither error modified authoritative surfaces.

Next safe action: Monday schedule/source readiness, Tuesday qualified FIRST_FROZEN if earned; independently qualify named-book source/update clocks and current player evidence, author actual 63-game six-market decisions, run complete producer/CI/readbacks, publish sole Hot Sheet only after gates pass. Natural scheduler startup is verified for this invocation, full production acceptance remains open.
