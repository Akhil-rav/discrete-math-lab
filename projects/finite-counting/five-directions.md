# Five calculations: what can the data recover?

## 1. Bohman: halve the sufficient ladder width

In the [finite-horizon proof](horizon.md), the bound on k comes from comparing entire radius-8t balls. One can instead compare only the images of the small test graphs. **Every even k > 8t suffices**, with t >= 1. This is a sufficient width, not a sharp threshold.

Both closures of the strip cover the same column cycle. More explicitly both are quotients of the infinite two-row strip by translation through k columns, with or without a row swap. For a connected test graph F on s<k vertices, root a spanning tree of F. Choose any root image in either finite strip and fix a lift of that image to the infinite strip. A homomorphism of the tree lifts uniquely along its edges because incident edges project bijectively. For each nontree edge its fundamental closed walk has length at most s (a simple tree path followed by the edge). In a lift of the walk, the column displacement is a multiple of k and at most s in absolute value, hence zero. The only two points over the same vertex with equal column coordinate are identical, so this edge closes in the strip too. Thus rooted homomorphisms of F correspond bijectively to homomorphisms into the infinite strip with fixed root image. These counts are finite and independent of the root by strip symmetry. Multiplication, quotient-by-kernel, and inclusion-exclusion now give the induced pattern counts used in the earlier argument for all s<=8t. Initial Q agrees because the two radius-two balls agree. No early termination: after at most t moves some vertex still has degree three, so at most 3(3+t) other vertices lie within two edges of it; this is less than 2k-1 for k even >8t. The support separation and history argument are unchanged.

## 2. Lavrov: a statistic invisible to the mean but visible to the variance

Let G be a disjoint union of cycles of lengths at least six, with n total vertices and c six-cycle components. The number of open pairs is Q=n(n-1)/2-2n. Write D for the number lost on adding a uniform legal pair. Its complete distribution is:

| D | 1 | 3 | 5 |
|---|---:|---:|---:|
| Number of choices | 3c | n-6c | Q-n+3c |

Indeed a legal uv normally costs itself and four other pairs (u to each neighbor of v and vice versa). A length-three path from u to v saves two of the four: those two pairs were already closed. These are the only savings. Each cycle of length at least six has one unoriented length-three path per vertex. Only antipodes of a 6-cycle support two such paths, saving all four. This proves the table, including choices across components.

Consequently E[D]=5-2n/Q is blind to c, but E[D²]=25-16n/Q+24c/Q determines c exactly. For example C14 and C6 plus C8 match in n, degrees, Q and drift, yet the latter has three moves losing just one open pair and the former has none. This is a statement about reachable states, not their prevalence in a random run.

## 3. He: mixed stars, including every extremal tournament

For integers a,b>=1, ask for a center with a outward and b inward leaves. The least tournament order which forces such a star is **2(a+b)-1**. Moreover the unique structural form of the avoiders on one fewer vertex is a regular block of size 2b-1 beating every vertex of a regular block of size 2a-1. Uniqueness here concerns the decomposition, not isomorphism of the regular blocks.

In an avoiding tournament let L be vertices with outdegree <a, and H the others, each of indegree <b. Internal arcs of L give |L|(|L|-1)/2 <= |L|(a-1); similarly |H| <= 2b-1, with the empty cases immediate. At the maximum order both bounds are equalities. Every low vertex exhausts its outgoing budget inside L; likewise every high vertex exhausts its incoming budget inside H. Thus the blocks are regular with all cross arcs H to L. Conversely this construction works since regular tournaments exist on every odd order (cyclic orientation). On labeled vertices the count is binomial(2a+2b-2,2a-1) times R(2a-1) times R(2b-1), where R counts labeled regular tournaments. This is an elementary extremal exercise; see [Dross and Havet](https://www.sciencedirect.com/science/article/pii/S009589562100040X) for the broader unavoidability problem.

## 4. Mani: recover girth and the number of shortest cycles from moments

Let X count monochromatic edges of a finite simple graph with m edges under iid uniform q-coloring (q>=2). Compare X with B~Binomial(m,1/q). If the graph has girth g, all factorial moments below g agree. At order g the exact excess, in binomial-moment normalization, is

    E[choose(X,g)] - E[choose(B,g)] = (# cycles of length g)(q-1)/q^g.

Expand choose(X,j) over j-edge subsets. Below girth every such set is a forest, so contributes q^(-j). At j=g the only cyclic sets are precisely the edge sets of shortest cycles. Their probability is q^(1-g), and each is counted once. For a forest the full law is binomial. Hence, given q and m, the first mismatch and its size recover the girth and number of shortest cycles; no mismatch means a forest. This is an elementary consequence of the standard subgraph moment expansion, not a claim to have invented it. See [Bhattacharya, Diaconis and Mukherjee](https://sites.stat.columbia.edu/sumitm/edge_color.pdf).

## 5. Gotti: every length set for generators 6, 9, 20 has at most one internal gap block

Here a gap block is a maximal run of missing integers between attainable lengths. This is stronger than identifying the first noninterval at 60. It concerns length **sets**, not the number of factorizations at each length.

For target N choose the largest C>=0 with 20C<=N and N-20C divisible by 3. If there is none, there are no lengths. Put u=(N-20C)/3, so 0<=u<20. The feasible candidates for the number of 20s are C-3j with 0<=j<=floor(C/3). Let s=u+20j. Solving 2a+3b=s shows that a+b runs from ceil(s/3) to floor(s/2): indeed if h=a+b then a=3h-s and b=s-2h. Thus the slice is the integer interval [C-3j+ceil(s/3), C-3j+floor(s/2)], empty only for s=1.

Both endpoints increase with j. The separation (next lower endpoint minus current upper endpoint) is d(s)=ceil((s+20)/3)-3-floor(s/2). Since d(s+6)=d(s)-1 and the six values at s=20,...,25 are 1,1,0,1,0,0, all slices after the first join without any missing integer. The only possible gap block therefore occurs between the first two nonempty slices, and occurs there precisely when C>=3, u!=1 and d(u)>1. Its size is d(u)-1 (at most three, by checking u=0,...,19). For N>=100, C>=3 and the block size is periodic with period 60: replacing N by N+60 adds 3 to C and leaves u fixed. Period 60 here need not be the least period. General delta-set periodicity is older: [Chapman, Hoyer and Kaplan](https://www.math.uci.edu/~nckaplan/research_files/deltasetsperiodic.pdf). No priority claim for this particular formula.
