"""Success counts among all n-subsets of 2n individually labeled color tokens."""
from itertools import combinations
from math import comb


def formula(counts):
    n = sum(counts) // 2
    ways = [1] + [0]*n
    for c in counts:
        for k in range(n, 0, -1):
            ways[k] += c * ways[k-1]
    double = counts.count(2)
    both = 2**double * comb(2*n-2*double, n-double) if max(counts) <= 2 else 0
    return 2*ways[n] - both


def inventories(total, largest):
    if not total:
        yield ()
    for c in range(1, min(total, largest)+1):
        for tail in inventories(total-c, c):
            yield (c,) + tail


def direct(counts):
    tokens = [i for i, c in enumerate(counts) for _ in range(c)]
    indices = set(range(len(tokens)))
    n = len(tokens)//2
    success = 0
    for subset in combinations(indices, n):
        first = {tokens[i] for i in subset}
        second = {tokens[i] for i in indices.difference(subset)}
        success += len(first) == n or len(second) == n
    return success


if __name__ == "__main__":
    for n in range(2, 7):
        cases = list(inventories(2*n, 2*n))
        for counts in cases:
            assert formula(counts) == direct(counts)
        print(2*n, len(cases))


def predicted_maxima(n, q):
    d = 2*n-q
    l = q-n
    balanced = (2,)*d + (1,)*(2*l)
    if d < 2:
        return {balanced}
    triple = (3,) + (2,)*(d-2) + (1,)*(2*l+1)
    if l == 0 or d <= 3 or (d == 4 and l <= 6) or (d == 5 and l == 1):
        return {triple}
    if (d, l) == (6, 1):
        return {balanced, triple}
    return {balanced}


if __name__ == "__main__":
    for n in range(2, 16):
        best = {}
        for c in inventories(2*n, 2*n):
            q = len(c)
            if q < n:
                continue
            score = formula(c)
            if q not in best or score > best[q][0]:
                best[q] = (score, {c})
            elif score == best[q][0]:
                best[q][1].add(c)
        for q in range(n, 2*n+1):
            assert best[q][1] == predicted_maxima(n, q)
    print("All maximizing inventories checked for 2 <= n <= 15.")
