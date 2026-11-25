"""Search a relaxation of tournament reversal paths below a fixed barrier."""
from collections import Counter, deque
from itertools import accumulate


def cheaper_reachable(t, cap):
    n = 10*t + 1
    initial = tuple(range(4*t)) + (7*t,) * (6*t+1)
    costs = [d * (n-1-d) * (n-2-d) // 2 for d in range(n)]
    queue = deque([(initial, 0)])
    visited = {initial}
    while queue:
        scores, cost = queue.popleft()
        counts = Counter(scores)
        for tail in counts:
            for head in counts:
                if not tail or head == n-1 or (tail == head and counts[tail] < 2):
                    continue
                change = costs[tail-1] + costs[head+1] - costs[tail] - costs[head]
                new_cost = cost + change
                if new_cost > cap:
                    continue
                updated = list(scores)
                updated.remove(tail)
                updated.remove(head)
                updated.extend((tail-1, head+1))
                candidate = tuple(sorted(updated))
                if candidate in visited:
                    continue
                if any(total < k*(k-1)//2
                       for k, total in enumerate(accumulate(candidate), start=1)):
                    continue
                if new_cost < 0:
                    return True, len(visited)
                visited.add(candidate)
                queue.append((candidate, new_cost))
    return False, len(visited)


def explicit_path(t):
    lower = 4*t
    upper = 6*t+1
    n = lower + upper
    arcs = set()
    for a in range(n):
        for b in range(a):
            if b < lower or (b-a) % upper <= upper//2:
                arcs.add((a, b))
            else:
                arcs.add((b, a))

    def stars():
        degrees = Counter(a for a, b in arcs)
        return sum(d * (n-1-d) * (n-2-d) // 2 for d in degrees.values())

    start = stars()
    outgoing = sorted(b for a, b in arcs if a == lower and b >= lower)
    heights = [0]
    for b in outgoing[:t+3]:
        arcs.remove((lower, b))
        arcs.add((b, lower))
        heights.append(stars()-start)
    return heights


if __name__ == "__main__":
    for t in range(2, 11):
        peak = max(h*(h+1)*(t+2-h)//2 for h in range(1, t+2))
        reached, size = cheaper_reachable(t, peak-1)
        heights = explicit_path(t)
        assert len(heights) == t+4 and heights[-1] < 0
        assert max(heights) == peak and not reached
        print(t, peak, size, flush=True)
