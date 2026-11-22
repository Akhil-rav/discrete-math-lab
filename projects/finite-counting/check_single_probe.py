"""Verify the single-probe threshold by conditional terminal counts."""
from math import gcd
from functools import reduce
from calibrated_paths import law
from single_probe_search import cases


def key(paths):
    row = law(paths)
    g = reduce(gcd,row.values())
    return tuple(row[k]//g for k in range(1+sum(l for l,s in paths)))


if __name__ == "__main__":
    count = 0
    for m in range(6,17):
        seen = set()
        for (ls,neg),_,_ in cases(m,3,(m+1)//2,2**(m+3)):
            paths = []
            for l,k in zip(sorted(set(ls)),neg):
                paths.extend([(l,-1)]*k+[(l,1)]*(ls.count(l)-k))
            signature = key(paths+[(m-2,1)])
            assert signature not in seen
            seen.add(signature)
            count += 1
        for p in range(2,m-2):
            shared=[(p,-1),(p,1)]
            assert key(shared+[(1,1),(m-p-1,1)]) == key(shared+[(1,-1),(m-p-1,-1)])
    print(count, "modified-host laws distinguished through m=16")
