"""Time cold construction plus 24 exact evaluations for both counting methods.

Run: python -m experiments.benchmark_rainbow_methods --output PATH [--repeat 3].
Timings are machine-dependent records and are not a reference-data check.
"""

import argparse
import json
import platform
from fractions import Fraction
from pathlib import Path
from statistics import median
from time import perf_counter

from experiments.sparse_rainbow import hosts
from experiments.rainbow_inclusion_exclusion import checked_matchings
from src.rainbow_constraints import (
    avoiding_partitions,
    completions,
)
from src.rainbow_inclusion_exclusion import evaluate, rainbow_union_polynomial
from src.rainbow_probability import rainbow_probability


def partition_method(n, edges):
    completions.cache_clear()
    data = avoiding_partitions(n, edges)
    return [
        rainbow_probability(len(edges), data["avoiding_histogram"], q)
        for q in range(1, 25)
    ]


def intersection_method(n, edges):
    matchings = checked_matchings(n, edges)
    polynomial = rainbow_union_polynomial(len(edges), matchings)["union_coefficients"]
    return [Fraction(evaluate(polynomial, q), q ** len(edges)) for q in range(1, 25)]


def run(repeat):
    if type(repeat) is not int or not 1 <= repeat <= 9:
        raise ValueError("Need one through nine repetitions.")
    records = {}
    for name, (n, edges) in hosts().items():
        samples = {"partition": [], "inclusion_exclusion": []}
        results = {}
        methods = [
            ("partition", partition_method),
            ("inclusion_exclusion", intersection_method),
        ]
        for trial in range(repeat):
            for label, method in methods[:: 1 if trial % 2 == 0 else -1]:
                started = perf_counter()
                results[label] = method(n, edges)
                samples[label].append(perf_counter() - started)
            if results["partition"] != results["inclusion_exclusion"]:
                raise RuntimeError("Timed methods disagree.")
        records[name] = {
            "edges": len(edges),
            "partition_seconds": samples["partition"],
            "inclusion_exclusion_seconds": samples["inclusion_exclusion"],
            "partition_median_seconds": median(samples["partition"]),
            "inclusion_exclusion_median_seconds": median(
                samples["inclusion_exclusion"]
            ),
        }
    return {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "processor": platform.processor(),
        "repetitions": repeat,
        "palettes": list(range(1, 25)),
        "timed_work": "Host construction and I/O excluded; matching generation, cold count construction, and 24 exact probability evaluations included. Count caches are cleared between calls; method order alternates by trial.",
        "hosts": records,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repeat", type=int, default=3)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = run(args.repeat)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    print("Wrote", args.output)
