# Week12 Nov20 — independent UTF-8 Git blob digest verification

**Result: PASS — actual reconstructed decision bytes match declared Hot Sheet decision Git blob.**

Retrieved actual immutable GitHub decision base blob `6862be6a1bd88a3290b1e90a49c33a7a87e92559` and delta blob `646bbe85edba726037e1b98125783ff2cd87a4e8`. Joined exact returned UTF-8 content without normalization. JavaScript SHA-1 over Git blob envelope `blob <UTF8_BYTE_LENGTH>\\0<RAW_UTF8_BYTES>` independently recomputed `98941e228072e6941b1c33e42d4d8dba570f7182`, exactly equal to the expected reconstructed decision blob and Hot Sheet declaration. Reconstructed text length 3,669,052 Unicode code units; UTF-8 payload length **3,669,292 bytes**. Initial diagnostic mistakenly used character count in Git blob header, producing `ecd6a1c9bf87d21eb92aeaabc470a25e2ddee6b1`; this was a **test harness encoding error**, not an actual data-integrity failure. Corrected to byte count and obtained exact PASS. Do not propagate the false mismatch.

This check independently verifies the reconstructed actual decision digest, not merely length. It does not execute the checked-in Python `audit` or `publication` functions or establish canonical publication selector acceptance. Existing Hot Sheet has one canonical-input declaration referencing this digest. Earlier negative tests and provisional release remain intact.

**Operational position:** manual Friday 07CT/13CT research recovery and provisional Hot Sheet publication already completed. No new source collection or operator-specific executable wagers. Production scheduled cycles remain RUN_INCOMPLETE; four tasks unchanged. Canonical selector/contract remains deferred.

**Next narrow slice:** validate actual `audit(sheet, virtual_ledger)` using original module when execution runtime is available, then address governed selector contract. Do not repeat compiler, checkout, overlay reconstruction or source research without new data.
