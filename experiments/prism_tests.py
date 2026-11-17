"""Deficit-one and deficit-two test families on the prism C_k x K_2, by brute force.

  python -m experiments.prism_tests 9
"""
from itertools import combinations
import sys

def prism(k):
    E = [("r", i) for i in range(k)] + [("u", i) for i in range(k)] + [("l", i) for i in range(k)]
    ends = {}
    for i in range(k):
        ends[("r", i)] = (("t", i), ("b", i))
        ends[("u", i)] = (("t", i), ("t", (i + 1) % k))
        ends[("l", i)] = (("b", i), ("b", (i + 1) % k))
    return E, ends

def perfect_matchings(E, ends):
    verts = sorted({v for e in E for v in ends[e]})
    out = []
    def go(used, chosen):
        free = [v for v in verts if v not in used]
        if not free:
            out.append(frozenset(chosen)); return
        v = free[0]
        for e in E:
            a, b = ends[e]
            if v in (a, b) and a not in used and b not in used:
                go(used | {a, b}, chosen + [e])
    go(frozenset(), [])
    return out

def analyse(k):
    E, ends = prism(k)
    ms = perfect_matchings(E, ends)
    n = len(ms)
    def mask(classes):
        return sum(1 << i for i, m in enumerate(ms) if all(len(m & c) <= 1 for c in classes))
    d1 = [mask([frozenset(p)]) for p in combinations(E, 2)]
    d2 = [mask([frozenset(t)]) for t in combinations(E, 3)]
    pairs = list(combinations(E, 2))
    for a in range(len(pairs)):
        for b in range(a + 1, len(pairs)):
            if not set(pairs[a]) & set(pairs[b]):
                d2.append(mask([frozenset(pairs[a]), frozenset(pairs[b])]))
    no_rainbow2 = sum(1 for x in d2 if x == 0)
    d1 = sorted(set(x for x in d1 if x)); d2 = sorted(set(x for x in d2 if x))
    def best(masks):
        for t in range(1, 6):
            cnt = 0
            for T in combinations(range(n), t):
                tm = sum(1 << i for i in T)
                if all(x & tm for x in masks): cnt += 1
            if cnt: return t, cnt
        return None, 0
    return n, no_rainbow2, best(d1), best(d2)

def jacobsthal(n):
    return (2 ** n - (-1) ** n) // 3


def predicted(k):
    extra = 0 if k % 2 else (9 if k == 4 else k + 1)
    return jacobsthal(k - 1) + k * jacobsthal(k - 2) + extra


if __name__ == "__main__":
    top = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    for k in range(3, top + 1):
        n, bad, b1, b2 = analyse(k)
        assert bad == 0 and b2 == (3, predicted(k)), (k, b2)
        print(f"k={k}: matchings={n}, deficit-one optimum {b1}, "
              f"deficit-two optimum {b2} = predicted {predicted(k)}", flush=True)
