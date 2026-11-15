"""Fixed-edge models and the proved extremal construction for even-cycle unions."""

from itertools import combinations

from src.color_patterns import normalize


def cycle_union(half_lengths):
    """Return edges and the two alternating edge-index sets of each component.

    Component i has length 2*half_lengths[i]. Vertices and edges are numbered
    consecutively, with edges in cyclic order inside each fixed component.
    Components and edge positions are not identified by graph symmetry.
    """
    half_lengths = tuple(half_lengths)
    if not half_lengths or any(type(n) is not int or n < 2 for n in half_lengths):
        raise ValueError("Need a nonempty tuple of integer half-lengths >= 2.")
    edges, alternating = [], []
    offset = 0
    for n in half_lengths:
        length = 2 * n
        edges.extend((offset + j, offset + (j + 1) % length) for j in range(length))
        alternating.append(
            (
                tuple(range(offset, offset + length, 2)),
                tuple(range(offset + 1, offset + length, 2)),
            )
        )
        offset += length
    return tuple(edges), tuple(alternating)


def extremal_partitions(half_lengths):
    """All proved extremizers, once each, normalized by first color appearance.

    Choose one component, a pair in each of its alternating matchings, and
    leave all other edges singleton. The proof is in notes/cycle_extremizers.md.
    This is a construction, not an exhaustive-search oracle.
    """
    edges, alternating = cycle_union(half_lengths)
    for first, second in alternating:
        for a, b in combinations(first, 2):
            for c, d in combinations(second, 2):
                colors = list(range(len(edges)))
                colors[b] = colors[a]
                colors[d] = colors[c]
                yield normalize(colors)
