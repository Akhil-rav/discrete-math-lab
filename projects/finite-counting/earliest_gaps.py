"""Independent earliest-attainment checks by adding generators, not slices."""
from math import gcd

def predicted(p,d,a,b):
    P=d//gcd(d,b-a*p)
    B=b*P; A=a*P
    # Direct x,y enumeration only for the two small-generator extrema.
    def lengths(s): return [x+(s-x*p)//(p+d) for x in range(s//p+1) if (s-x*p)%(p+d)==0]
    if not lengths(B): return None
    last=0
    for j in range(1,(p+d-1)//d+2):
        ls=lengths(j*B)
        if min(ls)-A-last<2*d: return [(i+1)*A*b for i in range(j-1)]
        last=max(ls)
    raise RuntimeError

def direct(p,d,a,b,cap):
    gs=(p*a,(p+d)*a,b); window=[0]*(b+1);window[0]=1
    mask=sum(1<<j for j in range(0,cap//gs[0]+1,d))
    seen=[]
    for n in range(1,cap+1):
        w=0
        for g in gs:
            if n>=g: w|=window[(n-g)%(b+1)]<<1
        window[n%(b+1)]=w
        m=0
        for r in range(d):
            v=w&(mask<<r)
            m=max(m,(v&~(v<<d)).bit_count()-1)
        seen.extend([n]*max(0,m-len(seen)))
    return seen

if __name__=='__main__':
    cnt=0
    for p in range(2,7):
        for d in range(1,6):
            if gcd(p,d)>1: continue
            for a in range(2,5):
                for b in range((p+d)*a+1,(p+d)*a+52,3):
                    if gcd(a,b)>1: continue
                    exp=predicted(p,d,a,b)
                    if exp is None: continue
                    assert direct(p,d,a,b,max([500]+exp)+120)==exp,(p,d,a,b)
                    cnt+=1
    print(cnt,'fixed-semigroup checks passed')
