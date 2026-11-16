# An incidence proof of the cube's seven-color bound

An elementary incidence argument proves the seven-color maximum.
The nine-orbit classification remains a separate exhaustive computation.

Let $Q$ be the cube, represented by $K_{4,4}$ minus its diagonal matching. A coloring
is arbitrary, not necessarily proper. Let $A(Q)$ be the largest number of colors
that can occur while every perfect matching has a repeated color.

## Matching incidences

Every edge lies in exactly three perfect matchings. To see this, by simultaneous
permutation of the left and right indices it suffices to fix $L_0R_1$. The remaining
three left vertices can be matched to columns 0,2,3 in 3! ways before excluding
the forbidden pairs $L_2R_2$ and $L_3R_3$. Inclusion-exclusion leaves
$3!-2(2!)+1=3$ completions.

There are twelve edges and every perfect matching has four edges, so double
counting edge-matching incidences gives exactly 12(3)/4 = **nine** matchings.
Two fixed distinct edges lie together in at most two perfect matchings: if they
meet, they lie in none; otherwise only two left and two right vertices remain,
with at most 2! completions.

## How many matchings can one color obstruct?

For a nonempty color class B of size s, let b(B) count perfect matchings using
at least two edges of B. Then

$$b(B)\le 2(s-1).$$

For $s=1$, $b(B)=0$. For $s=2$, the pair bound gives $b(B)\le2$.
For $s=3$, the edges of B have nine total matching appearances, and each obstructed
matching uses at least two of them, so $b(B)\le\lfloor9/2\rfloor=4$.
For $s\ge4$ the same incidence count gives

$$2b(B)\le 3s,\qquad b(B)\le 3s/2\le 2(s-1).$$

## The maximum

**Proposition.** $A(Q)=7$.

**Proof.** Suppose an avoiding coloring has r nonempty color classes
B1,...,Br, of sizes s1,...,sr. Every one of the nine perfect matchings is
obstructed by some class. A matching obstructed by several classes may be
counted more than once, which is harmless for this inequality:

$$9\le\sum_{i=1}^r b(B_i)\le 2\sum_{i=1}^r(s_i-1)=2(12-r).$$

Hence $r\le7$, since $r$ is an integer. Conversely, give all six edges incident to
two fixed left vertices one color and the other six edges distinct fresh
colors. Every perfect matching uses two edges of the common color. This gives
an avoiding seven-coloring. The upper and lower bounds agree. âˆŽ

## A restriction on every extremizer

For an avoiding seven-coloring define the unused capacity

$$U=\sum_i\bigl(2(s_i-1)-b(B_i)\bigr).$$

For each perfect matching M let q(M) count how many color classes repeat in M,
and put O=sum_M(q(M)-1). Because the coloring avoids rainbow matchings,
 $q(M)\ge1$. All summands in U and O are nonnegative integers. Counting the
incidences (color class, obstructed matching) in two ways gives

$$U+O=2(12-7)-9=1.$$

Therefore every extremizer has exactly one of two behaviors:

- U=1, O=0: one color class misses its capacity bound by one; every matching
  has exactly one repeated color class.
- U=0, O=1: every color class attains its capacity bound; exactly one matching
  has two repeated color classes and all other matchings have one.

This is a necessary structural condition, not a sufficient classification rule.
The [collision audit](../results/cube_collisions.md) evaluates it on all 174
recorded extremizers and checks the one-class inequality on all 4,095 nonempty
edge subsets. The proof above uses no enumeration as a premise.
