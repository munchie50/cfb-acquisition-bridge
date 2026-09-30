# CFB QA — Accepted-boundary evidence archive — 2026-09-29

Status: ARCHIVED / EXACT BYTE READBACK VERIFIED.
Scope: evidence preservation only. No change to scientific or operational snapshot authority.
Parents: CFB_QA_CADENCE_WAIT_READINESS_AUDIT_2026-09-29.md; September 29 S0 and v4 acceptance records.
Base repository head: b58b51585f8121ef27e2b278e00e02e83ef138c2.
Recovery inventory: 355 entries, recursive tree truncated=false; current checkpoint directly reread before write.

## Preserved immutable packages
Original GitHub artifacts remain intact. These are byte-identical secondary evidence copies, not new producer outputs.

| Artifact | Archive filename | Library identity | Version | Bytes | ZIP SHA-256 |
|---|---|---|---:|---:|---|
| 11031055060 | CFB_QA_RAW_11031055060.zip | libfile_11a456a5ee448191a32bec31161f7ed5 | 0 | 33104767 | 1495f453e5d9f262baddfa2b7ad21d2d9e8d5f8c2436f058f88fcb6ebc6d8d68 |
| 11064541770 | CFB_QA_S0_11064541770.zip | libfile_a90273e55d7881919412ce1a08b75a44 | 0 | 100762 | 78b58979a7a1a81bd3af0473c65fb760a94b73421e0ee97aa51adce1a540a259 |
| 11065575217 | CFB_QA_V4_11065575217.zip | libfile_31156486f2588191859a5cdd5ce5bb5c | 0 | 350487 | f1104a7fc509f2ef9ee1825698e0210bfd232c9acfafb34635bbd75f93567c8f |

Library root filenames above are the returned canonical paths.
Backing file IDs, respectively:
- file_000000009ea481f597c7e428da73c7ab
- file_00000000574c81fb92e822da02d62307
- file_00000000aafc81fb86a08557025fc525

Recovery uses exact Library identities with materialization, followed by ZIP and internal hash verification against the original acceptance records. Do not infer scientific acceptance from an archive write or substitute current upstream bytes.

## Verification
Fresh downloads of the three known GitHub artifacts reproduced every accepted ZIP SHA above and passed ZIP CRC integrity.
Every manifest-listed internal file actually present in each package reproduced its hash:
- raw: five source/checksum/projection/preflight files;
- S0: the team-side substrate (also matches its independent substrate manifest);
- v4: all three CSV files.

Each saved version was separately materialized from its returned Library identity to a readback directory. All three readback files equaled original ZIP bytes exactly and reproduced ZIP SHA-256. Returned Library identity/version metadata was applied and verified by the canonical transfer helper.

The S0 producer manifest also names prediction, exclusion, chronology, feature-ledger and target-ledger paths absent from this ZIP. Those absent filenames were explicitly recorded rather than treated as verified. The feature-ledger hash equals the retained side substrate hash, as already documented; no separate missing file was manufactured.
Archiving does not repair absent historical raw replay or accept unseen operational S0 prediction bytes.

## Attempts preserved
Two exact-title/short-title Library searches returned no matches for the intended archive filenames; no prior Library identity was resolved.
Initial canonical prepared-upload helper failed before preparation with a network tools/list error under the restricted shell. Approved network-enabled execution of the same ordered batch succeeded for all three files, with local metadata applied. No uncertain finalization or duplicate upload retry occurred.
No model or acquisition workflow was dispatched.

## Global dependency reconsideration / integration / stop
The finite GitHub-retention gap identified by the wait-period audit is now closed for these three accepted QA packages through independently verified secondary copies.
Current checkpoint links this archive record; prior readiness audit remains historical and is not rewritten.
Next scientific dependency is unchanged: weekly cadence and qualified fresh preflight before S2 consumer construction/prediction freezing.
No new snapshot, cadence exception, S2 prediction, outcome scoring, protected 2025 TEST access, refit, recalibration, Champion mutation, or promotion.
Disposition: preservation complete; CADENCE WAIT remains.
