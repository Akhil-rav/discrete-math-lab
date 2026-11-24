"""Exact sign certificates for forecasts after a run of unit losses."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, factorial

from forecast_support_dp import path_states, relabel


def core_moves(graph):
    for i, j in combinations(range(len(graph)), 2):
        if graph[i] & (1 << j) or graph[i] & graph[j]:
            continue
        loss = 1
        for a, b in ((i, j), (j, i)):
            for v, row in enumerate(graph):
                if graph[a] & (1 << v) and not graph[b] & row:
                    loss += 1
        yield i, j, loss


def terms(k, history, loss):
    states = list(path_states(history))[-1]
    by_depth = []
    while states:
        j = len(by_depth)
        row = Counter()
        following = Counter()
        for g, count in states.items():
            s = len(g)
            c = k-s+2*j
            internal = 0
            for u, v, delta in core_moves(g):
                internal += delta == loss
                if delta == 1:
                    child = list(g)
                    child[u] |= 1 << v
                    child[v] |= 1 << u
                    following[relabel(child)] += count
            if c < 0:
                continue
            # Forecast for b fresh independent edges has form A+B*b+C*binom(b,2).
            deg = Counter(bits.bit_count() for bits in g)
            constant = internal + c*deg[loss-1] + (comb(c,2) if loss == 1 else 0)
            linear = 2*deg[loss-2] + (2*c if loss == 2 else 0)
            quadratic = 4 if loss == 3 else 0
            weight = Fraction(count * 2**j, factorial(s)*factorial(c))
            for i, value in enumerate((1, constant, linear, quadratic)):
                row[i] += weight * value
        by_depth.append(row)
        states = following
    return by_depth


def path_counts(rows, t):
    p = a = 0
    for j, row in enumerate(rows[:t+1]):
        b = t-j
        p += comb(t,j)*row[0]
        a += comb(t,j)*(row[1]+b*row[2]+comb(b,2)*row[3])
    return p, a


def certify(k, histories, loss):
    left, right = [terms(k, h, loss) for h in histories]
    degree = len(left)+len(right)
    def difference(t):
        p, a = path_counts(left, t)
        q, b = path_counts(right, t)
        return a*q-b*p
    for start in range(50):
        values = [difference(t) for t in range(start, start+degree+1)]
        sign = values[0]
        if not sign:
            raise ValueError(f"equal forecasts at t={start}")
        while values and sign*values[0] >= 0:
            values = [b-a for a,b in zip(values,values[1:])]
        if not values:
            return start, degree
    raise ValueError("no sign certificate in tested range")


if __name__ == "__main__":
    histories = [(0,1,3,u,7,10,13) for u in (6,5)]
    for k in (6,7):
        print(k, certify(k, histories, 2), flush=True)

    from forecast_coefficients import evaluate
    from forecast_support_dp import path_tables

    histories = [(0,1,2,u,6,7,10,13,16,19,22,23,24) for u in (3,4)]
    for k in (8,9):
        assert certify(k, histories, 4) == (3,18)
        for h in histories:
            rows = terms(k, h, 4)
            for t in range(3):
                prefix = h + tuple(h[-1]+i for i in range(1,t+1))
                p, a = path_counts(rows, t)
                n = k+2*t
                direct_p, direct_a = list(path_tables(prefix+(prefix[-1]+4,)))[-2:]
                scale = Fraction(factorial(n), 2**t)
                assert p*scale == evaluate(direct_p, n)
                assert a*scale == evaluate(direct_a, n)
        print(k, "no exceptions for any nonnegative padding length")
