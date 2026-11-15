# A direct count of the fifteen five-column extremizers

Use the ladder $L_5=P_5\square K_2$, with columns numbered $0,\ldots,4$.
The rung in column $i$ is $r_i$, and
$H_i=\{t_i,b_i\}$ is the pair of rail edges across gap $i$.
Edge positions are ordered by rungs, top rail, then bottom rail.
Colors are arbitrary; edges remain fixed, and color names are ignored.

The [ladder bound](matching_covers.md) gives $A(L_5)=10$. Thus an extremal
partition has deficit $13-10=3$. Its nonsingleton classes have sizes
four, three and two, or two and two and two. All other classes are singletons.

**Theorem.** There are exactly fifteen extremal partitions: four with a
quadruple, eight with a triple and a pair, and three with three pairs.
They form six classes under graph automorphisms and color renaming.

## The eight perfect matchings

A perfect matching is specified by its nonadjacent horizontal gaps. Let
$A$ denote the all-rung matching, $S_i$ the matching using $H_i$, and
$D_{ij}$ the matching using $H_i,H_j$. These are all eight possibilities:

| Matching | Rungs | Rail pairs |
|---|---|---|
| $A$ | $r_0,r_1,r_2,r_3,r_4$ | none |
| $S_0$ | $r_2,r_3,r_4$ | $H_0$ |
| $S_1$ | $r_0,r_3,r_4$ | $H_1$ |
| $S_2$ | $r_0,r_1,r_4$ | $H_2$ |
| $S_3$ | $r_0,r_1,r_2$ | $H_3$ |
| $D_{02}$ | $r_4$ | $H_0,H_2$ |
| $D_{03}$ | $r_2$ | $H_0,H_3$ |
| $D_{13}$ | $r_0$ | $H_1,H_3$ |

To see completeness, the horizontal gaps are precisely the independent
subsets of the four-gap path: the empty set, four single gaps, and
$\{0,2\},\{0,3\},\{1,3\}$. The two matchings $D_{02}$ and $D_{13}$
are disjoint as edge sets. A class *blocks* a matching when they share at
least two edges.

## One quadruple: four partitions

Let $Q$ be the repeated class. Blocking the disjoint matchings $D_{02}$
and $D_{13}$ requires exactly two of its four edges in each. Blocking
$A$ requires at least two rungs. The only rungs in those two disjoint
matchings are $r_4$ and $r_0$, so

$$Q=\{r_0,r_4,x,y\},\qquad x\in H_0\cup H_2,\quad y\in H_1\cup H_3.$$

The matching $D_{03}$ contains neither end rung. Therefore both $x,y$
must lie in it, forcing $x\in H_0$ and $y\in H_3$. Conversely, every
such quadruple blocks all eight matchings in the table. There are
$2\cdot2=4$ choices.

## A triple and a pair: eight partitions

Any fixed pair belongs to at most three matchings. Indeed, two rails in
different gaps occur together only in their unique two-gap matching.
A rung and a rail occur together at most twice: for an end gap, the
three matchings containing it have no common rung; an interior gap
occurs only twice. A whole rail pair occurs at most three times.
For two rungs, the all-rung matching contributes one. Their columns are
incident to at least two of the four gaps, so at most two single-gap
matchings can retain both.

Consequently a triple $T$ must block at least five matchings.

If $T$ has at most one rung, it misses $A$. It blocks at most two
single-gap matchings: with one rung it has only two rails; with no
rung it needs a complete rail pair for each such matching. It blocks
at most two double-gap matchings, since it cannot meet both disjoint
sets $D_{02},D_{13}$ twice. Thus this case blocks at most four.

If $T$ has three rungs, it blocks no double-gap matching. Blocking five
matchings requires blocking $A$ and all four $S_i$. The three chosen
rung columns must contain no adjacent pair, or the corresponding $S_i$
would retain at most one. The only three-element independent subset of
the five-column path is $\{0,2,4\}$. But the remaining double-gap
matchings have empty intersection, so no pair can block them all.

It remains to consider $T=\{r_a,r_b,x\}$ with $x\in H_j$.
The following table gives the number of matchings blocked. Both edges
of $H_j$ have identical matching incidences, so the entry is independent
of the rail choice. Column reversal sends $(a,b,j)$ to
$(4-b,4-a,3-j)$ and supplies the four omitted rung pairs.

| Rung columns $(a,b)$ | $j=0$ | $j=1$ | $j=2$ | $j=3$ |
|---|---:|---:|---:|---:|
| $(0,1)$ | 3 | 5 | 3 | 4 |
| $(0,2)$ | 4 | 4 | 3 | 4 |
| $(0,3)$ | 3 | 3 | 3 | 4 |
| $(0,4)$ | 5 | 4 | 4 | 5 |
| $(1,2)$ | 4 | 2 | 3 | 3 |
| $(1,3)$ | 2 | 2 | 2 | 2 |

Each entry follows by intersecting the triple with the eight displayed
matchings. For example, $\{r_0,r_1,t_1\}$ blocks exactly
$A,S_1,S_2,S_3,D_{13}$. Only four forms reach five:

| Triple | Choice | Forced pair |
|---|---|---|
| $\{r_0,r_1,x\}$ | $x\in H_1$ | $H_0$ |
| $\{r_3,r_4,x\}$ | $x\in H_2$ | $H_3$ |
| $\{r_0,r_4,x\}$ | $x\in H_0$ | $H_3$ |
| $\{r_0,r_4,x\}$ | $x\in H_3$ | $H_0$ |

In the first and fourth rows the unblocked matchings are
$S_0,D_{02},D_{03}$, whose intersection is exactly $H_0$.
In the other rows they are $S_3,D_{03},D_{13}$, whose intersection
is exactly $H_3$. The forced pair is disjoint from the triple and
blocks every remaining matching. Four forms, each with two rail choices,
give eight distinct partitions.

## Three pairs: three partitions

Because each pair blocks at most three matchings, a cover of all eight
needs at least two pairs that block three. Exactly five pairs do so:

$$
U=\{r_0,r_1\},\quad V=\{r_0,r_4\},\quad
W=\{r_3,r_4\},\quad X=H_0,\quad Y=H_3.
$$

For the rung pairs, retaining both rungs means avoiding every gap incident
to either column. Exactly $U,V,W$ leave two permissible gaps; each
therefore occurs in $A$ and two single-gap matchings. Among rail pairs,
only the end gaps occur three times. The rung–rail and different-gap
cases have already been bounded by two and one.

Choose two of the five three-blocking pairs, denoted $P,Q$.
They must be disjoint as color classes. The third pair must lie in

$$
K(P,Q)=
\left(\bigcap_{\substack{M:\ P\nsubseteq M\\Q\nsubseteq M}}M\right)
\setminus(P\cup Q).
$$

The eight possible disjoint choices give the following intersections:

| $P,Q$ | $K(P,Q)$ |
|---|---|
| $U,W$ | empty |
| $U,X$ | $H_1$ |
| $U,Y$ | $\{r_4\}$ |
| $V,X$ | $H_3$ |
| $V,Y$ | $H_0$ |
| $W,X$ | $\{r_0\}$ |
| $W,Y$ | $H_2$ |
| $X,Y$ | $V$ |

Thus the only three-pair families are

$$
\{U,H_0,H_1\},\qquad
\{V,H_0,H_3\},\qquad
\{W,H_2,H_3\}.
$$

The middle family appears from three choices of $P,Q$ and is counted
only once. Each listed family consists of disjoint pairs and blocks
every matching. This proves the count $4+8+3=15$.

## Why there are six symmetry classes

The full automorphism group has order four, generated by rail exchange
$\sigma$ and column reversal $\rho$. To prove there are no others,
observe that an automorphism sends a degree-two corner to one of four
corners. Once its image is chosen, its degree-two and degree-three
neighbors have forced images. Continuing along the rails forces every
vertex. The four geometric maps realize all four corner choices.

The quadruples have two orbits of size two, according as their selected
end rails are on the same or opposite rails. The first two triple-and-pair
rows form one orbit of size four; the last two form another.
For the three-pair families, $\sigma$ fixes each, while $\rho$ exchanges
the first and third and fixes the middle. They give orbits of sizes
two and one.

In the saved representative order, the orbit sizes are therefore
$4,2,2,2,4,1$, with stabilizers $1,2,2,2,1,4$.
This proves the count and the six-class structure without a coloring
search. The [saved computation](../results/data/matching_covers.json)
remains an independent finite check, and the
[construction code](../src/l5_extremizers.py) lists the proved families.
The [literature note](literature/ladders.md) records the source scope;
no novelty claim is made.
