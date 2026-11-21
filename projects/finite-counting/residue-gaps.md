# Factorization gap blocks on residue classes

Fix coprime integers p>=2 and d>=1. Take coprime a>=2 and b>(p+d)a. Use generators pa,(p+d)a,b. They form a minimal generating set: the second is not divisible by the first, and the third is not divisible by a. For a fixed target N and residue r modulo d, list its attainable lengths congruent to r. A gap block on this lattice is a run of missing grid points *between two attained grid points*; going from 7 to 10 is not a gap when d=3.

**Proposition.** Each residue class has at most ceil(p/d) gap blocks, uniformly over a,b and N. For every coprime p,d such as above the bound is sharp for some generators and target. At d=1 this gives the earlier sharp p-gap bound. This is an all-target statement, not an eventual periodicity claim.

**Proof of the bound.** Let C be the largest nonnegative candidate for the number of b summands with N-bC a nonnegative multiple of a (if none exists there are no lengths). Put u=(N-bC)/a. The possibilities are c=C-aj, 0<=j<=floor(C/a), with s=u+bj. For fixed j solve px+(p+d)y=s. Writing h=x+y, a solution exists at h exactly when s/(p+d)<=h<=s/p and ph is congruent to s modulo d. Thus its lengths are the points of one residue class in the closed real interval

    I_j=[C-aj+s/(p+d), C-aj+s/p].

The residue is C+p^(-1)u + j(p^(-1)b-a) modulo d (use the sole class for d=1). Write P for its period as j varies, P=d/gcd(d,p^(-1)b-a). For a fixed attainable residue the contributing indices are j0,j0+P,...; after projecting all their intervals onto the same grid, each is an interval of grid points, possibly empty. Both real endpoints increase with j because b>(p+d)a.

The separation of I_(j+P)'s left endpoint from I_j's right endpoint equals

    -aP + bP/(p+d) - sd/[p(p+d)].

When j>=pP/d, we have s>=pbP/d and this separation is negative. From the first such index on, the union of the real intervals is a single interval; intersecting that union with the common grid commutes with taking the union. This also handles empty individual slices. Before that threshold there are at most ceil(p/d) indices on a progression of step P with nonnegative first term. At most that many early intervals plus one tail interval give at most ceil(p/d) internal gap blocks. If the sequence ends earlier the same upper bound holds.

**Sharpness.** Let H=ceil(p/d), take a=d+1, and let b=ap+d(aM+1) for arbitrarily large positive integers M. Then b is coprime to a and b congruent to ap modulo d, so P=1. For N=Ha*b, C=Ha and u=0, and there are H+1 slices j=0,...,H in the same residue class. Slice 0 is a singleton. All later real widths grow without bound as M grows. For j=0,...,H-1 the separation between successive real intervals is

    -a + b(p-jd)/[p(p+d)].

Each p-jd is strictly positive, so choose M large enough that each separation exceeds 2d and each nonsingleton slice has width greater than d. All are then nonempty on the grid and each join leaves a missing grid point. This gives exactly H gap blocks.

**Why the lattice matters.** For 4,10,25 all generators are 1 modulo 3. At N=20t, replacing five 4s by two 10s repeatedly realizes the t+1 lengths 5t,5t-3,...,2t. Every attainable length is congruent to 5t modulo 3, so on the ordinary integer line there are at least t internal gap blocks. There is no corresponding uniform ordinary-gap bound here.

**Relation to literature.** This proof uses overlapping slices of an integer cone. [Moskowitz and O'Neill](https://arxiv.org/abs/2311.05786) give an eventual structure theorem for general numerical semigroups using derived semigroups and Apery sets. [Chapman, Hoyer and Kaplan](https://www.math.uci.edu/~nckaplan/research_files/deltasetsperiodic.pdf) study eventual delta-set periodicity; the delta set records sizes of jumps, not their number of occurrences. A complete comparison with gluing-specific all-target bounds is still needed before any novelty claim. The proof here establishes the bound regardless of priority.

### Per-semigroup refinement: earliest attainment, not just a uniform bound

Let P be the residue period above, B=bP and A=aP. Assume B is representable using p,p+d (this holds automatically for p=2,d=1 since b>3a>=6). For representable s let m(s), M(s) be the smallest and largest number of summands in representations of s by p,p+d; both are zero at s=0. Define

    delta_j = m((j+1)B) - A - M(jB),   j>=0.

These differences are multiples of d. They are nonincreasing: add any fixed representation of B, of length h, to obtain m((j+2)B)<=m((j+1)B)+h and M((j+1)B)>=M(jB)+h. Eventually the real intervals in the proof above overlap, so the two rounded endpoints differ by at most d in the forward direction. Let K count the initial indices with delta_j>=2d. The exact maximum number of internal gap blocks on one residue class, over all targets in this semigroup, is K. For 1<=j<=K, **the least target with j or more such blocks is j*a*b*P**.

Proof: fix an arbitrary target and residue class and start at its first nonempty slice, with reduced target s0 and number of b-summands c0. All subsequent candidate slices at spacing P are nonempty because B is representable. The jth slice uses c0-jA copies of b and has grid endpoints c0-jA+m(s0+jB) and c0-jA+M(s0+jB). Choose any factorization length h0 of s0. By addition, its next join has separation at most delta_j: use m(s0+(j+1)B)<=h0+m((j+1)B) and M(s0+jB)>=h0+M(jB). Thus there are at most K gap blocks. (Even if rounded endpoints tie, a separation exceeding d gives exactly one block; endpoints are nondecreasing on the common grid.) To have j joins requires c0>=jA, hence target >=jAb. Conversely at target jAb take the residue of the pure-b factorization. Its slices correspond exactly to 0,B,...,jB and have those first j separations. For j<=K all are gaps. This proves equality and earliest attainment simultaneously.

For p=2,d=1 this gives a particularly short classification. With b>3a, any gap occurs iff ceil(b/3)-a>=2, first at ab. Two occur iff ceil(2b/3)-a-floor(b/2)>=2, first at 2ab. More than two are impossible. For a=3,b=20 this gives one possible block and first target 60; a=2,b=25 gives two and first double-gap target 100. No assumption is made that the refinement holds when B is not representable.

The independent generator-addition check in [earliest_gaps.py](earliest_gaps.py) tests the first attainment for 551 parameter choices.
