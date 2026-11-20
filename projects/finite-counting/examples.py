"""Small exact examples; Python 3.9+, standard library only."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from six import edges, moves

def drift(g):
    c = moves(g)
    return Fraction(sum(len(moves(h))-len(c) for h in c),len(c))

def witness():
    layer = {0}
    for m in range(10):
        groups = {}
        for g in sorted(layer):
            q = len(moves(g))
            if not q: continue
            if q in groups and drift(g) != drift(groups[q]):
                for h in [groups[q],g]:
                    print(m,q,[e for i,e in enumerate(edges) if h>>i&1],drift(h))
                return
            groups[q] = g
        layer = {h for g in layer for h in moves(g)}

def outstars(n):
    # A directed two-leaf out-star is present iff some vertex beats two others.
    pairs = list(combinations(range(n),2))
    avoid = 0
    for bits in product(range(2),repeat=len(pairs)):
        wins = Counter(p[b] for p,b in zip(pairs,bits))
        avoid += max(wins.values()) < 2
    return avoid

def lengths(target):
    return Counter(a+b+c for a in range(target//6+1)
                   for b in range(target//9+1) for c in range(target//20+1)
                   if 6*a+9*b+20*c == target)

if __name__ == '__main__':
    witness()
    print('out-star avoiding tournaments:',[(n,outstars(n)) for n in (3,4)])
    print('lengths for 60:',sorted(lengths(60).items()))
    print('monochromatic triangle edge counts:',sorted(Counter(
        sum(x[i]==x[j] for i,j in combinations(range(3),2))
        for x in product(range(2),repeat=3)).items()))
