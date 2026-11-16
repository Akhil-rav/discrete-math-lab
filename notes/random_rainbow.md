# Counting rainbow-matching probabilities exactly

These elementary counting identities connect avoiding partitions with exact
random-coloring probabilities.

All graphs are finite, and colors on different edges are independent and
uniform on the labeled palette $\{1,\ldots,q\}$, where $q$ is a positive integer.
Colorings are arbitrary and may leave palette colors unused.

## Partition weighting

For a graph with $m\ge1$ edges, let $a_k$ be the number of partitions of its fixed
edge set into $k$ blocks that avoid every rainbow perfect matching. Every
assignment of labeled edge colors has a unique partition into equal-color
blocks. A fixed $k$-block partition can receive distinct labels from $q$ colors
in exactly

$$ (q)_k=q(q-1)\cdots(q-k+1) $$

ways, with $(q)_0=1$ and $(q)_k=0$ for $k>q$. Since every labeled coloring has
probability $q^{-m}$,

$$
\Pr(\text{no rainbow perfect matching})
=q^{-m}\sum_k a_k(q)_k.
$$

Different blocks must get different labels; otherwise they would form one
block in the resulting partition. This explains why normalized partitions
cannot be averaged uniformly to model independent random edge colors.

## First and second moments

Let the graph have $N\ge1$ perfect matchings, each with $n\ge1$ edges. Define
$I_M$ to be one if matching $M$ is rainbow and zero otherwise, and $X=\sum_M I_M$.
There are $(q)_n$ rainbow assignments among $q^n$ assignments on $M$, so

$$ p=\Pr(I_M=1)=\frac{(q)_n}{q^n},\qquad \mathbb E[X]=Np. $$

Suppose distinct matchings $M$ and $M'$ share $s$ edges. If $q<n$, neither can be
rainbow and their joint probability is zero. Otherwise, condition on $M$
being rainbow. Its shared edges have $s$ distinct colors. The $n-s$ unshared
edges of $M'$ must avoid those $s$ colors and be mutually distinct, leaving
$(q-s)_{n-s}$ assignments out of $q^{n-s}$. They may reuse colors from the
unshared edges of $M$; those colors do not appear on a shared edge. Therefore

$$
\Pr(I_M=I_{M'}=1)
=\frac{(q)_n(q-s)_{n-s}}{q^{2n-s}},\qquad q\ge n.
$$

Expanding the square, using $I_M^2=I_M$, gives

$$
\mathbb E[X^2]=Np+
2\sum_{\{M,M'\}}\Pr(I_M=I_{M'}=1),
$$

where the sum runs over unordered distinct pairs. Overlap zero or one gives
independent rainbow indicators in this model. General overlapping events
must use the joint formula; the whole family need not be mutually independent.

Since $X$ is a nonnegative integer, $\mathbb E[X]\ge\Pr(X>0)$. For the lower bound, let
$u=\Pr(X>0)>0$. Nonnegative conditional variance gives

$$
\mathbb E[X^2]=u\mathbb E[X^2\mid X>0]
\ge u\mathbb E[X\mid X>0]^2
=\frac{\mathbb E[X]^2}{u}.
$$

Rearranging proves

$$
\frac{\mathbb E[X]^2}{\mathbb E[X^2]}
\le\Pr(X>0)\le\min(1,\mathbb E[X]).
$$

If $\mathbb E[X^2]=0$, $X$ is always zero and the probability and both bounds are zero.
No division by zero or claim about independent matching events is needed.

## Even cycles as a check

For $C_{2n}$, $n\ge2$, the two alternating perfect matchings have disjoint edge sets.
Their rainbow events are independent, so with $p=(q)_n/q^n$,

$$\Pr(\text{at least one rainbow matching in }C_{2n})=1-(1-p)^2.$$

This identity is independent of the partition-histogram implementation and
checks the saved probabilities on C4, C6, and C8 for all q=1,...,24.

## Inclusion-exclusion through conflict graphs

There is a second way to count the same event without an avoiding histogram.
Let $\mathcal M$ be the perfect-matching family. For a nonempty subfamily
$F\subseteq\mathcal M$, form a simple graph $H_F$ whose vertex set is the
**entire edge set of the host**. Join two of these positions when they occur
together in some matching in $F$. A proper $q$-coloring of $H_F$ is exactly
an edge coloring making every matching in $F$ rainbow. If $P_H(q)$ is the
chromatic polynomial, inclusion-exclusion gives the counting polynomial

$$
U_G(q)=\sum_{\varnothing\ne F\subseteq\mathcal M}
(-1)^{|F|+1}P_{H_F}(q),\qquad
\Pr(X>0)=\frac{U_G(q)}{q^m}.
$$

To justify the alternating sum directly, a coloring with $x$ rainbow matchings
is counted $\sum_{j=1}^{x}(-1)^{j+1}\binom{x}{j}=1$ times if $x>0$, and zero
times otherwise. Edge positions unused by $F$ remain isolated vertices of
$H_F$, so their free color choices are included. The denominator is always
$q^m$, even when the selected matchings use only part of the host.

The implementation counts proper colorings by **addition and contraction**.
For two nonadjacent vertices $u,v$ of a simple graph $H$,

$$P_H(q)=P_{H+uv}(q)+P_{H/uv}(q).$$

Indeed, proper colorings split into those giving $u,v$ different colors and
those giving them the same color. The first are colorings of $H+uv$; the
second correspond bijectively to colorings after identifying $u,v$ and
removing duplicate edges. Since $u,v$ were nonadjacent, no loop is introduced.
Each step either adds an edge at the same order or reduces the order, so the
recursion terminates. Its complete-graph terminal value is $(q)_{|V(H)|}$,
with $P_{K_0}=1$; disconnected components multiply because their color
choices are independent and may reuse labels. Memoization reuses identical
labeled conflict subproblems. This is an exact counting recurrence, not
sampling or numerical interpolation.

Consequently, both methods give the identity

$$U_G(q)=q^m-\sum_k a_k(q)_k.$$

The experiment checks **every coefficient** of this polynomial equality on
all six hosts. This checks the polynomial identity directly, alongside the
palette-grid comparisons. The new engine uses only the target family; saved partition counts
are loaded solely for the comparison. Its matching lists are independently
recovered from edge subsets and compared with permutation generation.

## Bounds from the first three intersection sums

Put $T_j=\sum_{|F|=j}\Pr(\bigcap_{M\in F}\{M\text{ is rainbow}\})$, with
$T_j=0$ when $j>N$. Then $T_j=\mathbb E\binom{X}{j}$. The usual second- and
third-order Bonferroni bounds are

$$\max(0,T_1-T_2)\le\Pr(X>0)\le\min(1,T_1-T_2+T_3).$$

For completeness, when $x\ge1$ the lower partial sum satisfies
$x-\binom{x}{2}-1=-\binom{x-1}{2}\le0$, and the upper partial sum satisfies
$x-\binom{x}{2}+\binom{x}{3}-1=\binom{x-1}{3}\ge0$. For $x=0$, both are
zero. Taking expectations proves the bounds; no independence assumption is
used. Also $T_1=\mathbb E[X]$ and $2T_2=\mathbb E[X^2]-\mathbb E[X]$,
which supply checks against the earlier matching-overlap formulas.

On the cube at $q=4$, the computation gives
$T_1=27/32$, $T_2=45/128$, and $T_3=3/32$, hence

$$\frac{63}{128}\le\frac{4653}{8192}\le\frac{75}{128}.$$

These are finite applications of standard counting identities. The engine
is limited to twelve edge positions and nine targets, and is not a general
polynomial-time algorithm. The [method comparison](../results/inclusion_exclusion.md)
records its exact checks and separate machine-dependent timings.

## Large palettes

Assume an avoiding coloring exists, and let $A=\max\{k:a_k>0\}$. Each $(q)_k$ is
monic of degree $k$. Thus the avoidance polynomial has leading term $a_Aq^A$,
and the exact identity above implies

$$ q^{m-A}\Pr(\text{no rainbow perfect matching})\longrightarrow a_A $$

as $q$ tends to infinity through the positive integers. If $A=m$, this limit
still holds; no decay is implied in that case. For the fixed cube, $A=7$ is
proved by [matching incidence counts](cube_upper_bound.md) and $a_7=174$ is
established by the exhaustive [classification](../results/cube_classification.md).
The resulting limit is 174 after multiplying the avoidance probability by $q^5$.
Its numerical constant depends on that finite count; the limiting argument
does not assert new graph-theoretic thresholds or literature novelty.

[Project report and plot](../projects/random-colorings/report.md)
