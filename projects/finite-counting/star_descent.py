"""Find the smallest tournament trapped above optimum by single-edge descent."""
from itertools import combinations


def values(n):
    edges = list(combinations(range(n), 2))
    def score(mask):
        d = [0]*n
        for i,(a,b) in enumerate(edges):
            d[b if mask >> i & 1 else a] += 1
        return sum(x*(n-1-x)*(n-2-x)//2 for x in d)
    table = [score(m) for m in range(1 << len(edges))]
    minimum = min(table)
    trapped = [m for m,v in enumerate(table) if v > minimum and
               all(table[m ^ (1 << i)] >= v for i in range(len(edges)))]
    reached = {m for m,v in enumerate(table) if v == minimum}
    stack = list(reached)
    while stack:
        m = stack.pop()
        for i in range(len(edges)):
            other = m ^ (1 << i)
            if other not in reached and table[other] >= table[m]:
                reached.add(other)
                stack.append(other)
    print("No nonincreasing path to minimum:", len(table)-len(reached))
    print(n, minimum, len(trapped), (trapped[0], table[trapped[0]]) if trapped else None)


if __name__ == "__main__":
    for n in range(4,7):
        values(n)
