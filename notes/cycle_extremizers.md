# Rainbow perfect matchings on disjoint unions of even cycles

**Akhil Ravuri**

**Abstract.** For every nonempty disjoint union of even cycles, we determine
the maximum number of colors avoiding a rainbow perfect matching and classify
every extremal partition of the fixed edge set. The cycle and two-square cases
introduce the general argument. The proofs are elementary and self-contained.

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
original sparse computation checks $C_4$, $C_6$, and $C_8$. The cycle-union
experiment below additionally checks $C_{10}$ and disconnected hosts.

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

## 4. Arbitrary disjoint unions of even cycles

**Theorem 4.** Let

$$G=\bigsqcup_{i=1}^{r}C_{2n_i},\qquad r\ge1,\quad n_i\ge2,$$

where $r,n_1,\ldots,n_r$ are integers, with fixed components and edge
positions. Put $m=2\sum_i n_i$. Then

$$
A(G)=m-2,\qquad
N_{\mathrm{ext}}(G)=\sum_{i=1}^{r}\binom{n_i}{2}^{2}.
$$

Every extremal partition has exactly two doubleton color classes. They lie
in a single component, with one pair inside each of that component's two
alternating perfect matchings. All remaining edges are singleton classes.

**Proof of the maximum.** Choose any component. In each of its alternating
matchings, merge one pair of edges into a color class; make every other edge
of $G$ a singleton class. There are $m-2$ classes. Every global perfect
matching chooses one of the two local matchings in that component and hence
contains one repeated pair. Thus $A(G)\ge m-2$.

With $m$ colors every edge has its own color. With $m-1$ colors there is
exactly one repeated pair, say $\{e,f\}$. Choose the alternating local
matching omitting $e$ in its component and any local matching in each other
component. Their union omits $e$ and cannot contain the only repeated pair,
so it is rainbow. Therefore $A(G)\le m-2$.

**Proof of the classification.** In a partition into $m-2$ classes, the total
excess $\sum_B(|B|-1)$ is two. Its nonsingleton classes are therefore either
one triple or two disjoint pairs.

There are $2^r$ global perfect matchings, from independent alternating choices
in each component. Every edge appears in exactly $2^{r-1}$ of them. If a
triple were the only nonsingleton class, its total appearances across the
global matchings would be $3\cdot2^{r-1}$. Obstructing every matching would
require at least $2\cdot2^r$ appearances, since each would need two edges of
that triple. This is impossible because $3<4$.

Now let $P,Q$ be the two repeated pairs. A pair lies in:

| Pair position | Global perfect matchings containing the pair |
|---|---:|
| One component, one alternating matching | $2^{r-1}$ |
| One component, different alternating matchings | $0$ |
| Two different components (only possible for $r\ge2$) | $2^{r-2}$ |

The first case fixes one local choice. The second demands incompatible local
choices. The third independently fixes two local choices. These exhaust all
pair positions, including nonadjacent edges of opposite parity in a long cycle.

Thus each pair obstructs at most half the global matchings. To cover all
$2^r$, both must attain that bound and their obstructed sets must be disjoint.
Each pair is consequently inside one alternating matching of a component.
If the pairs belonged to different components, choosing the other local
matching in each would omit both pairs and give a rainbow global matching.
If both belonged to the same alternating matching of one component, choosing
the other local matching there would do the same. Hence they must belong to
the two different alternating matchings of one component, as claimed.

**Counting.** In component $i$, each alternating matching has $n_i$ edges, so
there are $\binom{n_i}{2}^2$ choices of the two repeated pairs. The component
and the pair inside each alternating set are uniquely recoverable from the
partition. We therefore sum over components. There is no division by two,
color permutations, or permutations of equal-length components: the edge set
is fixed. Conversely every such choice is avoiding by the lower-bound
construction, completing the proof. ∎

In particular, $r$ fixed disjoint squares have $A(G)=4r-2$ and
$N_{\mathrm{ext}}(G)=r$. For $C_4\sqcup C_6$, the values are eight and ten;
for $C_6\sqcup C_6$, they are ten and eighteen. These are consequences of
the general proof, not new results established by the finite check.

## Verification and interpretation

The proofs are self-contained: their dependencies are the two alternating
matchings of each even cycle, independent component choices, class-size
counting, and double counting of edge appearances. Computation is not a premise.

The [existing sparse dataset](../results/data/sparse_rainbow.json)
agrees with $A(G)=6$ and $N_{\mathrm{ext}}(G)=2$. Its execution and coverage limits are documented
in [the sparse verification record](../results/sparse_verification.md).

The [cycle-union experiment](../experiments/cycle_unions.py) checks ten
specified hosts through twelve edges. Six hosts through ten edges receive
full partition enumeration; all ten receive complete searches in the
$m-2$, $m-1$, and $m$ color bands. The twelve-edge cases do **not** claim
full Bell-number coverage. Matching constraints are independently recovered
from edge subsets. See the [data](../results/data/cycle_unions.json) and
[proof and computation review](../results/cycle_union_verification.md) for
precise coverage, conventions, and self-review limits. No novelty is claimed.
