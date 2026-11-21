"""Exact six-vertex triangle-free process; run with standard Python 3.9+."""
from itertools import combinations
from fractions import Fraction
from collections import defaultdict
from functools import cache
from random import Random

edges = list(combinations(range(6), 2))
index = {e: 1 << i for i,e in enumerate(edges)}
tri = [sum(index[e] for e in combinations(t,2)) for t in combinations(range(6),3)]
@cache
def moves(g):
    return tuple(g|b for b in index.values() if not g&b and not any((g|b)&t == t for t in tri))

def main():
    level = {0: Fraction(1)}
    terminal = defaultdict(Fraction)
    for m in range(10):
        nxt = defaultdict(Fraction)
        drift = Fraction()
        for g,p in level.items():
            children = moves(g)
            if not children:
                terminal[m] += p
            for h in children:
                nxt[h] += p/len(children)
                drift += p*(len(moves(h))-len(children))/len(children)
        if m == 2:
            assert drift == Fraction(-191,91)
            print('Expected change after edge 2:',drift)
        level = nxt
    # Independent state-space check: enumerate all graphs by adjacency sets.
    seen = 0
    reachable = moves.cache_info().currsize
    for g in range(1<<15):
        adj = [set() for _ in range(6)]
        for i,(u,v) in enumerate(edges):
            if g>>i&1: adj[u].add(v); adj[v].add(u)
        if any(adj[u]&adj[v] for u in range(6) for v in adj[u]): continue
        seen += 1
        assert set(moves(g)) == {g|index[u,v] for u,v in edges if v not in adj[u] and not adj[u]&adj[v]}
    assert seen == reachable == moves.cache_info().currsize
    assert sum(terminal.values()) == 1
    print('Reachable labeled states:',seen)
    rng = Random(20261119)
    def trial():
        g = 0
        for _ in range(2): g = rng.choice(moves(g))
        return len(moves(rng.choice(moves(g))))-len(moves(g))
    print('Mean drift, 100000 trials:', sum(trial() for _ in range(100000))/100000)
    print('Terminal edge counts:',dict(terminal))
if __name__ == '__main__': main()
