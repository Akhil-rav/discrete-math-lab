"""Count prefix paths on each fixed support, grouping relabelings of states."""
from collections import Counter
from math import comb


def relabel(adj):
    # Ties can retain the old order. This may miss mergers, but every
    # merger still identifies two isomorphic graphs.
    labels = [row.bit_count() for row in adj]
    for _ in range(len(adj)):
        keys = [(labels[i], tuple(sorted(labels[j] for j in range(len(adj))
                                         if row & (1 << j))))
                for i, row in enumerate(adj)]
        ranks = {key: i for i, key in enumerate(sorted(set(keys)))}
        new = [ranks[key] for key in keys]
        if len(set(labels)) == len(ranks):
            labels = new
            break
        labels = new
    order = sorted(range(len(adj)), key=labels.__getitem__)
    return tuple(sum(1 << j for j, v in enumerate(order) if adj[u] & (1 << v))
                 for u in order)


def path_states(history):
    states = {(): 1}
    for old, target in zip(history, history[1:]):
        following = Counter()
        for graph, count in states.items():
            s = len(graph)
            adj = graph + (0, 0)
            for i in range(s+1):
                for j in range(i+1, s+1 if i < s else s+2):
                    if adj[i] & adj[j] or adj[i] & (1 << j):
                        continue
                    # Count open pairs newly blocked by the inserted edge.
                    loss = 1
                    for a, b in ((i, j), (j, i)):
                        neighbors = adj[a]
                        while neighbors:
                            bit = neighbors & -neighbors
                            neighbors ^= bit
                            if not adj[b] & adj[bit.bit_length()-1]:
                                loss += 1
                    if old + loss != target:
                        continue
                    size = max(s, j+1)
                    child = list(adj[:size])
                    child[i] |= 1 << j
                    child[j] |= 1 << i
                    following[relabel(child)] += count * comb(size, size-s)
        states = following
        yield states


def path_tables(history):
    for states in path_states(history):
        totals = Counter()
        for graph, count in states.items():
            totals[len(graph)] += count
        yield dict(sorted(totals.items()))


if __name__ == "__main__":
    from forecast_coefficients import evaluate, support_coefficients

    for u in (6, 5):
        history = (0, 1, 3, u, 7, 10, 13, 15)
        for length, row in enumerate(path_tables(history), 2):
            assert row == support_coefficients(history[:length])
    tables = []
    for u in (3, 4):
        history = (0, 1, 2, u, 6, 7, 10, 13, 16, 19, 22, 23, 24, 28)
        for length, row in enumerate(path_tables(history), 2):
            if length >= len(history)-1:
                tables.append(row)
                print(u, length, row, flush=True)

    p, a, q, b = tables
    assert max(map(max, (p, q))) == 16 and max(map(max, (a, b))) == 17

    def difference(n):
        return evaluate(a, n)*evaluate(q, n) - evaluate(b, n)*evaluate(p, n)

    assert all(difference(n) != 0 for n in range(8, 16))
    values = [difference(n) for n in range(16, 50)]
    for j in range(34):
        assert values[0] > 0 if j < 33 else values[0] == 0
        values = [right-left for left, right in zip(values, values[1:])]
    print("No exceptional graph orders n >= 8.")
