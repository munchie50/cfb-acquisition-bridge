"""Authentic parents/capture with EXPLICIT SYNTHETIC replay clocks/decisions."""
import copy
import json
import unittest
from pathlib import Path
from unittest.mock import patch
import cfb_neutral_publication_gate as g
import cfb_week9_publication as w
import cfb_hot_sheet_readiness as readiness
from cfb_neutral_publication_legacy_replay import historical
from cfb_week9_review_recovery import validate

ROOT=Path(__file__).resolve().parents[1]
AT='2026-10-26T18:25:00Z'
BY='2026-10-26T18:24:00Z'  # Synthetic replay, never a claimed real retrieval.
CYCLE='CFB_PRESENTATION_RECONCILIATION_20261026T182400Z'


class RecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.market=historical(ROOT/'evidence/operational/CFB_MARKET_MONITOR_STATE.md','02df1f08c249bc859760e13de38b0c160f0759a8')
        cls.decision=historical(ROOT/'evidence/operational/CFB_DECISION_WAIT_LEDGER.md','5df8464b0b2372134939cf81d576e155d641113b')
        cls.lineage=(ROOT/'evidence/scheduler_qa/CFB_WEEK9_ORIGINAL_ANCESTRY_RECOVERY_20261025.json').read_text()
        cls.capture=(ROOT/'evidence/operational/CFB_CBS_WEEK9_TEXT_TABLE_CAPTURE_20261026T180323Z.md').read_text()
        prior=g.selected_block(cls.decision,w.DECISION_TAG,g.WEEKLY_DECISION_SCHEMAS,g.clock(AT))
        cls.rows=[{k:v for k,v in r.items() if k not in ('state_recorded_at_utc','state_evidence')} for r in prior['rows']]
        for r in cls.rows:r.update(state='REVIEW_OVERDUE',reason='SYNTHETIC QA ONLY unfinished material review; missed original deadline retained')
        cls.pm,cls.pd=cls.build()

    @classmethod
    def build(cls,**changes):
        args=dict(market=cls.market,decision=cls.decision,capture=cls.capture,lineage=cls.lineage,
                  cycle=CYCLE,as_of=AT,recovered_by=BY,decision_rows=cls.rows)
        args.update(changes)
        return w.compile(**args)

    def test_real_parent_overdue_rejection_reproduced(self):
        with self.assertRaisesRegex(ValueError,'overdue'):
            g.inputs(self.market,self.decision,self.lineage,AT,'WEEK9')

    def test_current_overdue_visible_not_pass_and_all_history_exact(self):
        self.assertTrue(self.pm.startswith(self.market));self.assertTrue(self.pd.startswith(self.decision))
        _,_,_,_,rows=g.inputs(self.pm,self.pd,self.lineage,AT,'WEEK9')
        self.assertEqual({r['state'] for r in rows.values()},{'REVIEW_OVERDUE'})
        self.assertEqual({r['reconciliation_utc'] for r in rows.values()},{'2026-10-26T18:00:00Z'})
        sheet=g.render(self.pm,self.pd,'execution fixture','scorecard fixture',self.lineage,AT,'WEEK9')
        self.assertEqual(sum('REVIEW OVERDUE — NOT A PASS OR RECOMMENDATION' in l for l in sheet.splitlines()),56)
        self.assertIn('56 REVIEW_OVERDUE',sheet)
        a=readiness.audit(self.pm,self.pd,self.lineage,AT,'WEEK9')
        self.assertEqual(a['open_games'],56);self.assertEqual(len(a['overdue_open_decision_game_ids']),56)
        self.assertEqual(a['evaluation_coverage']['counts']['NOT_CERTIFIED'],45)

    def test_original_deadline_cannot_extend_or_disappear(self):
        for value in ('2026-10-27T18:00:00Z',None):
            r=copy.deepcopy(self.rows);r[0]['reconciliation_utc']=value
            with self.assertRaises(ValueError):self.build(decision_rows=r)

    def test_no_relabel_back_to_inconclusive_with_new_deadline(self):
        r=copy.deepcopy(self.rows);r[0].update(state='INCONCLUSIVE',reconciliation_utc='2026-10-27T18:00:00Z')
        with self.assertRaises(ValueError):self.build(decision_rows=r)

    def test_overdue_cannot_claim_limits_cutoff_or_review(self):
        for key,value in [('acceptable_number',{}),('cutoff_authority','REVIEW_EVIDENCED'),('planning_cutoff_utc','2026-10-27T18:00:00Z'),('review_ref',{})]:
            r=copy.deepcopy(self.rows);r[0][key]=value
            with self.assertRaises(ValueError):self.build(decision_rows=r)

    def test_unknown_week_and_elapsed_reconstruction_rejected(self):
        row=g.inputs(self.pm,self.pd,self.lineage,AT,'WEEK9')[4][self.rows[0]['game_id']]
        source=g.inputs(self.pm,self.pd,self.lineage,AT,'WEEK9')[3][row['game_id']]
        with self.assertRaises(ValueError):validate(row,source,self.pd,AT,'WEEK8')
        source=copy.deepcopy(source);source['kickoff_utc']='2026-10-26T18:00:00Z'
        with self.assertRaises(ValueError):validate(row,source,self.pd,AT,'WEEK9')

    def test_recognition_cannot_be_backdated(self):
        with self.assertRaises(ValueError):self.build(as_of='2026-10-26T18:20:00Z',recovered_by='2026-10-26T18:19:00Z')

    def test_mixed_independent_pass_is_not_all_game_research_acceptance(self):
        rows=copy.deepcopy(self.rows);rows[0].update(state='PASS',reason='SYNTHETIC independently reviewed no-bet disposition')
        pm,pd=self.build(decision_rows=rows)
        a=readiness.audit(pm,pd,self.lineage,AT,'WEEK9')
        self.assertEqual(a['preserved_pass'],1);self.assertEqual(a['open_games'],55)
        self.assertEqual(a['evaluation_coverage']['counts']['NOT_CERTIFIED'],45)

    def conditional_fixture(self):
        # Reuse the established synthetic three-operator fixture, never an
        # actual football opinion, source qualification or wager.
        from test_cfb_conditional_recommendation_profile import ConditionalTests
        import cfb_conditional_recommendation_profile as profile
        ConditionalTests.setUpClass();fixture=ConditionalTests();fixture.setUp()
        review=copy.deepcopy(fixture.review);rows=copy.deepcopy(self.rows);target=rows[0]
        review.update(game_id=target['game_id'],original_lineage_blob=w.WEEK9_LINEAGE_SHA,
                      recorded_at_utc='2026-10-26T18:24:15Z',reconciliation_utc='2026-10-27T17:00:00Z',
                      planning_cutoff_utc='2026-10-27T20:00:00Z',
                      execution_window={'start_utc':'2026-10-26T18:25:00Z','end_utc':'2026-10-27T20:00:00Z'})
        ref=review['market_reference'];ref.update(game_id=target['game_id'],kickoff_utc='2026-10-27T23:00:00Z',
              kickoff_source_url='https://example.org/SYNTHETIC-QUALIFIED-KICKOFF',
              collection_start='2026-10-26T18:24:00Z',collection_end='2026-10-26T18:24:10Z')
        for q in ref['quotes']:q.update(game_id=target['game_id'],retrieved_at='2026-10-26T18:24:05Z',offer_updated_at='2026-10-26T18:24:00Z')
        for s in review['material_sources']:s['retrieved_at']='2026-10-26T18:24:00Z'
        target.update(state='CONDITIONAL',reason=review['rationale'],cutoff_authority='REVIEW_EVIDENCED',review_ref=fixture.target['review_ref'])
        for key in ('acceptable_number','reconciliation_utc','planning_cutoff_utc','execution_window'):target[key]=copy.deepcopy(review[key])
        return rows,review,profile

    def test_qualified_week9_conditional_and_overdue_coexist(self):
        rows,review,profile=self.conditional_fixture()
        with patch.object(profile,'load_review',return_value=(json.dumps(review),'2026-10-26T18:24:20Z')):
            pm,pd=self.build(decision_rows=rows)
            sheet=g.render(pm,pd,'execution','scorecard',self.lineage,AT,'WEEK9')
            self.assertIn('1 CONDITIONAL',sheet);self.assertIn('55 REVIEW_OVERDUE',sheet)
            model=json.loads(self.lineage)['rows'][0]
            model['first_frozen_status']='EXCLUDED'
            inputs=g.inputs(pm,pd,self.lineage,AT,'WEEK9')
            with self.assertRaises(ValueError):profile.validate(inputs[4][rows[0]['game_id']],inputs[3][rows[0]['game_id']],model,AT,w.WEEK9_LINEAGE_SHA)
            with self.assertRaises(ValueError):profile.validate(inputs[4][rows[0]['game_id']],inputs[3][rows[0]['game_id']],model,AT,'0'*40)

    def test_closed_week9_conditional_retains_exact_origin(self):
        rows,review,profile=self.conditional_fixture()
        with patch.object(profile,'load_review',return_value=(json.dumps(review),'2026-10-26T18:24:20Z')):
            pm,pd=self.build(decision_rows=rows)
            old=g.inputs(pm,pd,self.lineage,AT,'WEEK9')[4]
            rows=[{k:v for k,v in r.items() if k not in ('state_recorded_at_utc','state_evidence')} for r in old.values()]
            pm2,pd2=self.build(market=pm,decision=pd,decision_rows=rows,
                              cycle='CFB_MARKET_MONITOR_20261027T202400Z',as_of='2026-10-27T20:25:00Z',recovered_by='2026-10-27T20:24:00Z')
            current=g.inputs(pm2,pd2,self.lineage,'2026-10-27T20:25:00Z','WEEK9')[4]
            self.assertEqual(current[rows[0]['game_id']],old[rows[0]['game_id']])
            sheet=g.render(pm2,pd2,'execution','scorecard',self.lineage,'2026-10-27T20:25:00Z','WEEK9')
            self.assertIn('HISTORICAL CONDITIONAL — WINDOW CLOSED',sheet)


if __name__=='__main__':unittest.main()
