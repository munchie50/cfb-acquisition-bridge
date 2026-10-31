"""Strict BetSharp page branch extraction. Shadow observations are never executable."""
import json
import re
import sys

BRANCHES = ("away_ml", "home_ml", "away_spread", "home_spread", "over_total", "under_total")

def inspect(markdown, source_url):
    heading = re.search(r"^# (.+?) odds\s*$", markdown, re.M)
    update = re.search(r"^Updated (\d{1,2}:\d{2} [AP]M ET)\s*$", markdown, re.M)
    section = markdown.split("## Game lines", 1)
    if len(section) != 2 or not heading or not update:
        raise ValueError("missing game identity, update time, or lines table")
    table = section[1].split("\n\nMargin:", 1)[0]
    rows = re.findall(r"^\| (.+?) \| (.+?) \| (.+?) \|$", table, re.M)
    observations = {}
    for market, best, book in rows:
        link = re.search(r"history\?m=(ml|spread|total)&s=(away|home|over|under)", market)
        if not link:
            continue
        key = {"ml": {"away": "away_ml", "home": "home_ml"},
               "spread": {"away": "away_spread", "home": "home_spread"},
               "total": {"over": "over_total", "under": "under_total"}}[link[1]][link[2]]
        if key in observations:
            raise ValueError("duplicate market side")
        quoted = re.search(r"^([+-]\d{2,4})<br>([A-Za-z ]+)$", best.strip())
        observations[key] = {"availability": "DISPLAYED_SHADOW" if quoted else "MISSING",
                             "price": int(quoted[1]) if quoted else None,
                             "book_label": quoted[2] if quoted else None}
    if set(observations) != set(BRANCHES):
        raise ValueError("incomplete market side structure")
    return {"status": "SHADOW_MARKET_OBSERVATION", "source_url": source_url,
            "source_heading": heading[1], "source_update_time_et_unanchored": update[1],
            "date_of_update_unverified": True, "source_price_executable": False,
            "canonical_identity_verified": False, "decision_authorized": False,
            "branches": observations}

if __name__ == "__main__":
    print(json.dumps(inspect(sys.stdin.read(), sys.argv[1]), indent=2))
