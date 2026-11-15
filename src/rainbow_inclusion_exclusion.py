"""Count rainbow events by inclusion-exclusion and chromatic polynomials.

Coefficients are exact integers in ascending powers of q. The small-graph
limits are 12 edge positions and nine distinct nonempty target sets.
"""

from functools import cache
from itertools import combinations, zip_longest


def evaluate(coefficients, q):
    """Evaluate a polynomial with coefficients ordered from constant upward."""
    value = 0
    for coefficient in reversed(coefficients):
        value = value * q + coefficient
    return value


def _add(first, second):
    return tuple(a + b for a, b in zip_longest(first, second, fillvalue=0))


def _multiply(first, second):
    result = [0] * (len(first) + len(second) - 1)
    for i, a in enumerate(first):
        for j, b in enumerate(second):
            result[i + j] += a * b
    return tuple(result)


def _induced(graph, vertices):
    return tuple(
        sum(1 << j for j, v in enumerate(vertices) if graph[u] >> v & 1)
        for u in vertices
    )


def _contract(graph, u, v):
    """Identify nonadjacent vertices u and v, then remove position v."""
    result = []
    for i, neighbors in enumerate(graph):
        if i == v:
            continue
        if i == u:
            neighbors |= graph[v]
        if neighbors >> v & 1:
            neighbors |= 1 << u
        result.append((neighbors & ((1 << v) - 1)) | ((neighbors >> (v + 1)) << v))
    return tuple(result)


def _chromatic_counter():
    @cache
    def count(graph):
        n = len(graph)
        if n == 0:
            return (1,)

        # Components, including isolated vertices, have independent colorings.
        remaining = (1 << n) - 1
        components = []
        while remaining:
            frontier = remaining & -remaining
            component = 0
            while frontier:
                bit = frontier & -frontier
                frontier ^= bit
                vertex = bit.bit_length() - 1
                component |= bit
                frontier |= graph[vertex] & ~component
            remaining &= ~component
            components.append(tuple(v for v in range(n) if component >> v & 1))
        if len(components) > 1:
            polynomial = (1,)
            for vertices in components:
                polynomial = _multiply(polynomial, count(_induced(graph, vertices)))
            return polynomial

        # A complete graph has the falling-factorial coloring polynomial.
        if all(neighbors.bit_count() == n - 1 for neighbors in graph):
            polynomial = (1,)
            for i in range(n):
                polynomial = _multiply(polynomial, (-i, 1))
            return polynomial

        u = max(
            (i for i in range(n) if graph[i].bit_count() < n - 1),
            key=lambda i: graph[i].bit_count(),
        )
        missing = ((1 << n) - 1) & ~graph[u] & ~(1 << u)
        v = (missing & -missing).bit_length() - 1
        joined = list(graph)
        joined[u] |= 1 << v
        joined[v] |= 1 << u
        # Proper colorings split according to whether u and v have equal colors.
        return _add(count(tuple(joined)), count(_contract(graph, u, v)))

    return count


def chromatic_polynomial(vertex_count, edges):
    """Return the coloring polynomial of a simple graph with at most 12 vertices."""
    if type(vertex_count) is not int or not 0 <= vertex_count <= 12:
        raise ValueError("Need an integer vertex count from 0 through 12.")
    graph = [0] * vertex_count
    for u, v in edges:
        if (
            type(u) is not int
            or type(v) is not int
            or not 0 <= u < vertex_count
            or not 0 <= v < vertex_count
            or u == v
        ):
            raise ValueError("Need distinct endpoints in the vertex range.")
        graph[u] |= 1 << v
        graph[v] |= 1 << u
    counter = _chromatic_counter()
    polynomial = counter(tuple(graph))
    counter.cache_clear()
    return polynomial


def rainbow_union_polynomial(edge_count, matchings):
    """Count assignments with at least one rainbow target, for every palette q.

    Only the edge positions and target family are used. No avoiding-partition
    histogram is read. Targets may have different sizes; unused positions are
    retained as isolated vertices in every conflict graph.
    """
    if type(edge_count) is not int or not 1 <= edge_count <= 12:
        raise ValueError("Need an integer edge count from 1 through 12.")
    matchings = tuple(tuple(matching) for matching in matchings)
    if not 1 <= len(matchings) <= 9:
        raise ValueError("Need one through nine distinct nonempty targets.")
    for matching in matchings:
        if (
            not matching
            or any(type(i) is not int or not 0 <= i < edge_count for i in matching)
            or len(set(matching)) != len(matching)
        ):
            raise ValueError(
                "Targets must contain distinct positions in the edge range."
            )
    if len({frozenset(matching) for matching in matchings}) != len(matchings):
        raise ValueError("Targets must be distinct.")

    conflicts = []
    for matching in matchings:
        graph = [0] * edge_count
        for u, v in combinations(matching, 2):
            graph[u] |= 1 << v
            graph[v] |= 1 << u
        conflicts.append(tuple(graph))

    counter = _chromatic_counter()
    graphs = [(0,) * edge_count]
    by_order = [(0,) * (edge_count + 1) for _ in matchings]
    for mask in range(1, 1 << len(matchings)):
        bit = mask & -mask
        previous = graphs[mask ^ bit]
        new = conflicts[bit.bit_length() - 1]
        graph = tuple(a | b for a, b in zip(previous, new))
        graphs.append(graph)
        order = mask.bit_count()
        by_order[order - 1] = _add(by_order[order - 1], counter(graph))

    union = [0] * (edge_count + 1)
    for order, polynomial in enumerate(by_order, 1):
        sign = 1 if order % 2 else -1
        for degree, coefficient in enumerate(polynomial):
            union[degree] += sign * coefficient
    result = {
        "union_coefficients": union,
        "intersection_sums": [list(polynomial) for polynomial in by_order],
        "event_subsets": len(graphs) - 1,
        "distinct_conflict_graphs": len(set(graphs[1:])),
        "chromatic_subproblems": counter.cache_info().misses,
    }
    counter.cache_clear()
    return result
