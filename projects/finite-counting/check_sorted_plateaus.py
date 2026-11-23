"""Second audit: enumerate only directly stuck tournaments with sorted scores.

No graph canonization. Backtrack over legal directions at fixed degrees; test an
exit by searching neutral reversals with the original vertex labels intact.
"""
from itertools import combinations, combinations_with_replacement
from collections import deque


def audit(n):
    edges=list(combinations(range(n),2)); N=n-1
    f=[x*(N-x)*(N-1-x)//2 for x in range(n)]
    def delta(a,b):return f[a-1]+f[b+1]-f[a]-f[b]
    def directions(ds,a,b):
        return ds[a]>0 and ds[b]<N and delta(ds[a],ds[b])>=0
    def realize(ds):
        allowed=[[(a,b) for a,b in ((i,j),(j,i)) if directions(ds,a,b)] for i,j in edges]
        if any(not x for x in allowed):return
        order=sorted(range(len(edges)),key=lambda j:len(allowed[j]))
        need=list(ds); avail=[0]*n
        for opts in allowed:
            for a,b in opts:avail[a]+=1
        def visit(pos,mask):
            if any(x<0 or x>y for x,y in zip(need,avail)):return
            if pos==len(order):
                yield mask;return
            j=order[pos]
            for a,b in allowed[j]:avail[a]-=1
            for a,b in allowed[j]:
                need[a]-=1
                yield from visit(pos+1,mask|((a>b)<<j))
                need[a]+=1
            for a,b in allowed[j]:avail[a]+=1
        yield from visit(0,0)
    def escape(mask):
        q=deque([(mask,0)]);seen={mask}
        while q:
            g,k=q.popleft();ds=[0]*n
            arcs=[(b,a) if g>>i&1 else (a,b) for i,(a,b) in enumerate(edges)]
            for a,b in arcs:ds[a]+=1
            changes=[delta(ds[a],ds[b]) for a,b in arcs]
            if min(changes)<0:return k
            for i,z in enumerate(changes):
                h=g^(1<<i)
                if z==0 and h not in seen:seen.add(h);q.append((h,k+1))
        return None
    scores=[s for s in combinations_with_replacement(range(n),n)
            if sum(s)==len(edges) and all(sum(s[:k])>=k*(k-1)//2 for k in range(1,n))]
    # Prefix conditions are necessary. An explicit attained score confirms
    # that this lower bound on the minimum is sharp.
    val=lambda s:sum(f[a] for a in s)
    opt=min(map(val,scores)); low=next(s for s in scores if val(s)==opt and next(realize(s),None) is not None)
    hist={}
    for s in scores:
        if val(s)==opt:continue
        for g in realize(s):
            k=escape(g);hist[k]=hist.get(k,0)+1
    return opt,low,hist


if __name__=='__main__':
    for n in range(4,10):
        print(n,*audit(n),flush=True)
