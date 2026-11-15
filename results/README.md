# Results

| Study | Result | Evidence |
|---|---|---|
| Independent random edge colors | Exact probabilities on six hosts, moment bounds, and a cube tail coefficient | [Report and plot](../projects/random-colorings/report.md), [data](data/random_rainbow.json), [verification](random_rainbow_verification.md) |
| Cube incidence bound | A(Q3)=7 by proof; capacity balance U+O=1; 150/24 extremal split checked | [Proof](../notes/cube_upper_bound.md), [collision audit](cube_collisions.md) |
| Cube extremal colorings | Nine symmetry classes among all 174 seven-color extremizers | [Classification and atlas](cube_classification.md), [complete data](data/cube_classification.json) |
| Expansion and random walks | Exact family formulas for cuts, periodicity, lazy mixing, and disconnection | [Expository paper](../papers/expansion_walks.pdf), [verification](walk_paper_verification.md) |
| Disjoint unions of even cycles | A(G)=|E(G)|-2 and all extremizers, counted by sum binomial(n_i,2)^2 | [General proof](../papers/cycle_extremizers.pdf), [verification and ten-host checks](cycle_union_verification.md), [data](data/cycle_unions.json) |
| Sparse bipartite hosts | Six exact searches through 12 edges, including the cube | [Report](../projects/rainbow-matchings/report.md), [data](data/sparse_rainbow.json) |
| Complete bipartite hosts | A(K22)=2 and A(K33)=4 | [Reproduction of published thresholds](rainbow_knn_small_cases.md) |
| Extremal K33 colorings | Four symmetry classes among 87 extremizers | [Finite classification](k33_classification.md) |
| Regular bipartite graphs | 4,477 labeled graphs with perfect matchings | [Hall-corollary reproduction](regular_bipartite_small_cases.md) |
| Rainbow progressions | Exact thresholds on small intervals and groups | [Tables and conventions](rainbow_progressions.md) |
| Color-coding and expansion | Independent path checks and exact walk examples | [Algorithm demonstrations](algorithm_demos.md) |

## Data and verification

[Verification index](verification_index.md) collects the proof reviews, run
records, reference datasets, and the portable integrity/reproduction command.

- [Original deterministic dataset](data/small_cases.json)
- [Sparse-host dataset](data/sparse_rainbow.json)
- [Original execution record](verification.md)
- [Sparse-host execution record](sparse_verification.md)

Historical manifests and logs remain in `runs/`, with mathematical contracts
in `contracts/`. Finite computations are reported within their stated bounds;
the writeups distinguish them from general proofs and cited results.
