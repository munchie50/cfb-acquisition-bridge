"""Audit saved publication integrity and current readiness as separate proofs.

Not a publisher: the live gate stays strict at the actual publication clock.
"""
import argparse
import json
import re
from pathlib import Path
import cfb_neutral_publication_gate as gate
import cfb_hot_sheet_readiness as readiness


def audit(sheet, market, decision, execution, scorecard, lineage, as_of):
    boundaries = re.findall(r'^\*\*Publication boundary:\*\* (\S+)$', sheet, re.M)
    if len(boundaries) != 1: raise ValueError('exactly one saved publication boundary required')
    saved_at = boundaries[0]
    if gate.clock(saved_at) > gate.clock(as_of): raise ValueError('future saved publication')
    gate.bootstrap(market, decision, lineage)
    # Whole-render equality binds cycle, boundary and every canonical digest;
    # changing the header to choose an easier clock cannot qualify the sheet.
    integrity = gate.audit(sheet, market, decision, execution, scorecard, lineage, saved_at)
    health = readiness.audit(market, decision, lineage, as_of)
    exceptions = []
    if health['elapsed_current_quote_game_ids']: exceptions.append('ELAPSED_CURRENT_QUOTES')
    if health['overdue_open_decision_game_ids']: exceptions.append('OVERDUE_OPEN_DECISIONS')
    return {'verdict': 'PASS_SAVED_PUBLICATION_INTEGRITY_ONLY',
            'publication_boundary_utc': saved_at, 'audit_as_of_utc': as_of,
            'integrity': integrity, 'operational_exceptions': exceptions,
            'elapsed_current_quote_game_ids': health['elapsed_current_quote_game_ids'],
            'overdue_open_decision_game_ids': health['overdue_open_decision_game_ids'],
            'current_operational_acceptance': 'NOT_CERTIFIED',
            'scope': 'CODE_QA_SAVED_VIEW_ONLY_NOT_FRESH_MARKET_OR_RUN_PASS'}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('sheet', 'market', 'decision', 'execution', 'scorecard', 'lineage'):
        p.add_argument('--' + key, type=Path, required=True)
    p.add_argument('--as-of', required=True)
    args = p.parse_args()
    print(json.dumps(audit(*(getattr(args, key).read_text() for key in
        ('sheet', 'market', 'decision', 'execution', 'scorecard', 'lineage')), args.as_of), indent=2))
