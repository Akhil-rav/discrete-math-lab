"""Polynomial path counts by ordering vertices when they first appear."""
from collections import Counter
from fractions import Fraction
from math import comb, factorial


def support_coefficients(deficits):
    coefficients = Counter()

    def visit(adj, step, fresh_pairs):
        s = len(adj)
        if step == len(deficits):
            # Every pair of simultaneous arrivals has two interchangeable
            # name assignments. All other first appearances fix a name.
            coefficients[s] += factorial(s) // (2**fresh_pairs)
            return
        adj = adj + [0, 0]
        for i in range(s+1):
            for j in range(i+1, s+1 if i < s else s+2):
                if adj[i] & (1 << j) or adj[i] & adj[j]:
                    continue
                size = max(s, j+1)
                adj[i] |= 1 << j
                adj[j] |= 1 << i
                blocked = sum(bool(adj[u] & adj[v]) for u in range(size)
                              for v in range(u+1, size))
                if step + blocked == deficits[step]:
                    visit(adj[:size], step+1, fresh_pairs + (i == s))
                adj[i] ^= 1 << j
                adj[j] ^= 1 << i
    if not deficits or deficits[0] != 0:
        raise ValueError("start from the empty graph")
    visit([], 1, 0)
    return dict(sorted(coefficients.items()))


def evaluate(coefs, n):
    return sum(count * comb(n, s) for s, count in coefs.items())


if __name__ == "__main__":
    for fourth in (6, 5):
        prefix = (0, 1, 3, fourth, 7, 10, 13)
        before = support_coefficients(prefix)
        after = support_coefficients(prefix + (15,))
        print(fourth, before, after)
        n = 6
        print(Fraction(evaluate(after, n), (comb(n, 2)-13)*evaluate(before, n)))
