"""Independent checks of edge-event independence from the full coloring table."""
from itertools import product, permutations, combinations
from math import factorial
from fractions import Fraction
from collections import Counter

def agree(p,q): return sum(x==y for x,y in zip(p,q))
def three(q):
    perms=list(permutations(range(q))); ident=perms[0]
    good=[agree(p,ident)==1 for p in perms]; freq=Counter()
    for i,p in enumerate(perms):
        for j,b in enumerate(perms): freq[good[i]+good[j]+(agree(p,b)==1)]+=1
    return Fraction(freq[1],factorial(q)**2),freq

def families(q,pathlabels):
    # Vertices 0,1 terminals and 2,3,4 internal. Six ordered indicator bits.
    hit=[0]*64
    for u,v,w0,w1,w2 in product(range(q),repeat=5):
        mask=0
        for j,w in enumerate((w0,w1,w2)):
            mask|=int(w==u)<<(2*j)
            mask|=int(v==pathlabels[j][w])<<(2*j+1)
        hit[mask]+=1
    for i in range(6):
        for m in range(64):
            if not(m>>i&1): hit[m]+=hit[m|(1<<i)]
    indep=[True]*64
    for m in range(1,64):
        indep[m]=(hit[m]*q**m.bit_count()==q**5 and
                  all(indep[m^(1<<i)] for i in range(6) if m>>i&1))
    return indep

def exchange(ok):
    levels=[[m for m in range(64) if ok[m] and m.bit_count()==j] for j in range(7)]
    return all(any(ok[a|bit] for bit in (1,2,4,8,16,32) if b&bit and not a&bit)
               for lv in range(6) for a in levels[lv] for b in levels[lv+1])

if __name__=='__main__':
    for q in (2,3,4):
        ps=list(permutations(range(q))); ident=ps[0]
        for p,b in product(ps,repeat=2):
            expect=sum(agree(i,j)==1 for i,j in combinations((ident,p,b),2))!=1
            assert exchange(families(q,(ident,p,b))) == expect
        f,_=three(q); print(q,'failure',f,'direct check passed')
    f,_=three(5); print(5,'failure',f)
