# Reproducing the experiments

Python **3.11+**, standard library only. Run from the repository root.
All defaults are bounded and deterministic; no RNG, network, or optional solver
is required. The suite produces [stable JSON](../results/data/small_cases.json).

```sh
python -m unittest discover -s tests -v
python -m experiments.reproduce --check results/data/small_cases.json
```

To save fresh output without replacing the reference data:

```sh
python -m experiments.reproduce --output results/local-run.json
```

| Module (`python -m …`) | Finite assertion / bounds | Coverage and checks |
|---|---|---|
| `experiments.regular_bipartite_matchings` | Every labeled d-regular bipartite graph, 1≤n≤5 and 1≤d≤n, has a perfect matching | 4,477 graphs; independent generator/matching checks through n=3 |
| `experiments.rainbow_complete_bipartite` | Maximum avoiding colors for K22 and K33 | B4=15 and B9=21,147 partitions; independent edge-subset oracle |
| `experiments.classify_k33` | Group the 87 extremizers by Aut(K33) and color renaming | Full 72-element vertex action; closure and orbit/stabilizer checks |
| `experiments.rainbow_progressions` | Exact aw for intervals/cyclic orders 3..9 and three specified products | All Bn partitions; independent equations for interval/cyclic/product AP generators |
| `experiments.color_coding_small_cases` | Color-mask DP on every graph of order ≤4 and every k-color assignment, 1≤k≤n | 22,955 permutation-oracle comparisons; exact probability and witness checks |
| `experiments.expansion_small_cases` | Exact cuts and walks on K4, C6, K33, 2K3 | All nonempty subsets up to half order; rational arithmetic; complete/cycle benchmarks |

The suite composes these modules. `--check` compares the mathematical JSON,
excluding machine-dependent provenance. A successful finite computation is not
a universal theorem or a novelty certificate.

## Conventions and limits

- Bipartite edges are ordered left/right pairs; arrays use row-major order.
- Restricted-growth strings remove color names only. Vertex symmetries are
  removed only in the separate classification experiment.
- Progressions have three distinct terms; duplicate presentations are removed.
  With no such AP, the convention is aw=|S|+1.
- Color-coding colors vertices and counts k vertices; anti-Ramsey matching
  experiments color edges and count matching edges.
- Expansion is boundary edges divided by subset size, without degree normalization.
- Arithmetic is exact: no floating-point tolerances or sampling seeds.
- Bell-number enumeration grows rapidly; `exhaustive_search` supports n=2,3 only.

[Recorded verification](../results/verification.md) documents environment,
input/output hashes, and bounded execution. The commands above do not depend
on the external provenance helper used for that historical run.
