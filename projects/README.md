# Combinatorics project portfolio

This index separates implemented computational work from future study. The code
and prose were developed with AI assistance. Repository outputs are reproducible;
they are not evidence that the student independently derived or mastered them.
The learning checkpoints below are intended to establish that understanding.

| Project | Existing artifact | Status | Next student-owned contribution |
|---|---|---|---|
| **Rainbow matchings on sparse hosts** | [Flagship report](rainbow-matchings/report.md), [exact data](../results/data/sparse_rainbow.json), [solver](../src/rainbow_constraints.py) | Implemented; finite computational observations; no novelty claim | Explain pruning; prove the cycle formula without code; analyze one extremal cube coloring |
| Extremal colorings and symmetry | [K33 classification](../results/k33_classification.md) | Implemented exhaustive finite classification | Derive one orbit size by hand; distinguish the last two classes structurally |
| Additive combinatorics | [Progression note](../notes/rainbow_progressions.md), [data](../results/rainbow_progressions.md) | Known benchmarks reproduced | Explain why interval and cyclic domains differ; verify a witness by hand |
| Parameterized graph algorithms | [Color-coding](../notes/color_coding.md) | Standard method implemented and checked | Derive the recurrence and success probability; add a directed worked example |
| Expansion and discrete probability | [Walk note](../notes/expansion_and_walks.md), [results](../results/algorithm_demos.md) | Exact finite demonstrations | Derive a transition matrix and explain the parity obstruction |

These are five tracks within one lab, not five claimed publications. Future
hypergraph experiments should reuse the exact-search and witness-checking habits
established here after their definitions and source results have been studied.

## What makes a project ready to show

A reader should be able to identify its precise question, see what is already
known, reproduce the computation, inspect a witness, and tell which reasoning
the student can explain independently. The [first-session worksheet](first-session.md)
and [12-week plan](roadmap.md) give concrete ways to progress toward that standard.

The working changes are reviewed in [PR #1](https://github.com/Akhil-rav/discrete-math-lab/pull/1).
An open pull request is not part of the default branch until merged.
