#!/usr/bin/env python3
"""Static regression gate for Wednesday's bounded weekly fallback."""
from pathlib import Path

wf = Path(".github/workflows/cfb_weekly_wednesday_fallback.yml").read_text()

required = [
    "WEDNESDAY — bounded fallback",
    '"event"=="schedule"',
    "target_date=(now-datetime.timedelta(days=1)).date()",
    't.date()==target_date',
    'r["status"]=="completed" and r["conclusion"]=="success"',
    "CFB_WEEKLY_WEDNESDAY_FALLBACK_NOOP_PRECEDING_TUESDAY_SCHEDULE_SUCCESS",
    "CFB_WEEKLY_WEDNESDAY_FALLBACK_REQUIRED",
    '["gh","workflow","run","cfb_weekly_tuesday_candidate_freeze.yml","--ref","main"]',
]
for token in required:
    assert token in wf, f"missing bounded-fallback control: {token}"

for forbidden in [
    "datetime.timedelta(hours=36)",
    'any(r["status"]=="completed" and r["conclusion"]=="success" for r in recent)',
]:
    assert forbidden not in wf, f"stale broad fallback logic returned: {forbidden}"

print("PASS_WEEKLY_WEDNESDAY_FALLBACK_STATIC_GATE")
