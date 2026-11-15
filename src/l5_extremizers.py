"""The fifteen L5 partitions from the direct block-classification proof."""

from itertools import product

from src.color_patterns import normalize


def extremal_block_families():
    """Nonsingleton classes, using rung–top–bottom edge positions."""
    rails = [(5 + i, 9 + i) for i in range(4)]
    for x, y in product(rails[0], rails[3]):
        yield ((0, 4, x, y),)
    forms = (
        ((0, 1), 1, 0),
        ((3, 4), 2, 3),
        ((0, 4), 0, 3),
        ((0, 4), 3, 0),
    )
    for rungs, gap, pair_gap in forms:
        for x in rails[gap]:
            yield (rungs + (x,), rails[pair_gap])
    yield ((0, 1), rails[0], rails[1])
    yield ((0, 4), rails[0], rails[3])
    yield ((3, 4), rails[2], rails[3])


def extremal_partitions():
    """Give every position outside the repeated blocks a singleton color."""
    for blocks in extremal_block_families():
        colors = list(range(13))
        for block in blocks:
            for i in block:
                colors[i] = min(block)
        yield normalize(colors)
