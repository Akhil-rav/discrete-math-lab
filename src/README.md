# Implementation guide

These are small, inspectable implementations for the repository's finite
experiments. They use Python 3.11+ and the standard library. Run examples from
the repository root; no package installation is needed. The code is intended
for the input ranges stated in each module.

## Source map

| Modules | Purpose | Mathematical context and checks |
|---|---|---|
| [bipartite_graph.py](bipartite_graph.py), [matchings.py](matchings.py) | Bipartite graph representation and augmenting-path maximum matching | [Hall's theorem](../notes/halls_theorem.md); [algorithm tests](../tests/test_algorithms.py) |
| [edge_coloring.py](edge_coloring.py), [color_patterns.py](color_patterns.py) | Color equality, normalization, and complete-bipartite symmetry | [Rainbow conventions](../notes/rainbow_matchings.md); [K33 classification](../results/k33_classification.md) |
| [rainbow_constraints.py](rainbow_constraints.py) | Perfect-matching constraints and pruned edge-partition enumeration, through 12 edges | [Coverage argument](../projects/rainbow-matchings/report.md); [independent small-host checks](../tests/test_sparse_rainbow.py) |
| [cube_symmetry.py](cube_symmetry.py) | Fixed cube edge order, exact-block partition iterator, and the 48 automorphisms | [Nine-class classification](../results/cube_classification.md); [symmetry tests](../tests/test_cube_classification.py) |
| [cycle_unions.py](cycle_unions.py) | Fixed even-cycle unions and construction of every proved extremizer | [General proof](../notes/cycle_extremizers.md); [ten-host verification](../results/cycle_union_verification.md) |
| [ladders.py](ladders.py) | Labeled ladders, column-recursive matchings, and full symmetry actions for 2–5 columns | [Bounds and classification](../results/ladder_matchings.md); [vertex-bijection and named-color tests](../tests/test_ladders.py) |
| [l5_extremizers.py](l5_extremizers.py) | Construct the fifteen L5 partitions from the proved block families | [Counting proof](../notes/l5_extremizers.md); [comparison with the exhaustive population](../tests/test_l5_extremizers.py) |
| [matching_covers.py](matching_covers.py), [matching_cover_certificate.py](matching_cover_certificate.py) | Weighted-cover minimum deficit and separate certificate checking | [Reduction and ladder theorem](../notes/matching_covers.md); [finite oracles](../tests/test_matching_covers.py) |
| [rainbow_probability.py](rainbow_probability.py) | Exact partition-weight probabilities, matching moments, and bounds | [Counting proofs](../notes/random_rainbow.md); [named-color oracles](../tests/test_rainbow_probability.py) |
| [rainbow_inclusion_exclusion.py](rainbow_inclusion_exclusion.py) | Matching-event inclusion-exclusion using conflict-graph coloring polynomials | [Method comparison](../results/inclusion_exclusion.md); [proper-coloring and event-family oracles](../tests/test_inclusion_exclusion.py) |
| [arithmetic_progressions.py](arithmetic_progressions.py) | Distinct-term three-term progressions in intervals and products of cyclic groups | [Definitions](../notes/rainbow_progressions.md); [algorithm tests](../tests/test_algorithms.py) |
| [color_coding.py](color_coding.py) | Subset dynamic programming for vertex-colorful paths | [Method and complexity](../notes/color_coding.md); [finite comparisons](../results/algorithm_demos.md) |
| [expansion.py](expansion.py) | Exact edge expansion and rational regular-graph walks | [Walk paper](../papers/expansion_walks.pdf); [closed-form oracles](../tests/test_walk_formulas.py) |

The [experiment guide](../experiments/README.md) lists runnable commands, tested
ranges, and independent checks. Experiments assemble these modules and write
results; the source modules keep the underlying operations separate.

## Two small examples

For a four-cycle, the only extremal avoiding partition up to color renaming
assigns one color to each pair of opposite edges. It uses two colors:

```python
from src.rainbow_constraints import avoiding_partitions

square = ((0, 0), (0, 1), (1, 0), (1, 1))
result = avoiding_partitions(2, square)
assert result['maximum_avoiding_colors'] == 2
assert result['extremal_partitions'] == 1
```

For independent uniform edge colors from four available colors, that same
host has rainbow-perfect-matching probability 15/16. Each of its two disjoint
perfect matchings is monochromatic with probability 1/4, so the probability
that both fail to be rainbow is 1/16:

```python
from fractions import Fraction
from src.rainbow_probability import rainbow_probability

# Avoidance has one one-block partition and one two-block partition.
probability = rainbow_probability(4, {1: 1, 2: 1}, 4)
assert probability == Fraction(15, 16)
```

Available labeled colors in the probability model and color classes in a
partition search are different quantities. The search fixes edge positions
and ignores color names; graph automorphisms are applied only in the separate
classification step. Color-coding instead colors vertices.

To check all current implementations and reference data:

```sh
python -m tools.verify_repository
```
