# Projects

## Where to start

| Interest | Reading route |
|---|---|
| Proofs | Start with the [even-cycle-union paper](../papers/cycle_extremizers.pdf), then the [cube incidence proof](../notes/cube_upper_bound.md). The first develops from one cycle to a complete union classification; the second develops a bound from matching incidences. |
| Computation | Open the [nine-class cube atlas](../results/cube_classification.md), then follow its [implementation](../src/README.md) and [verification record](../results/cube_verification.md). Distinguish fixed-edge partitions from classes under graph symmetry. |
| Probability and TCS | Read the [random-coloring study](random-colorings/report.md) for exact counting and moment bounds, or the [walk paper](../papers/expansion_walks.pdf) for elementary expansion and mixing examples. |

Each project links its mathematical argument, source code, finite data, and
checks. The [paper collection](../papers/README.md) is a separate entry point
for readers who prefer PDFs.

## Rainbow perfect matchings

The main project studies how many colors a fixed bipartite graph can use while
avoiding every rainbow perfect matching.

- [Project report: exact searches on small hosts](rainbow-matchings/report.md)
- [Paper: arbitrary disjoint unions of even cycles](../papers/cycle_extremizers.pdf)
- [LaTeX source](../papers/cycle_extremizers.tex)
- [Extremal K33 classification](../results/k33_classification.md)
- [Sparse-host data](../results/data/sparse_rainbow.json)
- [Cube classification: nine symmetry classes and labeled atlas](../results/cube_classification.md)
- [Ladder family formula and weighted covers](../results/matching_covers.md)
- [Direct count of the 15 L5 extremizers and six symmetry classes](../notes/l5_extremizers.md)
- [Search implementation](../src/rainbow_constraints.py)

The cycle-union, cube, and ladder maximum-color statements have elementary
proofs. The finite symmetry classifications retain all extremizers and their
orbits. Each report states its conventions and links the computations.

## Random edge colors

[Exact probability study](random-colorings/report.md) derives rainbow-matching
probabilities from exhaustive partition histograms on six hosts. It includes
moment bounds, direct named-color checks, a scientific plot, and the cube's
large-palette limit. Only the plotting step needs an optional dependency.
[Read the typeset report](../papers/random_rainbow.pdf).

For the effect of overlapping matchings on independence, see [uniform and biased edge colors](finite-counting/rainbow-independence.md).
The [inclusion-exclusion implementation](../results/inclusion_exclusion.md)
independently checks every polynomial coefficient, adds Bonferroni bounds,
and compares construction time with the partition search.

## Expansion and random walks

[Project report](expansion-and-walks/report.md) studies exact edge expansion,
bipartite periodicity, and the effect of laziness on four small regular graphs.
All walk probabilities are rational. This is an educational reproduction, not
an expander construction.

Related experiments in additive combinatorics and color-coding are indexed
in [the notes](../notes/README.md) and [results](../results/README.md). All completed mathematical studies have
[PDFs and editable LaTeX sources](../papers/README.md), including matching
foundations, rainbow progressions, and vertex color-coding.
