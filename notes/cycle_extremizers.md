# Rainbow perfect matchings on even cycles and two disjoint squares

**Akhil Ravuri**

**Abstract.** We determine the maximum number of colors in an edge coloring of
an even cycle that avoids a rainbow perfect matching and count all extremal
partitions of its fixed edge set. We also prove that two disjoint squares admit
at most six colors under the same restriction and characterize their exactly
two extremal partitions. The arguments are elementary and self-contained.

**Status:** elementary exposition; no novelty claim.

[Download the typeset paper](../papers/cycle_extremizers.pdf).
[Edit the LaTeX source](../papers/cycle_extremizers.tex).

We use finite simple graphs and arbitrary edge colorings, which need not be
proper. A perfect matching is **rainbow** if its edges have pairwise distinct
colors. For a graph $G$ admitting an avoiding coloring, write $A(G)$ for the maximum number of colors in a coloring avoiding every
rainbow perfect matching. Write $N_{\mathrm{ext}}(G)$ for the number of such colorings using
$A(G)$ colors, viewed as partitions of the **fixed edge set** into color classes.
Color names are ignored; graph automorphisms are not quotiented out.

## 1. Even cycles

**Theorem 1.** For every integer $n\ge 2$,

$$
A(C_{2n})=2n-2,
\qquad
N_{\mathrm{ext}}(C_{2n})=\binom{n}{2}^{2}.
$$

**Proof.** An even cycle has exactly two perfect matchings $M_1$ and $M_2$: once
the matching edge incident to one vertex is chosen, all subsequent choices
around the cycle are forced. They are the two alternating sets of edges, and
they partition the edge set.

Let $S_i$ be the color palette on $M_i$. In an avoiding coloring, neither matching
is rainbow, so $|S_i|\le n-1$. Consequently,

$$
|S_1\cup S_2|\le |S_1|+|S_2|\le 2n-2.
$$

Conversely, choose one pair of edges in each matching and give that pair one
color. Give every remaining edge its own color, using disjoint palettes in the
two matchings. There are $2n-2$ colors and neither matching is rainbow. This proves
the formula for $A$.

Equality forces $|S_1|=|S_2|=n-1$ and $S_1\cap S_2=\varnothing$. A partition of $n$ edges into $n-1$
nonempty classes has exactly one class of size two and all other classes of
size one: the total excess of class sizes over one is exactly one. Thus each
matching has one repeated pair, and the palettes are disjoint.

There are $\binom{n}{2}$ choices of the repeated pair in each fixed matching.
Each pair of choices specifies one edge partition, and every extremal partition
arises uniquely this way. This proves the formula for $N_{\mathrm{ext}}$. No division by
rotations, reflections, or color permutations is needed. ∎

For $C_4$, $C_6$, $C_8$, and $C_{10}$, the formulas give maximum color counts 2,4,6,8 and
extremal partition counts 1,9,36,100. These are consequences of the proof. The
repository's sparse computation checks $C_4$, $C_6$, and $C_8$; no additional $C_{10}$ run is
claimed by this note.

## 2. Maximum color count on two disjoint squares

**Theorem 2.** Let $G=H_1\sqcup H_2$, where each $H_i$ is a copy of $C_4$. Then

$$
A(G)=6.
$$

**Proof.** Color the cyclically ordered edges of $H_1$ with $A,B,A,B$. Color the
four edges of $H_2$ with four distinct new colors. Every perfect matching of $G$
restricts to one of the two monochromatic perfect matchings of $H_1$, so it is
not rainbow. This uses six colors.

For the upper bound, consider a coloring using at least seven colors on the
eight edges. If all eight colors are distinct, every perfect matching is
rainbow. Otherwise exactly seven colors are used: one pair of edges $e,f$ shares
a color and every other color class is a singleton.

In the component containing $e$, choose the alternating perfect matching that
omits $e$. Combine it with either perfect matching of the other component. The
result is a perfect matching of $G$ omitting $e$, so it cannot contain the only
repeated pair. It is therefore rainbow. An avoiding coloring uses at most six
colors, proving the claim. ∎

## 3. Exactly two extremal partitions

**Theorem 3.** With edge positions fixed and color names ignored,

$$
N_{\mathrm{ext}}(C_4\sqcup C_4)=2.
$$

**Proof.** A six-color partition of eight edges has class sizes $s_1,\ldots,s_6$ with
$\sum_{i=1}^{6}(s_i-1)=2$. The only possible size patterns are

$$
(3,1,1,1,1,1)
\quad\text{or}\quad
(2,2,1,1,1,1).
$$

**The triple case.** There are four global perfect matchings, obtained by
independently choosing one of the two local matchings in each component.
Every edge belongs to exactly two global matchings. If three edges share one
color, their total number of appearances across the four matchings is six.
To obstruct every matching, each would have to contain at least two of these
three edges, requiring at least eight appearances. This is impossible. Some
matching contains at most one of them and is rainbow.

**The two-pair case.** Let $P$ and $Q$ be the two size-two color classes. A matching
is non-rainbow exactly when it contains $P$ or $Q$ in full. The number of global
matchings containing a given pair is:

| Pair position | Global perfect matchings containing both edges |
|---|---:|
| Adjacent edges of one component | 0 |
| Opposite edges of one component | 2 |
| One edge in each component | 1 |

Adjacent edges cannot both occur in a matching. Opposite edges specify one
local matching, which can be combined with either choice in the other component.
An edge in each component specifies both local choices, giving exactly one
global matching.

To obstruct all four matchings, both $P$ and $Q$ must each obstruct two, with their
obstructed sets disjoint. Therefore each pair consists of opposite edges in a
component. If they lie in different components, choose the other local matching
in each component. Their union contains neither pair and is rainbow. Thus $P$ and
$Q$ lie in the same component. Since color classes are disjoint, they must be
precisely that component's two alternating perfect matchings.

There are two choices of this component. Once chosen, its two opposite pairs
are the repeated classes and the other component's four edges are singleton
classes. Conversely, each such partition avoids a rainbow perfect matching.
The two partitions are distinct on the fixed edge set. Interchanging color
names gives no further partitions. Hence $N_{\mathrm{ext}}(G)=2$. ∎

## Verification and interpretation

The proofs above are self-contained. Their dependencies are the two local
matchings of $C_4$, independent component choices, class-size counting, and
double counting of edge appearances. Computation is not a premise.

The [existing sparse dataset](../results/data/sparse_rainbow.json)
agrees with $A(G)=6$ and $N_{\mathrm{ext}}(G)=2$. Its execution and coverage limits are documented
in [the sparse verification record](../results/sparse_verification.md).
