# Weighted covers and ladder matchings

The ladder family has the elementary maximum-color formula

$$A(P_k\square K_2)=3k-5\qquad(k\ge3).$$

The [proof](../notes/matching_covers.md) uses a local construction and
the tiling description of perfect matchings. The square has maximum two.
A separate weighted-cover method supplies finite optimum certificates,
and the five-column study classifies every ten-color extremizer.

[Nine-page LaTeX report](../papers/matching_foundations.pdf) ·
[LaTeX source](../papers/matching_foundations.tex) ·
[Complete data](data/matching_covers.json) ·
[Verification](matching_cover_verification.md)

## The covering method

A block $B$ costs $|B|-1$ and covers the perfect matchings meeting it at
least twice. The least cover cost equals the minimum color deficit.
Intersecting blocks can be merged without increasing cost or losing coverage;
the remaining positions become singleton color classes.

The algorithm keeps the cheapest block for each coverage mask and computes
the least remaining cost for every covered-target state. The saved certificates
include those tables and an attaining coloring. A separate checker reconstructs
all blocks using combinations and verifies every state and witness.

| Host | Edges | Matchings | Minimum deficit | Maximum colors | Coverage masks | Cost states |
|---|---:|---:|---:|---:|---:|---:|
| C4 | 4 | 2 | 2 | 2 | 3 | 4 |
| C6 | 6 | 2 | 2 | 4 | 3 | 4 |
| C8 | 8 | 2 | 2 | 6 | 3 | 4 |
| 2C4 | 8 | 4 | 2 | 6 | 13 | 16 |
| K33 | 9 | 6 | 5 | 4 | 49 | 64 |
| cube | 12 | 9 | 5 | 7 | 275 | 512 |
| L3 | 7 | 3 | 3 | 4 | 7 | 8 |
| L4 | 10 | 5 | 3 | 7 | 27 | 32 |
| L5 | 13 | 8 | 3 | 10 | 139 | 256 |

Eight rows reproduce maxima from the older partition searches. L5 extends
the host range to thirteen edges. The new solver is limited to thirteen
positions and nine targets; the original partition solver still stops at twelve
edges. The method is exponential and is not presented as a scalable graph library.

## All five-column extremizers

L5 has thirteen edges and eight perfect matchings. Deficit-three enumeration
finds 15 extremizers, forming the following six symmetry classes.

| Representative | Orbit | Stabilizer |
|---|---:|---:|
| `0012340564789` | 4 | 1 |
| `0012345674589` | 2 | 2 |
| `0123004506789` | 2 | 2 |
| `0123004567890` | 2 | 2 |
| `0123004567896` | 4 | 1 |
| `0123045674897` | 1 | 4 |

Edges are ordered by rungs, top rail, then bottom rail, with columns
starting at zero. Color names are normalized by first appearance.
The four graph automorphisms exchange the rails and reverse column order.
Every orbit stays inside the saved extremal population. The orbits are
pairwise disjoint, and their sizes sum to 15.

There are four quadruple-class patterns, eight triple-and-pair patterns,
and three patterns with three pairs; all remaining classes are singletons.
The cover optimizer does not claim to enumerate these. A separate partition
iterator finds them, and a block-shape enumerator independently recovers them.

| Deficit | Partitions visited | Avoiding |
|---|---:|---:|
| 0 | 1 | 0 |
| 1 | 78 | 0 |
| 2 | 2,431 | 0 |
| 3 | 39,325 | 15 |

The 41,835 candidates cover every partition of deficit at most three.
This is not a full enumeration of all $B_{13}$ partitions. The general
bound has a written proof and the cover tables give another finite
certificate of the optimum.

## Reproduce

```sh
python -m experiments.matching_covers --check results/data/matching_covers.json
python -m unittest tests.test_matching_covers -v
```

Python 3.11+ and the standard library are sufficient. The
[source comparison](../notes/literature/ladders.md) records the limited
literature search. The elementary formula and cover reduction are proved
here without asserting that they are new. Probabilities for the
[first three ladders](ladder_matchings.md) remain a separate computation;
no L5 probability result is included.
