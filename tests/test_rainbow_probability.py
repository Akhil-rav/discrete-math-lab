"""Named-color oracles check partition weights and overlap-based moments."""
import json
import unittest
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

from experiments.random_rainbow import run
from src.rainbow_probability import falling_factorial, matching_moments, rainbow_probability

ROOT=Path(__file__).resolve().parents[1]


def matchings_by_subsets(n, edges):
    return [m for m in combinations(range(len(edges)),n)
            if len({edges[i][0] for i in m}) == n
            and len({edges[i][1] for i in m}) == n]


class RainbowProbabilityTests(unittest.TestCase):
    def test_named_colorings_and_moments(self):
        hosts=json.loads((ROOT/'results/data/sparse_rainbow.json').read_text())
        for name,max_q in (('C4',5),('C6',4),('2C4',4)):
            h=hosts[name]
            m=len(h['edges'])
            matchings=matchings_by_subsets(h['n_per_side'],h['edges'])
            histogram={int(k):v for k,v in h['avoiding_histogram'].items()}
            for q in range(1,max_q+1):
                successes=total_x=total_x2=0
                for colors in product(range(q),repeat=m):
                    # Pair equalities form an oracle distinct from the main set test.
                    x=sum(all(colors[a] != colors[b] for a,b in combinations(M,2))
                          for M in matchings)
                    successes += x > 0
                    total_x += x
                    total_x2 += x*x
                self.assertEqual(rainbow_probability(m,histogram,q),Fraction(successes,q**m))
                self.assertEqual(matching_moments(matchings,q),
                                 (Fraction(total_x,q**m),Fraction(total_x2,q**m)))

    def test_cycles_from_independent_matching_events(self):
        data=run()
        for name,n in (('C4',2),('C6',3),('C8',4)):
            for row in data['hosts'][name]['palettes']:
                q=row['q']
                single=Fraction(falling_factorial(q,n),q**n)
                self.assertEqual(Fraction(row['rainbow_probability']),1-(1-single)**2)
        reference=json.loads((ROOT/'results/data/random_rainbow.json').read_text())
        self.assertEqual(data,reference)

    def test_bounds_and_input_contracts(self):
        data=run()
        self.assertEqual(data['cube_large_palette_limit'],data['hosts']['cube']['extremal_partitions'])
        for host in data['hosts'].values():
            for row in host['palettes']:
                p=Fraction(row['rainbow_probability'])
                self.assertLessEqual(Fraction(row['second_moment_lower']),p)
                self.assertLessEqual(p,Fraction(row['union_upper']))
                if row['q'] < host['matching_size']:
                    self.assertEqual(p,0)
        self.assertEqual(falling_factorial(0,0),1)
        self.assertEqual(falling_factorial(2,3),0)
        for call in (lambda:falling_factorial(-1,2),
                     lambda:rainbow_probability(4,{1:1},0),
                     lambda:rainbow_probability(2,{1:10},2),
                     lambda:matching_moments([],3),
                     lambda:matching_moments([(0,1),(0,1)],3),
                     lambda:matching_moments([(0,),(0,1)],3)):
            with self.assertRaises(ValueError): call()

    def test_pair_overlap_moments_by_named_colors(self):
        # Every overlap of two distinct rainbow events on four positions.
        for shared in range(4):
            a=tuple(range(4))
            b=tuple(range(shared))+tuple(range(4,8-shared))
            for q in range(1,5):
                total_x=total_x2=0
                for colors in product(range(q),repeat=8-shared):
                    x=sum(all(colors[u] != colors[v] for u,v in combinations(M,2))
                          for M in (a,b))
                    total_x += x
                    total_x2 += x*x
                denominator=q**(8-shared)
                self.assertEqual(matching_moments((a,b),q),
                                 (Fraction(total_x,denominator),Fraction(total_x2,denominator)))


if __name__ == '__main__':
    unittest.main()
