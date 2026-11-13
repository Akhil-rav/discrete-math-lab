# Rainbow 3-term arithmetic progressions

**Status:** definitions from BE+16/Y16; exhaustive finite reproductions.
See [source records](literature/source_records.md) for versions and access limits.

A nondegenerate 3-term arithmetic progression is a set of three distinct terms
{a,a+d,a+2d}. A rainbow progression has three distinct colors. In an interval
we require d>0; in a finite abelian group we use its group addition and remove
duplicate sets. Reversal does not produce a new set.

The anti-van der Waerden threshold aw(S,3) is the smallest exact number of colors
forcing a rainbow 3-AP. Our search maximizes the number of colors avoiding one,
then adds one. Merging color classes preserves avoidance, which justifies this
translation. If no nondegenerate 3-AP exists, the convention is aw(S,3)=|S|+1.
The last value is a convention beyond the feasible palette size, not an actual
coloring with more than |S| colors.

The interval [n]={1,…,n} is represented by 0,…,n−1; translation preserves APs.
In Zn the progression can wrap around. In products of cyclic groups, all
coordinates are added modulo their individual moduli.

## What the code establishes

`src/arithmetic_progressions.py` enumerates interval and group AP sets.
`experiments/rainbow_progressions.py` checks every set partition of the domain
for intervals and cyclic groups of orders 3 through 9, plus Z2×Z2, Z2×Z4, and
Z2×Z2×Z2. Each search visits the corresponding Bell number of partitions.
This is deliberately small; it is not a fast general threshold algorithm.

The benchmarks come from [Butler et al.](https://arxiv.org/pdf/1404.7232v2),
Theorem 1.1 and cyclic discussion. The product-group definition is aligned with
[Young](https://arxiv.org/pdf/1603.08153v1), §1. We do not implement the general
group formulas or unitary colorings. The returned PDFs have internal-date
discrepancies documented in the source record.

## An elementary check

In G=(Z2)^s, 2d=0 for every d, so a+2d=a. There is no nondegenerate 3-AP.
Consequently aw(G,3)=2^s+1 by the stated convention. This elementary known fact
explains the order-eight example; a cyclic group of order eight behaves differently.
Equal orders alone do not determine the set of progressions.
