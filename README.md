# Discrete Math Lab

Proofs and reproducible experiments in graph theory, extremal combinatorics,
and algorithms. The main project studies edge colorings that avoid rainbow
perfect matchings.

## Featured work

**Nine symmetry classes of extremal cube colorings**

[Read the report](results/cube_classification.md) · [Typeset PDF](papers/cube_classification.pdf) · [Diagram atlas](results/figures/cube_classes.svg) · [Complete data](results/data/cube_classification.json)

All 174 extremal seven-color cube partitions split into nine classes under
the 48 graph automorphisms and color renaming. The report gives every
representative, explains structural differences, and records exhaustive
coverage and separate verification algorithms.

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

**Expansion and random walks: exact examples**

[Read the paper](papers/expansion_walks.pdf) · [LaTeX source](papers/expansion_walks.tex)

Self-contained proofs explain edge expansion, exact mixing on complete bipartite
graphs, and the difference between periodicity and disconnection. Closed-form
oracles check the rational walk implementation on bounded graph families.

[Research guide](projects/research-guide.md) explains the connections between
projects, their evidence, and concrete next development tasks.

| Topic | Notes | Results |
|---|---|---|
| Hall's theorem and regular bipartite graphs | [Proof](notes/halls_theorem.md) | [4,477 small regular graphs](results/regular_bipartite_small_cases.md) |
| Rainbow arithmetic progressions | [Definitions and groups](notes/rainbow_progressions.md) | [Exact small thresholds](results/rainbow_progressions.md) |
| Vertex color-coding | [Subset dynamic programming](notes/color_coding.md) | [Algorithm checks](results/algorithm_demos.md) |
| Expansion and random walks | [Project report](projects/expansion-and-walks/report.md) | [Exact rational computations](results/algorithm_demos.md) |

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
python -m experiments.classify_cube --check results/data/cube_classification.json
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
