"""Collision search for a single modified-host law at fixed total length."""
from itertools import groupby, product
from time import monotonic
from math import comb


def lengths(m, r, lo=1):
    if r == 1:
        if m >= lo: yield (m,)
        return
    for v in range(lo, m//r+1):
        for tail in lengths(m-v, r-1, max(2,v)):
            yield (v,)+tail


def cases(m, low, high, base):
    for r in range(low,min(high,(m+1)//2)+1):
        for ls in lengths(m,r):
            groups = [(l,len(list(g))) for l,g in groupby(ls)]
            for neg in product(*(range(n+1) for l,n in groups)):
                a = b = 1
                for (l,n),k in zip(groups,neg):
                    x = base**l
                    a *= (1+x)**(n-k)*(1-x)**k
                    b *= (1-x)**(n-k)*(1+x)**k
                yield (ls,neg),(a+b)//2,(a-b)//2


def scan(m,low,high,deadline,cap):
    # Every signed coefficient has magnitude below 2^(high+1).
    base = 1 << (high+3)
    probes = (m-2,m-1,m)
    shifts = [base**p for p in probes]
    seen = [{} for p in probes]
    collisions = {}
    n = 0
    for state,e,o in cases(m,low,high,base):
        n += 1
        if n > cap or (n%128==0 and monotonic()>=deadline):
            return n-1,collisions,False
        for p,s,d in zip(probes,shifts,seen):
            if p in collisions: continue
            key = e+s*o
            if key in d:
                collisions[p]=(d[key],state)
                d.clear()
            else:
                d[key]=state
    return n,collisions,True


if __name__ == "__main__":
    import argparse,json
    parser=argparse.ArgumentParser()
    parser.add_argument("--seconds",type=int,default=15)
    parser.add_argument("--max-edges",type=int,default=1200)
    args=parser.parse_args()
    end=monotonic()+args.seconds
    for m in range(6,args.max_edges+1):
        if monotonic()>=end: break
        # Bound memory; later fixed-r ranges are still useful if a wider scan is capped.
        for lo,hi in [(3,min(10,(m+1)//2)),(3,3),(4,4),(5,5)]:
            if hi<lo or monotonic()>=end: continue
            n,c,done=scan(m,lo,hi,end,min(45000,max(500,15000000//(hi*m))))
            print(json.dumps(dict(m=m,r=[lo,hi],states=n,complete=done,collisions=c)),flush=True)
