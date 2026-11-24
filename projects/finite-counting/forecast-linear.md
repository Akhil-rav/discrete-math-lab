# Forecast memory grows at least linearly

Write h(n) for the minimum number of past open-pair counts needed to predict the next one in the triangle-free process from the empty graph, with the move number known. Then

    liminf h(n)/n >= 1/2.

The argument extends a pair of ambiguous histories by arbitrarily many moves that each reduce the number of open pairs by exactly one. It uses the [finite witnesses and centered-count convention](forecast-transfer.md). It gives no finite threshold beyond which the asymptotic estimates hold.

## Extending a witness

Suppose that on k vertices two histories of length m moves agree on their last r observations but give different probabilities for a next loss of L. Both have positive probability and end with the same positive number of open pairs. On n=k+2t vertices retain the same centered histories (the centered count is the total number of pairs minus the open count), and append t successive unit losses to each. Both extensions are possible: embed an original path on k vertices and use the new vertices in disjoint pairs. The extended histories agree on their last r+t counts.

We show that their forecasts for loss L differ for every sufficiently large integer t. This step matters because observing t unit losses does not tell the observer which vertices were used.

## All ways to realize the appended losses

Fix one original centered history. Enumerate every compatible ordered path on the standard support of s vertices that uses all s vertices, for every s through 2m. The vertices not in this support are initially isolated. Adding an edge between different components creates at least one newly closed pair whenever either endpoint has an existing neighbor: the other endpoint previously had neither an edge nor a common neighbor with that neighbor. Consequently a unit loss between components must join two isolates. Each such move produces a separate single-edge component. That component has no internal move and cannot meet any other component during a later unit loss.

Thus each continuation consists of j moves entirely inside the original support and t-j ordered pairs of previously untouched vertices. The possible internal sequences are finite, independent of t, with j at most binom(s,2)-m. Fix such an internal sequence and its initial path, on the standard support. Choosing the support in the ambient labeled graph, choosing which slots are internal, and selecting the ordered list of disjoint unordered pairs gives multiplicity

    binom(n,s) binom(t,j) (n-s)_[2(t-j)] / 2^(t-j),

where the subscript is a falling factorial. After removing the common factor n!/2^t this becomes

    binom(t,j) 2^j / [s! (k-s+2j)!].

Omit terms with k-s+2j negative. Terms with j>t vanish by the usual binomial convention. These rules are valid also for t=0: a nonzero term has j<=t and s+2(t-j)<=n, so all required vertices exist. Every path is counted once. Summing the displayed terms gives a polynomial P(t) for the normalized count of paths with this extended history.

## Counting one more move

For a fixed summand the resulting graph consists of a fixed graph on s vertices, b=t-j isolated edges and c=k-s+2j isolated vertices. The number of choices producing any specified loss L is a polynomial in t of degree at most two. Within the fixed graph the number is constant; there are no moves within a single isolated edge. For an edge between different components its loss equals one plus the two endpoint degrees: all pairs it closes were open, and the two neighbor sets give distinct closed pairs. Hence moves between vertices of the fixed graph and the other vertices have counts linear in b for fixed c. Moves between two different isolated edges, between an edge and an isolate, or between two isolates have counts 4 binom(b,2), 2bc and binom(c,2), with respective losses 3, 2 and 1. These categories also cover the case of no available move of loss L.

Multiplying each path summand by this polynomial and adding gives a polynomial A(t) for the normalized number of paths extended by loss L. For j>t, evaluating the polynomial formally at b<0 causes no issue because the path factor vanishes. The conditional probability is A(t)/[P(t)Q(t)], where Q(t) is the common final open count. All paths for a fixed observed history have the same probability before the extra move.

For the two prefixes compare A_1 P_2 with A_2 P_1. Their difference is a polynomial nonzero at t=0 by the original witness. It has only finitely many integer roots. The denominators stay positive by the explicit disjoint-edge construction and the availability of a legal move on the original vertices. This proves h(k+2t)>=r+t+1 for all sufficiently large t.

The eight-vertex witness has r=9, and the seven-vertex witness has r=5. They give h(n)>=n/2+6 for sufficiently large even n and h(n)>=(n+5)/2 for sufficiently large odd n. The claimed limit inferior follows. Priority has not been established.
