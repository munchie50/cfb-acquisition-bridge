import copy
import unittest
import cfb_consensus_reference as consensus


class ConsensusTests(unittest.TestCase):
    def setUp(self):
        self.p = dict(game_id='synthetic_game', market='SPREAD', selection='away',
                      kickoff_utc='2026-10-17T17:00:00Z', kickoff_source_url='https://example.org/schedule/game',
                      period='PREGAME_FULL_GAME', collection_start='2026-10-16T23:00:00Z',
                      collection_end='2026-10-16T23:05:00Z', quotes=[])
        for i, line in enumerate((3, 3.5, 4)):
            self.p['quotes'].append(dict(game_id='synthetic_game', market='SPREAD', selection='away',
                period='PREGAME_FULL_GAME', book='SyntheticBook'+str(i), operator='SyntheticOperator'+str(i),
                operator_evidence_url='https://example.org/operator/'+str(i), source_url='https://example.org/quote/'+str(i),
                retrieved_at='2026-10-16T23:04:00Z', offer_updated_at='2026-10-16T23:03:00Z', line=line, price=-110))
    def run_ref(self): return consensus.reference(self.p, '2026-10-16T23:05:00Z')
    def test_three_independent_median_and_dispersion(self):
        r=self.run_ref(); self.assertEqual(r['reference_points'], 3.5)
        self.assertEqual(r['points_range'], [3,4]); self.assertEqual(r['reasons'], [])
        self.assertFalse(r['reference_is_executable_offer'])
    def test_fewer_than_three_unavailable(self):
        self.p['quotes'].pop(); self.assertIn('FEWER_THAN_THREE_INDEPENDENT_OPERATORS', self.run_ref()['reasons'])
    def test_duplicate_skin_does_not_add_operator(self):
        q=copy.deepcopy(self.p['quotes'][0]);q['book']='SyntheticSkin';self.p['quotes']=[self.p['quotes'][0],q,self.p['quotes'][1]]
        self.assertEqual(self.run_ref()['operator_count'],2)
    def test_caesars_is_excluded_not_required(self):
        q=copy.deepcopy(self.p['quotes'][0]);q.update(book='Caesars NJ',operator='Caesars');self.p['quotes'].append(q)
        r=self.run_ref();self.assertEqual(r['operator_count'],3);self.assertEqual(r['reasons'],[])
    def test_unknown_update_is_not_retrieval_time(self):
        self.p['quotes'][0]['offer_updated_at']=None
        r=self.run_ref();self.assertEqual(r['status'],'CONSENSUS_UNAVAILABLE')
        self.assertIsNone(r['constituents'][0]['offer_updated_at'])
    def test_stale_update_unavailable(self):
        self.p['quotes'][0]['offer_updated_at']='2026-10-15T23:00:00Z'
        self.assertIn('OFFER_UPDATE_OUTSIDE_COLLECTION_WINDOW',self.run_ref()['reasons'])
    def test_future_window_and_future_update_rejected(self):
        with self.assertRaises(ValueError): consensus.reference(self.p,'2026-10-16T23:00:00Z')
        self.p['quotes'][0]['offer_updated_at']='2026-10-16T23:05:00Z'
        with self.assertRaises(ValueError):self.run_ref()
    def test_even_midpoint_has_no_invented_price(self):
        self.p['quotes'][1]['line']=4; self.p['quotes'][2]['line']=5
        q=copy.deepcopy(self.p['quotes'][2]);q.update(book='SyntheticBook3',operator='SyntheticOperator3',line=6)
        self.p['quotes'].append(q)
        r=self.run_ref();self.assertEqual(r['reference_points'],4.5)
        self.assertIsNone(r['exact_reference_line_price_range'])
    def test_american_prices_never_averaged(self):
        self.p['quotes'][0].update(line=3.5,price=-120)
        r=self.run_ref();self.assertEqual(r['exact_reference_line_price_range'],[-120,-110])
    def test_moneyline_no_fabricated_consensus_probability(self):
        self.p['market']='MONEYLINE'
        for q in self.p['quotes']:q.update(market='MONEYLINE',line=None)
        r=self.run_ref();self.assertIsNone(r['reference_points']);self.assertIsNone(r['moneyline_probability'])
    def test_conflict_missing_price_and_wrong_selection_fail(self):
        for mode in ('conflict','price','selection'):
            p=copy.deepcopy(self.p)
            if mode=='conflict':
                q=copy.deepcopy(p['quotes'][0]);q['line']=7;p['quotes'].append(q)
            elif mode=='price':p['quotes'][0]['price']=None
            else:p['quotes'][0]['selection']='home'
            with self.assertRaises(ValueError):consensus.reference(p,'2026-10-16T23:05:00Z')
    def test_unknown_fields_and_nan_fail(self):
        self.p['quotes'][0]['line']=float('nan')
        with self.assertRaises(ValueError):self.run_ref()

    def test_padded_operator_labels_cannot_manufacture_three_books(self):
        for q, label in zip(self.p['quotes'], ('SyntheticOperator0', ' SyntheticOperator0', 'SyntheticOperator0 ')):
            q.update(operator=label, line=3)
        result=self.run_ref()
        self.assertEqual(result['operator_count'],1)
        self.assertEqual(result['status'],'CONSENSUS_UNAVAILABLE')

    def test_padding_and_case_together_still_deduplicate(self):
        for q, label in zip(self.p['quotes'], (' SyntheticOperator0 ', 'SYNTHETICOPERATOR0', '\u00a0syntheticoperator0\u00a0')):
            q.update(operator=label, line=3)
        self.assertEqual(self.run_ref()['operator_count'],1)

    def test_same_operator_conflict_cannot_hide_in_padding(self):
        self.p['quotes'][1]['operator']=' '+self.p['quotes'][0]['operator']+' '
        with self.assertRaisesRegex(ValueError,'same-operator'):
            self.run_ref()

    def test_padded_caesars_book_label_is_excluded(self):
        self.p['quotes'][0].update(book=' Caesars NJ ',operator='SyntheticSkin')
        result=self.run_ref()
        self.assertEqual(result['operator_count'],2)
        self.assertEqual(result['excluded'],[{'book':' Caesars NJ ','reason':'CAESARS_EXCLUDED'}])
        self.assertEqual(result['status'],'CONSENSUS_UNAVAILABLE')

    def test_padded_caesars_operator_label_is_excluded(self):
        self.p['quotes'][0].update(book='SyntheticSkin',operator='\u00a0cAeSaRs Entertainment\u00a0')
        result=self.run_ref()
        self.assertEqual(result['operator_count'],2)
        self.assertEqual(result['status'],'CONSENSUS_UNAVAILABLE')

    def test_semantically_invalid_market_selection_rejected(self):
        for market, selection in (('SPREAD','over'),('TOTAL','away'),('MONEYLINE','under'),('SPREAD','invented')):
            with self.subTest(market=market,selection=selection):
                p=copy.deepcopy(self.p);p.update(market=market,selection=selection)
                for q in p['quotes']:q.update(market=market,selection=selection,line=None if market=='MONEYLINE' else 3)
                with self.assertRaisesRegex(ValueError,'selection'):
                    consensus.reference(p,'2026-10-16T23:05:00Z')

    def test_normalization_preserves_all_raw_constituent_labels(self):
        self.p['quotes'][0].update(book=' SyntheticBook0 ',operator=' SyntheticOperator0 ')
        original=copy.deepcopy(self.p)
        result=self.run_ref()
        self.assertEqual(self.p,original)
        self.assertEqual(result['constituents'],original['quotes'])
        self.assertEqual(result['operator_count'],3)

    def test_conditional_display_marks_padded_caesars_excluded(self):
        from unittest.mock import patch
        import cfb_conditional_recommendation_profile as profile
        q=copy.deepcopy(self.p['quotes'][0]);q.update(book=' Caesars NJ ',operator='SyntheticSkin')
        self.p['quotes'].append(q)
        reference=self.run_ref()
        review=dict(acceptable_number=dict(line=3,minimum_price=-110,direction='AT_LEAST'),
                    selection='away',market='SPREAD',planning_cutoff_utc='2026-10-17T14:00:00Z',
                    uncertainty='Synthetic only',market_reference=self.p)
        with patch.object(profile,'validate',return_value=(review,reference)):
            conditions,context=profile.display({}, {}, {}, '2026-10-16T23:05:00Z')
        self.assertIn(' Caesars NJ  [EXCLUDED FROM REFERENCE]',context)
        self.assertIn('3 operators',context)
        self.assertIn('VENUE_CONFIRMATION_PENDING',conditions)

    def test_postkickoff_collection_rejected_and_old_reference_labelled(self):
        r=consensus.reference(self.p,'2026-10-18T00:00:00Z')
        self.assertIn('AT_OR_AFTER_KICKOFF',r['reasons'])
        self.assertFalse(r['current_freshness_certified'])
        self.p['kickoff_utc']='2026-10-16T23:04:00Z'
        with self.assertRaises(ValueError):self.run_ref()


if __name__=='__main__':unittest.main()
