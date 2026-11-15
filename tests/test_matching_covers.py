"""Finite oracles for the cover reduction, certificates, and L5 classification."""

import json
import unittest
from collections import Counter
from copy import deepcopy
from itertools import combinations, permutations, product
from pathlib import Path

from experiments.matching_covers import deficit_partitions
from experiments.rainbow_complete_bipartite import normalized_colorings
from src.ladders import ladder_actions, ladder_edges, ladder_matchings
from src.matching_cover_certificate import check_certificate
from src.matching_covers import minimum_cover

ROOT = Path(__file__).resolve().parents[1]


class MatchingCoverTests(unittest.TestCase):
    def test_all_pair_event_families_on_four_positions(self):
        pairs = tuple(combinations(range(4), 2))
        for mask in range(1, 1 << len(pairs)):
            targets = [pair for j, pair in enumerate(pairs) if mask >> j & 1]
            expected = max(
                len(set(colors))
                for colors in normalized_colorings(4)
                if all(len({colors[i] for i in target}) < 2 for target in targets)
            )
            result = minimum_cover(4, targets)
            self.assertEqual(result["maximum_avoiding_colors"], expected)
            self.assertTrue(check_certificate(4, targets, result))

    def test_mixed_targets_and_overlapping_cover_blocks(self):
        for targets in (
            ((0, 1), (1, 2)),
            ((0, 1, 2), (1, 2, 3)),
            ((0, 1), (0, 1, 2), (0, 2, 3)),
        ):
            result = minimum_cover(4, targets)
            expected = max(
                len(set(colors))
                for colors in normalized_colorings(4)
                if all(
                    len({colors[i] for i in target}) < len(target) for target in targets
                )
            )
            self.assertEqual(result["maximum_avoiding_colors"], expected)
            self.assertTrue(check_certificate(4, targets, result))
        result = minimum_cover(3, ((0, 1), (1, 2)))
        self.assertEqual(result["witness"], [0, 0, 0])
        self.assertEqual(len(result["cover_blocks"]), 2)
        self.assertTrue(set(result["cover_blocks"][0]) & set(result["cover_blocks"][1]))

    def test_altered_certificates_are_rejected(self):
        targets = ((0, 1), (1, 2))
        good = minimum_cover(3, targets)
        for change in ("cost", "block", "omit", "witness", "optimum", "states"):
            bad = deepcopy(good)
            if change == "cost":
                bad["cheapest_blocks"][0]["cost"] += 1
            elif change == "block":
                bad["cheapest_blocks"][0]["coverage"] = 0
            elif change == "omit":
                bad["cheapest_blocks"].pop()
            elif change == "witness":
                bad["witness"] = [0, 1, 2]
            elif change == "optimum":
                bad["minimum_deficit"] = 1
            else:
                bad["remaining_costs"].pop()
            with self.assertRaises(ValueError):
                check_certificate(3, targets, bad)

    def test_deficit_iterator_against_full_partitions(self):
        for m in range(2, 7):
            for deficit in range(min(3, m - 1) + 1):
                expected = {
                    p for p in normalized_colorings(m) if m - len(set(p)) == deficit
                }
                result = list(deficit_partitions(m, deficit))
                self.assertEqual(len(result), len(expected))
                self.assertEqual(set(result), expected)

    def test_l5_extremizers_by_block_shapes(self):
        data = json.loads((ROOT / "results/data/matching_covers.json").read_text())
        targets = [set(target) for target in ladder_matchings(5)]
        positions = set(range(13))

        def families():
            for block in combinations(range(13), 4):
                yield (block,)
            for triple in combinations(range(13), 3):
                for pair in combinations(sorted(positions - set(triple)), 2):
                    yield (triple, pair)
            for pairs in combinations(tuple(combinations(range(13), 2)), 3):
                if len(set().union(*map(set, pairs))) == 6:
                    yield pairs

        total = 0
        extremal = set()
        shapes = Counter()
        for blocks in families():
            total += 1
            if not all(
                any(len(target.intersection(block)) >= 2 for block in blocks)
                for target in targets
            ):
                continue
            colors = list(range(13))
            for block in blocks:
                for i in block:
                    colors[i] = block[0]
            names = {}
            extremal.add(tuple(names.setdefault(c, len(names)) for c in colors))
            shapes[tuple(sorted(map(len, blocks)))] += 1
        self.assertEqual(total, 39325)
        self.assertEqual(
            extremal,
            {tuple(c) for c in data["L5_classification"]["extremal_partitions"]},
        )
        self.assertEqual(shapes, {(4,): 4, (2, 3): 8, (2, 2, 2): 3})

    def test_l5_automorphisms_by_degree_preserving_bijections(self):
        edges = ladder_edges(5)
        index = {frozenset(edge): i for i, edge in enumerate(edges)}
        degrees = Counter(v for edge in edges for v in edge)
        corners = [v for v in range(10) if degrees[v] == 2]
        inner = [v for v in range(10) if degrees[v] == 3]
        actions = set()
        for a, b in product(permutations(corners), permutations(inner)):
            mapping = dict(zip(corners + inner, a + b))
            image = [frozenset((mapping[u], mapping[v])) for u, v in edges]
            if all(edge in index for edge in image):
                actions.add(tuple(index[edge] for edge in image))
        self.assertEqual(actions, set(ladder_actions(5)))
        self.assertEqual(len(actions), 4)

    def test_invalid_problems(self):
        for edge_count, targets in (
            (1, ((0, 1),)),
            (14, ((0, 1),)),
            (3, ()),
            (3, ((0,),)),
            (3, ((0, 1), (1, 0))),
            (3, ((0, 3),)),
            (3, ((0, 0, 1),)),
            (3, ((0, True),)),
        ):
            with self.assertRaises(ValueError):
                minimum_cover(edge_count, targets)

    def test_ladder_incidence_bounds_by_gap_subsets(self):
        counts = [1, 1]
        for _ in range(2, 11):
            counts.append(counts[-1] + counts[-2])
        for k in range(3, 11):
            # A subset of nonadjacent gaps specifies all two-column tiles.
            matchings = []
            for gaps in range(1 << (k - 1)):
                if gaps & (gaps << 1):
                    continue
                covered = set()
                matching = set()
                for i in range(k - 1):
                    if gaps >> i & 1:
                        covered.update((i, i + 1))
                        matching.update((k + i, 2 * k - 1 + i))
                matching.update(set(range(k)) - covered)
                matchings.append(matching)
            self.assertEqual(len(matchings), counts[k])
            m = 3 * k - 2
            self.assertTrue(
                all(
                    sum(i in target for target in matchings) <= counts[k - 1]
                    for i in range(m)
                )
            )
            self.assertTrue(
                all(
                    sum(set(pair) <= target for target in matchings) <= counts[k - 2]
                    for pair in combinations(range(m), 2)
                )
            )
            blocks = ({0, 1, k + 1}, {k, 2 * k - 1})
            self.assertTrue(
                all(
                    any(len(target & block) >= 2 for block in blocks)
                    for target in matchings
                )
            )
            if k >= 4:
                self.assertLess(3 * counts[k - 1], 2 * counts[k])


if __name__ == "__main__":
    unittest.main()
