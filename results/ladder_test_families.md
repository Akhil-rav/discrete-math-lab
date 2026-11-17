# Eight-test families for deficit three on longer ladders

Recorded November 16, 2026. Each line is the gap set of one perfect matching.
Both families were checked against every colouring of deficit three that has
a rainbow perfect matching, with `experiments/ladder_verify_family.cpp`
(arguments: `k 3` followed by the indices of the matchings in the program's
enumeration order). The check reported no defeating colouring.

## Fifteen columns (indices 127 193 329 464 540 675 865 984)

- {0, 2, 7, 9}
- {1, 5, 7, 10}
- {1, 3, 9, 11}
- {2, 4, 6, 8, 12}
- {0, 3, 5, 10, 12}
- {1, 4, 8, 13}
- {0, 6, 11, 13}
- {3, 5, 7, 9, 11, 13}

101,196,185 colourings with a rainbow perfect matching; none defeats the family.

## Sixteen columns (indices 105 460 548 798 915 1022 1316 1592)

- {2, 5, 9}
- {1, 3, 6, 8, 12}
- {0, 3, 6, 10, 12}
- {1, 4, 7, 10, 13}
- {0, 2, 5, 8, 11, 13}
- {0, 7, 14}
- {1, 3, 9, 11, 14}
- {4, 6, 8, 10, 12, 14}

## What this does and does not show

These families give $h_3(15)\le 8$ and $h_3(16)\le 8$. For $8\le k\le 14$
the value $h_3(k)=8$ is exact. For $k=15$ a solver run established only
$h_3(15)\ge 7$, and for $k=16$ no lower bound beyond the Sperner bound of the
note has been computed. The families were found by local search alternating
with full verification; the search is not part of the proof.
