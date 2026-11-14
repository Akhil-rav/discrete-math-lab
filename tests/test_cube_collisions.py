"""Bit-mask and color-counter oracles for the cube's collision certificates."""
import json
import unittest
from collections import Counter
from itertools import combinations
from pathlib import Path

from experiments.cube_collision_audit import certificate, run
from src.cube_symmetry import CUBE_EDGES

ROOT = Path(__file__).resolve().parents[1]


def matching_subsets():
    return [m for m in combinations(range(12),4)
            if len({CUBE_EDGES[i][0] for i in m}) == 4
            and len({CUBE_EDGES[i][1] for i in m}) == 4]


class CollisionTests(unittest.TestCase):
    def test_all_subset_capacities_by_bit_masks(self):
        data=run()
        masks=[sum(1<<i for i in m) for m in matching_subsets()]
        histograms={s:Counter() for s in range(1,13)}
        for mask in range(1,1<<12):
            blocked=sum((mask & m).bit_count() >= 2 for m in masks)
            histograms[mask.bit_count()][blocked] += 1
        self.assertEqual(sum(sum(h.values()) for h in histograms.values()),4095)
        for record in data['subset_sizes']:
            expected={str(k):v for k,v in sorted(histograms[record['size']].items())}
            self.assertEqual(record['coverage_histogram'],expected)
        reference=json.loads((ROOT/'results/data/cube_collisions.json').read_text())
        self.assertEqual(data,reference)

    def test_balance_from_matching_color_counters(self):
        data=json.loads((ROOT/'results/data/cube_classification.json').read_text())
        matchings=matching_subsets()
        balances=Counter()
        for cls in data['classes']:
            for colors in cls['members']:
                profiles=[Counter(colors[i] for i in m) for m in matchings]
                q=[sum(count>=2 for count in p.values()) for p in profiles]
                sizes=Counter(colors)
                unused=sum(2*(size-1)-sum(p[color]>=2 for p in profiles)
                           for color,size in sizes.items())
                overlap=sum(count-1 for count in q)
                result=certificate(colors,matchings)
                self.assertEqual(result['matching_obstruction_counts'],q)
                self.assertEqual((result['unused_capacity'],result['overlap']),
                                 (unused,overlap))
                self.assertTrue(all(count>=1 for count in q))
                self.assertEqual(unused+overlap,1)
                balances[unused,overlap] += 1
        self.assertEqual(balances,{(1,0):150,(0,1):24})
        rainbow=certificate(tuple(range(12)),matchings)
        self.assertEqual(rainbow['rainbow_matchings'],9)
        self.assertEqual(rainbow['unused_capacity'],0)
        self.assertEqual(rainbow['overlap'],0)


if __name__ == '__main__':
    unittest.main()
