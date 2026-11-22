"""Recover signed path lengths from a baseline and a calibrated path."""
from collections import Counter
from math import comb
from itertools import combinations_with_replacement, product


def law(paths):
    # Exact counts with the first terminal fixed; count mismatches on each path.
    total = Counter()
    for d in (0,1):
        row = {0:1}
        for l,s in paths:
            nxt = Counter()
            for i in range(l+1):
                if (-1)**(l-i+d) == s:
                    for k,v in row.items():
                        nxt[k+i] += v*comb(l,i)
            row = nxt
        total.update(row)
    return total


def transform(counts):
    weight = sum(counts.values())
    m,rem = divmod(2*sum(k*v for k,v in counts.items()),weight)
    assert rem == 0
    # E(x) = (1-x)^m G((1+x)/(1-x)).
    out = [0]*(m+1)
    for k,c in counts.items():
        for i in range(k+1):
            for j in range(m-k+1):
                out[i+j] += c*comb(k,i)*comb(m-k,j)*(-1)**j
    assert all(v % weight == 0 for v in out)
    return [v//weight for v in out]


def decode(e,o):
    # Peel shortest lengths in the two signed products simultaneously.
    n = len(e)-1
    a = [x+y for x,y in zip(e,o)]
    b = [x-y for x,y in zip(e,o)]
    ab = [0]*(2*n+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            ab[i+j] += x*y
    paths = []
    for l in range(1,n+1):
        count,delta = -ab[2*l],a[l]
        assert count >= abs(delta) and (count-delta)%2 == 0
        signs = [1]*((count+delta)//2)+[-1]*((count-delta)//2)
        for s in signs:
            for k in range(l,n+1):
                a[k] -= s*a[k-l]
            for k in range(2*l,2*n+1):
                ab[k] += ab[k-2*l]
            paths.append((l,s))
    return sorted(paths)


if __name__ == "__main__":
    cases = 0
    for r in range(2,5):
        for lengths in combinations_with_replacement(range(1,5),r):
            if lengths.count(1)>1: continue
            for signs in product([-1,1],repeat=r):
                paths = list(zip(lengths,signs))
                e = transform(law(paths))
                probe = transform(law(paths+[(2,1)]))
                o = [(probe[j+2]-(e[j+2] if j+2<len(e) else 0))
                     for j in range(len(e))]
                assert decode(e,o) == sorted(paths)
                cases += 1
    print(cases, "assignments recovered from two exact conflict-count laws")
