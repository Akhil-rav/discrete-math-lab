# What a second observation reveals about mixed cycle lengths

Use the notation and power-series expansions of [the cycle-history note](cycle-recovery.md). The input includes the vertex count and the multiplicities of lengths 4, 5 and 6, recoverable from the observations described there. All observations below are exact distributions from specified initial graphs.

**One experiment.** The rooted history polynomial H distinguishes every cycle type on a fixed number n of vertices for n < 168. With no bound on n it still distinguishes types within the class having at most four copies of each odd cycle length. Another sufficient restriction is at most seventeen copies of each even length.

**Proof.** Compare two types with the same short counts. Let (2s-1,2s), s >= 4, be the first pair of lengths with unequal multiplicities, and write u,v for their respective multiplicity differences. Substitute z = -y². By the expansion for the marked component in the linked note, the difference in H at degree 2s-4 in y is

    -[(2s-1)(s-1)u + 2s v].

Indeed, smaller component terms agree, all later pairs have higher order, and the unmarked products F agree to this order: factor out the common shorter cycles and normalize every remaining cycle by L to the power of its length. The total remaining length is fixed. Those normalized factors first differ at degree at least 2s. Thus they cannot affect the displayed coefficient.

Set g = gcd((2s-1)(s-1),2s) = gcd(s-1,2). Cancellation requires a nonzero integer multiple of

    (u,v) = (2s/g, -(2s-1)(s-1)/g).

Consequently one type contains at least (2s-1)(s-1)/g cycles of length 2s. For even s this costs at least 8 times 21 = 168 vertices; for odd s at least 10 times 18 = 180 vertices. In both parity classes the bound increases with s. The least possible absolute differences are at least five for u and eighteen for v. This gives all three assertions.

The 168 threshold is sharp **for this coefficient argument**, not necessarily for reconstruction. Eight 7-cycles and one 112-cycle have the same vertex count as twenty-one 8-cycles. Their degree-two coefficients in z agree, but the degree-three coefficients differ by -728 (first graph minus second). Five 9-cycles and one 135-cycle versus eighteen 10-cycles likewise first differ at degree four, by 1305. Run [mixed_cycle_examples.py](mixed_cycle_examples.py) to obtain these differences by polynomial multiplication.

**Two experiments.** For any cycle union G with all lengths at least four, the original observations on G and on the disjoint union of G with one known square determine every component length. This changes the observation model; it does not settle unrestricted recovery from G alone.

**Proof.** Marking the root in either component gives

    H(G + square) = (1+4z) H(G) + 4 F(G).

Here a square has four possible singleton leaves and no separated pair; fixing its root leaves no eligible vertex in the square. Thus the second experiment gives the entire unmarked polynomial F(G).

Now suppose both F and H agree for two distinct types, and choose the first differing pair as before. In F, the coefficient difference at degree 2s in y is

    (2s-1)u + 2v.

To see this, divide out common shorter factors and the large-root power for the remaining total length. All divisors are units of constant term one. In a normalized cycle factor of length k the correction is (a^k+b^k)/L^k. The two small roots are y+y²/2 and -y+y²/2 up to order three. For k=2s-1 the odd leading terms cancel, leaving coefficient k at degree 2s. For k=2s the coefficient is two. Every later length contributes strictly later. Multiplication adds these first corrections, counting multiplicities.

Together the two vanishing coefficients force

    (2s-1)u + 2v = 0,
    (2s-1)(s-1)u + 2s v = 0.

Subtract s-1 times the first equation from the second. This gives 2v=0 and then u=0, contradicting the choice of pair. Hence the two observations determine the type. No priority claim is made.
