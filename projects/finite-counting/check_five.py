"""Checks for five-directions.md. Run with standard Python 3.9+."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb
from horizon import ladder, law, moves

def cycles(parts):
    a=[0]*sum(parts)
    start=0
    for n in parts:
        for i in range(n):
            u,v=start+i,start+(i+1)%n
            a[u]|=1<<v
            a[v]|=1<<u
        start+=n
    return a

def losses(parts):
    a=cycles(parts)
    choices=moves(a)
    counts=Counter()
    for u,v in choices:
        b=a.copy()
        b[u]|=1<<v
        b[v]|=1<<u
        counts[len(choices)-len(moves(b))]+=1
    n,c=sum(parts),parts.count(6)
    q=comb(n,2)-2*n
    assert counts==+Counter({1:3*c,3:n-6*c,5:q-n+3*c})

def check_lengths():
    # Reachable lengths by adding a generator, independent of the slice proof.
    sets=[{0}]
    for n in range(1,1201):
        L={h+1 for x in (6,9,20) if x<=n for h in sets[n-x]}
        sets.append(L)
        missing=set(range(min(L),max(L)+1))-L if L else set()
        cs=[c for c in range(n//20+1) if (n-20*c)%3==0]
        pred=set()
        if cs:
            c=max(cs)
            u=(n-20*c)//3
            if c>=3 and u!=1:
                pred=set(range(c+u//2+1,c-3+(u+22)//3))
        assert missing==pred,(n,missing,pred)

def check_tournaments():
    for n in range(2,7):
        pairs=list(combinations(range(n),2))
        for bits in product((0,1),repeat=len(pairs)):
            d=[0]*n
            for p,b in zip(pairs,bits): d[p[b]]+=1
            for a in range(1,4):
                for b in range(1,4):
                    if n<2*(a+b)-2: continue
                    if any(x>=a and n-1-x>=b for x in d): continue
                    assert n==2*(a+b)-2
                    assert sorted(d)==[a-1]*(2*a-1)+[n-b]*(2*b-1)

def check_moments():
    for n,es,g,num in [(3,[(0,1),(1,2),(0,2)],3,1),
                        (4,list(combinations(range(4),2)),3,4),
                        (5,[(i,(i+1)%5) for i in range(5)],5,1)]:
        for q in (2,3):
            dist=Counter(sum(x[u]==x[v] for u,v in es) for x in product(range(q),repeat=n))
            for j in range(g+1):
                val=Fraction(sum(f*comb(k,j) for k,f in dist.items()),q**n)
                base=Fraction(comb(len(es),j),q**j)
                assert val-base==(Fraction(num*(q-1),q**g) if j==g else 0)

if __name__=='__main__':
    for k in (10,12,18): assert law(ladder(k,False),1)==law(ladder(k,True),1)
    for parts in ([6],[7],[8],[14],[6,8],[6,6,6],[7,9]): losses(parts)
    check_lengths()
    check_tournaments()
    check_moments()
    print('All five checks passed.')
