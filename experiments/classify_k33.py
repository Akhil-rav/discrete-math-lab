"""Exhaust all B_9 partitions, then classify extremizers by graph symmetry.

Run: python -m experiments.classify_k33
"""

import json
from collections import Counter

from experiments.rainbow_complete_bipartite import (
    has_rainbow_perfect_matching, normalized_colorings,
)
from src.color_patterns import canonical_square, square_orbit


def run():
    extremal = []
    best = -1
    checked = 0
    for colors in normalized_colorings(9):
        checked += 1
        if has_rainbow_perfect_matching(3, colors):
            continue
        count = max(colors) + 1
        if count > best:
            best, extremal = count, [colors]
        elif count == best:
            extremal.append(colors)
    classes = Counter(canonical_square(c, 3) for c in extremal)
    population = set(extremal)
    records = []
    for representative, size in sorted(classes.items()):
        orbit = square_orbit(representative, 3)
        if not orbit <= population or len(orbit) != size:
            raise RuntimeError("Orbit closure or size check failed.")
        if 72 % size:
            raise RuntimeError("Orbit size must divide |Aut(K33)| = 72.")
        records.append({
            "representative": list(representative), "orbit_size": size,
            "stabilizer_size": 72 // size,
            "color_class_sizes": sorted(Counter(representative).values()),
        })
    return {"patterns_checked": checked, "maximum_avoiding_colors": best,
            "extremal_patterns": len(extremal), "symmetry_classes": records}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
