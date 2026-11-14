"""Distinct-term 3-AP sets in intervals and products of cyclic groups."""

from itertools import product


def interval_three_aps(n):
    if n < 1:
        raise ValueError("Need n >= 1.")
    return tuple((a, a+d, a+2*d) for a in range(n)
                 for d in range(1, (n-1-a)//2 + 1))


def group_three_aps(moduli):
    """Return (lexicographically ordered elements, distinct 3-AP index sets).

    All a,d are enumerated. Reversal and other presentations of the same
    set are deduplicated. Degenerate progressions are excluded.
    """
    if not moduli or any(m < 2 for m in moduli):
        raise ValueError("Need a nonempty product of cyclic groups of order >= 2.")
    elements = tuple(product(*(range(m) for m in moduli)))
    index = {a: i for i, a in enumerate(elements)}
    progressions = set()
    for a in elements:
        for d in elements:
            terms = {tuple((x+t*y) % m for x, y, m in zip(a, d, moduli))
                     for t in range(3)}
            if len(terms) == 3:
                progressions.add(tuple(sorted(index[x] for x in terms)))
    return elements, tuple(sorted(progressions))


def contains_rainbow_three_ap(colors, progressions):
    return any(len({colors[i] for i in ap}) == 3 for ap in progressions)
