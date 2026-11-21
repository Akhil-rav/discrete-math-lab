"""Direct finite checks for further-results.md; standard library only."""
from itertools import combinations_with_replacement, combinations, product
from math import comb, gcd, prod
from collections import Counter
from check_five import cycles
from horizon import moves

def test_cycles():
    for size in (1,2,3):
        for parts in combinations_with_replacement(range(4,11),size):
            a=cycles(parts); o=moves(a); h=Counter()
            for i,j in o:
                b=a[:]; b[i]|=1<<j; b[j]|=1<<i
                h[len(o)-len(moves(b))]+=1
            n=sum(parts); q=comb(n,2)-2*n+2*parts.count(4)
            x=3*parts.count(6); y=n-4*parts.count(4)-5*parts.count(5)-6*parts.count(6)
            assert len(o)==q and h==+Counter({1:x,3:y,5:q-x-y})

def test_stars():
    for n in range(2,7):
        pairs=list(combinations(range(n),2))
        for bits in product((0,1),repeat=len(pairs)):
            arcs=[(p[b],p[1-b]) for p,b in zip(pairs,bits)]
            d=Counter(u for u,v in arcs)
            for a in range(1,4):
                for b in range(1,4):
                    if any(d[i]>=a and n-1-d[i]>=b for i in range(n)): continue
                    low={i for i in range(n) if d[i]<a}
                    l=len(low); h=n-l
                    cross=sum(u in low and v not in low for u,v in arcs)
                    assert 2*cross<=min(l*(2*a-1-l),h*(2*b-1-h))

def nblocks(bits):
    # One bit per attainable length; count starts of runs minus one.
    return max(0,(bits & ~(bits<<1)).bit_count()-1)

def test_semigroups():
    for p in range(2,9):
        for a in range(2,6):
            sharp=2*a*p*(p+1)+1
            for b in [*range((p+1)*a+1,(p+1)*a+17),sharp]:
                if gcd(a,b)!=1: continue
                cap=p*a*b if b==sharp else 500
                gens=(p*a,(p+1)*a,b)
                # Store only one circular window; integer bits are exact.
                window=[0]*(b+1); window[0]=1
                for n in range(1,cap+1):
                    bits=0
                    for g in gens:
                        if n>=g: bits|=window[(n-g)%(b+1)]<<1
                    window[n%(b+1)]=bits
                    assert nblocks(bits)<=p,(p,a,b,n)
                if b==sharp: assert nblocks(bits)==p

def test_coloring():
    # Compare polynomial coefficients by exact evaluation at m+1 distinct x.
    for edges,ls,theta in [
        ([(0,1),(1,2),(2,0),(0,3),(3,4),(4,5),(5,0),(0,6)],[3,4],False),
        ([(0,1),(0,2),(2,1),(0,3),(3,4),(4,1)],[1,2,3],True),
        ([(0,i) for i in (2,3,4)]+[(1,i) for i in (2,3,4)]+[(0,5)],[2,2,2],True)]:
        n=max(max(e) for e in edges)+1; m=len(edges)
        for q in (2,3,4):
            hist=Counter(sum(c[i]==c[j] for i,j in edges) for c in product(range(q),repeat=n))
            for x in range(m+1):
                left=sum(cnt*(1+x)**j for j,cnt in hist.items())*q**m
                if theta:
                    s=sum(ls)
                    right=(q+x)**m+sum((q-1)*x**(s-l)*(q+x)**(m-s+l) for l in ls)
                    right+=(q-1)*(q-2)*x**s*(q+x)**(m-s)
                else:
                    right=(q+x)**(m-sum(ls))*prod((q+x)**l+(q-1)*x**l for l in ls)
                assert left==q**n*right

if __name__=='__main__':
    test_cycles(); test_stars(); test_semigroups(); test_coloring()
    print('Direct cycle, tournament, semigroup, and coloring checks passed.')
