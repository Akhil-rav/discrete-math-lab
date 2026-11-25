"""Exact average effect of using one fewer observation than forecast memory."""
from collections import Counter, defaultdict
from fractions import Fraction

from open_pair_memory import observations
from open_pair_orbits import orbit_laws


def discrepancies(layers, n, length):
    # Terminal histories stay at zero and contribute zero to every discrepancy.
    mass = {(n*(n-1)//2,): Fraction(1)}
    absorbed = Fraction(0)
    for time, laws in enumerate(layers):
        assert sum(mass.values()) + absorbed == 1
        assert laws.keys() == mass.keys()
        groups = defaultdict(Counter)
        following = {}
        for history, law in laws.items():
            for q, p in law.items():
                joint = mass[history]*p
                groups[history[-length:]][q] += joint
                if q:
                    following[history+(q,)] = joint
                else:
                    absorbed += joint
        pooled = {key: {q: w/sum(row.values()) for q, w in row.items()}
                  for key, row in groups.items()}
        changed = average = maximum = Fraction(0)
        for history, law in laws.items():
            short = pooled[history[-length:]]
            tv = sum(abs(short[q]-law.get(q, 0)) for q in short)/2
            if tv:
                changed += mass[history]
                average += mass[history]*tv
                maximum = max(maximum, tv)
        yield time, changed, average, maximum
        mass = following


if __name__ == "__main__":
    for n, length in ((6, 3), (7, 5)):
        rows = list(discrepancies(orbit_laws(n), n, length))
        if n == 6:
            direct = (layer for layer in observations(n, 9) if layer)
            assert rows == list(discrepancies(direct, n, length))
        for row in rows:
            if row[1]:
                print(n, length, *row)
