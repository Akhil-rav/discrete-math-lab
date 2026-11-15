# Ladder verification

The [elementary proof](../notes/ladders.md) establishes $A(L_2)=2$,
$A(L_3)=4$, and $A(L_4)=7$. The [classification report](ladder_matchings.md)
separately records the computed extremizers and probabilities.

Proof source SHA-256: `802651379d558af79efefd46f1985a22a4ce474450890f8130369e70171ada36`.

## Proof checks

The first-column split gives the complete lists of 2, 3, and 5 matchings.
The lower-bound pairs are disjoint and cover those lists. Merging classes
preserves avoidance, so ruling out deficit two suffices for the larger hosts.
All deficit-two partitions have one triple or two doubletons; no other
nonsingleton shapes are possible. The pair capacities and triple incidence
bounds rule out both cases. The square is handled separately.

This is an internal proof check of the stated three bounds. The matching
incidences are also tested, but the proof can be read directly from the lists.
The classification completeness comes from the finite computation below,
rather than from the maximum-color proof.

## Finite computation

- Ladders with 2, 3, and 4 columns, hence 4, 7, and 10 edges.
- All 116,867 edge partitions visited without rainbow pruning; separate
  pruned histograms agree.
- Column-recursive, endpoint-subset, and bipartite-permutation matching lists
  agree.
- All 53 fixed-edge extremizers retained. Explicit symmetry orbits partition
  the population; orbit–stabilizer products are 8, 4, and 4 by host.
- Tests enumerate every vertex bijection, through $8!$, to recover the full
  automorphism groups independently of the reflection construction.
- Count polynomials agree coefficient by coefficient between the two methods;
  probabilities agree for every palette size 1 through 24.
- Tests directly enumerate all named-color assignments for L2 with 1–4
  labels, L3 with 1–3 labels, and L4 with 1–4 labels. These checks include
  nonzero rainbow probabilities on every host.
- Bell numbers are also recovered from a separate Stirling-number recurrence.

## Run record

[Contract](contracts/ladder-matchings.json) ·
[Manifest](runs/ladder-matchings-2026-11-15/manifest.json) ·
[Recorded complete data](runs/ladder-matchings-2026-11-15/ladder_matchings.json) ·
[Standard output](runs/ladder-matchings-2026-11-15/stdout.txt) ·
[Standard error](runs/ladder-matchings-2026-11-15/stderr.txt).

The recorded run completed successfully under a 60-second wall-clock limit.
Declared inputs were unchanged during the run; the manifest records their
hashes and the output hashes. The reference dataset matches the recorded
result. Windows did not supply POSIX memory or CPU caps; none are claimed.

```sh
python -m experiments.ladder_matchings --check results/data/ladder_matchings.json
python -m unittest tests.test_ladders -v
python -m tools.verify_repository
```

The [literature comparison](../notes/literature/ladders.md) is limited.
No conclusion for all ladder lengths, novelty assessment, or external review
follows from these checks.
