"""Matching algorithms for small bipartite graphs.

The first routine uses augmenting paths to compute a maximum matching.
It is written directly rather than delegating to a graph package so the
algorithm can be studied and modified in later experiments.
"""

from __future__ import annotations

from typing import Dict, Hashable, Optional

from .bipartite_graph import BipartiteGraph, Vertex


def maximum_matching(graph: BipartiteGraph) -> Dict[Vertex, Vertex]:
    """Return a maximum matching as a map from left vertices to right vertices."""

    matched_right: Dict[Vertex, Vertex] = {}

    def augment(u: Vertex, seen: set[Vertex]) -> bool:
        for v in graph.neighbors(u):
            if v in seen:
                continue
            seen.add(v)

            if v not in matched_right or augment(matched_right[v], seen):
                matched_right[v] = u
                return True

        return False

    for u in graph.left:
        augment(u, set())

    return {u: v for v, u in matched_right.items()}


def has_perfect_matching(graph: BipartiteGraph) -> bool:
    """Check for a matching covering both vertex classes (which must be equal)."""

    if len(graph.left) != len(graph.right):
        return False

    return len(maximum_matching(graph)) == len(graph.left)


def unmatched_left_vertex(
    graph: BipartiteGraph, matching: Dict[Vertex, Vertex]
) -> Optional[Vertex]:
    """Return one unmatched left vertex, if any."""

    for u in graph.left:
        if u not in matching:
            return u
    return None
