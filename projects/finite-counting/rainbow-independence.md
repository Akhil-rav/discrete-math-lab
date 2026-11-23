# When are rainbow matching events independent?

Give each edge an independent uniform color from q labels. Choose any family of distinct perfect matchings of size k. Make a bipartite incidence graph with one node per matching, one per host edge, and a link for membership. For q at least k and q at least two, the rainbow indicators are mutually independent exactly when this incidence graph is a forest. For q below k all indicators are constant zero.

**Forest direction.** Root each nontrivial component at a matching. Expose its matchings in increasing distance from the root, revealing each one's edge colors as it is visited. A nonroot matching meets the exposed edges in exactly one position, its parent edge node. Conditional on everything seen, its chance of being rainbow is the same for each color at that position, namely p=(q)_k/q^k. A root has the same unconditional chance. Multiplying the conditional probabilities for any pattern of successes and failures gives independence.

**Cycle direction.** If two matchings share s at least two positions, both are rainbow with probability p squared divided by the probability that the s shared colors are distinct. Indeed, conditional on the shared colors, the two private parts are independent, and their success probabilities are constant on the distinct-color event and zero outside it. The divisor is strictly between zero and one.

Otherwise choose a shortest incidence cycle, using r at least three matching nodes. Among these matchings only consecutive ones intersect, each in its designated cycle position. An extra incidence to a cycle position would give a chord. An off-cycle position shared by nonconsecutive matching nodes would join them by a path of length two, shorter than either intervening cycle arc, yielding a shorter cycle. Consecutive nodes already use their unique intersection. Thus after the r shared positions are colored, all remaining positions of the selected matchings are private.

Write b=(q-2)_(k-2)/q^(k-2), using the falling factorial. Each matching succeeds with conditional probability b if its two shared colors differ, and zero otherwise. The chance that all r succeed is b^r times the probability that a cycle of length r is properly colored. The latter probability is

    [(q-1)^r + (-1)^r (q-1)] / q^r.

Indeed the numerator is the trace of the r-th power of the q-by-q matrix with zeros on the diagonal and ones elsewhere. Its eigenvalues are q-1 once and -1 with multiplicity q-1. Since p=b(q-1)/q, the joint probability differs from p^r by the nonzero cycle correction. This proves the converse for every allowed palette size.

**Three-column ladder.** Its three matchings can be written 012, 034 and 256 in edge labels. Their incidence graph is a tree. The number of rainbow perfect matchings therefore has the full Binomial(3,p) law, including at q=3 where p=2/9. In contrast, the three matchings of K4,4 given by the column permutations 0123, 0231 and 1203 are pairwise independent but have a cycle with r=3. At q=4 exactly 192 of the 4^9 assignments on their union make all three rainbow. Direct enumeration checks this count and the entire ladder distribution for q=1 through 5 in [check_rainbow_independence.py](check_rainbow_independence.py).

**Literature context.** Simultaneous rainbow events are strong hypergraph colorings. Replacing each target by a clique on its positions gives the usual chromatic-polynomial formulation, also recorded in [Foissy, Hopf algebraic structures on hypergraphs and multi-complexes, Proposition 2.1](https://doi.org/10.1016/j.aam.2026.103067). The independence argument above uses elementary conditioning and the cycle polynomial. Priority of the criterion has not been established.
