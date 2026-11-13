# Sparse-host verification — November 13, 2026

**Outcome:** implementation and finite assertion verified in the stated range.
This is a new bounded extension; the original dataset and historical manifest
remain unchanged. The [report](../projects/rainbow-matchings/report.md) defines
the hosts, equality-pattern convention, pruning proof, counts, and non-claims.

- Python 3.13.7 on Windows 11; exact integers; no dependencies or RNG.
- `python -m unittest discover -s tests -v`: **15 tests passed**. New tests compare
  the pruned histogram with direct enumeration on every balanced bipartite host
  with part size 2 or 3 admitting a perfect matching. Perfect matchings themselves
  are checked using an independent edge-subset oracle on all six experiment hosts.
- `python -m experiments.sparse_rainbow --check results/data/sparse_rainbow.json`
  compares regenerated output with the stable reference. The original reproduction
  command also continues to pass.
- [Contract](contracts/sparse-rainbow.json), [manifest](runs/sparse-2026-11-13/manifest.json),
  [recorded output](runs/sparse-2026-11-13/sparse_rainbow.json),
  [stdout](runs/sparse-2026-11-13/stdout.txt), [stderr](runs/sparse-2026-11-13/stderr.txt).
- Recorded run: **completed**, exit 0, 23:15:25 UTC, **1.442895 seconds**; wall limit
  60 seconds and log limit 1 MiB; no requested CPU or memory hard caps.
- The manifest records the base commit with a dirty tree and unchanged before/after
  hashes for the declared Python inputs. It was validated against the working tree.
  Tests were run separately; listing their files does not claim execution by that run.

Recorded result SHA-256:

```text
8e97cd5269e7001bc79461f05e8818cd0efeef43b75cf5ea6c5db4cbeae3d9b0
```

Coverage is surviving partition leaves plus exactly counted disjoint rejected
subtrees, not a claim to visit every full leaf. The new solver is capped at twelve
edges. Full mathematical novelty, general cubic-graph formulas, and classification
of cube extremizers up to symmetry are not established. No paper submission or
claim of independently completed student research is implied.
