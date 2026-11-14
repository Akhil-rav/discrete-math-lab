"""Exact small anti-van der Waerden numbers, using set-partition enumeration.

Run: python -m experiments.rainbow_progressions
No 3-AP: use the literature convention aw(S,3)=|S|+1.
"""

import json

from experiments.rainbow_complete_bipartite import normalized_colorings
from src.arithmetic_progressions import (
    contains_rainbow_three_ap, group_three_aps, interval_three_aps,
)


def search(n, progressions):
    best, witness, checked = -1, (), 0
    for colors in normalized_colorings(n):
        checked += 1
        if contains_rainbow_three_ap(colors, progressions):
            continue
        count = max(colors) + 1
        if count > best:
            best, witness = count, colors
    return {"order": n, "three_ap_sets": len(progressions),
            "partitions_checked": checked, "maximum_avoiding_colors": best,
            "aw": best + 1, "witness": list(witness)}


def run():
    intervals = {str(n): search(n, interval_three_aps(n)) for n in range(3, 10)}
    groups = {}
    for moduli in [(n,) for n in range(3, 10)] + [(2, 2), (2, 4), (2, 2, 2)]:
        elements, aps = group_three_aps(moduli)
        groups["x".join(map(str, moduli))] = search(len(elements), aps)
    return {"intervals": intervals, "cyclic_products": groups}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
