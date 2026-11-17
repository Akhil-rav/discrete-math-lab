"""Exact minimum hitting set for the survivor sets written by ladder_survivor_sets.cpp.

  g++ -O2 -o survivors experiments/ladder_survivor_sets.cpp
  ./survivors 12 3 > sets12.txt
  python experiments/ladder_hitting_set.py sets12.txt 900     # needs: pip install ortools

Recorded on 2026-11-16 for deficit three: k = 8,...,14 all give 8 (status OPTIMAL).
For k = 15 this solver proved only a lower bound of 7; families of size 8 for k = 15, 16
are recorded in results/ladder_test_families.md.
"""
import sys
from ortools.sat.python import cp_model
lines=open(sys.argv[1]).read().split('\n'); n=int(lines[0]); sets=[list(map(int,l.split())) for l in lines[1:] if l.strip()]
m=cp_model.CpModel(); x=[m.NewBoolVar(str(i)) for i in range(n)]
for s in sets: m.AddBoolOr([x[i] for i in s])
m.Minimize(sum(x)); s=cp_model.CpSolver(); s.parameters.max_time_in_seconds=float(sys.argv[2]); s.parameters.num_workers=8
r=s.Solve(m); print(sys.argv[1], s.StatusName(r), "h =", int(s.ObjectiveValue()), "bound", s.BestObjectiveBound())
