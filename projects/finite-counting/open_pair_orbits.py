"""Exact history laws with isomorphic states grouped before each move."""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import cache
from itertools import combinations, permutations

from open_pair_memory import observations


def orbit_laws(n):
    edges = list(combinations(range(n), 2))
    index = {edge: i for i, edge in enumerate(edges)}
    relabel = [[1 << index[tuple(sorted((p[u], p[v])))] for u, v in edges]
               for p in permutations(range(n))]
    reps = {}

    def representative(mask):
        if mask not in reps:
            present = [i for i in range(len(edges)) if mask & (1 << i)]
            for row in relabel:
                reps[sum(row[i] for i in present)] = mask
        return reps[mask]

    @cache
    def successors(mask):
        neighbors = [set() for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            if mask & (1 << i):
                neighbors[u].add(v)
                neighbors[v].add(u)
        return Counter(representative(mask | (1 << i)) for i, (u, v) in enumerate(edges)
                       if v not in neighbors[u] and neighbors[u].isdisjoint(neighbors[v]))

    states = {(0, (len(edges),)): 1}
    while states:
        paths = defaultdict(Counter)
        following = Counter()
        for (graph, history), weight in states.items():
            for child, choices in successors(graph).items():
                q = sum(successors(child).values())
                paths[history][q] += weight * choices
                if q:
                    following[child, history + (q,)] += weight * choices
        yield {h: {q: Fraction(count, sum(row.values())) for q, count in row.items()}
               for h, row in paths.items()}
        states = following


def longest_witness(laws):
    best = None
    for size in range(1, len(next(iter(laws), ()))):
        seen = {}
        for h, law in laws.items():
            suffix = h[-size:]
            if suffix in seen and law != laws[seen[suffix]]:
                best = size, seen[suffix], h
                break
            seen[suffix] = h
        else:
            break
    return best


if __name__ == "__main__":
    direct = list(observations(6, 9))
    grouped = list(orbit_laws(6))
    assert grouped == [layer for layer in direct if layer]
    for time, laws in enumerate(orbit_laws(7)):
        witness = longest_witness(laws)
        if witness:
            size, a, b = witness
            print(time, size, a, laws[a], b, laws[b])
