# Rainbow Perfect Matchings in Small Complete Bipartite Graphs

**Status:** exhaustive computational small-case result; no novelty claim.

**Literature check, 2026-11-13:** these values reproduce Li–Tu–Jin,
Theorems 2.3 and 2.5, after translating their forcing threshold rb to A=rb−1.
See [the checked comparison](../notes/literature/young_and_matchings.md).

The experiment enumerates every edge-color equality pattern of $K_{n,n}$
up to relabeling of colors and asks whether the coloring contains a
rainbow perfect matching.

## Results

| graph | edge-color patterns checked | largest number of colors avoiding a rainbow perfect matching |
|---|---:|---:|
| $K_{2,2}$ | 15 | 2 |
| $K_{3,3}$ | 21,147 | 4 |

Thus the computation gives

$$
A(K_{2,2})=2
$$

and

$$
A(K_{3,3})=4
$$

for the local notation defined in `notes/rainbow_matchings.md`.

## One extremal coloring of $K_{2,2}$

Using the matrix entry in row $i$, column $j$ for the color of edge $(i,j)$:

```text
0 1
1 0
```

Both perfect matchings are monochromatic, so neither is rainbow.

## One extremal coloring of $K_{3,3}$

One four-color pattern found by the exhaustive search is

```text
0 0 0
0 0 0
1 2 3
```

Every perfect matching uses two edges from the first two rows, and those
two edges both have color 0. Therefore no perfect matching is rainbow.

## Search-space reduction

There are many ordinary assignments of named colors to nine edges.
However, the rainbow property is invariant under renaming colors.

So the program searches set partitions of the nine edges instead.
The number of such partitions is the Bell number

$$
B_9=21{,}147,
$$

which makes exhaustive verification of $K_{3,3}$ practical.

## Interpretation

The purpose of this experiment is to validate the rainbow-matching
detector and establish exact small cases before investigating larger graph
families.

No statement here is being claimed as a new theorem.

## Extremal classification

The 87 extremal four-color patterns of $K_{3,3}$ fall into
[four symmetry classes](k33_classification.md) under row and column permutations,
transpose, and color renaming.
