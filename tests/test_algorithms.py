"""Independent finite oracles and boundary tests for mathematical contracts."""

import unittest
from fractions import Fraction
from itertools import combinations, permutations, product

from experiments.rainbow_complete_bipartite import (
    exhaustive_search, has_rainbow_perfect_matching, normalized_colorings,
)
from experiments.regular_bipartite_matchings import generate_regular_bipartite_graphs
from src.arithmetic_progressions import group_three_aps, interval_three_aps
from src.bipartite_graph import BipartiteGraph
from src.color_coding import colorful_path
from src.color_patterns import normalize, square_orbit
from src.expansion import edge_expansion, walk_total_variation
from src.matchings import maximum_matching, has_perfect_matching


class MatchingTests(unittest.TestCase):
    def test_every_small_bipartite_graph(self):
        """Compare augmenting paths to partial-injection enumeration, n <= 3."""
        for n in range(4):
            for mask in range(1 << (n*n)):
                adj = {i: {n+j for j in range(n) if mask & (1 << (i*n+j))}
                       for i in range(n)}
                graph = BipartiteGraph(set(range(n)), set(range(n, 2*n)), adj)
                oracle = 0
                for size in range(n+1):
                    if any(all(v in adj[u] for u, v in zip(left, right))
                           for left in combinations(range(n), size)
                           for right in permutations(range(n, 2*n), size)):
                        oracle = size
                matching = maximum_matching(graph)
                self.assertEqual(len(matching), oracle)
                self.assertEqual(len(set(matching.values())), len(matching))
                self.assertTrue(all(v in adj[u] for u, v in matching.items()))
                self.assertEqual(has_perfect_matching(graph), oracle == n)

    def test_regular_generator_against_all_masks(self):
        for n in range(1, 4):
            for d in range(n+1):
                expected = set()
                for bits in product((0, 1), repeat=n*n):
                    if (all(sum(bits[i*n:(i+1)*n]) == d for i in range(n))
                        and all(sum(bits[i*n+j] for i in range(n)) == d for j in range(n))):
                        expected.add(bits)
                actual = [tuple(int(n+j in g.adjacency[i])
                                for i in range(n) for j in range(n))
                          for g in generate_regular_bipartite_graphs(n, d)]
                self.assertEqual(set(actual), expected)
                self.assertEqual(len(actual), len(expected))

    def test_unbalanced_and_invalid(self):
        self.assertFalse(has_perfect_matching(BipartiteGraph({0}, {1, 2}, {0: {1}})))
        with self.assertRaises(ValueError):
            BipartiteGraph({0}, {0})


class ColoringTests(unittest.TestCase):
    def test_bell_and_stirling_counts(self):
        # Independent recurrence S(n,k)=k*S(n-1,k)+S(n-1,k-1).
        row = [1]
        for n in range(10):
            colorings = list(normalized_colorings(n))
            self.assertEqual(len(colorings), len(set(colorings)))
            counts = [0]*(n+1)
            for c in colorings:
                self.assertEqual(normalize(c), c)
                counts[max(c)+1 if c else 0] += 1
            self.assertEqual(counts, row)
            row = [0] + [k*(row[k] if k < len(row) else 0)+row[k-1]
                         for k in range(1, n+2)]

    def test_rainbow_detector_against_edge_subsets(self):
        for n in (2, 3):
            edges = list(product(range(n), repeat=2))
            candidates = [c for c in combinations(range(n*n), n)
                          if len({edges[i][0] for i in c}) == n
                          and len({edges[i][1] for i in c}) == n]
            for colors in normalized_colorings(n*n):
                expected = any(len({colors[i] for i in c}) == n for c in candidates)
                self.assertEqual(has_rainbow_perfect_matching(n, colors), expected)
        self.assertEqual(exhaustive_search(2)[:3], (15, 2, 1))
        self.assertEqual(exhaustive_search(3)[:3], (21147, 4, 87))

    def test_orbit_invariance(self):
        for c in normalized_colorings(4):
            orbit = square_orbit(c, 2)
            self.assertIn(c, orbit)
            self.assertEqual(8 % len(orbit), 0)
            for transformed in orbit:
                self.assertEqual(square_orbit(transformed, 2), orbit)

    def test_bounds(self):
        for call in (lambda: list(normalized_colorings(-1)),
                     lambda: has_rainbow_perfect_matching(3, (0,)),
                     lambda: exhaustive_search(4)):
            with self.assertRaises(ValueError):
                call()


class ProgressionTests(unittest.TestCase):
    def test_interval_against_triples(self):
        for n in range(1, 10):
            expected = {t for t in combinations(range(n), 3) if t[0]+t[2] == 2*t[1]}
            self.assertEqual(set(interval_three_aps(n)), expected)

    def test_cyclic_against_middle_equation(self):
        for n in range(3, 10):
            _, aps = group_three_aps((n,))
            expected = {t for t in combinations(range(n), 3)
                        if any((a+c-2*b) % n == 0 for a, b, c in permutations(t))}
            self.assertEqual(set(aps), expected)
        self.assertEqual(group_three_aps((2, 2, 2))[1], ())

    def test_products_against_middle_equation(self):
        for moduli in ((2, 2), (2, 4), (2, 2, 2)):
            elements, aps = group_three_aps(moduli)
            expected = set()
            for indices in combinations(range(len(elements)), 3):
                if any(all((elements[a][j]+elements[c][j]-2*elements[b][j]) % m == 0
                           for j, m in enumerate(moduli))
                       for a, b, c in permutations(indices)):
                    expected.add(indices)
            self.assertEqual(set(aps), expected)


class AlgorithmBoundaryTests(unittest.TestCase):
    def test_colorful_path(self):
        self.assertIsNone(colorful_path([{1}, {0}], (0, 0), 2))
        self.assertEqual(colorful_path([set()], (0,), 1), (0,))
        self.assertEqual(colorful_path([{1}, {2}, set()], (0, 1, 2), 3), (0, 1, 2))
        with self.assertRaises(ValueError):
            colorful_path([set()], (2,), 2)

    def test_expansion_benchmarks(self):
        for n in range(2, 8):
            complete = [set(range(n))-{v} for v in range(n)]
            self.assertEqual(edge_expansion(complete)[0], n-n//2)
        for n in range(3, 10):
            cycle = [{(v-1)%n, (v+1)%n} for v in range(n)]
            self.assertEqual(edge_expansion(cycle)[0], Fraction(2, n//2))
        adj = [{2, 3}, {2, 3}, {0, 1}, {0, 1}]
        self.assertEqual(walk_total_variation(adj, 4, False),
                         [Fraction(3, 4)] + [Fraction(1, 2)]*4)
        lazy = walk_total_variation(adj, 8)
        self.assertTrue(all(a >= b for a, b in zip(lazy, lazy[1:])))
        self.assertLess(lazy[-1], Fraction(1, 100))


if __name__ == "__main__":
    unittest.main()
