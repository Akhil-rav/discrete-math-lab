# A forecast discrepancy persists at almost every larger order

In the triangle-free process started from the empty graph on n vertices, write Q_j for the number of legal pairs after j moves. The move number is known to the observer. Let h(n) be the minimum positive history length that always suffices for predicting the conditional distribution of the next count. When fewer observations are available, use all of them. A terminal count stays at zero.

**Transfer statement.** Suppose two possible histories through move m on k vertices agree in their last r counts and give different next-count laws. On every sufficiently large number n of vertices there are two histories with the same property. In fact, for n at least k the specific translated histories fail to witness a discrepancy at most 4(m+1) times.

**Center the observations.** Set D_j=binom(n,2)-Q_j, the number of present or closed pairs. Adding isolated vertices to any realized graph leaves D_j unchanged: every pair incident to a new vertex is absent and open. This holds at every prefix of a move sequence that uses only old vertices. Thus a history D=(D_0,...,D_m) realized at k remains possible at each n at least k. In particular, translating both count histories preserves their common suffix.

**Count ordered paths.** Fix the centered history D. For an integer z let A(D,z;n) count all ordered sequences of m+1 legal edge additions with this prefix of centered counts and final centered count z. Let B(D;n) count all such sequences with arbitrary final centered count. There are polynomials A and B in n of degree at most 2(m+1) representing these numbers at every positive integer n. Indeed a sequence uses s at most 2(m+1) distinct vertices. Choose that support in binom(n,s) ways. Its ordered sequences using all s vertices can be counted on the chosen support alone, since removing isolated vertices preserves every centered count. Summing the corresponding constant coefficients times binom(n,s) gives the assertion for both polynomials.

All complete paths counted by B have probability equal to the reciprocal of the product of the m+1 open counts in their common prefix. Consequently the conditional probability of z equals A(D,z;n)/B(D;n). A discrepancy at k requires a positive open count at the common final observation, since a zero count fixes the forecast. Thus both denominators are positive at k and at every larger order by embedding an actual path of m+1 moves.

Choose z witnessing a discrepancy for histories D and E at k. The polynomial

    A(D,z;n) B(E;n) - A(E,z;n) B(D;n)

is nonzero at k. Its degree is at most 4(m+1), so it can vanish at no more than that many larger integers. At every other order the conditional next-count probabilities still differ. This proves the transfer statement. It bounds the number of exceptional orders without locating them.

**Consequences.** The [eight-vertex witness](README.md#how-many-past-counts-help-predict-the-next-one) at m=12 agrees on nine counts. Hence h(n) is at least ten for all sufficiently large n, with at most 52 exceptions above eight for that translated witness. More generally h(n) converges to its supremum in the positive integers extended by infinity. For any integer r below that supremum, some order witnesses that r observations do not suffice, and transfer makes h(n)>r at all sufficiently large orders. In particular a bounded sequence of these minimum history lengths must eventually be constant. Whether the lengths are bounded is undetermined here.

## An example with no exceptional orders

Four observations are necessary at every n at least six. Consider the two centered histories (0,1,3,u,7,10,13), where u is 6 or 5, and ask whether the next centered count is 15. Their final three observations agree. Let P count paths with the given prefix and A count paths continuing to 15. In the binomial basis the nonzero coefficients are as follows.

| u | Path count | s=6 | s=7 | s=8 |
|---:|---|---:|---:|---:|
| 6 | P | 6480 | 30240 | 0 |
| 6 | A | 8640 | 90720 | 967680 |
| 5 | P | 34560 | 120960 | 0 |
| 5 | A | 57600 | 443520 | 3870720 |

The conditional probability is A divided by P times the common final open count in the denominator, that is, A/[P (binom(n,2)-13)]. Set x=n-6. Substitution in the table gives

    (A_6 P_5 - A_5 P_6) / binom(n,6)^2 = 12441600 (8x^2 - 17x - 6).

The discriminant 481 lies strictly between 21^2 and 22^2. Hence the forecasts differ at every integer n>=6. Their ordering can change: the probability for u=6 is smaller at n=8 and larger at n=9.

[forecast_coefficients.py](forecast_coefficients.py) enumerates the table directly. At each step a new edge has zero, one, or two previously unused endpoints. Assign fresh names in order of first appearance and branch once for an edge joining two fresh vertices. A completed path shape on s vertices with t such simultaneous pairs contributes s!/2^t to the coefficient of binom(n,s): permuting the s support labels gives every realization, with two equivalent name choices at each simultaneous arrival across the enumeration. Equivalently, an actual labeled path determines 2^t possible histories of fresh-name assignments, each with its own final bijection. The deficit after a legal edge addition is the number of edges plus the number of vertex pairs with a common neighbor. This test uses only vertices touched so far. At n=6 the table reproduces the independently counted forecasts 2/3 and 5/6.
