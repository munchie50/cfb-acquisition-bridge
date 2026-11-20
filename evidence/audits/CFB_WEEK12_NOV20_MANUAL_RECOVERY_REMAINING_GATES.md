# Week12 Nov20 manual recovery — executable closure gate checklist

**State: RECONCILIATION_COMPLETE / COMPILER_NOT_EXECUTED / PUBLICATION_NOT_ACCEPTED**

## Completed and independently verified
- 64 Friday/Saturday games and 384 CBS display fields; 58/58 Saturday games reconciled.
- Original FIRST_FROZEN and accepted Nov10 REFRESH separate; signed-spread correction propagated. Nine real projected-winner conflicts, not erroneous 42.
- Nine conflict games reviewed in one audit; other 49 Saturday games crosschecked in another.
- All 58 retain previous Nov19 PASS, not fresh Friday accepted decisions. Zero new approved wagers.

## Required closure gates
1. Authenticated pinned full checkout using scripts/cfb_runtime_checkout.py; GitHub HTTPS DNS, head, ancestry and immutable reviews must verify. Raw GitHub file fetch is not equivalent.
2. Typed CBS Week12 normalizer using original source markdown and governed lineage; validate all 70 governed Week12 identities. Direct source-file census shows the saved CBS raw capture contains all 70: 3 Tuesday, 2 Wednesday, 1 Thursday, 6 Friday, 58 Saturday. The separate 64-row working card intentionally filters to Friday/Saturday; do not confuse its scope with the raw source census. Working card alone is not accepted typed source.
3. Fresh prospective personnel and named-book price qualification, with deadlines and root review provenance. Do not retroactively certify Friday 1pm CT.
4. Execute scripts/cfb_week12_publication.py and scripts/cfb_neutral_publication_gate.py against actual market/decision/execution/scorecard/lineage sources and as-of clock. Presentation validator is not bet selector.
5. Only after acceptance, write canonical publication and independent readback of blobs/selector/CI.
6. Separately demonstrate successful natural scheduled-worker run; manual recovery does not prove scheduler repair.

## Drift containment
- Nov19 selected production Hot Sheet remains unchanged; Nov20 working card is noncanonical.
- No REFRESH substitution, invented venue offer, fabricated injury clearance, or new conditional promotion.
- No model, money ledger, wager, or production task mutation.
- Do not declare run DONE before checkout/compiler/publication gates close.

## Runtime handoff
A supported authenticated shell/worktree is required for the pinned full checkout and local Python validation. GitHub connector file access alone does not prove these steps.
## Nov20 additional code-level drift finding
- Direct inspection of scripts/cfb_cbs_full_board_normalizer.py: WEEK12 profile expects **70** governed game identities and checks exact identity-set equality. The 64-game Friday/Saturday working card is not an input-complete 70-game normalizer source, but the saved Nov20 raw CBS capture DOES contain 70 game headers, including the six earlier-week games. A successful normalizer run still requires identity/lineage validation.
- Direct inspection of scripts/cfb_week12_publication.py: proposal source must be captured within **900 seconds (15 minutes)** of as-of time; a Nov20 morning board cannot be reused as a fresh later publication quote. Refresh path preserves elapsed game kickoff identities and prohibits hindsight backfill.
- Direct CBS table check: columns are Final, Open, Spread, ML, Total; earlier six-market working card correctly extracted Spread/ML/Total, quarantining Final/Open. Source time is recovered-by, not bookmaker update time.
- This finding supersedes any earlier shorthand that 64/64 working-card completeness satisfies the 70-game compiler source census.

## Direct raw-source census correction
- Fresh read of evidence/operational/CFB_WEEK12_CBS_FULL_BOARD_20261120_MANUAL_0700_CATCHUP.md found 70 game headers: Tue 3, Wed 2, Thu 1, Fri 6, Sat 58. Previous assertion that the *raw source* had only 64 was false; only the derived working card is 64. No missing six-game raw capture reconstruction is needed. Normalizer runtime validation remains open.

## Additional structural preflight (Nov20)
- evidence/audits/CFB_WEEK12_NOV20_RAW_SOURCE_70_GAME_SCHEMA_PREFLIGHT.md independently parses 70 headers, 140 team rows, 420 market positions, and 70 unique directed CBS ID pairs. 136/140 moneyline cells available; four UNAVAILABLE moneyline cells are both sides of Chattanooga @ Alabama and Samford @ Auburn, supported by the normalizer. No other field-format failures observed.
- The earlier 128 team rows refers only to the 64-game Friday/Saturday working subset, not the 70-game source. The raw source structural preflight is not a substitute for governed normalizer/lineage execution.
- Local shell attempt to resolve github.com failed (DNS), so no pinned full checkout or compiler acceptance claimed.
