"""Bounded sparse-host extension. Run: python -m experiments.sparse_rainbow.

--output PATH saves JSON; --check PATH compares with a saved reference.
The cube host is K44 with one fixed perfect matching deleted.
"""
import argparse
import json
from pathlib import Path
from src.rainbow_constraints import avoiding_partitions


def hosts():
    cases = {}
    for n in (2, 3, 4):
        cases[f'C{2*n}'] = (n, sorted({(i, i) for i in range(n)} |
                                    {(i, (i+1) % n) for i in range(n)}))
    cases['2C4'] = (4, [(i, j) for i in range(4) for j in range(4) if i//2 == j//2])
    cases['K33'] = (3, [(i, j) for i in range(3) for j in range(3)])
    cases['cube'] = (4, [(i, j) for i in range(4) for j in range(4) if i != j])
    return cases


def run():
    return {name: avoiding_partitions(n, edges) for name, (n, edges) in hosts().items()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--output', type=Path)
    group.add_argument('--check', type=Path)
    args = parser.parse_args()
    data = json.loads(json.dumps(run()))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8', newline='\n')
        print('Wrote', args.output)
    elif args.check:
        if data != json.loads(args.check.read_text(encoding='utf-8')):
            raise SystemExit('FAIL: sparse results differ')
        print('PASS: sparse results match', args.check)
    else:
        print(json.dumps(data, indent=2))
