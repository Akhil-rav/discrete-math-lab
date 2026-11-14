# Cube classification: verification record

**Outcome:** implementation and finite assertion verified in the stated domain.
Review is a self-review with independent algorithms, not external refereeing.
No novelty is claimed.

## Exact contract and result

Host: the single cube Q3 represented by K4,4 minus the diagonal, with edge order
01,02,03,10,12,13,20,21,23,30,31,32. Arbitrary edge colorings need not be proper.
Color names are removed by restricted-growth normalization. Graph symmetries
are applied only in the orbit classification.

All S(12,7)=627,396 partitions into exactly seven colors were tested against
all nine perfect matchings; 174 avoid every rainbow perfect matching. The
48-element graph automorphism group splits them into nine orbits of sizes
12,4,4,48,12,48,24,6,16, with stabilizer sizes 4,12,12,1,4,1,2,8,3.
The dataset saves every orbit member and every matching constraint.

The seven-color pass alone is not an upper-bound proof. The existing full
sparse search, independently rerun in the tests, establishes maximum seven
and population 174 by exact Bell-number coverage.

## Implementation and orthogonal checks

- `src/cube_symmetry.py`: target-block partitions and source-to-image edge maps.
- `experiments/classify_cube.py`: exact search, orbits, explicit stabilizers.
- `tests/test_cube_classification.py`: all 8! vertex permutations; all four-edge
  matching subsets; equal-color-pair avoidance oracle; group composition;
  small-order target-partition comparison against unfiltered partitions.
- All 174 members are distinct and avoiding; orbits are disjoint, closed in the
  avoiding population, and cover it. All orbit-stabilizer products equal 48.
- Block sizes, largest-block vertex degrees, and matching multiplicity profiles
  distinguish the nine classes. The three displayed six-edge degree sequences
  are checked directly against the graph.
- No sampling, floating-point arithmetic, stochastic seed, or external solver.

Commands, from the root:

```sh
python -m unittest discover -s tests -v
python -m experiments.classify_cube --check results/data/cube_classification.json
python -m experiments.reproduce --check results/data/small_cases.json
python -m experiments.sparse_rainbow --check results/data/sparse_rainbow.json
```

All 20 tests passed. Both earlier datasets reproduced exactly. The new complete
classification equals the bounded run's saved JSON byte for byte.

## Execution provenance

The recorded classification ran with Python 3.13.7 on Windows 11, in exact
integer arithmetic. Runtime: 1.247629 seconds. Wall limit: 30 seconds; log
limit: 1 MiB. No memory or CPU hard cap was requested. Status: **completed**,
exit code 0. All five declared input hashes were unchanged. Manifest validation
passed against the current working tree. The tests ran separately; the manifest
records classification execution, not the test suite.

- [Contract](contracts/cube-classification.json)
- [Version-2 manifest](runs/cube-classification-2026-11-14/manifest.json)
- [Recorded dataset](runs/cube-classification-2026-11-14/classification.json)
- [stdout](runs/cube-classification-2026-11-14/stdout.txt) and
  [stderr](runs/cube-classification-2026-11-14/stderr.txt)

## Proof and interpretation checks

The group-order argument is internal and proved as written: connected
bipartiteness forces preservation or exchange of the parts; preserving maps
must agree on the unique cross-part nonneighbor; all simultaneous permutations
and their part swaps work. Completeness is also checked against all vertex maps.
The classification is finite enumerative evidence rather than an asymptotic
statement. The literature comparison remains limited as documented in the
[source note](../notes/literature/cube_classification.md).

## Presentation

The three-page note and labeled SVG atlas are generated from the same dataset.
The renderer only presents data; it is not part of the classification oracle.
Numerical labels on all edges make color equality readable independently of
palette. Nested-square drawings have no crossing edges. The drawing's binary
coordinate model is isomorphic to the explicitly ordered bipartite host.
The LaTeX was compiled, proofread for notation and references, and its rendered
pages visually inspected. These presentation checks do not add mathematical
independence to the review.
