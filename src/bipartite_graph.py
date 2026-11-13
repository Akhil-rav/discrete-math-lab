"""Minimal bipartite graph utilities for discrete-math experiments.

The implementation is intentionally small and readable so that later
experiments can be checked independently of a large graph library.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Hashable, Iterable, Set

Vertex = Hashable


@dataclass
class BipartiteGraph:
    left: Set[Vertex]
    right: Set[Vertex]
    adjacency: Dict[Vertex, Set[Vertex]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.left & self.right:
            raise ValueError("The two vertex classes must be disjoint.")

        for u in self.left:
            self.adjacency.setdefault(u, set())

        for u, neighbors in self.adjacency.items():
            if u not in self.left:
                raise ValueError("Adjacency keys must lie in the left vertex class.")
            if not neighbors <= self.right:
                raise ValueError("Every neighbor of a left vertex must lie on the right.")

    def add_edge(self, u: Vertex, v: Vertex) -> None:
        if u not in self.left or v not in self.right:
            raise ValueError("Edges must go from the left class to the right class.")
        self.adjacency.setdefault(u, set()).add(v)

    def neighbors(self, u: Vertex) -> Set[Vertex]:
        if u not in self.left:
            raise ValueError("This representation stores neighbors of left vertices.")
        return set(self.adjacency.get(u, set()))

    def degree_left(self, u: Vertex) -> int:
        return len(self.neighbors(u))

    def edges(self) -> Iterable[tuple[Vertex, Vertex]]:
        for u in self.left:
            for v in self.adjacency.get(u, set()):
                yield (u, v)

    def is_left_regular(self) -> bool:
        degrees = {self.degree_left(u) for u in self.left}
        return len(degrees) <= 1
