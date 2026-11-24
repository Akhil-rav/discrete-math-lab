"""Direct next-count checks at the last possible nondeterministic step."""
from collections import Counter
from itertools import combinations


def legal(n, graph):
    neighbors = [set() for _ in range(n)]
    for x, y in graph:
        neighbors[x].add(y)
        neighbors[y].add(x)
    return [e for e in combinations(range(n), 2)
            if e not in graph and neighbors[e[0]].isdisjoint(neighbors[e[1]])]


def check(n, x, y):
    # Left has x+1 vertices, right has y. Split one original left vertex.
    for size in range(y+1):
        graph = {(u, x+1+j) for u in range(x+1) for j in range(y)
                 if u >= 2 or u == int(j >= size)}
        assert len(graph) == (n-1)**2//4
        moves = legal(n, graph)
        actual = Counter(len(legal(n, graph | {e})) for e in moves)
        expected = Counter()
        if 0 < size < y:
            expected[0] = 1
            expected[y-1] = y
        else:
            expected[x-1] += x
            expected[y-1] += y
        assert actual == expected, (n, x, y, size, actual)


if __name__ == "__main__":
    for n in range(6, 25):
        x = (n-1)//2
        y = n-1-x
        for left, right in {(x, y), (y, x)}:
            check(n, left, right)
    print("Every split size checked for n=6 through 24.")
