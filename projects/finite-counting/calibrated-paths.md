# Recovering signed paths with one calibrated addition

The host consists of at least two internally disjoint paths between known terminals. The path lengths and their binary twist signs are unknown; there are no other edges. Observe only the exact distribution of the total number of conflicts under uniform independent binary vertex colors as in [the path law](binary-path-law.md). Add a new vertex and an untwisted path of length two through it between the terminals, leaving the original assignments unchanged. Observe the distribution again.

**Claim.** The two laws determine the original multiset of (length, sign) pairs. Even the absolute signs are recovered relative to the added positive path. Bits on the individual edges of an original path are not identified.

**Extracting two polynomials.** Let G(z) be the probability generating function before the addition. Every edge has conflict probability one half, so m=2G'(1) is the edge count, also for inconsistent twists. Use the [even-subgraph expansion](binary-path-law.md) in the form

    E(x) = (1-x)^m G((1+x)/(1-x)).

This sums the signed monomials indexed by even subsets of paths. Write O for the same sum on odd subsets. Apply the transform to the second law using m+2 in place of m. The result is E(x)+x?O(x): the added path is either absent or present, and in the second case must be paired with an odd subset of original paths. Subtraction and division by x? recover O.

**Reading lengths and signs.** If the unknown signs are s_i, put A=E+O and B=E-O. Then

    A = product (1+s_i x^l_i),   B = product (1-s_i x^l_i),
    AB = product (1-x^(2l_i)).

At the shortest remaining length l, the coefficient of degree 2l in AB is minus the total number of remaining paths of length l. The coefficient of degree l in A is the number of positive paths of that length minus the number of negative paths. Thus both multiplicities are known. Divide out the recovered factors in A and AB before increasing l. This gives an integer algorithm and proves uniqueness even when several lengths coincide or their signs cancel. Using A alone would be insufficient: (1+x^l)(1-x^l)=1-x^(2l).

**Why compare with the unmodified host?** Even knowing the number of paths and all lengths in advance does not always make the modified law alone sufficient to recover absolute signs. Take three length-two paths, all negative, or three length-two paths with two positive and one negative. After adding a positive length-two path the two assignments have respectively one and three positive signs. Global negation and a permutation give identical modified laws. The original laws differ, since the signed sums over pairs are 3 and -1 respectively.

**One measurement with a longer path.** If an upper bound M on the original total length is available before modifying the graph, add a positive path of length M+1 instead. In the transformed law E+x^(M+1)O the two coefficient ranges are disjoint. Thus this single modified-host law suffices, at the price of a larger modification. This is an upper bound on a sufficient probe length, not a minimality result.

**Source context and checks.** The separation into two terminal states is standard in the [two-terminal Potts partition-function framework](https://discovery.ucl.ac.uk/id/eprint/1399078/1/Sokal_130930133.pdf). The previous note already treats the unsigned four-path reflection, so that ambiguity is not a discovery here. The inverse procedure above is derived directly; priority has not been established. [calibrated_paths.py](calibrated_paths.py) constructs the two laws by conditioning on the terminal bits and then feeds only their coefficients to the decoder. It checks 564 assignments on two to four paths of lengths one through four, with at most one unit path. No random sampling or rounding is involved.
