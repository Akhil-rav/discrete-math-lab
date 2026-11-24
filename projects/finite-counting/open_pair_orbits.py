"""Exact history laws with isomorphic states grouped before each move."""
from argparse import ArgumentParser
from collections import Counter, defaultdict
from fractions import Fraction
from functools import cache
from itertools import combinations

from open_pair_memory import observations


def orbit_successors(n):
    edges = list(combinations(range(n), 2))

    @cache
    def representative(mask):
        neighbors = [set() for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            if mask & (1 << i):
                neighbors[u].add(v)
                neighbors[v].add(u)
        def canonical(cells):
            while True:
                refined = []
                for cell in cells:
                    groups = defaultdict(list)
                    for v in cell:
                        key = tuple(len(neighbors[v].intersection(other)) for other in cells)
                        groups[key].append(v)
                    refined.extend(groups[key] for key in sorted(groups))
                if len(refined) == len(cells):
                    break
                cells = refined
            # Identical neighborhoods are interchangeable in every completion.
            unresolved = [(len(cell), i) for i, cell in enumerate(cells)
                          if any(neighbors[v] != neighbors[cell[0]] for v in cell)]
            if not unresolved:
                order = [v for cell in cells for v in cell]
                return sum(1 << i for i, (u, v) in enumerate(edges)
                           if order[v] in neighbors[order[u]])
            _, i = min(unresolved)
            cell = cells[i]
            choices = {frozenset(neighbors[v]): v for v in cell}
            return min(canonical(cells[:i] + [[v], [w for w in cell if w != v]]
                                 + cells[i+1:]) for v in choices.values())

        return canonical([list(range(n))])

    @cache
    def successors(mask):
        neighbors = [set() for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            if mask & (1 << i):
                neighbors[u].add(v)
                neighbors[v].add(u)
        return Counter(representative(mask | (1 << i)) for i, (u, v) in enumerate(edges)
                       if v not in neighbors[u] and neighbors[u].isdisjoint(neighbors[v]))

    return successors


def orbit_laws(n):
    successors = orbit_successors(n)
    states = {(0, (n*(n-1)//2,)): 1}
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
