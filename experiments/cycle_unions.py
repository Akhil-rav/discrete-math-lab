"""Check ten even-cycle unions through 12 edges against the proved classification.

All partitions are checked through 10 edges. On every host, all partitions
with m-2, m-1, or m blocks are checked separately. The 12-edge cases do not
claim full Bell-number coverage. Run: python -m experiments.cycle_unions.
"""
import argparse
import json
from collections import Counter
from itertools import combinations, product
from math import comb
from pathlib import Path

from experiments.rainbow_complete_bipartite import normalized_colorings
from src.cube_symmetry import partitions_into_blocks
from src.cycle_unions import cycle_union, extremal_partitions

HOSTS = ((2,), (3,), (4,), (2, 2), (5,), (2, 3),
         (6,), (2, 4), (3, 3), (2, 2, 2))


def stirling(n, k):
    row = [1]
    for size in range(1, n+1):
        row = [0]+[(row[j-1] if j-1 < len(row) else 0)
                   + (j*row[j] if j < len(row) else 0) for j in range(1, size+1)]
    return row[k]


def subset_matchings(edges):
    """Independent oracle: edge subsets with every vertex used exactly once."""
    return {indices for indices in combinations(range(len(edges)), len(edges)//2)
            if len({v for i in indices for v in edges[i]}) == len(edges)}


def avoids(colors, matchings):
    return all(len({colors[i] for i in matching}) < len(matching)
               for matching in matchings)


def run():
    records = []
    for half_lengths in HOSTS:
        edges, alternating = cycle_union(half_lengths)
        m = len(edges)
        matchings = tuple(sorted(tuple(sorted(i for local in choices for i in local))
                                 for choices in product(*alternating)))
        if set(matchings) != subset_matchings(edges):
            raise RuntimeError('Alternating-product matchings disagree with edge subsets.')
        expected = set(extremal_partitions(half_lengths))
        expected_count = sum(comb(n, 2)**2 for n in half_lengths)
        if len(expected) != expected_count:
            raise RuntimeError('Construction has missing or duplicate extremizers.')
        bands = []
        for k in range(m-2, m+1):
            found, candidates = set(), 0
            for colors in partitions_into_blocks(m, k):
                candidates += 1
                if avoids(colors, matchings):
                    found.add(colors)
            if candidates != stirling(m, k):
                raise RuntimeError('Exact-block search has incomplete coverage.')
            if found != (expected if k == m-2 else set()):
                raise RuntimeError('Extremal band disagrees with the theorem.')
            bands.append({'colors': k, 'candidates_checked': candidates,
                          'avoiding_partitions': len(found)})
        full = None
        if m <= 10:
            histogram, found, visited = Counter(), set(), 0
            for colors in normalized_colorings(m):
                visited += 1
                # Separate predicate: an equal-colored pair in every matching.
                if all(any(colors[a] == colors[b] for a, b in combinations(matching, 2))
                       for matching in matchings):
                    blocks = max(colors)+1
                    histogram[blocks] += 1
                    if blocks == m-2:
                        found.add(colors)
            if visited != sum(stirling(m, k) for k in range(1, m+1)):
                raise RuntimeError('Full partition search has incomplete coverage.')
            if max(histogram) != m-2 or found != expected:
                raise RuntimeError('Full search disagrees with the classification.')
            full = {'partitions_checked': visited,
                    'avoiding_histogram': dict(sorted(histogram.items()))}
        records.append({'half_lengths': list(half_lengths),
                        'edges': [list(e) for e in edges],
                        'perfect_matchings': [list(matching) for matching in matchings],
                        'maximum_avoiding_colors': m-2,
                        'extremal_partitions': expected_count,
                        'exact_color_bands': bands,
                        'full_enumeration': full,
                        'extremizers': [list(c) for c in sorted(expected)]})
    return {'schema_version': 1, 'hosts': records}


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
            raise SystemExit('FAIL: even-cycle-union data differ')
        print('PASS: even-cycle-union classification matches', args.check)
    else:
        print(json.dumps([{k: v for k, v in h.items() if k not in
                          ('edges', 'perfect_matchings', 'extremizers', 'full_enumeration')}
                         for h in data['hosts']], indent=2))
