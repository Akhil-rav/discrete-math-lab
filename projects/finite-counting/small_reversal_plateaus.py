"""Search small unlabeled tournaments for a nonoptimal closed reversal plateau.

An adjacency row uses bit j for an outgoing arc to j. Extend all representatives
by a minimum-outdegree vertex; every tournament has such a deletion. Canonical
keys use equitable partition refinement with exhaustive individualization.
"""
import argparse
from collections import Counter
from functools import lru_cache
from itertools import combinations


def canon(g):
    n=len(g)
    def search(cells):
        while True:
            nxt=[]
            for c in cells:
                groups={}
                for i in range(n):
                    if c>>i&1:
                        sig=tuple((g[i]&b).bit_count() for b in cells)
                        groups[sig]=groups.get(sig,0)|(1<<i)
                nxt.extend(groups[s] for s in sorted(groups))
            if len(nxt)==len(cells):
                break
            cells=nxt
        for j,c in enumerate(cells):
            if c&(c-1):
                return min(search(cells[:j]+[v,c^v]+cells[j+1:])
                           for v in [1<<i for i in range(n) if c>>i&1])
        return tuple(sum(1<<j for j,b in enumerate(cells) if g[a.bit_length()-1]&b)
                     for a in cells)
    return search([(1<<n)-1])


def extend(reps,n):
    result=set()
    for g in reps:
        for s in range(1<<(n-1)):
            deg=s.bit_count()
            if deg>(n-1)//2 or any(x.bit_count()+1-(s>>i&1)<deg for i,x in enumerate(g)):
                continue
            result.add(canon(tuple(x|((1-(s>>i&1))<<(n-1)) for i,x in enumerate(g))+(s,)))
    return result


def score(g):
    N=len(g)-1
    return sum(x*(N-x)*(N-1-x)//2 for x in (v.bit_count() for v in g))


def audit(reps,n):
    optimum=min(map(score,reps))
    traps=set()
    for g in reps:
        if score(g)==optimum: continue
        ds=[v.bit_count() for v in g]
        if all((ds[a]-ds[b]-1)*(4*n-6-3*(ds[a]+ds[b]))>=0
               for a in range(n) for b in range(n) if g[a]>>b&1):
            traps.add(g)
    original=len(traps); closed=[]
    while traps:
        seed=traps.pop(); frontier=[seed]; component={seed}; escaping=False
        for g in frontier:
            s=score(g)
            for a,b in combinations(range(n),2):
                other=list(g);other[a]^=1<<b;other[b]^=1<<a
                if score(other)!=s: continue
                h=canon(tuple(other))
                if h in component:continue
                if h in traps:
                    traps.remove(h);component.add(h);frontier.append(h)
                else:escaping=True
        if not escaping:closed.append((s,len(component),seed))
    print('n',n,'types',len(reps),'minimum',optimum,'nonoptimal no-improvement types',original,
          'closed components',len(closed),'example',min(closed,default=None),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-order',type=int,default=8)
    args=parser.parse_args()
    reps={(0,)}
    for n in range(2,args.max_order+1):
        reps=extend(reps,n)
        audit(reps,n)
