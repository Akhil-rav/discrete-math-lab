"""Exact three-path matroid failure probability by weighted rook counting."""
from fractions import Fraction
from math import factorial


# A monomial records (rooks, agreements with identity, agreements with sigma).
# Agreements beyond one in either variable cannot contribute to [z w].
ONE = {(0, 0, 0): 1}
RED = {(1, 0, 0): -1, (1, 1, 0): 1}
BLUE = {(1, 0, 0): -1, (1, 0, 1): 1}
FIXED = {(0, 0, 0): 1, (1, 0, 0): -1, (1, 1, 1): 1}


def add_to(total, terms, scale=1):
    for monomial, coefficient in terms.items():
        total[monomial] = total.get(monomial, 0) + scale * coefficient


def multiply(left, right):
    result = {}
    for (i, a, b), u in left.items():
        for (j, c, d), v in right.items():
            if a + c <= 1 and b + d <= 1:
                key = i + j, a + c, b + d
                result[key] = result.get(key, 0) + u * v
    return result


def path(edges):
    before, current = ONE, ONE
    for edge in edges:
        updated = current.copy()
        add_to(updated, multiply(before, edge))
        before, current = current, updated
    return current


def cycle(length):
    # A permutation cycle gives a bipartite board cycle with 2*length edges.
    edges = [RED, BLUE] * length
    result = path(edges[1:])
    add_to(result, multiply(edges[0], path(edges[2:-1])))
    return result


def failure_rates(max_colors):
    cycles = {size: cycle(size) for size in range(2, max_colors)}
    boards = [ONE]
    for n in range(1, max_colors):
        current = {}
        for size in range(2, n + 1):
            ways = factorial(n - 1) // factorial(n - size)
            add_to(current, multiply(cycles[size], boards[n - size]), ways)
        boards.append(current)
    rates = {}
    for q in range(2, max_colors + 1):
        fixed_boards = multiply(FIXED, boards[q - 1])
        favorable = q * sum(count * factorial(q - rooks)
                            for (rooks, z, w), count in fixed_boards.items()
                            if z == w == 1)
        all_three = Fraction(favorable, factorial(q) ** 2)
        # The constant term at v=z=w=0 counts derangements of q-1 labels.
        one = Fraction(q * boards[q - 1].get((0, 0, 0), 0), factorial(q))
        rates[q] = 3 * (one - 2 * one ** 2 + all_three)
    return rates


if __name__ == '__main__':
    from correspondence_checks import three

    for q, failure in failure_rates(30).items():
        if q <= 6:
            assert failure == three(q)[0]
        if q <= 8 or q % 5 == 0:
            print(q, failure if q <= 8 else f'{float(failure):.10f}')
