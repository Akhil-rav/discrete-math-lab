"""Checks for the ladder test-family note. Standard library only.

  python -m experiments.ladder_thresholds
Edges of L_k: rungs r_i, and for each gap i the two rails ("u", i), ("l", i).
A perfect matching is a set J of pairwise nonconsecutive gaps.
"""
from itertools import combinations


def gap_sets(k):
    return [s for s in range(1 << (k - 1)) if not s & (s >> 1)]


def matching(k, s):
    edges = set()
    for c in range(k):
        if not ((s >> c) & 1 or (c and (s >> (c - 1)) & 1)):
            edges.add(("r", c))
    for g in range(k - 1):
        if (s >> g) & 1:
            edges |= {("u", g), ("l", g)}
    return frozenset(edges)


def rainbow(m, classes):
    return all(len(m & c) <= 1 for c in classes)


def jacobsthal(n):
    return (2 ** n - (-1) ** n) // 3


def deficit_two_families(k):
    """Triples passing the criterion of Lemma 2, found by direct search."""
    ms = [matching(k, s) for s in gap_sets(k)]
    good = 0
    for a, b, c in combinations(ms, 3):
        ab, ac, bc = a & b, a & c, b & c
        if max(len(ab), len(ac), len(bc)) > 1:
            continue
        if ab and ac and bc and not ab == ac == bc:
            continue
        good += 1
    return good


def brute_force_deficit_two(k):
    """Independent check: test every triple against every deficit-two colouring."""
    ms = [matching(k, s) for s in gap_sets(k)]
    edges = sorted(set().union(*ms))
    colourings = [[frozenset(t)] for t in combinations(edges, 3)]
    for p in combinations(edges, 2):
        for q in combinations(edges, 2):
            if p < q and not set(p) & set(q):
                colourings.append([frozenset(p), frozenset(q)])
    masks = []
    for cl in colourings:
        masks.append(sum(1 << i for i, m in enumerate(ms) if rainbow(m, cl)))
    assert all(masks), "some deficit-two colouring has no rainbow matching"
    return sum(
        all(mask & (1 << a | 1 << b | 1 << c) for mask in masks)
        for a, b, c in combinations(range(len(ms)), 3)
    ), any(
        all(mask & (1 << a | 1 << b) for mask in masks)
        for a, b in combinations(range(len(ms)), 2)
    )


def check_saturation(k):
    """Each matching is the only rainbow one in a colouring of deficit k-1."""
    sets = gap_sets(k)
    ms = {s: matching(k, s) for s in sets}
    for s in sets:
        classes = []
        for g in range(k - 1):
            if (s >> g) & 1:
                classes.append(frozenset({("r", g), ("r", g + 1)}))
            else:
                classes.append(frozenset({("u", g), ("l", g)}))
        assert sum(len(c) - 1 for c in classes) == k - 1
        assert [t for t in sets if rainbow(ms[t], classes)] == [s]


def check_lower_bound(k):
    """If T_i were inside T_j, the three classes below defeat the list."""
    sets = gap_sets(k)
    ms = {s: matching(k, s) for s in sets}
    for i in range(1, k - 1):
        for j in range(1, k - 1):
            if i == j:
                continue
            classes = [frozenset({("u", i - 1), ("l", i - 1)}),
                       frozenset({("u", i), ("l", i)}),
                       frozenset({("r", i), ("r", j)})]
            g = j if j > i else j - 1
            assert rainbow(ms[1 << g], classes)
            for s in sets:
                if rainbow(ms[s], classes):
                    # every surviving matching has column i free and column j covered
                    assert ("r", i) in ms[s] and ("r", j) not in ms[s]


def check_markov_bound(k, d=3):
    """Exact least avoidance probability under the chain of Theorem 5."""
    from fractions import Fraction
    sets = gap_sets(k)
    weight = {}
    for s in sets:
        p = Fraction(1, 3) if s & 1 else Fraction(2, 3)
        for g in range(1, k - 1):
            if not (s >> (g - 1)) & 1:
                p *= Fraction(1, 2)
        weight[s] = p
    assert sum(weight.values()) == 1
    edges = sorted(set().union(*(matching(k, s) for s in sets)))
    least = min(
        total for f in combinations(edges, d)
        if (total := sum(w for s, w in weight.items() if not matching(k, s) & set(f)))
    )
    assert least >= Fraction(4, 3) / 4 ** d
    return least


if __name__ == "__main__":
    for k in range(3, 13):
        n = deficit_two_families(k)
        assert n == jacobsthal(k - 2), (k, n)
        print(f"k={k:2d}: optimal three-test families = {n} = J_{k-2}")
    for k in range(3, 8):
        count, two_suffice = brute_force_deficit_two(k)
        assert count == jacobsthal(k - 2) and not two_suffice
        print(f"k={k}: brute force over all deficit-two colourings agrees; no pair suffices")
    for k in range(3, 13):
        check_saturation(k)
    print("saturation colourings verified for k=3..12")
    for k in range(4, 13):
        check_lower_bound(k)
    print("antichain colourings verified for k=4..12")
    for k in range(4, 10):
        print(f"k={k}: least avoidance probability {check_markov_bound(k)} >= 1/48")
