"""Check the even-subgraph formula against all binary vertex colorings."""
from collections import Counter
from itertools import combinations, product
from math import comb


def check(lengths, twists):
    n = 2
    edges = []
    for length, twist in zip(lengths, twists):
        path = [0, *range(n, n+length-1), 1]
        n += length-1
        edges.extend((a,b,twist if j == 0 else 0)
                     for j,(a,b) in enumerate(zip(path,path[1:])))
    m = len(edges)
    observed = Counter(sum((x[a]^x[b]^e) == 0 for a,b,e in edges)
                       for x in product(range(2),repeat=n))
    rhs = [0]*(m+1)
    for r in range(0,len(lengths)+1,2):
        for I in combinations(range(len(lengths)),r):
            h = sum(lengths[i] for i in I)
            for j in range(h+1):
                for k in range(m-h+1):
                    rhs[j+k] += ((-1)**(sum(twists[i] for i in I)+h-j)
                                 *comb(h,j)*comb(m-h,k))
    assert all(rhs[i]*2**n == observed[i]*2**m for i in range(m+1))


if __name__ == "__main__":
    cases = 0
    for lengths in [(1,2,3),(2,2,2),(2,3,4),(1,2,2,3),(2,2,2,2,2)]:
        for twists in product(range(2),repeat=len(lengths)):
            check(lengths,twists)
            cases += 1
    print(cases, "signed path systems checked")
