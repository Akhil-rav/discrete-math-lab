# Research guide

This guide distinguishes completed work from possible extensions. It is a
navigation aid for readers assessing the mathematics and its reproducibility.
Proposed tasks are not certified open problems.

| Direction | What is implemented | Evidence | Next bounded task |
|---|---|---|---|
| Independent random edge colors | Two exact polynomial methods, matching moments, and higher-order bounds | [Report and plot](random-colorings/report.md), [methods and timings](../results/inclusion_exclusion.md) | Compare cache growth under different fixed edge orders on the same hosts |
| Rainbow perfect matchings | Sparse-host searches, nine cube classes, an incidence proof of the cube bound | [Report](rainbow-matchings/report.md), [cube atlas](../results/cube_classification.md), [cube proof](../notes/cube_upper_bound.md) | Compare the incidence method with other specified small hosts and precise literature statements |
| Expansion and walks | Exact cuts and rational walk evolution on four regular graphs | [Report](expansion-and-walks/report.md), benchmark tests | Add an independent transition-matrix oracle before extending the graph domain |
| Rainbow arithmetic progressions | Exact searches on small intervals and specified finite groups | [Results](../results/rainbow_progressions.md), [definitions](../notes/rainbow_progressions.md) | Compare one published theorem with its precise hypotheses and small examples |
| Color-coding | Colorful-path subset dynamic programming | [22,955 finite comparisons](../results/algorithm_demos.md) | Document runtime and memory scaling without confusing experiments with asymptotic proofs |

## Literature connections

Michael Young's matching and progression papers are directly related to the
rainbow studies. See the [matching literature notes](../notes/literature/young_and_matchings.md)
and [source records](../notes/literature/source_records.md) for verified statements,
threshold conventions, and access limitations.

Huy Tuan Pham's [research and publication list](https://huytuanpham.github.io/)
includes combinatorics, probability, and work with Vishesh Jain on thresholds
for Latin squares, Steiner triple systems, and edge colorings. These themes
provide context for further reading. Threshold and proper-coloring questions
should not be identified with this repository's rainbow-avoidance objective.
No theorem from those papers is used here without a separate source check.

Max Hopkins's [lecture materials](https://cseweb.ucsd.edu/~nmhopkin/) connect
expansion to broader theoretical computer science. The current ordinary-graph
walk study is preparatory and does not implement high-dimensional expansion.

Zihan Zhang's [IAS profile](https://www.ias.edu/scholars/zihan-zhang) describes
coding theory, combinatorics, and pseudorandomness. Error-correcting codes are
not currently implemented in this repository. An introductory coding project
would be a new direction requiring finite-field linear algebra and separate
verification, rather than a relabeling of the existing matching experiments.

These are subject connections, checked November 13, 2026. They imply no
collaboration, mentoring arrangement, acceptance, or endorsement.

## Reading a result

For each result, check the host and target, whether colors label vertices or
edges, the equivalence relation used when counting, and whether evidence is a
proof, an exhaustive finite search, or a cited external theorem. A reproducible
small case alone does not establish a general theorem or novelty.
