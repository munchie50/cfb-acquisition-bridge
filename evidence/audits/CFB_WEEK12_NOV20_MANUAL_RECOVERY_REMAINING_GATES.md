# Week12 Nov20 manual recovery — executable closure gate checklist

**State: RECONCILIATION_COMPLETE / COMPILER_NOT_EXECUTED / PUBLICATION_NOT_ACCEPTED**

## Completed and independently verified
- 64 Friday/Saturday games and 384 CBS display fields; 58/58 Saturday games reconciled.
- Original FIRST_FROZEN and accepted Nov10 REFRESH separate; signed-spread correction propagated. Nine real projected-winner conflicts, not erroneous 42.
- Nine conflict games reviewed in one audit; other 49 Saturday games crosschecked in another.
- All 58 retain previous Nov19 PASS, not fresh Friday accepted decisions. Zero new approved wagers.

## Required closure gates
1. Authenticated pinned full checkout using scripts/cfb_runtime_checkout.py; GitHub HTTPS DNS, head, ancestry and immutable reviews must verify. Raw GitHub file fetch is not equivalent.
2. Typed CBS Week12 normalizer using original source markdown and governed lineage; validate all 70 governed Week12 identities (the Friday/Saturday working card covers only 64 and cannot by itself satisfy the normalizer); six earlier-week identities must be preserved from governed retained sources or an authorized complete capture. Working card alone is not accepted typed source.
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
- Direct inspection of scripts/cfb_cbs_full_board_normalizer.py: WEEK12 profile expects **70** governed game identities and checks exact identity-set equality. The 64-game Friday/Saturday working card is not an input-complete 70-game normalizer source.
- Direct inspection of scripts/cfb_week12_publication.py: proposal source must be captured within **900 seconds (15 minutes)** of as-of time; a Nov20 morning board cannot be reused as a fresh later publication quote. Refresh path preserves elapsed game kickoff identities and prohibits hindsight backfill.
- Direct CBS table check: columns are Final, Open, Spread, ML, Total; earlier six-market working card correctly extracted Spread/ML/Total, quarantining Final/Open. Source time is recovered-by, not bookmaker update time.
- This finding supersedes any earlier shorthand that 64/64 working-card completeness satisfies the 70-game compiler source census.
