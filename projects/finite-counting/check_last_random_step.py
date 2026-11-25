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

    for s in range(3, 13):
        n = 2*s
        graph = {(u, s+j) for u in range(s) for j in range(s) if u != j}
        moves = legal(n, graph)
        assert len(graph) == s*(s-1) and len(moves) == s
        assert all(len(legal(n, graph | {e})) == s-1 for e in moves)

    for i in range(1, 6):
        s = i*(i+1)+2
        n = 2*s+1
        a = s-i
        bip = {(u, v) for u in range(a) for v in range(a, n)}
        bip.difference_update({(0, a), (1, a+1)})
        # Ordinary left vertices are 2..s; the last right vertex sees neither 0 nor 1.
        other = {(u, v) for u in range(2, s+1) for v in range(s+1, n)}
        other.update({(0, 1), (0, s+1)})
        other.update((1, v) for v in range(s+2, n-1))
        for graph, forecast in ((bip, 1), (other, 0)):
            moves = legal(n, graph)
            assert len(graph) == s*s and len(moves) == 2
            assert all(len(legal(n, graph | {e})) == forecast for e in moves)
    print("Checked equal-count examples at even orders 6..24 and five exceptional odd orders.")
