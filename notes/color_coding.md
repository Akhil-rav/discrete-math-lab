# Vertex color-coding: a combinatorics-to-algorithms bridge

**Status:** implementation/reproduction of a standard method; no novelty claim.

Alon, Yuster, and Zwick's [Color-coding](https://www.math.tau.ac.il/~nogaa/PDFS/col5.pdf),
§3 and Lemma 3.1, motivates `src/color_coding.py`. Alon's author manuscript
lists IAS and Tel Aviv University. These are **vertex** colors; the anti-Ramsey
matching searches elsewhere in this lab color **edges**.

Here k means a number of vertices, so the desired path has length k−1.
For a fixed coloring, D[S,v] is true if a colorful path ends at v and uses exactly
the color set S. Initialize singleton paths. For each neighbor w of v whose color
is outside S, extend to D[S∪{c(w)},w]. Each extension adds a color, so processing
masks in increasing order is valid. Repeated vertices would repeat a color;
every reported witness is therefore simple.

The implementation stores one path per reachable state. Equal states can share
future extensions because a new color rules out every previously used vertex.
With explicit tuple copying, the teaching implementation takes
O(k 2^k (|V|+|E|)) time and O(k 2^k |V|) space. It is not an implementation of
the paper's entire algorithm collection or its perfect-hash derandomization.

For a fixed k-vertex path, independent uniform colors from a palette of size k
make it colorful with probability k!/k^k: there are k! injective assignments
among k^k assignments on its vertices. If any such path exists, one color-coding
trial therefore finds some path with at least this probability. A failed trial
does not certify that no uncolored path exists.

Our experiment enumerates **all** assignments on every labeled simple undirected
graph of order 1 through 4, for each 1≤k≤n. It compares the DP with independent
ordered-vertex enumeration, verifies witnesses, and calculates exact success
fractions. No random sampling or seed is involved. This finite audit does not
replace the general correctness argument above.
