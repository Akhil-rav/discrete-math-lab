# Verification record — November 13, 2026

**Outcome:** implementation and finite assertions verified in the stated ranges.
This is not a proof of general thresholds, a full-paper proof audit, or a novelty
certificate. Literature checks are scoped in [source records](../notes/literature/source_records.md).

## Local execution

- Python 3.13.7; Windows 11, AMD64 (Intel64 Family 6 Model 186 Stepping 2).
- No third-party dependencies; exact integers and rational arithmetic; no RNG.
- `python -m unittest discover -s tests -v`: **12 tests passed**.
- `python -m experiments.reproduce --check results/data/small_cases.json`:
  regenerated data matched the reference exactly.
- `git diff --check`: passed.

The suite's recorded bounded execution began at 23:05:54 UTC (6:05:54 p.m.
America/New_York) and took **1.18565 seconds**, within a 60-second wall limit
and 1 MiB log limit. No memory/CPU hard limits were requested. Status:
**completed**, exit code 0. All 16 declared code/test input hashes were unchanged.
The tests were run separately; the suite's manifest does not assert it executed
the test module merely because that module is included among pinned inputs.

## Provenance

- [Mathematical contract](contracts/small-cases.json)
- [Version-2 run manifest](runs/2026-11-13/manifest.json)
- [Recorded result](runs/2026-11-13/small_cases.json)
- [stdout](runs/2026-11-13/stdout.txt) and [stderr](runs/2026-11-13/stderr.txt)

The manifest was created and validated using the installed computation provenance
helper; validation checked input and output hashes against the working tree.
The portable reproduction command is documented above and does not require that
helper. The machine-specific interpreter path in the manifest is historical argv,
not a path collaborators need to use.

Result SHA-256:

```text
ec8cb6926d843e9b4508c7af20199438f4a012b1830ffd186c6c0ba25401437e
```

The base revision was `aeda9be6cc8dafe0aee7d83f127c3323f3e3ff90` with a dirty
working tree containing the additions. The individual before/after hashes,
rather than the base revision alone, identify the executed code. Text source
files use LF line endings to make byte hashes reproducible across checkouts.

## Meaningful checks

- Set-partition coverage: independent Stirling recurrence through B9.
- Maximum matching: all 531 balanced bipartite graphs with part size 0..3,
  including the empty graph, checked against partial-injection enumeration;
  output endpoints and edges validated.
- Regular generator: all matrices through part size 3, all feasible degrees,
  compared with an independent bit-matrix filter, including degree zero.
- Rainbow detector: all partitions for K22/K33, compared with edge-subset search.
- K33 quotient: complete automorphism action, orbit closure, class sizes, and
  orbit/stabilizer divisibility.
- AP generators: independent middle-term equations for intervals, cyclic groups,
  and each of the three product groups used in the experiments.
- Color-coding: all 22,955 graph/k/color assignments checked against ordered paths;
  witnesses validated; exact success fractions checked against k!/k^k.
- Expansion: complete-graph and cycle formulas checked across the stated small
  ranges; bipartite parity example and lazy-walk TV monotonicity checked.

## Limits

Local execution used Python 3.13.7. The workflow also targets Python 3.11 and
3.13 on Linux; its remote results are separate from this historical local record.
The programs are educational exhaustive implementations and are not optimized
for large instances. General theorems retain their cited hypotheses. The selected
literature review does not establish global novelty or current open status.

Self-review covered all added mathematical notes and changed statements, including
color-count shifts, distinct-term AP conventions, k-vertex versus k-edge indexing,
and expansion normalization. It corrected the hand-transcribed Z2×Z4 AP-set count
to 16 before publication; the computed threshold was unchanged. No unresolved
notation error was identified in that scope. Inaccessible source formulas and
PDF internal-date discrepancies remain explicitly documented.
