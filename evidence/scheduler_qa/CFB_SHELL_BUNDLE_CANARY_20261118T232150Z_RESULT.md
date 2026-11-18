# CFB shell bundle canary

| Field | Observed value |
| --- | --- |
| Scheduled time (UTC) | 2026-11-18T23:20:09Z |
| Observed time (UTC) | 2026-11-18T23:21:50Z (shell clock sampled after the probe) |
| Direct shell probe | Exit 0; SHELL_STARTED; git version 2.52.0 |
| Diagnostic result | PAYLOAD_TRANSFER_UNAVAILABLE |
| First blocked stage | SOURCE_TRANSFER |
| First error | The embedded message was available as conversation text, with no exact-byte export exposed to the shell and no script file present in scratch. |
| Expected source SHA-256 | `3a4336f1e63572af4efbfe74867a5a38f36739ab6118e521bce2ee83190449da` |
| Source hash result | Unverified; no source file was written |
| Git checkout markers | BUNDLE_BYTES_VERIFIED, HEAD, SHALLOW, and connectivity were not observed |
| Sanitized stderr | No error output from the successful direct probe. The embedded script was not invoked. |
| Receipt verification | Independent GitHub fetch at the creation commit, with the returned content compared against this receipt. The verification outcome is reported separately after the fetch. |

A passing fixture run would establish local offline checkout of the pinned history only.
