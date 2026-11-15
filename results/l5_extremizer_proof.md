# Direct five-column classification: proof checks

The [counting proof](../notes/l5_extremizers.md) establishes exactly fifteen
ten-color avoiding partitions of L5, split as 4 + 8 + 3 by nonsingleton
class sizes, and explains all six graph-symmetry classes.

Proof source SHA-256: `b7f64efe1f6821789d397eeecccb2b33d3ebd0a36989d8ae0a7da649cc181f3e`.

## Argument and scope

The proof uses the earlier maximum $A(L_5)=10$, then lists the eight perfect
matchings by their horizontal gaps. Deficit three leaves exactly the three
class-size shapes treated in the argument.

- A quadruple must meet the two disjoint double-gap matchings twice.
  The all-rung and remaining double-gap matchings force the two end rungs
  and one rail edge from each end gap, giving four choices.
- A triple must block at least five matchings, since a pair blocks at most
  three. Triples with at most one rung fail this bound; the sole possible
  three-rung triple leaves no common residual pair. The two-rung incidence
  table and reflection cover all ten rung pairs. Four forms survive, each
  with two rail choices and a unique disjoint completing pair.
- Three pairs must include at least two of the five pairs occurring in
  three matchings. All eight disjoint choices are listed. Their residual
  intersections give only three distinct completions; the central family,
  encountered three times, is counted once.
- A corner determines an automorphism. The four geometric maps give the
  full group, and the proved block families split into orbits of sizes
  4, 2, 2, 2, 4, 1 in the saved representative order.

Every listed family is also shown to block all eight matchings. The count
keeps edges fixed and ignores color names; the six-class quotient is separate.
This is an internal check of the written argument, not external refereeing.
The proof does not rely on the coloring enumerator.

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
