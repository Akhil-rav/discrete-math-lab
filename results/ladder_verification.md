# Small ladders: computation checks

The [elementary proof](../notes/ladders.md) establishes $A(L_2)=2$,
$A(L_3)=4$, and $A(L_4)=7$. The [classification report](ladder_matchings.md)
separately records the computed extremizers and probabilities.

Proof source SHA-256: `f37e42fa9bcf12f5253f7e92204c8c76e741af9eac04bf29bf55f0cd082aa529`.

The maximum-color argument is given in the linked note. The classification
and probabilities are checked by the finite computations below.

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

The later [family formula and cover reduction](matching_covers.md) have a
separate written proof and verification record. The three-host dataset above
retains its original finite scope.
