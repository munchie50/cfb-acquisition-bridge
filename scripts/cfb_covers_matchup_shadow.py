"""Parse a Covers matchup odds markdown snapshot; never certify an executable offer."""
import json
import re
import sys

def inspect(markdown, source_url, observed_at_utc):
    if not re.fullmatch(r"https://www\.covers\.com/sport/football/ncaaf/matchup/\d+/odds", source_url):
        raise ValueError("unsupported matchup source")
    if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", observed_at_utc):
        raise ValueError("explicit retrieval clock required")
    title = re.search(r"^([^\n]+) Odds$", markdown, re.M)
    if not title:
        raise ValueError("missing matchup identity")
    rows = []
    for line in markdown.splitlines():
        if not line.startswith("| ") or "sportsbooks/" not in line:
            continue
        if "fanduel_icon.svg" not in line:
            continue
        match = re.search(r"\|\s*([+-]\d{2,5})!\[FanDuel", line)
        if match:
            rows.append({"displayed_moneyline": int(match.group(1)),
                         "book_display": "FanDuel", "source_row": line[:160]})
    return {"status": "UNQUALIFIED_SHADOW_SOURCE_ONLY", "matchup": title.group(1),
            "source_url": source_url, "retrieved_at_utc": observed_at_utc,
            "displayed_moneyline_rows": rows[:2],
            "independent_price_clock": None, "executable_offer_verified": False,
            "decision_authorized": False}

if __name__ == "__main__":
    print(json.dumps(inspect(sys.stdin.read(), sys.argv[1], sys.argv[2]), indent=2))
