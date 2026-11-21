# Local counts, coloring distributions, and factorization gaps

These are working derivations and finite checks. The sections distinguish established tools from what the calculations demonstrate; none asserts priority.

## 1. Detecting short cycles from one legal move

Let a reachable triangle-free graph be a disjoint union of cycles on n vertices. Let c_j be the number of components of length j, Q the number of legal pairs, and D the loss of legal pairs on the next move (when Q>0). Then

    Q = n(n-1)/2 - 2n + 2c_4
    number of choices with D=1:  3c_6
    number of choices with D=3:  n - 4c_4 - 5c_5 - 6c_6
    number of choices with D=5:  all remaining choices.

**Proof.** Subtract the n edges and the distinct pairs at distance two. A 4-cycle has only two such pairs rather than four. Components of length four or five have no legal internal move. Moves across components cost five (the chosen pair plus four pairs to its endpoint neighbors). In longer components the proof in [the previous note](five-directions.md) applies: one length-three path between the chosen endpoints saves two pairs; two paths save four. This gives the formulas. Conversely n and Q recover c_4; the probabilities of losses one and three, multiplied by Q, recover c_6 and then c_5. The component lengths >=7 cannot be distinguished by these one-step data apart from their total size. For instance, C14 and two C7 components have identical one-step laws but only the former can complete to K(7,7).

## 2. Counting crossings in nearly extremal mixed-star avoiders

Keep the notation of the [mixed-star proof](five-directions.md): L consists of vertices with outdegree below a, H is the complement, and all vertices of H have indegree below b. Set l=|L|, h=|H|, x=2a-1-l, y=2b-1-h. Both deficits are nonnegative. The number e of arcs directed from L to H satisfies

    e <= min(l*x, h*y)/2.

Summing outdegrees over L counts exactly choose(l,2)+e; summing indegrees over H gives choose(h,2)+e. Applying their degree caps proves the bound. Thus on **one vertex below the extremal order** (x+y=1), all cross arcs still point H to L. At two below, reversal first becomes possible, and the bound can be sharp. For a=b=2 take two two-vertex blocks with internal arcs L1 to L2 and H1 to H2. Orient all cross arcs H to L except L2 to H1. The low vertices have outdegree one and the high vertices indegree one; no mixed (2,2)-star occurs. For a nonvacuous instance at order greater than the size of the star, take a=b=3 and two four-vertex blocks obtained by deleting a vertex from a regular five-vertex tournament. Each block has two vertices of each outdegree 1 and 2. Begin with all arcs H to L; reverse a matching from the two L vertices of outdegree 1 to the two H vertices of indegree 1. Degree caps of 2 still hold, e=2 attains the bound, and the eight-vertex host is larger than the seven-vertex star.

## 3. What the full coloring distribution remembers on a cactus

A cactus here is a simple graph in which every edge belongs to at most one simple cycle. Let X count monochromatic edges under independent uniform q-coloring, q>=2, and m be the number of edges. Then the polynomial identity

    E[(1+x)^X] = (1+x/q)^m * product over cycles C of [1+(q-1)(x/(q+x))^|C|]

holds after clearing denominators. Indeed, expand the left side over edge subsets S. The probability all edges in S are monochromatic is q^(-|S|+b(S)), where b(S) is the cycle rank. For a cactus, deleting an edge from each complete cycle in S leaves a forest without changing component count, so b(S) is the number of complete cycles in S. Expand q^b as a product of factors 1+(q-1) times the indicator of inclusion, i.e. each factor is 1+(q-1)1_{C subset S}. Summing over S now factors because the cycles have disjoint edge sets, giving the display. This is a specialization of the [multivariate Tutte / Potts expansion](https://arxiv.org/abs/math/0503607).

**Converse within this class.** Given q and the law of X, m is the maximum possible X. Divide by (1+x/q)^m, and use z=x/(q+x). The result is a polynomial product of 1+(q-1)z^j with multiplicity c_j at length j. After dividing out the already recovered shorter factors, the coefficient at z^j equals (q-1)c_j. Thus the law recovers every cycle length with multiplicity, and the number of bridges is the remaining edge count. It need not recover how the cycles are attached, nor isolated vertices. This sharpens the shortest-cycle calculation *within cacti*, not for arbitrary graphs.

## 4. A two-gap bound for a whole family of factorization length sets

Fix coprime integers a>=2 and b>3a and generators 2a,3a,b. Count the lengths of nonnegative factorizations of an integer N. There are at most **two separate runs of missing lengths** between attained lengths. This counts runs, not their widths, and two runs actually occur.

**Proof.** For the number c of copies of b the candidates satisfy bc congruent to N modulo a and 0<=bc<=N. Take the greatest candidate C; if none exists, the set is empty. Set u=(N-bC)/a, so 0<=u<b. Write c=C-aj, j=0,...,floor(C/a), and s=u+bj. As in the earlier proof, each slice is the whole integer interval

    [C-aj+ceil(s/3), C-aj+floor(s/2)],

empty only if s=1. Both endpoints are nondecreasing since b>3a. The separation between the lower endpoint of the next slice and the upper endpoint of this one is d(s)=ceil((s+b)/3)-a-floor(s/2). If s=2b+w with w>=0 then d(s)=ceil(w/3)-floor(w/2)-a <=1-a: check w=0,...,5 and note a decrease by one per additional six. Consequently all slices from j=2 onward form a single interval; only the first two joins can leave gaps. An empty first slice cannot introduce another join. For a=2,b=25,N=100 the slices are {4}, [11,14], [17,25], giving two internal gap blocks. In contrast, for b=20,a=3 only one run is possible as shown earlier.

This is a family-level bound with a sharp example, not a new result about the classical Chicken McNugget monoid in isolation. Relevant comparison: [Chapman, Garcia-Sanchez and O'Neill](https://arxiv.org/abs/1912.04494), [Moskowitz and O'Neill](https://arxiv.org/abs/2311.05786). Whether the family-level statement already follows from a published length-set description has not been settled here.

**Generalization and optimal bound.** Replace 2a,3a by pa,(p+1)a for any integer p>=2. Suppose b>(p+1)a, gcd(a,b)=1 and a>=2. Every length set has at most **p internal gap blocks**, and for each p this is best possible across this family. For a target N the same choice of C gives slices indexed by j with s=u+bj. The slice is [C-aj+ceil(s/(p+1)), C-aj+floor(s/p)]: for h summands of p and p+1 the attainable totals are exactly ph,...,(p+1)h. Endpoints are nondecreasing. When s=pb+w, w>=0, the next separation is ceil(w/(p+1))-floor(w/p)-a <= 1-a. Such slices are nonempty: s>=pb>p(p+1), so s/p-s/(p+1)>1. Therefore slices j>=p have no internal break when combined, and the earlier at most p individual nonempty intervals give the claimed bound even if some are empty.

For sharpness choose b=2a*p*(p+1)+1 and N=pa*b. Then C=pa, u=0 and j runs from 0 to p. All p+1 slices are nonempty (s=0 or s>=b). For j<p, separation is at least b*(p-j)/(p*(p+1))-a >= b/(p*(p+1))-a > a. Thus each of the p joins has missing integers. This establishes an optimal bound on the **number** of gap blocks, uniformly over targets, with no asymptotic assumption. The generators are minimal in this construction: b is not divisible by a; the other two are less than b, and neither is a multiple of the other.

## 5. Theta graphs: an ordinary-coloring test case beyond cacti

Take three internally vertex-disjoint paths of positive lengths A,B,C between two distinguished vertices, giving a simple graph (at most one length one). Set s=A+B+C. For uniform q-coloring define the normalized transform F(z) by dividing E[(1+x)^X] by (1+x/q)^s and substituting z=x/(q+x). Then

    F(z) = 1 + (q-1)(z^(A+B)+z^(A+C)+z^(B+C)) + (q-1)(q-2)z^s.

One proof uses the path transfer matrix J+xI, where J is the all-ones q by q matrix. An edge contributes 1+x for equal colors and 1 otherwise. The eigenvalues of the path matrix are q+x on constants and x on the orthogonal complement. For a path of length l, given its endpoint colors, sum the weights over internal colors; after division by (q+x)^l/q this is 1+(q-1)z^l if endpoints agree and 1-z^l otherwise. The products over the three paths are averaged with endpoint weights 1/q and (q-1)/q, respectively (all independent internal vertex normalization factors cancel against (1+x/q)^s). Expansion gives the formula. The same reasoning applies if trees are attached: each new leaf adds a factor 1+x/q to the unnormalized expectation.

**Recovery.** Within this family the distribution determines the multiset of path lengths, even with attached trees. If q>2, the largest exponent in F is s, so subtract its known term; if q=2 that term is absent. The three pair-sum exponents, counted with multiplicity by dividing coefficients by q-1, remain. Their sum is 2s, and subtracting each pair sum from s gives the missing path length. Attached trees need not be individually recoverable. This is an inverse observation for ordinary independent colors, not a DP-coloring theorem; compare [Kaul's research on theta graphs and graph gluings](https://www.math.iit.edu/~kaul/research.html).

## 6. Tighter finite-horizon comparison for the two ladder closures

In [the small-pattern proof](horizon.md) each marked initial pattern has a dominating set of at most 2t marked vertices: every other pattern vertex neighbors a mark. This remains true upon adding edges and taking vertex-identification quotients. For each connected component of every resulting pattern and every homomorphism into a finite ladder closure, the image uses at most **6t columns**. Each dominating vertex covers only its own column and its two neighboring columns. Hence if k>6t the image misses an entire column. Deleting any column cuts the closure into an ordinary strip and eliminates winding. Equivalently every closed walk in the image lifts closed to the infinite strip. The rooted lifting proof in [five-directions.md](five-directions.md) therefore applies to these particular patterns without needing k>8t. The quotient and inclusion-exclusion steps need only these patterns. The two initial counts are the same for these widths; moreover for even k>6t and t>=1, 2k-1>3(3+t), so the previous nontermination bound still applies. Thus even k>6t suffices. No sharp threshold is asserted.

For empirical lower-width checks, path_counts.py counts *ordered histories*, not just support, using the identity that a particular history with open counts q0,...,qt has probability 1/(q0*...*q(t-1)). It groups equivalent first moves by a translation/reflection of the cyclic strip, optionally exchanging the rails. A move from row s to r across l columns is equivalent to one across k-l columns with parity s XOR r XOR twist. At the final step the loss is computed directly from the two rows of open pairs and the old neighbor sets. These shortcuts are checked against the full-state recursion on small instances. A terminal state ends a history; it is not padded.

## 7. How many mixed-star centers are forced? Equality and stability

Fix a,b>=1 and n>=N=2a+2b-2. A center is a vertex with at least a outgoing and b incoming arcs. **Every tournament has at least n-N centers, and this is attained at every such n.** Moreover every minimizer has a canonical ordered partition

    regular H (2b-1 vertices)  ->  arbitrary M (n-N vertices)  ->  regular L (2a-1 vertices),

with every H-to-L arc also forward. Thus the exact number of labeled minimizers is the multinomial coefficient for these three sizes multiplied by R(2a-1) R(2b-1) 2^choose(n-N,2), with R(s) the number of regular labeled tournaments on a fixed s-set. This counts centers, not embeddings of the star.

Proof: use the low-outdegree set L and low-indegree set H. They are disjoint since n>=a+b. Their internal degree sums force l<=2a-1 and h<=2b-1 even when centers are present. Every vertex outside them is a center. At equality both bounds are tight, which forces regularity and leaves no outgoing capacity from L and no incoming capacity to H. Conversely the displayed construction has exactly the required centers: each middle vertex beats 2a-1 vertices and loses to 2b-1, and no outer vertex qualifies. Regular tournaments of both odd orders exist. This also proves the count, since the partition is recoverable from the degree tests.

**Quantitative extension.** If there are e extra centers beyond this lower bound, put x=2a-1-l and y=2b-1-h; then x+y=e. All arcs pointing the wrong way between the three blocks (in the displayed order) belong either to the arcs leaving L or those entering H. There are at most (l*x+h*y)/2 such arcs, by subtracting internal arcs from the corresponding degree budgets. Reversing just those arcs orders the three blocks; this does not assert that the smaller outer blocks become regular. Thus a small excess of centers controls an explicit edit distance to this ordered-block property.

**Translation of gaps once the last slices join.** With generators pa,(p+1)a,b as above, for all N>=a(b-1)+pab the set of missing internal lengths at N+b is exactly the corresponding set at N translated by one. Indeed the unique u in [0,b-1] with au congruent to N modulo b does not change, and C=(N-au)/b increases by one. Our bound on N ensures C>=pa. Existing slices translate by one. There is at most one new end slice; if present its preceding j is at least p and the join has no gap. Since its lower endpoint is at or above the lower endpoint of the previous nonempty last slice, it cannot fill an earlier hole. Thus b is an eventual period for the widths and relative positions of the gaps (not necessarily the least period). This explicit sufficient threshold may be far from optimal.

**Centers and embeddings are different optimizations.** At n=7, a=1, b=2 the proved lower bound is three centers. But among hosts with *exactly* three centers the minimum number of stars is 31, whereas the unrestricted minimum is 30 and is attained with four or six centers. An unordered choice of leaves with center v contributes choose(d(v),a)choose(n-1-d(v),b), without dividing by automorphisms. The independent Gray-code enumeration in star_gray.py reverses one arc at a time and checks all 2^21 labeled tournaments. The minima at center counts 3,4,5,6,7 are 31,30,31,30,45. A second calculation in star_scores.py uses the classical tournament score-sequence characterization (nondecreasing scores, first j summing to at least choose(j,2), equality at j=n). It produces scores (0,1,2,4,4,5,5) attaining 30. No classification of all copy-minimizers is claimed.
