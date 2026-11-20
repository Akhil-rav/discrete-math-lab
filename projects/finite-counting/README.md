# What does the open-pair count remember?

In [Bohman's triangle-free process](https://www.math.cmu.edu/~tbohman/papers/r3t.pdf), choose uniformly from the absent edges that would not complete a triangle. Write Q for the number of choices. On six vertices, even the pair (number of edges, Q) does not determine the expected change in Q at the next step.

| Four-edge graph | Open pairs | Distribution of the loss of open pairs on the next move | Expected change |
|---|---:|---|---:|
| Three-leaf star plus a separate edge | 8 | 2 choices lose 5; 6 lose 3 | -7/2 |
| Five-vertex path plus an isolated vertex | 8 | 4 choices lose 2; 4 lose 3 | -5/2 |

Both graphs are reachable: every prefix of any ordering of their edges is triangle-free. For the star, every open pair joins the two components. Joining the center to either end of the separate edge costs the selected pair, the three pairs from its leaves to that end, and the pair from the center to the opposite end. Joining a leaf instead costs three pairs. For the path, number its vertices 1 through 5 and call the isolate 6. The eight choices are 14, 15, 25 and the five pairs incident to 6. Pairs 14, 25, 16, 56 each cost two; the other four each cost three. This shows why simply tracking the number of choices loses information. It is a finite worked example, not an asymptotic result or a claim of novelty.

Run `python examples.py` from this directory to reproduce the first such witness by number of edges. The search is over labeled reachable states, not graph isomorphism classes. Run `python six.py` for the exact two-edge drift (-191/91), transition checks against a separate common-neighbor test on all 5,789 states, and a seeded simulation.

## Three short counting exercises

- **Oriented Ramsey example.** Exactly two of the eight labeled tournaments on three vertices avoid an outward-directed two-leaf star: the directed cycles. On four vertices every tournament contains the star, since its six edges give average outdegree 3/2. This is an elementary starting point for the bounded-degree question on [Xiaoyu He's problem list](https://alkjash.github.io/problems/), not progress on that open problem.
- **Random coloring.** Under independent fair binary vertex colors on a triangle, each edge is monochromatic with probability 1/2. Two specified edges are both monochromatic with probability 1/4, but all three are monochromatic with probability 1/4 rather than 1/8. Thus the indicators are pairwise independent but not jointly independent. Enumerating the eight vertex colorings gives six with one monochromatic edge and two with three. A next exercise is to identify which edge subsets in a larger graph yield independent indicators.
- **Factorization lengths.** Count unordered representations of 60 using 6, 9 and 20. In 6a+9b+20c=60, reducing modulo 3 forces c=0 or 3. The latter gives length 3. The former gives 2a+3b=20, hence b=0,2,4,6 and lengths 10,9,8,7. Each length occurs once. An accessible next question is when gaps between consecutive lengths first exceed one for other targets.

The last three counts are independently enumerated by `examples.py`. All scripts use only the Python standard library.

[General formulas and their finite checks](extensions.md) extend all four examples.

[Finite-horizon laws for straight and twisted ladders](horizon.md) compares whole sequences of open-pair counts with the support of the terminal edge count.

[Five further derivations](five-directions.md) and [the representative-family comparison](representative-families.md). Run python check_five.py for finite checks.
