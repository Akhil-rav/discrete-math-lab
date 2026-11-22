# Must a single reversal improve a nonoptimal tournament?

For a tournament on n vertices let S count stars with one outgoing and two unordered incoming leaves, without restrictions on edges between leaves. A vertex of outdegree x contributes f(x)=x choose(n-1-x,2). Reversing u -> v changes the objective by exactly f(d_u-1)-f(d_u)+f(d_v+1)-f(d_v).

On vertices 0,...,5 orient every pair from smaller to larger except 04 and 13. This tournament has value 15; the optimum is 12. No single reversal strictly decreases its value.

The [exhaustive check](star_descent.py) finds no such counterexample at orders four or five (below four there are no such stars). At order six there are 384 labeled nonoptimal tournaments without a strictly improving move. Allowing ties changes the picture: every tournament of orders four through six reaches an optimum along a nonincreasing path. To test this, start at all minimizers and traverse single reversals backwards, allowing only nondecreasing values. No conclusion for larger orders follows.
