"""Count full arrival permutations yielding a fixed graph on a small vertex set."""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial, prod

from terminal_bicliques import biclique_probability


def terminal_probability(n, target):
    edges = set(combinations(range(n), 2))
    target = sorted(target)
    index = {edge: i for i, edge in enumerate(target)}
    witnesses = []
    for a, b in edges:
        paths = []
        for c in range(n):
            left = tuple(sorted((a, c)))
            right = tuple(sorted((b, c)))
            if left in index and right in index:
                paths.append((index[left], index[right]))
        if (a, b) in index:
            if paths:
                return Fraction(0)
        elif paths:
            witnesses.append(paths)
        else:
            return Fraction(0)

    total = 0
    m = len(target)
    for ranks in permutations(range(1, m + 1)):
        thresholds = sorted((min(max(ranks[x], ranks[y]) for x, y in paths)
                             for paths in witnesses), reverse=True)
        total += prod(m - rank + 1 + j for j, rank in enumerate(thresholds))
    return Fraction(total, factorial(len(edges)))


if __name__ == "__main__":
    for n in range(3, 7):
        for a in range(1, n // 2 + 1):
            target = list((i, j) for i in range(a) for j in range(a, n))
            cuts = comb(n, a) // (2 if 2*a == n else 1)
            assert cuts * terminal_probability(n, target) == biclique_probability(a, n-a)
    pentagon = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]
    p = terminal_probability(5, pentagon)
    assert 12*p + biclique_probability(1, 4) + biclique_probability(2, 3) == 1
    print("All bipartition sizes checked at orders 3..6. Fixed pentagon:", p)
