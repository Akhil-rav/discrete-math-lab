"""Check local links, JSON, evidence hashes, proof revisions, and reproductions.

Run: python -m tools.verify_repository [--static-only]
This never executes commands read from a manifest. Historical output hashes are
verified; current input differences are reported separately from corruption.
The link scan supports the simple inline links used in this repository, not
every possible Markdown extension, external URLs, or heading-anchor validation.
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PureWindowsPath
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]
DATASETS={
    'results/data/small_cases.json':'results/runs/2026-11-13/small_cases.json',
    'results/data/sparse_rainbow.json':'results/runs/sparse-2026-11-13/sparse_rainbow.json',
    'results/data/cube_classification.json':'results/runs/cube-classification-2026-11-14/classification.json',
    'results/data/cube_collisions.json':'results/runs/cube-collisions-2026-11-14/audit.json',
    'results/data/random_rainbow.json':'results/runs/random-rainbow-2026-11-14/probabilities.json',
}
PROOF_REVIEWS={
    'notes/cube_upper_bound.md':'results/cube_bound_review.md',
    'notes/random_rainbow.md':'results/random_rainbow_verification.md',
    'papers/expansion_walks.tex':'results/walk_paper_verification.md',
}
REPRODUCTIONS=(
    ('experiments.reproduce','results/data/small_cases.json'),
    ('experiments.sparse_rainbow','results/data/sparse_rainbow.json'),
    ('experiments.classify_cube','results/data/cube_classification.json'),
    ('experiments.cube_collision_audit','results/data/cube_collisions.json'),
    ('experiments.random_rainbow','results/data/random_rainbow.json'),
)


class VerificationError(ValueError):
    pass


def project_path(root, name):
    path=Path(name)
    if path.is_absolute() or PureWindowsPath(name).is_absolute():
        raise VerificationError(f'Expected a project-relative path: {name}')
    resolved=(root/path).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise VerificationError(f'Path leaves the repository: {name}')
    return resolved


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    def unique(pairs):
        result={}
        for key,value in pairs:
            if key in result:
                raise VerificationError(f'Duplicate JSON key {key!r} in {path}')
            result[key]=value
        return result

    def invalid_constant(value):
        raise VerificationError(f'Non-finite JSON value {value} in {path}')

    return json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=unique,
                      parse_constant=invalid_constant)


def audit_manifest(root, path):
    record=read_json(path)
    if record.get('schema_version') != 2:
        raise VerificationError(f'Unsupported manifest version: {path}')
    completed=record.get('run',{}).get('status') == 'completed'
    if completed and record['run'].get('exit_status') != 0:
        raise VerificationError(f'Contradictory successful-run status: {path}')
    current=changed=outputs=0
    for item in record['input_artifacts']:
        source=project_path(root,item['path'])
        if completed and item['sha256'] != item.get('sha256_after'):
            raise VerificationError(f'Inputs changed during a claimed successful run: {path}')
        if source.is_file() and digest(source) == item['sha256']:
            current += 1
        else:
            changed += 1
    for item in record['outputs']:
        output=project_path(root,item['path'])
        if not output.is_file() or digest(output) != item['sha256']:
            raise VerificationError(f'Missing or altered recorded output: {item["path"]}')
        outputs += 1
    return {'completed':completed,'outputs':outputs,
            'current_inputs':current,'historical_inputs':changed}


def local_links(root):
    checked=0
    for document in sorted(root.rglob('*.md')):
        if '.git' in document.relative_to(root).parts:
            continue
        text=re.sub(r'```.*?```','',document.read_text(encoding='utf-8'),flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)',text):
            target=target.strip().strip('<>')
            if urlsplit(target).scheme or target.startswith('#'):
                continue
            target=unquote(target.split('#',1)[0])
            destination=(document.parent/target).resolve()
            if not destination.is_relative_to(root.resolve()) or not destination.exists():
                raise VerificationError(f'Broken local link in {document.relative_to(root)}: {target}')
            checked += 1
    return checked


def static_checks(root):
    links=local_links(root)
    json_files=[p for p in root.rglob('*.json') if '.git' not in p.relative_to(root).parts]
    for path in json_files:
        read_json(path)
    manifests=sorted((root/'results/runs').glob('*/manifest.json'))
    summaries=[audit_manifest(root,p) for p in manifests]
    for reference,recorded in DATASETS.items():
        if read_json(root/reference) != read_json(root/recorded):
            raise VerificationError(f'Reference differs from its recorded result: {reference}')
        manifest=read_json((root/recorded).parent/'manifest.json')
        if manifest['run']['status'] != 'completed':
            raise VerificationError(f'Reference is linked to an unsuccessful run: {reference}')
    for source,review in PROOF_REVIEWS.items():
        match=re.search(r'SHA-256: `([a-f0-9]{64})`',(root/review).read_text(encoding='utf-8'))
        if not match or match.group(1) != digest(root/source):
            raise VerificationError(f'Proof changed since its recorded review: {source}')
    print(f'PASS: {links} local links; {len(json_files)} JSON files; '
          f'{len(manifests)} run records; {sum(s["outputs"] for s in summaries)} output hashes; '
          f'{len(DATASETS)} reference datasets; {len(PROOF_REVIEWS)} reviewed source hashes.',flush=True)
    changed=sum(s['historical_inputs'] for s in summaries)
    if changed:
        print(f'NOTE: {changed} historical input references differ from current files; '
              'run the reproduction commands to validate the current implementation.')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--static-only',action='store_true',help='Skip tests and mathematical reruns.')
    args=parser.parse_args()
    try:
        static_checks(ROOT)
        if not args.static_only:
            commands=[['-m','unittest','discover','-s','tests','-v']]
            commands += [['-m',module,'--check',path] for module,path in REPRODUCTIONS]
            for command in commands:
                subprocess.run([sys.executable,*command],cwd=ROOT,check=True,timeout=60)
            print('PASS: all mathematical tests and five data reproductions.')
    except (VerificationError,OSError,ValueError,KeyError,subprocess.SubprocessError) as error:
        print(f'FAIL: {error}',file=sys.stderr)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
