"""Independent DP on length supports; no slicing formula used."""
from math import gcd,ceil

def check(a,b,p,d,cap,sharp=False):
    bound=(p+d-1)//d
    # Rolling bitsets by target; project to each residue via a precomputed mask.
    gens=(a*p,a*(p+d),b)
    win=[0]*(b+1); win[0]=1
    hi=cap//gens[0]+1
    mask=sum(1<<j for j in range(0,hi,d))
    for n in range(1,cap+1):
        v=0
        for g in gens:
            if n>=g: v|=win[(n-g)%(b+1)]<<1
        win[n%(b+1)]=v
        best=0
        for r in range(d):
            w=v&(mask<<r)
            best=max(best,(w&~(w<<d)).bit_count()-1)
        assert best<=bound,(a,b,p,d,n,best)
    if sharp: assert best==bound,(a,b,p,d,cap,best)

if __name__=='__main__':
    runs=0
    for p in range(2,9):
        for d in range(1,8):
            if gcd(p,d)>1: continue
            for a in (2,3,4):
                for b in range((p+d)*a+1,(p+d)*a+12):
                    if gcd(a,b)==1: check(a,b,p,d,350);runs+=1
            a=d+1; M=1
            while True:
                b=a*p+d*(a*M+1)
                H=ceil(p/d)
                if b*(p-(H-1)*d)>(2*d+a)*p*(p+d) and b>p*(p+d): break
                M+=1
            check(a,b,p,d,H*a*b,True)
    print(runs,'parameter triples per (p,d) combined, and each sharpness construction passed')
