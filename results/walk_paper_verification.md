# Random-walk formula checks

Proof source SHA-256: `69c0aa20c8711cf09b6cb41072ca83636a1d6cf8e375525f1489b371c115e8ac`.

Recorded November 14, 2026.

The [paper](../papers/expansion_walks.pdf) proves the formulas. The tests
compare their finite instances with stepwise rational walk evolution.

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

Build instructions are in the [report index](../papers/README.md).
