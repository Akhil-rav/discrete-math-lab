"""Deterministic bounded suite. Run from root: python -m experiments.reproduce.

Use --output PATH to write JSON; --check PATH to compare with checked-in data.
The mathematical contracts and scope are in experiments/README.md.
"""

import argparse
import json
from pathlib import Path

from experiments.classify_k33 import run as classification
from experiments.color_coding_small_cases import run as color_coding
from experiments.expansion_small_cases import run as expansion
from experiments.rainbow_complete_bipartite import exhaustive_search
from experiments.rainbow_progressions import run as progressions
from experiments.regular_bipartite_matchings import verify_case


def run():
    regular = []
    for n in range(1, 6):
        for d in range(1, n+1):
            checked, failures = verify_case(n, d)
            if failures:
                raise RuntimeError("Regular matching benchmark failed.")
            regular.append({"n": n, "d": d, "graphs_checked": checked, "failures": failures})
    rainbow = {}
    for n in (2, 3):
        checked, best, count, histogram, witness = exhaustive_search(n)
        rainbow[str(n)] = {"patterns_checked": checked, "maximum_avoiding_colors": best,
                           "extremal_patterns": count, "avoiding_histogram": histogram,
                           "witness": witness}
    return {"schema_version": 1, "regular_bipartite": regular,
            "rainbow_bipartite": rainbow, "k33_classification": classification(),
            "progressions": progressions(), "color_coding": color_coding(),
            "expansion": expansion()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path)
    group.add_argument("--check", type=Path)
    args = parser.parse_args()
    # Round-trip converts integer mapping keys and tuples into JSON conventions.
    result = json.loads(json.dumps(run()))
    if args.check:
        if result != json.loads(args.check.read_text(encoding="utf-8")):
            raise SystemExit("FAIL: regenerated results differ")
        print("PASS: all bounded results match " + str(args.check))
    elif args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        print("Wrote " + str(args.output))
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
