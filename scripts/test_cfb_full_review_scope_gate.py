import unittest
import cfb_full_review_scope_gate as gate

GAMES=['Team '+str(i)+' @ Host '+str(i) for i in range(38)]
def document(games=GAMES):
    header='| '+' | '.join(gate.REVIEW_HEADER)+' |\n'
    separator='|'+'---|'*9+'\n'
    rows=''.join('| Sat 1 PM | '+g+' | Host -3 / 50 | +3 -110 | -3 -110 | o50 -110 / u50 -110 | PASS | PASS | 0 |\n' for g in games)
    reasons=''.join('\n### '+g+'\n\nSide: Incomplete source qualification; PASS.\n\nTotal: Insufficient evidence; PASS.\n' for g in games)
    return header+separator+rows+'\n'+reasons+'\n## Nebraska — mandatory unmodeled row\nUNMODELED\n'

class ScopeTests(unittest.TestCase):
    def test_full_scope_pass_is_structural_only(self):
        result=gate.check(GAMES,document())
        self.assertEqual(result['market_verdicts'],76)
        self.assertEqual(result['executability'],'NOT_CERTIFIED')
        self.assertEqual(result['decision_quality'],'NOT_CERTIFIED')
    def test_four_candidate_review_cannot_claim_full_scope(self):
        with self.assertRaisesRegex(ValueError,'identity union/count'):
            gate.check(GAMES,document(GAMES[:4]))
    def test_shortlist_without_full_table_rejected(self):
        with self.assertRaisesRegex(ValueError,'shortlist'):
            gate.check(GAMES,'| Game | Recommendation |\n| A @ B | B -3 |')
    def test_38_rows_with_wrong_identity_rejected(self):
        with self.assertRaises(ValueError):gate.check(GAMES,document(GAMES[:-1]+['Other @ Team']))
    def test_duplicate_identity_cannot_replace_omission(self):
        with self.assertRaises(ValueError):gate.check(GAMES,document(GAMES[:-1]+[GAMES[0]]))
    def test_missing_total_verdict_rejected(self):
        with self.assertRaises(ValueError):gate.check(GAMES,document().replace('| PASS | PASS | 0 |','| PASS |  | 0 |',1))
    def test_missing_total_rationale_rejected(self):
        with self.assertRaises(ValueError):gate.check(GAMES,document().replace('Total: Insufficient evidence; PASS.','',1))
    def test_duplicate_rationale_rejected(self):
        with self.assertRaises(ValueError):gate.check(GAMES,document()+'\n### '+GAMES[0]+'\n')
    def test_nebraska_stays_separate_required(self):
        with self.assertRaises(ValueError):gate.check(GAMES,document().replace('## Nebraska — mandatory unmodeled row',''))
    def test_unqualified_baseline_rejected(self):
        with self.assertRaisesRegex(ValueError,'baseline blob'):gate.expected_games('Unverified slate')
    def test_earlier_friday_trip_beats_saturday_default(self):
        result=gate.effective_deadline('2026-10-10T07:00:00-05:00','2026-10-09T18:00:00-05:00')
        self.assertEqual(result['deadline_utc'],'2026-10-09T23:00:00Z')
        self.assertEqual(result['binding_constraints'],['trip'])
    def test_later_trip_cannot_relax_default(self):
        result=gate.effective_deadline('2026-10-10T07:00:00-05:00','2026-10-10T09:00:00-05:00')
        self.assertEqual(result['binding_constraints'],['default'])
    def test_earlier_execution_cutoff_binds(self):
        result=gate.effective_deadline('2026-10-10T12:00:00Z','2026-10-09T23:00:00Z','2026-10-09T22:30:00Z')
        self.assertEqual(result['binding_constraints'],['execution'])
    def test_unknown_trip_is_not_invented(self):
        result=gate.effective_deadline('2026-10-10T12:00:00Z')
        self.assertEqual(result['trip_constraint'],'UNVERIFIED_NOT_INVENTED')
        self.assertEqual(result['execution_constraint'],'UNVERIFIED_NOT_INVENTED')
    def test_timezone_required(self):
        for field in ['default','trip','execution']:
            args={'default':'2026-10-10T12:00:00Z',field:'2026-10-10T07:00:00'}
            with self.subTest(field=field),self.assertRaises(ValueError):gate.effective_deadline(**args)
    def test_equivalent_clocks_retain_tied_constraints(self):
        result=gate.effective_deadline('2026-10-09T23:00:00Z','2026-10-09T18:00:00-05:00')
        self.assertEqual(result['binding_constraints'],['default','trip'])

if __name__=='__main__':unittest.main()
