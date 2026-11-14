"""Classify all seven-color cube partitions avoiding rainbow perfect matchings.

Run: python -m experiments.classify_cube [--output PATH | --check PATH].
Scope: all S(12,7) partitions; the existing full search separately establishes
that seven is the maximum. Color names and all cube automorphisms are ignored
only for the final orbit classification. No novelty claim.
"""

import argparse
import json
from collections import Counter
from pathlib import Path

from src.cube_symmetry import (
    CUBE_EDGES, cube_edge_actions, cube_orbit, partitions_into_blocks,
    transform_partition,
)
from src.rainbow_constraints import matching_constraints


def stirling(n, k):
    row = [1] + [0]*k
    for _ in range(n):
        row = [0] + [j*row[j]+row[j-1] for j in range(1, k+1)]
    return row[k]


def run():
    matchings = matching_constraints(4, CUBE_EDGES)
    population = set()
    checked = 0
    for colors in partitions_into_blocks(12, 7):
        checked += 1
        if all(len({colors[i] for i in m}) < 4 for m in matchings):
            population.add(colors)
    if checked != stirling(12, 7):
        raise RuntimeError('Exact-seven partition coverage failed.')
    actions = cube_edge_actions()
    if len(set(actions)) != 48:
        raise RuntimeError('Expected 48 distinct edge actions.')
    remaining = set(population)
    records = []
    while remaining:
        representative = min(remaining)
        orbit = cube_orbit(representative)
        stabilizer = sum(transform_partition(representative, a) == representative
                         for a in actions)
        if not orbit <= population or not orbit <= remaining:
            raise RuntimeError('Orbits must be disjoint and closed in the population.')
        if len(orbit)*stabilizer != 48:
            raise RuntimeError('Orbit-stabilizer check failed.')
        remaining -= orbit
        records.append({
            'class_id': len(records)+1,
            'representative': list(representative),
            'orbit_size': len(orbit), 'stabilizer_size': stabilizer,
            'color_class_sizes': sorted(Counter(representative).values(), reverse=True),
            'matching_color_profiles': dict(sorted(Counter(
                ','.join(map(str, sorted(Counter(representative[i] for i in m).values(), reverse=True)))
                for m in matchings).items())),
            'members': [list(c) for c in sorted(orbit)],
        })
    return {
        'host': 'K4,4 minus the diagonal (cube Q3)',
        'edges': [list(e) for e in CUBE_EDGES],
        'colors': 7, 'partitions_checked': checked,
        'perfect_matchings': [list(m) for m in matchings],
        'automorphism_group_order': 48,
        'avoiding_partitions': len(population),
        'symmetry_class_count': len(records), 'classes': records,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--output', type=Path)
    group.add_argument('--check', type=Path)
    args = parser.parse_args()
    data = run()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8', newline='\n')
        print('Wrote', args.output)
    elif args.check:
        if data != json.loads(args.check.read_text(encoding='utf-8')):
            raise SystemExit('FAIL: cube classification differs')
        print('PASS: cube classification matches', args.check)
    else:
        summary = {k:v for k,v in data.items() if k != 'classes'}
        summary['classes'] = [{k:v for k,v in c.items() if k != 'members'} for c in data['classes']]
        print(json.dumps(summary, indent=2))
