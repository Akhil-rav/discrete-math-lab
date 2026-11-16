# The finite base for the ladder classification

The companion note [How many perfect matchings test a ladder?](../papers/ladder_tests.pdf)
proves the logarithmic test-family bounds and gives the unique minimum list for
five columns. To reproduce the check of all 39,325 deficit-three partitions and
all 256 candidate lists, run

```sh
python -m unittest discover -s tests -p test_ladder_test_families.py -v
```

The [working note](../papers/ladder_stability.pdf) reduces the classification at
every length above 17 to a shorter ladder. Both searches below keep edges fixed
and ignore color names. They compare the actual repeated edge classes with the
[fifteen constructions](../src/l5_extremizers.py).

| Columns | Perfect matchings | One quadruple | Triple and pair | Three pairs |
|---:|---:|---:|---:|---:|
| 5 | 8 | 4 | 8 | 3 |
| 6 | 13 | 4 | 8 | 3 |
| 7 | 21 | 4 | 8 | 3 |
| 8 | 34 | 4 | 8 | 3 |
| 9 | 55 | 4 | 8 | 3 |
| 10 | 89 | 4 | 8 | 3 |
| 11 | 144 | 4 | 8 | 3 |
| 12 | 233 | 4 | 8 | 3 |
| 13 | 377 | 4 | 8 | 3 |
| 14 | 610 | 4 | 8 | 3 |
| 15 | 987 | 4 | 8 | 3 |
| 16 | 1,597 | 4 | 8 | 3 |
| 17 | 2,584 | 4 | 8 | 3 |

Run both commands from the repository root with Python 3.11 or later.

```sh
python -m experiments.ladder_stability
python -m unittest discover -s tests -p test_ladder_stability.py -v
```

The [first search](../experiments/ladder_stability.py) enumerates the three
possible shapes and uses intersections of matchings to complete a partition.
Its [recorded output](runs/ladder-stability-2026-11-16/stdout.txt) and
[input and output hashes](runs/ladder-stability-2026-11-16/manifest.json)
come from the November 16 run with Python 3.13.7.
The [second search](../tests/test_ladder_stability.py) constructs matchings
directly from vertex adjacency, then searches sequences of three color merges.
The test compares both sets of perfect matchings, both sets of partitions,
and the explicit list. The earlier [direct count](../notes/l5_extremizers.md)
gives a pencil-and-paper check of the first row. The table supplies the finite
part of a computer-assisted proof. External review and prior coverage of the
classification remain to be established.
