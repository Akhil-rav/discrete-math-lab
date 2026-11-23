"""Independent deficit-one and deficit-two counts. Run with Python 3.10+."""

from itertools import combinations


def graph_matchings(k, prism):
    """Pair the first unmatched vertex with every free neighbor."""
    edges = [(i, k + i) for i in range(k)]
    for row in (0, k):
        gaps = range(k if prism else k - 1)
        edges.extend((row + i, row + (i + 1) % k) for i in gaps)
    neighbors = [[] for _ in range(2 * k)]
    for i, (u, v) in enumerate(edges):
        neighbors[u].append((v, i))
        neighbors[v].append((u, i))

    def visit(open_vertices, matching):
        if not open_vertices:
            yield matching
            return
        u = min(open_vertices)
        for v, e in neighbors[u]:
            if v in open_vertices:
                yield from visit(open_vertices - {u, v}, matching | {e})

    return len(edges), list(visit(set(range(2 * k)), set()))


def colourings(edges, deficit):
    """Yield nonsingleton classes; all other colours occur just once."""
    if deficit == 1:
        for pair in combinations(range(edges), 2):
            yield (pair,)
    elif deficit == 2:
        for triple in combinations(range(edges), 3):
            yield (triple,)
        for a, b, c, d in combinations(range(edges), 4):
            yield ((a, b), (c, d))
            yield ((a, c), (b, d))
            yield ((a, d), (b, c))
    else:
        raise ValueError(deficit)


def count(k, prism, deficit):
    edges, matchings = graph_matchings(k, prism)
    # Encode sets of defeated matchings. Multiplicity of colourings realizing
    # a particular constraint is irrelevant to testing against all colourings.
    containing_pair = {
        pair: sum(1 << i for i, m in enumerate(matchings) if set(pair) <= m)
        for pair in combinations(range(edges), 2)
    }
    full = (1 << len(matchings)) - 1
    defeats = set()
    for blocks in colourings(edges, deficit):
        defeated = 0
        for block in blocks:
            for pair in combinations(block, 2):
                defeated |= containing_pair[pair]
        if defeated != full:
            defeats.add(defeated)

    # Transpose the matching-by-constraint relation. A candidate fails if
    # some constraint defeats every member, even if another matching survives.
    flags = [bytearray((len(defeats) + 7) // 8) for _ in matchings]
    for j, defeated in enumerate(sorted(defeats)):
        while defeated:
            one = defeated & -defeated
            flags[one.bit_length() - 1][j // 8] |= 1 << (j % 8)
            defeated -= one
    rows = [int.from_bytes(bits, "little") for bits in flags]
    pair_count = sum(not (a & b) for a, b in combinations(rows, 2))
    if deficit == 1:
        assert all(rows), "A single matching suffices"
        return pair_count
    assert pair_count == 0, "A pair of matchings suffices"
    return sum(not (a & b & c) for a, b, c in combinations(rows, 3))


if __name__ == "__main__":
    for k in range(3, 8):
        print(k, count(k, True, 2), flush=True)
