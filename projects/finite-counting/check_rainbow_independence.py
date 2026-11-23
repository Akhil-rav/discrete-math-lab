"""Enumerate colorings on the union of the specified matchings."""
from collections import Counter
from itertools import product
from math import comb, perm, prod


def histogram(matchings, q):
    positions = sorted(set().union(*matchings))
    targets = [[positions.index(edge) for edge in m] for m in matchings]
    counts = Counter()
    for colors in product(range(q), repeat=len(positions)):
        rainbow = sum(len({colors[i] for i in m}) == len(m) for m in targets)
        counts[rainbow] += 1
    return counts


if __name__ == "__main__":
    ladder = [{0, 1, 2}, {0, 3, 4}, {2, 5, 6}]
    for q in range(1, 6):
        counts = histogram(ladder, q)
        a, b = perm(q, 3), q**3
        for j in range(4):
            assert counts[j] * b**3 == q**7 * comb(3, j) * a**j * (b-a)**(3-j)
    bipartite_example = [set(enumerate(p)) for p in
                     [(0, 1, 2, 3), (0, 2, 3, 1), (1, 2, 0, 3)]]
    counts = histogram(bipartite_example, 4)
    assert counts[3] == 4 * 3 * 2 * 2**3
    print("Ladder checks passed for q = 1..5. K4,4 all-rainbow count:", counts[3])

    # Each integer weight counts equally likely tickets for its color.
    weights = (3, 2, 1)
    mass = Counter()
    joint_mass = 0
    for colors in product(range(3), repeat=7):
        hits = [len({colors[i] for i in target}) == 3 for target in ladder]
        tickets = prod(weights[c] for c in colors)
        mass[sum(hits)] += tickets
        if hits[0] and hits[1]:
            joint_mass += tickets
    total = sum(weights)**7
    assert [mass[j]*324 for j in range(4)] == [total*x for x in (191,106,25,2)]
    assert 324*joint_mass == total*11  # 1/36 + 1/162
