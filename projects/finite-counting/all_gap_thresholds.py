"""First targets with each possible gap count, including empty initial slices."""
from math import gcd


def thresholds(p, d, a, b):
    if min(p, a) < 2 or d < 1 or b <= (p+d)*a or gcd(p, d) != 1 or gcd(a, b) != 1:
        raise ValueError('use coprime p,d and a,b with b > (p+d)a')
    period = d // gcd(d, b-a*p)
    stride, shift = b*period, a*period
    inverse = pow(p, -1, d) if d > 1 else 0
    conductor = (p-1)*(p+d-1)
    stop = max((p+d-1)//d, (conductor+stride-1)//stride)
    earliest = {}
    for start in range(stride):
        last = None
        gaps = 0
        for j in range(stop+1):
            s = start + j*stride
            residue = s*inverse % d
            low = (s+p+d-1)//(p+d)
            low += (residue-low) % d
            high = s//p
            high -= (high-residue) % d
            if low > high:
                continue
            if last is not None and low-j*shift-last >= 2*d:
                gaps += 1
                target = a*s
                earliest[gaps] = min(earliest.get(gaps, target), target)
            last = high-j*shift
    return [earliest[j] for j in range(1, len(earliest)+1)]


if __name__ == '__main__':
    from earliest_gaps import direct, predicted

    covered = 0
    missing_step = []
    for p in range(2, 14):
        for d in range(1, 11):
            if gcd(p,d) > 1:
                continue
            for a in (2, 3):
                for b in range((p+d)*a+1, (p+d)*a+26):
                    if gcd(a,b) != 1:
                        continue
                    exact = thresholds(p,d,a,b)
                    simpler = predicted(p,d,a,b)
                    if simpler is not None:
                        assert simpler == exact
                    else:
                        missing_step.append(((p,d,a,b),exact))
                    assert direct(p,d,a,b,max([350]+exact)+30) == exact
                    covered += 1
    print(covered, 'parameter choices;', len(missing_step), 'unrepresentable strides')
    for item in [pair for pair in missing_step if pair[1]][:8]:
        print(item)
