"""Check a cubic degree bound against all tournament scores at small orders."""
from itertools import combinations_with_replacement
from math import comb


def tail_scores(n, prefix):
    size = n - prefix
    lower, remainder = divmod((prefix + n - 1) * size // 2, size)
    return tuple(range(prefix)) + (lower,) * (size - remainder) + (lower + 1,) * remainder


def score_sequences(n):
    target = comb(n, 2)
    for scores in combinations_with_replacement(range(n), n):
        if sum(scores) != target:
            continue
        total = 0
        for count, value in enumerate(scores, 1):
            total += value
            if total < comb(count, 2):
                break
        else:
            yield scores


def check_cubics(n):
    sequences = list(score_sequences(n))
    moments = [(sum(x*x for x in row), sum(x**3 for x in row)) for row in sequences]
    tails = [tail_scores(n, b) for b in range(n)]
    for s in range(-3, 9 * n + 4):
        actual = min(3 * cubes - s * squares for squares, cubes in moments)
        expected = min(sum(3 * x**3 - s * x*x for x in row) for row in tails)
        assert actual == expected, (n, s)
    return len(sequences)


if __name__ == '__main__':
    from star_scores import optimize

    for n in range(2, 11):
        print(n, check_cubics(n), 'score sequences', flush=True)
    for n in range(4, 25):
        row = tail_scores(n, (n-1)//2)
        count = sum(x * comb(n-1-x, 2) for x in row)
        assert optimize(n, 1, 2)[0] == count
        print(n, count, 'mixed stars', flush=True)
