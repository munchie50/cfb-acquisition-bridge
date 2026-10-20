"""Audit saved publication integrity and current readiness as separate proofs.

Not a publisher: the live gate stays strict at the actual publication clock.
"""
import argparse
import json
import re
from pathlib import Path
import cfb_neutral_publication_gate as gate
import cfb_hot_sheet_readiness as readiness
from cfb_neutral_publication_legacy_replay import historical


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


def audit_repository(sheet, market, decision, execution, scorecard, lineage, as_of, root):
    """Recover exact declared saved inputs; evaluate live readiness separately."""
    refs = re.findall(r'^\*\*Canonical inputs:\*\* market ([0-9a-f]{40}); decision ([0-9a-f]{40}); execution ([0-9a-f]{40}); scorecard ([0-9a-f]{40})\.$', sheet, re.M)
    if len(refs) != 1: raise ValueError('unique complete saved canonical binding required')
    supplied = (market, decision, execution, scorecard)
    names = ('CFB_MARKET_MONITOR_STATE.md', 'CFB_DECISION_WAIT_LEDGER.md',
             'CFB_EXECUTION_LEDGER.md', 'CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md')
    saved = [text if gate.blob(text) == digest else
             historical(root / 'evidence/operational' / name, digest)
             for text, name, digest in zip(supplied, names, refs[0])]
    if any(gate.blob(text) != digest for text, digest in zip(saved, refs[0])):
        raise ValueError('saved canonical byte identity mismatch')
    result = audit(sheet, *saved, lineage, as_of)
    current = readiness.audit(market, decision, lineage, as_of)
    result['saved_canonical_blobs'] = dict(zip(names, refs[0]))
    result['operational_exceptions'] = ([ 'ELAPSED_CURRENT_QUOTES' ] if current['elapsed_current_quote_game_ids'] else []) + ([ 'OVERDUE_OPEN_DECISIONS' ] if current['overdue_open_decision_game_ids'] else [])
    result['elapsed_current_quote_game_ids'] = current['elapsed_current_quote_game_ids']
    result['overdue_open_decision_game_ids'] = current['overdue_open_decision_game_ids']
    return result


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('sheet', 'market', 'decision', 'execution', 'scorecard', 'lineage'):
        p.add_argument('--' + key, type=Path, required=True)
    p.add_argument('--as-of', required=True)
    p.add_argument('--recover-saved-inputs', action='store_true')
    p.add_argument('--repository-root', type=Path, default=Path('.'))
    args = p.parse_args()
    values = [getattr(args, key).read_text() for key in
              ('sheet', 'market', 'decision', 'execution', 'scorecard', 'lineage')]
    result = (audit_repository(*values, args.as_of, args.repository_root) if args.recover_saved_inputs
              else audit(*values, args.as_of))
    print(json.dumps(result, indent=2))
