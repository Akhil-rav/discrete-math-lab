# Independent referee report

Reviewed main revision `10cae2357be09f41a5eae4459e879d025ce99d67`.

## Proof audit

1. **Lemma 1, monotonicity — no gap found.** Pick a rainbow witness outside a
   failing list. Above $k$ colors there is a color unused by the witness. Merging
   it into any other class preserves all witness distinctions and all existing
   collisions. The strict upper endpoint is exactly where this step is needed.
2. **Lemma 2, triple criterion — no gap found.** At deficit two the only
   nonsingleton sizes are 3 or 2+2. If two tests contain the same pair,
   the third either contains it or has at least two edges outside it. If
   pair intersections have size at most one, a triple blocking all tests
   has to contribute three different two-subsets, producing precisely (b).
   Two tests can always be blocked by disjoint pairs as in the text.
   Necessity here uses the ambient rainbow-existence hypothesis: a coloring
   defeating the list must admit a witness elsewhere. On the prism, deleting
   the two closing rails leaves a ladder, and each deleted edge lowers the
   deficit by zero or one. This supplies that hypothesis. A matching size
   of at least three supplies the spare edges. The earlier ladder bound can
   also be bypassed: the word construction in Theorem 3 gives three tests
   satisfying (a),(b), whose sufficiency needs no ambient hypothesis.
3. **Theorem 3, optimal triples — no gap found.** The end rungs must occur in two distinct pairs of tests.
   Those pairs already intersect once. Condition (b) excludes an intersection
   in the third pair. Each interior column is then covered at least twice.
   Each chosen gap covers two columns in one test, and disjointness leaves
   only $k-1$ gaps, giving equality. Conversely adjacent gap labels differ,
   so only the two end rungs repeat. Fixing two distinct end labels removes
   all label symmetry. The off-diagonal entry of the triangle adjacency
   matrix to power $k-2$ is the stated Jacobsthal number. The statement expressly allows the empty gap set needed at $k=3$. In the parity remark the unspoken upper bound of two incidences at an
   interior column follows from its two adjacent gaps and gap disjointness.
   With a third intersection, precisely one interior column has one
   incidence and all others have two. The resulting odd total is impossible.
4. **Theorem 4, prisms — no gap found.** A rung splits each rail into even
   runs of uncovered vertices with forced path matchings. Without rungs
   there are four alternating rail choices for even $k$, two aligned and
   two twisted. For gap triples a column covered zero times would consume
   all three allowable pair intersections while wasting two incident gaps;
   the incidence total instead permits only one unused gap. With no such
   column, parity and (b) leave zero or two singly covered columns. These
   correspond to a properly labeled cycle or a path with distinct end labels.
   The trace of the triangle adjacency matrix to power $k$ gives the first
   count before division by six. For two twists, the gap matching can use
   at most one gap. For one twist, both gap matchings have at most one gap
   and share at least $k-4$ rungs. At $k=4$ an empty and a singleton
   share two rungs. Adjacent singleton gaps share one rung, and the twist
   meets the two matchings on distinct rails, violating (b). Opposite gaps
   work, giving two choices times two twists. These cases are disjoint.
5. **Theorem 5, fixed deficit — no gap found.** For the ordered column pair
   $i,j$, the gap on the far side of $j$ is valid even for adjacent
   interior columns. The three repeated pairs force the claimed antichain.
   The stationary probabilities are $2/3,1/3$. From either starting
   state the probability of a one obeys $p'=(1-p)/2$, giving the two
   displayed formulas. The minima for transitions into one are $1/4$
   at distances two (from zero) and three (from one) over the permitted
   ranges. A one-to-zero transition at distance one has probability one.
   Constraints on a common gap must be deduplicated; the witnessing tiling
   ensures consistency. Thus the product bound and rounded sample size
   hold. In the expectation sentence the counted sets must be **avoidable**
   sets, as specified earlier in the proof.
6. **Proposition 6, end windows — no gap found in the reduction.** A left
   rung with index 0 through 3 sees only gaps -1 through 3, with -1 absent.
   The right rungs see only gaps $k-5$ through $k-1$, with the last
   absent. All rails are read directly from their gap. At $k=10$ the
   nearest selected gap indices can be 3 and 5; gap 4 can always be set
   to zero. All larger separations work as well. Thus all 64 products
   extend, and fresh singleton colors outside preserve exactly the rainbow
   traces. Lower bounds at 8 and 9 and the upper-bound certificates are
   separate finite obligations.
7. **Theorem 7, saturation — no gap found.** Each selected gap supplies a
   disjoint rung pair, all other gaps supply disjoint rail pairs. Any other
   tiling uses a forbidden rail pair or omits a selected gap and takes its
   two rungs. This forces every individual test at deficit $k-1$.
   Conversely, when all rungs are rainbow and at most $k-2$ edges are
   discarded, one of the $k-1$ rail pairs survives intact, yielding a
   second rainbow witness. Both endpoints are included correctly.

The current manuscript extends Proposition 6 through 17 columns. The trace argument above does not on its own certify the minimum hitting set or the upper witnesses through 17.
