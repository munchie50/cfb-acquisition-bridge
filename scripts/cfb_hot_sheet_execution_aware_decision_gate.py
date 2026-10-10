#!/usr/bin/env python3
"""Qualified Oct10 execution-aware verdict display; no bet/settlement acceptance."""
import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from cfb_full_review_scope_gate import expected_games, cells
from cfb_hot_sheet_current_decision_binding_gate import publication, blob

CYCLE = 'CFB_MARKET_MONITOR_20261010T180302Z'
MARKER = '## Saturday 13:00 CT final reconciliation and execution-aware disposition — 2026-10-10 13:12 CT'
EXECUTION_PATH = 'evidence/operational/CFB_EXECUTION_LEDGER.md'
TICKETS = {
    'CFB_OCT09-01': ('James Madison @ Georgia Southern', 'James Madison', 'JMU', False),
    'CFB_OCT09-02': ('Boise State @ Fresno State', 'Fresno State', 'Fresno', True),
    'CFB_OCT09-03': ('Old Dominion @ App State', 'Appalachian State', 'App State', True),
    'CFB_OCT09-04': ('Miami (OH) @ Massachusetts', 'Massachusetts', 'UMass', True),
}

def audit(sheet, baseline, decision, execution):
    cycle = re.findall(r'^Run: (.+)$', sheet, re.M)
    if cycle != [CYCLE] or decision.count(MARKER) != 1:
        raise ValueError('unsupported current execution-aware boundary')
    body = decision.split(MARKER, 1)[1]
    if re.search(r'^## ', body, re.M) or not body.lstrip().startswith('Run: '+CYCLE+'.'):
        raise ValueError('later or mismatched decision boundary requires qualification')
    bindings = re.findall(r'^Canonical inputs: market [0-9a-f]{40}; decision ([0-9a-f]{40}); execution ([0-9a-f]{40})\.$', sheet, re.M)
    if bindings != [(blob(decision), blob(execution))]:
        raise ValueError('current decision/execution source binding mismatch')
    expected = set(expected_games(baseline))
    rows = [cells(l) for l in sheet.splitlines() if l.startswith('| Sat')]
    if len(rows) != 38 or any(len(r) != 9 for r in rows) or len({r[1] for r in rows}) != 38 or {r[1] for r in rows} != expected:
        raise ValueError('Saturday decision identity/schema mismatch')
    rendered = {r[1]: r for r in rows}
    actual = {}
    for line in execution.splitlines():
        if not line.startswith('| CFB_OCT09-'):
            continue
        row = cells(line)
        if len(row) != 9 or row[0] not in TICKETS or row[0] in actual:
            raise ValueError('unsupported or duplicate current ticket identity/schema')
        actual[row[0]] = row
    if set(actual) != set(TICKETS):
        raise ValueError('four established current tickets required')
    ticket_games = {}
    stake = 0
    for eid, (game, selection, display_name, completed) in TICKETS.items():
        ticket = actual[eid]
        canonical_game = game.replace(' @ ', ' at ').replace('App State', 'Appalachian State')
        if ticket[2] != canonical_game or ticket[3] != selection+' / SPREAD' or not re.fullmatch(r'[+-]?\d+(?:\.\d+)?', ticket[4]) or not re.fullmatch(r'-\d+', ticket[5]) or ticket[6] != '$5.00':
            raise ValueError('ticket game/selection/stake schema mismatch')
        stake += 5
        quoted = display_name+' '+ticket[4]+' ('+ticket[5]+'), $5, issued Oct 9'
        if 'actual Caesars execution '+quoted not in rendered[game][3]:
            raise ValueError('displayed execution facts differ from canonical ticket')
        source_quote = 'actual '+selection+' '+ticket[4]+' ('+ticket[5]+'), $5'
        if not re.search(re.escape('Canonical execution '+eid+' records ')+r'(?:an )?'+re.escape(source_quote), body):
            raise ValueError('decision execution reference differs from canonical ticket')
        ticket_games[game] = completed
    for game, row in rendered.items():
        if ticket_games.get(game):
            wanted = 'BET NOW CONDITIONAL — EXECUTED / TOTAL PASS'
            if row[5] != wanted or row[8] != 'Complete / no further action' or 'Execution established' not in row[6]:
                raise ValueError('completed wager reopened or execution qualifier missing: '+game)
        elif game in ticket_games:
            if row[5] != 'PASS / TOTAL PASS; ACTUAL EXECUTION RECORDED' or row[8] != 'None / no further action' or 'Prospective PASS preserved' not in row[6]:
                raise ValueError('actual ticket rewrote JMU prospective PASS')
        elif row[5] != 'PASS / TOTAL PASS' or row[8] != 'None / PASS':
            raise ValueError('unexecuted PASS/current total disposition changed: '+game)
    required = ['prior BET NOW CONDITIONAL is now execution-complete for portfolio management.',
                'decision remains PASS / TOTAL PASS.',
                'Remaining 34 Saturday sides and all 38 Saturday totals remain PASS.',
                'No further casino trip or Saturday wager is recommended']
    if any(x not in body for x in required) or body.count(required[0]) != 3:
        raise ValueError('unsupported canonical portfolio disposition')
    if 'three previously conditional sides are executed' not in sheet or 'remaining 34 sides remain PASS' not in sheet or 'all 38 totals remain PASS' not in sheet or 'Four established October 9 tickets total $20' not in sheet:
        raise ValueError('published portfolio summary mismatch')
    return {'verdict': 'PASS_QUALIFIED_OCT10_EXECUTION_AWARE_DECISION_DISPLAY',
            'matched_games': 38, 'matched_market_verdicts': 76,
            'completed_conditional_sides': 3, 'separate_actual_pass_side': 1,
            'remaining_pass_sides': 34, 'actual_tickets': 4, 'stake_usd': stake,
            'decision_blob': blob(decision), 'execution_blob': blob(execution), 'sheet_blob': blob(sheet),
            'scope': 'exact qualified current decision/execution projection only; not betting quality, current offers, chronology, allocation, settlement or all source truth'}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--index', required=True, type=Path)
    p.add_argument('--decision', required=True, type=Path)
    p.add_argument('--execution', required=True, type=Path)
    p.add_argument('--baseline', required=True, type=Path)
    p.add_argument('--repository-root', type=Path, default=Path('.'))
    p.add_argument('--as-of')
    a = p.parse_args()
    root = a.repository_root.resolve()
    def loader(path):
        target = (root/path).resolve()
        if not target.is_relative_to(root):
            raise ValueError('source path escapes repository')
        return target.read_bytes().decode()
    index = a.index.read_bytes().decode()
    decision = a.decision.read_bytes().decode()
    execution = a.execution.read_bytes().decode()
    at = a.as_of or datetime.now(timezone.utc).isoformat()
    bound = publication(index, decision, loader, at)
    from cfb_recovery_navigation_reader import read
    refs = [r for r in read(index, at)['frontier']['pointers'] if r['path'] == EXECUTION_PATH]
    if len(refs) != 1 or refs[0]['blob'] != blob(execution):
        raise ValueError('stale or missing current execution pointer')
    result = audit(loader(bound['sheet_path']), a.baseline.read_bytes().decode(), decision, execution)
    print(json.dumps({'sheet_path': bound['sheet_path'], **result}, indent=2))

if __name__ == '__main__':
    main()
