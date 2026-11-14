"""Exact partition search for rainbow-perfect-matching avoidance on small hosts."""

from collections import Counter
from functools import lru_cache
from itertools import permutations


@lru_cache(None)
def completions(remaining, colors):
    """Number of restricted-growth continuations of a prefix with `colors` blocks."""
    if remaining == 0:
        return 1
    return colors * completions(remaining-1, colors) + completions(remaining-1, colors+1)


def matching_constraints(n, edges):
    """All perfect matchings as edge indices, via permutation enumeration."""
    if n < 2 or len(edges) != len(set(edges)):
        raise ValueError('Need n>=2 and no duplicate edges.')
    if any(u not in range(n) or v not in range(n) for u, v in edges):
        raise ValueError('Edges must be pairs from range(n) x range(n).')
    index = {edge: i for i, edge in enumerate(edges)}
    return tuple(tuple(sorted(index[i, p[i]] for i in range(n)))
                 for p in permutations(range(n))
                 if all((i, p[i]) in index for i in range(n)))


def avoiding_partitions(n, edges):
    """Exhaustive histogram with early rejection and exact subtree accounting.

    Edge order is supplied explicitly. Color names alone are quotiented out.
    At most 12 edges are allowed; this is a bounded educational solver.
    A completed rainbow matching in a prefix persists under every extension.
    Rejected subtrees are counted using `completions`, not treated as one case.
    """
    edges = tuple(edges)
    constraints = matching_constraints(n, edges)
    m = len(edges)
    if not 1 <= m <= 12 or not constraints:
        raise ValueError('Need 1..12 edges and at least one perfect matching.')
    ending = [[] for _ in edges]
    for matching in constraints:
        ending[max(matching)].append(matching)
    histogram, witnesses = Counter(), {}
    rejected = 0
    colors = [0] * m

    def visit(position, blocks):
        nonlocal rejected
        if position == m:
            histogram[blocks] += 1
            witnesses.setdefault(blocks, tuple(colors))
            return
        for color in range(blocks+1):
            colors[position] = color
            new_blocks = max(blocks, color+1)
            if any(len({colors[i] for i in matching}) == n for matching in ending[position]):
                rejected += completions(m-position-1, new_blocks)
            else:
                visit(position+1, new_blocks)

    # Unique normalized first color. No n>=2 matching is complete at this prefix.
    visit(1, 1)
    total = completions(m-1, 1)
    if sum(histogram.values()) + rejected != total:
        raise RuntimeError('Partition coverage failed.')
    best = max(histogram)
    return {'n_per_side': n, 'edges': [list(e) for e in edges],
            'perfect_matchings': len(constraints), 'total_partitions': total,
            'rejected_partitions': rejected,
            'avoiding_histogram': dict(sorted(histogram.items())),
            'maximum_avoiding_colors': best, 'extremal_partitions': histogram[best],
            'witness': list(witnesses[best])}
