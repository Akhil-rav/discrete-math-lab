# Testing one repeated color: an intersection criterion

Let M be a nonempty finite family of equal-size subsets of a ground set with at least two elements, and let T be a nonempty subfamily. Write K(U) for the intersection of the members of U. With exactly one fewer color than elements there is just one repeated pair. T detects every rainbow witness in M precisely when

    every two-element subset of K(T) is contained in K(M).

Indeed a repeated pair defeats every test exactly when it lies in the intersection of the tests. It defeats every possible witness exactly when it lies in the global intersection. Consequently a test list works if and only if its common intersection has size at most one or equals the global intersection. This applies to arbitrary set families; it does not require bipartiteness.

For any single member of size at least two, the singleton test list therefore fails unless that member equals the global intersection. For distinct equal-size members this is impossible. Two tests suffice precisely when some two members meet in at most one element or meet exactly in the global intersection. Here one assumes there are at least two distinct members of size at least two; otherwise the singleton exception applies. For example the alternating perfect matchings of an even cycle are disjoint. This gives a direct two-test certificate without enumerating partitions.

Computational form: index each member by a bit position. For each element store the mask of members containing it. A repeated pair excludes the intersection of its two masks; its complement (relative to the full family) is exactly the mask of rainbow witnesses. Discard zero complements, since that coloring has no witness. A test list must intersect each remaining mask. This gives a small exact hitting-set instance and a way to check the criterion independently.
