"""Read-only Market Monitor run classifier. QA prototype; never changes production."""
from dataclasses import dataclass

STATES = ("NO_UPDATE", "START_ONLY", "WRITE_REJECTED", "PARTIAL_SOURCE", "PUBLISHED_UNVERIFIED", "RUN_PASS")

@dataclass(frozen=True)
class Evidence:
    scheduler_no_update: bool = False
    producer_started: bool = False
    canonical_write_attempted: bool = False
    canonical_write_accepted: bool = False
    source_complete: bool = False
    publication_present: bool = False
    independent_publication_verified: bool = False
    terminal_closure_verified: bool = False

def classify(e: Evidence) -> str:
    """Conservative classification. A green workflow is not acceptance evidence."""
    if e.scheduler_no_update and not e.producer_started:
        return "NO_UPDATE"
    if not e.producer_started:
        return "NO_UPDATE"
    if e.canonical_write_attempted and not e.canonical_write_accepted:
        return "WRITE_REJECTED"
    if not e.source_complete:
        return "PARTIAL_SOURCE" if e.canonical_write_accepted else "START_ONLY"
    if not e.canonical_write_accepted:
        return "START_ONLY"
    if not e.publication_present or not e.independent_publication_verified:
        return "PUBLISHED_UNVERIFIED"
    if not e.terminal_closure_verified:
        return "PUBLISHED_UNVERIFIED"
    return "RUN_PASS"
