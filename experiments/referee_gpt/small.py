"""Independent finite referee computation. Requires python-sat (Cadical195).

Run this file to print the deficit-three results. Each counterexample
is a nonempty set of rainbow matchings on a real coloring, hence a necessary
hitting clause. An unsatisfiable master instance at a given bound proves
that bound impossible even when only some such clauses have been generated.
An admissible master solution with no counterexample is a sufficient list.
For k >= 7 every hitting clause is generated upfront, by partition shape.
"""
import json
from itertools import combinations

from pysat.card import CardEnc, EncType
from pysat.solvers import Cadical195


def vertex_matchings(k):
    edges = [(2*i, 2*i+1) for i in range(k)]
    edges += [(i, i+2) for i in range(2*k-2)]
    def visit(free, selected):
        if not free:
            yield tuple(selected)
            return
        v = min(free)
        for e, (a, b) in enumerate(edges):
            if v in (a,b) and a in free and b in free:
                yield from visit(free - {a,b}, selected + [e])
    return list(visit(set(range(2*k)), [])), len(edges)


def constraints_three(rows, m):
    """Enumerate partitions by nontrivial block shape, ignoring singleton blocks."""
    everything = (1 << len(rows)) - 1
    incident = [sum(1 << i for i, row in enumerate(rows) if e in row) for e in range(m)]
    pairs = {(a,b): incident[a] & incident[b] for a,b in combinations(range(m), 2)}
    def collisions(block):
        mask = 0
        for pair in combinations(block, 2):
            mask |= pairs[pair]
        return mask
    survivors = {everything ^ collisions(q) for q in combinations(range(m),4)}
    for triple in combinations(range(m),3):
        alive = everything ^ collisions(triple)
        for pair in combinations(sorted(set(range(m))-set(triple)),2):
            survivors.add(alive & ~pairs[pair])
    for a,b,c,e,f,g in combinations(range(m),6):
        rest = [b,c,e,f,g]
        for j, partner in enumerate(rest):
            u,v,w,x = rest[:j] + rest[j+1:]
            live = everything ^ pairs[a,partner]
            for p,q in [((u,v),(w,x)),((u,w),(v,x)),((u,x),(v,w))]:
                survivors.add(live & ~(pairs[p] | pairs[q]))
    survivors.discard(0)
    return survivors


def members(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def master(n, masks, bound):
    clauses = [[i+1 for i in members(mask)] for mask in masks]
    clauses += CardEnc.atmost(list(range(1,n+1)), bound, top_id=n).clauses
    with Cadical195(bootstrap_with=clauses) as sat:
        if sat.solve():
            return [i for i in range(n) if sat.get_model()[i] > 0]
    return None


class Adversary:
    """Encode equivalence relations on edges, exact deficit and rainbow row flags."""
    def __init__(self, rows, m, deficit):
        clauses = []
        eq = {p:i for i,p in enumerate(combinations(range(m),2),1)}
        top = len(eq)
        for a,b,c in combinations(range(m),3):
            x,y,z = eq[a,b], eq[b,c], eq[a,c]
            clauses.extend([[-x,-y,z],[-y,-z,x],[-z,-x,y]])
        repeats = []
        for e in range(1,m):
            top += 1
            repeats.append(top)
            earlier = [eq[f,e] for f in range(e)]
            clauses.append([-top,*earlier])
            clauses.extend([[-v,top] for v in earlier])
        cardinality = CardEnc.equals(repeats, deficit, top_id=top, encoding=EncType.seqcounter)
        clauses += cardinality.clauses
        top = max(top, cardinality.nv)
        self.flags = []
        for row in rows:
            top += 1
            self.flags.append(top)
            equalities = [eq[p] for p in combinations(sorted(row),2)]
            clauses.append([top,*equalities])
            clauses.extend([[-top,-x] for x in equalities])
        clauses.append(self.flags)
        self.solver = Cadical195(bootstrap_with=clauses)

    def counterexample(self, indices):
        if not self.solver.solve(assumptions=[-self.flags[i] for i in indices]):
            return None
        true = set(self.solver.get_model())
        return sum(1<<i for i,v in enumerate(self.flags) if v in true)


def minimum(k, d):
    rows,m = vertex_matchings(k)
    masks = set()
    oracle = None
    if k >= 7:
        assert d == 3
        masks = constraints_three(rows,m)
    else:
        oracle = Adversary(rows,m,d)
        # Seed with genuine singleton constraints, where available.
        for i in range(len(rows)):
            seed = oracle.counterexample([j for j in range(len(rows)) if j != i])
            if seed is not None:
                masks.add(seed)
    bound = sum(mask.bit_count() == 1 for mask in masks)
    while True:
        candidate = master(len(rows),masks,bound)
        if candidate is None:
            bound += 1
            continue
        obstruction = oracle.counterexample(candidate) if oracle else None
        if obstruction is None:
            if oracle:
                oracle.solver.delete()
            return {"k":k,"d":d,"h":len(candidate),"test_gap_sets":[
                sorted((e-k)//2 for e in rows[i] if e>=k and (e-k)%2==0)
                for i in candidate]}
        assert obstruction not in masks
        masks.add(obstruction)


if __name__ == "__main__":
    for k in range(4, 9):
        print(json.dumps(minimum(k, 3)), flush=True)
