"""Read-only Week12 catch-up provenance guard. Never accepts outcomes or posts money."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FINAL = "evidence/audits/CFB_WEEK12_CBS_FINAL_CANDIDATE_20261122_RESEARCH_ONLY.json"
FRONTIER = "evidence/audits/CFB_WEEK12_OFFICIAL_FINAL_ADMISSION_FRONTIER_20261122_QA_ONLY.json"
GRADE = "evidence/audits/CFB_WEEK12_NOV21_13_TICKET_GRADE_CANDIDATE_20261122_QA_ONLY.json"
PAYOUT = "evidence/audits/CFB_NOV21_TICKET_PRINTED_TERMS_CONDITIONAL_PAYOUT_QA_20261122.json"
INTAKE = "evidence/operational/CFB_EXECUTION_TICKETS_20261121_USER_PHOTO_INTAKE.md"
LEDGER = "evidence/operational/CFB_EXECUTION_LEDGER.md"
SCORE = "evidence/audits/CFB_WEEK12_FIRST_FROZEN_SCORE_CANDIDATE_20261122_QA_ONLY.json"


def blob(data):
    header = ("blob %d\0" % len(data)).encode()
    return hashlib.sha1(header + data).hexdigest()


def load(path):
    data = (ROOT / path).read_bytes()
    return json.loads(data), blob(data)


def check():
    final, final_sha = load(FINAL)
    frontier, _ = load(FRONTIER)
    grade, _ = load(GRADE)
    payout, _ = load(PAYOUT)
    score, _ = load(SCORE)
    _, ledger_sha = load_text(LEDGER)
    intake, intake_sha = load_text(INTAKE)
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    require(grade["source_final_blob"] == final_sha, "ticket grade final source drift")
    require(score["source_final_candidate_blob"] == final_sha, "score QA final source drift")
    require(grade["execution_ledger_blob"] == ledger_sha, "ticket grade ledger drift")
    bindings = {s["path"]: s["blob"] for s in payout["sources"]}
    require(bindings.get(GRADE) == load(GRADE)[1], "payout grade source drift")
    require(bindings.get(INTAKE) == intake_sha, "payout intake source drift")
    frows = frontier["rows"]
    require(len(frows) == 70 and len({r["game_id"] for r in frows}) == 70, "frontier cardinality")
    require(all(r["canonical_admission"] == "HOLD" for r in frows), "unexpected canonical admission")
    require(len(grade["rows"]) == 13, "ticket grade cardinality")
    ids = [r["execution_id"] for r in grade["rows"]]
    require(len(set(ids)) == 13, "duplicate ticket grades")
    ledger_text = (ROOT / LEDGER).read_text()
    require(all(ledger_text.count("| " + x + " |") == 1 for x in ids), "execution ID missing/duplicate")
    require(len(payout["rows"]) == 13, "payout cardinality")
    require(payout["summary"]["verified_book_settlements"] == 0, "unexpected settlement certification")
    require(frontier["summary"]["canonical_admitted"] == 0, "unexpected scorecard admission")
    return errors


def load_text(path):
    data = (ROOT / path).read_bytes()
    return data.decode("utf-8"), blob(data)


if __name__ == "__main__":
    issues = check()
    if issues:
        raise SystemExit("FAIL: " + "; ".join(issues))
    print("PASS: Week12 catch-up source bindings and admission holds")
