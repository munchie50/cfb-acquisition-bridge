# CFB Analytics v1 — genuine local Python QA execution — Nov 20, 2026

**Status:** EXECUTED / LOCAL PASS / GIT BLOB IDENTITY VERIFIED. NOT SCHEDULED PRODUCTION ACCEPTANCE.

Executed with Python 3.13.5 and Git 2.47.3 in current chat container, from locally staged copies of exact GitHub source. Independently computed Git object identities using `git hash-object`, matching fresh GitHub connector source blobs:
- `analytics/cfb_read_only_analytics_v1.py`: `269976fe5dabdf71730066545b638a0a6f167a74`
- `qa/test_cfb_read_only_analytics_v1.py`: `b6adf10900aca4ecf7699c29c6442702f26bc619`

Commands and observed stdout:
```text
python qa/test_cfb_read_only_analytics_v1.py
QA_PASS: deterministic read-only analytics invariants
python -O qa/test_cfb_read_only_analytics_v1.py
QA_PASS: deterministic read-only analytics invariants
```
Both exit 0. Tests include status counts, decision lateness, rejection reason, within-book market movement, other-book exclusion, empty input incomplete, and missing source provenance rejection.

**Newly discovered drift defect:** first live input probe showed a row labelled CERTIFIED_MARKET could be accepted without any source path or Git blob identity. Source and QA were corrected and the exact corrected blobs executed above. Required source_path and 40-hex source_blob are necessary but not sufficient to prove external certification: adapter must independently authenticate source contents and timestamps before supplying them.

**Boundaries:** Tests use synthetic fixtures only, not historical real-market evidence. No certified JSONL adapter or original selector QA executed. This chat container execution does not prove the scheduled worker's connector-to-shell transfer. No Champion, wagering recommendation, gate, Hot Sheet, task count or schedule change. Next: build independently authenticated source adapter, then demonstrate scheduled task execution and independent readback. 
