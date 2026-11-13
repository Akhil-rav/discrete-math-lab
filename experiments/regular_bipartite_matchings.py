"""Exhaustive small-case verification for regular bipartite graphs.

Known theorem:
Every finite d-regular bipartite graph with d >= 1 has a perfect matching.

This script does NOT prove the theorem. It exhaustively generates every
labeled d-regular bipartite graph with n vertices on each side for n <= 5
and checks that the matching algorithm finds a perfect matching.

Run from the repository root:

    python -m experiments.regular_bipartite_matchings
"""

from __future__ import annotations

from itertools import combinations, product
from typing import Iterable

from src.bipartite_graph import BipartiteGraph
from src.matchings import has_perfect_matching


def generate_regular_bipartite_graphs(
    n: int, d: int
) -> Iterable[BipartiteGraph]:
    """Generate all labeled d-regular bipartite graphs with n+n vertices.

    Left vertices are 0, ..., n-1 and right vertices are n, ..., 2n-1.
    Each left vertex chooses d neighbors. We keep exactly those choices
    for which every right vertex also has degree d.
    """

    if not 0 <= d <= n:
        raise ValueError("Need 0 <= d <= n.")

    left = set(range(n))
    right = set(range(n, 2 * n))
    possible_rows = list(combinations(range(n), d))

    for rows in product(possible_rows, repeat=n):
        right_degrees = [0] * n

        for row in rows:
            for v in row:
                right_degrees[v] += 1

        if not all(degree == d for degree in right_degrees):
            continue

        adjacency = {
            u: {n + v for v in rows[u]}
            for u in range(n)
        }

        yield BipartiteGraph(
            left=set(left),
            right=set(right),
            adjacency=adjacency,
        )


def verify_case(n: int, d: int) -> tuple[int, int]:
    """Return (graphs_checked, failures)."""

    checked = 0
    failures = 0

    for graph in generate_regular_bipartite_graphs(n, d):
        checked += 1
        if not has_perfect_matching(graph):
            failures += 1

    return checked, failures


def main() -> None:
    total = 0
    print("n  d  graphs checked  failures")
    print("-" * 33)

    for n in range(1, 6):
        for d in range(1, n + 1):
            checked, failures = verify_case(n, d)
            total += checked
            print(f"{n:<2} {d:<2} {checked:<15} {failures}")

            # Any failure would contradict the known theorem, so stop loudly.
            assert failures == 0

    print("-" * 33)
    print(f"Total graphs checked: {total}")


if __name__ == "__main__":
    main()
