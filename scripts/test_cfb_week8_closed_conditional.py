"""Authentic failed Evening inputs; proposals only, no replayed production writes."""
import copy
import unittest
from pathlib import Path
import cfb_neutral_publication_gate as gate
import cfb_week8_publication as week
import cfb_hot_sheet_readiness as readiness
from cfb_neutral_publication_legacy_replay import historical
from cfb_neutral_publication_legacy_replay import packet

ROOT=Path(__file__).resolve().parents[1]
AT='2026-10-24T01:33:00Z'
BY='2026-10-24T01:32:12Z'
CYCLE='CFB_EVENING_AVAILABILITY_20261024T012553Z'

class ClosedConditionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.market=historical(ROOT/'evidence/operational/CFB_MARKET_MONITOR_STATE.md','457b6db6fde5bf8c7706f55598d7b274bb80d9e9')
        cls.decision=historical(ROOT/'evidence/operational/CFB_DECISION_WAIT_LEDGER.md','fb4e7a08c38c68490a43a6fef3c7811ed7665b23')
        cls.lineage=(ROOT/'evidence/scheduler_qa/CFB_WEEK8_ORIGINAL_ANCESTRY_RECOVERY_20261020.json').read_text()
        cls.capture=(ROOT/'evidence/operational/CFB_CBS_WEEK8_TEXT_TABLE_CAPTURE_20261024T013212Z.md').read_text()
        cls.old=gate.inputs(cls.market,cls.decision,cls.lineage,'2026-10-23T18:18:00Z','WEEK8')
        cls.rows=[{k:v for k,v in r.items() if k not in ('state_evidence','state_recorded_at_utc')} for r in cls.old[4].values()]
        cls.proposals=cls.build()
    @classmethod
    def build(cls,rows=None):
        return week.compile(cls.market,cls.decision,cls.capture,cls.lineage,CYCLE,AT,BY,cls.rows if rows is None else rows)
    def test_authentic_failed_case_advances_and_preserves_all_decisions(self):
        m,d= self.proposals
        result=gate.inputs(m,d,self.lineage,AT,'WEEK8')
        self.assertEqual(result[4],self.old[4])
        self.assertEqual(len(result[3]),56)
        self.assertTrue(m.startswith(self.market));self.assertTrue(d.startswith(self.decision))
        air=result[3]['401864525']
        self.assertIsNone(air['current'])
        self.assertEqual(air['retained'],self.old[3]['401864525']['current'])
    def test_closed_display_never_presents_new_opportunity_or_no_execution_claim(self):
        sheet=gate.render(*self.proposals,'existing executions','scorecard',self.lineage,AT,'WEEK8')
        self.assertEqual(sheet.count('| HISTORICAL CONDITIONAL — WINDOW CLOSED |'),5)
        self.assertIn('**Primary section:** NONE',sheet)
        self.assertNotIn('Conditional recommendations are shown',sheet)
        air=next(l for l in sheet.splitlines() if l.startswith('| ') and 'Air Force @ Wyoming' in l)
        self.assertIn('execution tracked separately',air)
        self.assertNotIn('historical PASS; no execution',air)
        self.assertEqual(sum(l.startswith('| ') and ' @ ' in l for l in sheet.splitlines()),56)
        gate.audit(sheet,*self.proposals,'existing executions','scorecard',self.lineage,AT,'WEEK8')
    def test_readiness_has_no_reopened_window(self):
        r=readiness.audit(*self.proposals,self.lineage,AT,'WEEK8')
        rows=[x for x in r['rows'] if x['state']=='CONDITIONAL']
        self.assertEqual(len(rows),5)
        self.assertTrue(all(x['disposition']=='HISTORICAL_CONDITIONAL_WINDOW_CLOSED' and not x['review_window']['review_required'] for x in rows))
    def test_changed_expired_review_rejected(self):
        for field,value in [('reason','Rewritten later'),('planning_cutoff_utc','2026-10-24T02:00:00Z'),('acceptable_number',None)]:
            rows=copy.deepcopy(self.rows)
            row=next(r for r in rows if r['game_id']=='401864525');row[field]=value
            with self.subTest(field=field),self.assertRaises(ValueError):self.build(rows)
    def test_postkickoff_pass_conversion_still_rejected(self):
        rows=copy.deepcopy(self.rows);r=next(x for x in rows if x['game_id']=='401864525')
        r.update(state='PASS',reason='Late fabricated pass',review_ref=None,acceptable_number=None,execution_window=None,cutoff_authority='UNVERIFIED')
        with self.assertRaisesRegex(ValueError,'postkickoff'):self.build(rows)
    def test_backdated_or_relabelled_origin_rejected(self):
        m,d=self.proposals
        p=gate.selected_block(d,week.DECISION_TAG,gate.WEEKLY_DECISION_SCHEMAS,gate.clock(AT))
        for field,value in [('state_evidence',CYCLE),('state_recorded_at_utc',AT),('reason','Later revision')]:
            changed=copy.deepcopy(p);r=next(x for x in changed['rows'] if x['game_id']=='401864525');r[field]=value
            prefix=d[:d.rfind('```'+week.DECISION_TAG)]
            with self.subTest(field=field),self.assertRaises(ValueError):
                gate.inputs(m,prefix+packet(changed,week.DECISION_TAG).lstrip('\n'),self.lineage,AT,'WEEK8')
    def test_missing_origin_and_changed_source_binding_rejected(self):
        m,d=self.proposals
        p=gate.selected_block(m,week.MARKET_TAG,gate.WEEKLY_MARKET_SCHEMA,gate.clock(AT))
        r=next(x for x in p['rows'] if x['game_id']=='401864525')
        r['kickoff_source_url']='https://example.org/changed'
        prefix=m[:m.rfind('```'+week.MARKET_TAG)]
        with self.assertRaisesRegex(ValueError,'kickoff binding changed'):
            gate.inputs(prefix+packet(p,week.MARKET_TAG).lstrip('\n'),d,self.lineage,AT,'WEEK8')
        row=copy.deepcopy(self.old[4]['401864525']);row['state_evidence']='CFB_MARKET_MONITOR_20261023T180000Z'
        with self.assertRaisesRegex(ValueError,'origin missing'):
            gate.conditional_boundary(row,{'cycle_id':CYCLE,'as_of_utc':AT},m,d,'WEEK8')
    def test_week7_live_validation_route_unchanged(self):
        row=copy.deepcopy(self.old[4]['401864525'])
        self.assertEqual(gate.conditional_boundary(row,{'as_of_utc':AT},'','', 'WEEK7'),(AT,None))

if __name__=='__main__':unittest.main()
