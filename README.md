# Discrete Math Lab

[![Mathematical checks](https://github.com/Akhil-rav/discrete-math-lab/actions/workflows/checks.yml/badge.svg?branch=main)](https://github.com/Akhil-rav/discrete-math-lab/actions/workflows/checks.yml)

Proofs and reproducible experiments in extremal combinatorics, graph theory,
and algorithms. The main thread studies rainbow perfect matchings, from
small-case searches to structural proofs and exact probabilities.

## Selected work

| Study | Main outcome | Read |
|---|---|---|
| **Extremal cube colorings** | A proof of the seven-color maximum; all 174 extremizers classified into nine symmetry classes | [Report](results/cube_classification.md) · [Four-page paper](papers/cube_classification.pdf) · [Labeled atlas](results/figures/cube_classes.svg) |
| **Independent random edge colors** | Two exact counting methods on six hosts, moment and Bonferroni bounds, and a measured runtime comparison | [Five-page paper](papers/random_rainbow.pdf) · [Methods and timings](results/inclusion_exclusion.md) · [Report and plot](projects/random-colorings/report.md) |
| **Ladder matchings and weighted covers** | A color bound for every ladder with at least three columns; cover certificates on nine hosts; a direct count of all 15 five-column extremizers | [Proof and classification](results/matching_covers.md) · [Twelve-page matching report](papers/matching_foundations.pdf) |
| **Expansion and random walks** | Elementary cut formulas and exact examples separating periodicity from disconnection | [Three-page paper](papers/expansion_walks.pdf) · [Project report](projects/expansion-and-walks/report.md) |

The cube study combines an [incidence proof](notes/cube_upper_bound.md), an
exhaustive [symmetry classification](results/cube_classification.md), and a
[capacity-and-overlap analysis](results/cube_collisions.md). Color names and
graph symmetries are distinguished throughout.

![Exact probabilities under independent uniform edge colors](results/figures/random_rainbow.svg)

The plot compares three eight-vertex hosts and the cube's analytic moment
bounds. The underlying probabilities are exact rationals; the curves are a
presentation of the saved data.

## Foundations and supporting studies

| Topic | Artifact |
|---|---|
| Disjoint unions of even cycles | [General maximum and complete extremal classification](papers/cycle_extremizers.pdf) · [Proof and finite checks](results/cycle_union_verification.md) |
| Sparse bipartite hosts | [Six exact searches through twelve edges](projects/rainbow-matchings/report.md) |
| Complete bipartite symmetry | [Four classes among 87 extremal K3,3 partitions](results/k33_classification.md) · [Typeset report](papers/matching_foundations.pdf) |
| Matching theory | [Hall's theorem and 4,477 regular-graph checks](papers/matching_foundations.pdf) |
| Additive combinatorics | [Rainbow arithmetic progressions](papers/rainbow_progressions.pdf) · [Results](results/rainbow_progressions.md) |
| Graph algorithms | [Vertex color-coding](papers/color_coding.pdf) · [Finite algorithm checks](results/algorithm_demos.md) |

[Project guide](projects/README.md) · [Literature and source scope](notes/literature/README.md)
· [Implementation guide](src/README.md) · [References](references.bib)
· [All results](results/README.md)

Each study links its proofs, code, and data. Published results are cited in
the reports and literature notes; computational results include their tested ranges.

## Reproduce

Python **3.11+**; mathematical computations use the standard library. From the
repository root, one command runs the integrity checks, tests, and all nine
reference-data reproductions. To start from a fresh clone:

```sh
git clone https://github.com/Akhil-rav/discrete-math-lab.git
cd discrete-math-lab
python -m tools.verify_repository
```

Automated checks run on Linux with Python 3.11 and 3.13, and on Windows with
Python 3.13. No package installation is required for this sequence.

Use `--static-only` to check links and saved-file integrity without rerunning
the mathematics. See the [experiment commands](experiments/README.md) and
[test records](results/verification_index.md) for details.

Plots need optional [Matplotlib requirements](requirements-figures.txt) only to
regenerate their images. [Typeset notes](papers/README.md) include LaTeX sources
and build instructions for all seven completed mathematical reports. Reading
the committed figures and PDFs needs neither.

These projects grew out of several months of study. I organized the repository
for public release in November 2026 and continue to extend the work here.

Akhil Ravuri
