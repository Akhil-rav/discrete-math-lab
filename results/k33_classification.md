# The 87 extremal K33 patterns: four symmetry classes

**Status:** exhaustive finite classification under the specified equivalence;
no novelty claim or extrapolation to larger hosts.

Run `python -m experiments.classify_k33` from the repository root.
The complete data also appear in [small_cases.json](data/small_cases.json).

First enumerate all B9=21,147 edge partitions, with edges in row-major order.
The maximum avoiding color count is 4, attained by 87 partitions. Color names
were already quotiented out; vertices were still labeled.

We further identify patterns under independent permutations of three rows,
three columns, and exchange of the bipartition classes (matrix transpose).
The graph automorphism group has order 2(3!)²=72. After each transformation,
rename colors in order of first appearance. The lexicographically least resulting
array is the canonical representative. This full group action preserves edges,
perfect matchings, and color equality.

| Class | Representative rows | Color-class sizes | Orbit size | Stabilizer size |
|---|---|---|---:|---:|
| 1 | `000 / 000 / 123` | 1,1,1,6 | 6 | 12 |
| 2 | `001 / 110 / 230` | 1,1,3,4 | 36 | 2 |
| 3 | `001 / 120 / 230` | 1,2,2,4 | 36 | 2 |
| 4 | `001 / 230 / 320` | 1,2,2,4 | 9 | 8 |

The orbit sizes sum to 87. Every transformed pattern is checked to remain in
the enumerated extremal population; each canonical bucket size equals its
explicit orbit size. Orbit size times stabilizer size is 72 in each row.
The last two classes show why the multiset of color-class sizes alone is not
a complete invariant.

The rainbow detector was independently compared with all three-edge subsets
with distinct endpoints. Enumeration coverage was checked against the
Bell/Stirling recurrence. These checks establish the finite classification in
the stated model; they do not establish that it is absent from previous literature.

A(K33)=4 is a known result after translating LTJ09's convention;
see the [literature comparison](../notes/literature/young_and_matchings.md).
