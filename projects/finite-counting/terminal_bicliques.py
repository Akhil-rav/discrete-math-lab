"""Exact absorption probabilities for complete bipartite terminal graphs."""
from fractions import Fraction
from functools import cache
from itertools import combinations
from math import comb, factorial


def biclique_probability(a, b):
    if not 1 <= a <= b:
        raise ValueError("use positive part sizes in increasing order")
    masks = range(1 << a)

    @cache
    def finish(counts):
        if counts[-1] == b:
            return Fraction(1)
        open_pairs = sum(counts[m] * (a - m.bit_count()) for m in masks)
        for i, j in combinations(range(a), 2):
            pair = (1 << i) | (1 << j)
            open_pairs += all(not counts[m] or m & pair != pair for m in masks)
        for m in masks:
            for h in range(m):
                if not m & h:
                    open_pairs += counts[m] * counts[h]
        open_pairs += comb(counts[0], 2)
        weight = Fraction()
        for m in masks:
            if counts[m]:
                for i in range(a):
                    dest = m | (1 << i)
                    if dest != m:
                        new = list(counts)
                        new[m] -= 1
                        new[dest] += 1
                        weight += counts[m] * finish(tuple(new))
        return weight / open_pairs

    cuts = comb(a + b, a) // (2 if a == b else 1)
    return cuts * finish((b,) + (0,) * ((1 << a) - 1))


if __name__ == "__main__":
    for n in range(3, 16):
        assert biclique_probability(1, n - 1) == Fraction(
            2**(n - 1) * factorial(n), factorial(2*n - 2))
    for n in range(4, 9):
        print(n, biclique_probability(1, n-1), biclique_probability(2, n-2))
