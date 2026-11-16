# Matching-cover verification

The [mathematical note](../notes/matching_covers.md) proves two statements:
the minimum color deficit equals the minimum weighted block-cover cost,
and $A(P_k\square K_2)=3k-5$ for every $k\ge3$.
The square is treated separately. The [finite report](matching_covers.md)
records the certificate computations and L5 classification.

Proof source SHA-256: `1eaa47f50db69d4380dfeb5fd19aca253e1e6a53268b2e086843e01fcf2d44e3`.

The reduction and general ladder formula have separate proofs in the note.
The records below document their finite implementations and witnesses.

## Computation and independent checks

- Nine exact cover certificates, with at most thirteen positions and nine
  targets. Eight maxima agree with saved partition searches.
- The checker rebuilds every block by combinations and set intersections,
  verifies all cost states, and checks covering and coloring witnesses.
- Every nonempty family of pair targets on four positions is compared with
  complete partition enumeration. Mixed target sizes and overlapping blocks
  exercise the merge step. Altered certificates are rejected.
- All 41,835 L5 partitions of deficits 0, 1, 2, and 3 are visited.
  The maximum band has 39,325 candidates and fifteen avoiding partitions.
- An independent block-shape enumerator recovers exactly those fifteen.
  It yields 4 quadruple, 8 triple-and-pair, and 3 three-pair patterns.
- All degree-preserving vertex bijections recover the full four-element
  L5 automorphism group. The six orbits have sizes 4, 2, 2, 2, 4, 1.
- A separate nonadjacent-gap enumeration checks matching counts, edge and
  pair capacities, and the general construction for k=3 through 10.
  This supports implementation checks; the proof handles arbitrary k.

## Execution record

[Contract](contracts/matching-covers.json) ·
[Manifest](runs/matching-covers-2026-11-15/manifest.json) ·
[Recorded data](runs/matching-covers-2026-11-15/covers.json) ·
[Output](runs/matching-covers-2026-11-15/stdout.txt) ·
[Error log](runs/matching-covers-2026-11-15/stderr.txt).

The run completed under a 60-second wall-clock limit, with unchanged declared
inputs and recorded output hashes. The reference dataset matches its recorded
result. No POSIX CPU or memory cap was requested on Windows.

```sh
python -m experiments.matching_covers --check results/data/matching_covers.json
python -m unittest tests.test_matching_covers -v
python -m tools.verify_repository
```

The original twelve-edge partition solver and the earlier datasets are
preserved. This run does not enumerate all L5 partitions or compute its
random-coloring probabilities. The [literature record](../notes/literature/ladders.md)
does not establish novelty.

The L5 population now also has a [direct counting proof](../notes/l5_extremizers.md),
with its own [proof checks](l5_extremizer_proof.md). The recorded search above
is preserved as a separate finite check.
