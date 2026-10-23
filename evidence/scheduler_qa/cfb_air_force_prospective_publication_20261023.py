"""Manual prospective earned-input replay, not acquisition or automatic execution.

Keep prior canonical bytes and Buffalo's actual immutable review/limits. Compose
new full56 source using retained elapsed context through the normal compiler,
then qualify only the new AirForce kickoff/review from independently read facts.
"""
import copy,json,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
import cfb_week8_publication as w
import cfb_neutral_publication_gate as g
from cfb_neutral_weekly_reconciliation import latest
from cfb_neutral_publication_legacy_replay import packet
REVIEW='evidence/operational/recommendation_reviews/CFB_AIR_FORCE_CONTROLLED_BETA_20261023T023719Z.json'
REF={'path':REVIEW,'commit':'fe7b579df24bb8cfde0e5c8158760cdec5b246dd','blob':'177374b1313f488e2078cd9cc0eb832f5f1a8a88'}

def propose(as_of):
    def read(p):return (ROOT/p).read_text()
    m=read('evidence/operational/CFB_MARKET_MONITOR_STATE.md');d=read('evidence/operational/CFB_DECISION_WAIT_LEDGER.md')
    assert g.blob(m)=='8c8e98e6cb56d638da7420d42ca1fa07c7fc6691'
    assert g.blob(d)=='13709bb0eb6e8e9c0ebc115dda22130737b198a1'
    lineage=read('evidence/scheduler_qa/CFB_WEEK8_ORIGINAL_ANCESTRY_RECOVERY_20261020.json')
    r=json.loads(read(REVIEW));assert g.blob(read(REVIEW))==REF['blob']
    old=latest(d,w.DECISION_TAG)
    assert next(x for x in old['rows'] if x['game_id']==r['game_id'])['state']=='INCONCLUSIVE'
    rows=[{k:copy.deepcopy(v) for k,v in x.items() if k not in ('state_recorded_at_utc','state_evidence')} for x in old['rows']]
    pm,pd=w.compile(m,d,read('evidence/operational/CFB_CBS_WEEK8_TEXT_TABLE_CAPTURE_20261023T023243Z.md'),lineage,
        'CFB_MARKET_MONITOR_20261023T023243Z',as_of,'2026-10-23T02:34:29Z',rows)
    mp,dp=latest(pm,w.MARKET_TAG),latest(pd,w.DECISION_TAG)
    mr=next(x for x in mp['rows'] if x['game_id']==r['game_id'])
    assert mr['kickoff_utc']==r['market_reference']['kickoff_utc']
    mr.update(kickoff_status='QUALIFIED',kickoff_source_url=r['market_reference']['kickoff_source_url'])
    dr=next(x for x in dp['rows'] if x['game_id']==r['game_id'])
    dr.update(state='CONDITIONAL',reason=r['rationale'],cutoff_authority='REVIEW_EVIDENCED',review_ref=REF)
    for key in ('acceptable_number','reconciliation_utc','planning_cutoff_utc','execution_window'):dr[key]=copy.deepcopy(r[key])
    pm=m+packet(mp,w.MARKET_TAG).lstrip('\n');pd=d+packet(dp,w.DECISION_TAG).lstrip('\n')
    assert pm.startswith(m) and pd.startswith(d)
    w.bootstrap_check(pm,pd,lineage);g.inputs(pm,pd,lineage,as_of,'WEEK8')
    execution=read('evidence/operational/CFB_EXECUTION_LEDGER.md');scorecard=read('evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md')
    sheet=g.render(pm,pd,execution,scorecard,lineage,as_of,'WEEK8')
    result=g.audit(sheet,pm,pd,execution,scorecard,lineage,as_of,'WEEK8')
    return pm,pd,sheet,result

if __name__=='__main__':
    out=Path(sys.argv[1]);assert out.is_dir()
    at=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    pm,pd,sheet,result=propose(at)
    for name,content in [('market.md',pm),('decision.md',pd),('sheet.md',sheet)]:
        target=out/name;assert not target.exists();target.write_text(content)
    print(json.dumps({'as_of_utc':at,'gate':result,'market_blob':g.blob(pm),'decision_blob':g.blob(pd),'sheet_blob':g.blob(sheet)}))
