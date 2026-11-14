# Regular Bipartite Graphs: Small Cases

**Status:** Reproduction of a known theorem.

The script
`experiments/regular_bipartite_matchings.py`
exhaustively generated every labeled $d$-regular bipartite graph with
$n\le 5$ vertices in each part and tested whether a perfect matching exists.

## Output

| $n$ | $d$ | labeled graphs checked | failures |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 |
| 2 | 1 | 2 | 0 |
| 2 | 2 | 1 | 0 |
| 3 | 1 | 6 | 0 |
| 3 | 2 | 6 | 0 |
| 3 | 3 | 1 | 0 |
| 4 | 1 | 24 | 0 |
| 4 | 2 | 90 | 0 |
| 4 | 3 | 24 | 0 |
| 4 | 4 | 1 | 0 |
| 5 | 1 | 120 | 0 |
| 5 | 2 | 2,040 | 0 |
| 5 | 3 | 2,040 | 0 |
| 5 | 4 | 120 | 0 |
| 5 | 5 | 1 | 0 |

**Total:** 4,477 labeled regular bipartite graphs checked; 0 failures.

## Interpretation

This agrees with the standard theorem that every finite
$d$-regular bipartite graph with $d\ge 1$ has a perfect matching.

The computation is not a proof. The proof follows from Hall's Marriage
Theorem and is written in `notes/halls_theorem.md`.

## Related study

The [rainbow-matching project](../projects/rainbow-matchings/report.md) adds edge
colors and studies when perfect matchings can have pairwise distinct colors.
