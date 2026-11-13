"""Exhaustive rainbow-perfect-matching search for K_{n,n}, n <= 3.

For a fixed graph, the rainbow property depends only on which edges share
a color, not on the names of the colors. Therefore colorings can be
enumerated up to color relabeling using restricted-growth strings.

The experiment computes the largest number of colors appearing in an
edge-coloring of K_{n,n} that contains no rainbow perfect matching.

Run from the repository root:

    python -m experiments.rainbow_complete_bipartite
"""

from __future__ import annotations

from itertools import permutations
from typing import Iterable

from src.edge_coloring import EdgeColoring


def perfect_matchings_complete_bipartite(
    n: int,
) -> Iterable[tuple[tuple[int, int], ...]]:
    """Generate all perfect matchings of K_{n,n}."""

    for permutation in permutations(range(n)):
        yield tuple((i, permutation[i]) for i in range(n))


def has_rainbow_perfect_matching(
    n: int,
    colors: tuple[int, ...],
) -> bool:
    """Check whether the encoded coloring of K_{n,n} has a rainbow PM."""

    coloring = EdgeColoring(
        {
            (i, j): colors[i * n + j]
            for i in range(n)
            for j in range(n)
        }
    )

    return any(
        coloring.is_rainbow(matching)
        for matching in perfect_matchings_complete_bipartite(n)
    )


def normalized_colorings(number_of_edges: int) -> Iterable[tuple[int, ...]]:
    """Enumerate set partitions of the edges via restricted-growth strings.

    Example:
        (0, 0, 1, 2)

    means the first two edges share one color and the final two edges
    receive two new colors.

    This removes redundant copies caused only by renaming colors.
    """

    if number_of_edges == 0:
        yield ()
        return

    coloring = [0] * number_of_edges

    def generate(position: int, maximum_color: int):
        if position == number_of_edges:
            yield tuple(coloring)
            return

        for color in range(maximum_color + 2):
            coloring[position] = color
            yield from generate(position + 1, max(maximum_color, color))

    yield from generate(1, 0)


def exhaustive_search(
    n: int,
) -> tuple[int, int, int, dict[int, int], tuple[int, ...]]:
    """Search every color pattern of K_{n,n}, up to color relabeling.

    Returns:
        patterns_checked,
        maximum_colors_without_rainbow_pm,
        number_of_extremal_patterns,
        avoiding_patterns_by_number_of_colors,
        one_extremal_example
    """

    patterns_checked = 0
    maximum_colors = -1
    number_of_extremal_patterns = 0
    avoiding_by_colors: dict[int, int] = {}
    extremal_example: tuple[int, ...] = ()

    for colors in normalized_colorings(n * n):
        patterns_checked += 1
        number_of_colors = max(colors) + 1 if colors else 0

        if has_rainbow_perfect_matching(n, colors):
            continue

        avoiding_by_colors[number_of_colors] = (
            avoiding_by_colors.get(number_of_colors, 0) + 1
        )

        if number_of_colors > maximum_colors:
            maximum_colors = number_of_colors
            number_of_extremal_patterns = 1
            extremal_example = colors
        elif number_of_colors == maximum_colors:
            number_of_extremal_patterns += 1

    return (
        patterns_checked,
        maximum_colors,
        number_of_extremal_patterns,
        avoiding_by_colors,
        extremal_example,
    )


def display_matrix(colors: tuple[int, ...], n: int) -> str:
    """Display the edge-color pattern as an n x n matrix."""

    rows = []
    for i in range(n):
        rows.append(" ".join(str(colors[i * n + j]) for j in range(n)))
    return "\n".join(rows)


def main() -> None:
    print("Exhaustive rainbow perfect matching search")
    print()

    for n in (2, 3):
        (
            checked,
            maximum_colors,
            extremal_count,
            avoiding_by_colors,
            example,
        ) = exhaustive_search(n)

        print(f"K_{{{n},{n}}}")
        print(f"  color patterns checked: {checked}")
        print(
            "  maximum colors with no rainbow perfect matching: "
            f"{maximum_colors}"
        )
        print(f"  extremal patterns: {extremal_count}")
        print(f"  avoiding patterns by color count: {avoiding_by_colors}")
        print("  one extremal pattern:")
        print(display_matrix(example, n))
        print()


if __name__ == "__main__":
    main()
