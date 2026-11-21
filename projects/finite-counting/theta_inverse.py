"""Exact theta inverse; forward transfer polynomial plus independent colorings."""
from collections import Counter
from itertools import combinations, combinations_with_replacement, product
from fractions import Fraction
from math import comb

def coefficient(j,q): return ((q-1)**j+(q-1)*(-1)**j)//q

def forward(lengths,q):
    out=Counter()
    for j in range(len(lengths)+1):
        for part in combinations(lengths,j): out[sum(part)]+=coefficient(j,q)
    return +out

def inverse(f,q):
    mass=sum(f.values()); r=1
    while q**(r-1)<mass: r+=1
    assert q**(r-1)==mass
    s=Fraction(q*sum(i*v for i,v in f.items()),(q-1)*mass)
    assert s.denominator==1
    s=int(s); found=[]; c=coefficient(r-1,q)
    if not c: raise ValueError('singleton peeling is singular')
    for d in range(1,s+1):
        x=f.get(s-d,0)
        for size in range(2,len(found)+1):
            x-=coefficient(r-size,q)*sum(sum(p)==d for p in combinations(found,size))
        assert x>=0 and x%c==0
        found.extend([d]*(x//c))
        if len(found)==r: break
    assert sum(found)==s and forward(found,q)==f
    return tuple(found)

def direct(lengths,q,leaf=False):
    nxt=2; edges=[]
    for l in lengths:
        path=[0,*range(nxt,nxt+l-1),1]; nxt+=l-1
        edges.extend(zip(path,path[1:]))
    if leaf: edges.append((0,nxt)); nxt+=1
    return Counter(sum(colors[i]==colors[j] for i,j in edges)
                   for colors in product(range(q),repeat=nxt))

if __name__=='__main__':
    runs=0
    for r in range(3,8):
        for ls in combinations_with_replacement(range(1,7),r):
            if ls.count(1)>1: continue
            for q in (2,3,4):
                if q==2 and r%2==0: continue
                assert inverse(forward(ls,q),q)==ls
                runs+=1
    left,right=(2,2,2,4),(1,3,3,3)
    for leaf in (False,True):
        assert direct(left,2,leaf)==direct(right,2,leaf)
        assert direct(left,3,leaf)!=direct(right,3,leaf)
    # From direct coloring moments, verify that normalization removes the leaf.
    for leaf in (False,True):
        h=direct(right,3,leaf); m=max(h); f=forward(right,3)
        for x in range(m+1):
            assert (sum(n*(1+x)**i for i,n in h.items())*3**m
                    ==sum(h.values())*sum(n*x**j*(3+x)**(m-j) for j,n in f.items()))
    print(runs,'successful reconstructions and binary/ternary direct checks')
