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

Hafner and Sendler, [Some asymptotic results on multiple matching](https://doi.org/10.2307/3212692), *Journal of Applied Probability* 11 (1974), 479–492, studied Poisson limits for column multiplicity patterns in exactly this random-permutation array. Their abstract classifies rows by multiplicities; here a statistic specifies the identities of the two path indices. The factorial-moment proof above directly covers that choice of indices.

### Exact probabilities for three paths

Write p for the probability that a uniform permutation of q colors fixes exactly one, and t for the probability that all three pairs of path totals agree exactly once. The three pair events are pairwise independent: condition on their one shared permutation. Inclusion-exclusion gives the probability of precisely one event as 3(p−2p²+t). Here p=q D(q−1)/q!, with D the derangement numbers.

For a finite calculation use simultaneous relabeling of the output colors to make the first path permutation the identity. The remaining two are independent uniform permutations, say A and B. To compute t, restrict A to permutations fixing exactly one point. For such A, mark the identity cells (i,i) red and the cells (i,A(i)) blue. On a cell used by B the required generating-function factors are z, w, or zw according to which marks are present. Expand each factor as one plus its increment. Any selected subset of cells must be nonattacking; if it has k cells there are (q−k)! ways to complete it to B. Thus, in the rook polynomial, mark a red-only cell by v(z−1), blue-only by v(w−1), and a doubly marked cell by v(zw−1). Multiply its coefficient of v^k z w by (q−k)! and sum over k and the admissible A. Dividing by (q!)² gives t. Setting z²=w²=0 throughout preserves the needed coefficients exactly.

Each cycle of A of length l>=2 yields one alternating cycle of 2l red/blue edges in the row–column graph. Its rook polynomial M_l counts matchings on that cycle. One edge is either absent (leaving a path) or present (delete both endpoints); along a path the two-term recurrence for selection of its last edge suffices. To sum over derangements of n labels, let R_0=1 and use

    R_n = sum_{l=2}^n [(n−1)!/(n−l)!] M_l R_(n−l).

The factor orders the other l−1 labels of the cycle containing the least remaining label. There are q choices for the one fixed point; the combined board polynomial is q (1+v(zw−1)) R_(q−1).

| Palette size | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Failure probability | 0 | 0 | 1/2 | 73/160 | 7/16 | 1519/3456 | 88709/201600 |

Run [three_paths.py](three_paths.py) to compute through q=30. It compares the result to every ordered pair of permutations through q=6. Direct testing of independence and exchange on the actual five-vertex graph is in [correspondence_checks.py](correspondence_checks.py) through q=4. At q=30 the failure probability is about 0.44090457.
