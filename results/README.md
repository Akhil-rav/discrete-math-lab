# Results

| Study | Result | Evidence |
|---|---|---|
| Cycles and two disjoint squares | Maximum color counts and complete extremal partition counts | [Elementary proofs](../papers/cycle_extremizers.pdf) |
| Sparse bipartite hosts | Six exact searches through 12 edges, including the cube | [Report](../projects/rainbow-matchings/report.md), [data](data/sparse_rainbow.json) |
| Complete bipartite hosts | A(K22)=2 and A(K33)=4 | [Reproduction of published thresholds](rainbow_knn_small_cases.md) |
| Extremal K33 colorings | Four symmetry classes among 87 extremizers | [Finite classification](k33_classification.md) |
| Regular bipartite graphs | 4,477 labeled graphs with perfect matchings | [Hall-corollary reproduction](regular_bipartite_small_cases.md) |
| Rainbow progressions | Exact thresholds on small intervals and groups | [Tables and conventions](rainbow_progressions.md) |
| Color-coding and expansion | Independent path checks and exact walk examples | [Algorithm demonstrations](algorithm_demos.md) |

## Data and verification

- [Original deterministic dataset](data/small_cases.json)
- [Sparse-host dataset](data/sparse_rainbow.json)
- [Original execution record](verification.md)
- [Sparse-host execution record](sparse_verification.md)

Historical manifests and logs remain in `runs/`, with mathematical contracts
in `contracts/`. Finite computations are reported within their stated bounds;
the writeups distinguish them from general proofs and cited results.
