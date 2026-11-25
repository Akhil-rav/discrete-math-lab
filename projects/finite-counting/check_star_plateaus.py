"""Direct checks of the nonoptimal plateau construction."""
from collections import Counter
from itertools import combinations, permutations


def graph(n,k,order=None):
    order = list(range(k)) if order is None else order
    rank = {v:i for i,v in enumerate(order)}
    r = n-k
    return {(a,b) if (rank[a]>rank[b] if b<k else
                       False if a<k else (b-a)%r<=r//2) else (b,a)
            for a,b in combinations(range(n),2)}


def stars(arcs,n):
    return sum(sum((c,v) in arcs for v in triple)==1
               for c in range(n) for triple in combinations(set(range(n))-{c},3))


if __name__ == "__main__":
    n,k=10,3
    cohort={frozenset(graph(n,k,order)) for order in permutations(range(k))}
    histogram=Counter()
    for arcs in cohort:
        assert stars(arcs,n)==196
        for a,b in arcs:
            moved=arcs-{(a,b)}|{(b,a)}
            change=stars(moved,n)-196
            assert change>=0 and ((change==0)==(moved in cohort))
            histogram[change]+=1
    assert stars(graph(n,k+2),n)==190
    print("Six plateau states; reversal histogram across them:",sorted(histogram.items()))
    for t in range(1,101):
        N=6*t+3;k=2*t+1;r=4*t+3;v=4*t+2
        def f(x):return x*(N-x)*(N-x-1)//2
        assert f(k)+f(k+1)+(r-2)*f(v+1)-r*f(v)==-8*t**3-2*t**2+3*t+1
