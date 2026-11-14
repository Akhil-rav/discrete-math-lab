"""Small exact examples for the Hoory-Linial-Wigderson survey; not constructions.

Run: python -m experiments.expansion_small_cases
"""

import json
from src.expansion import edge_expansion, walk_total_variation


def run():
    examples = {
        "K4": [set(range(4))-{v} for v in range(4)],
        "C6": [{(v-1)%6, (v+1)%6} for v in range(6)],
        "K3,3": [set(range(3, 6)) if v < 3 else set(range(3)) for v in range(6)],
        "2K3": [set(range(0 if v < 3 else 3, 3 if v < 3 else 6))-{v}
                 for v in range(6)],
    }
    results = {}
    for name, adj in examples.items():
        h, subset = edge_expansion(adj)
        results[name] = {"h": str(h), "minimizing_set": list(subset),
                         "lazy_tv": list(map(str, walk_total_variation(adj, 8))),
                         "nonlazy_tv": list(map(str, walk_total_variation(adj, 8, False)))}
    return results


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
