# Cube incidence bound: checks

**Claim:** for the fixed cube Q3 and arbitrary edge colorings, A(Q3)=7.
For every avoiding seven-coloring the unused-capacity and overlap quantities
U and O defined in the proof are nonnegative integers with U+O=1.

Recorded November 14, 2026. The [proof](../notes/cube_upper_bound.md) uses
the incidence counts summarized below.

## Counting argument

Each cube edge occurs in three perfect matchings, giving nine matchings in
total. A pair occurs in at most two. These counts give b(B)<=2(|B|-1) for
every nonempty color class; summing over the classes bounds the number of
colors by seven. The construction with six edges of one color attains seven.
Counting class-matching obstructions in two ways gives U+O=1.

## Details

| Detail | Argument |
|---|---|
| Host and target | Twelve edges; a perfect matching uses four; colors need not be proper |
| Uniform edge incidence | Simultaneous relabelings take any ordered unequal pair to (0,1); remaining forbidden assignments give 6-4+1=3 |
| Matching count | Count all edge-matching incidences as 12*3 and as four times the number of matchings |
| Pair incidence | Incident edges give zero; otherwise only a two-by-two matching remains, with at most two completions |
| Singleton class | Cannot create a repeated color in a matching |
| Size-two class | Use pair incidence, not the weaker bound from individual edges |
| Size-three class | Nine appearances imply at most floor(9/2)=4 obstructed matchings |
| Larger class | 2b<=3s and 3s/2<=2(s-1) for s>=4, including s=4 equality |
| Covering step | Avoidance makes every matching belong to at least one obstruction set; overlaps only increase the sum |
| Integer conclusion | 9<=24-2r gives r<=7.5, hence integer r<=7 |
| Lower bound | Six edges in one color and six distinct new colors; each matching uses two common-color edges |
| Equality analysis | Sum b(B)=sum q(M); capacities total ten and q(M)>=1 on all nine matchings; both resulting deficits are nonnegative integers |
| Type interpretation | U+O=1 permits exactly (1,0) or (0,1); a unit overlap means one matching is counted twice |

The proof's O is defined on avoiding colorings as sum(q-1). The computational
routine clips q-1 at zero to provide meaningful output on a negative control;
these definitions agree on the 174 avoiding colorings. The review does not use
the clipped extension to assert a converse or classify arbitrary colorings.

## Scope

The maximum seven and the stated balance identity are proved for the fixed
cube, independently of search. No proof of the complete nine-orbit classification
is supplied by this inequality. Its exact population split and the sharper
per-size obstruction maxima remain exhaustive finite computations. The
literature comparison remains limited as recorded in
[the source note](../notes/literature/cube_classification.md).

Reviewed source: [cube_upper_bound.md](../notes/cube_upper_bound.md).
SHA-256: `26ea2f69f72618cc36d88c809b67a8b1175d44d877cbbc06a7b9a3f667f94efd`.
