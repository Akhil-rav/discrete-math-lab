"""Boundary and construction checks; broader exact searches live in the experiment."""
import unittest
from itertools import product
from math import comb

from src.cycle_unions import cycle_union, extremal_partitions


class CycleUnionTests(unittest.TestCase):
    def test_domain_and_smallest_extremizers(self):
        for lengths in ((), (1,), (2, -3), (2, 2.0), (True,)):
            with self.assertRaises(ValueError):
                cycle_union(lengths)
        self.assertEqual(list(extremal_partitions((2,))), [(0, 1, 0, 1)])
        self.assertEqual(set(extremal_partitions((2, 2))),
                         {(0, 1, 0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5, 4, 5)})

    def test_mixed_components_and_parameter_order(self):
        for lengths in ((2, 3, 4), (4, 3, 2), (3, 3), (2, 2, 2)):
            edges, local = cycle_union(lengths)
            population = list(extremal_partitions(lengths))
            self.assertEqual(len(population), len(set(population)))
            self.assertEqual(len(population), sum(comb(n, 2)**2 for n in lengths))
            for colors in population:
                self.assertEqual(len(set(colors)), len(edges)-2)
                for choices in product(*local):
                    selected = [i for matching in choices for i in matching]
                    self.assertLess(len({colors[i] for i in selected}), len(selected))
