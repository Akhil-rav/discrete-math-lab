"""Subset dynamic programming for vertex-colorful simple paths (AYZ)."""


def colorful_path(adjacency, colors, k):
    """Return a path on k vertices using all k colors, or None.

    Vertices are 0..n-1; colors are integers in 0..k-1. Directed and
    undirected adjacency lists are supported. A color mask prevents repeats.
    Witnesses are retained for inspection; time O(k 2^k (n+m)), space O(k2^k n)
    including the explicit path tuples. This is a teaching implementation.
    """
    n = len(adjacency)
    if k < 1 or len(colors) != n or any(c not in range(k) for c in colors):
        raise ValueError("Need k >= 1 and one color in range(k) per vertex.")
    if any(v not in range(n) for row in adjacency for v in row):
        raise ValueError("Neighbor outside vertex range.")
    states = {(1 << colors[v], v): (v,) for v in range(n)}
    full = (1 << k) - 1
    for mask in range(1, full + 1):
        for v in range(n):
            path = states.get((mask, v))
            if path is None:
                continue
            if mask == full:
                return path
            for w in adjacency[v]:
                bit = 1 << colors[w]
                if not mask & bit:
                    states.setdefault((mask | bit, w), path + (w,))
    return None
