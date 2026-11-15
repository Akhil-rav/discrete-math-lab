# Contributing and recording claims

Use Python 3.11+ and the standard library. Run from the root:

```sh
python -m tools.verify_repository
```

This includes integrity checks and the following mathematical commands:

```sh
python -m unittest discover -s tests -v
python -m experiments.reproduce --check results/data/small_cases.json
python -m experiments.sparse_rainbow --check results/data/sparse_rainbow.json
python -m experiments.classify_cube --check results/data/cube_classification.json
python -m experiments.cube_collision_audit --check results/data/cube_collisions.json
python -m experiments.random_rainbow --check results/data/random_rainbow.json
python -m experiments.cycle_unions --check results/data/cycle_unions.json
```

State each mathematical change's domain, conventions, and tested range.
Record the command, raw data or digest, revision, interpreter version,
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

Keep the public presentation focused on mathematical writeups, implementations,
data, and reproducibility. The main README should provide a short route to the
paper, project report, and experiments. Keep personal study plans and editorial
conversation notes outside the public repository; avoid duplicating result
summaries or retaining completed tasks as future work.
