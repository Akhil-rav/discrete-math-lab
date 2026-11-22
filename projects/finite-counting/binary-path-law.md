# When can a count detect a twisted path?

Take internally disjoint paths of lengths l_i between two terminals, with m edges in total. Color vertices with independent fair bits. An edge has a prescribed bit b and records a conflict when its endpoint bits have XOR equal to b. Write X for the number of conflicts and t_i for the XOR of the prescribed bits along path i.

For each even subset I of paths put h_I=sum of their lengths and s_I=(-1) raised to the sum of their t_i. Then

    2^m E[z^X] = sum_I s_I (z-1)^h_I (z+1)^(m-h_I).

Indeed, for endpoint signs U,V in {-1,1} a single factor is ((z+1)+(z-1)(-1)^b UV)/2. Expanding the product and averaging kills every edge subset with an odd degree at any vertex. Even degree at internal vertices forces a whole path or none; the terminal condition requires evenly many paths. This is the binary even-subgraph expansion, specialized to parallel paths. In coding terms the surviving supports are the binary cycle space; no general coding identity is claimed as new.

**First detectable moment.** Start with all bits zero and flip one edge on path i. For at least two paths, let h be l_i plus the shortest other path length, and let a count the other paths attaining that shortest length. In the difference (untwisted minus twisted), only even subsets containing i contribute, each with multiplier two. The shortest such subsets are exactly the a path pairs. At z=1 the difference thus vanishes to order exactly h, with leading coefficient a times 2^(1-h). Hence the binomial moments E[choose(X,j)] agree for every j<h and differ by exactly a times 2^(1-h) at j=h. This is a distributional statement for a fixed assignment, not a minimum over assignments.

Example: lengths 2,3,4, twisting the longest path. The first five moments agree, although the distributions differ. The sixth binomial moment drops by 1/32. [Direct enumeration](binary_path_law.py) compares every coefficient for 72 signed path systems.


[Recovery from the entire distribution](twist-recovery.md) compares two arbitrary sign assignments, including when several paths have the same length.
