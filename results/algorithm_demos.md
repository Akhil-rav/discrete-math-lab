# Checked algorithm demonstrations

**Status:** reproductions of standard methods on bounded finite domains.
Commands and contracts are in [experiments](../experiments/README.md).

## Vertex color-coding

On every labeled simple undirected graph on n=1,…,4 vertices, for each k=1,…,n,
the experiment checks all k^n assignments of vertex colors: **22,955 cases**.
The subset DP agrees with ordered-vertex path enumeration in every case.
Each returned path is checked for length, distinct vertices, adjacency, and colors.

For every tested graph containing a k-vertex path, the exact success fraction
is at least k!/k^k. This audits the finite implementation and reproduces the
known fixed-path probability argument. See [the method](../notes/color_coding.md).

## Edge expansion and walks

All eligible cuts are enumerated; all walk probabilities are exact rationals.

| Graph | h(G) | Lazy-walk TV at time 8 | Ordinary-walk TV at time 8 |
|---|---:|---:|---:|
| K4 | 2 | 1/8748 | 1/8748 |
| C6 | 2/3 | 2187/32768 | 1/2 |
| K33 | 5/3 | 1/384 | 1/2 |
| Two disjoint triangles | 0 | 1/2 | 1/2 |

Walks start at vertex 0 and TV is measured against uniform measure on all
vertices. K4's two walk types happen to have the same TV sequence from that
start; their distributions need not agree. Bipartite examples retain an
ordinary-walk parity obstruction; disconnection persists after adding laziness.

Independent benchmarks check h(Kn)=ceil(n/2) for 2≤n≤7 and h(Cn)=2/floor(n/2)
for 3≤n≤9, using simple cycles. See [normalization and limits](../notes/expansion_and_walks.md).
