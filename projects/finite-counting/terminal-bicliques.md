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
