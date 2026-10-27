"""Authentic four reviews, retained source, explicit synthetic publication clock.

These fixtures test publication behavior, never substitute for current research.
"""
import copy
import json
import unittest
from pathlib import Path
from unittest.mock import patch
import cfb_expired_unpublished_review as expired
import cfb_neutral_publication_gate as gate
import cfb_hot_sheet_readiness as readiness
import cfb_week9_publication as week
from cfb_neutral_publication_legacy_replay import historical

ROOT=Path(__file__).resolve().parents[1]
AT='2026-10-27T22:10:00Z'
CYCLE='CFB_MARKET_MONITOR_20261027T220900Z'

class ExpiredUnpublishedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.market=historical(ROOT/'evidence/operational/CFB_MARKET_MONITOR_STATE.md','02df1f08c249bc859760e13de38b0c160f0759a8')
        cls.decision=historical(ROOT/'evidence/operational/CFB_DECISION_WAIT_LEDGER.md',expired.PRIOR_BLOB)
        cls.lineage=(ROOT/'evidence/scheduler_qa/CFB_WEEK9_ORIGINAL_ANCESTRY_RECOVERY_20261025.json').read_text()
        cls.capture=(ROOT/'evidence/operational/CFB_CBS_WEEK9_TEXT_TABLE_CAPTURE_20261026T232059Z.md').read_text()

    @staticmethod
    def loader(ref):
        trusted=next(t for t in expired.TRUSTED.values() if t['path']==ref['path'])
        return (ROOT/ref['path']).read_text(),trusted['committed_at']

    def setUp(self):
        self.patcher=patch.object(expired,'load_review',side_effect=self.loader)
        self.patcher.start();self.addCleanup(self.patcher.stop)
        self.rows=[dict(game_id=r['game_id'],state='PASS',reason='SYNTHETIC QA ONLY researched no supported offer',
                        reconciliation_utc=None,planning_cutoff_utc=None,cutoff_authority='UNVERIFIED',
                        acceptable_number=None,execution_window=None)
                   for r in json.loads(self.lineage)['rows']]
        for row in self.rows:
            if row['game_id'] in expired.TRUSTED:row.update(expired.decision_row(row['game_id']))

    def build(self,**changes):
        args=dict(market=self.market,decision=self.decision,capture=self.capture,lineage=self.lineage,
                  cycle=CYCLE,as_of=AT,recovered_by=AT,decision_rows=self.rows)
        args.update(changes)
        return week.compile(**args)

    def test_full_compiler_renderer_readiness_and_no_opportunities(self):
        m,d=self.build()
        sheet=gate.render(m,d,'execution fixture','scorecard fixture',self.lineage,AT,'WEEK9')
        gate.audit(sheet,m,d,'execution fixture','scorecard fixture',self.lineage,AT,'WEEK9')
        r=readiness.audit(m,d,self.lineage,AT,'WEEK9')
        self.assertTrue(m.startswith(self.market));self.assertTrue(d.startswith(self.decision))
        self.assertEqual(sheet.count('| EXPIRED BEFORE PUBLICATION — HISTORY ONLY |'),4)
        self.assertEqual(sum(l.startswith('| ') and ' @ ' in l for l in sheet.splitlines()),56)
        self.assertIn('**Primary section:** NONE',sheet)
        self.assertNotIn('Conditional recommendations are shown',sheet)
        self.assertEqual(r['expired_unpublished_reviews'],4)
        self.assertEqual(r['conditional_recommendations'],0)
        self.assertEqual(r['evaluation_coverage']['counts']['EXPIRED_UNPUBLISHED_REVIEW'],4)
        self.assertTrue(all(not row['review_window']['review_required'] for row in r['rows'] if row['state']==expired.STATE))

    def test_exact_retention_after_kickoff_without_current_offer(self):
        m,d=self.build()
        rows=[{k:v for k,v in r.items() if k not in ('state_recorded_at_utc','state_evidence')}
              for r in gate.inputs(m,d,self.lineage,AT,'WEEK9')[4].values()]
        later='2026-10-29T04:00:00Z'
        pm,pd=week.compile(m,d,self.capture,self.lineage,'CFB_MARKET_MONITOR_20261029T040000Z',later,later,rows)
        parsed=gate.inputs(pm,pd,self.lineage,later,'WEEK9')
        self.assertEqual(parsed[4]['401871058'],gate.inputs(m,d,self.lineage,AT,'WEEK9')[4]['401871058'])
        self.assertIsNone(parsed[3]['401871058']['current'])
        sheet=gate.render(pm,pd,'execution fixture','scorecard fixture',self.lineage,later,'WEEK9')
        self.assertIn('no reconstructed decision',sheet)

    def test_preexpiry_or_postkickoff_first_recognition_rejected(self):
        for at in ('2026-10-27T17:59:00Z','2026-10-29T04:00:00Z'):
            with self.subTest(at=at),self.assertRaises(ValueError):
                self.build(as_of=at,recovered_by=at,cycle='CFB_MARKET_MONITOR_'+gate.clock(at).strftime('%Y%m%dT%H%M%SZ'))

    def test_changed_review_fields_and_wrong_identity_rejected(self):
        original=copy.deepcopy(self.rows)
        for field,value in [('planning_cutoff_utc','2026-10-28T18:00:00Z'),
                            ('acceptable_number',dict(market='SPREAD',selection='away',line=99,minimum_price=-999,direction='AT_LEAST')),
                            ('reason','rewritten review')]:
            self.rows=copy.deepcopy(original)
            next(r for r in self.rows if r['game_id']=='401871058')[field]=value
            with self.subTest(field=field),self.assertRaises(ValueError):self.build()
        self.rows=copy.deepcopy(original)
        target=next(r for r in self.rows if r['game_id']=='401871058')
        target['review_ref']=copy.deepcopy(expired.TRUSTED['401856842'])
        target['review_ref'].pop('committed_at')
        with self.assertRaises(ValueError):self.build()

    def test_unknown_profile_and_changed_prior_bytes_rejected(self):
        m,d=self.build()
        row=gate.inputs(m,d,self.lineage,AT,'WEEK9')[4]['401871058']
        model=json.loads(self.lineage)['rows'][0]
        source=gate.inputs(m,d,self.lineage,AT,'WEEK9')[3]['401871058']
        packet={'as_of_utc':AT}
        for profile in ('WEEK7','WEEK8','WEEK10'):
            with self.subTest(profile=profile),self.assertRaises(ValueError):expired.validate(row,source,model,packet,d,profile)
        with self.assertRaises(ValueError):self.build(decision=self.decision.replace('CFB','CFX',1))

    def test_expired_recognition_cannot_change_reopen_or_become_pass(self):
        m,d=self.build()
        originals=[{k:v for k,v in r.items() if k not in ('state_recorded_at_utc','state_evidence')}
                   for r in gate.inputs(m,d,self.lineage,AT,'WEEK9')[4].values()]
        for change in ({'state':'PASS','review_ref':None,'acceptable_number':None,'execution_window':None,'cutoff_authority':'UNVERIFIED'},
                       {'state':'CONDITIONAL'}, {'reason':'changed'}):
            rows=copy.deepcopy(originals)
            next(r for r in rows if r['game_id']=='401871058').update(change)
            with self.subTest(change=change),self.assertRaises(ValueError):
                week.compile(m,d,self.capture,self.lineage,'CFB_MARKET_MONITOR_20261027T221100Z',
                             '2026-10-27T22:11:00Z','2026-10-27T22:11:00Z',rows)

    def test_forged_content_or_commit_clock_rejected(self):
        ref={k:expired.TRUSTED['401871058'][k] for k in ('path','commit','blob')}
        content,committed=self.loader(ref)
        for pair in ((content+' ',committed),(content,'2026-10-27T17:59:00Z')):
            with patch.object(expired,'load_review',return_value=pair),self.assertRaises(ValueError):self.build()

if __name__=='__main__':unittest.main()
