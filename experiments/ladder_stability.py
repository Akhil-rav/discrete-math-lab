"""Compare every deficit-three avoiding partition with the terminal list."""

from argparse import ArgumentParser
from functools import reduce
from itertools import combinations
from operator import or_

from src.l5_extremizers import extremal_block_families


def canonical(blocks):
    return tuple(sorted(tuple(sorted(block)) for block in blocks))


def tilings(k):
    """Choose nonconsecutive horizontal gaps, then fill free columns with rungs."""
    for size in range(k // 2 + 1):
        # Adding 0,1,... to an increasing tuple makes its gaps at least two.
        for small in combinations(range(k - size), size):
            gaps = [value + j for j, value in enumerate(small)]
            used = set(gaps) | {i + 1 for i in gaps}
            yield tuple(i for i in range(k) if i not in used) + tuple(
                e for i in gaps for e in (k + i, 2 * k - 1 + i)
            )


def avoiding_partitions(k):
    edges = range(3 * k - 2)
    matchings = list(tilings(k))
    all_rows = (1 << len(matchings)) - 1
    incidence = [0] * len(edges)
    for row, matching in enumerate(matchings):
        for edge in matching:
            incidence[edge] |= 1 << row
    pairs = {p: incidence[p[0]] & incidence[p[1]] for p in combinations(edges, 2)}

    def missed(block):
        return all_rows ^ reduce(or_, (pairs[p] for p in combinations(block, 2)))

    def finishing_pairs(rows, occupied):
        common = (e for e in edges if e not in occupied and incidence[e] & rows == rows)
        yield from combinations(common, 2)

    found = set()
    for block in combinations(edges, 4):
        if not missed(block):
            found.add((block,))
    for triple in combinations(edges, 3):
        for pair in finishing_pairs(missed(triple), triple):
            found.add(canonical((triple, pair)))

    # Some final pair must lie in the all-rung matching. Some other
    # final pair must then lie in a matching missed by that first pair.
    for first in combinations(range(k), 2):
        rows = all_rows ^ pairs[first]
        witness = matchings[(rows & -rows).bit_length() - 1]
        for second in combinations(sorted(set(witness).difference(first)), 2):
            occupied = first + second
            for third in finishing_pairs(rows & ~pairs[second], occupied):
                found.add(canonical((first, second, third)))
    return found


def check(k):
    actual = avoiding_partitions(k)
    expected = {canonical(blocks) for blocks in extremal_block_families(k)}
    if actual != expected or len(expected) != 15:
        raise ValueError(f"L{k}: unexpected={actual - expected}, missing={expected - actual}")
    counts = [sum(len(partition) == n for partition in actual) for n in (1, 2, 3)]
    return (k, sum(1 for _ in tilings(k)), *counts, len(actual))


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, choices=range(5, 18), default=17)
    args = parser.parse_args()
    print("columns,matchings,quadruple,triple_and_pair,three_pairs,total")
    for k in range(5, args.through + 1):
        print(*check(k), sep=",", flush=True)
