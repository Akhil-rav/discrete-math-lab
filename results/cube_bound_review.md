# Cube incidence bound and collision checks

Proof source SHA-256: `cdb44456a50eab91c761c656ee5de69669232455d9d258745573d3e2c4602e1d`.

The [incidence proof](../notes/cube_upper_bound.md) establishes $A(Q_3)=7$
and the capacity identity $U+O=1$ for every avoiding seven-color partition.
The [LaTeX report](../papers/cube_classification.pdf) includes the proof
and complete symmetry atlas.

The [collision results](cube_collisions.md) connect that identity with
the exhaustive extremal population.

## Finite checks

- All 4,095 nonempty subsets of the twelve-edge cube are checked against
  the one-class bound $b(B)\le2(|B|-1)$.
- Every one of the 174 extremizers satisfies the capacity identity.
- The split is 150 partitions with $(U,O)=(1,0)$ and 24 with $(U,O)=(0,1)$.
  The latter population is exactly symmetry class seven.
- Independent bit-mask and matching color-counter predicates check the
  obstruction counts. The proof itself does not depend on these computations.

## Reproduce

```sh
python -m unittest tests.test_cube_collisions -v
python -m experiments.cube_collision_audit --check results/data/cube_collisions.json
```

[Data](data/cube_collisions.json) ·
[Execution record and test scope](cube_collision_verification.md).

The source comparison and its access limits are recorded in
[the literature note](../notes/literature/cube_classification.md).
