# Exact random-coloring probabilities: verification

**Outcome:** implementation and finite assertion verified in the stated range.
The counting identities below were self-reviewed; there is no independent
external refereeing or novelty claim.

## Mathematical contract

Six fixed hosts: C4, C6, C8, two disjoint C4s, K3,3, and the cube. Every edge
receives an independent, uniform label from q available colors. The coloring
is not conditioned on using all labels and need not be proper.

All 144 host/palette rows for q=1..24 use exact rational arithmetic. Five
additional cube rows use q=32,64,128,256,1024 for the scaled avoidance example.
Avoiding histograms are imported from the existing exhaustive sparse dataset;
this command does not re-enumerate the underlying partitions.

## Proof review

Primary verdict for the stated counting identities and moment/limit arguments:
**proved as written**, with the numerical applications depending on the validated
finite input histograms.

| Obligation | Status | Decisive argument |
|---|---|---|
| Sampling space | Passed | Each of the q^m labeled edge assignments has equal probability |
| Partition weight | Passed | A k-block equality partition has exactly (q)_k injective block labelings; different blocks cannot share labels |
| Single-matching event | Passed | (q)_n of q^n assignments have distinct colors |
| Pair event | Passed | Conditional on one rainbow matching, shared colors are distinct; the other matching's new edges use mutually distinct labels avoiding only the shared colors |
| Small palette | Passed | q<n makes every n-edge rainbow event impossible; the pair calculation bypasses potentially negative falling-factorial arguments |
| Second moment | Passed | Diagonal indicators square to themselves; each unordered pair appears twice |
| Upper bound | Passed | A nonnegative integer X has expectation at least Pr(X>0), clipped above by one |
| Lower bound | Passed | Nonnegative conditional variance gives E[X^2] >= E[X]^2/Pr(X>0); zero second moment is handled separately |
| Cycle check | Passed | Alternating matchings have disjoint edge sets, making the two events independent |
| Large-palette limit | Passed | The highest falling factorial is monic; lower-degree terms vanish after scaling |

The two-event formula does not assume that all matching events are mutually
independent. Testing every overlap of two four-position events includes more
general event sets than are necessary for two perfect matchings on one host.
The cube's limit coefficient 174 uses the validated fixed-edge partition count,
not the nine symmetry-class count. The five large-q values illustrate the limit;
they do not prove convergence or quantify an error bound.

Reviewed proof source: [random_rainbow.md](../notes/random_rainbow.md).
SHA-256: `f32bf992bfada4300413a440a3e73aec1d17609d450051bd1be4756c33e80ccb`.

## Independent finite checks

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
hashes were unchanged. Manifest validation passed against current inputs.
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

## Figure and presentation

The plot is rendered from the saved exact dataset with Matplotlib 3.10.7.
The optional renderer converts fractions to floats only for display. The
mathematical commands and tests require only the standard library. SVG and PNG
are exported; the final chart was visually inspected for axes, legend placement,
legibility, and agreement with the tabulated values. Shading shows the moment
bounds, not a confidence interval. No visual observation supplies a proof.

Scope and non-claims are stated in the [project report](../projects/random-colorings/report.md).
