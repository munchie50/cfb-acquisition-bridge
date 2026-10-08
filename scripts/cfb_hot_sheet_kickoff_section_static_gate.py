#!/usr/bin/env python3
"""Fail-closed kickoff-section QA for the Week 6 research candidate."""
import re
from pathlib import Path

sheet = Path("evidence/operational/CFB_WEEK6_HOT_SHEET_RESEARCH_CANDIDATE_2026-10-07.md").read_text()
section = None
counts = {}
identities = set()
for line in sheet.splitlines():
    match = re.fullmatch(r"## (Tuesday|Wednesday|Thursday|Friday|Saturday morning|Saturday afternoon|Saturday evening/night) \((\d+)\)", line)
    if match:
        section = match.group(1)
        counts[section] = {"expected": int(match.group(2)), "actual": 0}
        continue
    if not line.startswith("| ") or line.startswith("| Kickoff") or line.startswith("|---"):
        continue
    cols = [c.strip() for c in line.strip("|").split("|")]
    if not re.fullmatch(r"(Tue|Wed|Thu|Fri|Sat) \d{1,2}:\d{2} (AM|PM)", cols[0]):
        continue
    assert section in counts, f"game outside governed section: {cols[1]}"
    assert len(cols) == 8, f"unexpected row columns: {cols[1]}"
    day, clock, meridiem = cols[0].split()
    hour, minute = map(int, clock.split(":"))
    assert 1 <= hour <= 12 and 0 <= minute < 60
    hour24 = hour % 12 + (12 if meridiem == "PM" else 0)
    expected = {"Tue": "Tuesday", "Wed": "Wednesday", "Thu": "Thursday", "Fri": "Friday"}.get(day)
    if day == "Sat":
        expected = "Saturday morning" if hour24 < 12 else ("Saturday afternoon" if hour24 < 17 else "Saturday evening/night")
    assert section == expected, f"{cols[1]} {cols[0]} incorrectly in {section}; expected {expected}"
    assert cols[1] not in identities, f"duplicate game: {cols[1]}"
    identities.add(cols[1])
    counts[section]["actual"] += 1

assert len(identities) == 49, f"modeled game count {len(identities)} != 49"
assert set(counts) == {"Tuesday", "Wednesday", "Thursday", "Friday", "Saturday morning", "Saturday afternoon", "Saturday evening/night"}
for name, count in counts.items():
    assert count["actual"] == count["expected"], f"{name}: {count}"
assert [counts[s]["actual"] for s in ("Tuesday", "Wednesday", "Thursday", "Friday", "Saturday morning", "Saturday afternoon", "Saturday evening/night")] == [1, 2, 3, 5, 7, 17, 14]
print("PASS_HOT_SHEET_KICKOFF_SECTION_STATIC_GATE")
