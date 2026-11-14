# Review of the cube incidence proof

**Claim:** for the fixed cube Q3 and arbitrary edge colorings, A(Q3)=7.
For every avoiding seven-coloring the unused-capacity and overlap quantities
U and O defined in the proof are nonnegative integers with U+O=1.

**Primary verdict: proved as written.** Review date: November 14, 2026.
This is self-review, not independent refereeing or a novelty determination.

## Dependency graph

Fixed host K4,4 minus diagonal -> each edge occurs in three perfect matchings
-> nine matchings in total. Two-edge extension count -> each pair occurs in
at most two. These incidence facts -> b(B)<=2(|B|-1) for every nonempty class
-> union bound across colors -> r<=7. The explicit common-color construction
on edges incident to two left vertices -> r>=7. Double counting class-matching
obstructions -> the U+O=1 identity for extremizers.

All leaves are internal elementary arguments or stated conventions. No
external theorem or computation is a premise, and there is no circular
reliance on the previously computed maximum or orbit list.

## Obligation matrix

| Obligation | Status | Check |
|---|---|---|
| Host and target | Passed | Twelve edges; a perfect matching uses four; colors need not be proper |
| Uniform edge incidence | Passed | Simultaneous relabelings take any ordered unequal pair to (0,1); remaining forbidden assignments give 6-4+1=3 |
| Matching count | Passed | Count all edge-matching incidences as 12*3 and as four times the number of matchings |
| Pair incidence | Passed | Incident edges give zero; otherwise only a two-by-two matching remains, with at most two completions |
| Singleton class | Passed | Cannot create a repeated color in a matching |
| Size-two class | Passed | Use pair incidence, not the weaker bound from individual edges |
| Size-three class | Passed | Nine appearances imply at most floor(9/2)=4 obstructed matchings |
| Larger class | Passed | 2b<=3s and 3s/2<=2(s-1) for s>=4, including s=4 equality |
| Covering step | Passed | Avoidance makes every matching belong to at least one obstruction set; overlaps only increase the sum |
| Integer conclusion | Passed | 9<=24-2r gives r<=7.5, hence integer r<=7 |
| Lower bound | Passed | Six edges in one color and six distinct new colors; each matching uses two common-color edges |
| Equality analysis | Passed | Sum b(B)=sum q(M); capacities total ten and q(M)>=1 on all nine matchings; both resulting deficits are nonnegative integers |
| Type interpretation | Passed | U+O=1 permits exactly (1,0) or (0,1); a unit overlap means one matching is counted twice |

The proof's O is defined on avoiding colorings as sum(q-1). The computational
routine clips q-1 at zero to provide meaningful output on a negative control;
these definitions agree on the 174 avoiding colorings. The review does not use
the clipped extension to assert a converse or classify arbitrary colorings.

## Strongest safe conclusion and remaining limits

The maximum seven and the stated balance identity are proved for the fixed
cube, independently of search. No proof of the complete nine-orbit classification
is supplied by this inequality. Its exact population split and the sharper
per-size obstruction maxima remain exhaustive finite computations. No logical
gap was found in the stated proof; independent external review remains absent.
The literature comparison remains limited as recorded in
[the source note](../notes/literature/cube_classification.md).

Reviewed source: [cube_upper_bound.md](../notes/cube_upper_bound.md).
SHA-256: `26ea2f69f72618cc36d88c809b67a8b1175d44d877cbbc06a7b9a3f667f94efd`.
