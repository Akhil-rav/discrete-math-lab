# Projects

## Rainbow perfect matchings

The main project studies how many colors a fixed bipartite graph can use while
avoiding every rainbow perfect matching.

- [Project report: exact searches on small hosts](rainbow-matchings/report.md)
- [Paper: even cycles and two disjoint squares](../papers/cycle_extremizers.pdf)
- [LaTeX source](../papers/cycle_extremizers.tex)
- [Extremal K33 classification](../results/k33_classification.md)
- [Sparse-host data](../results/data/sparse_rainbow.json)
- [Search implementation](../src/rainbow_constraints.py)

The cycle and disjoint-square statements have elementary proofs. The cube
result is an exhaustive finite computation. Detailed conventions, checks,
and limits appear in the report.

## Expansion and random walks

[Project report](expansion-and-walks/report.md) studies exact edge expansion,
bipartite periodicity, and the effect of laziness on four small regular graphs.
All walk probabilities are rational. This is an educational reproduction, not
an expander construction.

[Research guide](research-guide.md) maps completed work, literature connections,
and bounded development tasks. Related experiments in additive combinatorics
and color-coding are indexed in [the notes](../notes/README.md) and
[results](../results/README.md).
