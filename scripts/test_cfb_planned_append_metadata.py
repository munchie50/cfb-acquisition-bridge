import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
import cfb_planned_append_metadata as m


class ExactTransferTests(unittest.TestCase):
    def test_manifest_contains_no_source_text(self):
        data='private source text'.encode();r=m.transfer(data,m.git_blob(data))
        self.assertFalse(r['raw_content_included']);self.assertNotIn('content',r)
        self.assertEqual(r['status'],'TRANSPORT_ONLY_NOT_WRITE_SUCCESS')

    def test_unicode_large_complete_reassembly(self):
        data=('é😀 line\n'*10000).encode();sha=m.git_blob(data)
        r=m.transfer(data,sha);parts=[m.transfer(data,sha,i) for i in range(r['chunk_count'])]
        self.assertGreater(r['bytes'],r['characters'])
        for i,p in enumerate(parts):
            self.assertEqual(p['chunk_index'],i)
            self.assertLessEqual(len(p['content']),12000)
            self.assertEqual(m.git_blob(p['content'].encode()),p['chunk_git_blob'])
        self.assertEqual(''.join(p['content'] for p in parts).encode(),data)

    def test_truncated_source_rejected_before_transfer(self):
        data=b'a'*100000;sha=m.git_blob(data)
        with self.assertRaisesRegex(ValueError,'complete Git blob'):m.transfer(data[:2000],sha)

    def test_changed_source_between_chunks_rejected(self):
        data=b'a'*14000;sha=m.git_blob(data);m.transfer(data,sha,0)
        with self.assertRaises(ValueError):m.transfer(data+b'b',sha,1)

    def test_missing_duplicate_or_reordered_pieces_differ_from_complete_blob(self):
        data=b'aabbcc';sha=m.git_blob(data);p=[m.transfer(data,sha,i,2)['content'] for i in range(3)]
        for wrong in (p[:2],p+[p[0]],list(reversed(p))):
            self.assertNotEqual(m.git_blob(''.join(wrong).encode()),sha)

    def test_invalid_bounds(self):
        data=b'abc';sha=m.git_blob(data)
        for i in (-1,1,True):
            with self.assertRaises(ValueError):m.transfer(data,sha,i)
        for n in (0,12001,True):
            with self.assertRaises(ValueError):m.transfer(data,sha,chunk_characters=n)

    def test_invalid_encoding_or_expected_hash(self):
        with self.assertRaises(UnicodeDecodeError):m.transfer(b'\xff',m.git_blob(b'\xff'))
        with self.assertRaises(ValueError):m.transfer(b'a','bad')

    def test_existing_append_contract_preserved(self):
        a=b'prior\n';b=a+'é\n'.encode();r=m.metadata(a,b,m.git_blob(a),['provenance'])
        self.assertTrue(r['prior_bytes_preserved']);self.assertEqual(r['delta_characters'],2)
        self.assertEqual(r['status'],'PROPOSED_ONLY_NOT_WRITE_SUCCESS')
        with self.assertRaises(ValueError):m.metadata(a,b'changed',m.git_blob(a),['provenance'])

    def test_cli_chunk_and_normal_missing_arguments(self):
        script=Path(m.__file__)
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'text';p.write_text('é😀')
            result=subprocess.run([sys.executable,str(script),'--transfer-file',str(p),
                '--expected-transport-sha',m.git_blob(p.read_bytes()),'--chunk-index','0'],capture_output=True,text=True)
            self.assertEqual(result.returncode,0);self.assertEqual(json.loads(result.stdout)['content'],'é😀')
        result=subprocess.run([sys.executable,str(script)],capture_output=True,text=True)
        self.assertNotEqual(result.returncode,0)


if __name__=='__main__':unittest.main()
