# What does the open-pair count remember?

In [Bohman's triangle-free process](https://www.math.cmu.edu/~tbohman/papers/r3t.pdf), choose uniformly from the absent edges that would not complete a triangle. Write Q for the number of choices. On six vertices, even the pair (number of edges, Q) does not determine the expected change in Q at the next step.

| Four-edge graph | Open pairs | Distribution of the loss of open pairs on the next move | Expected change |
|---|---:|---|---:|
| Three-leaf star plus a separate edge | 8 | 2 choices lose 5; 6 lose 3 | -7/2 |
| Five-vertex path plus an isolated vertex | 8 | 4 choices lose 2; 4 lose 3 | -5/2 |

Both graphs are reachable: every prefix of any ordering of their edges is triangle-free. For the star, every open pair joins the two components. Joining the center to either end of the separate edge costs the selected pair, the three pairs from its leaves to that end, and the pair from the center to the opposite end. Joining a leaf instead costs three pairs. For the path, number its vertices 1 through 5 and call the isolate 6. The eight choices are 14, 15, 25 and the five pairs incident to 6. Pairs 14, 25, 16, 56 each cost two; the other four each cost three. This shows why simply tracking the number of choices loses information. It is a finite worked example, not an asymptotic result or a claim of novelty.

Run `python examples.py` from this directory to reproduce the first such witness by number of edges. The search is over labeled reachable states, not graph isomorphism classes. Run `python six.py` for the exact two-edge drift (-191/91), transition checks against a separate common-neighbor test on all 5,789 states, and a seeded simulation.

## How many past counts help predict the next one?

On six vertices, starting from the empty graph, even the last **three** open-pair counts can give different forecasts at the same time. After six moves, consider the following complete observation histories.

| Open-pair counts from time zero | Ordered seven-move paths ending with zero choices | Paths ending with one choice | Chance the next move ends the process |
|---|---:|---:|---:|
| 15, 14, 12, 9, 8, 5, 2 | 8640 | 4320 | 2/3 |
| 15, 14, 12, 10, 8, 5, 2 | 57600 | 11520 | 5/6 |

For a fixed history through time six, each compatible seven-move path has the same probability, the reciprocal of the product of those seven observed counts. Dividing within each row therefore gives the conditional probability. This tests the observed process with one prescribed starting graph. Comparing individual graph states alone would leave open whether the histories mix those states in the same proportions.

In fact four is the minimum sufficient history length for time-dependent one-step prediction on six vertices (use the entire available history at earlier times). The lower bound follows from the table. For the upper bound, [open_pair_memory.py](open_pair_memory.py) enumerates every positive-probability history and groups the exact conditional distributions by time and suffix. The longest suffix giving unequal forecasts has length three. At a terminal count of zero the process can be held at zero deterministically. Nine moves exhaust the possible range by the six-vertex triangle-free edge bound. These finite findings make no assertion for other graph orders.

On seven vertices the minimum increases to **six**. For example, compare the two histories

    21, 20, 18, 15, 14, 11, 9, 5, 4
    21, 20, 18, 16, 14, 11, 9, 5, 4.

They agree on the last five counts, yet the conditional probabilities of seeing three choices next are 5/7 and 5/6 respectively. Exhaustive enumeration finds no pair with six common final counts at the same time and different forecasts.

Run [open_pair_orbits.py](open_pair_orbits.py) to reproduce the search. Each state stores a graph up to vertex relabeling and its entire observed history. For each successor graph type the recurrence multiplies by the number of actual open edges leading to that type. This retains the multiplicity of labeled paths because graph isomorphisms biject the available moves. The script checks every six-vertex history distribution against the labeled computation before running the seven-vertex case.

On eight vertices the minimum sufficient history length is **ten**. After twelve moves consider the histories

    28, 27, 26, 25, 22, 21, 18, 15, 12, 9, 6, 5, 4
    28, 27, 26, 24, 22, 21, 18, 15, 12, 9, 6, 5, 4.

They agree on the last nine counts. The probabilities that the next move ends the process are respectively 11/2864 and 11/4764. The [labeled history checker](check_forecast_history.py) counts compatible move orders directly and independently verifies both fractions. For the upper bound, run `python open_pair_orbits.py --order 8` from this directory. It compares all reachable histories at each time through termination. Its graph labels are canonical: vertices are grouped by degree and the sorted degrees of their neighbors, and the least adjacency encoding among orders respecting those groups is used. Permutations within a group whose vertices have identical neighbor sets leave the encoding unchanged. The longest ambiguous suffixes at times 4 through 12 have lengths 1 through 9 respectively; no later time has ambiguous forecasts even with just the current count.

A [counting argument using the vertices touched by each path](forecast-transfer.md) shows that the eight-vertex discrepancy persists at every order n>=8. Exact path polynomials exclude all exceptional orders, so at least ten observations are necessary throughout this range.

### A general upper bound on the number of past counts

For n at least six, let D=floor((n-1)^2/4). Knowing the move number, the last **D-2** open-pair counts suffice to determine the conditional distribution of the next count. For six and eight vertices this proves the computed upper bounds of four and ten without enumerating histories.

At time three the open-pair count determines the entire graph up to relabeling. The three edges form either a matching, a two-edge path and a disjoint edge, a three-edge path, or a three-leaf star, together with isolated vertices. These have respectively zero, one, two and three closed nonedges. Given the time-three count, all compatible labeled states thus have the same future count law by symmetry. Conditioning further on any subsequent count history preserves this equality. At times from three through D inclusive it therefore suffices to remember the counts starting at time three, at most D-2 observations. At earlier times the whole history fits within the bound.

At any time m>D the next count is max(Q-1,0). To prove this, first consider a nonbipartite state. The classical nonbipartite triangle-free edge bound gives m<=D+1. Any legal addition would leave the graph nonbipartite and violate the bound, so Q=0. The edge bound and its attribution to Erdős–Gallai and independently Andrásfai are recalled in [Ren, Wang, Wang and Yang](https://arxiv.org/abs/2404.07486).

For a bipartite state fix parts of sizes a,b. If two vertices in the first part formed an open pair, they would have disjoint neighborhoods, so their combined degree would be at most b. The entire graph would then have at most (a-1)b<=D edges. Interchanging the parts gives the same contradiction. Thus the open pairs are exactly the missing cross edges, and a legal addition reduces their count by one. This proves the asserted late-time rule, including the terminal case.

### The last step with a random next count

The cutoff above is exact for every n at least six, even when the whole current graph is known. At m=D, every state with two possible next counts has one of the following forms. Write x+y=n-1 with |x-y|<=1, so xy=D.

- **Split a vertex of K(x,y).** Replace one vertex on the x-side by two vertices with disjoint, nonempty neighborhoods partitioning its y former neighbors. The open pairs are the pair of split vertices and the y missing cross edges. Joining the split vertices leaves zero choices: every missing cross edge now has a two-edge blocking path through the other split vertex. Any missing cross edge instead gives the split vertices a common neighbor and leaves y-1 cross edges open. Thus the next counts 0 and y-1 have probabilities 1/(y+1) and y/(y+1). Every such state is reachable by adding its edges in any order.
- **An isolated vertex alongside K(x,y).** Here all x+y pairs incident to the isolate are open. Joining it to a vertex on the x-side leaves x-1 choices; joining it to the y-side leaves y-1. Their probabilities are x/(x+y) and y/(x+y). These counts differ exactly when n is even.

For completeness, a nonbipartite graph at D edges is already terminal or every legal move reaches the nonbipartite edge bound D+1 and terminates. A bipartite graph with no open internal pair loses exactly one choice at its next move, if any. In the remaining case the argument above forces equality in m<=(a-1)b<=D for an open internal pair. Equality makes every other vertex in its part adjacent to the entire opposite part; the two exceptional neighborhoods partition that part. They are both nonempty in the first construction, and an empty neighborhood gives the second. This exhausts the possibilities. [Direct next-step checks](check_last_random_step.py) cover both choices of part and every split size for orders 6 through 24. Sharpness here concerns the time of the last genuinely random transition from a specified graph; the minimum observable history length is a separate question.

The same process also gives exact probabilities for reaching a specified terminal graph. The [terminal graph calculation](terminal-bicliques.md) derives a closed formula for stars and checks small complete bipartite graphs by two counting methods.

## Three short counting exercises

- **Oriented Ramsey example.** Exactly two of the eight labeled tournaments on three vertices avoid an outward-directed two-leaf star: the directed cycles. On four vertices every tournament contains the star, since its six edges give average outdegree 3/2. This is an elementary starting point for the bounded-degree question on [Xiaoyu He's problem list](https://alkjash.github.io/problems/), not progress on that open problem.
- **Random coloring.** Under independent fair binary vertex colors on a triangle, each edge is monochromatic with probability 1/2. Two specified edges are both monochromatic with probability 1/4, but all three are monochromatic with probability 1/4 rather than 1/8. Thus the indicators are pairwise independent but not jointly independent. Enumerating the eight vertex colorings gives six with one monochromatic edge and two with three. A next exercise is to identify which edge subsets in a larger graph yield independent indicators.
- **Factorization lengths.** Count unordered representations of 60 using 6, 9 and 20. In 6a+9b+20c=60, reducing modulo 3 forces c=0 or 3. The latter gives length 3. The former gives 2a+3b=20, hence b=0,2,4,6 and lengths 10,9,8,7. Each length occurs once. An accessible next question is when gaps between consecutive lengths first exceed one for other targets.

The last three counts are independently enumerated by `examples.py`. All scripts use only the Python standard library.

[General formulas and their finite checks](extensions.md) extend all four examples.

[Finite-horizon laws for straight and twisted ladders](horizon.md) compares whole sequences of open-pair counts with the support of the terminal edge count.

[Five further derivations](five-directions.md) and [the representative-family comparison](representative-families.md). Run python check_five.py for finite checks.

## Further calculations

- [Escape heights for tournament star counts](escape-heights.md) determines the first order where neutral reversals cannot reach a cheaper tournament, and proves the exact barrier for an infinite family.
- [Optimal color inventories on an even cycle (two-page PDF)](cycle-inventories.pdf) classifies the best fixed multiplicities for every cycle length and palette size. [LaTeX source](cycle-inventories.tex).
- [Independence of rainbow matching events](rainbow-independence.md) characterizes when the full set of indicators is independent under uniform and biased edge colors.

[Minimizing a mixed star in a tournament](tournament-scores.pdf) gives the exact minimum for every order and a proof for general cubic objectives. [LaTeX source](tournament-scores.tex) · [score-sequence checks](cubic_scores.py).

- [Straight versus twisted ladders: an explicit distinguishing event](maximal-loss.md); [exact joint-law enumerator](path_counts.py).
- [Cycle losses, mixed-star centers and stability, and cactus coloring laws](further-results.md); [direct checks](check_further.py).
- [Recovering parallel path lengths](theta-inverse.md); [inverse tests](theta_inverse.py).
- [Independent correspondence-conflict events](correspondence.md) and [random assignments on theta graphs](random-correspondence.md); [five-vertex checks](correspondence_checks.py).
- [Sharp bounds on runs of missing factorization lengths](residue-gaps.md); [direct dynamic-programming checks](residue_gaps.py).


- [First detectable moment of a binary path twist](binary-path-law.md) and [single-reversal traps for mixed stars](star-descent.md).
- [Recovering a strip seam from closed walks](strip-spectrum.md).
- [An intersection criterion for one repeated color](one-repeat.md) and [recovery of mixed cycle lengths](mixed-cycle-recovery.md).


[Identifying signed paths with a single probe (two-page PDF)](single-probe.pdf) starts with the six-edge example and proves the sharp probe length. [LaTeX source](single-probe.tex) and [reproducible check](check_single_probe.py).
