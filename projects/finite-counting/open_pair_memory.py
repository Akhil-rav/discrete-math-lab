"""Exact conditional next-step laws from the empty triangle-free graph."""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations


def observations(n, horizon):
    edges = list(combinations(range(n), 2))

    @lru_cache(None)
    def children(graph):
        neighbors = [0] * n
        for index, (u, v) in enumerate(edges):
            if graph & (1 << index):
                neighbors[u] |= 1 << v
                neighbors[v] |= 1 << u
        return tuple(graph | (1 << i) for i, (u, v) in enumerate(edges)
                     if not graph & (1 << i) and not neighbors[u] & neighbors[v])

    states = {(0, (len(edges),)): 1}
    for step in range(horizon + 1):
        counts = defaultdict(Counter)
        following = Counter()
        for (graph, history), multiplicity in states.items():
            for child in children(graph):
                q = len(children(child))
                counts[history][q] += multiplicity
                if step < horizon:
                    following[child, history + (q,)] += multiplicity
        yield {h: {q: Fraction(v, sum(b.values())) for q, v in b.items()}
               for h, b in counts.items()}
        states = following


if __name__ == "__main__":
    for step, laws in enumerate(observations(6, 9)):
        # Find the longest common suffix at this time with different forecasts.
        for length in range(step, 0, -1):
            seen = {}
            for history in sorted(laws):
                key = history[-length:]
                if key in seen and laws[history] != laws[seen[key]]:
                    previous = seen[key]
                    print(step, length, previous, laws[previous], history, laws[history])
                    break
                seen[key] = history
            else:
                continue
            break
