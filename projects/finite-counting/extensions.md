# Four extensions of the finite examples

These are elementary derivations and reproducible checks, not priority claims. Run `python extensions.py` in this directory (Python 3.9+).

## The triangle-free process: a statistic that actually determines the drift

Call an absent pair open if adding it keeps the graph triangle-free. Let Q>0 count the open pairs, and let W count **unordered vertex triples** with exactly one present edge and two open pairs. If Q' is the next open-pair count, then

    E[Q' - Q | G] = -1 - 2W/Q.

The chosen pair itself always disappears. Another formerly open pair closes precisely if it and the chosen pair complete a triangle with an existing edge. These two pairs determine a unique third vertex and a unique present edge. Thus each triple counted by W contributes exactly twice to the sum of additional losses over all choices, once for each choice of which open pair is added. Divide by Q. The formula is for nonterminal states; it needs no independence assumption.

In the star-plus-edge example W=10; in the path-plus-isolate example W=6. The difference of four triples explains the full unit of drift separating these two states. Q and W suffice for this **conditional mean**; the identity does not say the pair determines future transitions. The script computes W directly from triples and checks the identity against the full transition lists of every reachable nonterminal six-vertex graph.

## Outward stars in tournaments: the general threshold

For a star with r outward arcs (r>=1), the least tournament order forcing it is 2r. At order 2r the average outdegree is r-1/2, so an integer outdegree is at least r. On residues modulo 2r-1, direct i to i+1 through i+r-1 cyclically. Every vertex has outdegree exactly r-1. This gives the lower bound, including r=1 by the singleton tournament. Furthermore, at order 2r-1 the avoiding tournaments are **exactly** the regular ones: all outdegrees must be at most their average, hence equal. Direct enumeration checks the first three thresholds, including the 24 labeled regular tournaments on five vertices. This concerns stars only.

## Random vertex colors: precisely when edge indicators are independent

Give each vertex independently one of q>=2 uniform colors. For an edge set S, write v for the number of incident vertices and c for the number of connected components on those vertices. The probability that every edge of S is monochromatic is q^(c-v): choose one color per component, out of q^v assignments. It follows that the monochromaticity indicators for an edge family are jointly independent **if and only if the family is a forest** (finite simple graphs). In a forest every subset has v-c=|S|, so every all-ones event factors; inclusion-exclusion gives factorization for arbitrary zero/one patterns. On a cycle of length l the all-ones probability is q^(1-l), not q^(-l). Every nonforest contains such a cycle. The script compares predicted all-ones counts with direct coloring on every edge subset of K4 for q=2 and 3.

## Factorization lengths: compute every length without enumerating triples

For a target n>=0 solve 6a+9b+20c=n in nonnegative integers. Enumerate just the c with 0<=20c<=n and 20c congruent to n modulo 3. Write t=(n-20c)/3. Then 2a+3b=t, so b runs from b0=t mod 2 to floor(t/3) in steps of two. If the range is empty, skip it. The total length is c+(t-b)/2, which falls by exactly one each step. Thus each c gives an integer interval of lengths, and overlapping intervals add multiplicities. This proves a formula for every target, including unrepresentable targets and n=0 (empty factorization). The script compares exact multiplicities with direct enumeration through n=240.

For n<60, at most one admissible c exists: admissible c values differ by at least three. All nonempty length sets below 60 are therefore intervals. At 60 the two slices are {3} and {7,8,9,10}. Consequently **60 is the first target with an internal gap** for these three generators.
