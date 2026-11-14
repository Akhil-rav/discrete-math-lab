"""Negative controls for the portable evidence-integrity checks."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from tools.verify_repository import VerificationError, audit_manifest, local_links, project_path, read_json


class RepositoryVerificationTests(unittest.TestCase):
    def test_duplicate_keys_and_escaping_paths_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary)
            bad=root/'duplicate.json'
            bad.write_text('{"count":1,"count":2}')
            with self.assertRaises(VerificationError): read_json(bad)
            bad.write_text('{"value":NaN}')
            with self.assertRaises(VerificationError): read_json(bad)
            for name in ('../outside.json','C:/outside.json','/outside.json'):
                with self.assertRaises(VerificationError): project_path(root,name)

    def test_output_corruption_is_distinct_from_historical_source_changes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary)
            source=root/'source.py'
            result=root/'result.json'
            source.write_bytes(b'original')
            result.write_bytes(b'{"answer":7}')
            hashed=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
            record={'schema_version':2,'run':{'status':'completed','exit_status':0},
                    'input_artifacts':[{'path':'source.py','sha256':hashed(source),'sha256_after':hashed(source)}],
                    'outputs':[{'path':'result.json','sha256':hashed(result)}]}
            path=root/'manifest.json'
            path.write_text(json.dumps(record))
            self.assertEqual(audit_manifest(root,path)['current_inputs'],1)
            source.write_bytes(b'new implementation')
            self.assertEqual(audit_manifest(root,path)['historical_inputs'],1)
            result.write_bytes(b'{"answer":8}')
            with self.assertRaises(VerificationError): audit_manifest(root,path)

    def test_local_images_and_links_are_checked(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary)
            (root/'figure.svg').write_text('<svg/>')
            (root/'README.md').write_text('![figure](figure.svg) [web](https://example.com)')
            self.assertEqual(local_links(root),1)
            (root/'README.md').write_text('[missing](does-not-exist.md)')
            with self.assertRaises(VerificationError): local_links(root)


if __name__ == '__main__':
    unittest.main()
