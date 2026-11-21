"""QA-only Week12 overlay transaction preflight. No canonical writes or authority."""
import hashlib
import re
from datetime import datetime, timezone

EXPECTED_BASE = "6862be6a1bd88a3290b1e90a49c33a7a87e92559"
EXPECTED_DELTA = "646bbe85edba726037e1b98125783ff2cd87a4e8"
EXPECTED_RESULT = "98941e228072e6941b1c33e42d4d8dba570f7182"
CANONICAL_LEDGER = "evidence/operational/CFB_DECISION_WAIT_LEDGER.md"
SHEET_PATTERN = re.compile(r"evidence/operational/CFB_WEEK[0-9]{1,2}_HOT_SHEET_[0-9]{4}-[0-9]{2}-[0-9]{2}_[0-9]{4}CT\.md")

def blob(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def utc(value):
    if not isinstance(value, str):
        raise ValueError("timestamp must be string")
    d = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if d.tzinfo is None:
        raise ValueError("timezone required")
    return d.astimezone(timezone.utc)

def preflight(tx, base, delta, sheet, *, current_index_blob, current_ledger_blob,
              observed_sequence, active_leases=(), used_ids=(), now=None):
    """Validate a candidate only; caller must separately run original selector."""
    required = {"schema", "scope", "transaction_id", "parent_index_blob",
                "expected_ledger_blob", "sequence", "writer", "lease_id",
                "lease_expires_utc", "created_utc", "sheet_path", "sheet_blob",
                "base_blob", "delta_blob", "result_blob"}
    if not isinstance(tx, dict) or set(tx) != required:
        raise ValueError("candidate schema fields mismatch")
    if tx["schema"] != "CFB_WEEK12_OVERLAY_CANDIDATE_V1" or tx["scope"] != "QA_ONLY_NOT_CANONICAL":
        raise ValueError("candidate cannot claim canonical authority")
    for key in ("transaction_id", "writer", "lease_id"):
        if not isinstance(tx[key], str) or not tx[key].strip():
            raise ValueError("missing identity: " + key)
    if tx["transaction_id"] in used_ids:
        raise ValueError("duplicate transaction id")
    if tx["lease_id"] in active_leases:
        raise ValueError("competing lease")
    if tx["parent_index_blob"] != current_index_blob or tx["expected_ledger_blob"] != current_ledger_blob:
        raise ValueError("stale parent or canonical ledger lease")
    if type(tx["sequence"]) is not int or tx["sequence"] != observed_sequence + 1:
        raise ValueError("nonconsecutive sequence")
    current = now or datetime.now(timezone.utc)
    if current.tzinfo is None:
        raise ValueError("naive now")
    if utc(tx["created_utc"]) > current.astimezone(timezone.utc):
        raise ValueError("future candidate")
    if utc(tx["lease_expires_utc"]) <= current.astimezone(timezone.utc):
        raise ValueError("expired lease")
    if not isinstance(tx["sheet_path"], str) or not SHEET_PATTERN.fullmatch(tx["sheet_path"]):
        raise ValueError("unsupported candidate sheet path")
    if any(not isinstance(v, bytes) for v in (base, delta, sheet)):
        raise ValueError("byte inputs required")
    if (tx["base_blob"], tx["delta_blob"], tx["result_blob"]) != (EXPECTED_BASE, EXPECTED_DELTA, EXPECTED_RESULT):
        raise ValueError("unexpected immutable lineage")
    if (blob(base), blob(delta), blob(base + delta)) != (EXPECTED_BASE, EXPECTED_DELTA, EXPECTED_RESULT):
        raise ValueError("actual overlay bytes mismatch")
    if blob(sheet) != tx["sheet_blob"]:
        raise ValueError("candidate sheet bytes mismatch")
    from cfb_hot_sheet_current_decision_binding_gate import audit
    result = audit(sheet.decode("utf-8"), (base + delta).decode("utf-8"))
    return {"status": "QA_CANDIDATE_PREFLIGHT_ONLY", "decision_binding": result["verdict"],
            "sheet_blob": tx["sheet_blob"], "decision_blob": EXPECTED_RESULT,
            "canonical_mutation": False, "production_acceptance": False}
