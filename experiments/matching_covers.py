"""Certified minimum deficits on nine hosts and the full extremal band of L5.

Run: python -m experiments.matching_covers [--output PATH | --check PATH].
The older partition solver retains its 12-edge limit.
"""

import argparse
import json
from collections import Counter
from pathlib import Path

from experiments.rainbow_inclusion_exclusion import checked_matchings
from experiments.sparse_rainbow import hosts
from src.cube_symmetry import transform_partition
from src.ladders import bipartite_edges, ladder_actions, ladder_edges, ladder_matchings
from src.matching_covers import minimum_cover
from src.matching_cover_certificate import check_certificate

ROOT = Path(__file__).resolve().parents[1]


def deficit_partitions(length, deficit):
    """Restricted-growth strings with length - deficit blocks, through 13 edges."""
    if not 2 <= length <= 13 or not 0 <= deficit <= min(3, length - 1):
        raise ValueError("Need 2..13 positions and deficit 0..3 below the length.")
    colors = [0] * length

    def visit(position, blocks):
        used = position - blocks
        if used > deficit or used + length - position < deficit:
            return
        if position == length:
            yield tuple(colors)
            return
        for color in range(blocks + 1):
            colors[position] = color
            yield from visit(position + 1, max(blocks, color + 1))

    yield from visit(1, 1)


def run():
    sparse = json.loads((ROOT / "results/data/sparse_rainbow.json").read_text())
    ladders = json.loads((ROOT / "results/data/ladder_matchings.json").read_text())[
        "hosts"
    ]
    cases = hosts()
    cases.update({f"L{k}": (k, bipartite_edges(k)) for k in (3, 4, 5)})
    certificates = {}
    for name, (n, edges) in cases.items():
        targets = checked_matchings(n, edges)
        result = minimum_cover(len(edges), targets)
        check_certificate(len(edges), targets, result)
        if name != "L5":
            reference = sparse[name] if name in sparse else ladders[name]
            if (
                result["maximum_avoiding_colors"]
                != reference["maximum_avoiding_colors"]
            ):
                raise RuntimeError(
                    "Cover optimum differs from a saved partition search."
                )
        certificates[name] = {
            "edge_count": len(edges),
            "matchings": targets,
            "certificate": result,
        }
    targets = ladder_matchings(5)
    if set(targets) != set(certificates["L5"]["matchings"]):
        raise RuntimeError("The three L5 matching generators disagree.")
    best_deficit = certificates["L5"]["certificate"]["minimum_deficit"]
    bands = []
    extremal = []
    for deficit in range(best_deficit + 1):
        total = avoiding = 0
        for colors in deficit_partitions(13, deficit):
            total += 1
            if all(len({colors[i] for i in target}) < 5 for target in targets):
                avoiding += 1
                if deficit != best_deficit:
                    raise RuntimeError("The cover lower bound is contradicted.")
                extremal.append(colors)
        bands.append({"deficit": deficit, "partitions": total, "avoiding": avoiding})
    actions = ladder_actions(5)
    remaining = set(extremal)
    classes = []
    while remaining:
        representative = min(remaining)
        orbit = {transform_partition(representative, action) for action in actions}
        if not orbit <= remaining or len(actions) % len(orbit):
            raise RuntimeError("L5 orbit partition failed.")
        remaining -= orbit
        classes.append(
            {
                "representative": representative,
                "orbit_size": len(orbit),
                "stabilizer_size": len(actions) // len(orbit),
                "color_class_sizes": sorted(Counter(representative).values()),
            }
        )
    return json.loads(
        json.dumps(
            {
                "conventions": "Fixed edges; color renaming ignored; symmetry quotient separate.",
                "hosts": certificates,
                "L5_classification": {
                    "edges": ladder_edges(5),
                    "matchings": targets,
                    "deficit_bands": bands,
                    "extremal_partitions": sorted(extremal),
                    "automorphism_order": len(actions),
                    "symmetry_classes": classes,
                },
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
            raise SystemExit("FAIL: matching-cover results differ")
        print("PASS: matching-cover results match", args.check)
    else:
        for name, host in data["hosts"].items():
            result = host["certificate"]
            print(
                name,
                "deficit",
                result["minimum_deficit"],
                "maximum colors",
                result["maximum_avoiding_colors"],
            )
        print(
            "L5 extremizers:",
            len(data["L5_classification"]["extremal_partitions"]),
            "classes:",
            len(data["L5_classification"]["symmetry_classes"]),
        )
