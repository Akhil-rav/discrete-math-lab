# Recovering cycle lengths from legal-move histories

Start the triangle-free process from an n-vertex disjoint union of simple cycles, each of length at least four. Observe the number Q of open pairs before and after each move. For t>=1 consider only the event that the first t losses are exactly 5,6,...,4+t. The upper bound on a loss in a regular starting graph makes this the greatest possible loss at each successive step.

**Working result.** Given n, the initial Q, the one-step loss law and these event probabilities, the graph is determined within the class of unions of even cycles. The same is true within the class of unions of odd cycles. More generally it suffices to know in advance at most one allowable component length from each pair (7,8), (9,10), (11,12), ... . These are statements about exact laws from a prescribed initial state; a single sample path does not supply the probabilities.

### The polynomial being observed

Let C_l(z) count subsets of vertices of a cycle of length l with pairwise distances at least three, by cardinality. Write P_m(z) for the path version on m vertices, with P_0=1. Write c_l for the number of l-cycle components. By the [maximum-loss star argument](maximal-loss.md), after choosing a center x the leaves must be at distance at least four from x and at pairwise distance at least three. On x's own cycle the eligible vertices form a path of length max(0,l−7) in **vertices**; paths through the omitted arc cannot shorten a distance to less than three. Thus the polynomial of rooted leaf sets is

    H(z) = F(z) sum_l l c_l P_max(0,l−7)(z) / C_l(z),
    F(z) = product_l C_l(z)^c_l.

Here H(0)=n. For t>=2, the number of ordered histories of the stated loss word is t! times the coefficient of z^t in H. Each such star of added edges has exactly one center. For t=1 divide the coefficient by two, as either endpoint can be chosen as center. All histories of a given loss word have the same probability: multiply the observed word probability by the product of its pre-move open counts to get the history count. If a prescribed prefix would have no remaining move, any longer word has count zero. The one-step calculation [here](further-results.md) gives c_4, c_5 and c_6. When Q=0 the single component must be a 4- or 5-cycle and n distinguishes them.

### Where a component first changes H

The following formal power series calculation compares cycles of arbitrary lengths. Work with z=−y². The characteristic equation x³−x²−z=0 has one root L=1+O(y²) and two small roots

    a = y+y²/2+O(y³),     b = −y+y²/2+O(y³).

For the last assertion invert x sqrt(1−x) at zero as a power series and substitute y and −y. The large root is even in y. For l>=4, C_l=L^l+a^l+b^l. One direct proof reads a cyclic binary word with chosen positions separated by at least two blanks. Use three states recording the compulsory blanks still to be read. From state 0 either read a blank and stay or choose a position of weight z and move to state 2. The other transitions are 2 to 1 and 1 to 0. The trace of the lth power counts the cyclic words with a distinguished starting index: each legal word has a unique state at that index, including the all-blank word. The matrix has characteristic polynomial x³−x²−z.

The path recurrence P_m=P_(m−1)+z P_(m−3) for m>=3 starts at 1,1+z,1+2z. Its generating function is (1+zv+zv²)/(1−v−zv³). Partial fractions therefore give

    P_m = sum over x=L,a,b of x^(m+3)/(3x−2).

Indeed the coefficient of 1/(1−xv) is (1+z/x+z/x²) divided by the product of (1−x'/x) at the other two roots. Using z=x²(x−1) reduces that coefficient to x³/(3x−2).

Put U=L^(−4)/(3L−2) and t=ceil((l−4)/2). For l>=7 the normalized one-component contribution has expansion

    P_(l−7)/C_l = U − gamma_l (−1)^t z^t + O(z^(t+1)),
    gamma_l = 1 if l is even, (l−1)/2 if l is odd.

To check the coefficient, the denominator differs from L^l by O(y^l), of strictly higher order than y^(2t). The small-root part of the numerator is the sum of x^p/(3x−2) at a,b, where p=l−4. For even p its first term is −y^p. For odd p the two degree-p terms cancel. Expanding the denominator as −(1+3x/2+...)/2 and using the displayed roots gives −(p+3)y^(p+1)/2. The remaining series is even in y, and division by L^l preserves the leading term. Since y^(2t)=(−1)^t z^t this gives the stated signs.

Compare two cycle types on the same number of vertices with matching counts through length six. Let l be the smallest length with different multiplicities. The factors from lengths below l agree in F; for larger lengths j, C_j/L^j=1+O(y^j). Since both graphs have the same total length, their F factors agree through order y^(2t). In the sum defining H, subtract the common nU. The shorter-length terms then cancel. Inside a fixed parity class, or under the stated one-choice-per-pair condition, all longer allowable lengths first contribute at higher order. The first difference of H is consequently at z^t, where its signed coefficient is

    − l (c_l−c'_l) gamma_l (−1)^t.

The constants of both F factors are one. This proves the reconstruction claim and gives the exact earliest distinguishing *maximum-loss* word for such a pair of graphs. Other loss words could distinguish the graphs sooner.

**A two-component example.** Compare the cycle on 2k vertices with two cycles of length k, for any k>=8. The comparison just proved applies directly because the first differing length is k and 2k contributes strictly later. The difference in their ordered history counts is zero up to t−1 and equals 2k t! gamma_k (−1)^t at t=ceil((k−4)/2), in the order single cycle minus double cycle. In particular the sign need not be positive.

**Boundary of the investigation.** For mixed parities two different lengths can first contribute at the same order. The triangular proof therefore does not settle arbitrary unions. [cycle_histories.py](cycle_histories.py) checks the product formula against direct subsets on small examples and compared all 197,895 admissible cycle types on 4 through 66 vertices, using the short counts and the entire H polynomial. There were no collisions at fixed n in this range. No priority claim is made for the inverse result. The ingredients are elementary path and cyclic spacing polynomials and the [triangle-free process](https://www.math.cmu.edu/~tbohman/papers/r3t.pdf).

Run `python check_cycle_moves.py` from this directory to compare the leaf counts with legal graph moves. It checks each of the first three prefix counts on all 19 cycle types through 12 vertices, recomputing open pairs after each edge addition.
