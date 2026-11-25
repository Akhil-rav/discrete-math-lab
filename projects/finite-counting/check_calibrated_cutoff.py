"""Check both sides of the sharp cutoff by exhaustive moment-prefix comparison."""
from single_probe_search import cases


def signature(a,b,base,t):
    # Truncate the even polynomial at t and the odd polynomial at t-2.
    return a % base**(t+1), b % base**(t-1)


if __name__ == "__main__":
    for m in range(12,25):
        high=(m+1)//2
        base=1 << (high+3)
        seen,short=set(),set()
        for paths,e,o in cases(m,3,high,base):
            key=signature(e,o,base,m-2)
            assert key not in seen
            seen.add(key)
            short.add(signature(e,o,base,m-3))
        assert len(short)<len(seen)
        print(m,len(seen),len(seen)-len(short))
