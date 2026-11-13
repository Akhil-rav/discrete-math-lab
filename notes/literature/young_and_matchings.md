# Young's matching papers and the existing experiments

**Status:** literature-derived facts and a reproduction of known small cases.
Source versions and access limits are in the [source records](source_records.md).

## A convention dictionary

For a host G and matching target kK2, write

$$
f(G,kK_2)=\max\{|c(E(G))|:c\text{ avoids a rainbow }kK_2\}.
$$

An exact r-coloring uses every one of its r colors. In the feasible cases here,
the minimum forcing number is f+1: an avoiding coloring can be merged to use
any smaller positive number of colors, while merging cannot create a rainbow
copy. In our original perfect-matching notes, A(G)=f(G,nK2) for a 2n-vertex host.

Li–Tu–Jin call the forcing threshold rb. Haas–Young and Özkahya–Young use a
minimum forcing anti-Ramsey convention. Other papers use “anti-Ramsey number”
for f. Always check the definition before comparing a numeric answer.

## Known bipartite result: LTJ09

For m≥n≥k≥3, Theorem 2.5 of
[LTJ09](https://arxiv.org/pdf/math/0610910v1) gives

$$
rb(K_{m,n},kK_2)=m(k-2)+2.
$$

Thus A(Knn)=n(n−2)+1 for n≥3. The case n=2 is exceptional:
Theorem 2.3 gives rb(K22,2K2)=3, hence A(K22)=2.
The repository's values 2 and 4 are therefore **reproductions**, not conjectures.

For the lower bound when n≥3, give all edges incident to n−2 left vertices
distinct colors, and color all remaining edges with one fresh color.
Every perfect matching uses two edges in that last color. This supplies
n(n−2)+1 colors; the cited theorem supplies the upper bound.

## Direct connections to Michael Young

[Haas–Young (2012)](https://doi.org/10.1016/j.disc.2011.10.017) studies perfect
matchings in a **complete graph**, not a complete bipartite graph. Its bibliographic
record and subject were checked, but its exact theorem formula was not extracted
reliably. No complete-graph formula is imported into this lab.

[Özkahya–Young (2013)](https://web.cs.hacettepe.edu.tr/~ozkahya/pub/AR-hyperg.pdf)
extends matching questions to complete uniform hypergraphs and relates their
forcing thresholds to extremal matching-free edge counts. Proposition 1's
construction is recorded in the source notes. A historical conjecture in that
paper is not automatically a currently open problem.

[De Silva et al. (2018)](https://arxiv.org/abs/1801.00474v2), with Young, studies
anti-Ramsey multiplicity: optimizing the number/proportion of rainbow copies
with a fixed palette. That is a separate objective from avoiding every rainbow
perfect matching. It is included as a reading direction, not an implemented result.

## Bounded next tasks, without novelty claims

- Extend the finite orbit classification to a specified small sparse host with
  a proved search-space bound and an explicit automorphism group.
- Study a published extremal-coloring classification before proposing a general
  structural statement. The K33 orbit list alone supplies no general classification.
- Reproduce a small complete-graph matching case only after extracting HY12's
  precise conventions and exceptions from primary full text.

These are repository development tasks, not claims of open mathematical problems.
