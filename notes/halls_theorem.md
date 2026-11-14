# Hall's Theorem and Regular Bipartite Graphs

## Known theorem: Hall's Marriage Theorem

Let $G=(L,R,E)$ be a finite bipartite graph. There is a matching that
saturates every vertex of $L$ if and only if

$$
|N(S)| \ge |S|
$$

for every subset $S \subseteq L$, where $N(S)$ is the set of neighbors
of vertices in $S$.

A primary-paper formulation equivalent to this statement is the matching
deficiency formula in Li–Tu–Jin, [Lemma 2.1](https://arxiv.org/pdf/math/0610910v1).
Their formula says the largest matching saturates L exactly when every subset
has nonpositive deficiency |S|−|N(S)|. The empty subset has deficiency zero.
The regular-graph argument below is the standard elementary corollary.

## Corollary: every $d$-regular bipartite graph has a perfect matching

Assume $G=(L,R,E)$ is finite, bipartite, and $d$-regular with $d\ge 1$.

First, counting edges from the two sides gives

$$
d|L| = |E| = d|R|,
$$

so $|L|=|R|$.

Now take any $S\subseteq L$. Exactly $d|S|$ edges leave $S$.
Every vertex of $N(S)$ has total degree $d$, so at most $d|N(S)|$
edges can run from $S$ into $N(S)$. Therefore

$$
d|S| \le d|N(S)|.
$$

Since $d>0$,

$$
|S| \le |N(S)|.
$$

Hall's condition holds, so there is a matching saturating $L$. Because
$|L|=|R|$, this matching is perfect.

## Why run a computation if the theorem is already proved?

The computation is a **reproduction / sanity check**, not evidence needed
for the theorem. It serves three purposes:

1. verifies that the graph representation and matching code behave correctly;
2. creates a trusted base for later experiments where no theorem is known;
3. practices the research workflow of moving between proof and computation.

The accompanying experiment exhaustively checks all labeled
$d$-regular bipartite graphs with $n\le 5$ vertices on each side.
