# V6 terminal closure contract reconciliation

Authority: evidence/CFB_TERMINAL_RUN_RECEIPT_CLOSURE_CONTRACT_2026-10-05.md, blob 9a2f158beddcde783c25fbecfa6d8d66dd8b2ca8.

October 8 morning production Market Monitor: RUN_STARTED persisted; terminal candidate RUN_INCOMPLETE independently read back as blob 36bb04d0d6e0816760218ed17e23b073b63db3c8; later separate RUN_CLOSURE blob 32c568b0591625a6b446307cb98ec5109a1f10f0. Closure correctly identifies unchanged canonical market blob and missing refreshed Hot Sheet. Status: INCOMPLETE correctly closed, not PASS.

Natural scheduled V6 isolated canary: STARTED blob d41f8ac745d123306e4bb292c4fcf0d417c58162; RESULT PASS blob 9f2b3158172b9efbc85f61e30b29d7f62d20365a; later CLOSURE blob a98bd465f5e4f34d049eaf6bf81a41b2bd19d32b. Isolated fixture exact readback verified. Status: DIAGNOSTIC PASS only.

Outstanding production acceptance: natural scheduled Market Monitor invocation plus applicable canonical market, decision, Hot Sheet and terminal candidate readbacks, followed by separate closure RUN_PASS. No historical status changes, no model or production mutations.

## 2026-10-09 test-routing repository-ancestry demonstration

Trigger: inherited receipt claims described terminal-before-closure ordering. Current files and their prose alone do not establish which exact bytes existed before closure.

Expected control: recover path-specific commit history and fetch the terminal candidate at the closure commit's actual parent; recover STARTED at the candidate parent. Reconcile exact referenced blob identities and preserve operational classifications. Do not substitute timestamp or filename sorting for Git ancestry.

Observed repository evidence:

| Case | STARTED creation commit | Candidate creation commit | Closure creation commit |
| --- | --- | --- | --- |
| October 8 production Market Monitor | 5f4b1a37576c7cbcc2e22289903656eea2c99bb1 | 31bbe9cbe1d25b6077709fef2a3c4f611491b58f | 41bbb541595d967531bfa63ae51f6255f1a56a0d |
| Natural isolated V6 canary | 26cfe0e359943fe035fc45909098cc57fcd3aa97 | 8dbbe07339991874049b2a16638aa9af947c7e72 | e75b5a2b94ec66829477c3e5cf01f60d6d08def1 |

- Production closure's sole parent is the candidate creation commit. Independent fetch at that parent returns candidate blob 36bb04d0d6e0816760218ed17e23b073b63db3c8, exactly matching the closure's reference.
- Production candidate's sole parent is the STARTED creation commit. Independent fetch there returns STARTED blob 541890e15da763d0012468a286b40554e8542fe3, matching both candidate and closure.
- Canary closure's sole parent is the RESULT creation commit. Independent fetch there returns RESULT blob 9f2b3158172b9efbc85f61e30b29d7f62d20365a, exactly matching its closure reference.
- Canary RESULT's parent is fixture-update commit 1cbb6a731ed3a4fd54c9f84f423c120699fc2360. Independent fetch there returns STARTED blob d41f8ac745d123306e4bb292c4fcf0d417c58162, matching RESULT and closure.
- Each of these six receipt paths has one path-specific commit in the recovered history (per_page=100 returned one); no subsequent rewrite appears in that history at audited main tip b0fa9d8d835e193257a8dd827c87213ce4c00210.
- Executed 14 fail-closed assertions on returned history, single-parent relationships, referenced blob identities, production INCOMPLETE classification and canary's explicit absence of production certification. All passed.

Expected-vs-actual: PASS for repository persistence ordering and exact receipt-reference consistency. Risk detected/prevented: upgrading isolated diagnostic PASS or trusting mutable current receipt prose as historical ordering proof.

Proof limit: Git ancestry proves that the cited candidate bytes were persisted before closure. It does not independently expose or prove the original runtime fetch/readback operation. The retained receipts attest that operation; this audit's newly executed historical fetches verify the referenced persisted objects.

Disposition remains: production RUN_INCOMPLETE; isolated canary DIAGNOSTIC PASS. Natural production RUN_PASS and canonical/Hot Sheet freshness remain pending. No historical status upgrade, canonical mutation, task change, model change or protected TEST access.

Control result: REPOSITORY_ANCESTRY_REPLAY_DEMONSTRATED. This is not NATURAL_PRODUCTION_DEMONSTRATED or production routine promotion.
