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

## Biased colors change the criterion

Now give every edge the same finite color distribution, still independently, and discard labels of probability zero. Suppose the support has at least k colors, k is at least two, and two positive probabilities differ. A family of size-k matchings then has mutually independent rainbow indicators exactly when its members are edge-disjoint. In fact every overlapping pair has strictly positive covariance.

To prove this, condition on the colors Z of the shared edges of two matchings. The private colors are independent, and each matching has the same conditional success probability f(Z). Thus the covariance equals Var(f(Z)). For at least two shared edges the event that two shared colors agree has positive probability and forces f=0. A distinct assignment to all shared positions also has positive probability and admits a successful completion. The variance is therefore positive.

For just one shared edge let its color be i with probability w_i. Then f(i)=(k-1)! times the elementary symmetric sum of degree k-1 in all the weights except w_i: the remaining positions must receive different labels other than i. Compare colors i and j. Terms using neither cancel, so

    f(i)-f(j) = (k-1)! (w_j-w_i) e_(k-2)(weights outside i,j).

Here e_0=1. The support assumption makes the symmetric sum strictly positive. Unequal weights therefore give two different conditional success probabilities. This proves the claim since edge-disjoint matchings depend on independent inputs. When the support has fewer than k colors all indicators are constant zero.

For the three-column ladder with color probabilities (1/2,1/3,1/6), a single matching succeeds with probability 1/6. The covariance of two matchings sharing one edge is 1/162. The probabilities of exactly zero, one, two and three rainbow matchings are respectively 191/324, 53/162, 25/324 and 1/162. The count consequently has a different law from the uniform-palette binomial example.

## Balancing two colors increases the chance of finding a rainbow matching

Fix any finite family of targets (for instance, all perfect matchings in a graph). Color each position independently from one common palette distribution. Keeping the sum of two color probabilities fixed and moving them closer together can only increase the probability that at least one target is rainbow. In particular the uniform palette maximizes this probability on every fixed number of labels.

**Proof.** Call the two colors red and blue. Reveal all colors except that each red or blue position is marked without revealing which one it is. The law of this partial observation depends only on their total probability. If the total is positive, each marked position is independently red with probability p equal to the red share of the total.

Discard every target already having a repeated unmarked color or at least three marked positions. If any remaining target has at most one marked position, success is certain. Otherwise every surviving target has exactly two marked positions and succeeds precisely when their colors differ. Form a graph on the marked positions by joining the two in each surviving target. Failure now means that every connected component is monochromatic. Its conditional probability is therefore

    product over components C of [p^|C| + (1-p)^|C|].

Each factor is symmetric and nondecreasing in the distance of p from one half, by differentiation (and is constant for singleton components). This proves the two-color statement after averaging over the partial observation. Zero total mass needs no change. To reach the uniform distribution in finitely many such steps, take one weight above the mean and one below, and transfer the smaller of their deviations from the mean. At least one additional weight reaches the mean at each step.

For the three-column ladder, success has probability 133/324 with weights (1/2,1/3,1/6), compared with 386/729 under the uniform three-color palette. The argument concerns the event that at least one target succeeds. It also applies to families with targets of different sizes. Priority has not been established.

The same optimization fails for simultaneous success. Take five positions, one center and four leaves, and use the four center-leaf pairs as targets. With two colors, every target succeeds precisely when all leaves have the color opposite to the center. This has probability p(1-p)^4+(1-p)p^4, which is 52/625 at p=1/5 and only 1/16 at p=1/2.
