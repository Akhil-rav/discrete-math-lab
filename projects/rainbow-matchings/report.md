# Exact rainbow-matching avoidance on small bipartite hosts

**Status:** computational study and elementary exposition. Known facts, finite
observations, and future development tasks are separated below. No novelty is
claimed.

[Typeset small-host and matching-foundations report](../../papers/matching_foundations.pdf)
· [LaTeX source](../../papers/matching_foundations.tex)

## Question

Given a fixed bipartite graph G with n vertices in each class and at least one
perfect matching, how many colors can its edges use while avoiding every rainbow
perfect matching? The coloring need not be proper. Define A(G) as that maximum.

The [earlier experiments](../../results/rainbow_knn_small_cases.md) reproduced
A(K22)=2 and A(K33)=4. The [literature comparison](../../notes/literature/young_and_matchings.md)
explains why these are known Li–Tu–Jin results after translating their minimum
forcing threshold. The present extension tests sparse hosts with different
perfect-matching structures, including cycles, disconnected graphs, and a cube.

## Finite observations

| Host | Edges | Perfect matchings | Edge partitions covered | A(G) | Extremal partitions |
|---|---:|---:|---:|---:|---:|
| C4 | 4 | 2 | 15 | 2 | 1 |
| C6 | 6 | 2 | 203 | 4 | 9 |
| C8 | 8 | 2 | 4,140 | 6 | 36 |
| Two disjoint C4s | 8 | 4 | 4,140 | 6 | 2 |
| K33 | 9 | 6 | 21,147 | 4 | 87 |
| Cube, represented as K44 minus the diagonal | 12 | 9 | 4,213,597 | 7 | 174 |

These are exhaustive finite observations in the stated model. Color names are
removed; vertex labels remain fixed. The 174 cube extremizers are **not** 174
isomorphism classes. No statement that these numbers are new is made. The
literature review has not certified their novelty or compared the cube value
against every published regular-bipartite theorem.

[Machine-readable results](../../results/data/sparse_rainbow.json) contain the
edge order, full avoiding histograms, rejected counts, and an extremal witness.

The [cube classification](../../results/cube_classification.md) now partitions
the 174 extremizers into nine classes under all 48 cube automorphisms. It includes
a labeled atlas, every orbit member, explicit stabilizers, and independent
matching and automorphism oracles.

## Elementary known fact: even cycles

For n≥2, A(C2n)=2n−2. This is an elementary calculation, not a new theorem.
An even cycle has exactly two perfect matchings, alternating around the cycle;
they partition its 2n edges. To avoid a rainbow matching, each of these two sets
can contain at most n−1 distinct colors. The total number of colors is therefore
at most 2(n−1). Conversely, in each alternating matching give one pair of edges
a common color and give its other edges distinct colors, using disjoint palettes
between the matchings. This uses 2n−2 colors and neither matching is rainbow.

The extremal partition count is binomial(n,2)²: equality in the upper bound
requires disjoint palettes and exactly one merged pair in each alternating
matching. This gives 1,9,36 for the three tested cycles.

The [complete cycle and disjoint-square proofs](../../notes/cycle_extremizers.md)
also establish A(C4⊔C4)=6 and characterize its exactly two extremal partitions.
For these hosts, the recorded finite values now have an explicit elementary
proof in the repository. The note states its conventions and review scope and
does not claim novelty.
The [typeset version](../../papers/cycle_extremizers.pdf) includes the complete
proofs and a diagram of the six-color construction.

The paper now extends this to every nonempty union G of even cycles C(2n_i),
with n_i>=2: A(G)=|E(G)|-2, and the fixed-edge extremal count is
sum_i binomial(n_i,2)^2. Every extremizer repeats one pair in each alternating
matching of a single component and gives all other edges distinct colors.
The [general proof and review](../../results/cycle_union_verification.md)
separate the universal argument from ten-host finite checks. The original
six-host dataset above remains unchanged.

For the cube, a simple lower-bound witness uses seven colors: color the six
edges incident to two fixed left vertices alike, and give the other six edges
six distinct fresh colors. Every perfect matching uses two edges in the common
color. The [incidence proof](../../notes/cube_upper_bound.md) now supplies the
matching upper bound without search. Its scope is the fixed cube, not an
asserted theorem for all cubic bipartite graphs. The equality analysis and
finite [collision audit](../../results/cube_collisions.md) further explain
the obstruction structure of the 174 extremizers.

## Three small ladders

The [ladder study](../../results/ladder_matchings.md) fixes Lk = Pk square K2
for k=2,3,4. Elementary incidence proofs give A(L2)=2, A(L3)=4, A(L4)=7.
Exhausting all 116,867 partitions gives 1, 27, and 25 extremizers, respectively;
the larger two hosts each have nine symmetry classes. Both exact probability
methods agree coefficient by coefficient. The
[matching report](../../papers/matching_foundations.pdf) includes the
proofs, complete orbit tables, and probabilities. The original six-host data
above remains unchanged; the ladder data is a separate reproducible study.

The [weighted-cover extension](../../results/matching_covers.md) proves
A(Lk)=3k-5 for every k>=3 by a tiling-incidence argument. A separate exact
cover algorithm reproduces nine host maxima and supplies verifiable cost
tables. On L5, a [direct counting proof](../../notes/l5_extremizers.md) now gives
all fifteen extremizers and their six symmetry classes. The full
deficit-three band is checked without increasing the old partition solver's
12-edge limit.

## Search method and coverage argument

An edge coloring up to color renaming is a set partition of the edge positions.
Restricted-growth strings give one representative of each partition. For a
prefix with k existing color classes, the next edge can use any existing class
or the unique next new class.

Enumerate all perfect matchings first. When the last edge of a matching is
assigned, test whether its colors are all distinct. If they are, every extension
of this prefix contains that rainbow matching, so the whole subtree is rejected.
Existing colors are never changed or merged while extending a prefix.

Let T(r,k) count completions of r remaining positions when k classes already
exist. Then T(0,k)=1 and

$$
T(r,k)=kT(r-1,k)+T(r-1,k+1).
$$

The first term chooses an existing class; the second creates one new class.
A rejected prefix accounts for exactly T(r,k) full partitions. Pruning therefore
does not mean visiting all 4,213,597 cube leaves individually: the reported
coverage is surviving leaves plus disjoint rejected subtrees. The solver checks
that this sum equals T(m−1,1), the Bell number for m edges. This is an exact
coverage reduction, not sampling.

`src/rainbow_constraints.py` implements the search with a 12-edge limit.
`experiments/sparse_rainbow.py` specifies the six hosts explicitly. Perfect
matchings are generated by permutations; an independent edge-subset oracle
checks them. On every balanced bipartite host with part size 2 or 3 that admits
a perfect matching, the pruned histogram is compared with direct unpruned
partition enumeration. Larger-host witnesses and the cycle formula supply
additional checks. All arithmetic is integral and deterministic.

## Reproduction

From the repository root, using Python 3.11+ and its standard library:

```sh
python -m unittest discover -s tests -v
python -m experiments.sparse_rainbow --check results/data/sparse_rainbow.json
```

The original suite and its historical evidence record remain unchanged.
The new execution provenance is linked from [the sparse verification record](../../results/sparse_verification.md).

## Further work

Compare the fixed-host proof and classification with precise published
sparse-host results before proposing general statements. The cube upper bound
and finite symmetry classification are complete in the linked notes. Further
host comparisons are project-development directions; their current status in the
literature has not been established here.
