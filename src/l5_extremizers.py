"""The fifteen L5 partitions from the direct block-classification proof."""

from itertools import product

from src.color_patterns import normalize


def extremal_block_families(k=5):
    """The fifteen terminal patterns for a ladder with k >= 5 columns."""
    if not isinstance(k, int) or k < 5:
        raise ValueError("The terminal classification starts at five columns.")
    last = k - 1
    rails = [(k + i, 2 * k - 1 + i) for i in range(last)]
    for x, y in product(rails[0], rails[-1]):
        yield ((0, last, x, y),)
    forms = (
        ((0, 1), 1, 0),
        ((last - 1, last), last - 2, last - 1),
        ((0, last), 0, last - 1),
        ((0, last), last - 1, 0),
    )
    for rungs, gap, pair_gap in forms:
        for x in rails[gap]:
            yield (rungs + (x,), rails[pair_gap])
    yield ((0, 1), rails[0], rails[1])
    yield ((0, last), rails[0], rails[-1])
    yield ((last - 1, last), rails[-2], rails[-1])


def extremal_partitions():
    """Give every position outside the repeated blocks a singleton color."""
    for blocks in extremal_block_families():
        colors = list(range(13))
        for block in blocks:
            for i in block:
                colors[i] = min(block)
        yield normalize(colors)
