#!/usr/bin/env python3
"""Read-only Week 6 presentation gate; no source freshness or betting acceptance."""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

REFERENCE = 'evidence/operational/CFB_WEEK6_HOT_SHEET_RESEARCH_CANDIDATE_2026-10-07.md'
REFERENCE_BLOB = '9c2ae1f17bf01bcde2aa82c56c01b1431a1bd6eb'
SECTIONS = {'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY MORNING',
            'SATURDAY AFTERNOON', 'SATURDAY EVENING/NIGHT', 'UNRESOLVED KICKOFF'}
PRODUCTION = re.compile(r'evidence/operational/CFB_WEEK6_HOT_SHEET_\d{4}-\d{2}-\d{2}_\d{4}CT\.md')

def identity(game):
    sides = re.split(r' @ | vs ', game)
    if len(sides) != 2 or not all(sides):
        raise ValueError('unsupported ordered matchup: ' + game)
    return tuple({'FIU': 'Florida International'}.get(s, s) for s in sides)

def reference_ids(content):
    raw = content.encode()
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if blob != REFERENCE_BLOB:
        raise ValueError('reference differs from pinned accepted Week 6 presentation baseline')
    ids = []
    for line in content.splitlines():
        if re.match(r'^\| (Tue|Wed|Thu|Fri|Sat) ', line):
            cells = [s.strip() for s in line.strip('|').split('|')]
            ids.append(identity(cells[1]))
    if len(ids) != 49 or len(set(ids)) != 49:
        raise ValueError('reference must contain 49 unique modeled identities')
    return set(ids)

def validate(content, expected):
    section = None
    sections = set()
    ids = set()
    counts = {}
    for line in content.splitlines():
        if line.startswith('#'):
            heading = line.lstrip('#').strip().upper()
            section = heading if heading in SECTIONS else None
            if section:
                if section in sections:
                    raise ValueError('duplicate section: ' + section)
                sections.add(section)
                counts[section] = 0
            continue
        if not line.startswith('|'):
            continue
        cells = [s.strip() for s in line.strip('|').split('|')]
        if cells[0].startswith('Kickoff') or all(re.fullmatch(r':?-+:?', x) for x in cells):
            continue
        # Any data table row must belong to an explicitly supported kickoff section.
        if section is None or len(cells) != 9:
            raise ValueError('unsectioned or unsupported production table row')
        key = identity(cells[1])
        if key in ids:
            raise ValueError('duplicate game: ' + cells[1])
        if cells[0] == 'UNRESOLVED':
            bucket = 'UNRESOLVED KICKOFF'
        else:
            m = re.fullmatch(r'(Tue|Wed|Thu|Fri|Sat) (\d{1,2}):(\d{2}) (AM|PM)', cells[0])
            if not m:
                raise ValueError('unsupported kickoff display: ' + cells[0])
            day, hour, minute, ampm = m.groups()
            if not 1 <= int(hour) <= 12 or not 0 <= int(minute) <= 59:
                raise ValueError('invalid clock: ' + cells[0])
            h = int(hour) % 12 + (12 if ampm == 'PM' else 0)
            bucket = {'Tue':'TUESDAY','Wed':'WEDNESDAY','Thu':'THURSDAY','Fri':'FRIDAY'}.get(day)
            if day == 'Sat':
                bucket = 'SATURDAY MORNING' if h < 12 else ('SATURDAY AFTERNOON' if h < 17 else 'SATURDAY EVENING/NIGHT')
        if bucket != section:
            raise ValueError('kickoff/section conflict: ' + cells[1])
        ids.add(key)
        counts[section] += 1
    if ids != expected:
        raise ValueError('modeled identity union differs from pinned Week 6 slate')
    if not {'TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY MORNING',
            'SATURDAY AFTERNOON','SATURDAY EVENING/NIGHT'} <= sections:
        raise ValueError('required Week 6 sections missing')
    if '## Nebraska — mandatory unmodeled inclusion' not in content or 'Indiana @ Nebraska' not in content:
        raise ValueError('separate required Nebraska exclusion display missing')
    return {'verdict':'PASS_WEEK6_PRODUCTION_SECTION_PRESENTATION', 'modeled':len(ids), 'counts':counts,
            'scope':'presentation identity/section only; kickoff/source freshness, frozen values, quotes and decisions not certified'}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--reference', default=REFERENCE)
    ap.add_argument('--sheet', action='append', default=[])
    ap.add_argument('--changed-since')
    args = ap.parse_args()
    paths = list(args.sheet)
    if args.changed_since:
        if not re.fullmatch(r'[0-9a-f]{40}', args.changed_since) or set(args.changed_since) == {'0'}:
            raise ValueError('changed-since requires a nonzero full commit SHA')
        changed = subprocess.run(['git','diff','--name-only','--diff-filter=ACMR',args.changed_since,'HEAD'],
                                 check=True,capture_output=True,text=True).stdout.splitlines()
        paths.extend(p for p in changed if PRODUCTION.fullmatch(p))
    if not paths:
        raise ValueError('no production sheet selected')
    expected = reference_ids(Path(args.reference).read_text())
    for path in dict.fromkeys(paths):
        print(json.dumps({'path':path, **validate(Path(path).read_text(),expected)}))

if __name__ == '__main__':
    main()
