"""Proper-coloring and rainbow-event oracles independent of the graph recurrence."""

import unittest
from itertools import combinations, permutations, product

from src.rainbow_inclusion_exclusion import (
    chromatic_polynomial,
    evaluate,
    rainbow_union_polynomial,
)


class InclusionExclusionTests(unittest.TestCase):
    def test_every_graph_through_four_vertices(self):
        for n in range(5):
            possible = tuple(combinations(range(n), 2))
            for mask in range(1 << len(possible)):
                edges = [edge for i, edge in enumerate(possible) if mask >> i & 1]
                polynomial = chromatic_polynomial(n, edges)
                self.assertEqual(len(polynomial), n + 1)
                self.assertEqual(polynomial[-1], 1)
                for q in range(5):
                    expected = sum(
                        all(colors[u] != colors[v] for u, v in edges)
                        for colors in product(range(q), repeat=n)
                    )
                    self.assertEqual(evaluate(polynomial, q), expected)

    def test_relabeling_components_and_unused_positions(self):
        edges = ((0, 1), (1, 2), (2, 3), (3, 0), (0, 2))
        expected = chromatic_polynomial(4, edges)
        for p in permutations(range(4)):
            self.assertEqual(
                chromatic_polynomial(4, [(p[u], p[v]) for u, v in edges]), expected
            )
        self.assertEqual(chromatic_polynomial(4, [(0, 1)]), (0, 0, 0, -1, 1))
        counts = rainbow_union_polynomial(4, ((0,),))
        self.assertEqual(counts["union_coefficients"], [0, 0, 0, 0, 1])
        contained = rainbow_union_polynomial(4, ((0,), (0, 1)))
        self.assertEqual(contained["union_coefficients"], [0, 0, 0, 0, 1])
        self.assertEqual(contained["event_subsets"], 3)
        self.assertEqual(contained["distinct_conflict_graphs"], 2)
        self.assertEqual(
            rainbow_union_polynomial(4, ((0, 1),))["union_coefficients"],
            [0, 0, 0, -1, 1],
        )

    def test_all_families_of_two_position_events(self):
        targets = tuple(combinations(range(4), 2))
        for mask in range(1, 1 << len(targets)):
            family = [target for i, target in enumerate(targets) if mask >> i & 1]
            counts = rainbow_union_polynomial(4, family)
            self.assertEqual(counts["event_subsets"], 2 ** len(family) - 1)
            for q in range(1, 5):
                expected = sum(
                    any(colors[u] != colors[v] for u, v in family)
                    for colors in product(range(q), repeat=4)
                )
                self.assertEqual(evaluate(counts["union_coefficients"], q), expected)

    def test_mixed_target_sizes_by_direct_colorings(self):
        family = ((0, 1, 2), (1, 2, 3), (0, 3), (2, 4))
        counts = rainbow_union_polynomial(5, family)
        for q in range(1, 5):
            observed = [0] * len(family)
            successes = 0
            for colors in product(range(q), repeat=5):
                x = sum(
                    len({colors[i] for i in target}) == len(target) for target in family
                )
                successes += x > 0
                for order in range(1, len(family) + 1):
                    observed[order - 1] += sum(1 for _ in combinations(range(x), order))
            self.assertEqual(evaluate(counts["union_coefficients"], q), successes)
            self.assertEqual(
                [evaluate(poly, q) for poly in counts["intersection_sums"]], observed
            )

    def test_invalid_domains(self):
        for call in (
            lambda: chromatic_polynomial(13, []),
            lambda: chromatic_polynomial(2, [(0, 0)]),
            lambda: chromatic_polynomial(2, [(0, 2)]),
            lambda: rainbow_union_polynomial(0, [(0,)]),
            lambda: rainbow_union_polynomial(3, []),
            lambda: rainbow_union_polynomial(3, [()]),
            lambda: rainbow_union_polynomial(3, [(0, 0)]),
            lambda: rainbow_union_polynomial(3, [(0, 3)]),
            lambda: rainbow_union_polynomial(3, [(0, 1), (1, 0)]),
            lambda: rainbow_union_polynomial(5, list(combinations(range(5), 2))),
        ):
            with self.assertRaises(ValueError):
                call()
