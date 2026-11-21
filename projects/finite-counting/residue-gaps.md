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
