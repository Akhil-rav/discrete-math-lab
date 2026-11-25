# A neutral reversal need not lead downhill

Let S count stars consisting of one outgoing and two unordered incoming leaves in a tournament. Edges between leaves are unrestricted. Can every tournament reach a global minimum using single-edge reversals that never increase S? The small cases in [the descent experiment](star-descent.md) suggest yes. The answer in general is **no**.

**An example on ten vertices.** Take a transitive triple and a regular tournament on seven vertices. Direct all cross edges from the seven to the three. The outdegrees are 0,1,2 and seven copies of 6. The star count is 196. The only neutral moves exchange consecutive vertices of the transitive triple, and every other reversal strictly increases the count. Thus even an unlimited number of neutral moves cannot help. A transitive five below a regular five has star count 190 on the same ten vertices. No assertion that 190 is optimal is needed.

**Reversal formula.** Write N=n-1 and f(x)=x(N-x)(N-x-1)/2. Then S is the sum of f over all outdegrees. If an arc points from a vertex of score a to one of score b, its reversal changes S by

    (a-b-1)(4N-2-3(a+b))/2.

Indeed a+b stays fixed and the product of the two scores increases by a-b-1. Substituting into the cubic gives the formula. In particular if n is not a multiple of three, all neutral reversals interchange scores differing by one.

**An infinite family.** For t>=1 put n=6t+4, N=6t+3. Take a lower transitive tournament on k=2t+1 vertices and an upper regular tournament on r=4t+3 vertices with all cross edges pointing down. The lower scores are 0 through k-1 and all upper scores equal v=4t+2. Regular tournaments of each required odd order exist: on a cyclic ordering orient each edge toward the next (r-1)/2 vertices.

- In the lower part every arc points from a larger score to a smaller one. The second factor in the reversal formula is positive since the sum of the two scores is at most 4t-1. The change vanishes exactly for consecutive scores. Reversing such an arc interchanges two consecutive positions in the total order.
- In the upper part both scores are v. The two factors are -1 and -2, so the change is +1.
- For a cross arc from v to i<=2t the first factor is positive and the second is at least 4N-2-3(v+2t)=6t+4>0.

Every neutral move therefore stays in the same construction, with the same cut and the same upper tournament. A cheaper competitor is obtained by using k+2 lower vertices and a regular upper part of size r-2. Its common upper score is v+1. Relative to the old count its change is

    f(k)+f(k+1)+(r-2)f(v+1)-r*f(v) = -8t^3-2t^2+3t+1 < 0.

This gives nonoptimal plateaus with no nonincreasing route out at infinitely many orders. The [escape-height analysis](escape-heights.md) identifies the first such order, determines the height of this family, and gives another family with unbounded height. Priority in the literature has not been established.
