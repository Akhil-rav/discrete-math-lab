"""Fixed cube model, exact color partitions, and its 48 graph automorphisms."""

from itertools import permutations

from src.color_patterns import normalize


CUBE_EDGES = tuple((i, j) for i in range(4) for j in range(4) if i != j)


def partitions_into_blocks(length, blocks):
    """All restricted-growth strings with exactly `blocks` classes, once each.

    This iterator only prunes impossible class counts, never rainbow constraints.
    Bounds prevent accidental unbounded use in this finite experiment.
    """
    if not 1 <= blocks <= length <= 12:
        raise ValueError('Need 1 <= blocks <= length <= 12.')
    colors = [0]*length

    def visit(position, used):
        if used > blocks or used + length-position < blocks:
            return
        if position == length:
            yield tuple(colors)
            return
        for color in range(min(used+1, blocks)):
            colors[position] = color
            yield from visit(position+1, max(used, color+1))

    yield from visit(1, 1)


def cube_edge_actions():
    """Image of each edge index under simultaneous S4 relabeling and part swap."""
    index = {edge: i for i, edge in enumerate(CUBE_EDGES)}
    return tuple(tuple(index[(p[v], p[u]) if swap else (p[u], p[v])]
                       for u, v in CUBE_EDGES)
                 for p in permutations(range(4)) for swap in (False, True))


def transform_partition(colors, action):
    """Apply a source-index -> image-index permutation, then forget color names."""
    if len(colors) != len(action) or sorted(action) != list(range(len(action))):
        raise ValueError('Action must permute the color positions.')
    image = [None]*len(colors)
    for source, destination in enumerate(action):
        image[destination] = colors[source]
    return normalize(image)


def cube_orbit(colors):
    if len(colors) != 12:
        raise ValueError('A cube coloring has 12 edge positions.')
    return {transform_partition(colors, a) for a in cube_edge_actions()}
