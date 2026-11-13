# Edge expansion and exact random-walk examples

**Status:** finite educational reproductions, inspired by
[Hoory–Linial–Wigderson](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/HLW06/hlw06.pdf).

Following their Definition 2.1, for a simple graph on N≥2 vertices define

$$
h(G)=\min_{0<|S|\le N/2}\frac{|E(S,V\setminus S)|}{|S|}.
$$

A cut edge is counted once. This is unnormalized edge expansion, not vertex
expansion or conductance. `src/expansion.py` enumerates all eligible subsets
and returns an exact rational value and a minimizing set.

For a positive d-regular graph the ordinary walk chooses a neighbor uniformly.
The lazy walk stays with probability 1/2, otherwise choosing a neighbor uniformly.
Our transition is P_lazy=(I+A/d)/2. Uniform measure is stationary because every
row and column sums to one. The code starts at vertex 0 and measures total
variation distance to uniform, (1/2)Σ_v |p(v)−1/N|, at times 0 through 8.
All probabilities use rational arithmetic.

K4, C6, K33, and two disjoint triangles demonstrate three separate issues:
cut size, bipartite periodicity, and disconnection. In a bipartite graph an
ordinary walk alternates sides; laziness removes that periodicity. Laziness
does not connect separate components. The examples record both kinds of walk.

These four graphs are not an infinite expander construction. The survey's
Definition 2.2 requires growing graph orders, bounded fixed degree, and a
uniform positive expansion lower bound. No eigenvalue computation, spectral
inequality, Ramanujan certificate, or interlacing-family construction is claimed.

For the next reading step, Wigderson's [March 2019 book draft](https://www.math.ias.edu/files/Website03-25-19.pdf),
Chapters 7–8, gives randomness/pseudorandomness context. For an advanced
existence result see [Marcus–Spielman–Srivastava](https://arxiv.org/abs/1304.4132v2).
That paper and the IAS past-visitor link for Srivastava are recorded separately
in the literature map; these small examples do not reproduce its proof.
