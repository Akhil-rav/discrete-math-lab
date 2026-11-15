"""Exact ladder partitions, symmetry classes, and rainbow probabilities.

Run: python -m experiments.ladder_matchings [--output PATH | --check PATH].
All partitions of the 4, 7, and 10 fixed edge positions are visited.
"""

import argparse
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

from experiments.rainbow_complete_bipartite import normalized_colorings
from experiments.rainbow_inclusion_exclusion import (
    checked_matchings,
    histogram_polynomial,
)
from src.cube_symmetry import transform_partition
from src.ladders import bipartite_edges, ladder_actions, ladder_edges, ladder_matchings
from src.rainbow_constraints import avoiding_partitions
from src.rainbow_inclusion_exclusion import evaluate, rainbow_union_polynomial
from src.rainbow_probability import rainbow_probability


def run():
    records = {}
    for k in (2, 3, 4):
        edges = ladder_edges(k)
        m = len(edges)
        matchings = ladder_matchings(k)
        if set(matchings) != set(checked_matchings(k, bipartite_edges(k))):
            raise RuntimeError("Column, edge-subset, and permutation matchings differ.")
        histogram = Counter()
        extremal = []
        best = 0
        total = 0
        for colors in normalized_colorings(m):
            total += 1
            if any(len({colors[i] for i in matching}) == k for matching in matchings):
                continue
            blocks = max(colors) + 1
            histogram[blocks] += 1
            if blocks > best:
                best, extremal = blocks, [colors]
            elif blocks == best:
                extremal.append(colors)
        pruned = avoiding_partitions(k, bipartite_edges(k))
        if (
            histogram != pruned["avoiding_histogram"]
            or total != pruned["total_partitions"]
        ):
            raise RuntimeError("Unpruned and pruned partition searches disagree.")
        actions = ladder_actions(k)
        remaining = set(extremal)
        classes = []
        while remaining:
            representative = min(remaining)
            orbit = {transform_partition(representative, action) for action in actions}
            if not orbit <= remaining or len(actions) % len(orbit):
                raise RuntimeError(
                    "Orbit closure, disjointness, or divisibility failed."
                )
            remaining -= orbit
            classes.append(
                {
                    "representative": list(representative),
                    "orbit_size": len(orbit),
                    "stabilizer_size": len(actions) // len(orbit),
                    "color_class_sizes": sorted(Counter(representative).values()),
                }
            )
        polynomial = rainbow_union_polynomial(m, matchings)
        if polynomial["union_coefficients"] != histogram_polynomial(m, histogram):
            raise RuntimeError("The two exact count polynomials differ.")
        probabilities = []
        for q in range(1, 25):
            exact = rainbow_probability(m, histogram, q)
            if exact != Fraction(evaluate(polynomial["union_coefficients"], q), q**m):
                raise RuntimeError("The two exact probabilities differ.")
            probabilities.append({"q": q, "rainbow_probability": str(exact)})
        records[f"L{k}"] = {
            "columns": k,
            "edges": edges,
            "matchings": matchings,
            "total_partitions": total,
            "avoiding_histogram": dict(sorted(histogram.items())),
            "maximum_avoiding_colors": best,
            "extremal_partitions": sorted(extremal),
            "automorphism_order": len(actions),
            "symmetry_classes": classes,
            "inclusion_exclusion": polynomial,
            "palettes": probabilities,
        }
    return json.loads(
        json.dumps(
            {
                "conventions": "Fixed edges; color names ignored. Lk = Pk square K2.",
                "coefficient_order": "ascending powers of q",
                "hosts": records,
            }
        )
    )


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
            raise SystemExit("FAIL: ladder results differ")
        print("PASS: ladder results match", args.check)
    else:
        for name, host in data["hosts"].items():
            print(
                name,
                "A =",
                host["maximum_avoiding_colors"],
                "extremizers:",
                len(host["extremal_partitions"]),
                "classes:",
                len(host["symmetry_classes"]),
            )
