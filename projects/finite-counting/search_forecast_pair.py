"""Search pairs of histories exactly, prioritizing the longest possible suffix."""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import gcd

from open_pair_orbits import orbit_successors


def normalized(weights):
    divisor = gcd(*weights.values())
    return tuple(sorted((state, w // divisor) for state, w in weights.items()))


def seek(n):
    successors = orbit_successors(n)
    end = (n-1)**2//4

    @lru_cache(maxsize=20000)
    def advance(weights):
        following = defaultdict(Counter)
        for g, w in weights:
            for child, choices in successors(g).items():
                following[sum(successors(child).values())][child] += w*choices
        return {q: (sum(row.values()), normalized(row)) for q, row in following.items()}

    def search(left, right, time):
        if left == right:
            return None
        a, b = advance(left), advance(right)
        if time == end:
            total_a = sum(v[0] for v in a.values())
            total_b = sum(v[0] for v in b.values())
            for q in sorted(a.keys() | b.keys()):
                p1 = Fraction(a.get(q, (0,))[0], total_a)
                p2 = Fraction(b.get(q, (0,))[0], total_b)
                if p1 != p2:
                    return (), (q, p1, p2)
            return None
        for q in sorted(a.keys() & b.keys()):
            if q <= end-time-1:
                continue
            result = search(a[q][1], b[q][1], time+1)
            if result is not None:
                suffix, forecasts = result
                return (q,) + suffix, forecasts
        return None

    prefixes = {((n*(n-1)//2),): ((0, 1),)}
    for _ in range(3):
        prefixes = {history + (q,): child for history, weights in prefixes.items()
                    for q, (_, child) in advance(weights).items() if q}
    for (ha, left), (hb, right) in combinations(prefixes.items(), 2):
        if ha[-1] != hb[-1]:
            result = search(left, right, 3)
            if result:
                suffix, forecasts = result
                return ha + suffix, hb + suffix, forecasts


if __name__ == "__main__":
    from forecast_coefficients import evaluate
    from forecast_support_dp import path_tables

    first, second, (next_count, a, b) = seek(9)
    for observed, prob in ((first, a), (second, b)):
        centered = tuple(36-q for q in observed) + (36-next_count,)
        prefix, full = list(path_tables(centered, max_support=9))[-2:]
        checked = Fraction(evaluate(full, 9), observed[-1]*evaluate(prefix, 9))
        assert checked == prob
        print(observed, next_count, checked)
    assert first[-13:] == second[-13:] and a != b
