"""Write the two-end window system used for the bound h_3(k) >= 8.

The left window has gaps 0..a-1 and the rungs of columns 0..a-1; the right
window is its mirror image with b gaps. A "matching" of the system is a pair
of gap patterns, one per window. Any test family for L_k with k >= a+b+2
induces a hitting set for the survivor sets of this system.

  g++ -O2 -o survivors_generic experiments/survivor_sets_generic.cpp
  python experiments/ladder_end_windows.py 4 4 | ./survivors_generic 3 > windows44.txt
  python experiments/ladder_hitting_set.py windows44.txt 300   # prints OPTIMAL h = 8

Recorded on 2026-11-16: windows (3,3) give 7; (4,4), (5,4) and (5,5) give 8.
"""
import sys
a,b=int(sys.argv[1]),int(sys.argv[2])
def pats(n): return [s for s in range(1<<n) if not s&(s>>1)]
# left piece: gaps 0..a-1, rungs of columns 0..a-1 ; right piece mirrored with b gaps
def piece(n,s,off):
    E=[]
    for c in range(n):                       # column c free iff gaps c-1,c not selected
        if not((s>>c)&1 or (c and (s>>(c-1))&1)): E.append(off+c)
    for g in range(n):
        if (s>>g)&1: E+= [off+n+2*g, off+n+2*g+1]
    return E
m=3*a+3*b; L=pats(a); R=pats(b)
print(m,len(L)*len(R))
for s in L:
    for t in R:
        E=piece(a,s,0)+piece(b,t,3*a); print(len(E),*E)
