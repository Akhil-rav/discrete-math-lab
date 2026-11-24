"""Exact history laws with isomorphic states grouped before each move."""
from argparse import ArgumentParser
from collections import Counter, defaultdict
from fractions import Fraction
from functools import cache
from itertools import combinations, permutations, product

from open_pair_memory import observations


def orbit_laws(n):
    edges = list(combinations(range(n), 2))

    @cache
    def representative(mask):
        neighbors = [set() for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            if mask & (1 << i):
                neighbors[u].add(v)
                neighbors[v].add(u)
        groups = defaultdict(list)
        for v, adjacent in enumerate(neighbors):
            key = (len(adjacent), tuple(sorted(len(neighbors[w]) for w in adjacent)))
            groups[key].append(v)
        orders = []
        for key in sorted(groups):
            group = groups[key]
            # Permuting false twins leaves every adjacency unchanged.
            if all(neighbors[v] == neighbors[group[0]] for v in group):
                orders.append([group])
            else:
                orders.append(permutations(group))
        best = None
        for blocks in product(*orders):
            order = [v for block in blocks for v in block]
            code = sum(1 << i for i, (u, v) in enumerate(edges)
                       if order[v] in neighbors[order[u]])
            if best is None or code < best:
                best = code
        return best

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
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--order", type=int, choices=(7, 8), default=7)
    order = parser.parse_args().order
    direct = list(observations(6, 9))
    grouped = list(orbit_laws(6))
    assert grouped == [layer for layer in direct if layer]
    memory = 1
    for time, laws in enumerate(orbit_laws(order)):
        witness = longest_witness(laws)
        if witness:
            size, a, b = witness
            memory = max(memory, size + 1)
            print(time, size, a, laws[a], b, laws[b])
    assert memory == {7: 6, 8: 10}[order]
    print(order, 'vertices, minimum sufficient history length', memory)
