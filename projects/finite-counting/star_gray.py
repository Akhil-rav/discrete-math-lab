"""Independent exhaustive n=7 check: one edge reverses per Gray-code step."""
from itertools import combinations
from math import comb

def minima(n,a,b):
    pairs=list(combinations(range(n),2))
    d=list(range(n-1,-1,-1))
    cost=[comb(v,a)*comb(n-1-v,b) for v in range(n)]
    good=[int(a<=v<=n-1-b) for v in range(n)]
    s=sum(cost[v] for v in d); c=sum(good[v] for v in d)
    ans={c:s}; mask=0
    for t in range(1,1<<len(pairs)):
        bit=t&-t; i,j=pairs[bit.bit_length()-1]
        change=1 if mask&bit else -1
        u,v=d[i],d[j]; d[i]+=change; d[j]-=change
        s+=cost[d[i]]+cost[d[j]]-cost[u]-cost[v]
        c+=good[d[i]]+good[d[j]]-good[u]-good[v]
        mask^=bit
        if s<ans.get(c,10**9): ans[c]=s
    return ans

if __name__=='__main__':
    print(sorted(minima(7,1,2).items()))
