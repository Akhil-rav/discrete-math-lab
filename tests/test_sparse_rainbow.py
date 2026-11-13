import unittest
from collections import Counter
from itertools import combinations, product

from experiments.rainbow_complete_bipartite import normalized_colorings
from experiments.sparse_rainbow import hosts, run
from src.rainbow_constraints import avoiding_partitions, matching_constraints


def subset_matchings(n, edges):
    return {indices for indices in combinations(range(len(edges)), n)
            if len({edges[i][0] for i in indices}) == n
            and len({edges[i][1] for i in indices}) == n}


class SparseTests(unittest.TestCase):
    def test_all_small_hosts_and_all_color_partitions(self):
        # All bipartite graphs with part size 2 or 3 that admit a PM.
        for n in (2, 3):
            possible = list(product(range(n), repeat=2))
            for mask in range(1 << (n*n)):
                edges = [e for i, e in enumerate(possible) if mask & (1 << i)]
                matchings = subset_matchings(n, edges)
                self.assertEqual(set(matching_constraints(n, edges)), matchings)
                if not matchings:
                    continue
                expected = Counter()
                for c in normalized_colorings(len(edges)):
                    if not any(len({c[i] for i in p}) == n for p in matchings):
                        expected[max(c)+1] += 1
                result = avoiding_partitions(n, edges)
                self.assertEqual(result['avoiding_histogram'], dict(expected))

    def test_larger_hosts_and_cycle_formula(self):
        data = run()
        for n in (2, 3, 4):
            self.assertEqual(data[f'C{2*n}']['maximum_avoiding_colors'], 2*n-2)
        for name, (n, edges) in hosts().items():
            self.assertEqual(set(matching_constraints(n, edges)), subset_matchings(n, edges))
            witness = data[name]['witness']
            self.assertTrue(all(len({witness[i] for i in p}) < n
                                for p in subset_matchings(n, edges)))

    def test_resource_and_input_guards(self):
        for n, edges in [(2, [(0, 0)]), (2, [(0, 0), (0, 0)]),
                         (4, list(product(range(4), repeat=2)))]:
            with self.assertRaises(ValueError):
                avoiding_partitions(n, edges)
