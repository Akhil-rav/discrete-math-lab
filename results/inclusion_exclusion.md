# Two exact methods for rainbow-matching probabilities

[Paper](../papers/random_rainbow.pdf) · [Counting proofs](../notes/random_rainbow.md)
· [Polynomial data](data/rainbow_inclusion_exclusion.json)

The partition method counts avoiding equality patterns, then weights them by
falling factorials. The new method instead applies inclusion-exclusion to the
perfect-matching events. For each selected family, a conflict graph records
which edge positions must receive different colors. Its proper-coloring
polynomial counts assignments making all selected matchings rainbow.

Both are implementations of standard counting identities. The new counting
engine reads only the edge count and target family; it does not read a saved
avoiding histogram.

## Exact agreement

On every host, the resulting polynomial agrees coefficient by coefficient with
q^m minus the weighted avoiding histogram. All 144 probabilities for q=1..24
also agree with the existing data. Matching families are generated from edge
subsets and compared with the permutation generator.

| Host | Perfect matchings | Nonempty event families | Cached chromatic subproblems |
|---|---:|---:|---:|
| C4 | 2 | 3 | 5 |
| C6 | 2 | 3 | 5 |
| C8 | 2 | 3 | 5 |
| Two disjoint C4s | 4 | 15 | 101 |
| K3,3 | 6 | 63 | 2,652 |
| Cube | 9 | 511 | 156,885 |

Each conflict graph includes all host-edge positions, including isolated
positions unused by the selected matchings. This retains their free color
choices and keeps the probability denominator equal to q^m. Addition/contraction
counts proper colorings, with complete-graph and connected-component terminal
rules; all arithmetic is integral until the final rational probability.

## Higher-order bounds

For T_j equal to the sum of j-event intersection probabilities, the second and
third Bonferroni partial sums give

$$\max(0,T_1-T_2)\le\Pr(X>0)\le\min(1,T_1-T_2+T_3).$$

At q=4 on the cube, T_1=27/32, T_2=45/128, and T_3=3/32. Thus

$$\frac{63}{128}\le\frac{4653}{8192}\le\frac{75}{128}.$$

This improves the earlier first/second-moment interval at that palette. All
144 rows are checked exactly. These are applications of standard inequalities,
not a new general probability bound. The two-event sum also agrees with
(E[X^2]-E[X])/2, independently checking the matching-overlap formula.

## Measured construction times

Milliseconds below are medians of three trials, recorded with Python 3.13.7
on Windows 11, Intel64 Family 6 Model 186. Both methods construct counts from
the host and evaluate all 24 palettes. The timed region includes matching
generation and the new method's subset/permutation cross-check. It excludes
imports, host definitions, and file I/O. Counting caches start empty per call;
method order alternates by trial. The [raw record](runs/rainbow-method-benchmark-2026-11-15/benchmark.json)
contains every sample and the environment details.

| Host | Partition search (ms) | Inclusion-exclusion (ms) |
|---|---:|---:|
| C4 | 0.122 | 0.109 |
| C6 | 0.267 | 0.132 |
| C8 | 3.633 | 0.193 |
| Two disjoint C4s | 3.961 | 1.188 |
| K3,3 | 3.548 | 22.688 |
| Cube | 1589.737 | 2790.843 |

In this run, inclusion-exclusion was faster on the cycles and disjoint squares;
the partition search was faster on K3,3 and the cube. Cycles have just two
matching events, whose conflict graphs split into complete graphs and isolated
vertices. Overlapping matching families can generate many more chromatic
subproblems. C4's very small times do
not support a useful speed distinction. The 511 cube event families required
156,885 cached chromatic subproblems, so counting event families alone is not
an estimate of total work. Three trials on one machine do not give an
asymptotic comparison or a confidence interval. Evaluating probabilities from
already-saved histograms is a separate, cheaper task than the construction
measured here.

## Checks and limits

- Every simple labeled graph through four vertices (76 graphs) is checked
  against named proper-coloring enumeration for q=0..4, including the empty
  graph and zero-color boundary.
- Every nonempty family of two-position events on four positions (63 families)
  is checked against direct named-color enumeration for q=1..4.
- A mixed-size target family checks every intersection sum by direct counting.
- All relabelings of one four-vertex graph, isolated positions, singleton
  targets, duplicate targets, and invalid domains are checked separately.
- The six full counting polynomials are compared exactly with the earlier
  exhaustive histograms, using a signed-Stirling conversion implemented outside
  the new counting engine. The coefficient identity checks all palette sizes.

The implementation is capped at twelve positions and nine targets. Recurrence
caching does not remove its exponential worst-case growth. These are finite
implementation checks accompanying the written bijection and counting proofs.

## Reproduce

```sh
python -m experiments.rainbow_inclusion_exclusion --check results/data/rainbow_inclusion_exclusion.json
python -m unittest discover -s tests -p test_inclusion_exclusion.py -v
python -m experiments.benchmark_rainbow_methods --repeat 3 --output results/local-benchmark.json
```

Only the first command compares deterministic reference data. Benchmark
seconds vary across runs and are not used as a CI equality check. All commands
use Python 3.11+ and its standard library.

Recorded runs on November 15, 2026:

- [Exact-comparison contract](contracts/inclusion-exclusion.json) and
  [manifest](runs/inclusion-exclusion-2026-11-15/manifest.json): completed,
  exit zero, about 1.87 seconds under a 60-second wall cap.
- [Benchmark contract](contracts/rainbow-method-benchmark.json) and
  [manifest](runs/rainbow-method-benchmark-2026-11-15/manifest.json): completed,
  exit zero, about 12.07 seconds under a 120-second wall cap.

The manifests retain the input versions and hashes, revision and dirty state,
interpreter, output hashes, and exact commands. Both observed unchanged inputs.
