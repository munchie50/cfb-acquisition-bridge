#!/usr/bin/env python3
"""Read-only Week 6 full Saturday scope and explicit-deadline checks.

Coverage PASS is not football research, source truth or betting acceptance.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

BASELINE_BLOB = 'eaeded90f81dd1190e0ef77fc52a448f73ea5dca'
REVIEW_HEADER = ['Kickoff CT','Game','Frozen fair side / total',
                 'DK away spread (price)','DK home spread (price)',
                 'DK over / under (prices)','Side decision','Total decision','Total raw gap']

def blob(text):
    data=text.encode('utf-8')
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def cells(line):
    return [v.strip() for v in line.strip().strip('|').split('|')]

def expected_games(text, expected_blob=BASELINE_BLOB):
    if blob(text)!=expected_blob:
        raise ValueError('baseline blob mismatch; qualify the new baseline separately')
    rows=[cells(line) for line in text.splitlines() if line.startswith('| Sat')]
    if len(rows)!=38 or any(len(row)!=9 for row in rows):
        raise ValueError('unsupported Saturday baseline population/schema')
    games=[row[1] for row in rows]
    if len(set(games))!=38:
        raise ValueError('duplicate baseline identity')
    return games

def review_rows(text):
    lines=text.splitlines()
    headers=[i for i,line in enumerate(lines) if line.startswith('|') and cells(line)==REVIEW_HEADER]
    if len(headers)!=1:
        raise ValueError('exactly one supported full-review table required; shortlist is not full coverage')
    at=headers[0]
    if at+1>=len(lines) or not re.fullmatch(r'[| :\-]+',lines[at+1]):
        raise ValueError('missing review table separator')
    rows=[]
    for line in lines[at+2:]:
        if not line.strip(): break
        if not line.startswith('|'): raise ValueError('malformed review table row')
        row=cells(line)
        if len(row)!=9 or any(not value for value in row):
            raise ValueError('missing market/decision or malformed review row')
        rows.append(row)
    return rows

def check(expected, text):
    if len(expected)!=38 or len(set(expected))!=38:
        raise ValueError('caller scope must declare 38 unique qualified identities')
    rows=review_rows(text)
    games=[row[1] for row in rows]
    if len(games)!=38 or len(set(games))!=38 or set(games)!=set(expected):
        raise ValueError('full-review identity union/count mismatch')
    for game in expected:
        if text.splitlines().count('### '+game)!=1:
            raise ValueError('missing or duplicate per-game rationale section')
        section=text.split('### '+game+'\n',1)[1].split('\n### ',1)[0]
        if not re.search(r'^Side: \S',section,re.M) or not re.search(r'^Total: \S',section,re.M):
            raise ValueError('side and total rationale required independently')
    if '## Nebraska — mandatory unmodeled row' not in text:
        raise ValueError('mandatory unmodeled Nebraska row missing')
    return {'status':'STRUCTURAL_COVERAGE_PASS_NOT_BETTING_ACCEPTANCE',
            'modeled_games':38,'market_verdicts':76,'rationale_sections':38,
            'review_blob':blob(text),'source_truth':'NOT_CERTIFIED',
            'availability_completeness':'NOT_CERTIFIED','executability':'NOT_CERTIFIED',
            'decision_quality':'NOT_CERTIFIED'}

def clock(value):
    if not isinstance(value,str): raise ValueError('explicit timestamp required')
    result=datetime.fromisoformat(value.replace('Z','+00:00'))
    if result.tzinfo is None: raise ValueError('timezone-aware timestamp required')
    return result.astimezone(timezone.utc)

def effective_deadline(default, trip=None, execution=None):
    """Compose explicit inputs; never invent dinner hour or scheduler execution."""
    clocks={'default':clock(default)}
    if trip is not None: clocks['trip']=clock(trip)
    if execution is not None: clocks['execution']=clock(execution)
    earliest=min(clocks.values())
    return {'deadline_utc':earliest.isoformat().replace('+00:00','Z'),
            'binding_constraints':sorted(k for k,v in clocks.items() if v==earliest),
            'trip_constraint':'EXPLICIT' if trip is not None else 'UNVERIFIED_NOT_INVENTED',
            'execution_constraint':'EXPLICIT' if execution is not None else 'UNVERIFIED_NOT_INVENTED',
            'scope':'CLOCK_COMPOSITION_ONLY_NOT_SOURCE_OR_WAIT_ACCEPTANCE'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline',required=True,type=Path)
    parser.add_argument('--review',required=True,type=Path)
    parser.add_argument('--default-deadline')
    parser.add_argument('--trip-deadline')
    parser.add_argument('--execution-cutoff')
    args=parser.parse_args()
    if (args.trip_deadline or args.execution_cutoff) and not args.default_deadline:
        parser.error('default deadline required to compose explicit constraints')
    # Preserve exact bytes, including CRLF, for Git blob verification.
    baseline=args.baseline.read_bytes().decode('utf-8')
    review=args.review.read_bytes().decode('utf-8')
    result=check(expected_games(baseline),review)
    if args.default_deadline:
        result['timing']=effective_deadline(args.default_deadline,args.trip_deadline,args.execution_cutoff)
    else:
        result['timing']='NOT_EVALUATED_NO_EXPLICIT_DEADLINE_INPUT'
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
