"""Finite checks of the elementary cube collision bound and extremal balance.

Run: python -m experiments.cube_collision_audit [--output PATH | --check PATH].
All 4095 nonempty edge subsets and every saved extremal coloring are checked.
The general proof is in notes/cube_upper_bound.md; this is corroboration.
"""
import argparse
import json
from collections import Counter
from itertools import combinations
from pathlib import Path

from src.cube_symmetry import CUBE_EDGES
from src.rainbow_constraints import matching_constraints


def certificate(colors, matchings):
    blocks = []
    for color in sorted(set(colors)):
        positions = {i for i,c in enumerate(colors) if c == color}
        covered = [j for j,m in enumerate(matchings) if len(positions.intersection(m)) >= 2]
        capacity = 2*(len(positions)-1)
        blocks.append({'color':color, 'size':len(positions),
                       'obstructed_matchings':covered,
                       'capacity':capacity, 'unused_capacity':capacity-len(covered)})
    multiplicities = [sum(j in b['obstructed_matchings'] for b in blocks)
                      for j in range(len(matchings))]
    return {'blocks':blocks,
            'matching_obstruction_counts':multiplicities,
            'unused_capacity':sum(b['unused_capacity'] for b in blocks),
            'overlap':sum(max(0,q-1) for q in multiplicities),
            'rainbow_matchings':multiplicities.count(0)}


def run():
    matchings = matching_constraints(4, CUBE_EDGES)
    appearances = [sum(i in m for m in matchings) for i in range(12)]
    pair_counts = [sum(a in m and b in m for m in matchings)
                   for a,b in combinations(range(12),2)]
    if appearances != [3]*12 or max(pair_counts) != 2:
        raise RuntimeError('Matching incidence constants failed.')
    subset_records = []
    for size in range(1,13):
        histogram = Counter()
        for subset in combinations(range(12),size):
            chosen = set(subset)
            covered = sum(len(chosen.intersection(m)) >= 2 for m in matchings)
            if covered > 2*(size-1):
                raise RuntimeError('A color-class bound failed.')
            histogram[covered] += 1
        subset_records.append({'size':size, 'subsets':sum(histogram.values()),
                               'maximum_obstructed':max(histogram),
                               'coverage_histogram':{str(k):v for k,v in sorted(histogram.items())}})
    data_path = Path(__file__).resolve().parents[1]/'results/data/cube_classification.json'
    data = json.loads(data_path.read_text(encoding='utf-8'))
    classes = []
    population = Counter()
    for cls in data['classes']:
        representative = certificate(cls['representative'],matchings)
        balances = Counter()
        for colors in cls['members']:
            result = certificate(colors,matchings)
            if result['rainbow_matchings'] or result['unused_capacity'] < 0:
                raise RuntimeError('Invalid recorded extremizer.')
            if result['unused_capacity']+result['overlap'] != 1:
                raise RuntimeError('Extremal capacity balance failed.')
            key = f"U={result['unused_capacity']},O={result['overlap']}"
            balances[key] += 1
            population[key] += 1
        if len(balances) != 1:
            raise RuntimeError('Balance is not invariant on an orbit.')
        classes.append({'class_id':cls['class_id'], 'members_checked':len(cls['members']),
                        'balances':dict(balances), 'representative_certificate':representative})
    return {'edge_appearances':appearances, 'maximum_pair_appearances':max(pair_counts),
            'nonempty_subsets_checked':sum(r['subsets'] for r in subset_records),
            'subset_sizes':subset_records, 'extremizers_checked':sum(population.values()),
            'extremal_balances':dict(sorted(population.items())), 'classes':classes}


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--output',type=Path)
    group.add_argument('--check',type=Path)
    args=parser.parse_args()
    data=run()
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
        print('Wrote',args.output)
    elif args.check:
        if data != json.loads(args.check.read_text(encoding='utf-8')):
            raise SystemExit('FAIL: cube collision audit differs')
        print('PASS: cube collision audit matches',args.check)
    else:
        print(json.dumps({k:v for k,v in data.items() if k not in ('classes','subset_sizes')},indent=2))
