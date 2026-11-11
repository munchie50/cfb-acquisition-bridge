"""Ensure timing comparisons cannot omit, duplicate or change original checks."""
import copy
from pathlib import Path
import unittest
import cfb_validation_timing_qa as qa


def fixtures():
    groups={**qa.GROUPS,'serial':sum(qa.GROUPS.values(),[])}
    return [{'group':g,'commit':'fixed','protected_inputs_sha256':'fixed',
             'status':'PASS_UNCHANGED_REGRESSION_GROUP_ONLY',
             'started_at_utc':'2026-10-30T02:00:00+00:00','ended_at_utc':'2026-10-30T02:00:04+00:00',
             'elapsed_seconds':9 if g=='serial' else 4,'original_inventory':sum(qa.GROUPS.values(),[]),
             'runs':[{'pattern':p,'tests':3,'skipped':0,'returncode':0} for p in patterns]}
            for g,patterns in groups.items()]


class TimingTests(unittest.TestCase):
    def test_inventory_is_exactly_the_existing_nine_pattern_stage(self):
        text=(Path(__file__).resolve().parents[1]/qa.WORKFLOW).read_text()
        self.assertEqual(len(qa.inventory(text)),9)
        broken=text.replace('python -m unittest discover -s scripts -p test_cfb_week8_publication.py','echo omitted')
        with self.assertRaisesRegex(ValueError,'differ from original'):qa.inventory(broken)

    def test_identical_checks_compare_without_claiming_full_workflow_acceptance(self):
        r=qa.compare(fixtures())
        self.assertEqual(r['tests'],27)
        self.assertEqual(r['observed_stage_seconds_saved'],5)
        self.assertEqual(r['patterns'],9)

    def test_missing_group_failures_and_different_inputs_are_rejected(self):
        with self.assertRaisesRegex(ValueError,'missing or duplicate'):qa.compare(fixtures()[:-1])
        for field,value,expected in [('status','INCOMPLETE','unfinished'),('commit','different','same exact'),
                                     ('protected_inputs_sha256','different','same exact')]:
            r=fixtures();r[0][field]=value
            with self.subTest(field=field),self.assertRaisesRegex(ValueError,expected):qa.compare(r)

    def test_case_count_skip_count_and_duplicate_patterns_are_rejected(self):
        for field,value in [('tests',4),('skipped',1)]:
            r=fixtures();r[0]['runs'][0][field]=value
            with self.subTest(field=field),self.assertRaisesRegex(ValueError,'counts differ'):qa.compare(r)
        r=fixtures();r[0]['runs'].append(copy.deepcopy(r[0]['runs'][0]))
        with self.assertRaisesRegex(ValueError,'duplicate regression'):qa.compare(r)


if __name__=='__main__':unittest.main()
