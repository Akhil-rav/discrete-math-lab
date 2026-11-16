"""A second enumeration, using vertex matchings and successive color merges."""

import unittest
from itertools import combinations

from experiments.ladder_stability import avoiding_partitions, tilings


def vertex_matchings(k):
    rungs = [(i, k + i) for i in range(k)]
    rails = [(row + i, row + i + 1) for row in (0, k) for i in range(k - 1)]
    adjacent = [[] for _ in range(2 * k)]
    for edge, (u, v) in enumerate(rungs + rails):
        adjacent[u].append((v, edge))
        adjacent[v].append((u, edge))

    def visit(free):
        if not free:
            yield ()
            return
        u = min(free)
        for v, edge in adjacent[u]:
            if v in free:
                for rest in visit(free - {u, v}):
                    yield (edge,) + rest

    return list(visit(set(range(2 * k))))


def by_color_merges(k, matchings):
    edges = list(range(3 * k - 2))
    rows = [0] * len(edges)
    for i, matching in enumerate(matchings):
        for edge in matching:
            rows[edge] |= 1 << i
    answer = set()

    def visit(blocks, masks, rainbow, steps):
        if steps == 1:
            # One merge remains. Both colors must occur in every surviving row.
            options = [b for b in blocks if masks[b] & rainbow == rainbow]
        else:
            if not rainbow:
                raise AssertionError("An avoiding coloring used deficit below three")
            witness = set(matchings[(rainbow & -rainbow).bit_length() - 1])
            options = [b for b in blocks if witness.intersection(b)]
        for a, b in combinations(options, 2):
            merged = tuple(sorted(a + b))
            new_blocks = (blocks - {a, b}) | {merged}
            if steps == 1:
                answer.add(tuple(sorted(c for c in new_blocks if len(c) > 1)))
            else:
                new_rainbow = rainbow & ~(masks[a] & masks[b])
                visit(new_blocks, masks | {merged: masks[a] | masks[b]}, new_rainbow, steps - 1)

    blocks = {(e,) for e in edges}
    visit(blocks, {(e,): rows[e] for e in edges}, (1 << len(matchings)) - 1, 3)
    return answer


class StabilityTests(unittest.TestCase):
    def test_all_base_cases(self):
        from src.l5_extremizers import extremal_block_families

        for k in range(5, 18):
            with self.subTest(k=k):
                matchings = vertex_matchings(k)
                self.assertEqual(
                    {tuple(sorted(m)) for m in matchings},
                    {tuple(sorted(m)) for m in tilings(k)},
                )
                actual = avoiding_partitions(k)
                self.assertEqual(actual, by_color_merges(k, matchings))
                expected = {
                    tuple(sorted(tuple(sorted(b)) for b in blocks))
                    for blocks in extremal_block_families(k)
                }
                self.assertEqual(actual, expected)
                self.assertEqual(len(actual), 15)

    def test_three_tiles_can_be_necessary(self):
        repeated = [{0, 1}, {3, 4}, {6, 7}]
        sizes = [
            sum(e >= 8 for e in m) // 2
            for m in vertex_matchings(8)
            if all(not block.issubset(m) for block in repeated)
        ]
        self.assertEqual(min(sizes), 3)
