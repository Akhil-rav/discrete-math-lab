# Verification index

The current implementation can be checked from a clean clone using Python
3.11+ and the standard library:

```sh
python -m tools.verify_repository
```

This runs portable integrity checks, the complete test suite, and six exact
dataset reproductions. It does not install dependencies, contact external sites,
or execute commands stored in evidence records.

## Evidence records

| Study | Execution / review record | Mathematical output |
|---|---|---|
| Original matching, progression, algorithm studies | [Original bounded run](verification.md) | [small_cases.json](data/small_cases.json) |
| Sparse rainbow-perfect-matching search | [Coverage and execution](sparse_verification.md) | [sparse_rainbow.json](data/sparse_rainbow.json) |
| Disjoint unions of even cycles | [General proof review and bounded checks](cycle_union_verification.md) | [Ten-host data and every extremizer](data/cycle_unions.json) |
| Cube symmetry classification | [Classification checks](cube_verification.md) | [All 174 extremizers and nine classes](data/cube_classification.json) |
| Cube incidence proof and collision audit | [Proof review](cube_bound_review.md), [bounded audit](cube_collision_verification.md) | [Collision certificates](data/cube_collisions.json) |
| Independent random edge colors | [Proof scope and exact computation](random_rainbow_verification.md) | [Exact probabilities](data/random_rainbow.json) |
| Random-walk formulas | [Proof and finite formula checks](walk_paper_verification.md) | [Walk examples](algorithm_demos.md) |

Dates, test counts, and interpreter paths in these records describe the original
executions. They are historical evidence, rather than claims that an old test
count is the size of today's suite. Current checks rerun the present sources.

## What the portable checker establishes

`python -m tools.verify_repository --static-only` checks:

- The simple inline local links and image references used in the Markdown files.
- JSON syntax, duplicate keys, and non-finite constants.
- The SHA-256 of every recorded output in the version-2 run records.
- Agreement between each of the six reference datasets and its successful
  recorded JSON result, allowing harmless text formatting differences.
- The exact source hashes pinned by the cube proof, probability proof,
  random-walk, and cycle-union review records.

Recorded paths must stay inside the repository. External URLs and Markdown
heading anchors are not validated by this offline link scan. It is a scoped
checker for the repository's artifacts, not a complete validation of every
possible manifest format or Markdown extension.

Current source hashes are compared with historical run inputs. A changed input
is reported as historical, rather than falsely treating a preserved old run as
corrupt. Altered output bytes or a changed proof with an unchanged review record
are errors. The full command then runs current tests and reproductions to check
the present implementation independently of historical source compatibility.

## Interpretation

Passing integrity checks is not a theorem, an independent referee report, or a
novelty certificate. A successful computation only supports its recorded finite
domain and interpretation. General mathematical statements rely on the written
proofs or on precisely checked external results.

Figure regeneration and LaTeX compilation are separate presentation checks.
Their dependencies are documented in the relevant project and paper pages.
