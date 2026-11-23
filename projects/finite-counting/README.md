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

## Three short counting exercises

- **Oriented Ramsey example.** Exactly two of the eight labeled tournaments on three vertices avoid an outward-directed two-leaf star: the directed cycles. On four vertices every tournament contains the star, since its six edges give average outdegree 3/2. This is an elementary starting point for the bounded-degree question on [Xiaoyu He's problem list](https://alkjash.github.io/problems/), not progress on that open problem.
- **Random coloring.** Under independent fair binary vertex colors on a triangle, each edge is monochromatic with probability 1/2. Two specified edges are both monochromatic with probability 1/4, but all three are monochromatic with probability 1/4 rather than 1/8. Thus the indicators are pairwise independent but not jointly independent. Enumerating the eight vertex colorings gives six with one monochromatic edge and two with three. A next exercise is to identify which edge subsets in a larger graph yield independent indicators.
- **Factorization lengths.** Count unordered representations of 60 using 6, 9 and 20. In 6a+9b+20c=60, reducing modulo 3 forces c=0 or 3. The latter gives length 3. The former gives 2a+3b=20, hence b=0,2,4,6 and lengths 10,9,8,7. Each length occurs once. An accessible next question is when gaps between consecutive lengths first exceed one for other targets.

The last three counts are independently enumerated by `examples.py`. All scripts use only the Python standard library.

[General formulas and their finite checks](extensions.md) extend all four examples.

[Finite-horizon laws for straight and twisted ladders](horizon.md) compares whole sequences of open-pair counts with the support of the terminal edge count.

[Five further derivations](five-directions.md) and [the representative-family comparison](representative-families.md). Run python check_five.py for finite checks.

## Further calculations

[Minimizing a mixed star in a tournament](tournament-scores.pdf) gives the exact minimum for every order and a proof for general cubic objectives. [LaTeX source](tournament-scores.tex) · [score-sequence checks](cubic_scores.py).

- [Straight versus twisted ladders: an explicit distinguishing event](maximal-loss.md); [exact joint-law enumerator](path_counts.py).
- [Cycle losses, mixed-star centers and stability, and cactus coloring laws](further-results.md); [direct checks](check_further.py).
- [Recovering parallel path lengths](theta-inverse.md); [inverse tests](theta_inverse.py).
- [Independent correspondence-conflict events](correspondence.md) and [random assignments on theta graphs](random-correspondence.md); [five-vertex checks](correspondence_checks.py).
- [Sharp bounds on runs of missing factorization lengths](residue-gaps.md); [direct dynamic-programming checks](residue_gaps.py).


- [First detectable moment of a binary path twist](binary-path-law.md) and [single-reversal traps for mixed stars](star-descent.md).
- [Recovering a strip seam from closed walks](strip-spectrum.md) and [factorization gaps on residue classes](residue-gaps.md).
- [An intersection criterion for one repeated color](one-repeat.md) and [recovery of mixed cycle lengths](mixed-cycle-recovery.md).


[Identifying signed paths with a single probe (two-page PDF)](single-probe.pdf) starts with the six-edge example and proves the sharp probe length. [LaTeX source](single-probe.tex) and [reproducible check](check_single_probe.py).
