"""Compare color-mask DP with permutation search on every graph of order <=4.

Enumerate every k-color assignment for 1 <= k <= n, so the measured success
probabilities are exact rational numbers, not estimates from random trials.
Run: python -m experiments.color_coding_small_cases
"""

import json
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial

from src.color_coding import colorful_path


def run():
    rows = []
    for n in range(1, 5):
        edges = tuple(combinations(range(n), 2))
        totals = {k: {"assignments_checked": 0, "graphs_with_path": 0,
                      "minimum_success": Fraction(1)} for k in range(1, n+1)}
        for mask in range(1 << len(edges)):
            adj = [set() for _ in range(n)]
            for i, (u, v) in enumerate(edges):
                if mask & (1 << i):
                    adj[u].add(v)
                    adj[v].add(u)
            for k, record in totals.items():
                paths = [p for p in permutations(range(n), k)
                         if all(v in adj[u] for u, v in zip(p, p[1:]))]
                successes = 0
                for colors in product(range(k), repeat=n):
                    expected = any(len({colors[v] for v in p}) == k for p in paths)
                    witness = colorful_path(adj, colors, k)
                    if (witness is not None) != expected:
                        raise RuntimeError("DP disagrees with permutation oracle.")
                    if witness is not None:
                        if (len(witness) != k or len(set(witness)) != k
                            or len({colors[v] for v in witness}) != k
                            or not all(v in adj[u] for u, v in zip(witness, witness[1:]))):
                            raise RuntimeError("Invalid path witness.")
                    successes += expected
                    record["assignments_checked"] += 1
                if paths:
                    record["graphs_with_path"] += 1
                    probability = Fraction(successes, k**n)
                    if probability < Fraction(factorial(k), k**k):
                        raise RuntimeError("Violates fixed-path success bound.")
                    record["minimum_success"] = min(record["minimum_success"], probability)
        for k, record in totals.items():
            record["minimum_success"] = str(record["minimum_success"])
            rows.append({"n": n, "k_vertices": k, "graphs_checked": 1 << len(edges),
                         **record})
    return rows


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
