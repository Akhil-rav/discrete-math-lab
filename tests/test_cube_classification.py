"""Independent vertex-automorphism and matching-subset oracles for the cube."""

import json
import unittest
from itertools import combinations, permutations
from pathlib import Path

from experiments.classify_cube import run, stirling
from experiments.rainbow_complete_bipartite import normalized_colorings
from src.cube_symmetry import CUBE_EDGES, cube_edge_actions, partitions_into_blocks
from src.rainbow_constraints import avoiding_partitions


class CubeClassificationTests(unittest.TestCase):
    def test_target_partition_iterator(self):
        for n in range(1, 8):
            for k in range(1, n+1):
                expected = {c for c in normalized_colorings(n) if len(set(c)) == k}
                actual = list(partitions_into_blocks(n, k))
                self.assertEqual(set(actual), expected)
                self.assertEqual(len(actual), len(expected))
                self.assertEqual(len(actual), stirling(n, k))
        for n, k in ((0, 0), (2, 3), (13, 7)):
            with self.assertRaises(ValueError):
                list(partitions_into_blocks(n, k))

    def test_full_vertex_automorphism_oracle(self):
        edges = tuple(frozenset((u, 4+v)) for u, v in CUBE_EDGES)
        index = {edge:i for i, edge in enumerate(edges)}
        oracle = set()
        for p in permutations(range(8)):
            images = [frozenset(p[v] for v in edge) for edge in edges]
            if all(e in index for e in images):
                oracle.add(tuple(index[e] for e in images))
        actions = set(cube_edge_actions())
        self.assertEqual(actions, oracle)
        self.assertEqual(len(actions), 48)
        # Composition closure checked as index maps, not just cardinality.
        self.assertTrue(all(tuple(b[a[i]] for i in range(12)) in actions
                            for a in actions for b in actions))

    def test_classification_against_independent_oracles(self):
        data = run()
        sparse = avoiding_partitions(4, CUBE_EDGES)
        self.assertEqual(sparse['maximum_avoiding_colors'], 7)
        self.assertEqual(sparse['extremal_partitions'], data['avoiding_partitions'])
        # Perfect matchings via all four-edge subsets, independently of permutations.
        matchings = [m for m in combinations(range(12), 4)
                     if len({CUBE_EDGES[i][0] for i in m}) == 4
                     and len({CUBE_EDGES[i][1] for i in m}) == 4]
        self.assertEqual(set(matchings), {tuple(m) for m in data['perfect_matchings']})
        members = [tuple(c) for cls in data['classes'] for c in cls['members']]
        self.assertEqual(len(members), len(set(members)))
        self.assertEqual(len(members), 174)
        signatures = []
        for cls in data['classes']:
            c = cls['representative']
            largest = max(range(7), key=c.count)
            degrees = [0]*8
            for i, (u,v) in enumerate(CUBE_EDGES):
                if c[i] == largest:
                    degrees[u] += 1
                    degrees[4+v] += 1
            signatures.append((tuple(cls['color_class_sizes']),
                               tuple(sorted(degrees, reverse=True)),
                               tuple(sorted(cls['matching_color_profiles'].items()))))
        self.assertEqual(len(set(signatures)), 9)
        self.assertEqual([s[1] for s in signatures[:3]],
                         [(3,3,2,2,1,1,0,0), (3,3,1,1,1,1,1,1), (2,2,2,2,2,2,0,0)])
        for c in members:
            # Direct equality-pair obstruction, instead of a set-cardinality test.
            self.assertTrue(all(any(c[a] == c[b] for a, b in combinations(m, 2))
                                for m in matchings))
        reference = Path(__file__).resolve().parents[1]/'results/data/cube_classification.json'
        self.assertEqual(data, json.loads(reference.read_text(encoding='utf-8')))


if __name__ == '__main__':
    unittest.main()
