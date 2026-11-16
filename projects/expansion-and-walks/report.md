# Expansion, periodicity, and random walks

This study uses exact finite computations to illustrate expansion and
random walks.
This report organizes the existing experiment; it introduces no new computed
results or expander construction.

## Question

The accompanying [expository paper](../../papers/expansion_walks.pdf)
([LaTeX](../../papers/expansion_walks.tex)) proves formulas for graph families
that explain these examples. Its proofs do not rely on computation; the
[formula tests](../../tests/test_walk_formulas.py) compare them with the walk
routine over explicitly bounded parameter ranges.

How do sparse cuts, bipartiteness, and disconnection affect a random walk?
The experiment separates these issues using four small regular graphs rather
than treating a single mixing statistic as a complete description of a graph.

## Method

The implementation enumerates every nonempty vertex subset of size at most
half the graph order and minimizes boundary-edge count divided by subset size.
It returns both the exact rational minimum and a witnessing subset.

Starting at vertex 0, it then evolves ordinary and lazy random walks through
time 8. An ordinary step chooses a neighbor uniformly. A lazy step stays with
probability one half and otherwise takes an ordinary step. Total variation is
measured against the uniform distribution on all vertices. Uniform is stationary
on these regular graphs, including the disconnected example; stationarity alone
does not imply convergence from a point mass.

Every probability and distance uses Python's rational arithmetic. There is no
sampling, floating-point approximation, or fitted convergence rate.

## Existing results

| Host | Edge expansion | Lazy TV at time 8 | Ordinary TV at time 8 |
|---|---:|---:|---:|
| Complete graph K4 | 2 | 1/8748 | 1/8748 |
| Cycle C6 | 2/3 | 2187/32768 | 1/2 |
| Complete bipartite graph K3,3 | 5/3 | 1/384 | 1/2 |
| Two disjoint triangles | 0 | 1/2 | 1/2 |

These values reproduce the [recorded table](../../results/algorithm_demos.md).
The full time sequences and minimizing sets are emitted by the experiment.

In C6 and K3,3, the ordinary walk alternates bipartition sides. At each time it
assigns zero mass to one side, which has uniform mass one half. Laziness removes
this parity obstruction. In two disjoint triangles the walk cannot leave its
starting component; adding holding probability does not repair disconnection.
The equal time-8 distances for K4 do not assert equal walk distributions.

## Reproduce and inspect

From the repository root, with Python 3.11 or later:

```sh
python -m experiments.expansion_small_cases
python -m experiments.reproduce --check results/data/small_cases.json
python -m unittest discover -s tests -v
```

- [Algorithm](../../src/expansion.py): graph validation, cut enumeration, walks.
- [Experiment](../../experiments/expansion_small_cases.py): explicit graph inputs.
- [Tests](../../tests/test_algorithms.py): complete-graph and cycle expansion
  benchmarks, a bipartite parity example, and lazy-walk checks.
- [Conventions and sources](../../notes/expansion_and_walks.md).
- [Historical execution records](../../results/verification.md).

## Scope

Four small graphs do not constitute an infinite expander family. Expansion here
is not degree-normalized; comparisons between different degrees require care.
No spectral gap, Cheeger inequality, high-dimensional expansion, or coding
application is implemented or certified.

## Reference

The edge-expansion convention follows Hoory, Linial, and Wigderson,
[*Expander graphs and their applications*](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/HLW06/hlw06.pdf),
Definitions 2.1 and 2.2. The [source notes](../../notes/expansion_and_walks.md)
give the convention and distinguish these finite examples from an expander family.
