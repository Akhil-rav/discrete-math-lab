"""Check seam detection using closed walks in the graph itself."""
from collections import Counter
from itertools import combinations


def partitions(n, low=1):
    if n == 0:
        yield ()
    for first in range(low, n + 1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def adjacency(k, parts):
    q = sum(parts)
    seam = []
    for length in parts:
        start = len(seam)
        seam.extend(start + (j + 1) % length for j in range(length))
    neighbors = [set() for _ in range(k * q)]
    for i in range(k):
        for j in range(q):
            v = i * q + j
            neighbors[v].update(i * q + h for h in range(q) if h != j)
            w = ((i + 1) % k) * q + (j if i + 1 < k else seam[j])
            neighbors[v].add(w)
            neighbors[w].add(v)
    return neighbors


def traces(neighbors, steps):
    counts = [0] * (steps + 1)
    for root in range(len(neighbors)):
        ways = [int(i == root) for i in range(len(neighbors))]
        for m in range(steps + 1):
            counts[m] += ways[root]
            if m < steps:
                ways = [sum(ways[w] for w in row) for row in neighbors]
    return counts


if __name__ == '__main__':
    cases = pairs = 0
    for k in range(3, 7):
        for q in range(2, 9):
            rows = {p: traces(adjacency(k, p), k * (q // 2)) for p in partitions(q)}
            cases += len(rows)
            for p, r in combinations(rows, 2):
                a, b = Counter(p), Counter(r)
                l = min(i for i in a.keys() | b.keys() if a[i] != b[i])
                m = next(i for i, (x, y) in enumerate(zip(rows[p], rows[r])) if x != y)
                assert m == k*l and rows[p][m]-rows[r][m] == 2*k*l*(a[l]-b[l])
                pairs += 1
    print(cases, 'graphs;', pairs, 'pairs checked')
