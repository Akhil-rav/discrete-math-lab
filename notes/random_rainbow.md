# Counting rainbow-matching probabilities exactly

**Status:** elementary identities with finite applications. No novelty claim.

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
