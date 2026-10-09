#!/usr/bin/env python3
"""Read-only Week 6 decision evidence coverage audit; never creates decisions."""
import argparse
import hashlib
import json
import re
import unicodedata
from collections import Counter
from datetime import date, datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

CT = ZoneInfo("America/Chicago")
MARKER = "## Week 6 Sunday opening-board decision boundary"
ALIASES = {"Florida International": "FIU"}

def key(s):
    for old, new in ALIASES.items():
        s = s.replace(old, new)
    s = "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]", "", s.lower().replace(" @ ", " at "))

def deadline_authority(cadence):
    required = [
        "Status: ACTIVE DEVELOPMENT / BETA CADENCE CONTROL",
        "## Kickoff-window reconciliation deadlines — 2026-09-29",
        "FRIDAY games: default reconciliation deadline Friday 13:00 CT",
        "SATURDAY AFTERNOON games (12:00–16:59 CT): default reconciliation deadline Saturday 07:00 CT",
        "SATURDAY EVENING/NIGHT games (17:00 CT or later): default reconciliation deadline Saturday 13:00 CT",
        "SATURDAY MORNING games (kickoff before 12:00 CT): default reconciliation deadline Friday evening availability review",
        "THURSDAY games: reconcile by the final scheduled Market Monitor pass",
        "if the ordinary 13:00 CT pass is safely pre-kickoff",
        "A game-specific earlier deadline must be used",
    ]
    if any(cadence.count(fragment) != 1 for fragment in required):
        raise ValueError("unrecognized or ambiguous recovered deadline authority; reconcile before audit")

def audit(slate, ledger, as_of, tuesday, cadence):
    deadline_authority(cadence)
    if as_of.tzinfo is None:
        raise ValueError("as-of must have an explicit timezone")
    as_of = as_of.astimezone(CT)
    if tuesday.weekday() != 1:
        raise ValueError("week-tuesday must be a Tuesday")
    if ledger.count(MARKER) != 1:
        raise ValueError("unique Week 6 ledger boundary required")
    tail = ledger.split(MARKER, 1)[1]
    named_lines = [line for line in tail.splitlines() if line.startswith("- ") and (" @ " in line or " at " in line)]
    rows = []
    section = None
    days = {"Tue": 0, "Wed": 1, "Thu": 2, "Fri": 3, "Sat": 4}
    for line in slate.splitlines():
        m = re.fullmatch(r"## (Tuesday|Wednesday|Thursday|Friday|Saturday morning|Saturday afternoon|Saturday evening/night) \((\d+)\)", line)
        if m:
            section = m[1]
            continue
        if not line.startswith("| "):
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        m = re.fullmatch(r"(Tue|Wed|Thu|Fri|Sat) (\d{1,2}):(\d{2}) (AM|PM)", cols[0])
        if not m:
            continue
        if len(cols) != 8 or section is None:
            raise ValueError("invalid slate row")
        day, hour, minute, meridiem = m.groups()
        hour, minute = int(hour), int(minute)
        if not 1 <= hour <= 12 or not 0 <= minute < 60:
            raise ValueError("invalid kickoff clock")
        hour24 = hour % 12 + (12 if meridiem == "PM" else 0)
        expected = {"Tue": "Tuesday", "Wed": "Wednesday", "Thu": "Thursday", "Fri": "Friday"}.get(day)
        if day == "Sat":
            expected = "Saturday morning" if hour24 < 12 else "Saturday afternoon" if hour24 < 17 else "Saturday evening/night"
        if section != expected:
            raise ValueError("kickoff/section mismatch")
        kickoff = datetime.combine(tuesday + timedelta(days=days[day]), time(hour24, minute), CT)
        # Naming coverage only. A matched line is not a qualified decision.
        matches = [line for line in named_lines if key(cols[1]) == key(line.split(" — ", 1)[0])]
        if len(matches) > 1:
            raise ValueError("ambiguous named ledger record")
        if as_of >= kickoff:
            timing = "KICKOFF_BOUNDARY_PASSED"
        elif section == "Friday" and as_of.date() == tuesday + timedelta(days=2):
            timing = "THURSDAY_REVIEW_DAY_NO_EXACT_DEADLINE"
        elif section == "Saturday morning" and as_of.date() == tuesday + timedelta(days=3):
            timing = "FRIDAY_REVIEW_DAY_NO_EXACT_DEADLINE"
        elif section == "Friday" and as_of.date() > tuesday + timedelta(days=2):
            timing = "THURSDAY_REVIEW_DAY_PASSED"
        elif section == "Saturday morning" and as_of.date() > tuesday + timedelta(days=3):
            timing = "FRIDAY_REVIEW_DAY_PASSED"
        elif section == "Saturday afternoon" and as_of >= datetime.combine(tuesday + timedelta(days=4), time(7), CT):
            timing = "EXPLICIT_SATURDAY_0700_REVIEW_DUE"
        elif section == "Saturday evening/night" and as_of >= datetime.combine(tuesday + timedelta(days=4), time(13), CT):
            timing = "EXPLICIT_SATURDAY_1300_REVIEW_DUE"
        else:
            timing = "OTHER_OR_FUTURE_REVIEW_WINDOW"
        default = None
        if section == "Friday":
            default = datetime.combine(tuesday + timedelta(days=3), time(13), CT)
        elif section == "Thursday" and kickoff.hour >= 13 and kickoff > datetime.combine(kickoff.date(), time(13), CT):
            default = datetime.combine(tuesday + timedelta(days=2), time(13), CT)
        elif section == "Saturday afternoon":
            default = datetime.combine(tuesday + timedelta(days=4), time(7), CT)
        elif section == "Saturday evening/night":
            default = datetime.combine(tuesday + timedelta(days=4), time(13), CT)
        if default is not None:
            deadline_status = "DEFAULT_TIME_REACHED" if as_of >= default else "DEFAULT_TIME_FUTURE"
            deadline_event = None
        elif section == "Saturday morning":
            deadline_status = "EVENT_TIMED_NOT_CERTIFIED"
            deadline_event = "Friday evening availability review; fallback last Friday Market Monitor if no evening run applies"
        else:
            deadline_status = "DEFAULT_NOT_EXTRACTED"
            deadline_event = None
        rows.append({"game": cols[1], "section": section, "kickoff_ct": kickoff.isoformat(),
                     "timing": timing, "named_week6_ledger_record": bool(matches),
                     "default_reconciliation_deadline_ct": default.isoformat() if default else None,
                     "default_reconciliation_event": deadline_event,
                     "default_deadline_status": deadline_status,
                     "effective_game_deadline": "NOT_CERTIFIED_EARLIER_CONSTRAINTS_NOT_EXTRACTED",
                     "decision_validation": "NOT_CERTIFIED", "hard_cutoff": "NOT_EXTRACTED"})
    identities = [key(r["game"]) for r in rows]
    expected_counts = {"Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 5,
                       "Saturday morning": 7, "Saturday afternoon": 17, "Saturday evening/night": 14}
    if len(rows) != 49 or len(set(identities)) != 49 or dict(Counter(r["section"] for r in rows)) != expected_counts:
        raise ValueError("Week 6 49-row unique section population mismatch")
    return {"status": "QA_COVERAGE_ONLY", "as_of_ct": as_of.isoformat(), "rows": rows,
            "counts": {"slate": len(rows), "named_records": sum(r["named_week6_ledger_record"] for r in rows),
                       "timing": dict(Counter(r["timing"] for r in rows)),
                       "default_deadline_status": dict(Counter(r["default_deadline_status"] for r in rows))},
            "limitations": ["Ledger naming coverage is not decision quality or completion.",
                            "Passed scheduled kickoff is not proof of actual start or final.",
                            "Evening review has no invented exact deadline.",
                            "Review-day timing is separate from default decision reconciliation deadlines.",
                            "Defaults do not override earlier game-specific deadlines, travel/access constraints or hard execution cutoffs.",
                            "A safely pre-kickoff Thursday clock does not prove a practical execution opportunity.",
                            "No quote, threshold, prediction, wager or canonical state generated."]}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--slate", type=Path, required=True)
    p.add_argument("--ledger", type=Path, required=True)
    p.add_argument("--cadence", type=Path, required=True, help="recovered active v1.237 deadline authority")
    p.add_argument("--as-of", required=True)
    p.add_argument("--week-tuesday", required=True)
    a = p.parse_args()
    sb, lb, cb = a.slate.read_bytes(), a.ledger.read_bytes(), a.cadence.read_bytes()
    result = audit(sb.decode(), lb.decode(), datetime.fromisoformat(a.as_of), date.fromisoformat(a.week_tuesday), cb.decode())
    result["input_sha256"] = {"slate": hashlib.sha256(sb).hexdigest(), "ledger": hashlib.sha256(lb).hexdigest(), "cadence": hashlib.sha256(cb).hexdigest()}
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
