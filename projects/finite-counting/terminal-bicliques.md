# How often does the triangle-free process end in a biclique?

Start with the empty labeled graph on n vertices. At each step add a uniformly chosen open pair, meaning an absent edge whose addition would create no triangle. A complete bipartite graph with both parts nonempty is terminal. Its probability can be computed without following paths that have already chosen an edge inside one of its parts.

**Stars.** For n at least three the probability of terminating in a star is

    2^(n-1) n! / (2n-2)!.

After the first edge either endpoint can become the center, and the two final events are disjoint. If a particular center has accumulated m edges and all other edges are absent, exactly m(m-1)/2 absent leaf pairs are closed. Thus there are (n+m)(n-1-m)/2 open pairs and n-1-m continue the star at this center. Multiply 2/(n+m) over m from 1 through n-2 and double the result.

**General cuts.** Fix the side of size a, labeling its vertices. Classify each of the b vertices on the other side by the subset S of its current neighbors. The state records the multiplicity c(S) of each subset. To compute the chance of completing this cut, assign value one to the full graph. At an earlier state every absent cross edge is open. For each i outside S there are c(S) choices that move one vertex from type S to type S union {i}. Sum the successor values with these multiplicities and divide by the total number of open pairs, including internal pairs. An internal move contributes zero to this fixed cut's success probability.

On the a-side an internal pair is open if no occupied type contains both its endpoints. On the b-side a pair is open if its types are disjoint, including pairs of distinct isolated vertices. These rules determine the whole recurrence from c. Since a connected bipartite graph has a unique bipartition up to interchange, multiply the empty-state probability by binom(a+b,a), dividing by two for equal parts. For fixed a there are at most binom(b+2^a-1,2^a-1) multiplicity vectors.

| n | Terminal star | Terminal K(2,n-2) |
|---:|---:|---:|
| 4 | 4/15 | 11/15 |
| 5 | 1/21 | 776/945 |
| 6 | 2/315 | 3584123/14189175 |
| 7 | 1/1485 | 16584270751/329983453800 |
| 8 | 8/135135 | 8766996399857300777/1230747867207658800000 |

Run [terminal_bicliques.py](terminal_bicliques.py) to regenerate the table. Independent propagation on all labeled graphs agreed for every bipartition size at n=3 through 6. These finite probabilities and elementary recurrence carry no priority claim.

## A lower bound from common-neighbor counts

Fix any labeled maximal triangle-free graph H. For each nonedge uv let c(uv) be the number of common neighbors of u and v in H. Then the probability of terminating at this particular H is at least

    product over nonedges uv of [1 - (2c(uv))!! / (2c(uv)+1)!!].

To see this, assign independent uniform arrival times in [0,1] to all pairs. Inspect pairs in increasing order and accept each legal pair. At every acceptance, all currently open pairs remain unexamined and their remaining order is uniform, so this gives the uniform-open-pair process. For a nonedge uv, define B(uv) as the earliest time at which a two-edge path in H from u to v has arrived, namely the minimum over common neighbors w of max(time(uw),time(wv)). The output equals H precisely when every nonedge arrives later than its B. Necessity follows from the triangle that blocked it. For sufficiency, induct through the arrival order: edges of H remain legal, and each nonedge has an earlier blocking path in H.

Conditional on the arrival times of H, the exact probability is the product of 1-B(uv) over its nonedges. These nonnegative factors are coordinatewise decreasing in independent arrival times, so their expected product is at least the product of their expectations. For completeness the two-function inequality in one variable follows from the nonnegative product of differences evaluated at two independent copies. Conditioning on one coordinate and inducting proves the inequality for product measures, and iterating handles any number of factors.

For fixed uv the c blocking paths use disjoint edge pairs. Thus Pr(B(uv)>x)=(1-x^2)^c, and integrating from zero to one gives E[B(uv)]=(2c)!!/(2c+1)!! by integration by parts. This proves the bound. For a fixed K(a,b) cut, the two types of nonedges have common-neighbor counts b and a respectively. For C5 every nonedge has one common neighbor, so the probability of a specified labeled pentagon is at least (1/3)^5. The product bound need not give the exact probability.

The uniform-open-pair model is the one studied by [Bohman, The triangle-free process](https://www.math.cmu.edu/~tbohman/papers/r3t.pdf). The bound above applies the elementary product-measure correlation inequality to that model. No priority claim is made.

## Exact verification by counting arrival orders

Fix the relative order of the m edges of H. For each nonedge compute the earliest rank at which a witness path has both edges present. Sort these thresholds in decreasing order as b_0,...,b_(s-1), breaking ties in any fixed order. Insert the corresponding labeled nonedges in that order. At insertion j every previous insertion lies after target edge b_j, so exactly m-b_j+1+j slots are legal. Deleting the inserted edges in reverse order recovers all choices uniquely. Multiply the slot counts, sum over all m! target orders, and divide by the factorial of the total number of pairs.

[check_terminal_orders.py](check_terminal_orders.py) implements this integer count independently of the open-pair recurrence. It agrees for every complete bipartite type on three through six vertices. For a specified labeled pentagon it gives 31/2835, above the common-neighbor bound of 1/243. The twelve labeled pentagons together have mass 124/945. Adding this to the two bipartite masses on five vertices gives exactly one.
