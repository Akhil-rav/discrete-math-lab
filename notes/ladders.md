# Rainbow perfect matchings on three small ladders

Let $L_k=P_k\square K_2$, where $P_k$ has $k$ vertices. There are two
rows of vertices and $k$ columns. Write $r_i$ for rung $i$, and $t_i,b_i$
for the top and bottom edges across gap $i$, starting at zero. The edge order is

\[
r_0,\ldots,r_{k-1},t_0,\ldots,t_{k-2},b_0,\ldots,b_{k-2}.
\]

Colorings are arbitrary, not necessarily proper. As elsewhere, $A(G)$ is the
maximum number of colors actually used while avoiding every rainbow perfect
matching. A partition forgets color names but keeps all edge positions fixed.

## Matchings and maximum color counts

Scanning from the first column, a perfect matching takes either the first rung
or both rail edges across the first gap. The remaining graph is a shorter
ladder. Thus the familiar domino-tiling recurrence is $p_k=p_{k-1}+p_{k-2}$,
with $p_0=p_1=1$. In particular, the first three hosts have 2, 3, and 5
perfect matchings. For the two larger hosts, their edge-index sets are

| Host | Complete list of perfect matchings |
|---|---|
| $L_3$ | 012, 046, 235 |
| $L_4$ | 0123, 0169, 0358, 2347, 4679 |

Here a string such as 046 denotes the set of edge positions $\{0,4,6\}$,
not a color pattern.

**Proposition.** $A(L_2)=2$, $A$L_3$=4$, and $A$L_4$=7$.

**Proof.** $L_2=C_4$, whose two alternating matchings must each be
monochromatic. Two colors suffice.

For $L_3$, give a distinct color to each of the pairs

\[
\{r_0,r_1\},\quad \{t_0,b_0\},\quad \{t_1,b_1\},
\]

and a fourth color to $r_2$. The matching list shows that each perfect
matching contains one of these pairs, proving $A$L_3$\ge4$.

For $L_4$, repeat colors on the three disjoint pairs

\[
\{r_0,r_3\},\quad \{t_0,b_0\},\quad \{t_2,b_2\},
\]

using a different color for each pair and four fresh singleton colors.
Every perfect matching in the list contains one of these pairs, so
$A$L_4$\ge7$.

For the upper bounds, write $m=|E(L_k)|$. If an avoiding coloring used at
least $m-2$ colors, merging color classes would yield an avoiding coloring
using exactly $m-2$. Such a partition has either one triple and otherwise
singletons, or two doubletons and otherwise singletons: its color deficit
$\sum_B(|B|-1)$ is two.

In $L_3$, any fixed pair belongs to at most one perfect matching. Two
doubletons therefore obstruct at most two of the three matchings. Each edge
belongs to at most two matchings, and only $r_0,r_2$ attain two. Any triple
has total edge–matching incidence at most $2+2+1=5$. To obstruct all three
matchings, it would need at least two incidences per matching, hence at least
six, a contradiction.

In $L_4$, any fixed pair belongs to at most two perfect matchings. Two
doubletons obstruct at most four of the five. The two end rungs belong to
three matchings each; all other edges belong to at most two. Any triple has
total incidence at most $3+3+2=8<10$, whereas obstructing all five
matchings would require at least ten.

These pair and edge incidence bounds follow directly from the complete
matching lists above. Thus $A$L_3$\le7-3=4$ and $A$L_4$\le10-3=7$,
as required. \(\square\)

The proof uses no exhaustive coloring search. The incidence values are also
checked by the test suite, using the generated matchings.

## Finite classification and probabilities

The [classification report](../results/ladder_matchings.md) records every
symmetry representative, the complete fixed-edge extremal populations, and
the two exact probability computations. The maximum-color proposition above
is proved; the extremizer counts and orbit lists are exhaustive finite
computations. No formula for all ladder lengths is asserted.

The [source comparison](literature/ladders.md) states the literature search's
scope and access limits. Neither the elementary bounds nor these computed
classifications are presented as new research results.
