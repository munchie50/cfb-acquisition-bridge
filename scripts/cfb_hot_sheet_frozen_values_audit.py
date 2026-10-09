#!/usr/bin/env python3
"""Read-only audit of combined Hot Sheet frozen values against accepted ZIP bytes."""
import argparse, csv, hashlib, io, json, re, unicodedata, zipfile
from datetime import date, datetime
from zoneinfo import ZoneInfo

ACCEPTED_ZIP_SHA256 = "772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf"
ALIASES = {"fiu": "florida international"}
def team(s):
    s = "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))
    s = re.sub(r"\s+", " ", s.strip().lower())
    return ALIASES.get(s, s)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", required=True)
    ap.add_argument("--hot-sheet-json", required=True, help="GitHub fetch_file structuredContent JSON")
    ap.add_argument("--first-date", required=True)
    ap.add_argument("--last-date", required=True)
    ap.add_argument("--expected-modeled", required=True, type=int)
    args = ap.parse_args()
    first, last = date.fromisoformat(args.first_date), date.fromisoformat(args.last_date)
    assert first <= last, "invalid date window"
    raw = open(args.archive, "rb").read()
    digest = hashlib.sha256(raw).hexdigest()
    assert digest == ACCEPTED_ZIP_SHA256, "archive does not match accepted v1.208 identity"
    z = zipfile.ZipFile(io.BytesIO(raw))
    tz = ZoneInfo("America/Chicago")
    def scoped(name):
        data = list(csv.DictReader(io.StringIO(z.read(name).decode("utf-8"))))
        return [r for r in data if first <= datetime.fromisoformat(r["start_date"]).astimezone(tz).date() <= last]
    predictions = scoped("challenger_b_2026_fair_predictions_v1_206.csv")
    exclusions = scoped("challenger_b_2026_exclusions_v1_206.csv")
    targets = scoped("challenger_b_2026_target_ledger_v1_206.csv")
    def ids(rows):
        result = {r["game_id"] for r in rows}
        assert len(result) == len(rows), "duplicate frozen game ID"
        return result
    pi, ei, ti = ids(predictions), ids(exclusions), ids(targets)
    assert len(pi) == args.expected_modeled, "unexpected scoped modeled count"
    assert not pi & ei and pi | ei == ti, "prediction/exclusion/target identity reconciliation failed"
    indexed = {}
    for r in predictions:
        key = (team(r["away_team"]), team(r["home_team"]))
        assert key not in indexed, "ambiguous ordered matchup; game ID required"
        indexed[key] = r
    obj = json.load(open(args.hot_sheet_json))
    content = obj["content"]
    blob = hashlib.sha1(b"blob " + str(len(content.encode())).encode() + b"\0" + content.encode()).hexdigest()
    assert blob == obj["sha"], "Hot Sheet Git blob digest mismatch"
    rows = []
    for line in content.splitlines():
        if not re.match(r"^\| (Tue|Wed|Thu|Fri|Sat) ", line):
            continue
        cells = [c.strip() for c in line.split("|")][1:-1]
        assert len(cells) == 9, "unsupported Hot Sheet row schema"
        matchup = re.split(r" @ | vs ", cells[1])
        assert len(matchup) == 2, "unparsed ordered matchup"
        key = tuple(team(x) for x in matchup)
        assert key in indexed, "Hot Sheet matchup absent from modeled frozen set: " + cells[1]
        r = indexed[key]
        parts = cells[2].split(" / ")
        assert len(parts) == 3, "unparsed combined prediction fields"
        m = re.fullmatch(r"(.+?) (-\d+\.\d)", parts[0])
        assert m, "unparsed fair spread"
        margin = float(r["pred_margin"])
        favorite = r["home_team"] if margin >= 0 else r["away_team"]
        expected_spread = format(abs(margin), ".1f")
        expected_total = format(float(r["pred_total"]), ".1f")
        expected_win = format(float(r["pred_win"]), ".3f")
        assert team(m.group(1)) == team(favorite), "favorite direction mismatch: " + cells[1]
        assert m.group(2) == "-" + expected_spread, "fair spread mismatch: " + cells[1]
        assert parts[1] == expected_total, "frozen total mismatch: " + cells[1]
        assert parts[2].endswith(" home"), "home probability label missing"
        assert format(float(parts[2].removesuffix(" home")), ".3f") == expected_win, "probability mismatch: " + cells[1]
        rows.append({"game_id": r["game_id"], "game": cells[1], "favorite": favorite,
                     "spread_magnitude": expected_spread, "total": expected_total, "home_probability": expected_win})
    rendered = {r["game_id"] for r in rows}
    assert len(rendered) == len(rows) and rendered == pi, "Hot Sheet duplicate/omitted frozen identity"
    nebraska = [r for r in exclusions if r["home_team"] == "Nebraska" and r["away_team"] == "Indiana"]
    assert len(nebraska) == 1 and nebraska[0]["reasons"] == "away_prior_points_missing", "Nebraska exclusion ancestry mismatch"
    assert "## Nebraska — mandatory unmodeled inclusion" in content, "separate Nebraska display missing"
    result = {"verdict": "PASS", "accepted_archive_sha256": digest, "hot_sheet_blob": blob,
              "frozen_date_scope_ct": [str(first), str(last)], "modeled": len(pi),
              "excluded": len(ei), "targets": len(ti), "matched_rows": len(rows),
              "matched_numeric_fields": 3 * len(rows), "matched_favorite_directions": len(rows),
              "nebraska_exclusion": nebraska[0], "rows": rows,
              "limitations": ["One-to-one ordered matchup mapping because display lacks game IDs; no fuzzy matching.",
                              "Frozen date scope only; current kickoff section authority checked separately.",
                              "No current market, source freshness, calibrated edge, wager or numerical model rerun."]}
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

