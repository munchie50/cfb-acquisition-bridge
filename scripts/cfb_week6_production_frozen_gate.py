#!/usr/bin/env python3
"""Read-only frozen-value checks for sheets selected by the production section gate."""
import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from cfb_hot_sheet_production_section_gate import PRODUCTION

def audit_sheet(path, archive):
    content=Path(path).read_text()
    raw=content.encode()
    sha=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    with tempfile.TemporaryDirectory() as temp:
        payload=Path(temp)/'sheet.json'
        payload.write_text(json.dumps({'content':content,'sha':sha}))
        result=subprocess.run([sys.executable,str(Path(__file__).with_name('cfb_hot_sheet_frozen_values_audit.py')),
                               '--archive',str(archive),'--hot-sheet-json',str(payload),
                               '--first-date','2026-10-06','--last-date','2026-10-10',
                               '--expected-modeled','49'],check=True,capture_output=True,text=True)
    audit=json.loads(result.stdout)
    return {'path':str(path),'verdict':'PASS_WEEK6_FROZEN_DISPLAY_VALUES',
            'matched_rows':audit['matched_rows'],'matched_numeric_fields':audit['matched_numeric_fields'],
            'matched_favorite_directions':audit['matched_favorite_directions'],
            'accepted_archive_sha256':audit['accepted_archive_sha256'],'sheet_blob':sha,
            'scope':'accepted FIRST_FROZEN display fidelity only; no current kickoff, market or decision acceptance'}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--archive',required=True)
    ap.add_argument('--selection-file',required=True)
    args=ap.parse_args()
    records=[json.loads(line) for line in Path(args.selection_file).read_text().splitlines() if line.strip()]
    if not records: raise ValueError('no selected production sheets')
    paths=[]
    for r in records:
        if not isinstance(r,dict) or not isinstance(r.get('path'),str) or not PRODUCTION.fullmatch(r['path']):
            raise ValueError('selection must contain explicit Week 6 production paths')
        if r.get('verdict')!='PASS_WEEK6_PRODUCTION_SECTION_PRESENTATION' or r.get('modeled')!=49:
            raise ValueError('selected section gate did not pass')
        if r['path'] in paths: raise ValueError('duplicate selected path')
        paths.append(r['path'])
    for path in paths: print(json.dumps(audit_sheet(path,args.archive)))

if __name__=='__main__': main()
