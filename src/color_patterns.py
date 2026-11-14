"""Canonical set partitions and automorphisms of square edge-color arrays."""

from itertools import permutations


def normalize(colors):
    """Rename colors in order of first appearance; preserve equality exactly."""
    names = {}
    return tuple(names.setdefault(c, len(names)) for c in colors)


def square_orbit(colors, n):
    """Row/column permutations, optional transpose, and color renaming.

    This is the full automorphism action of K_{n,n} for n >= 2.
    Color names are quotiented out after each vertex transformation.
    """
    if n < 2 or len(colors) != n * n:
        raise ValueError("Need n >= 2 and an n*n array.")
    orbit = set()
    for rows in permutations(range(n)):
        for cols in permutations(range(n)):
            orbit.add(normalize(colors[i*n+j] for i in rows for j in cols))
            orbit.add(normalize(colors[j*n+i] for i in rows for j in cols))
    return orbit


def canonical_square(colors, n):
    return min(square_orbit(colors, n))
