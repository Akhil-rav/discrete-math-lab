# Rainbow-perfect-matching avoidance on cycles and two disjoint squares

**Status:** elementary exposition; no novelty claim.

We use finite simple graphs and arbitrary edge colorings, which need not be
proper. A perfect matching is **rainbow** if its edges have pairwise distinct
colors. Write A(G) for the maximum number of colors in a coloring avoiding every
rainbow perfect matching. Write N_ext(G) for the number of such colorings using
A(G) colors, viewed as partitions of the **fixed edge set** into color classes.
Color names are ignored; graph automorphisms are not quotiented out.

## 1. Even cycles

For every integer n≥2,

$$
A(C_{2n})=2n-2,
\qquad
N_{\mathrm{ext}}(C_{2n})=\binom{n}{2}^{\!2}.
$$

**Proof.** An even cycle has exactly two perfect matchings M1 and M2: once
the matching edge incident to one vertex is chosen, all subsequent choices
around the cycle are forced. They are the two alternating sets of edges, and
they partition the edge set.

Let Si be the color palette on Mi. In an avoiding coloring, neither matching
is rainbow, so |Si|≤n−1. Consequently,

$$
|S_1\cup S_2|\le |S_1|+|S_2|\le 2n-2.
$$

Conversely, choose one pair of edges in each matching and give that pair one
color. Give every remaining edge its own color, using disjoint palettes in the
two matchings. There are 2n−2 colors and neither matching is rainbow. This proves
the formula for A.

Equality forces |S1|=|S2|=n−1 and S1∩S2 empty. A partition of n edges into n−1
nonempty classes has exactly one class of size two and all other classes of
size one: the total excess of class sizes over one is exactly one. Thus each
matching has one repeated pair, and the palettes are disjoint.

There are binomial(n,2) choices of the repeated pair in each fixed matching.
Each pair of choices specifies one edge partition, and every extremal partition
arises uniquely this way. This proves the formula for N_ext. No division by
rotations, reflections, or color permutations is needed. ∎

For C4, C6, C8, and C10, the formulas give maximum color counts 2,4,6,8 and
extremal partition counts 1,9,36,100. These are consequences of the proof. The
repository's sparse computation checks C4, C6, and C8; no additional C10 run is
claimed by this note.

## 2. Maximum color count on two disjoint squares

Let G=H1⊔H2, where each Hi is a copy of C4. Then

$$
A(G)=6.
$$

**Proof.** Color the cyclically ordered edges of H1 with A,B,A,B. Color the
four edges of H2 with four distinct new colors. Every perfect matching of G
restricts to one of the two monochromatic perfect matchings of H1, so it is
not rainbow. This uses six colors.

For the upper bound, consider a coloring using at least seven colors on the
eight edges. If all eight colors are distinct, every perfect matching is
rainbow. Otherwise exactly seven colors are used: one pair of edges e,f shares
a color and every other color class is a singleton.

In the component containing e, choose the alternating perfect matching that
omits e. Combine it with either perfect matching of the other component. The
result is a perfect matching of G omitting e, so it cannot contain the only
repeated pair. It is therefore rainbow. An avoiding coloring uses at most six
colors, proving the claim. ∎

## 3. Exactly two extremal partitions

With edge positions fixed and color names ignored,

$$
N_{\mathrm{ext}}(C_4\sqcup C_4)=2.
$$

**Proof.** A six-color partition of eight edges has class sizes s1,…,s6 with
sum(si−1)=2. The only possible size patterns are

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

**The two-pair case.** Let P and Q be the two size-two color classes. A matching
is non-rainbow exactly when it contains P or Q in full. The number of global
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

To obstruct all four matchings, both P and Q must each obstruct two, with their
obstructed sets disjoint. Therefore each pair consists of opposite edges in a
component. If they lie in different components, choose the other local matching
in each component. Their union contains neither pair and is rainbow. Thus P and
Q lie in the same component. Since color classes are disjoint, they must be
precisely that component's two alternating perfect matchings.

There are two choices of this component. Once chosen, its two opposite pairs
are the repeated classes and the other component's four edges are singleton
classes. Conversely, each such partition avoids a rainbow perfect matching.
The two partitions are distinct on the fixed edge set. Interchanging color
names gives no further partitions. Hence N_ext(G)=2. ∎

## Verification and interpretation

The proofs above are self-contained. Their dependencies are the two local
matchings of C4, independent component choices, class-size counting, and
double counting of edge appearances. Computation is not a premise.

The [existing sparse dataset](../results/data/sparse_rainbow.json) independently
agrees with A(G)=6 and N_ext(G)=2. Its execution and coverage limits are documented
in [the sparse verification record](../results/sparse_verification.md).

**Review, November 13, 2026:** the submitted logical arguments were checked for
the n=2 boundary case, upper and lower bounds, equality conditions, uniqueness
of partitions, and the different-component alternative in the two-pair case.
Verdict: proved under the stated fixed-edge, color-renaming convention. This
records a logical review, not external refereeing. Only the repository's
documented computations are used as computational evidence. No literature
novelty determination was made.
