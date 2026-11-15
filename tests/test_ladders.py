"""Independent graph and named-color checks for the finite ladder study."""

import json
import unittest
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path

from src.ladders import bipartite_edges, ladder_actions, ladder_edges, ladder_matchings
from src.rainbow_inclusion_exclusion import evaluate

ROOT = Path(__file__).resolve().parents[1]


class LadderTests(unittest.TestCase):
    def test_graphs_matchings_and_bipartition(self):
        for k, count in ((2, 2), (3, 3), (4, 5)):
            edges = ladder_edges(k)
            self.assertEqual(len(edges), 3 * k - 2)
            subsets = {
                positions
                for positions in combinations(range(len(edges)), k)
                if len({v for i in positions for v in edges[i]}) == 2 * k
            }
            self.assertEqual(set(ladder_matchings(k)), subsets)
            self.assertEqual(len(subsets), count)
            converted = bipartite_edges(k)
            for i, j in combinations(range(len(edges)), 2):
                self.assertEqual(
                    bool(set(edges[i]) & set(edges[j])),
                    converted[i][0] == converted[j][0]
                    or converted[i][1] == converted[j][1],
                )

    def test_full_automorphisms_by_vertex_bijections(self):
        for k, order in ((2, 8), (3, 4), (4, 4)):
            edges = ladder_edges(k)
            index = {frozenset(edge): i for i, edge in enumerate(edges)}
            actions = set()
            for mapping in permutations(range(2 * k)):
                image = [frozenset((mapping[u], mapping[v])) for u, v in edges]
                if all(edge in index for edge in image):
                    actions.add(tuple(index[edge] for edge in image))
            self.assertEqual(len(actions), order)
            self.assertEqual(set(ladder_actions(k)), actions)

    def test_upper_bound_incidence_numbers(self):
        for k, pair_cap, triple_cap in ((3, 1, 5), (4, 2, 8)):
            matchings = [set(m) for m in ladder_matchings(k)]
            m = len(ladder_edges(k))
            self.assertEqual(
                max(
                    sum(set(pair) <= matching for matching in matchings)
                    for pair in combinations(range(m), 2)
                ),
                pair_cap,
            )
            incidences = [
                sum(i in matching for matching in matchings) for i in range(m)
            ]
            self.assertEqual(sum(sorted(incidences, reverse=True)[:3]), triple_cap)
            self.assertLess(2 * pair_cap, len(matchings))
            self.assertLess(triple_cap, 2 * len(matchings))
            pairs = ((0, 1), (3, 5), (4, 6)) if k == 3 else ((0, 3), (4, 7), (6, 9))
            self.assertTrue(
                all(
                    any(set(pair) <= matching for pair in pairs)
                    for matching in matchings
                )
            )

    def test_saved_probabilities_against_all_named_colorings(self):
        data = json.loads((ROOT / "results/data/ladder_matchings.json").read_text())
        for k, q_max in ((2, 4), (3, 3), (4, 2)):
            host = data["hosts"][f"L{k}"]
            edges = ladder_edges(k)
            # Matchings come from endpoint coverage, independently of column recursion.
            matchings = [
                s
                for s in combinations(range(len(edges)), k)
                if len({v for i in s for v in edges[i]}) == 2 * k
            ]
            for q in range(1, q_max + 1):
                count = sum(
                    any(
                        len({colors[i] for i in matching}) == k
                        for matching in matchings
                    )
                    for colors in product(range(q), repeat=len(edges))
                )
                exact = Fraction(count, q ** len(edges))
                self.assertEqual(
                    exact, Fraction(host["palettes"][q - 1]["rainbow_probability"])
                )
                self.assertEqual(
                    count,
                    evaluate(host["inclusion_exclusion"]["union_coefficients"], q),
                )

    def test_partition_coverage_and_saved_extremizers(self):
        data = json.loads((ROOT / "results/data/ladder_matchings.json").read_text())
        for k, best, extremal in ((2, 2, 1), (3, 4, 27), (4, 7, 25)):
            host = data["hosts"][f"L{k}"]
            row = [1]
            for _ in ladder_edges(k):
                row = [0] + [
                    (j * row[j] if j < len(row) else 0) + row[j - 1]
                    for j in range(1, len(row) + 1)
                ]
            self.assertEqual(host["total_partitions"], sum(row))
            self.assertEqual(host["maximum_avoiding_colors"], best)
            population = {tuple(c) for c in host["extremal_partitions"]}
            self.assertEqual(len(population), extremal)
            self.assertEqual(
                sum(c["orbit_size"] for c in host["symmetry_classes"]), extremal
            )
            for colors in population:
                self.assertEqual(len(set(colors)), best)
                self.assertTrue(
                    all(
                        len({colors[i] for i in matching}) < k
                        for matching in host["matchings"]
                    )
                )

    def test_domain(self):
        for value in (0, 1, 6, 2.5, "3", None):
            with self.assertRaises(ValueError):
                ladder_edges(value)


if __name__ == "__main__":
    unittest.main()
