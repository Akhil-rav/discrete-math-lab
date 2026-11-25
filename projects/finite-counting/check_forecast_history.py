"""Count labeled move orders compatible with one prescribed open-pair history."""
from collections import Counter
from itertools import combinations


def next_counts(n, history):
    pairs = list(combinations(range(n), 2))
    bits = {pair: 1 << i for i, pair in enumerate(pairs)}
    triangles = {edge: [] for edge in bits.values()}
    for a, b, c in combinations(range(n), 3):
        triangle = bits[a, b] | bits[a, c] | bits[b, c]
        for pair in ((a, b), (b, c), (a, c)):
            edge = bits[pair]
            triangles[edge].append(triangle ^ edge)

    all_open = (1 << len(pairs)) - 1
    if not history or history[0] != len(pairs):
        raise ValueError("history must start at the empty graph")
    states = {(0, all_open): 1}
    for target in (*history[1:], None):
        following = Counter()
        forecast = Counter()
        for (graph, open_mask), ways in states.items():
            choices = open_mask
            while choices:
                edge = choices & -choices
                choices ^= edge
                remaining = open_mask ^ edge
                for others in triangles[edge]:
                    if others & graph:
                        remaining &= ~others
                q = remaining.bit_count()
                if target is None:
                    forecast[q] += ways
                elif q == target:
                    following[graph | edge, remaining] += ways
        if target is None:
            return forecast
        states = following


if __name__ == "__main__":
    for fourth in (15, 16):
        history = (21, 20, 18, fourth, 14, 11, 9, 5, 4)
        counts = next_counts(7, history)
        print(history, sorted(counts.items()))

    expected = {22: (5, 9), 23: (5, 7)}
    for fourth, (numerator, denominator) in expected.items():
        history = (28, 27, 25, fourth, 21, 18, 16, 12, 11, 6)
        counts = next_counts(8, history)
        assert counts[5]*denominator == numerator*sum(counts.values()) > 0
        print(history, sorted(counts.items()))

    for fourth, denominator in [(25, 2864), (24, 4764)]:
        history = (28, 27, 26, fourth, 22, 21, 18, 15, 12, 9, 6, 5, 4)
        counts = next_counts(8, history)
        assert counts[0] * denominator == 11 * sum(counts.values()) > 0
        print(history, sorted(counts.items()))
