# Rainbow perfect matchings on small ladders

Let $L_k=P_k\square K_2$, with $k$ columns. The first three ladders connect
the cycle and sparse-host studies through a small graph family. The maximum
color counts below have [elementary incidence proofs](../notes/ladders.md).
The extremizer populations and symmetry classes are complete finite computations.

[LaTeX report](../papers/matching_foundations.pdf) ·
[LaTeX source](../papers/matching_foundations.tex) ·
[All data and extremizers](data/ladder_matchings.json) ·
[Verification and run](ladder_verification.md)

| Host | Edges | Perfect matchings | All partitions visited | $A(G)$ | Extremizers | Symmetry classes |
|---|---:|---:|---:|---:|---:|---:|
| L2 | 4 | 2 | 15 | 2 | 1 | 1 |
| L3 | 7 | 3 | 877 | 4 | 27 | 9 |
| L4 | 10 | 5 | 115,975 | 7 | 25 | 9 |

Edges remain fixed when counting partitions; only color names are ignored.
The symmetry quotient is a separate step. The $L_2$ square has eight
automorphisms, while $L_3$ and $L_4$ each have four.

## Complete symmetry lists

Number columns from zero. Rungs come first, then top rail edges, then bottom
rail edges. Each representative lists the colors in that order. Relabel colors
by first appearance after an automorphism; the least resulting string is used.

| Host | Representative | Orbit | Stabilizer |
|---|---|---:|---:|
| L2 | `0011` | 1 | 8 |
| L3 | `0011023` | 4 | 1 |
| L3 | `0011230` | 4 | 1 |
| L3 | `0011232` | 4 | 1 |
| L3 | `0012023` | 4 | 1 |
| L3 | `0012323` | 2 | 2 |
| L3 | `0100023` | 2 | 2 |
| L3 | `0100230` | 2 | 2 |
| L3 | `0100232` | 4 | 1 |
| L3 | `0102323` | 1 | 4 |
| L4 | `0010234256` | 2 | 2 |
| L4 | `0012304356` | 4 | 1 |
| L4 | `0012324356` | 4 | 1 |
| L4 | `0012345346` | 2 | 2 |
| L4 | `0120030456` | 2 | 2 |
| L4 | `0120034560` | 2 | 2 |
| L4 | `0120034564` | 4 | 1 |
| L4 | `0120234564` | 4 | 1 |
| L4 | `0120345365` | 1 | 4 |

The nine orbit sizes sum to 27 for $L_3$ and 25 for $L_4$. Every orbit
is disjoint from the others and contained in the extremal population; together
they cover it. The saved data also retains every fixed-edge extremizer.

Both larger ladders have color deficit three. Grouped by their nonsingleton
color-class sizes, the extremizers split as follows:

| Host | One quadruple | A triple and a pair | Three pairs |
|---|---:|---:|---:|
| L3 | 4 | 16 | 7 |
| L4 | 4 | 10 | 11 |

## Two exact probability computations

Every edge independently receives one of $q$ available labeled colors, uniformly.
Colors need not all appear. The partition method weights each avoiding
$j$-block partition by $(q)_j$. Independently, matching-event inclusion–exclusion
uses proper-coloring polynomials of conflict graphs. The two methods agree
coefficient by coefficient, as well as on all 72 probability rows for $q=1,\ldots,24$.

| Host | Nonempty event subfamilies | Probability with four labels |
|---|---:|---:|
| L2 | 3 | 15/16 |
| L3 | 7 | 387/512 |
| L4 | 31 | 12357/32768 |

The count polynomials and all intersection sums are saved in the dataset;
coefficients are listed in ascending powers of $q$. No timings or speedup
claim are inferred from the event-subfamily counts. The
[six-host benchmark](inclusion_exclusion.md) explains why chromatic subproblems
also matter when comparing the methods.

The extremal counts control the leading avoidance tails:
$q^3(1-P_3(q))\to27$ and $q^3(1-P_4(q))\to25$.
This follows from the leading coefficient of the highest-degree falling
factorial term, rather than from a numerical fit.

## Reproduce

```sh
python -m experiments.ladder_matchings --check results/data/ladder_matchings.json
python -m unittest tests.test_ladders -v
```

These commands use Python 3.11+ and the standard library. The
[source comparison](../notes/literature/ladders.md) records nearby literature
and access limits. These three-host computations are complemented by the
[general ladder proof and five-column classification](matching_covers.md).
The family formula has a separate written proof; the searches alone do not
establish it.
