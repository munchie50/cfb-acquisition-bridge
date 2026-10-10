#!/usr/bin/env python3
"""Read-only total-number fidelity for separately qualified Oct9/Oct10 Week6 schemas."""
import argparse
import hashlib
import json
import re
import subprocess
import unicodedata
from decimal import Decimal
from pathlib import Path

MARKET_PATH = 'evidence/operational/CFB_MARKET_MONITOR_STATE.md'
CYCLE = 'CFB_MARKET_MONITOR_20261009T180108Z'
MARKER = '## Friday 13:01 CT scheduled full-board benchmark — 2026-10-09'
PROFILES = {
    CYCLE: (MARKER, ('Fri ', 'Sat '), 43, 6, 'PASS_QUALIFIED_OCT09_MARKET_TOTAL_DISPLAY'),
    'CFB_MARKET_MONITOR_20261010T120036Z': (
        '## Saturday scheduled board refresh — 2026-10-10 07:03 CT',
        ('Sat ',), 38, 11, 'PASS_QUALIFIED_OCT10_MARKET_TOTAL_DISPLAY'),
}
ALIASES = {'Appalachian State': 'App State', 'Massachusetts': 'UMass'}

def blob(content):
    raw = content.encode('utf-8')
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()

def identity(game):
    parts = game.replace(' vs ', ' @ ').split(' @ ')
    if len(parts) != 2:
        raise ValueError('unsupported ordered game identity')
    def team(s):
        s = ALIASES.get(s.strip(), s.strip())
        s = ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))
        return re.sub(r'[^a-z0-9]', '', s.lower())
    return tuple(team(p) for p in parts)

def declared_market(sheet):
    refs = re.findall(r'^Canonical inputs: market ([0-9a-f]{40}); decision [0-9a-f]{40}\.$', sheet, re.M)
    cycles = re.findall(r'^(?:Run|Underlying market/decision cycle): (CFB_MARKET_MONITOR_[A-Za-z0-9]+)$', sheet, re.M)
    if len(refs) != 1 or len(cycles) != 1 or cycles[0] not in PROFILES:
        raise ValueError('unsupported or ambiguous sheet canonical cycle/source binding')
    return refs[0]

def totals(text):
    # Ordinary total tuples and source-labelled o/u endpoints are separate forms.
    # Never extract odds, ML, frozen totals or first-observed values.
    text = text.split('; First observation', 1)[0].split('. First observation', 1)[0]
    ordinary = re.findall(r'\btotal[s]?\s+(\d+(?:\.\d+)?(?:\s*[/–-]\s*\d+(?:\.\d+)?)*)', text, re.I)
    labelled = re.findall(r'\bdisplayed totals\s+([^;]+)', text, re.I)
    if len(ordinary) + len(labelled) != 1:
        raise ValueError('missing or ambiguous total-number display')
    if ordinary:
        raw = re.findall(r'\d+(?:\.\d+)?', ordinary[0])
    else:
        raw = re.findall(r'\b[ou](\d+(?:\.\d+)?)\b', labelled[0], re.I)
    values = [Decimal(n) for n in raw]
    if not values or any(v <= 0 or v > 200 for v in values) or len(set(values)) != len(values):
        raise ValueError('invalid or duplicate total endpoints')
    return frozenset(values)

def audit(sheet, market):
    source_sha = declared_market(sheet)
    cycle = re.findall(r'^(?:Run|Underlying market/decision cycle): (CFB_MARKET_MONITOR_[A-Za-z0-9]+)$', sheet, re.M)[0]
    marker, days, modeled, uncovered, verdict = PROFILES[cycle]
    if blob(market) != source_sha:
        raise ValueError('declared market blob does not match supplied bytes')
    if market.count(marker) != 1:
        raise ValueError('unsupported or ambiguous canonical benchmark boundary')
    block = market.split(marker, 1)[1].split('\n## ', 1)[0]
    if len(re.findall(r'^Run: '+cycle+r'\.', block, re.M)) != 1:
        raise ValueError('canonical benchmark cycle mismatch')
    source = {}
    for line in block.splitlines():
        if not line.startswith('- ') or ': ' not in line:
            continue
        game, quote = line[2:].split(': ', 1)
        k = identity(game)
        if k in source:
            raise ValueError('duplicate canonical quote identity')
        source[k] = totals(quote)
    nebraska = identity('Indiana @ Nebraska')
    if len(source) != modeled + 1 or nebraska not in source:
        raise ValueError('qualified modeled-plus-Nebraska source population mismatch')
    displays = {}
    weekly_rows = 0
    for line in sheet.splitlines():
        if not line.startswith('| '):
            continue
        cols = [c.strip() for c in line.strip('|').split('|')]
        if not re.fullmatch(r'(Tue|Wed|Thu|Fri|Sat) \d{1,2}:\d{2} (AM|PM)|UNRESOLVED', cols[0]):
            continue
        if len(cols) != 9:
            raise ValueError('unsupported production table schema')
        weekly_rows += 1
        if cols[0].startswith(days):
            k = identity(cols[1])
            if k in displays:
                raise ValueError('duplicate displayed quote identity')
            displays[k] = totals(cols[3])
    lines = [l for l in sheet.splitlines() if l.startswith('Indiana @ Nebraska — ')]
    if len(lines) != 1:
        raise ValueError('unique mandatory Nebraska display required')
    displays[nebraska] = totals(lines[0].split('Current public benchmark: ', 1)[-1].split('Decision:', 1)[0])
    if weekly_rows != 49 or len(displays) != modeled + 1 or set(displays) != set(source):
        raise ValueError('display/source identity union mismatch')
    for k in source:
        if displays[k] != source[k]:
            raise ValueError('unsupported or omitted total endpoint for '+str(k)+': displayed '+str(sorted(displays[k]))+' vs canonical '+str(sorted(source[k])))
    return {'verdict': verdict, 'cycle': cycle,
            'matched_modeled_total_displays': modeled, 'matched_unmodeled_total_displays': 1,
            'market_blob': source_sha, 'sheet_blob': blob(sheet),
            'uncovered_earlier_week_modeled_rows': uncovered,
            'scope': 'declared canonical total-number endpoints only; no spread/price/ML, source truth/freshness, execution or decision certification'}

def recovered_market(sha):
    objects = subprocess.run(['git', 'rev-list', '--objects', '--all', '--', MARKET_PATH],
                             check=True, capture_output=True, text=True).stdout.splitlines()
    if sha+' '+MARKET_PATH not in objects:
        raise ValueError('declared blob not recovered at canonical market path in repository history')
    raw = subprocess.run(['git', 'cat-file', 'blob', sha], check=True, capture_output=True).stdout
    return raw.decode('utf-8')

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--sheet')
    group.add_argument('--selection-file')
    ap.add_argument('--market', help='explicit exact declared source snapshot; otherwise recover canonical Git blob locally')
    a = ap.parse_args()
    if a.sheet:
        paths = [a.sheet]
    else:
        from cfb_hot_sheet_production_section_gate import PRODUCTION
        records = [json.loads(l) for l in Path(a.selection_file).read_text().splitlines() if l.strip()]
        if not records:
            raise ValueError('empty selected sheets')
        paths = []
        for r in records:
            if not isinstance(r, dict) or not isinstance(r.get('path'), str) or not PRODUCTION.fullmatch(r['path']):
                raise ValueError('unsupported selected production path')
            if r.get('verdict') != 'PASS_WEEK6_PRODUCTION_SECTION_PRESENTATION' or r.get('modeled') != 49 or r['path'] in paths:
                raise ValueError('invalid or duplicate section-gate selection')
            paths.append(r['path'])
    for path in paths:
        sheet = Path(path).read_text()
        market = Path(a.market).read_text() if a.market else recovered_market(declared_market(sheet))
        print(json.dumps({'path': path, **audit(sheet, market)}))

if __name__ == '__main__':
    main()
