"""Check the witness table and the exact minimum test family on five columns."""

import unittest
from collections import Counter
from math import comb

from experiments.matching_covers import deficit_partitions
from src.ladders import ladder_matchings


class TestLadderFamilies(unittest.TestCase):
    def test_witness_table(self):
        # Edge indices 0..4 are rungs, 5..8 upper rails, 9..12 lower rails.
        table = {
            (0,): ((0, 4, 7), (8, 12)),
            (1,): ((0, 1, 8), (5, 9)),
            (0, 2): ((0, 2, 4, 8),),
            (0, 3): ((0, 1, 6), (4, 5)),
        }
        for expected, blocks in table.items():
            survivors = []
            for matching in ladder_matchings(5):
                if all(len(set(matching).intersection(b)) <= 1 for b in blocks):
                    survivors.append(tuple(e - 5 for e in matching if 5 <= e < 9))
            self.assertEqual(survivors, [expected])

    def test_every_candidate_list(self):
        matchings = ladder_matchings(5)
        populations = Counter()
        for colors in deficit_partitions(13, 3):
            mask = sum(
                1 << i for i, matching in enumerate(matchings)
                if len({colors[e] for e in matching}) == 5
            )
            populations[mask] += 1
        # Count partitions of shapes (4), (3,2), and (2,2,2).
        total = comb(13, 4) + comb(13, 3) * comb(10, 2) + 15 * comb(13, 6)
        self.assertEqual(sum(populations.values()), total)
        self.assertEqual(populations[0], 15)
        full = (1 << len(matchings)) - 1
        all_rungs = matchings.index(tuple(range(5)))
        valid = {
            mask for mask in range(full + 1)
            if all(mask & witness for witness in populations if witness)
        }
        self.assertEqual(valid, {full, full ^ (1 << all_rungs)})
