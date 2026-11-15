"""Minimum color deficit as an exact weighted cover of target events."""


def minimum_cover(edge_count, targets):
    """Return a minimum-deficit avoiding coloring and a checkable cost table.

    A block B costs |B|-1 and covers each target meeting B at least twice.
    Overlapping chosen blocks are merged before constructing the coloring.
    Limits: 2..13 edge positions, 1..9 distinct targets, each of size >=2.
    """
    if type(edge_count) is not int or not 2 <= edge_count <= 13:
        raise ValueError("Need 2..13 edge positions.")
    targets = tuple(tuple(target) for target in targets)
    if not 1 <= len(targets) <= 9:
        raise ValueError("Need 1..9 targets.")
    if any(
        len(target) < 2
        or len(target) != len(set(target))
        or any(type(i) is not int or not 0 <= i < edge_count for i in target)
        for target in targets
    ):
        raise ValueError("Targets need distinct valid positions and size >=2.")
    if len({frozenset(target) for target in targets}) != len(targets):
        raise ValueError("Targets must be distinct.")
    masks = [sum(1 << i for i in target) for target in targets]
    cheapest = {}
    for block in range(1 << edge_count):
        size = block.bit_count()
        if size < 2:
            continue
        coverage = sum(
            1 << j
            for j, target in enumerate(masks)
            if (block & target).bit_count() >= 2
        )
        candidate = (size - 1, block)
        if coverage and candidate < cheapest.get(coverage, (edge_count, 0)):
            cheapest[coverage] = candidate
    full = (1 << len(targets)) - 1
    costs = [0] * (full + 1)
    for covered in range(full - 1, -1, -1):
        costs[covered] = min(
            cost + costs[covered | coverage]
            for coverage, (cost, _) in cheapest.items()
            if covered | coverage != covered
        )
    chosen = []
    covered = 0
    while covered != full:
        _, coverage, block = min(
            (cost + costs[covered | coverage], coverage, block)
            for coverage, (cost, block) in cheapest.items()
            if covered | coverage != covered
        )
        chosen.append(block)
        covered |= coverage
    parent = list(range(edge_count))

    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i

    blocks = [tuple(i for i in range(edge_count) if block >> i & 1) for block in chosen]
    for block in blocks:
        for i in block[1:]:
            parent[root(i)] = root(block[0])
    names = {}
    witness = [names.setdefault(root(i), len(names)) for i in range(edge_count)]
    if edge_count - len(set(witness)) != costs[0]:
        raise RuntimeError("Merging the optimal cover changed its minimum deficit.")
    return {
        "minimum_deficit": costs[0],
        "maximum_avoiding_colors": edge_count - costs[0],
        "witness": witness,
        "cover_blocks": blocks,
        "cheapest_blocks": [
            {
                "coverage": coverage,
                "cost": cost,
                "block": [i for i in range(edge_count) if block >> i & 1],
            }
            for coverage, (cost, block) in sorted(cheapest.items())
        ],
        "remaining_costs": costs,
        "subsets_examined": (1 << edge_count) - edge_count - 1,
    }
