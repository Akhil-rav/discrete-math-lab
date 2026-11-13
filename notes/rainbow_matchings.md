# Rainbow Matchings and Anti-Ramsey Questions

## Edge colorings

An **edge coloring** of a graph $G=(V,E)$ is a map

$$
c:E\to C,
$$

where $C$ is a set of colors.

The coloring here is not assumed to be proper: adjacent edges are allowed
to have the same color.

## Rainbow subgraphs

A set of edges $F\subseteq E$ is **rainbow** if all its edges receive
different colors:

$$
e\neq f \in F \implies c(e)\neq c(f).
$$

A **rainbow perfect matching** is therefore a perfect matching whose edges
all have pairwise distinct colors.

## Anti-Ramsey viewpoint

For a fixed host graph $G$ and target structure $H$, an anti-Ramsey-type
question asks how many colors can appear in an edge coloring of $G$ while
still avoiding a rainbow copy of $H$.

For the experiments in this repository, the target is a perfect matching.

I will use the computational quantity

$$
A(G)=\max\{|c(E(G))|: c \text{ has no rainbow perfect matching}\}.
$$

This notation is local to these notes. Before comparing with a paper, the
paper's exact anti-Ramsey convention must be checked because authors may
package the threshold differently.

## Why color relabeling can be removed

Suppose two edge colorings have exactly the same equality pattern: two
edges have the same color in one coloring if and only if they have the
same color in the other.

Then a set of edges is rainbow in one coloring exactly when it is rainbow
in the other.

Therefore, for exhaustive search, color names themselves do not matter.
Only the partition of the edge set into color classes matters.

The experiment
`experiments/rainbow_complete_bipartite.py`
enumerates these partitions using restricted-growth strings.

## Literature comparison

The values A(K22)=2 and A(K33)=4 reproduce Li–Tu–Jin's known results.
Their forcing threshold rb is A+1 for these perfect-matching hosts;
see [the hypotheses and exceptional n=2 case](literature/young_and_matchings.md).
The [four-class K33 computation](../results/k33_classification.md) additionally
quotients by row/column permutations and transpose, beyond color renaming.
