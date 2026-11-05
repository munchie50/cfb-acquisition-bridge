"""Authentic unresolved history, hypothetical later source clock; no live decision."""
import copy
import json
import re
import unittest
from pathlib import Path
import cfb_neutral_publication_gate as gate
import cfb_week10_publication as week
import cfb_week10_missed_review as missed
from cfb_neutral_publication_legacy_replay import packet, historical

ROOT = Path(__file__).resolve().parents[1]
AT = '2026-11-05T01:00:00Z'
CYCLE = 'CFB_MARKET_MONITOR_20261105T005623Z'


class MissedReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.market = historical(ROOT/'evidence/operational/CFB_MARKET_MONITOR_STATE.md', '9a2391743e3b72840437e6b066f3225054cd7203')
        cls.decision = historical(ROOT/'evidence/operational/CFB_DECISION_WAIT_LEDGER.md', missed.PRIOR_BLOB)
        cls.lineage = (ROOT/'evidence/scheduler_qa/CFB_WEEK10_ORIGINAL_ANCESTRY_RECOVERY_20261104.json').read_text()
        cls.capture = (ROOT/'evidence/operational/CFB_CBS_WEEK10_TABLE_CAPTURE_20261104T191505Z.md').read_text()
        cls.prior = gate.selected_block(cls.decision,week.DECISION_TAG,gate.WEEKLY_DECISION_SCHEMAS,gate.clock(AT))
        cls.rows = [{k:v for k,v in r.items() if k not in ('state_recorded_at_utc','state_evidence')} for r in cls.prior['rows']]
        row = next(r for r in cls.rows if r['game_id']==missed.GAME)
        row.update(state='HISTORICAL_GAP',reason=missed.REASON,reconciliation_utc=None)

    @classmethod
    def build(cls, **kw):
        args=dict(market=cls.market,decision=cls.decision,capture=cls.capture,lineage=cls.lineage,
                  cycle=CYCLE,as_of=AT,recovered_by='2026-11-05T00:59:30Z',decision_rows=copy.deepcopy(cls.rows))
        args.update(kw)
        return week.compile(**args)

    def test_honest_recognition_preserves_original_history_and_closes_expired_condition(self):
        pm,pd=self.build()
        self.assertTrue(pm.startswith(self.market));self.assertTrue(pd.startswith(self.decision))
        result=gate.inputs(pm,pd,self.lineage,AT,'WEEK10')
        row=result[4][missed.GAME]
        self.assertEqual(row['state'],'HISTORICAL_GAP')
        self.assertEqual(row['state_recorded_at_utc'],AT)
        self.assertEqual(row['state_evidence'],CYCLE)
        self.assertEqual(sum(r['state']=='HISTORICAL_GAP' for r in result[4].values()),3)
        old=next(r for r in self.prior['rows'] if r['game_id']=='401866455')
        self.assertEqual(result[4]['401866455'],old)
        sheet=gate.render(pm,pd,'execution fixture','scorecard fixture',self.lineage,AT,'WEEK10')
        self.assertIn('3 HISTORICAL_GAP',sheet)
        self.assertIn('Closed conditional history',sheet)
        self.assertIn('MISSED PRE-EVENT REVIEW',sheet)

    def test_retaining_expired_inconclusive_still_fails(self):
        rows=copy.deepcopy(self.rows)
        old=next(r for r in self.prior['rows'] if r['game_id']==missed.GAME)
        rows[ next(i for i,r in enumerate(rows) if r['game_id']==missed.GAME) ]={k:v for k,v in old.items() if k not in ('state_recorded_at_utc','state_evidence')}
        with self.assertRaises(ValueError):self.build(decision_rows=rows)

    def test_no_hindsight_pass_or_unknown_gap_or_limit(self):
        for gid,state,field,value in [(missed.GAME,'PASS','reason','made-up completed review'),
                                      ('401869964','HISTORICAL_GAP','reconciliation_utc',None),
                                      (missed.GAME,'HISTORICAL_GAP','acceptable_number',1.5)]:
            rows=copy.deepcopy(self.rows);r=next(r for r in rows if r['game_id']==gid)
            r['state']=state;r[field]=value
            with self.subTest(game=gid,state=state,field=field),self.assertRaises(ValueError):self.build(decision_rows=rows)

    def test_backdating_or_modified_prior_rejected(self):
        with self.assertRaises(ValueError):self.build(as_of='2026-11-05T00:50:00Z',recovered_by='2026-11-05T00:49:30Z',cycle='CFB_MARKET_MONITOR_20261105T004900Z')
        with self.assertRaises(ValueError):self.build(decision=self.decision.replace('Over44.5is a candidate only','Over44.5is already resolved',1))

    def test_recognition_is_immutable_and_remains_valid_afterward(self):
        pm,pd=self.build();ctx=week.recovery_context(pm,pd,self.lineage)
        self.assertIn(missed.GAME,ctx['recognized_gaps'])
        last=json.loads(list(re.finditer(r'^```'+week.DECISION_TAG+r'\n(.*?)^```[ \t]*$',pd,re.M|re.S))[-1][1])
        for state in ('INCONCLUSIVE','PASS'):
            newer=copy.deepcopy(last);newer['cycle_id']='CFB_MARKET_MONITOR_20261105T010100Z';newer['as_of_utc']='2026-11-05T01:02:00Z'
            next(r for r in newer['rows'] if r['game_id']==missed.GAME)['state']=state
            with self.subTest(state=state),self.assertRaises(ValueError):
                week.recovery_context(pm,pd+packet(newer,week.DECISION_TAG),self.lineage)


if __name__=='__main__':unittest.main()
