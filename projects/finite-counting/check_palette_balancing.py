"""Exhaust strict two-color balancing on families of targets on four positions."""
from collections import Counter
from itertools import combinations, product
from math import prod


def color_patterns(targets, weights):
    patterns = Counter()
    for colors in product(range(len(weights)), repeat=4):
        weight = prod(weights[i] for i in colors)
        if weight:
            pattern = sum(1 << j for j, target in enumerate(targets)
                          if len({colors[i] for i in target}) == len(target))
            patterns[pattern] += weight
    return patterns


if __name__ == "__main__":
    targets = [s for k in range(2, 5) for s in combinations(range(4), k)]
    families = range(1, 1 << len(targets))
    tested = 0
    for outside in [(0, 0), (2, 0), (2, 1)]:
        for pair in [(4, 0), (3, 1)]:
            before = color_patterns(targets, pair + outside)
            after = color_patterns(targets, (2, 2) + outside)
            for family in families:
                delta = (sum(w for hits, w in after.items() if hits & family)
                         - sum(w for hits, w in before.items() if hits & family))
                k = min(len(s) for j, s in enumerate(targets) if (1 << j) & family)
                strict = sum(w > 0 for w in outside) >= k-2
                assert delta > 0 if strict else delta == 0
                tested += 1
    print(tested, "family/palette comparisons passed")
