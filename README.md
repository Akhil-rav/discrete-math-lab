# Discrete Math Lab

[![Mathematical checks](https://github.com/Akhil-rav/discrete-math-lab/actions/workflows/checks.yml/badge.svg?branch=main)](https://github.com/Akhil-rav/discrete-math-lab/actions/workflows/checks.yml)

Proofs and exact experiments in combinatorics, graph theory, and algorithms.
The main project studies rainbow perfect matchings: color bounds, extremal
partitions, and probabilities under random edge colors.

## Selected reports

| Study | Main results | Read |
|---|---|---|
| **Three regimes for testing a ladder** | For color deficit at most two, $d+1$ tests suffice at every length, and the optimal three-test families are counted by Jacobsthal numbers. For each fixed deficit $d\ge3$ the minimum has order $\log k$. From deficit $k-1$ on, every perfect matching must be tested. | [Working note (PDF)](papers/ladder_thresholds.pdf) · [LaTeX](papers/ladder_thresholds.tex) · [Checks](experiments/ladder_thresholds.py) · [Exact search](experiments/ladder_test_exact.cpp) |
| **Testing a ladder for a rainbow matching** | At color deficit three, a fixed list of $\Theta(\log k)$ matchings suffices and this order is necessary. On five columns the unique minimum list has seven members. | [Proofs (PDF)](papers/ladder_tests.pdf) · [LaTeX](papers/ladder_tests.tex) · [Exact check](tests/test_ladder_test_families.py) |
| **Fifteen extremal colorings of the ladder** | Every ladder with at least five columns has the same fifteen terminal patterns, in six symmetry classes. A square contraction reduces the classification to thirteen finite cases. | [Working note (PDF)](papers/ladder_stability.pdf) · [LaTeX](papers/ladder_stability.tex) · [Base cases](results/ladder_stability.md) |
| **Matching bounds and classifications** | $A(P_k\square K_2)=3k-5$ for $k\ge3$; a direct count of the fifteen five-column extremizers; weighted-cover certificates on nine hosts | [PDF](papers/matching_foundations.pdf) · [LaTeX](papers/matching_foundations.tex) · [Results](results/matching_covers.md) |
| **Extremal cube colorings** | A seven-color maximum; all 174 extremizers in nine symmetry classes | [PDF](papers/cube_classification.pdf) · [LaTeX](papers/cube_classification.tex) · [Atlas](results/figures/cube_classes.svg) |
| **Random edge colors** | Two exact counting methods, moment and Bonferroni bounds, and a measured runtime comparison on six hosts | [PDF](papers/random_rainbow.pdf) · [LaTeX](papers/random_rainbow.tex) · [Results](results/inclusion_exclusion.md) |
| **Expansion and random walks** | Elementary cut formulas and exact examples of periodicity, lazy mixing, and disconnection | [PDF](papers/expansion_walks.pdf) · [LaTeX](papers/expansion_walks.tex) · [Results](projects/expansion-and-walks/report.md) |

The matching counts keep edges fixed and ignore color names. Graph symmetries
are applied separately. Each report identifies its proofs, cited results, and
finite computational claims.

![Exact rainbow-matching probabilities on selected hosts](results/figures/random_rainbow.svg)

## Other studies

- [Disjoint unions of even cycles](papers/cycle_extremizers.pdf): the maximum color count and every extremal partition.
- [Rainbow arithmetic progressions](papers/rainbow_progressions.pdf): exact small interval and finite-group calculations.
- [Vertex color-coding](papers/color_coding.pdf): the standard colorful-path method and 22,955 finite comparisons.
- [Matching foundations](papers/matching_foundations.pdf): Hall's theorem, 4,477 regular-bipartite checks, and four extremal $K_{3,3}$ classes.

[All reports and LaTeX sources](papers/README.md) ·
[Projects](projects/README.md) · [Results and data](results/README.md) ·
[Code](src/README.md) · [Literature](notes/literature/README.md)

## Reproduce

Python **3.11+**; the mathematical computations use the standard library.

```sh
git clone https://github.com/Akhil-rav/discrete-math-lab.git
cd discrete-math-lab
python -m tools.verify_repository
```

This checks links and saved-file integrity, runs the tests, and reproduces
all nine reference datasets. GitHub runs the same checks on Linux and Windows.
Use `--static-only` for file checks alone.

[Experiment commands](experiments/README.md) ·
[Verification records](results/verification_index.md) ·
[LaTeX build instructions](papers/README.md)

Only figure regeneration needs the optional
[Matplotlib requirements](requirements-figures.txt). Reading the committed
PDFs and figures requires no installation.

These projects grew out of several months of study and were organized for
public release in November 2026.

Akhil Ravuri
