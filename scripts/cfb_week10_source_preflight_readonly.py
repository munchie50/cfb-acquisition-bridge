"""Read-only prospective Week10 CBS capture preflight; not a decision or publication producer."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

EXPECTED_URL = "https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-10/"


def check(capture, source_url, recovered_by, as_of):
    if source_url != EXPECTED_URL:
        raise ValueError("exact Week10 CBS source URL required")
    recovered = datetime.fromisoformat(recovered_by.replace("Z", "+00:00"))
    now = datetime.fromisoformat(as_of.replace("Z", "+00:00"))
    if recovered.tzinfo is None or now.tzinfo is None:
        raise ValueError("timezone-aware timestamps required")
    age = (now - recovered).total_seconds()
    if not 0 <= age <= 900:
        raise ValueError("fresh source must be recovered within fifteen minutes")
    if not capture.strip():
        raise ValueError("empty capture")
    if EXPECTED_URL not in capture:
        raise ValueError("capture must explicitly identify its source URL")
    if "week-9/" in capture.lower():
        raise ValueError("Week9 capture contamination")
    data = capture.encode("utf-8")
    digest = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\\0" + data).hexdigest()
    return {"status": "WEEK10_SOURCE_PREFLIGHT_ONLY", "source_url": source_url,
            "capture_git_blob": digest, "capture_bytes": len(data),
            "recovered_by_utc": recovered.astimezone(timezone.utc).isoformat(),
            "age_seconds": age, "decision_rows_authored": False,
            "qualified_games": None, "publication_authorized": False}


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--capture", type=Path, required=True)
    p.add_argument("--source-url", required=True)
    p.add_argument("--recovered-by", required=True)
    p.add_argument("--as-of", required=True)
    a = p.parse_args()
    print(json.dumps(check(a.capture.read_text(), a.source_url, a.recovered_by, a.as_of), indent=2))
