# Random-walk formula checks

Recorded November 14, 2026.

## Formulas

The paper gives elementary proofs of the following formulas. The computations
compare their finite instances with rational walk evolution.

| Claim | Domain / conclusion | Decisive check |
|---|---|---|
| Proposition 1 | Complete graphs n>=2; simple cycles n>=3; exact unnormalized expansion | Complete cut ratio n-s; a proper cycle set has at least two boundary edges, attained by a consecutive half-block |
| Proposition 2 | K(d,d), d>=1, point start; exact ordinary and lazy TV for t>=1 | Part imbalance is killed by one lazy step; within-part residual is scaled by 1/2; its absolute sum is 2(d-1)/d |
| Proposition 3 | r>=2 disjoint K_d, d>=2; zero expansion and persistent global TV | A whole component is an eligible zero cut; support implies TV >= 1-1/r; within-component residual scales by (d-2)/(2(d-1)) |

Boundary checks: distinguish t=0 from t>=1 in Proposition 2; d=1 is K2
and mixes after one lazy step. In Proposition 3, d=2 gives factor zero and
r=2 makes a whole component exactly half the graph. The local matrix there
has degree d-1, whereas Proposition 2 has degree d. Distributions are row
vectors throughout. General bipartite graphs have TV at least 1/2 at each
time from a point start; equality is asserted only for K(d,d), t>=1.

The tolerance-time consequence of Proposition 2 is checked for d>=2 and
0<epsilon<1/2. The time-zero distance exceeds the tolerance, and for t>=1
the inequality is exactly 2^t >= (d-1)/(d*epsilon). Its logarithmic ceiling
is at least one in this domain. The worked K3,3 example has TV 1/96 at
time six and 1/192 at time seven, so 1/100 is first attained at time seven.

## Source scope

[Hoory--Linial--Wigderson](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/HLW06/hlw06.pdf),
published 2006 version, Definition 2.1 supplies the expansion convention.
Sections 2--3 are background reading. The three proofs are written out in
the note rather than attributed as exact named theorems in the survey.
No novelty or complete literature search is claimed.

## Finite implementation checks

- `python -m unittest discover -s tests -v`: 17 tests passed.
- Both `experiments.reproduce --check results/data/small_cases.json` and
  `experiments.sparse_rainbow --check results/data/sparse_rainbow.json`
  regenerated data equal to their reference datasets.
- `python -m unittest discover -s tests -p test_walk_formulas.py -v`:
  both new test methods passed.
- Domain: K(d,d), d=1..8, ordinary and half-lazy walks; r disjoint K_d,
  r=2..4 and d=2..6, half-lazy walks. Every integer time 0..12 is checked.
- Closed-form distributions/TV are compared against stepwise rational walk
  evolution; the finite checks do not establish the universal propositions.
- Outcome: **implementation and finite assertion verified in the stated range**.
- [Contract](contracts/walk-formulas.json),
  [manifest](runs/walk-formulas-2026-11-14/manifest.json),
  [test output](runs/walk-formulas-2026-11-14/stderr.txt).
- Recorded run status: **completed**; manifest validation passed at that
  checkpoint. Test inputs were unchanged during the recorded run.

## Typesetting and proofreading

The three-page PDF was compiled using
Tectonic 0.17.0 with the official tlextras-2022.0r0 bundle; compilation
reported no overfull boxes, undefined references, or missing characters.
Every rendered page was visually inspected for layout and legibility.

Reviewed source SHA-256: `69c0aa20c8711cf09b6cb41072ca83636a1d6cf8e375525f1489b371c115e8ac`.
