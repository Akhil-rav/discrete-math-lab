"""Closed-form oracles for the exact walk routine; proofs are in the paper.

Finite domain: K(d,d), 1 <= d <= 8, and r disjoint K_d,
2 <= r <= 4, 2 <= d <= 6, all at times 0..12. No sampling.
"""

import unittest
from fractions import Fraction

from src.expansion import walk_total_variation


class WalkFormulaTests(unittest.TestCase):
    def test_complete_bipartite_formulas(self):
        for d in range(1, 9):
            adjacency = [
                set(range(d, 2 * d)) if v < d else set(range(d)) for v in range(2 * d)
            ]
            initial = Fraction(2 * d - 1, 2 * d)
            ordinary = [initial] + [Fraction(1, 2)] * 12
            lazy = [initial] + [Fraction(d - 1, d * 2**t) for t in range(1, 13)]
            self.assertEqual(walk_total_variation(adjacency, 12, False), ordinary)
            self.assertEqual(walk_total_variation(adjacency, 12), lazy)

    def test_disjoint_clique_formula(self):
        for r in range(2, 5):
            for d in range(2, 7):
                adjacency = [
                    set(range((v // d) * d, (v // d + 1) * d)) - {v}
                    for v in range(r * d)
                ]
                factor = Fraction(d - 2, 2 * (d - 1))
                expected = []
                for t in range(13):
                    # Closed distribution, not a second transition simulation.
                    distribution = [
                        (
                            Fraction(1, d) + factor**t * (int(v == 0) - Fraction(1, d))
                            if v < d
                            else Fraction(0)
                        )
                        for v in range(r * d)
                    ]
                    expected.append(
                        sum(abs(p - Fraction(1, r * d)) for p in distribution) / 2
                    )
                observed = walk_total_variation(adjacency, 12)
                self.assertEqual(observed, expected)
                self.assertTrue(all(tv >= Fraction(r - 1, r) for tv in observed))


if __name__ == "__main__":
    unittest.main()
