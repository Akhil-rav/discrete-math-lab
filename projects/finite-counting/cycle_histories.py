"""Count maximal-loss histories on cycle unions by separated leaf sets."""
from itertools import combinations
from math import comb


def cycle_count(length, leaves):
    if leaves == 0:
        return 1
    if leaves > length//3:
        return 0
    return length * comb(length-2*leaves-1, leaves-1) // leaves


def path_count(length, leaves):
    if leaves == 0:
        return 1
    top = length-2*(leaves-1)
    return comb(top, leaves) if top >= leaves else 0


def pack(length, func, base):
    return sum(func(length, t)*base**t for t in range(length//3+2))


def scan(max_vertices):
    # No carry: at each degree there are at most n*2^n rooted leaf sets.
    base = 1 << (max_vertices + max_vertices.bit_length() + 1)
    cycles = {l: pack(l,cycle_count,base) for l in range(4,max_vertices+1)}
    rooted = {l: l*pack(max(0,l-7),path_count,base) for l in cycles}
    cases = 0
    first = None
    for n in range(4,max_vertices+1):
        seen = {}
        def visit(left, low, parts, product, derivative):
            nonlocal cases, first
            if left == 0:
                cases += 1
                key = (parts.count(4), parts.count(5), parts.count(6), derivative)
                if key in seen and first is None:
                    first = (seen[key], parts)
                seen[key] = parts
            for l in range(low, left+1):
                visit(left-l,l,parts+(l,), product*cycles[l],
                      derivative*cycles[l]+product*rooted[l])
        visit(n,4,(),1,0)
    return cases, first


def direct_polynomial(parts):
    from collections import Counter
    size = sum(parts)
    component = []
    for index, length in enumerate(parts):
        component.extend((index, i, length) for i in range(length))
    def distance(v, w):
        a, i, length = component[v]
        b, j, _ = component[w]
        return min(abs(i-j), length-abs(i-j)) if a == b else size+1
    counts = Counter()
    for root in range(size):
        eligible = [v for v in range(size) if distance(root,v) >= 4]
        for t in range(len(eligible)+1):
            for chosen in combinations(eligible,t):
                if all(distance(v,w)>=3 for v,w in combinations(chosen,2)):
                    counts[t] += 1
    return counts


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-vertices', type=int, default=60)
    args = parser.parse_args()
    for parts in [(4,), (6,), (9,), (12,), (4,5), (4,8), (7,7), (4,5,6)]:
        base = 1 << (sum(parts)+sum(parts).bit_length()+1)
        prod, rooted = 1, 0
        for l in parts:
            c = pack(l,cycle_count,base)
            rooted = rooted*c+prod*l*pack(max(0,l-7),path_count,base)
            prod *= c
        assert rooted == sum(count*base**t for t,count in direct_polynomial(parts).items())
    print(scan(args.max_vertices))
