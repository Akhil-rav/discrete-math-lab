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


def prescribed_forecast(n, history):
    successors = orbit_successors(n)
    states = Counter({0: 1})
    if history[0] != n*(n-1)//2:
        raise ValueError("expected an empty initial graph")
    for observed in history[1:]:
        following = Counter()
        for graph, weight in states.items():
            for child, ways in successors(graph).items():
                if sum(successors(child).values()) == observed:
                    following[child] += weight*ways
        states = following
    result = Counter()
    for graph, weight in states.items():
        for child, ways in successors(graph).items():
            result[sum(successors(child).values())] += weight*ways
    return {q: Fraction(w, sum(result.values())) for q, w in result.items()}


if __name__ == "__main__":
    from forecast_coefficients import evaluate
    from forecast_support_dp import path_tables

    from argparse import ArgumentParser

    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--order", type=int, choices=(9, 10, 11), default=9)
    n = parser.parse_args().order
    total = n*(n-1)//2
    if n == 11:
        first, second = [(55,54,53,u,49,45,41,36,33,29,27,25,23,22,21,20,19,18,
                          17,16,15,8,4,3,2) for u in (52,51)]
        next_count = 0
        a, b = [prescribed_forecast(n, h).get(0, 0) for h in (first, second)]
    else:
        first, second, (next_count, a, b) = seek(n)
    for observed, prob in ((first, a), (second, b)):
        centered = tuple(total-q for q in observed) + (total-next_count,)
        prefix, full = list(path_tables(centered, max_support=n))[-2:]
        checked = Fraction(evaluate(full, n), observed[-1]*evaluate(prefix, n))
        assert checked == prob
        print(observed, next_count, checked)
    assert first[4:] == second[4:] and a != b
    assert len(first[4:])+1 == {9: 14, 10: 18, 11: 22}[n]
