# Color collisions as weighted covers

Let $E$ be a finite set of $m\ge2$ positions and let $\mathcal M$ be a
nonempty family of subsets of $E$, each of size at least two. For a graph,
$E$ is its edge set and $\mathcal M$ can be its perfect matchings.
Let $A(\mathcal M)$ be the maximum number of colors used by a coloring
in which no member of $\mathcal M$ is rainbow.

## From partitions to a covering problem

For each $B\subseteq E$ with $|B|\ge2$, define its cost and coverage by

$$
w(B)=|B|-1,\qquad
\Gamma(B)=\{M\in\mathcal M:|M\cap B|\ge2\}.
$$

Let $\tau$ be the minimum total cost of a collection of blocks whose coverage
sets cover $\mathcal M$. The chosen blocks are allowed to overlap.

**Proposition.** $A(\mathcal M)=m-\tau$.

**Proof.** A coloring is a partition of $E$ into color classes. Its deficit is
$m$ minus the number of colors, or $\sum_B(|B|-1)$. It avoids every rainbow
target exactly when its nonsingleton classes cover $\mathcal M$.
Consequently the minimum deficit of an avoiding coloring is at least $\tau$.

Conversely, start with any covering collection. Whenever two blocks intersect,
replace them by their union. Coverage is preserved, since the union contains
both old blocks. The cost does not increase:

$$
|B\cup C|-1
= (|B|-1)+(|C|-1)-(|B\cap C|-1)
\le (|B|-1)+(|C|-1).
$$

Continue until the blocks are disjoint, and add singleton classes at all
unused positions. The resulting coloring avoids every target and has deficit
at most the original cover cost. Applying this to a minimum cover gives the
opposite inequality. $\square$

Overlaps are therefore harmless for computing the optimum. They cannot simply
be treated as separate color classes: the coloring witness must merge them.
The method computes the optimum and a witness, not all extremizers.

## Cost tables and certificates

Number the $N$ targets and represent a covered subfamily by a bit mask $S$.
For each nonempty coverage mask $T$, retain the least cost $c_T$ of any block
with exactly that coverage. For value computation, another block with the
same mask and greater cost can never help.

Let $F(S)$ be the least additional cost needed to cover all targets. Then

$$
F(\mathrm{full})=0,\qquad
F(S)=\min_{T:\,S\cup T\ne S}\bigl(c_T+F(S\cup T)\bigr).
$$

Every transition adds a target, so the table is evaluated in decreasing mask
order. A complete block $E$ covers every target, ensuring that each state has
a finite continuation. The optimum is $F(0)$.

A certificate stores the cheapest block for each coverage mask, the entire
$F$ table, a covering collection, and its merged coloring. The separate
checker rebuilds all subsets using combinations, verifies the coverage table
and every recurrence, and checks the coloring directly. For a lower-bound
interpretation, each inequality $F(S)\le c_T+F(S\cup T)$ telescopes along
any cover; a covering witness attaining $F(0)$ gives the matching upper bound.

There are at most $2^m$ block masks and $2^N$ cost states. If $C$ distinct
nonempty coverage masks occur, the table uses at most $2^N C$ transitions
after block generation. These are exponential bounds, not a polynomial-time
algorithm. The implementation is deliberately limited to 13 positions and
nine targets. It does not increase the original partition solver's 12-edge
limit.

## The maximum for every ladder

Write $L_k=P_k\square K_2$ for a ladder with $k$ columns, and use the rung
and rail notation from the [small-ladder note](ladders.md).

**Theorem.** For every integer $k\ge3$,

$$
A(L_k)=3k-5.
$$

The exceptional square has $A(L_2)=2$.

**Proof.** Color $\{r_0,r_1,t_1\}$ with one color and $\{t_0,b_0\}$ with
another. Give every other edge its own fresh color. If a matching omits
$r_0$, its first column forces $t_0,b_0$. If it contains $r_0$, the next
column either uses $r_1$ or forces $t_1,b_1$. In either case the matching
contains two edges from one repeated class. The construction has deficit
three, hence $3k-5$ colors.

For the upper bound, identify perfect matchings with tilings of the columns
by a one-column rung or a two-column pair of rail edges. Let $p_j$ count
tilings of $j$ columns, with $p_0=p_1=1$ and
$p_j=p_{j-1}+p_{j-2}$. Concatenating tilings is injective, so
$p_a p_b\le p_{a+b}$ for nonnegative $a,b$; the same holds for any finite
product of such counts.

A fixed edge forces a tile of width one or two. Removing it leaves ladder
segments of total width at most $k-1$, so the edge belongs to at most
$p_{k-1}$ matchings. Two distinct compatible edges force tiles occupying at
least two columns. Their remaining segments have total width at most $k-2$;
thus the pair belongs to at most $p_{k-2}$ matchings. Incompatible pairs
belong to none.

If an avoiding coloring had at least $m-2$ colors, where $m=3k-2$, merge
classes until exactly $m-2$ remain. The nonsingleton classes are either two
pairs or one triple. Two pairs obstruct at most $2p_{k-2}<p_k$ matchings
for $k\ge3$, since $p_{k-1}>p_{k-2}$.

For $k\ge4$, a triple has at most $3p_{k-1}<2p_k$ edge–matching
incidences. The strict inequality follows from
$p_{k-1}=p_{k-2}+p_{k-3}<2p_{k-2}$. Obstructing every matching with
that triple would require at least two incidences per matching, or at least
$2p_k$, a contradiction.

For $k=3$, there are three matchings. Only the two end rungs occur twice;
each other edge occurs once. A triple has at most five incidences, fewer
than the six needed. Thus deficit two is impossible in every case, proving
the upper bound. $\square$

This general proof uses the tiling description and elementary counting.
The weighted-cover algorithm supplies separate finite certificates; it is
not a premise of the theorem.

## The five-column classification

For $L_5$, the theorem gives $A(L_5)=10$. The
[direct counting proof](l5_extremizers.md) now derives all fifteen extremal
partitions and their six symmetry classes. The
[finite report](../results/matching_covers.md) retains the computational check. This enumeration covers every
partition of deficit at most three, not the full Bell number $B_{13}$.
The [source comparison](literature/ladders.md) records the literature limits.
The formula and reduction are presented as self-contained elementary
arguments, with no claim that they are new.
