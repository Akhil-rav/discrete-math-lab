"""Compare legal graph moves with rooted leaf-set counts for cycle unions."""
from itertools import combinations
from math import factorial

from cycle_histories import direct_polynomial


def types(n, low=4):
    if n == 0:
        yield ()
    for k in range(low, n + 1):
        for rest in types(n-k, k):
            yield (k,) + rest


def histories(parts, depth):
    adj = [set() for _ in range(sum(parts))]
    offset = 0
    for k in parts:
        for i in range(k):
            a, b = offset+i, offset+(i+1) % k
            adj[a].add(b)
            adj[b].add(a)
        offset += k

    def moves():
        return [(a,b) for a,b in combinations(range(len(adj)), 2)
                if b not in adj[a] and adj[a].isdisjoint(adj[b])]

    totals = [0]*(depth+1)

    def visit(options, t):
        for a,b in options:
            adj[a].add(b)
            adj[b].add(a)
            after = moves()
            if len(options)-len(after) == 4+t:
                totals[t] += 1
                if t < depth:
                    visit(after, t+1)
            adj[a].remove(b)
            adj[b].remove(a)

    visit(moves(), 1)
    return totals[1:]


if __name__ == "__main__":
    cases = 0
    for n in range(4, 13):
        for parts in types(n):
            rooted = direct_polynomial(parts)
            expected = [rooted[1]//2, 2*rooted[2], factorial(3)*rooted[3]]
            observed = histories(parts, 3)
            if observed != expected:
                raise ValueError((parts, observed, expected))
            cases += 1
    print(f"{cases} cycle types: all three prefix counts agree")
