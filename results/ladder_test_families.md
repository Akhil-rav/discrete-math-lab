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

## Attempted lower bounds for 15 columns (November 16, 2026)

Two routes to $h_3(15)\ge 8$ were tried and neither succeeded.

1. *Monotonicity in the length.* If deleting an end column always turned a
   test family for $L_{k+1}$ into one for $L_k$, then $h_3$ would be
   nondecreasing in $k$ and $h_3(15)=h_3(16)=8$ would follow from
   $h_3(14)=8$. This reduction is false: deleting the last column from the
   sixteen-column family above (drop gap 14 where present) gives eight
   matchings of $L_{15}$ that are defeated by 553 colourings, and deleting
   the first column gives a family defeated by 117. Whether $h_3(k)$ is
   nondecreasing in $k$ remains open; a proof would need a different
   reduction.
2. *Direct search.* A CP-SAT run asking for a hitting set of size at most
   seven for all 38,816 minimal survivor sets of $L_{15}$ ended without a
   decision after 53 minutes on two cores.

The proven statement for $k=15$ is therefore $7\le h_3(15)\le 8$.

## Resolution (later on November 16, 2026)

The lower bound was obtained by a different route. Colourings confined to
two windows of four gaps, one at each end of the ladder, already force eight
tests, and the window system is the same for every $k\ge 10$
(`experiments/ladder_end_windows.py`, Proposition 6 of the note). Together
with the families above this gives $h_3(15)=h_3(16)=8$, and $h_3(k)\ge 8$ for
every $k\ge 8$.

## Seventeen columns (November 17, 2026)

Indices 494 873 901 1118 1580 1603 1917 2400 in the enumeration order of
`experiments/ladder_verify_family.cpp` (compiled with a bitset width of 4096):

- {1, 3, 6, 9, 12}
- {0, 4, 6, 11, 13}
- {2, 8, 11, 13}
- {4, 7, 9, 14}
- {0, 2, 5, 8, 10, 12, 14}
- {0, 3, 15}
- {2, 4, 6, 8, 11, 15}
- {1, 5, 7, 10, 13, 15}

229,037,941 colourings with a rainbow perfect matching; none defeats the
family. The faster checker `experiments/ladder_defeating_colourings.cpp`
agrees. With Proposition 6 this gives $h_3(17)=8$. The family was found by
`experiments/ladder_family_search.py` after about 33,500 learned constraints.
