"""Exact rainbow-matching probabilities for the six saved sparse hosts.

Run: python -m experiments.random_rainbow [--output PATH | --check PATH].
Main grid: integer palettes 1..24. Large-palette cube values illustrate the
proved leading-term formula using the computational extremizer count 174.
"""

import argparse
import json
from pathlib import Path

from src.rainbow_constraints import matching_constraints
from src.rainbow_probability import probability_bounds, rainbow_probability

ROOT = Path(__file__).resolve().parents[1]


def run():
    hosts = json.loads((ROOT / "results/data/sparse_rainbow.json").read_text())
    records = {}
    for name, host in hosts.items():
        edges = host["edges"]
        histogram = {int(k): v for k, v in host["avoiding_histogram"].items()}
        matchings = matching_constraints(host["n_per_side"], [tuple(e) for e in edges])
        if len(matchings) != host["perfect_matchings"]:
            raise RuntimeError("Saved matching count differs from the host.")
        rows = []
        for q in range(1, 25):
            exact = rainbow_probability(len(edges), histogram, q)
            first, second, lower, upper = probability_bounds(matchings, q)
            if not 0 <= lower <= exact <= upper <= 1:
                raise RuntimeError("A probability bound failed.")
            rows.append(
                {
                    "q": q,
                    "rainbow_probability": str(exact),
                    "expected_rainbow_matchings": str(first),
                    "second_moment": str(second),
                    "second_moment_lower": str(lower),
                    "union_upper": str(upper),
                }
            )
        records[name] = {
            "edges": len(edges),
            "matching_size": host["n_per_side"],
            "perfect_matchings": len(matchings),
            "maximum_avoiding_colors": max(histogram),
            "extremal_partitions": histogram[max(histogram)],
            "palettes": rows,
        }
    cube = hosts["cube"]
    histogram = {int(k): v for k, v in cube["avoiding_histogram"].items()}
    tail = []
    for q in (32, 64, 128, 256, 1024):
        avoiding = 1 - rainbow_probability(12, histogram, q)
        tail.append(
            {
                "q": q,
                "avoiding_probability": str(avoiding),
                "q5_times_avoiding": str(q**5 * avoiding),
            }
        )
    return {
        "model": "Each edge independently receives one of q equally likely labeled colors.",
        "palette_min": 1,
        "palette_max": 24,
        "hosts": records,
        "cube_large_palette_limit": 174,
        "cube_large_palette_examples": tail,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path)
    group.add_argument("--check", type=Path)
    args = parser.parse_args()
    data = run()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n"
        )
        print("Wrote", args.output)
    elif args.check:
        if data != json.loads(args.check.read_text(encoding="utf-8")):
            raise SystemExit("FAIL: random-coloring probabilities differ")
        print("PASS: exact probabilities match", args.check)
    else:
        for name, host in data["hosts"].items():
            print(
                name,
                [
                    (r["q"], r["rainbow_probability"])
                    for r in host["palettes"]
                    if r["q"] in (4, 8, 12)
                ],
            )
