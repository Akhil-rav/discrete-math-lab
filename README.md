# Discrete Math Lab

Proofs and reproducible experiments in graph theory, extremal combinatorics,
and algorithms. The main project studies edge colorings that avoid rainbow
perfect matchings.

## Featured work

**Rainbow perfect matchings on even cycles and two disjoint squares**

[Read the paper](papers/cycle_extremizers.pdf) · [LaTeX source](papers/cycle_extremizers.tex) · [Web version](notes/cycle_extremizers.md)

Elementary proofs determine the maximum color count and all extremal color
partitions for even cycles and two disjoint squares.

**Exact searches on sparse bipartite graphs**

[Project report](projects/rainbow-matchings/report.md) · [Data](results/data/sparse_rainbow.json) · [Implementation](src/rainbow_constraints.py)

An exact partition search covers six hosts through 12 edges. For the cube,
it accounts for 4,213,597 color partitions and finds a maximum avoiding count
of seven colors, attained by 174 normalized partitions. Vertex labels remain
fixed; the report explains the pruning and coverage argument.

**Extremal colorings of $K_{3,3}$**

[Classification](results/k33_classification.md) · [Experiment](experiments/classify_k33.py)

The 87 extremal four-color partitions form four classes under graph
automorphisms and color renaming, with orbit sizes 6, 36, 36, and 9.

## Related studies

| Topic | Notes | Results |
|---|---|---|
| Hall's theorem and regular bipartite graphs | [Proof](notes/halls_theorem.md) | [4,477 small regular graphs](results/regular_bipartite_small_cases.md) |
| Rainbow arithmetic progressions | [Definitions and groups](notes/rainbow_progressions.md) | [Exact small thresholds](results/rainbow_progressions.md) |
| Vertex color-coding | [Subset dynamic programming](notes/color_coding.md) | [Algorithm checks](results/algorithm_demos.md) |
| Expansion and random walks | [Definitions and examples](notes/expansion_and_walks.md) | [Exact rational computations](results/algorithm_demos.md) |

[Literature guide](notes/literature/README.md) · [References](references.bib) · [All results](results/README.md)

The repository contains elementary exposition, reproductions of published
results, and exhaustive finite computations. Each writeup states its scope;
no novelty is claimed.

## Reproduce

Python **3.11+**, standard library only. Run from the repository root:

```sh
python -m unittest discover -s tests -v
python -m experiments.reproduce --check results/data/small_cases.json
python -m experiments.sparse_rainbow --check results/data/sparse_rainbow.json
```

See [individual experiments](experiments/README.md) for bounds and conventions,
[verification records](results/verification.md) for execution details, and
[paper build instructions](papers/README.md) for LaTeX.

## Contents

`papers/` typeset notes and LaTeX · `projects/` project reports · `notes/`
mathematical background and literature · `src/` algorithms · `experiments/`
bounded computations · `results/` tables, data, and run records · `tests/`
independent checks.

Akhil Ravuri
