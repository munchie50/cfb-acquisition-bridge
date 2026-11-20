# Week12 07CT/13CT manual Market Monitor — pinned commit/tree linkage test

STATUS: CONNECTOR REST COMMIT/TREE/BLOB LINKAGE VERIFIED AT ONE HISTORICAL REVISION. NOT FULL ANCESTRY, NOT CHAMPION EXECUTION.

Pinned commit: e8b5c545621b0db469d64d4927bf5b1c0a54ab21 (previously observed main head). Authenticated GitHub REST /git/commits/{sha} returned same SHA and parent 300ac9bf3a6347b60d7bfe039bedd760626306dd; linked root tree 7a9ba8c79fe6559fd85bded3fe25aff2b3c0bf2b. REST /git/trees/{tree}?recursive=1 returned same root SHA, truncated=false, 3083 entries. scripts/cfb_runtime_checkout.py tree entry type blob, mode 100644, size 3780, blob b13930cb714eb87c8dce6136ffab6fbceeb44898. Separate path and immutable blob reads matched exact text (prior smoke test).

Important drift correction: prior generic fetch_commit response did not expose parent/tree fields, but raw GitHub REST /git/commits/{sha} DOES expose both. One parent link is verified, NOT full ancestry. Commit unsigned (verification.verified=false, reason unsigned); do not claim cryptographic signature verification. The pinned commit is a historical observed main, not necessarily current head after audit writes.

This is a new bounded test of a real workaround for the Git DNS blocker, not a relaxed production acceptance contract. Still missing: complete historical ancestry chain and immutable review checks, independent Git object hash recomputation, materialized isolated runtime, deterministic v1 champion fixture, qualified market prices, and canonical Hot Sheet acceptance. Both missed Nov20 07CT and 13CT runs remain incomplete; 13CT deadline cannot be backdated. No schedule, ledger, frozen model or bets modified.
