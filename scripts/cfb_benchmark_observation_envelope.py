#!/usr/bin/env python3
"""Validate and render retrieval-only pregame benchmark records; never writes."""
import argparse
import json
import math
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit

FIELDS = {"source_game_id", "game", "observed_at", "kickoff_at", "source_url",
          "book", "provenance", "time_semantics", "offer_updated_at",
          "execution_status", "markets"}
MARKETS = {"spread": ("away", "home"), "total": ("over", "under"),
           "moneyline": ("away", "home")}

def clock(value):
    if not isinstance(value, str):
        raise ValueError("timestamp must be explicit text")
    result = datetime.fromisoformat(value)
    if result.tzinfo is None:
        raise ValueError("timestamp requires timezone")
    return result

def text_field(value, limit=256):
    if not isinstance(value, str) or not value.strip() or len(value) > limit:
        raise ValueError("invalid bounded text field")
    if any(ord(c) < 32 or ord(c) == 127 for c in value):
        raise ValueError("control characters prohibited")

def validate(records, as_of):
    if as_of.tzinfo is None or not records or not isinstance(records, list):
        raise ValueError("records and timezone-aware audit boundary required")
    seen = set()
    for row in records:
        if not isinstance(row, dict) or set(row) != FIELDS:
            raise ValueError("unknown or missing record fields")
        for name in ("source_game_id", "game", "book", "provenance"):
            text_field(row[name])
        if not re.fullmatch(r"[A-Za-z0-9_.:-]{1,80}", row["source_game_id"]):
            raise ValueError("invalid source identity")
        text_field(row["source_url"], 2048)
        url = urlsplit(row["source_url"])
        if url.scheme not in ("https", "http") or not url.hostname or url.username or url.password:
            raise ValueError("invalid public source URL")
        identity = (row["source_url"], row["source_game_id"])
        if identity in seen:
            raise ValueError("duplicate source game identity")
        seen.add(identity)
        observed, kickoff = clock(row["observed_at"]), clock(row["kickoff_at"])
        if observed > as_of or kickoff <= observed:
            raise ValueError("future observation or non-pregame boundary")
        if row["time_semantics"] != "RETRIEVAL_ONLY" or row["offer_updated_at"] is not None:
            raise ValueError("this formatter does not certify book update time")
        if row["execution_status"] != "NOT_VERIFIED":
            raise ValueError("benchmark is not an executable offer")
        markets = row["markets"]
        if not isinstance(markets, dict) or set(markets) != set(MARKETS):
            raise ValueError("all market availability groups required")
        for market, sides in MARKETS.items():
            group = markets[market]
            if not isinstance(group, dict) or set(group) != set(sides):
                raise ValueError("selection identities missing or unknown")
            for quote in group.values():
                if not isinstance(quote, dict) or set(quote) != {"line", "price", "availability"}:
                    raise ValueError("atomic quote fields required")
                line, price, availability = quote["line"], quote["price"], quote["availability"]
                if availability == "NOT_YET_AVAILABLE":
                    if line is not None or price is not None:
                        raise ValueError("unavailable quote cannot contain invented values")
                    continue
                if availability != "PUBLIC_DISPLAY_OBSERVED":
                    raise ValueError("invalid availability")
                if market == "moneyline":
                    if line is not None or price is None:
                        raise ValueError("moneyline requires price and no spread line")
                elif type(line) not in (int, float) or not math.isfinite(line):
                    raise ValueError("observed line must be finite")
                elif market == "total" and line <= 0:
                    raise ValueError("total must be positive")
                if price is not None and (type(price) is not int or abs(price) < 100):
                    raise ValueError("invalid American price")
    # Side-specific numbers are retained; no invented symmetric consensus.
    return records

def render(records, as_of, run_id):
    if not re.fullmatch(r"[A-Za-z0-9_.:-]{1,100}", run_id):
        raise ValueError("invalid run identity")
    validate(records, as_of)
    header = "\n\n## Pregame public benchmark capture — " + run_id + "\n"
    header += "Schema: CFB_BENCHMARK_ENVELOPE_V1; retrieval-only; executability NOT_VERIFIED.\n"
    header += "Validation does not qualify source truth, frozen identity or a betting decision.\n"
    return header + "\n".join(json.dumps(r, sort_keys=True, ensure_ascii=True, separators=(",", ":"), allow_nan=False)
                              for r in records) + "\n"

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--as-of", required=True)
    p.add_argument("--run-id", required=True)
    a = p.parse_args()
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result
    records = json.loads(a.input.read_text(), object_pairs_hook=unique_keys)
    print(render(records, clock(a.as_of), a.run_id), end="")

if __name__ == "__main__":
    main()
