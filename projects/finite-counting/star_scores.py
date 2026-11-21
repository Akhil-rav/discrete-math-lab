"""Minimize unordered mixed-star copies over tournament score sequences."""
from functools import lru_cache
from math import comb
from itertools import product, combinations

def optimize(n,a,b,restrict=False):
    cap=n-(2*a+2*b-2)
    @lru_cache(None)
    def visit(i,last,total,centers):
        if i==n: return (0,()) if total==comb(n,2) else None
        rem=n-1-i
        best=None
        for d in range(last,n):
            t=total+d
            if t<comb(i+1,2) or t+rem*(n-1)<comb(n,2): continue
            if t+rem*d>comb(n,2): break
            c=int(a<=d<=n-1-b)
            if restrict and centers+c>cap: continue
            child=visit(i+1,d,t,centers+c if restrict else 0)
            if child is None: continue
            opt=(comb(d,a)*comb(n-1-d,b)+child[0],(d,)+child[1])
            if best is None or opt<best: best=opt
        return best
    return visit(0,0,0,0)

if __name__=='__main__':
    for a,b in [(1,1),(1,2),(2,2),(2,3),(3,3)]:
        for n in range(2*a+2*b-1,2*a+2*b+12):
            best=optimize(n,a,b); restricted=optimize(n,a,b,True)
            if best[0]!=restricted[0]:
                print(a,b,n,best,restricted,flush=True); break
        else: print(a,b,'no discrepancy in range',flush=True)
