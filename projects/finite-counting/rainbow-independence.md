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

### Equality and uniqueness

Suppose the family is nonempty and its smallest target has size k at least two. A strict move toward equality between red and blue increases the success probability **strictly** if and only if at least k-2 other labels have positive mass. With fewer such labels even after balancing there are fewer than k usable colors, so success is impossible.

For sufficiency, fix a smallest target T. In the partial observation from the proof, expose k-2 specified positions of T in distinct colors outside red and blue, and mark every other position in the ground set. This observation has positive probability, including when k=2. No target can already succeed with at most one marked position, since it would contain at most k-1 positions. But T survives with exactly two marked positions, so the graph in the proof has an edge. Its component has size at least two; its monochromatic probability strictly decreases under balancing. All remaining factors are positive and nonincreasing. Thus conditional success strictly increases on an observation of positive probability.

In particular, if q is at least k, the uniform distribution is the unique maximizing vector on q labels. A distribution supported on fewer than k labels has zero success probability while uniform gives T positive probability. Any other nonuniform distribution has at least k positive labels, so balancing any unequal pair strictly improves it. A target of size at most one makes success certain and is excluded from this conclusion.

[check_palette_balancing.py](check_palette_balancing.py) checks the strict and equality cases by enumeration on every nonempty family formed from the eleven subsets of sizes two through four on four positions. It tests six palette transfers per family, including initially unused colors, for 12,282 exact comparisons.

### Fixing the number of edges of each color

The independent draws assumption matters even for perfect matchings. On the cycle with 2n edges, n at least two, take exactly n colors. Give two of them multiplicities three and one and every other color multiplicity two. Shuffle this fixed inventory uniformly over the edges. Moving one copy from the most frequent color to the least frequent color makes the inventory perfectly balanced, but **reduces the probability of a rainbow perfect matching by one third**.

Indeed, distinguish the tokens even when their colors agree. The first alternating matching receives a uniform n-subset of the 2n tokens. With multiplicities (3,1,2,...,2), exactly 3 times 2^(n-2) subsets make that matching rainbow. Both alternating matchings cannot be rainbow, since three copies of one color must be split between them. Thus success has probability 6 times 2^(n-2) divided by binom(2n,n). With two tokens of every color, either both matchings are rainbow or neither is. Exactly 2^n subsets give success, yielding two thirds of the previous probability.

More generally, for positive multiplicities c summing to 2n, the number of successful subsets is 2 e_n(c) minus the number that make both matchings rainbow. The elementary symmetric sum counts the ways to take one token of each of n colors. The intersection count vanishes if any color has more than two tokens. Otherwise, with d doubled colors, it is 2^d binom(2n-2d,n-d): split every doubled color and choose the remaining tokens from the singletons. Divide by binom(2n,n) for the probability. [check_cycle_inventory.py](check_cycle_inventory.py) checks every multiplicity partition on cycles with 4, 6, 8, 10 and 12 edges by direct subset enumeration.

### Which inventory is best on a cycle?

Fix exactly q used labels on the 2n-cycle. For q<n success is impossible. For n<=q<=2n put d=2n-q and l=q-n. Up to renaming, the only possible maximizers are the balanced inventory B (d doubles and 2l singles) and, when d>=2, the inventory T obtained by changing two doubles to a triple and a single.

| Condition | Maximizers |
|---|---|
| d=0 or 1 | B |
| d>=2 and l=0 | T |
| l>=1 and d=2 or 3 | T |
| d=4 and 1<=l<=6 | T |
| d=5 and l=1 | T |
| d=6 and l=1 | B and T |
| All remaining cases | B |

**Reduction.** If every multiplicity is at most two the inventory is B. Otherwise the intersection count is zero and success is proportional to the elementary symmetric sum e_n(c). A transfer from entries a,b with a>=b+2 to a-1,b+1 increases e_n by (a-b-1)e_(n-2) of the other entries, which is positive since q>=n. Reduce a largest entry to three whenever it exceeds three, transferring the excess to singles (there must be a single while any entry exceeds two since the mean is at most two). Hold that triple fixed and balance the remaining entries. Their mean is strictly below two, so the result is T. Every transfer strictly improves success while retaining a triple.

**Comparison.** Assume d>=2. The intersection count for B is 2^d binom(2l,l). Moving from T to B increases e_n by e_(n-2) of the remaining d-2 doubles and 2l singles. Write

    R = sum over i=0,...,min(d-2,l) of
        binom(d-2,i) 2^(-i) binom(2l,l+i) / binom(2l,l).

Selecting all but i of the remaining doubles gives exactly this expression after dividing e_(n-2) by 2^(d-2) binom(2l,l). Consequently T wins for R<2, B wins for R>2, and equality gives the tie.

For l=0 the sum is one. For l>=1 it is nondecreasing in d and l: each binomial ratio is the product of (l-j)/(l+j+1) over j=0,...,i-1 for i<=l, and is zero before then. For d<=3 the sum is below two. For d=4 its sign relative to two is the sign of l(l-1)-4(l+2), which changes between six and seven. For d=5 it is below two at l=1 and above two at l=2. At l=1 it equals 1+(d-2)/4, and for d>=3 the i=1 term strictly increases with l. These comparisons give all rows of the table. The inventory checker also exhausts all maximizing types for n from two through fifteen.
