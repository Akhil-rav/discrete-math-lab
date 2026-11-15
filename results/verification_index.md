# Tests and reproducibility

The current implementation can be checked from a clean clone using Python
3.11+ and the standard library:

```sh
python -m tools.verify_repository
```

This checks saved files, runs the tests, and reproduces all nine datasets.
It uses Python's standard library and works offline.

## Results and test records

| Study | Checks | Data |
|---|---|---|
| Original matching, progression, algorithm studies | [Original bounded run](verification.md) | [small_cases.json](data/small_cases.json) |
| Sparse rainbow-perfect-matching search | [Coverage and execution](sparse_verification.md) | [sparse_rainbow.json](data/sparse_rainbow.json) |
| Disjoint unions of even cycles | [Counting argument and finite checks](cycle_union_verification.md) | [Ten-host data and every extremizer](data/cycle_unions.json) |
| Cube symmetry classification | [Classification checks](cube_verification.md) | [All 174 extremizers and nine classes](data/cube_classification.json) |
| Cube incidence proof and collision audit | [Incidence counts](cube_bound_review.md), [subset checks](cube_collision_verification.md) | [Collision certificates](data/cube_collisions.json) |
| Independent random edge colors | [Proof scope and exact computation](random_rainbow_verification.md) | [Exact probabilities](data/random_rainbow.json) |
| Matching-event inclusion-exclusion | [Coefficient checks and benchmark protocol](inclusion_exclusion.md) | [Counting polynomials and Bonferroni bounds](data/rainbow_inclusion_exclusion.json) |
| Direct five-column classification | [Counting proof and checks](l5_extremizer_proof.md) | [Proved-family constructor](../src/l5_extremizers.py), compared with [saved extremizers](data/matching_covers.json) |
| Weighted matching covers | [Reduction, general ladder proof, and certificate checks](matching_cover_verification.md) | [Nine certificates and all L5 extremizers](data/matching_covers.json) |
| Small ladders | [Proof checks and exhaustive classification](ladder_verification.md) | [All extremizers and two probability methods](data/ladder_matchings.json) |
| Random-walk formulas | [Proof and finite formula checks](walk_paper_verification.md) | [Walk examples](algorithm_demos.md) |

Dates and test counts in the records describe those runs. The command above
runs the current code.

## File checks

`python -m tools.verify_repository --static-only` checks:

- Local Markdown links and images.
- JSON syntax, duplicate keys, and non-finite constants.
- Recorded output hashes and the nine reference datasets.
- Source hashes attached to the proof notes.

Recorded paths must stay inside the repository. External URLs and Markdown
heading anchors are not checked.

Old run records retain their original inputs. Later source changes are reported
as historical differences; the full command checks the current implementation
against the saved data. Missing or altered recorded outputs are errors.

Tests check the algorithms on their stated finite domains. General statements
are supported by the written proofs and cited results.

Figure regeneration and LaTeX compilation are separate presentation checks.
Their dependencies are documented in the relevant project and paper pages.
