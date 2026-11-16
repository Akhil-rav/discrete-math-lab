# Exact random-coloring probabilities: verification

Proof source SHA-256: `758f411073ff47541672d8a081bdeb35bfe54d5a06e085e01fd52b63a78f0393`.

The computation checks exact probabilities and moment bounds on the six
hosts below. The [counting note](../notes/random_rainbow.md) gives the proofs.

## Model and range

Six fixed hosts: C4, C6, C8, two disjoint C4s, K3,3, and the cube. Every edge
receives an independent, uniform label from q available colors. The coloring
is not conditioned on using all labels and need not be proper.

All 144 host/palette rows for q=1..24 use exact rational arithmetic. Five
additional cube rows use q=32,64,128,256,1024 for the scaled avoidance example.
Avoiding histograms are imported from the existing exhaustive sparse dataset;
this command does not re-enumerate the underlying partitions.

The [counting note](../notes/random_rainbow.md) proves the identities used
by the implementation. This record documents the model, test ranges, and
executed computation.

## Finite checks

- Direct named-color enumeration on C4 (q=1..5), C6 (q=1..4), and two disjoint
  squares (q=1..4) checks the exact success probability and both moments.
- Analytic cycle probabilities check C4, C6, C8 for every q=1..24.
- Direct named-color enumeration of two four-position events checks all shared
  position counts 0..3 with every q=1..4.
- Every main-grid row satisfies lower <= exact <= upper within [0,1], using
  fractions rather than tolerances. Palettes below matching size have probability zero.
- The reported cube limit coefficient equals its saved extremal-partition count.
- At the probability-study checkpoint, the project suite had 26 passing tests.
  The [verification index](verification_index.md) describes current checks.
  All four earlier reference datasets
  regenerate unchanged; the new probability dataset matches the recorded run.

## Provenance

Python 3.13.7, Windows 11, exact integers and fractions, no sampled random values.
Runtime: 0.139785 seconds; status **completed**, exit 0. Wall limit 30 seconds;
log limit 1 MiB; no CPU/memory hard caps requested. All five declared input
hashes were unchanged. Manifest validation passed for those recorded inputs.
The tests run separately; the manifest records the probability-table command.

- [Contract](contracts/random-rainbow.json)
- [Manifest](runs/random-rainbow-2026-11-14/manifest.json)
- [Recorded data](runs/random-rainbow-2026-11-14/probabilities.json)
- [stdout](runs/random-rainbow-2026-11-14/stdout.txt) and
  [stderr](runs/random-rainbow-2026-11-14/stderr.txt)

```sh
python -m experiments.random_rainbow --check results/data/random_rainbow.json
python -m unittest discover -s tests -v
```

## Figure

The plot is rendered from the saved exact dataset with Matplotlib 3.10.7.
The optional renderer converts fractions to floats only for display. The
mathematical commands and tests require only the standard library. SVG and PNG
are exported. Shading shows the moment bounds, not a confidence interval.

The model and tested range are described in the [project report](../projects/random-colorings/report.md).

## Inclusion-exclusion extension

The counting note also gives the conflict-graph bijection, inclusion-exclusion
identity, addition/contraction recurrence, and order-two/order-three Bonferroni
bounds. The recurrence partitions colorings by equality of two nonadjacent
vertices. Unused host-edge positions remain isolated; complete graphs and the
empty graph give the falling-factorial terminal values. Nonnegative binomial
remainders give the bounds, including X=0 and families with fewer than three
matchings. These arguments require no experimental premise.

The [method comparison](inclusion_exclusion.md) records the separate finite
checks, polynomial coefficient identities, and timings. The numerical
applications use the six specified hosts.
