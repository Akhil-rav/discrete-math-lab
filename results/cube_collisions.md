# The cube bound: incidence, capacity, and overlap

**Status:** elementary proof plus finite implementation checks. No novelty claim.

[Complete proof](../notes/cube_upper_bound.md) · [Typeset report](../papers/cube_classification.pdf)
· [Audit data](data/cube_collisions.json) · [Proof review](cube_bound_review.md)

The cube has nine perfect matchings. Each edge belongs to three, and each
pair of distinct edges belongs together to at most two. These statements have
short counting proofs in the linked note.

For a nonempty color class B with s edges, let b(B) count perfect matchings
containing at least two of its edges. The incidence argument gives

$$b(B)\le 2(s-1).$$

Every avoiding coloring must obstruct all nine matchings. With r colors,
the sum of these capacities is 2(12-r), so

$$9\le 2(12-r),\qquad r\le7.$$

The usual seven-color construction attains the bound. **A(Q3)=7 is now proved
without exhaustive search.** The computation still supplies the complete
nine-orbit classification, which this inequality alone does not establish.

## What equality says about the 174 extremizers

Define U as the sum of the unused capacities 2(s-1)-b(B). Define O as the
number of repeated-class obstructions beyond the first obstruction in each
matching. Both are nonnegative integers in an avoiding coloring. At seven
colors, double counting gives **U+O=1**.

| Type | Number of fixed-edge partitions | Meaning |
|---|---:|---|
| U=1, O=0 | 150 | Exactly one unit of unused capacity; every matching is obstructed by exactly one color class |
| U=0, O=1 | 24 | All classes attain their bounds; one matching is obstructed by two classes and all others by one |

The 24 partitions in the second row are exactly **class 7** of the
[symmetry atlas](cube_classification.md). Its exceptional matching has color
multiplicities (2,2), so it repeats two different colors. In contrast, a matching
with profile (3,1) or (4) repeats only one color class.

The identity U+O=1 is a proved necessary condition. The population counts and
identification with class 7 are finite computational observations on the full
classified population. The balance summarizes obstruction counts rather than
classifying partitions up to symmetry. Its derivation here assumes avoidance;
the audit separately checks that every matching is obstructed.

## Checks and reproduction

The audit visits all 2^12-1=4,095 nonempty edge subsets and records the histogram
of their obstruction counts by size. It verifies the incidence constants and
the one-class inequality, then creates per-class certificates and checks the
balance on every one of the 174 saved orbit members.

Separate tests use integer bit masks for the full subset audit and color
multiplicity counters for the matching certificates. A fully rainbow coloring
is included as a negative control. Arithmetic is exact; no sampling is used.

The subset audit also computes the sharp maximum obstruction count at each
size. The uniform bound used in the proof need not be sharp for every size:

| Edges in one color class | Computed maximum b(B) | Uniform proof bound 2(s-1) |
|---:|---:|---:|
| 1 | 0 | 0 |
| 2 | 2 | 2 |
| 3 | 3 | 4 |
| 4 | 6 | 6 |
| 5 | 6 | 8 |
| 6 | 9 | 10 |

The middle column is an exhaustive finite observation, not an additional
non-enumerative lemma. For sizes 7 through 12 the computed maximum remains nine.

```sh
python -m experiments.cube_collision_audit --check results/data/cube_collisions.json
python -m unittest discover -s tests -p test_cube_collisions.py -v
```

The proof does not rely on these checks. See the
[execution record](cube_collision_verification.md) for the exact run, bounds,
hashes, and the distinction between proof and finite corroboration.
