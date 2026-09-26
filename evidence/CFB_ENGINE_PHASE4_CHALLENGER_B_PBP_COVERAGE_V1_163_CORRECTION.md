# CFB Engine — v1.163 PBP Coverage Audit Correction

v1.163 execution run 36209311277 succeeded technically and its row-level missing-PBP ledger is useful, but its summary class counter compared against the nonexistent literal `FBS_NONFBS` instead of the authoritative `FBS_VS_NONFBS`. Therefore v1.163 summary class counts are INVALID and must not be accepted as evidence. The ledger itself exposed the defect during readback/reconciliation.

Replacement v1.165 adds an allowed-class assertion and corrected counters. No model fitting/scoring or 2025 access occurred.
