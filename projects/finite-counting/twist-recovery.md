# Which twists give the same conflict-count distribution?

Fix a multiset of positive path lengths between two terminals as in [the binary path model](binary-path-law.md). Let a path have sign + or - according to its twist parity. Only the total number of conflicts is observed; the paths carrying those conflicts are not observed.

**Recovery criterion.** Two assignments give the same law if and only if one can be obtained from the other at the level of path signs by permuting paths of equal length and, optionally, negating every sign. Individual edge bits within a path are not recoverable.

For signs s_i and lengths l_i define E_s(x) by summing the monomials product(s_i) times x raised to the total length, over even subsets of paths. The previous note gives the probability generating function as ((1+z)/2)^m E_s((z-1)/(z+1)). This substitution is invertible over rational functions, so it suffices to compare E.

**Proof.** Compare signs s and t in any fixed ordering of the lengths. Write D for the paths on which they differ and U for the others. For a set B of paths let O_B denote the analogous sum over its odd subsets, using the signs s. Then

    E_s - E_t = 2 O_D O_U.

Indeed the surviving subsets choose oddly many paths from D and, to have even total size, oddly many from U. This factorization prevents accidental cancellation between the two groups.

The polynomial O_B is zero exactly when positive and negative signs balance at every length in B. To see this, twice O_B is the difference between the products of (1+s_i x^l_i) and (1-s_i x^l_i) over B. Cancel opposite-sign pairs of equal length: they contribute the same factor (1-x^(2l)) on each side. If anything remains, let j be its shortest length. The degree-j coefficient of the remaining difference is twice the nonzero signed count at j. The canceled factors have constant term one, so they do not change this first difference.

If O_D is zero, flipping D preserves the counts of both signs at every length; the assignments agree up to permutation. If O_U is zero, compare s to the global negative of t instead: they now differ exactly on U. Conversely permutations do not change E, and global negation preserves every even product. This proves the criterion.

**Which moment distinguishes two inequivalent assignments?** In each of D and U let j_D,j_U be the shortest lengths with nonzero signed imbalance, and b_D,b_U the corresponding signed counts. The difference E_s-E_t first appears at degree h=j_D+j_U with coefficient 2 b_D b_U. Expanding the probability generating functions at z=1, the first differing binomial moment is therefore of order h, with difference 2^(1-h) b_D b_U. This allows arbitrarily many twists in either assignment. For instance on lengths 2,2,3,4 compare (+++-) with (-+++). D contains lengths 2,4 with opposite signs and U contains lengths 2,3 with positive signs. The first differing order is four, with difference 1/8.

**Finite check.** [twist_recovery.py](twist_recovery.py) computes distributions independently by fixing the terminal colors and counting compatible choices on each path. It groups assignments by their full distributions and also by the two stated symmetries, checking both directions. For two through six paths of lengths one through four, with at most one unit path, this covers 135 length multisets and 4,852 assignments, yielding 929 equivalence classes summed over the length multisets. The argument assumes the lengths are supplied. No priority claim is made.


On all 100,976 unordered pairs of assignments with different laws in this range the same independent distributions also confirm the first differing moment order and its signed difference.
