"""Compare matching-event inclusion-exclusion with the six saved host histograms.

Run: python -m experiments.rainbow_inclusion_exclusion [--output PATH | --check PATH].
"""

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path

from experiments.sparse_rainbow import hosts
from src.rainbow_constraints import matching_constraints
from src.rainbow_inclusion_exclusion import evaluate, rainbow_union_polynomial
from src.rainbow_probability import probability_bounds

ROOT = Path(__file__).resolve().parents[1]


def checked_matchings(n, edges):
    matchings = tuple(
        indices
        for indices in combinations(range(len(edges)), n)
        if len({edges[i][0] for i in indices}) == n
        and len({edges[i][1] for i in indices}) == n
    )
    if set(matchings) != set(matching_constraints(n, edges)):
        raise RuntimeError("Subset and permutation matching generators disagree.")
    return matchings


def histogram_polynomial(edge_count, histogram):
    """Convert q^m - sum a_k(q)_k by the signed Stirling recurrence."""
    result = [0] * (edge_count + 1)
    result[edge_count] = 1
    row = [1]
    for k in range(1, edge_count + 1):
        row = [0] + [
            (row[j - 1] if j - 1 < len(row) else 0)
            - (k - 1) * (row[j] if j < len(row) else 0)
            for j in range(1, k + 1)
        ]
        for degree, coefficient in enumerate(row):
            result[degree] -= histogram.get(k, 0) * coefficient
    return result


def run():
    saved = json.loads((ROOT / "results/data/sparse_rainbow.json").read_text())
    reference = json.loads((ROOT / "results/data/random_rainbow.json").read_text())
    records = {}
    for name, (n, edges) in hosts().items():
        m = len(edges)
        matchings = checked_matchings(n, edges)
        result = rainbow_union_polynomial(m, matchings)
        histogram = {int(k): v for k, v in saved[name]["avoiding_histogram"].items()}
        if result["union_coefficients"] != histogram_polynomial(m, histogram):
            raise RuntimeError(f"Polynomial coefficients differ for {name}.")
        rows = []
        for q in range(1, 25):
            intersection_sums = [
                Fraction(evaluate(poly, q), q**m)
                for poly in result["intersection_sums"]
            ]
            if any(value < 0 for value in intersection_sums):
                raise RuntimeError("Negative intersection count.")
            exact = Fraction(evaluate(result["union_coefficients"], q), q**m)
            if exact != Fraction(
                reference["hosts"][name]["palettes"][q - 1]["rainbow_probability"]
            ):
                raise RuntimeError(f"Saved probability differs for {name}, q={q}.")
            first, second, _, _ = probability_bounds(matchings, q)
            if (
                intersection_sums[0] != first
                or 2 * intersection_sums[1] != second - first
            ):
                raise RuntimeError("Intersection sums disagree with matching moments.")
            lower = max(
                Fraction(0),
                sum((-1) ** j * value for j, value in enumerate(intersection_sums[:2])),
            )
            upper = min(
                Fraction(1),
                sum((-1) ** j * value for j, value in enumerate(intersection_sums[:3])),
            )
            if not 0 <= lower <= exact <= upper <= 1:
                raise RuntimeError("Bonferroni bounds failed.")
            rows.append(
                {
                    "q": q,
                    "rainbow_probability": str(exact),
                    "bonferroni_lower_2": str(lower),
                    "bonferroni_upper_3": str(upper),
                }
            )
        records[name] = {
            "edges": m,
            "perfect_matchings": len(matchings),
            **result,
            "palettes": rows,
        }
    return {
        "coefficient_order": "ascending powers of q",
        "palette_min": 1,
        "palette_max": 24,
        "hosts": records,
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
            raise SystemExit("FAIL: inclusion-exclusion results differ")
        print("PASS: inclusion-exclusion results match", args.check)
    else:
        for name, host in data["hosts"].items():
            print(
                name,
                host["event_subsets"],
                "event subsets;",
                host["distinct_conflict_graphs"],
                "conflict graphs; q=4:",
                host["palettes"][3]["rainbow_probability"],
            )
