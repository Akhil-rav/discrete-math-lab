# Reproducing the experiments

For the complete integrity, test, and reproduction sequence from a clean clone:

```sh
python -m tools.verify_repository
```

The [verification index](../results/verification_index.md) explains the exact
scope of the portable checker and how historical input hashes are interpreted.
The individual mathematical commands below remain available.

Python **3.11+**, standard library only. Run from the repository root.
All defaults are bounded and deterministic; no RNG, network, or optional solver
is required. The suite produces [stable JSON](../results/data/small_cases.json).

```sh
python -m unittest discover -s tests -v
python -m experiments.reproduce --check results/data/small_cases.json
python -m experiments.sparse_rainbow --check results/data/sparse_rainbow.json
python -m experiments.classify_cube --check results/data/cube_classification.json
python -m experiments.cube_collision_audit --check results/data/cube_collisions.json
python -m experiments.random_rainbow --check results/data/random_rainbow.json
python -m experiments.cycle_unions --check results/data/cycle_unions.json
python -m experiments.rainbow_inclusion_exclusion --check results/data/rainbow_inclusion_exclusion.json
python -m experiments.ladder_matchings --check results/data/ladder_matchings.json
python -m experiments.matching_covers --check results/data/matching_covers.json
```

To save fresh output without replacing the reference data:

```sh
python -m experiments.reproduce --output results/local-run.json
```

| Module (`python -m …`) | Finite assertion / bounds | Coverage and checks |
|---|---|---|
| `experiments.regular_bipartite_matchings` | Every labeled d-regular bipartite graph, 1≤n≤5 and 1≤d≤n, has a perfect matching | 4,477 graphs; independent generator/matching checks through n=3 |
| `experiments.rainbow_complete_bipartite` | Maximum avoiding colors for K22 and K33 | B4=15 and B9=21,147 partitions; independent edge-subset oracle |
| `experiments.sparse_rainbow` | Exact avoidance histograms on six hosts through 12 edges | Counted rejected subtrees; independent small-host partition oracle |
| `experiments.cycle_unions` | Ten specified even-cycle unions through 12 edges | Full partition search on six hosts through 10 edges; complete m-2, m-1, m color bands on all ten; subset-matching oracle and Stirling coverage checks |
| `experiments.classify_k33` | Group the 87 extremizers by Aut(K33) and color renaming | Full 72-element vertex action; closure and orbit/stabilizer checks |
| `experiments.classify_cube` | All S(12,7)=627,396 seven-color cube partitions, then all 174 avoiding partitions modulo graph symmetry | Nine classes; full 48-element action checked against all 8! vertex maps; matching-subset oracle |
| `experiments.cube_collision_audit` | Every nonempty cube edge subset and all 174 extremizers | 4,095 subset checks, incidence constants, and the proved extremal balance U+O=1; separate bit-mask and color-counter oracles |
| `experiments.matching_covers` | Weighted-cover optima on nine hosts; complete deficit bands 0..3 on L5 | All cost states checked separately; eight saved maxima reproduced; 41,835 band partitions and an independent block-shape oracle |
| `experiments.ladder_matchings` | All partitions on L2, L3, L4; every extremizer and exact probabilities for palettes 1..24 | 116,867 unpruned partitions; separate pruned solver; full vertex-automorphism and named-color oracles; coefficientwise polynomial agreement |
| `experiments.random_rainbow` | Exact probabilities and moment bounds on six hosts for palettes 1..24, plus five cube tail examples | Weighted partition counts; direct named-color, cycle-formula, and overlap-event oracles |
| `experiments.rainbow_inclusion_exclusion` | Exact counting polynomials and order-two/order-three Bonferroni bounds on the same six hosts | All coefficients agree with the histograms; 144 palette rows agree; matching families checked by edge subsets |
| `experiments.rainbow_progressions` | Exact aw for intervals/cyclic orders 3..9 and three specified products | All Bn partitions; independent equations for interval/cyclic/product AP generators |
| `experiments.color_coding_small_cases` | Color-mask DP on every graph of order ≤4 and every k-color assignment, 1≤k≤n | 22,955 permutation-oracle comparisons; exact probability and witness checks |
| `experiments.expansion_small_cases` | Exact cuts and walks on K4, C6, K33, 2K3 | All nonempty subsets up to half order; rational arithmetic; complete/cycle benchmarks |

The suite composes these modules. `--check` compares the mathematical JSON,
excluding machine-dependent provenance. A successful finite computation is not
a universal theorem or a novelty certificate.

The additional `tests/test_walk_formulas.py` compares rational walk evolution
with the closed formulas proved in the [walk paper](../papers/expansion_walks.pdf).
It checks K(d,d) for d=1..8 (ordinary and lazy), and r disjoint K_d for
r=2..4 and d=2..6 (lazy), at every time 0..12. Run it with
`python -m unittest discover -s tests -p test_walk_formulas.py -v`.

## Conventions and limits

The optional timing comparison uses fresh count caches, three trials with
alternating method order, and 24 exact probability evaluations per trial:

```sh
python -m experiments.benchmark_rainbow_methods --repeat 3 --output results/local-benchmark.json
```

Timings are machine-dependent and are not part of deterministic verification.
The [method comparison](../results/inclusion_exclusion.md) links raw samples
and describes the work included in each timed region.

The probability figure is a separate optional presentation step:
`python -m pip install -r requirements-figures.txt`, then
`python -m experiments.plot_random_rainbow`. This uses Matplotlib; all commands
in the main reproduction block and all mathematical checks remain
standard-library-only. Fractions are converted to floats only for plotting.

The additional `experiments.sparse_rainbow` command covers six specified hosts
through 12 edges. It uses exact rejection-subtree counts and independent small-host
checks; see the [project report](../projects/rainbow-matchings/report.md). It is
separate from the original dataset so the historical run remains reproducible.

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
