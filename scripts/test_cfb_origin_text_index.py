"""Parsing reuse must preserve provenance rejection and per-call validation."""
import copy
import json
import unittest
import cfb_neutral_publication_gate as gate


def block(packet,tag=gate.DECISION_TAG,space=''):
    return '```'+tag+space+'\n'+json.dumps(packet)+'\n```\n'


class OriginIndexTests(unittest.TestCase):
    def setUp(self):
        gate._origin_packet_index.cache_clear()
        self.proof='CFB_MARKET_MONITOR_20261023T170000Z'
        self.row={'game_id':'one','state':'PASS','state_recorded_at_utc':'2026-10-23T17:00:00Z',
                  'state_evidence':self.proof}
        self.origin={'schema':gate.WEEKLY_DECISION_SCHEMA,'cycle_id':self.proof,
                     'as_of_utc':'2026-10-23T17:01:00Z','rows':[self.row]}
        self.raw=block(self.origin)
        self.current={'cycle_id':'CFB_MARKET_MONITOR_20261023T180000Z','as_of_utc':'2026-10-23T18:01:00Z'}

    def validate_state(self,raw=None,row=None,packet=None):
        gate.state_evidence(row or self.row,packet or self.current,raw or self.raw,
                            gate.clock('2026-10-24T00:00:00Z'),gate.clock('2026-10-23T18:01:00Z'))

    def test_identical_bytes_reuse_index_but_return_independent_mutable_packets(self):
        first=gate._matching_origin_packets(self.raw,gate.DECISION_TAG,self.proof,gate.WEEKLY_DECISION_SCHEMAS)
        first[0]['rows'][0]['state']='CONDITIONAL'
        second=gate._matching_origin_packets(self.raw,gate.DECISION_TAG,self.proof,gate.WEEKLY_DECISION_SCHEMAS)
        self.assertEqual(second[0]['rows'][0]['state'],'PASS')
        self.assertGreater(gate._origin_packet_index.cache_info().hits,0)
        self.validate_state()

    def test_changed_bytes_and_duplicate_origins_are_not_cached_as_valid(self):
        self.validate_state()
        changed=copy.deepcopy(self.origin);changed['rows'][0]['state']='CONDITIONAL'
        with self.assertRaisesRegex(ValueError,'origin mismatch'):self.validate_state(block(changed))
        with self.assertRaisesRegex(ValueError,'missing/ambiguous'):self.validate_state(self.raw+self.raw)

    def test_duplicate_json_keys_and_bad_nonmatching_packets_still_rejected(self):
        self.validate_state()
        bad='```'+gate.DECISION_TAG+'\n{"schema":"a","schema":"b","cycle_id":"other"}\n```\n'
        with self.assertRaisesRegex(ValueError,'duplicate'):self.validate_state(self.raw+bad)
        with self.assertRaises((ValueError,json.JSONDecodeError)):
            self.validate_state(self.raw+'```'+gate.DECISION_TAG+'\n{broken}\n```\n')

    def test_missing_schema_and_short_circuit_cycle_rules_preserved(self):
        missing={'cycle_id':'other','rows':[]}
        with self.assertRaises(KeyError):self.validate_state(self.raw+block(missing))
        wrong={'schema':'IGNORED_SCHEMA','rows':[]}
        self.validate_state(self.raw+block(wrong))
        allowed={'schema':gate.WEEKLY_DECISION_SCHEMA,'rows':[]}
        with self.assertRaises(KeyError):self.validate_state(self.raw+block(allowed))

    def test_warm_index_never_caches_clock_or_postkickoff_validation(self):
        self.validate_state()
        with self.assertRaisesRegex(ValueError,'future state'):
            self.validate_state(packet={'as_of_utc':'2026-10-23T16:59:00Z'})
        changed=copy.deepcopy(self.row);changed['state_recorded_at_utc']='2026-10-23T18:30:00Z'
        with self.assertRaisesRegex(ValueError,'future state'):self.validate_state(row=changed)
        with self.assertRaisesRegex(ValueError,'postkickoff'):
            gate.state_evidence(self.row,self.current,self.raw,gate.clock('2026-10-23T16:00:00Z'),
                                gate.clock('2026-10-23T18:01:00Z'))

    def test_header_mode_and_tag_do_not_share_a_looser_index(self):
        raw=block(self.origin,space=' ')
        self.assertEqual(len(gate._matching_origin_packets(raw,gate.DECISION_TAG,self.proof)),1)
        self.assertEqual(gate._matching_origin_packets(raw,gate.DECISION_TAG,self.proof,strict_header=True),[])
        self.assertEqual(gate._matching_origin_packets(self.raw,'other-tag',self.proof),[])

    def test_cache_is_bounded_and_contains_no_mutable_packet_objects(self):
        for i in range(8):
            r={**self.origin,'cycle_id':str(i)}
            records=gate._origin_packet_index(block(r),gate.DECISION_TAG,False)
            self.assertTrue(all(isinstance(x,(str,bool)) for record in records for x in record))
        self.assertLessEqual(gate._origin_packet_index.cache_info().currsize,4)


if __name__=='__main__':unittest.main()
