# Contributing

Use Python 3.11+ and run the complete check from the repository root:

```sh
python -m tools.verify_repository
```

The [experiment guide](experiments/README.md) lists individual commands and
input limits. The [verification index](results/verification_index.md) links
the saved data and execution records.

## Mathematical changes

State definitions, hypotheses, conventions, and the exact range covered.
Separate a written proof from a finite computation or a cited result.
For a source-dependent claim, give the precise version, theorem, and
notation translation. Record unavailable statements rather than infer them
from an abstract.

For code changes, include an independent oracle, invariant, or known example
appropriate to the change. Keep deterministic result data separate from
machine-dependent timings and execution metadata.

## Preserving results

Retain earlier datasets and raw run records. Add a dated correction when
an interpretation changes, and update the affected reports and links.
Document enough information to reproduce new computations: commands,
input hashes, software versions, bounds, and output hashes.

Keep third-party papers outside Git; cite the consulted versions in the
[source records](notes/literature/source_records.md). A conjecture or proposed
extension needs clear quantifiers and evidence. Its novelty or open status
requires a separate literature check.
