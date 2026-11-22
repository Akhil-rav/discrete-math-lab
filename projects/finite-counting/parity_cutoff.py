"""Minimum common moment order if both conflict parities are observable."""
from single_probe_search import cases


def cutoff(m):
    high=(m+1)//2
    base=2**(high+3)
    rows=[(len(ls)%2, sum(neg)%2, e,o)
          for (ls,neg),e,o in cases(m,3,high,base)]
    for t in range(2,m+1):
        key={(r,s,e%base**(t+1),o%base**(t-1)) for r,s,e,o in rows}
        if len(key)==len(rows):
            return t,len(rows)
    raise AssertionError(m)


if __name__ == "__main__":
    for m in range(6,26):
        print(m,*cutoff(m))

    from calibrated_paths import law
    from fractions import Fraction
    for b in range(2,19):
        for a in (1,2):
            for probe in ([],[(2,1)]):
                left=law([(a,1),(b,1),(b,1)]+probe)
                right=law([(a,1),(b,-1),(b,-1)]+probe)
                variation=Fraction(sum(abs(left[k]-right[k]) for k in left.keys()|right.keys()),
                                   2*sum(left.values()))
                bound=Fraction(4 if probe else 2,2**b)
                assert variation<=bound
                if a==1 and not probe: assert variation==bound
    print("68 exact total variation checks passed")
