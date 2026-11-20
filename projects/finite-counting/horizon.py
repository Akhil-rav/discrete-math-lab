"""Brute-force two-step laws, recomputing legal pairs for every successor."""
from itertools import combinations
from collections import Counter
from fractions import Fraction

def ladder(k,twist):
    a=[0]*(2*k)
    def edge(i,j):
        a[i]|=1<<j; a[j]|=1<<i
    for i in range(k):
        edge(2*i,2*i+1)
        for s in range(2):
            edge(2*i+s,2*((i+1)%k)+(s^(twist and i==k-1)))
    return a

def moves(a):
    return [(i,j) for i,j in combinations(range(len(a)),2)
            if not (a[i]>>j)&1 and not a[i]&a[j]]

def law(a,t):
    choices=moves(a)
    if not choices or t==0: return {(len(choices),):Fraction(1)}
    ans=Counter()
    for i,j in choices:
        b=a.copy(); b[i]|=1<<j; b[j]|=1<<i
        for path,p in law(b,t-1).items(): ans[(len(choices),)+path]+=p/len(choices)
    return ans

if __name__=='__main__':
    for k in (4,6,8,10,12):
        a,b=(ladder(k,s) for s in (False,True))
        print(k,*(law(a,t)==law(b,t) for t in (1,2)),flush=True)
