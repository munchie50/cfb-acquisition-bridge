"""Read-only output completeness gate; never certifies wager quality or executes bets."""
REQUIRED = ("TOP 10", "PARLAY", "FULL SLATE")
def check(text):
    if not isinstance(text, str):
        raise TypeError("sheet must be text")
    upper = text.upper()
    missing = [x for x in REQUIRED if x not in upper]
    return {"status": "OUTPUT_GAP" if missing else "PRESENTATION_ONLY_PASS",
            "missing": missing,
            "scope": "REQUIRED_SECTIONS_ONLY_NOT_PRODUCER_ACCEPTANCE"}
if __name__ == "__main__":
    import argparse, json
    from pathlib import Path
    p = argparse.ArgumentParser()
    p.add_argument("sheet")
    a = p.parse_args()
    print(json.dumps(check(Path(a.sheet).read_text(encoding="utf-8")), sort_keys=True))
