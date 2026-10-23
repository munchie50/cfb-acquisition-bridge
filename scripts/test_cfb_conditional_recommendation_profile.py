"""Synthetic richer decisions over authentic saved source; never actual picks."""
import copy
import json
import subprocess
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch
import cfb_neutral_publication_gate as gate
import cfb_neutral_weekly_reconciliation as compiler
import cfb_conditional_recommendation_profile as profile
from cfb_neutral_publication_legacy_replay import packet, historical

AT='2026-10-17T00:06:00Z'
CYCLE='CFB_MARKET_MONITOR_20261017T000500Z'


class ConditionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root=Path('evidence/operational')
        cls.market=historical(root/'CFB_MARKET_MONITOR_STATE.md','f96df574ef69a6d1e21139c9c721bd1804295501')
        cls.decision=historical(root/'CFB_DECISION_WAIT_LEDGER.md','579ee3d16c76663428b3a00e49d4861a8ed512f1')
        cls.lineage=(root/'CFB_WEEK7_ORIGINAL_FIRST_FROZEN_LINEAGE_2026-10-11.json').read_text()
        cls.capture=(root/'CFB_CBS_FULL_BOARD_TABLES_20261016T180051Z.md').read_text()
        cls.execution=historical(root/'CFB_EXECUTION_LEDGER.md','75caee4052e02ea7d2453d1d37fd3866e13ecc07')
        cls.scorecard=historical(root/'CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md','4380a04b9ce285288861e910fc7b754f977529d1')

    def setUp(self):
        # Hypothetical clocks and qualifications below are TEST FIXTURES ONLY.
        self.m=copy.deepcopy(compiler.latest(self.market,gate.MARKET_TAG))
        self.d=copy.deepcopy(compiler.latest(self.decision,gate.DECISION_TAG))
        for p in (self.m,self.d):p.update(cycle_id=CYCLE,as_of_utc=AT)
        self.d['schema']=gate.CONDITIONAL_DECISION_SCHEMA
        for r in self.d['rows']:
            r['review_ref']=None
            if r['state']!='PASS':r.update(state_recorded_at_utc=AT,state_evidence=CYCLE)
        for r in self.m['rows']:
            if gate.clock(r['kickoff_utc'])<=gate.clock(AT):
                r.update(retained=r['current'] or r['retained'],current=None,current_availability='UNAVAILABLE')
        self.target=next(r for r in self.d['rows'] if r['state']=='INCONCLUSIVE')
        self.source=next(r for r in self.m['rows'] if r['game_id']==self.target['game_id'])
        self.source['kickoff_status']='QUALIFIED'
        ref={'game_id':self.target['game_id'],'market':'SPREAD','selection':'away','period':'PREGAME_FULL_GAME',
             'kickoff_utc':self.source['kickoff_utc'],'kickoff_source_url':self.source['kickoff_source_url'],
             'collection_start':'2026-10-17T00:04:00Z','collection_end':'2026-10-17T00:04:30Z','quotes':[]}
        for i in range(3):
            ref['quotes'].append(dict(game_id=ref['game_id'],market='SPREAD',selection='away',period='PREGAME_FULL_GAME',
                book='SYNTHETIC_BOOK_'+str(i),operator='SYNTHETIC_OPERATOR_'+str(i),
                operator_evidence_url='https://example.org/operator/'+str(i),source_url='https://example.org/quote/'+str(i),
                retrieved_at='2026-10-17T00:04:20Z',offer_updated_at='2026-10-17T00:04:10Z',line=14+i,price=-110))
        self.review=dict(schema=profile.REVIEW_SCHEMA,game_id=self.target['game_id'],state='CONDITIONAL',
            recorded_at_utc='2026-10-17T00:04:40Z',original_lineage_blob=gate.LINEAGE_SHA,
            maturity='CONTROLLED_BETA_RECOMMENDATION',market='SPREAD',selection='away',
            rationale='SYNTHETIC QA REVIEW ONLY — not an actual recommendation',
            model_review='Synthetic independently reviewed original frozen model basis',
            material_sources=[dict(url='https://example.org/team-report',retrieved_at='2026-10-17T00:04:00Z',finding='Synthetic material availability review')],
            uncertainty='Synthetic descriptive uncertainty, no calibrated EV',decision_rule='Synthetic governed rule evidence, no production promotion',
            source_qualification='Synthetic independent operator/source qualification, not actual research',market_reference=ref,
            acceptable_number=dict(market='SPREAD',selection='away',line=14,minimum_price=-110,direction='AT_LEAST'),
            reconciliation_utc='2026-10-17T00:20:00Z',planning_cutoff_utc='2026-10-17T14:00:00Z',
            cutoff_basis='Synthetic preserved practical cutoff authority',
            execution_window=dict(start_utc='2026-10-17T00:05:00Z',end_utc='2026-10-17T14:00:00Z'))
        self.target.update(state='CONDITIONAL',reason=self.review['rationale'],cutoff_authority='REVIEW_EVIDENCED',
            review_ref=dict(path='evidence/operational/recommendation_reviews/SYNTHETIC_QA_ONLY.json',commit='a'*40,blob='b'*40))
        for k in ('acceptable_number','reconciliation_utc','planning_cutoff_utc','execution_window'):
            self.target[k]=copy.deepcopy(self.review[k])

    def args(self):
        return [self.market+packet(self.m,gate.MARKET_TAG),self.decision+packet(self.d,gate.DECISION_TAG),
                self.execution,self.scorecard,self.lineage,AT]

    def mocked(self):
        return patch.object(profile,'load_review',return_value=(json.dumps(self.review),'2026-10-17T00:04:50Z'))

    def reject(self):
        with self.mocked(),self.assertRaises((ValueError,TypeError,KeyError)):gate.render(*self.args())

    def test_original_v2_rejection_and_new_v3_render(self):
        content=subprocess.check_output(['git','show','855844e49f2fa69d839d3a4a86f367ebf20cb40a:scripts/cfb_neutral_publication_gate.py'],text=True)
        old=types.ModuleType('old_neutral_gate');exec(content,old.__dict__)
        args=self.args()
        with self.assertRaisesRegex(ValueError,'unknown schema'):old.render(*args)
        with self.mocked():
            sheet=gate.render(*args);result=gate.audit(sheet,*args)
        self.assertEqual(result['games'],62)
        self.assertEqual(sheet.count('| CONDITIONAL |'),1)
        self.assertIn('51 INCONCLUSIVE; 10 PASS; 1 CONDITIONAL',sheet)
        self.assertIn('minimum price -110',sheet);self.assertIn('VENUE_CONFIRMATION_PENDING',sheet)
        self.assertIn('Engine Prediction (Frozen)',sheet)
        self.assertIn('source truth independently reviewed, not certified by renderer',sheet)

    def test_v2_cannot_smuggle_conditional_state(self):
        self.d['schema']=gate.WEEKLY_DECISION_SCHEMA
        for r in self.d['rows']:r.pop('review_ref')
        self.reject()

    def reconsideration_fixture(self):
        self.retrieval_only_review()
        prior=copy.deepcopy(self.target)
        prior.update(state='PASS',reason='Earlier evidence-limited PASS',review_ref=None,
            state_recorded_at_utc='2026-10-17T00:01:00Z',state_evidence='EARLIER_TEST_CYCLE',
            acceptable_number=None,execution_window=None,cutoff_authority='UNVERIFIED')
        self.review['schema']='CFB_PROSPECTIVE_RECONSIDERATION_REVIEW_V3'
        self.review['reconsideration']={'prior_row_blob':gate.blob(json.dumps(prior,sort_keys=True,separators=(',',':'))),
            'reason':'New identified benchmark and material review complete the earlier missing evaluation'}
        return prior

    def test_explicit_prospective_reconsideration_preserves_prior_pass(self):
        prior=self.reconsideration_fixture();unchanged=copy.deepcopy(prior)
        with self.mocked():profile.reconsideration(self.target,prior,AT)
        self.assertEqual(prior,unchanged)

    def test_reconsideration_requires_exact_prior_row_binding(self):
        prior=self.reconsideration_fixture();prior['reason']='Different earlier decision'
        with self.mocked(),self.assertRaises(ValueError):profile.reconsideration(self.target,prior,AT)

    def test_ordinary_review_still_cannot_reopen_pass(self):
        prior=self.reconsideration_fixture();self.review['schema']=profile.RETRIEVAL_REVIEW_SCHEMA
        with self.mocked(),self.assertRaises(ValueError):profile.reconsideration(self.target,prior,AT)

    def test_reconsideration_cannot_reuse_old_source_or_erase_limits(self):
        prior=self.reconsideration_fixture();prior['state_recorded_at_utc']='2026-10-17T00:04:10Z'
        self.review['reconsideration']['prior_row_blob']=gate.blob(json.dumps(prior,sort_keys=True,separators=(',',':')))
        with self.mocked(),self.assertRaises(ValueError):profile.reconsideration(self.target,prior,AT)
        prior=self.reconsideration_fixture();prior['acceptable_number']={'existing':'limit'}
        self.review['reconsideration']['prior_row_blob']=gate.blob(json.dumps(prior,sort_keys=True,separators=(',',':')))
        with self.mocked(),self.assertRaises(ValueError):profile.reconsideration(self.target,prior,AT)

    def test_reconsideration_cannot_reopen_expired_cutoff(self):
        prior=self.reconsideration_fixture();prior['planning_cutoff_utc']='2026-10-17T00:05:00Z'
        self.review['reconsideration']['prior_row_blob']=gate.blob(json.dumps(prior,sort_keys=True,separators=(',',':')))
        with self.mocked(),self.assertRaises(ValueError):profile.reconsideration(self.target,prior,AT)

    def test_reconsideration_full_render_still_requires_qualified_review(self):
        self.reconsideration_fixture()
        with self.mocked():gate.render(*self.args())

    def test_history_accepts_only_bound_reconsideration_and_keeps_old_packet(self):
        prior=self.reconsideration_fixture()
        first=copy.deepcopy(self.d);first.update(cycle_id='CFB_MARKET_MONITOR_20261017T000300Z',as_of_utc='2026-10-17T00:03:00Z')
        first['rows']=[prior if r['game_id']==prior['game_id'] else r for r in first['rows']]
        original=packet(first,gate.DECISION_TAG)
        with self.mocked():result=gate.selected_block(original+packet(self.d,gate.DECISION_TAG),gate.DECISION_TAG,gate.WEEKLY_DECISION_SCHEMAS,gate.clock(AT))
        self.assertEqual(next(r for r in result['rows'] if r['game_id']==prior['game_id'])['state'],'CONDITIONAL')
        self.assertEqual(first['rows'][next(i for i,r in enumerate(first['rows']) if r['game_id']==prior['game_id'])],prior)
        self.review['reconsideration']['prior_row_blob']='0'*40
        with self.mocked(),self.assertRaisesRegex(ValueError,'binding mismatch'):
            gate.selected_block(original+packet(self.d,gate.DECISION_TAG),gate.DECISION_TAG,gate.WEEKLY_DECISION_SCHEMAS,gate.clock(AT))

    def test_intervening_pass_cannot_reset_original_conditional_limits(self):
        prior=self.reconsideration_fixture()
        first=copy.deepcopy(self.d);first.update(cycle_id='CFB_MARKET_MONITOR_20261017T000000Z',as_of_utc='2026-10-17T00:00:00Z')
        middle=copy.deepcopy(first);middle.update(cycle_id='CFB_MARKET_MONITOR_20261017T000300Z',as_of_utc='2026-10-17T00:03:00Z')
        middle['rows']=[prior if r['game_id']==prior['game_id'] else r for r in middle['rows']]
        self.target['acceptable_number']['line']=15
        content=packet(first,gate.DECISION_TAG)+packet(middle,gate.DECISION_TAG)+packet(self.d,gate.DECISION_TAG)
        with self.mocked(),self.assertRaisesRegex(ValueError,'historical original conditional limits'):
            gate.selected_block(content,gate.DECISION_TAG,gate.WEEKLY_DECISION_SCHEMAS,gate.clock(AT))

    def retrieval_only_review(self):
        self.review['schema']='CFB_PROSPECTIVE_CONDITIONAL_REVIEW_V2'
        ref=self.review['market_reference']
        ref['clock_semantics']='RESPONSE_RECOVERED_BY'
        ref['quotes']=ref['quotes'][:1]
        ref['quotes'][0].update(book='DraftKings',operator='DraftKings',offer_updated_at=None,
            source_url='https://www.espn.com/college-football/odds',
            operator_evidence_url='https://sportsbook.draftkings.com/gateway?s=example')

    def test_identified_retrieval_only_beta_review_can_publish_without_consensus(self):
        self.retrieval_only_review()
        with self.mocked():
            sheet=gate.render(*self.args());gate.audit(sheet,*self.args())
        self.assertIn('IDENTIFIED_RETRIEVAL_ONLY_BENCHMARK',sheet)
        self.assertIn('CONSENSUS_UNAVAILABLE',sheet)
        self.assertIn('offer-update UNKNOWN',sheet)
        self.assertIn('VENUE_CONFIRMATION_PENDING',sheet)
        self.assertNotIn('3 operators',sheet)

    def aggregate_table_review(self):
        # Hypothetical protocol fixture, never an actual offer or recommendation.
        self.retrieval_only_review()
        self.review['schema']='CFB_PROSPECTIVE_CONDITIONAL_REVIEW_V4'
        ref=self.review['market_reference']
        ref['source_kind']='DRAFTKINGS_PUBLIC_AGGREGATE_TABLE'
        ref['quotes'][0].update(
            source_url='https://dknetwork.draftkings.com/draftkings-sportsbook-betting-splits/?itm_content=NCAA+Football&tb_edate=n30days&tb_eg=87637&tb_page=3',
            operator_evidence_url='https://sportsbook.draftkings.com/event/12345?dkinternal_referrer_source=dknetwork&outcomes=fixture_away')

    def test_versioned_aggregate_benchmark_renders_its_nonvenue_scope(self):
        self.aggregate_table_review()
        with self.mocked():
            sheet=gate.render(*self.args());gate.audit(sheet,*self.args())
        self.assertIn('DRAFTKINGS_PUBLIC_AGGREGATE_TABLE',sheet)
        self.assertIn('ALL_JURISDICTIONS_NOT_A_VENUE_OFFER',sheet)
        self.assertIn('CONSENSUS_UNAVAILABLE',sheet)
        self.assertIn('offer-update UNKNOWN',sheet)
        self.assertIn('VENUE_CONFIRMATION_PENDING',sheet)

    def test_aggregate_host_is_not_silently_added_to_prior_review_versions(self):
        for version in ('CFB_PROSPECTIVE_CONDITIONAL_REVIEW_V2','CFB_PROSPECTIVE_RECONSIDERATION_REVIEW_V3'):
            self.setUp();self.aggregate_table_review()
            self.review['schema']=version
            self.review['market_reference'].pop('source_kind')
            with self.assertRaisesRegex(ValueError,'source/operator evidence mismatch'):
                profile.market_reference(self.review,AT)

    def test_aggregate_source_kind_is_required_and_not_a_venue_claim(self):
        for value in (None,'EXECUTION_CONFIRMED','DRAFTKINGS_LIVE_VENUE'):
            self.setUp();self.aggregate_table_review()
            if value is None:self.review['market_reference'].pop('source_kind')
            else:self.review['market_reference']['source_kind']=value
            self.reject()

    def test_aggregate_source_does_not_accept_other_pages_or_sports(self):
        for url in ('https://dknetwork.draftkings.com/other/',
                    'https://dknetwork.draftkings.com.evil.test/draftkings-sportsbook-betting-splits/?itm_content=NCAA+Football&tb_eg=87637&tb_page=3',
                    'http://dknetwork.draftkings.com/draftkings-sportsbook-betting-splits/?itm_content=NCAA+Football&tb_eg=87637&tb_page=3',
                    'https://dknetwork.draftkings.com/draftkings-sportsbook-betting-splits/?itm_content=NFL&tb_eg=87637&tb_page=3',
                    'https://dknetwork.draftkings.com/draftkings-sportsbook-betting-splits/?itm_content=NCAA+Football&tb_eg=87637&tb_page=3&tb_page=4'):
            self.setUp();self.aggregate_table_review()
            self.review['market_reference']['quotes'][0]['source_url']=url
            self.reject()

    def test_aggregate_requires_observed_selection_link_not_generic_operator_home(self):
        for url in ('https://sportsbook.draftkings.com/',
                    'https://sportsbook.draftkings.com/event/12345',
                    'https://sportsbook.draftkings.com/event/12345?outcomes=fixture',
                    'https://example.org/event/12345?dkinternal_referrer_source=dknetwork&outcomes=fixture'):
            self.setUp();self.aggregate_table_review()
            self.review['market_reference']['quotes'][0]['operator_evidence_url']=url
            self.reject()

    def test_aggregate_rejects_duplicate_blank_query_values(self):
        for field, suffix in (('source_url','&tb_page='),
                              ('operator_evidence_url','&outcomes='),
                              ('operator_evidence_url','&dkinternal_referrer_source=')):
            self.setUp();self.aggregate_table_review()
            self.review['market_reference']['quotes'][0][field]+=suffix
            self.reject()

    def test_aggregate_keeps_identity_maturity_and_clock_rejections(self):
        self.aggregate_table_review();self.review['market_reference']['quotes'][0]['operator']='FanDuel';self.reject()
        self.setUp();self.aggregate_table_review();self.review['maturity']='PRODUCTION_QUALIFIED';self.reject()
        self.setUp();self.aggregate_table_review();self.review['market_reference']['quotes'][0]['offer_updated_at']='2026-10-16T00:00:00Z';self.reject()
        self.setUp();self.aggregate_table_review();self.review['market_reference']['quotes'][0]['selection']='home';self.reject()
        self.setUp();self.aggregate_table_review();self.review['market_reference']['quotes']*=2;self.reject()

    def test_aggregate_still_requires_material_review_limits_and_future_kickoff(self):
        self.aggregate_table_review();self.review['material_sources']=[];self.reject()
        self.setUp();self.aggregate_table_review();self.review['acceptable_number']['minimum_price']=None;self.reject()
        self.setUp();self.aggregate_table_review();self.source['kickoff_status']='RETAINED_UNVERIFIED';self.reject()

    def test_aggregate_review_cannot_reopen_pass_without_existing_reconsideration(self):
        prior=self.reconsideration_fixture();self.aggregate_table_review()
        self.review.pop('reconsideration',None)
        with self.mocked(),self.assertRaisesRegex(ValueError,'explicit reconsideration review'):
            profile.reconsideration(self.target,prior,AT)

    def test_retrieval_only_profile_cannot_accept_unidentified_or_wrong_source(self):
        for change in ({'operator':'UNIDENTIFIED'},{'book':'Caesars','operator':'Caesars'},
                       {'source_url':'https://example.org/not-the-identified-book'},
                       {'operator_evidence_url':'https://example.org/unrelated'}):
            self.retrieval_only_review();self.review['market_reference']['quotes'][0].update(change);self.reject()

    def test_retrieval_only_profile_requires_one_quote_and_clock_semantics(self):
        self.retrieval_only_review();self.review['market_reference'].pop('clock_semantics');self.reject()
        self.retrieval_only_review();self.review['market_reference']['clock_semantics']='BOOK_UPDATE_VERIFIED';self.reject()
        self.retrieval_only_review();self.review['market_reference']['quotes']*=2;self.reject()

    def test_retrieval_only_profile_preserves_old_consensus_rejections(self):
        self.review['market_reference']['quotes'][0]['offer_updated_at']=None;self.reject()
        self.retrieval_only_review();self.review['maturity']='PRODUCTION_QUALIFIED';self.reject()

    def test_retrieval_only_profile_still_requires_material_limits_and_future_kickoff(self):
        self.retrieval_only_review();self.review['material_sources']=[];self.reject()
        self.setUp();self.retrieval_only_review();self.review['acceptable_number']['minimum_price']=None;self.reject()
        self.setUp();self.retrieval_only_review();self.source['kickoff_status']='RETAINED_UNVERIFIED';self.reject()

    def test_retrieval_only_profile_cannot_relabel_known_stale_update(self):
        self.retrieval_only_review();self.review['market_reference']['quotes'][0]['offer_updated_at']='2026-10-16T00:00:00Z';self.reject()

    def test_missing_review_cannot_publish(self):
        with patch.object(profile,'load_review',side_effect=ValueError('missing actual review')),self.assertRaises(ValueError):gate.render(*self.args())

    def test_future_review_or_commit_rejected(self):
        self.review['recorded_at_utc']='2026-10-17T00:07:00Z';self.reject()
        self.review['recorded_at_utc']='2026-10-17T00:04:40Z'
        with patch.object(profile,'load_review',return_value=(json.dumps(self.review),'2026-10-17T00:07:00Z')),self.assertRaises(ValueError):gate.render(*self.args())

    def test_missing_source_or_unknown_clocks_rejected(self):
        self.review['market_reference']['quotes'][0]['offer_updated_at']=None;self.reject()
        self.review['market_reference']['quotes']=self.review['market_reference']['quotes'][:2];self.reject()

    def test_wrong_model_or_game_rejected(self):
        self.review['original_lineage_blob']='0'*40;self.reject()
        self.review['original_lineage_blob']=gate.LINEAGE_SHA;self.review['game_id']='UNKNOWN';self.reject()

    def test_wrong_selection_or_market_rejected(self):
        self.review['market_reference']['selection']='home';self.reject()

    def test_missing_material_rule_or_qualified_schedule_rejected(self):
        original=copy.deepcopy(self.review)
        for key,value in (('material_sources',[]),('decision_rule','')):
            self.review=copy.deepcopy(original);self.review[key]=value;self.reject()
        self.review=original;self.source['kickoff_status']='RETAINED_UNVERIFIED';self.reject()

    def test_price_line_direction_and_cutoff_binding_rejected(self):
        for field,value in (('minimum_price',None),('direction','AT_MOST'),('line',None)):
            original=copy.deepcopy(self.review['acceptable_number']);self.review['acceptable_number'][field]=value;self.reject();self.review['acceptable_number']=original
        self.target['planning_cutoff_utc']='2026-10-17T14:01:00Z';self.reject()

    def test_future_material_and_late_reference_rejected(self):
        self.review['material_sources'][0]['retrieved_at']='2026-10-17T00:05:00Z';self.reject()
        self.review['material_sources'][0]['retrieved_at']='2026-10-17T00:04:00Z'
        self.review['market_reference']['collection_end']='2026-10-17T00:05:00Z';self.reject()

    def test_original_exclusion_cannot_be_substituted(self):
        model=next(r for r in json.loads(self.lineage)['rows'] if r['first_frozen_status']!='PREDICTION')
        source=next(r for r in self.m['rows'] if r['game_id']==model['game_id'])
        row=copy.deepcopy(self.target);row['game_id']=model['game_id'];self.review['game_id']=model['game_id']
        with self.mocked(),self.assertRaisesRegex(ValueError,'exclusion'):
            profile.validate(row,source,model,AT)

    def test_unearned_production_maturity_and_added_ev_rejected(self):
        self.review['maturity']='PRODUCTION_QUALIFIED';self.reject()
        self.review['maturity']='CONTROLLED_BETA_RECOMMENDATION';self.review['ev']=0.2;self.reject()

    def test_production_review_resolver_rejects_bad_or_missing_ancestry(self):
        for ref in ({'path':'secrets.json','commit':'a'*40,'blob':'b'*40},
                    {'path':'evidence/operational/recommendation_reviews/MISSING.json','commit':'0'*40,'blob':'0'*40}):
            with self.assertRaises(ValueError):profile.load_review(ref)

    def test_reviewed_limits_and_closed_pass_cannot_be_reopened(self):
        a=self.args();later_m=copy.deepcopy(self.m);later_d=copy.deepcopy(self.d)
        for p in (later_m,later_d):p.update(cycle_id='CFB_MARKET_MONITOR_20261017T000700Z',as_of_utc='2026-10-17T00:08:00Z')
        target=next(r for r in later_d['rows'] if r['game_id']==self.target['game_id']);target['acceptable_number']['line']=13
        with self.mocked(),self.assertRaisesRegex(ValueError,'limits cannot change'):
            gate.render(a[0]+packet(later_m,gate.MARKET_TAG),a[1]+packet(later_d,gate.DECISION_TAG),*a[2:-1],'2026-10-17T00:08:00Z')
        first=next(r for r in self.d['rows'] if r['state']=='PASS');first['state']='CONDITIONAL';self.reject()

    def test_conditional_cannot_downgrade_to_inconclusive_or_v2(self):
        a=self.args();lm=copy.deepcopy(self.m);ld=copy.deepcopy(self.d)
        for p in (lm,ld):p.update(cycle_id='CFB_MARKET_MONITOR_20261017T000700Z',as_of_utc='2026-10-17T00:08:00Z')
        next(r for r in ld['rows'] if r['game_id']==self.target['game_id'])['state']='INCONCLUSIVE'
        with self.mocked(),self.assertRaisesRegex(ValueError,'silently downgrade'):
            gate.inputs(a[0]+packet(lm,gate.MARKET_TAG),a[1]+packet(ld,gate.DECISION_TAG),self.lineage,'2026-10-17T00:08:00Z')
        ld['schema']=gate.WEEKLY_DECISION_SCHEMA
        next(r for r in ld['rows'] if r['game_id']==self.target['game_id'])['state']='CONDITIONAL'
        with self.mocked(),self.assertRaisesRegex(ValueError,'schema downgrade'):
            gate.inputs(a[0]+packet(lm,gate.MARKET_TAG),a[1]+packet(ld,gate.DECISION_TAG),self.lineage,'2026-10-17T00:08:00Z')

    def test_normal_compiler_and_replay_do_not_require_caesars(self):
        # Accepted qualified schedule persists only when a new source clock agrees.
        self.source['kickoff_utc']=self.source['kickoff_utc'].replace('Z','+00:00')
        self.review['market_reference']['kickoff_utc']=self.source['kickoff_utc']
        base_m=copy.deepcopy(self.m);base_d=copy.deepcopy(self.d)
        for p in (base_m,base_d):p.update(cycle_id='CFB_MARKET_MONITOR_20261017T000100Z',as_of_utc='2026-10-17T00:02:00Z')
        base_d['schema']=gate.WEEKLY_DECISION_SCHEMA
        for r in base_d['rows']:
            r.pop('review_ref')
            if r['state']!='PASS':
                old=next(x for x in compiler.latest(self.decision,gate.DECISION_TAG)['rows'] if x['game_id']==r['game_id'])
                r.update({k:v for k,v in old.items() if k not in ('state_recorded_at_utc','state_evidence')})
                r.update(state_recorded_at_utc='2026-10-17T00:02:00Z',state_evidence=base_d['cycle_id'])
        rows=[{k:v for k,v in r.items() if k not in ('state_recorded_at_utc','state_evidence')} for r in self.d['rows']]
        with self.mocked():
            m,d=compiler.advance(self.market+packet(base_m,gate.MARKET_TAG),self.decision+packet(base_d,gate.DECISION_TAG),
                self.capture,self.lineage,CYCLE,AT,'2026-10-17T00:04:30Z',rows)
            sheet=gate.render(m,d,self.execution,self.scorecard,self.lineage,AT)
        self.assertIn('1 CONDITIONAL',sheet)
        self.assertEqual(compiler.latest(d,gate.DECISION_TAG)['schema'],gate.CONDITIONAL_DECISION_SCHEMA)

    def test_actual_immutable_resolver_in_isolated_synthetic_git_repo(self):
        import os
        with tempfile.TemporaryDirectory(prefix='cfb-synthetic-review-') as temp:
            root=Path(temp);path=root/self.target['review_ref']['path'];path.parent.mkdir(parents=True)
            path.write_text(json.dumps(self.review))
            def git(*args,env=None):return subprocess.check_output(['git','-C',str(root),*args],text=True,stderr=subprocess.DEVNULL,env=env).strip()
            git('init','-q');git('add','evidence')
            env=dict(os.environ,GIT_AUTHOR_DATE='2026-10-17T00:04:50Z',GIT_COMMITTER_DATE='2026-10-17T00:04:50Z')
            git('-c','user.name=Synthetic CFB QA','-c','user.email=synthetic@example.org','commit','-qm','Synthetic review fixture only',env=env)
            self.target['review_ref'].update(commit=git('rev-parse','HEAD'),blob=gate.blob(path.read_text()))
            with patch.object(profile,'ROOT',root):
                sheet=gate.render(*self.args())
                self.assertIn('1 CONDITIONAL',sheet)
                self.target['review_ref']['blob']='0'*40
                with self.assertRaisesRegex(ValueError,'blob/path binding'):gate.render(*self.args())

    def test_historical_review_still_validated_after_later_pass(self):
        a=self.args();lm=copy.deepcopy(self.m);ld=copy.deepcopy(self.d)
        for p in (lm,ld):p.update(cycle_id='CFB_MARKET_MONITOR_20261017T000700Z',as_of_utc='2026-10-17T00:08:00Z')
        row=next(r for r in ld['rows'] if r['game_id']==self.target['game_id'])
        row.update(state='PASS',review_ref=None,acceptable_number=None,execution_window=None,
                   cutoff_authority='UNVERIFIED',state_recorded_at_utc=ld['as_of_utc'],state_evidence=ld['cycle_id'])
        args=[a[0]+packet(lm,gate.MARKET_TAG),a[1]+packet(ld,gate.DECISION_TAG),*a[2:-1],ld['as_of_utc']]
        with self.mocked():gate.render(*args)
        self.review['maturity']='INVENTED_PRODUCTION_PROMOTION'
        with self.mocked(),self.assertRaisesRegex(ValueError,'maturity'):gate.render(*args)

    def test_carried_state_cannot_substitute_a_different_review_origin(self):
        a=self.args();lm=copy.deepcopy(self.m);ld=copy.deepcopy(self.d)
        for p in (lm,ld):p.update(cycle_id='CFB_MARKET_MONITOR_20261017T000700Z',as_of_utc='2026-10-17T00:08:00Z')
        row=next(r for r in ld['rows'] if r['game_id']==self.target['game_id'])
        row['review_ref']['blob']='c'*40
        with self.mocked(),self.assertRaisesRegex(ValueError,'originating decision'):
            gate.render(a[0]+packet(lm,gate.MARKET_TAG),a[1]+packet(ld,gate.DECISION_TAG),*a[2:-1],'2026-10-17T00:08:00Z')


if __name__=='__main__':unittest.main()
