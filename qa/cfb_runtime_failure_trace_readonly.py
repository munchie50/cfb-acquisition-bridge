"""Bounded, diagnostic-only classification for CFB runtime failures.

Never contains secrets, changes acceptance, or performs network requests.
"""
import json
import re
from datetime import datetime, timezone

CATEGORIES = (
    "DNS_RESOLUTION", "NETWORK_TIMEOUT", "AUTHORIZATION",
    "GIT_ANCESTRY", "MISSING_INPUT", "COMPILER",
    "PUBLICATION", "CONNECTOR", "UNKNOWN",
)
_SECRET = re.compile(r"(?i)(token|password|authorization|secret|api[_-]?key)\s*[:=]\s*\S+")
_URL_CREDENTIALS = re.compile(r"(https?://)[^/@\s]+@")

def classify(stage, error):
    message = str(error).lower()
    if any(s in message for s in ("could not resolve host", "name or service not known", "temporary failure in name resolution")):
        return "DNS_RESOLUTION"
    if any(s in message for s in ("timed out", "timeout", "connection reset")):
        return "NETWORK_TIMEOUT"
    if any(s in message for s in ("permission denied", "403", "401", "authentication failed")):
        return "AUTHORIZATION"
    if any(s in message for s in ("not an ancestor", "shallow repository", "checkout head differs", "bad object")):
        return "GIT_ANCESTRY"
    if any(s in message for s in ("no such file", "file not found", "missing governed", "missing input")):
        return "MISSING_INPUT"
    if stage == "compiler":
        return "COMPILER"
    if stage == "publication":
        return "PUBLICATION"
    if stage == "connector":
        return "CONNECTOR"
    return "UNKNOWN"

def trace(stage, outcome, error="", correlation_id="", timestamp=None):
    if outcome not in ("PASS", "FAIL", "BLOCKED", "SKIPPED"):
        raise ValueError("invalid diagnostic outcome")
    if not re.fullmatch(r"[A-Za-z0-9_.-]{0,100}", correlation_id):
        raise ValueError("unsafe correlation identifier")
    safe = _URL_CREDENTIALS.sub(r"\1[REDACTED]@", _SECRET.sub("[REDACTED]", str(error)))
    return {
        "schema": "CFB_RUNTIME_DIAGNOSTIC_V1",
        "timestamp_utc": timestamp or datetime.now(timezone.utc).isoformat(),
        "correlation_id": correlation_id,
        "stage": stage,
        "outcome": outcome,
        "failure_category": classify(stage, error) if outcome in ("FAIL", "BLOCKED") else None,
        "error_excerpt": safe[:240],
        "scope": "DIAGNOSTIC_ONLY_NO_PRODUCTION_ACCEPTANCE",
    }

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--stage", required=True)
    p.add_argument("--outcome", required=True)
    p.add_argument("--error", default="")
    p.add_argument("--correlation-id", default="")
    a = p.parse_args()
    print(json.dumps(trace(a.stage, a.outcome, a.error, a.correlation_id), sort_keys=True))
