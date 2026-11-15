"""Check a cover certificate without calling the optimization routine."""

from itertools import combinations


def check_certificate(edge_count, targets, certificate):
    """Rebuild every block by combinations, check every cost state and the witness.

    Inputs have the same finite domain as minimum_cover; no claim follows from
    a partial cost table. Incorrect tables or witnesses raise ValueError.
    """
    entries = tuple(tuple(target) for target in targets)
    if any(len(target) != len(set(target)) for target in entries):
        raise ValueError("Target positions must be distinct.")
    targets = tuple(frozenset(target) for target in entries)
    if (
        type(edge_count) is not int
        or not 2 <= edge_count <= 13
        or not 1 <= len(targets) <= 9
        or len(set(targets)) != len(targets)
        or any(
            len(t) < 2 or any(type(i) is not int or not 0 <= i < edge_count for i in t)
            for t in targets
        )
    ):
        raise ValueError("Invalid finite cover problem.")
    cheapest = {}
    for size in range(2, edge_count + 1):
        for block in combinations(range(edge_count), size):
            hits = [
                j
                for j, target in enumerate(targets)
                if len(target.intersection(block)) >= 2
            ]
            coverage = sum(2**j for j in hits)
            candidate = (size - 1, sum(2**i for i in block))
            if coverage and candidate < cheapest.get(coverage, (edge_count, 0)):
                cheapest[coverage] = candidate
    expected = [
        {
            "coverage": coverage,
            "cost": cost,
            "block": [i for i in range(edge_count) if mask // (2**i) % 2],
        }
        for coverage, (cost, mask) in sorted(cheapest.items())
    ]
    if certificate["cheapest_blocks"] != expected:
        raise ValueError("Incomplete or incorrect block coverage table.")
    full = 2 ** len(targets) - 1
    values = certificate["remaining_costs"]
    if (
        len(values) != full + 1
        or values[full] != 0
        or any(
            type(value) is not int or not 0 <= value < edge_count for value in values
        )
    ):
        raise ValueError("Invalid cost states.")
    for covered in range(full):
        candidates = [
            cost + values[covered | coverage]
            for coverage, (cost, _) in cheapest.items()
            if covered | coverage != covered
        ]
        if values[covered] != min(candidates):
            raise ValueError("A cost recurrence fails.")
    deficit = certificate["minimum_deficit"]
    witness = certificate["witness"]
    if (
        deficit != values[0]
        or certificate["maximum_avoiding_colors"] != edge_count - deficit
        or len(witness) != edge_count
        or len(set(witness)) != edge_count - deficit
        or any(len({witness[i] for i in target}) == len(target) for target in targets)
    ):
        raise ValueError("The claimed optimum or coloring witness fails.")
    blocks = certificate["cover_blocks"]
    if (
        any(
            len(block) < 2
            or len(block) != len(set(block))
            or any(type(i) is not int or not 0 <= i < edge_count for i in block)
            or len({witness[i] for i in block}) != 1
            for block in blocks
        )
        or sum(len(block) - 1 for block in blocks) != deficit
        or any(
            not any(len(target.intersection(block)) >= 2 for block in blocks)
            for target in targets
        )
        or certificate["subsets_examined"] != 2**edge_count - edge_count - 1
    ):
        raise ValueError("The covering witness or subset count fails.")
    return True
