"""Audit twist recovery via path colorings with both terminal bits fixed."""
from itertools import combinations_with_replacement, product
from collections import Counter
from math import comb


def law(lengths, twists):
    # Fix the first terminal to zero. The other terminal is d.
    total = Counter()
    for d in (0, 1):
        row = {0: 1}
        for l,t in zip(lengths,twists):
            nxt = Counter()
            for j in range(l+1):
                # j conflicts; the other l-j edges disagree with their bits.
                if (l-j+t) % 2 == d:
                    for k,v in row.items():
                        nxt[k+j] += v*comb(l,j)
            row = nxt
        total.update(row)
    return tuple(total[i] for i in range(sum(lengths)+1))


def orbit(lengths,twists):
    def counts(bits):
        return tuple(sum(t for l,t in zip(lengths,bits) if l == s)
                     for s in sorted(set(lengths)))
    return min(counts(twists), counts([1-t for t in twists]))


if __name__ == "__main__":
    systems = assignments = classes = comparisons = 0
    for r in range(2,7):
        for lengths in combinations_with_replacement(range(1,5), r):
            if lengths.count(1)>1:
                continue
            seen, reverse, prior = {}, {}, []
            for t in product(range(2), repeat=r):
                key, p = orbit(lengths,t), law(lengths,t)
                assert seen.setdefault(p,key) == key
                assert reverse.setdefault(key,p) == p
                size = sum(lengths)-r+1  # free vertex bits after fixing one terminal
                moments = [sum(v*comb(i,j) for i,v in enumerate(p) if i >= j)
                           for j in range(len(p))]
                for old, prev in prior:
                    if moments == prev:
                        continue
                    groups = [Counter(),Counter()]
                    for l,a,b in zip(lengths,t,old):
                        groups[a != b][l] += 1-2*a
                    j,k = (min(l for l,v in group.items() if v) for group in groups)
                    h = next(i for i,(a,b) in enumerate(zip(moments,prev)) if a != b)
                    assert h == j+k
                    assert (moments[h]-prev[h])*2**(h-1) == 2**size*groups[0][j]*groups[1][k]
                    comparisons += 1
                prior.append((t,moments))
                assignments += 1
            systems += 1
            classes += len(seen)
    print(systems, assignments, classes, comparisons)
