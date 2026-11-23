# Escape heights for tournament star counts

Use the score function and single-arc reversal formula in [the plateau construction](star-plateaus.md). Define the escape height of a nonoptimal tournament to be the smallest possible peak increase above its initial star count on a path to any strictly cheaper tournament.

## The first obstruction

Ten is the smallest order with positive escape height. The ten-vertex example is proved in the preceding note. The exclusion through order nine is computational. The unlabeled search in `small_reversal_plateaus.py` found the following counts.

| Order | Tournament isomorphism types | Minimum star count | Nonoptimal types with no immediate decrease | Closed nonoptimal neutral components |
|---:|---:|---:|---:|---:|
| 6 | 56 | 12 | 2 | 0 |
| 7 | 456 | 30 | 1 | 0 |
| 8 | 6880 | 60 | 1 | 0 |
| 9 | 191536 | 111 | 12 | 0 |

At orders two through five there were no nonoptimal types without an immediate decrease. At order one the sole tournament has cost zero.

An independent search, `python projects/finite-counting/check_sorted_plateaus.py`, fixes a sorted outdegree list and tries every orientation that realizes it and has no decreasing reversal. The prefix of length m must have degree sum at least m(m-1)/2 by counting internal arcs. Minimizing over this necessary condition gives a lower bound which the program checks is attained by an actual tournament. A breadth-first search through equal-cost reversals then measures how many neutral steps are needed before a decreasing arc appears. With the vertex labels fixed in sorted-score order, all 26, 2 and 2 nonoptimal stuck orientations at orders six, seven and eight respectively require one neutral step. At order nine, 2762 require one and 68 require two. These multiplicities count orientations with sorted scores, so vertices of equal score can still exchange labels.

## Exact height for the original family

For the transitive/regular example of order 6t+4, t at least one, the height is exactly one. Every exit costs at least one by the plateau proof and integrality. Pick an upper vertex and reverse three of its original outgoing upper arcs, one at a time. It has 2t+1 such arcs. Before step j+1 its degree is v-j, and the fresh head still has degree v. Substitution in the reversal formula gives changes +1, -1, -6. The final cost lies six below the initial cost.

## Unbounded height

For each integer t at least two, take a transitive lower part of size 4t and a regular upper part of size 6t+1, with all cross arcs directed down. Here N=10t and the common upper score is v=7t. This tournament has escape height at least t+1.

Indeed, an upper arc reversal costs t+1. A lower reversal between consecutive ranks interchanges them at zero cost. For every other lower reversal the first factor a-b-1 is at least one and the second factor 4N-2-3(a+b) is at least 16t+7. For a cross arc these factors are respectively at least 3t and 7t+1. After any sequence of zero-cost reversals the same bounds apply, since only the lower order has been permuted. Thus the first move of positive cost already reaches height at least t+1.

To see explicitly that escape is possible, reverse h outgoing upper arcs of a single vertex toward distinct original heads. At step j+1 the change is (j+1)(2t+2-3j)/2. Summing from j=0 to h-1 gives h(h+1)(t+2-h)/2 above the initial cost. Taking h=t+3 makes this negative, and there are 3t outgoing upper arcs available. The largest value of this expression over 0 through t+3 gives a constructive upper bound. The argument below proves sharpness even for unrestricted paths.

## Exact height when only upper arcs can change

Under this restriction the preceding upper bound is sharp. Write x_i for the change in upper vertex i's outdegree from 7t. Since the total upper outdegree stays fixed, the x_i sum to zero. Expanding the cubic score and cancelling its linear part shows that the increase in cost equals

    sum_i x_i^2 (t+1+x_i)/2.

To reach a cheaper tournament some x_i must drop below -(t+1). For each integer h from 1 through t+1, consider the first time the minimum deviation reaches -h. Such a time exists because one reversal changes each affected score by one. A vertex of deviation -h contributes h^2(t+1-h)/2. Every other negative deviation contributes a nonnegative amount. Each positive integer deviation x contributes at least x(t+2)/2, and the positive deviations sum to at least h. Hence the cost increase at that moment is at least

    [h^2(t+1-h) + h(t+2)]/2 = h(h+1)(t+2-h)/2.

The single-vertex construction attains this bound for every h along one path. The only other steps on that path, h=0, t+2 and t+3, have nonpositive increase. Thus the restricted escape height is precisely the maximum of the displayed expression over 1 through t+1. For example, at t=2 the restricted height is 6, and the next argument shows that the unrestricted height is also 6.

## The same height for unrestricted moves

Fix the original upper and lower vertex sets throughout the walk. Let q count the cross arcs pointing up, and write x_i for the upper degree deviations as before. Their sum is now -q. Put f(y)=y(10t-y)(10t-1-y)/2 and g(x)=x^2(t+1+x)/2. By exact cubic expansion, the upper contribution relative to the starting cost is

    -q f'(7t) + sum_i g(x_i).

For q at most t, the change in the lower contribution is at least q f'(5t). To see this, first use only the internal lower degrees y_i. The transitive degree vector majorizes every such vector: the largest m scores sum to at most m(m-1)/2 + m(4t-m), with equality for the transitive vector. Since f is concave on [0,5t] (its second derivative is 3y+1-20t), the sum of f on the internal degrees is minimized by the transitive vector. Now restore the external wins. They increase the lower degrees by q in total and no resulting degree exceeds 4t-1+q. Each unit of increase contributes at least f'(5t) by concavity. Consequently the full increase D obeys

    D >= q c + sum_i g(x_i),     c = f'(5t)-f'(7t) = 4t^2-2t.

Let h maximize H(h)=h(h+1)(t+2-h)/2 over the integers 1 through t+1. Follow a path toward a strictly cheaper state and stop when either q reaches t or the minimum upper deviation reaches -h. One event must occur: before both events all g terms are nonnegative and the displayed bound precludes any decrease below the initial cost. Both coordinates change by at most one per reversal.

If q=t occurs first (including a tie), every g is still nonnegative, so D is at least tc. This exceeds H(h): for t at least two, h and t+2-h are at most 3t/2, h+1 is at most 2t, and tc is at least 3t^3.

Otherwise a vertex has deviation -h, every other negative deviation contributes nonnegatively, and the positive deviations sum to at least h-q. As in the restricted proof this yields

    D >= q c + g(-h) + (h-q)(t+2)/2
      = H(h) + q [c-(t+2)/2] >= H(h).

Hence every unrestricted escape has height at least H(h). The explicit upper-arc path gives equality for every t at least two. In particular the heights in this family grow cubically in t.

These are statements about the specified star count and single-arc moves. Their priority in the literature is undetermined.
