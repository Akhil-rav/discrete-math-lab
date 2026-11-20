"""Independent finite checks for extensions.md; no external packages."""
from itertools import combinations, product
from collections import Counter
from six import edges, index, moves
from examples import lengths

def check_drift():
    layer, checked = {0}, 0
    while layer:
        nxt = set()
        for g in layer:
            children = moves(g)
            if not children: continue
            nxt.update(children)
            opened = {h ^ g for h in children}
            w = 0
            for vertices in combinations(range(6),3):
                tri = [index[e] for e in combinations(vertices,2)]
                w += sum(bool(g & b) for b in tri)==1 and sum(b in opened for b in tri)==2
            q = len(children)
            assert sum(len(moves(h))-q for h in children)==-q-2*w
            checked += 1
        layer = nxt
    return checked

def avoid(n,r):
    pairs = list(combinations(range(n),2))
    return sum(max(Counter(p[b] for p,b in zip(pairs,bits)).values(),default=0)<r
               for bits in product(range(2),repeat=len(pairs)))

def check_colors():
    es = list(combinations(range(4),2))
    for mask in range(64):
        chosen = [e for j,e in enumerate(es) if mask>>j&1]
        roots = list(range(4))
        for a,b in chosen:
            old,new = roots[b],roots[a]
            roots = [new if x==old else x for x in roots]
        for q in (2,3):
            count = sum(all(x[a]==x[b] for a,b in chosen) for x in product(range(q),repeat=4))
            assert count == q**len(set(roots))

def slices(n):
    counts = Counter()
    for c in range(n//20+1):
        if (n-20*c)%3: continue
        t = (n-20*c)//3
        for b in range(t%2,t//3+1,2):
            counts[c+(t-b)//2] += 1
    return counts

if __name__ == '__main__':
    print('Nonterminal states checked:',check_drift())
    for r,expected in ((1,1),(2,2),(3,24)):
        assert (avoid(2*r-1,r),avoid(2*r,r)) == (expected,0)
    check_colors()
    for n in range(241): assert slices(n)==lengths(n)
    print('Tournament, coloring and factorization checks passed.')
