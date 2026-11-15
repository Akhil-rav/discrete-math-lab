"""Check the direct classification against the older exhaustive population."""

import json
import unittest
from collections import Counter
from itertools import combinations
from pathlib import Path

from src.cube_symmetry import transform_partition
from src.l5_extremizers import extremal_block_families, extremal_partitions
from src.ladders import ladder_actions, ladder_edges

ROOT = Path(__file__).resolve().parents[1]


def endpoint_matchings():
    edges = ladder_edges(5)
    return [
        set(positions)
        for positions in combinations(range(13), 5)
        if len({v for i in positions for v in edges[i]}) == 10
    ]


class DirectL5Tests(unittest.TestCase):
    def test_constructed_families_equal_all_saved_extremizers(self):
        saved = json.loads(
            (ROOT / "results/data/matching_covers.json").read_text(encoding="utf-8")
        )["L5_classification"]
        population = list(extremal_partitions())
        self.assertEqual(len(population), 15)
        self.assertEqual(
            set(population), {tuple(c) for c in saved["extremal_partitions"]}
        )
        shapes = Counter()
        for blocks in extremal_block_families():
            self.assertEqual(sum(map(len, blocks)), len(set().union(*map(set, blocks))))
            self.assertEqual(sum(len(block) - 1 for block in blocks), 3)
            shapes[tuple(sorted(map(len, blocks)))] += 1
        self.assertEqual(shapes, {(4,): 4, (2, 3): 8, (2, 2, 2): 3})
        for colors in population:
            self.assertEqual(len(set(colors)), 10)
            self.assertTrue(
                all(
                    len({colors[i] for i in matching}) < 5
                    for matching in endpoint_matchings()
                )
            )

    def test_two_rung_triple_table(self):
        matchings = endpoint_matchings()
        rows = {
            (0, 1): [3, 5, 3, 4],
            (0, 2): [4, 4, 3, 4],
            (0, 3): [3, 3, 3, 4],
            (0, 4): [5, 4, 4, 5],
            (1, 2): [4, 2, 3, 3],
            (1, 3): [2, 2, 2, 2],
        }
        full_rows = dict(rows)
        for (a, b), values in rows.items():
            full_rows[(4 - b, 4 - a)] = list(reversed(values))
        self.assertEqual(set(full_rows), set(combinations(range(5), 2)))
        for (a, b), values in full_rows.items():
            for start in (5, 9):
                actual = [
                    sum(
                        len({a, b, start + gap} & matching) >= 2
                        for matching in matchings
                    )
                    for gap in range(4)
                ]
                self.assertEqual(actual, values)

    def test_maximum_pair_support_and_completion_table(self):
        matchings = endpoint_matchings()
        U, V, W = {0, 1}, {0, 4}, {3, 4}
        rails = [{5 + i, 9 + i} for i in range(4)]
        X, Y = rails[0], rails[3]
        maximum_pairs = {
            frozenset(pair)
            for pair in combinations(range(13), 2)
            if sum(set(pair) <= matching for matching in matchings) == 3
        }
        self.assertEqual(maximum_pairs, set(map(frozenset, (U, V, W, X, Y))))
        self.assertTrue(
            all(
                sum(set(pair) <= m for m in matchings) <= 3
                for pair in combinations(range(13), 2)
            )
        )
        rows = [
            (U, W, set()),
            (U, X, rails[1]),
            (U, Y, {4}),
            (V, X, rails[3]),
            (V, Y, rails[0]),
            (W, X, {0}),
            (W, Y, rails[2]),
            (X, Y, V),
        ]
        self.assertEqual(
            len(rows), sum(not (a & b) for a, b in combinations((U, V, W, X, Y), 2))
        )
        for first, second, expected in rows:
            residual = [m for m in matchings if not first <= m and not second <= m]
            self.assertTrue(residual)
            self.assertEqual(set.intersection(*residual) - first - second, expected)

    def test_orbits_have_the_proved_shapes_and_sizes(self):
        saved = json.loads(
            (ROOT / "results/data/matching_covers.json").read_text(encoding="utf-8")
        )["L5_classification"]
        remaining = set(extremal_partitions())
        for record in saved["symmetry_classes"]:
            representative = tuple(record["representative"])
            orbit = {
                transform_partition(representative, action)
                for action in ladder_actions(5)
            }
            self.assertEqual(len(orbit), record["orbit_size"])
            self.assertTrue(orbit <= remaining)
            remaining -= orbit
        self.assertFalse(remaining)


if __name__ == "__main__":
    unittest.main()
