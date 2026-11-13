"""Edge-coloring utilities for rainbow-matching experiments."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Iterable, Mapping

Vertex = Hashable
Edge = tuple[Vertex, Vertex]
Color = Hashable


@dataclass(frozen=True)
class EdgeColoring:
    """A finite edge coloring represented by a map edge -> color."""

    colors: Mapping[Edge, Color]

    def color(self, edge: Edge) -> Color:
        return self.colors[edge]

    def is_rainbow(self, edges: Iterable[Edge]) -> bool:
        """Return True when all supplied edges receive different colors."""

        color_list = [self.color(edge) for edge in edges]
        return len(color_list) == len(set(color_list))
