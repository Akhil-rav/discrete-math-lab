"""Exact path counts. Normalize a path by the product of its pre-move Q's."""
from collections import Counter
from itertools import combinations
from fractions import Fraction
from horizon import ladder, law

def opens(a):
    rows=[]
    for i,row in enumerate(a):
        banned=row | 1<<i
        bits=row
        while bits:
            bit=bits&-bits
            banned |= a[bit.bit_length()-1]
            bits ^= bit
        rows.append(((1<<len(a))-1)^banned)
    return rows

def choices(o):
    for i,row in enumerate(o):
        bits=row & ~((2<<i)-1)
        while bits:
            b=bits&-bits
            yield i,b.bit_length()-1
            bits ^= b

def histogram(a,t,k,twist):
    root=opens(a)
    def descend(state,depth):
        o=opens(state); q=sum(x.bit_count() for x in o)//2
        hist=Counter()
        for i,j in choices(o):
            if depth==1:
                loss=1+(o[i]&state[j]).bit_count()+(o[j]&state[i]).bit_count()
                hist[(q,q-loss)]+=1
            else:
                b=state.copy(); b[i]|=1<<j; b[j]|=1<<i
                for path,n in descend(b,depth-1).items(): hist[(q,)+path]+=n
        if not q: hist[(0,)]=1
        return hist
    if t<1: raise ValueError("t must be positive")
    if t==1 or not any(root): return descend(a,t)
    # Translating one endpoint to column zero, reflections, row swaps.
    def key(i,j):
        d,s=divmod(i,2); e,r=divmod(j,2)
        l=e-d
        return min((l,s^r),(k-l,s^r^twist))
    types={}
    for i,j in choices(root):
        entry=types.setdefault(key(i,j),[i,j,0]); entry[2]+=1
    q=sum(x.bit_count() for x in root)//2
    hist=Counter()
    for i,j,m in types.values():
        b=a.copy(); b[i]|=1<<j; b[j]|=1<<i
        for path,n in descend(b,t-1).items(): hist[(q,)+path]+=m*n
    return hist

def probability(path,n):
    d=1
    for q in path[:-1]: d*=q
    return Fraction(n,d)

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument('k',type=int); p.add_argument('t',type=int)
    args=p.parse_args()
    hs=[]
    for s in range(2):
        a=ladder(args.k,s); h=histogram(a,args.t,args.k,s); hs.append(h)
        assert sum(probability(path,n) for path,n in h.items())==1
        if args.k<=8 and args.t<=2:
            assert {p:probability(p,n) for p,n in h.items()}==law(a,args.t)
    diffs=[(p,hs[0][p],hs[1][p]) for p in sorted(hs[0].keys()|hs[1].keys()) if hs[0][p]!=hs[1][p]]
    print(args.k,args.t,'equal' if not diffs else 'different',diffs[:1],flush=True)
