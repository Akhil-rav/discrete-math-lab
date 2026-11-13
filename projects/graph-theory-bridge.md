# From olympiad proofs to graph theory

Starting point: comfortable with olympiad proofs, new to graph theory. Begin with
counting arguments, injections, extremal choices, and explicit constructions.
Advanced linear algebra is not needed for the flagship matching project.

## A small dictionary

| Language | Meaning | Familiar proof tool |
|---|---|---|
| Simple graph | Vertices joined by unordered edges, with no loops or repeated edges | Encode a relation or compatibility condition |
| Bipartite graph | Vertices split into disjoint classes L,R; all edges cross between them | Two kinds of objects to pair |
| Degree of v | Number of edges incident to v | Count the same set of incidences in two ways |
| Neighborhood N(S) | Right vertices adjacent to at least one left vertex in S | Union of available choices |
| Matching | Edges with no shared endpoints | A partial injective assignment |
| Perfect matching | A matching covering every vertex | A complete pairing |
| Rainbow matching | A matching whose edges have distinct colors | Distinctness imposed on top of an injection |
| Isomorphism | A bijection of vertices preserving adjacency | Relabeling without changing structure |

In code a bipartite edge may be written (i,j) with both labels drawn from the
same numerical range: the left/right positions distinguish their vertex classes.
The original `BipartiteGraph` class instead requires globally disjoint labels.
Check the representation before copying an example between modules.

## Three proof exercises, in order

1. **Necessary condition.** If a matching covers every left vertex, prove
   |N(S)|≥|S| for every S⊆L. Hint: restrict the matching's injective assignment to S.
2. **Regular case.** In a finite d-regular bipartite graph with d>0, count all edges
   from both sides to get |L|=|R|. Then count edges leaving S to get
   d|S|≤d|N(S)|. Hall's theorem now supplies a perfect matching. Read
   [the note](../notes/halls_theorem.md) and identify which step is a cited theorem
   rather than the counting argument itself.
3. **An extremal coloring.** On C6, use its two alternating perfect matchings to
   prove A(C6)=4. Give an explicit coloring for the lower bound and an independent
   obstruction for the upper bound. Then generalize to C2n.

## Learn the algorithm through one trace

Let L={a,b}, R={x,y}, with edges ax, ay, bx. A greedy choice ax can leave b
unmatched. The alternating path b–x–a–y lets you remove ax and add bx, ay,
increasing matching size by one. Trace this on paper before reading
`src/matchings.py`. An augmenting path alternates unused and used edges and starts
and ends at unmatched vertices. This is the bridge between an existence proof
and the reusable algorithm.

Start with [the first session](first-session.md), then return to the
[roadmap](roadmap.md). Use the expansion material after you can explain the
matching project comfortably; its spectral literature needs additional background.
