import copy,json,sys
from unittest.mock import patch
sys.path.insert(0,'scripts')
from test_cfb_conditional_recommendation_profile import ConditionalTests,AT
import cfb_conditional_recommendation_profile as profile
import cfb_neutral_publication_gate as gate
from cfb_neutral_publication_legacy_replay import packet
ConditionalTests.setUpClass();t=ConditionalTests();t.setUp()
old_review=copy.deepcopy(t.review)
first_m,first_d=t.args()[:2]
new_review=copy.deepcopy(old_review)
new_review['recorded_at_utc']='2026-10-17T00:20:10Z'
new_review['reconciliation_utc']='2026-10-17T00:40:00Z'
new_review['execution_window']['start_utc']='2026-10-17T00:20:30Z'
ref=new_review['market_reference'];ref.update(collection_start='2026-10-17T00:19:00Z',collection_end='2026-10-17T00:19:30Z')
for q in ref['quotes']:q.update(retrieved_at='2026-10-17T00:19:20Z',offer_updated_at='2026-10-17T00:19:10Z')
new_review['material_sources'][0]['retrieved_at']='2026-10-17T00:19:00Z'
new_review['rationale']='SYNTHETIC QA renewed review; same limits and final cutoff'
now='2026-10-17T00:21:00Z';cycle='CFB_MARKET_MONITOR_20261017T002000Z'
for p in (t.m,t.d):p.update(cycle_id=cycle,as_of_utc=now)
t.target.update(reason=new_review['rationale'],state_recorded_at_utc=now,state_evidence=cycle,review_ref=dict(path='evidence/operational/recommendation_reviews/SYNTHETIC_RENEWAL_ONLY.json',commit='c'*40,blob='d'*40))
for k in ('acceptable_number','reconciliation_utc','planning_cutoff_utc','execution_window'):t.target[k]=copy.deepcopy(new_review[k])
def load(ref):
 return (json.dumps(old_review),'2026-10-17T00:04:50Z') if ref['commit']=='a'*40 else (json.dumps(new_review),'2026-10-17T00:20:20Z')
a=[first_m+packet(t.m,gate.MARKET_TAG),first_d+packet(t.d,gate.DECISION_TAG),t.execution,t.scorecard,t.lineage,now]
with patch.object(profile,'load_review',side_effect=load):
 sheet=gate.render(*a);r=gate.audit(sheet,*a)
 print('Existing full-history/render accepts renewed conditional after old reconciliation:',r)
 assert old_review['acceptable_number']==new_review['acceptable_number']
 assert old_review['planning_cutoff_utc']==new_review['planning_cutoff_utc']
 bad=copy.deepcopy(t.d);target=next(x for x in bad['rows'] if x['game_id']==t.target['game_id'])
 for k in ('acceptable_number','reconciliation_utc','planning_cutoff_utc','execution_window'):target[k]=copy.deepcopy(old_review[k])
 target.update(reason=old_review['rationale'],review_ref=dict(path='evidence/operational/recommendation_reviews/SYNTHETIC_QA_ONLY.json',commit='a'*40,blob='b'*40))
 try:gate.render(a[0],first_d+packet(bad,gate.DECISION_TAG),*a[2:])
 except ValueError as e:print('Old expired review still rejected:',e)
 else:raise AssertionError('expired review accepted')
print('PROTOCOL_REPLAY_ONLY: mocked synthetic immutable reviews, not actual-source review or production publication')
