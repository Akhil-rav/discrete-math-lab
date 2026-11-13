# Small rainbow-progression thresholds

**Status:** exhaustive finite computations; selected known benchmarks reproduced.

Run `python -m experiments.rainbow_progressions`. Definitions and the no-progression
convention are in [the note](../notes/rainbow_progressions.md). Counts and avoiding
witnesses are in [the data](data/small_cases.json).

| n | Bell number: partitions per domain | aw([n],3) | aw(Zn,3) |
|---:|---:|---:|---:|
| 3 | 5 | 3 | 3 |
| 4 | 15 | 4 | 3 |
| 5 | 52 | 4 | 3 |
| 6 | 203 | 4 | 4 |
| 7 | 877 | 4 | 3 |
| 8 | 4,140 | 5 | 3 |
| 9 | 21,147 | 4 | 4 |

Each interval and cyclic group is searched separately. Interval values for
3≤n≤8 agree with BE+16 Theorem 1.1. No monotonicity is assumed: the interval
threshold drops from n=8 to n=9.

| Group | Partitions checked | Distinct 3-AP sets | aw(G,3) |
|---|---:|---:|---:|
| Z2×Z2 | 15 | 0 | 5 |
| Z2×Z4 | 4,140 | 16 | 5 |
| Z2×Z2×Z2 | 4,140 | 0 | 9 |

With no nondegenerate progression, the threshold is |G|+1 by convention;
it does not assert a feasible coloring with that many colors. Z2×Z4 is an
enumerated example, not an implementation of Young's general group formula.

Interval AP generation was checked against all triples satisfying a+c=2b;
cyclic AP generation against all triples with some ordering satisfying that
equation modulo n. Partition counts were checked by the Stirling recurrence.
