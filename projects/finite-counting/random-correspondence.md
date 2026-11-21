# Random full correspondence assignments on a parallel-path graph

This continues [the elementary independence criterion](correspondence.md). The graph has r>=3 internally disjoint paths between two terminals, no other core edges; path lengths do not enter the answer. Put independent uniform permutations of [q] on its edges, in chosen orientations. Independently choose uniform vertex colors. We sample the **assignment** and ask whether, conditional on that assignment, probabilistic independence of the edge-conflict indicators forms the independent sets of a matroid. We do not average out the assignment before testing independence.

### Exact deterministic test

Let sigma_i be the total permutation along the ith path, all read in the same direction. Say i and j are *separated* if their permutations agree on exactly one input color. This is exactly the condition allowing their simple cycle in a unicyclic independent set. Mark i related to j when i=j or they are not separated.

The fixed assignment gives a matroid **if and only if this relation is an equivalence relation**. Reflexivity and symmetry are automatic. If transitivity fails, three paths form the circuit-elimination obstruction in the preceding note. If the relation is transitive, give each equivalence class a different element of a cyclic group large enough for the number of classes. Put that element as the path gain. Now the identity-product simple cycles are exactly those pairs of paths in the same class: every simple cycle is two full paths. The frame-matroid exchange argument applies. Attachments that are trees do not change the test.

For r=3 failure is exactly one separated pair, not zero or two. For every fixed q>=4 it has strictly positive probability by the explicit K(2,3) assignment. Because disjoint triples of path totals are independent, the chance the full r-path assignment yields a matroid is at most (1-f_q)^floor(r/3), where f_q is this three-path failure probability. In particular it tends to zero with r at fixed q>=4. At q=2,3 it is always one.

### Limiting probability with a large palette

Fix r. As q grows the numbers of agreements for the choose(r,2) pairs of path totals converge jointly to **independent Poisson variables of mean one**. Consequently the limiting probability of a matroid on this graph is

    sum over set partitions P of [r] of
        (1-p)^within(P) p^(choose(r,2)-within(P)),     p=1/e,

where within(P) is the sum of choose(block size,2). Distinct equivalence relations give disjoint events. With r=3 the limiting failure probability is 3p(1-p)^2. This is a fixed-r limit, not a uniform estimate for r growing with q.

**Factorial-moment proof.** The path totals are independent uniform permutations since edge permutations are independent and the paths share no edges. For arbitrary fixed nonnegative integers k_ij, expand the product of falling factorials of agreement counts. For each pair ij choose an ordered list of k_ij distinct input rows. Let K=sum k_ij. In the terms where all K rows are distinct there are (q)_K choices. First generate independent uniform outputs in every permutation column at these rows, then condition on no within-column repetition; this is exactly the permutation restriction law. Before conditioning, the K required pair agreements have probability q^(-K). Even conditionally on the agreements, distinct rows are independent and each single entry is uniform, so by a union bound the probability of a within-column repeat is O(1/q). The unconditioned repeat probability is also O(1/q). Thus the total contribution of distinct-row terms tends to 1.

If only m<K distinct rows occur, there are O(q^m) choices of a fixed coincidence pattern. At each row the equality constraints are a nonempty simple graph on the permutation columns: repetitions of one pair within a row are excluded by the falling factorial. Under sampling with replacement, each row costs a power q^(-rank), with rank the number of vertices minus the number of components on its incident columns. A row with two or more distinct edges has rank at least two. Thus the total rank is at least m+1. Conditioning on injectivity in each column increases probabilities by at most 1/(1-O(1/q)). All row-overlap terms together are O(1/q). The mixed factorial moments therefore tend to those of independent Poisson(1) variables. The joint Poisson law is moment-determinate (finite joint moment-generating function near zero); the factorial-moment criterion gives the claim. Point-pattern probabilities for the indicators of exactly one agreement converge as well, by using thresholds at half-integers.

**Scope and attribution.** Poisson limits for fixed points and rare agreement counts are classical; the proof is included rather than a claim of a new Poisson limit method. The gate being tested is transitivity of the nonseparation relation for a *single* full correspondence assignment. This is not the DP color function and not a probability that a graph is colorable. No priority claim has been settled for this probability formula.
