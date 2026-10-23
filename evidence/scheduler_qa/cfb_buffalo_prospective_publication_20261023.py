"""Manual earned-input publication replay; no acquisition, bet placement or model change.

Uses the unchanged full56 normal compiler, then qualifies ONLY the new packet's
Buffalo kickoff/review from the committed independent evidence. Old bytes remain
exact prefixes. Source truth remains a human review obligation, not code proof.
"""
import copy,json,sys
from datetime import datetime,timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'scripts'))
import cfb_week8_publication as w
import cfb_neutral_publication_gate as g
from cfb_neutral_weekly_reconciliation import latest
from cfb_neutral_publication_legacy_replay import packet

ROOT=Path(__file__).resolve().parents[2]
REVIEW='evidence/operational/recommendation_reviews/CFB_BUFFALO_CONTROLLED_BETA_20261023T021956Z.json'
REF={'path':REVIEW,'commit':'3133a89a3079c3a58aa30825f81797401f14c244','blob':'90b9db5fb6814a47e399f61f1f6aab74741daea9'}

def propose(as_of):
    def read(p):return (ROOT/p).read_text()
    m=read('evidence/operational/CFB_MARKET_MONITOR_STATE.md')
    d=read('evidence/operational/CFB_DECISION_WAIT_LEDGER.md')
    lineage=read('evidence/scheduler_qa/CFB_WEEK8_ORIGINAL_ANCESTRY_RECOVERY_20261020.json')
    r=json.loads(read(REVIEW));assert g.blob(read(REVIEW))==REF['blob']
    old=latest(d,w.DECISION_TAG)
    assert next(x for x in old['rows'] if x['game_id']==r['game_id'])['state']=='INCONCLUSIVE'
    rows=[]
    for row in old['rows']:
        row={k:copy.deepcopy(v) for k,v in row.items() if k not in ('state_recorded_at_utc','state_evidence')}
        if row['state']=='INCONCLUSIVE':
            if row['reconciliation_utc'] is None or g.clock(row['reconciliation_utc'])>g.clock('2026-10-23T18:00:00Z'):
                row['reconciliation_utc']='2026-10-23T18:00:00Z'
            row['reason']+='; Prior partial football review carried, not requalified in this focused Buffalo pass. Existing Friday13CT research obligation applies before actual Friday19CT latest placement; refreshed prices alone are not a recommendation'
        rows.append(row)
    # First generate a normal full-population neutral packet; compiler's final
    # validation intentionally cannot invent independent kickoff qualification.
    pm,pd=w.compile(m,d,read('evidence/operational/CFB_CBS_WEEK8_TEXT_TABLE_CAPTURE_20261023T020603Z.md'),lineage,
        'CFB_MARKET_MONITOR_20261023T020603Z',as_of,'2026-10-23T02:11:40Z',rows)
    mp,dp=latest(pm,w.MARKET_TAG),latest(pd,w.DECISION_TAG)
    mr=next(x for x in mp['rows'] if x['game_id']==r['game_id'])
    assert mr['kickoff_utc']==r['market_reference']['kickoff_utc']
    mr.update(kickoff_status='QUALIFIED',kickoff_source_url=r['market_reference']['kickoff_source_url'])
    dr=next(x for x in dp['rows'] if x['game_id']==r['game_id'])
    dr.update(state='CONDITIONAL',reason=r['rationale'],cutoff_authority='REVIEW_EVIDENCED',review_ref=REF)
    for key in ('acceptable_number','reconciliation_utc','planning_cutoff_utc','execution_window'):dr[key]=copy.deepcopy(r[key])
    dp['schema']=g.CONDITIONAL_DECISION_SCHEMA
    for x in dp['rows']:x.setdefault('review_ref',None)
    pm=m+packet(mp,w.MARKET_TAG).lstrip('\n');pd=d+packet(dp,w.DECISION_TAG).lstrip('\n')
    assert pm.startswith(m) and pd.startswith(d)
    w.bootstrap_check(pm,pd,lineage);g.inputs(pm,pd,lineage,as_of,'WEEK8')
    execution=read('evidence/operational/CFB_EXECUTION_LEDGER.md')
    scorecard=read('evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md')
    sheet=g.render(pm,pd,execution,scorecard,lineage,as_of,'WEEK8')
    result=g.audit(sheet,pm,pd,execution,scorecard,lineage,as_of,'WEEK8')
    return pm,pd,sheet,result

if __name__=='__main__':
    out=Path(sys.argv[1]);assert out.is_dir()
    at=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    pm,pd,sheet,result=propose(at)
    for name,content in [('market.md',pm),('decision.md',pd),('sheet.md',sheet)]:
        target=out/name
        assert not target.exists()
        target.write_text(content)
    print(json.dumps({'as_of_utc':at,'gate':result,'market_blob':g.blob(pm),'decision_blob':g.blob(pd),'sheet_blob':g.blob(sheet)}))
