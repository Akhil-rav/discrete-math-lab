"""Exact finite edge expansion and regular-graph random walks."""

from fractions import Fraction
from itertools import combinations


def validate_graph(adjacency):
    n = len(adjacency)
    if n < 2:
        raise ValueError("Need at least two vertices.")
    for u, row in enumerate(adjacency):
        if len(row) != len(set(row)) or u in row:
            raise ValueError("Need a simple graph.")
        for v in row:
            if v not in range(n) or u not in adjacency[v]:
                raise ValueError("Need symmetric adjacency on 0..n-1.")


def edge_expansion(adjacency):
    """Minimize cut edges / |S| for 0 < |S| <= |V|/2; count cut edges once."""
    validate_graph(adjacency)
    n = len(adjacency)
    best, witness = None, None
    for size in range(1, n//2+1):
        for subset in combinations(range(n), size):
            chosen = set(subset)
            boundary = sum(v not in chosen for u in subset for v in adjacency[u])
            value = Fraction(boundary, size)
            if best is None or value < best:
                best, witness = value, subset
    return best, witness


def walk_total_variation(adjacency, steps, lazy=True):
    """Start at vertex 0; return exact TV distances to uniform at times 0..steps."""
    validate_graph(adjacency)
    n, d = len(adjacency), len(adjacency[0])
    if steps < 0 or d == 0 or any(len(row) != d for row in adjacency):
        raise ValueError("Need steps >= 0 and a positive regular degree.")
    distribution = [Fraction(i == 0) for i in range(n)]
    distances = []
    for time in range(steps+1):
        if sum(distribution) != 1:
            raise RuntimeError("Probability mass changed.")
        distances.append(sum(abs(p-Fraction(1, n)) for p in distribution)/2)
        if time == steps:
            break
        next_distribution = [p/2 if lazy else Fraction(0) for p in distribution]
        for u, row in enumerate(adjacency):
            for v in row:
                next_distribution[v] += distribution[u] / (2*d if lazy else d)
        distribution = next_distribution
    return distances
