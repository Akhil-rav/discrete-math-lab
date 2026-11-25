# Forecast memory grows at least linearly

Write h(n) for the minimum number of past open-pair counts needed to predict the next one in the triangle-free process from the empty graph, with the move number known. Then

    liminf h(n)/n >= 1/2.

The argument extends a pair of ambiguous histories by arbitrarily many moves that each reduce the number of open pairs by exactly one. It uses the [finite witnesses and centered-count convention](forecast-transfer.md). The last section supplies an exact certificate valid at every order from eight onward.

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

## Removing the asymptotic qualifier

For every integer n>=8 the following explicit lower bound holds:

    h(n) >= floor(n/2) + 6.

Use the two twelve-move centered histories from the eight-vertex witness and ask for a next loss of four. Use the same centered histories at k=9 for the odd orders. In both cases the common suffix length is nine. Writing n=k+2t, it suffices to prove that the extended forecasts differ for every t>=0.

[check_unit_loss_padding.py](check_unit_loss_padding.py) implements the polynomial construction above with exact rational arithmetic. It first groups prefixes on a fixed support by their final graph. For each internal unit-loss continuation of depth j, let b=t-j, and let c=k-s+2j be the number of remaining isolates. If c<0 the term contributes nothing. For fixed c, the number of ways to realize a specified next loss has the form U+V b+W binom(b,2), obtained by the component counts above. The program accumulates the coefficients by j, expanding only moves on the core graph. It exhausts all internal continuations because each adds an edge to a fixed finite vertex set.

For each parity the resulting cross-product difference has degree at most 18 (the sum of the two maximum internal depths plus two). It is nonzero by direct evaluation at t=0,1,2. At t=3 its value is nonzero, and all its forward differences through order 18 are either zero or have the sign of that value. Newton's forward formula proves it has that same strict sign for every t>=3. Thus ten plus t observations are necessary for all n=8+2t and n=9+2t, giving the formula. As an implementation check the program also computes the unnormalized path counts by direct support growth for t=0,1,2 in both parities and for both histories.
