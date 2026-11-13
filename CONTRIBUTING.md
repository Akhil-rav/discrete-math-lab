# Contributing and recording claims

Use Python 3.11+ and the standard library. Run from the root:

```sh
python -m unittest discover -s tests -v
python -m experiments.reproduce --check results/data/small_cases.json
```

State each mathematical change's exact domain, conventions, finite bound, and
non-claims. Record the command, raw data or digest, revision, interpreter version,
and whether inputs changed during execution. Separate machine-dependent run
provenance from deterministic result data.

A known result needs a checked primary source and hypotheses. A computation
needs coverage checks and a meaningful independent oracle or invariant.
A conjecture needs precise quantifiers and evidence; do not describe it as new
or currently open without a scoped literature check. Supply a verifiable witness
when an example disproves a precise statement.

Keep full third-party papers out of Git. Record consulted versions, unavailable
statements, and version discrepancies. Distinguish metadata checks, theorem
extraction, proof audits, and implementations.

Do not replace historical results silently. Add a dated correction and update
dependent summaries when an interpretation changes. Preserve old experiments
as regression checks when extending the code.
