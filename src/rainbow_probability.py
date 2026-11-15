"""Exact probabilities for independent uniform edge colors on a fixed host.

The palette has q available labeled colors; using every color is not required.
Input partition histograms count avoiding partitions with fixed edge positions.
"""

from fractions import Fraction
from itertools import combinations


def falling_factorial(q, k):
    if not isinstance(q, int) or not isinstance(k, int) or q < 0 or k < 0:
        raise ValueError("Need nonnegative integer q and k.")
    if k > q:
        return 0
    value = 1
    for i in range(k):
        value *= q - i
    return value


def rainbow_probability(edge_count, avoiding_histogram, q):
    """Probability of at least one rainbow target, from avoiding block counts."""
    if (
        not isinstance(edge_count, int)
        or edge_count < 1
        or not isinstance(q, int)
        or q < 1
    ):
        raise ValueError("Need positive integer edge count and palette size.")
    if any(
        not isinstance(k, int)
        or not 1 <= k <= edge_count
        or not isinstance(count, int)
        or count < 0
        for k, count in avoiding_histogram.items()
    ):
        raise ValueError("Invalid avoiding-partition histogram.")
    avoiding = sum(
        count * falling_factorial(q, k) for k, count in avoiding_histogram.items()
    )
    if avoiding > q**edge_count:
        raise ValueError("Avoiding count exceeds the full coloring space.")
    return 1 - Fraction(avoiding, q**edge_count)


def matching_moments(matchings, q):
    """Return E[X], E[X^2] for the number of rainbow perfect matchings.

    Matching sets must be distinct, nonempty, and of equal size. Their edges
    are positions with independently uniform colors. The pair formula depends
    only on the number of shared positions.
    """
    if not isinstance(q, int) or q < 1:
        raise ValueError("Need a positive integer palette size.")
    matchings = tuple(frozenset(m) for m in matchings)
    if not matchings or len(set(matchings)) != len(matchings):
        raise ValueError("Need a nonempty family of distinct matchings.")
    n = len(matchings[0])
    if not n or any(len(m) != n for m in matchings):
        raise ValueError("Matchings must have the same positive size.")
    single = Fraction(falling_factorial(q, n), q**n)
    first = len(matchings) * single
    second = first
    if q < n:
        return first, second
    for a, b in combinations(matchings, 2):
        shared = len(a & b)
        joint = Fraction(
            falling_factorial(q, n) * falling_factorial(q - shared, n - shared),
            q ** (2 * n - shared),
        )
        second += 2 * joint
    return first, second


def probability_bounds(matchings, q):
    first, second = matching_moments(matchings, q)
    lower = first * first / second if second else Fraction(0)
    return first, second, lower, min(Fraction(1), first)
