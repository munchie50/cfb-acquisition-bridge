# Week12 Friday manual catch-up — authoritative operational ledger read recovery

STATUS: VERIFIED READ-ONLY RECOVERY; NO DECISION/PUBLICATION PROMOTION.

## Finding
The GitHub fetch_file connector returned empty strings for the two very large operational ledgers, despite valid blob SHA. Recovered the actual contents through approved GitHub fetch URL route (GitHub REST contents URL). Do not infer repository truncation, emptiness, deletion, or corruption from the earlier empty wrapper result.

- evidence/operational/CFB_DECISION_WAIT_LEDGER.md: 3,605,685 characters recovered; starts with '# CFB Decision and WAIT Ledger', active append-only operational surface. String occurrence screen: 2026-11-19 = 83, 2026-11-20 = 0. This is a text occurrence check, not exhaustive schema validation.
- evidence/operational/CFB_MARKET_MONITOR_STATE.md: 6,815,072 characters recovered; starts with '# CFB Market Monitor State', active append-only operational surface. String occurrence screen: 2026-11-19 = 77, 2026-11-20 = 10. This indicates Friday observations occur in market ledger, but does not certify a Friday prospective decision or publication.
- Recovery index evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_295.md SHA ebc25a8385ba82b0988cdbe39507d3a793c71e1e; read-only recovery did not modify it.

## Corrected operational interpretation
Prior 'zero-length' was a tool read limitation, not verified empty ledgers. The Decision/WAIT ledger's absent exact Friday date string is not conclusive proof no other decision evidence exists, but no Friday entry was identified by this bounded search. The market ledger contains Friday date strings and needs specific identity/time/source reconciliation. Preserve append-only semantics; do not overwrite or regenerate large ledgers. No scheduler, model, money, wager, or publication change.

## Next
Identify Friday market observation sections in recovered ledger; compare with 64-game Friday working card; obtain qualified prospective decision evidence; execute canonical compiler only if runtime and authority gates permit. Friday 13CT deadline not retroactively certified.
