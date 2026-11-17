"""Independent check of Proposition 6: no seven traces suffice for the (4,4) end windows.

Pure Python, no solver: enumerates every deficit-three colouring of the 24 window
edges by shape (4), (3,2), (2,2,2), then runs an exhaustive depth-first search.

  python experiments/ladder_end_windows_check.py      # about two minutes
"""
import subprocess, sys
from itertools import combinations
out=subprocess.run([sys.executable,'experiments/ladder_end_windows.py','4','4'],capture_output=True,text=True).stdout.split('\n')
m,n=map(int,out[0].split()); Ms=[set(map(int,l.split()[1:])) for l in out[1:1+n]]
inc=[sum(1<<j for j,M in enumerate(Ms) if e in M) for e in range(m)]
full=(1<<n)-1
pair={p:inc[p[0]]&inc[p[1]] for p in combinations(range(m),2)}
def kill(block): 
    k=0
    for p in combinations(block,2): k|=pair[p]
    return k
masks=set()
for q in combinations(range(m),4): masks.add(full&~kill(q))
tri={t:kill(t) for t in combinations(range(m),3)}
for t,kt in tri.items():
    rest=[e for e in range(m) if e not in t]
    for p in combinations(rest,2): masks.add(full&~(kt|pair[p]))
P=list(pair.items())
for i,(p1,k1) in enumerate(P):
    for j in range(i+1,len(P)):
        p2,k2=P[j]
        if p1[0] in p2 or p1[1] in p2: continue
        k12=k1|k2
        for l in range(j+1,len(P)):
            p3,k3=P[l]
            if p3[0] in p1 or p3[1] in p1 or p3[0] in p2 or p3[1] in p2: continue
            masks.add(full&~(k12|k3))
masks.discard(0)
ms=sorted(masks,key=lambda x:bin(x).count('1')); mn=[]
for x in ms:
    if not any(y&x==y for y in mn): mn.append(x)
print("distinct survivor sets", len(masks), "minimal", len(mn))
# independent exhaustive proof that no 7 traces suffice: depth-first on smallest unhit set
sets=sorted(mn,key=lambda x:bin(x).count('1'))
cnt=0
def go(T,left):
    global cnt; cnt+=1
    best=None
    for s in sets:
        if not s&T:
            c=bin(s).count('1')
            if best is None or c<best[0]: best=(c,s)
            if c<=2: break
    if best is None: return True
    if left==0: return False
    s=best[1]
    while s:
        b=s&-s; s^=b
        if go(T|b,left-1): return True
    return False
result = go(0, 7)
print("7 traces suffice:", result, "search nodes", cnt)
assert result is False and len(mn) == 300
