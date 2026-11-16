# Direct five-column classification: construction checks

The [counting proof](../notes/l5_extremizers.md) establishes exactly fifteen
ten-color avoiding partitions of L5, split as 4 + 8 + 3 by nonsingleton
class sizes, and explains all six graph-symmetry classes.

Proof source SHA-256: `b7f64efe1f6821789d397eeecccb2b33d3ebd0a36989d8ae0a7da649cc181f3e`.

The note gives the direct counting argument. The tests below compare its
constructed families with the independently saved exhaustive population.

## Implementation checks

[Construction module](../src/l5_extremizers.py) ·
[Tests](../tests/test_l5_extremizers.py) ·
[Earlier exhaustive data](data/matching_covers.json).

Four focused tests check:

- The fifteen constructed partitions are distinct, have ten colors, avoid
  every endpoint-generated perfect matching, and equal the older saved set.
  Their shapes occur 4, 8, and 3 times.
- All ten two-rung incidence rows, including reflected rows and both rail
  choices, agree with the endpoint-based matching list.
- The five maximum-support pairs and every residual-intersection row are
  correct, with all eight disjoint choices covered.
- The constructed population splits into exactly the saved six disjoint orbits.

No new search dataset replaces the previous results. The full repository
command continues to reproduce all nine reference datasets.

```sh
python -m unittest tests.test_l5_extremizers -v
python -m tools.verify_repository
```

The [source record](../notes/literature/ladders.md) retains the literature
search limits. A direct proof of this finite classification does not establish
novelty or an extremizer formula for every ladder length.
