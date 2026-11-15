"""Labeled ladder graphs and their matching and symmetry actions."""

from itertools import permutations


def ladder_edges(k):
    """Rungs first, then top and bottom rails; vertices are row*k + column."""
    if not isinstance(k, int) or not 2 <= k <= 5:
        raise ValueError("This finite study supports 2 <= k <= 5.")
    return (
        tuple((i, k + i) for i in range(k))
        + tuple((i, i + 1) for i in range(k - 1))
        + tuple((k + i, k + i + 1) for i in range(k - 1))
    )


def bipartite_edges(k):
    edges = ladder_edges(k)
    left = [v for v in range(2 * k) if (v // k + v % k) % 2 == 0]
    right = [v for v in range(2 * k) if v not in left]
    li = {v: i for i, v in enumerate(left)}
    ri = {v: i for i, v in enumerate(right)}
    return tuple((li[u], ri[v]) if u in li else (li[v], ri[u]) for u, v in edges)


def ladder_matchings(k):
    """Scan columns: take one rung, or the two rails across the next gap."""
    ladder_edges(k)

    def visit(column):
        if column == k:
            yield ()
            return
        for rest in visit(column + 1):
            yield tuple(sorted((column,) + rest))
        if column + 1 < k:
            for rest in visit(column + 2):
                yield tuple(sorted((k + column, 2 * k - 1 + column) + rest))

    return tuple(sorted(visit(0)))


def ladder_actions(k):
    """Full edge automorphism group: D4 for L2, two reflections for L3 through L5."""
    edges = ladder_edges(k)
    index = {frozenset(edge): i for i, edge in enumerate(edges)}
    if k == 2:
        maps = permutations(range(4))
    else:
        maps = (
            tuple(
                (row ^ swap) * k + (k - 1 - col if reverse else col)
                for row in range(2)
                for col in range(k)
            )
            for swap in (0, 1)
            for reverse in (False, True)
        )
    actions = set()
    for mapping in maps:
        image = [frozenset((mapping[u], mapping[v])) for u, v in edges]
        if all(edge in index for edge in image):
            actions.add(tuple(index[edge] for edge in image))
    return tuple(sorted(actions))
