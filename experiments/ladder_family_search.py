"""Search for a test family of t matchings on L_k at deficit three, learning from failures.

A CP-SAT model chooses the t gap sets directly. Each candidate is checked by
ladder_defeating_colourings.cpp; every colouring that defeats it becomes a new
constraint, and the model is solved again. The constraints are necessary
conditions, so INFEASIBLE proves that no family of size t exists.

  g++ -O2 -o defeating experiments/ladder_defeating_colourings.cpp
  python experiments/ladder_family_search.py 10 7 300 60    # ends with INFEASIBLE
  python experiments/ladder_family_search.py 10 8 300 60    # ends with FOUND

Arguments: k, t, total seconds, seconds per solve. Needs ortools; 3k-2 <= 64.
"""
import sys, subprocess, os, time
from ortools.sat.python import cp_model
k=int(sys.argv[1]); t=int(sys.argv[2]); budget=float(sys.argv[3]); per=float(sys.argv[4]) if len(sys.argv)>4 else 120
store=f'cegar_k{k}.txt'   # cuts are valid for every family size, so one file per k
cuts=set(open(store).read().split('\n')) if os.path.exists(store) else set(); cuts.discard('')
t0=time.time()
def parse(line): return [list(map(int,c.split())) for c in line.split('|') if c.strip()]
def solve():
    m=cp_model.CpModel()
    x=[[m.NewBoolVar(f'x{i}_{g}') for g in range(k-1)] for i in range(t)]
    f=[[None]*k for _ in range(t)]
    for i in range(t):
        for g in range(k-2): m.AddBoolOr([x[i][g].Not(), x[i][g+1].Not()])
        for c in range(k):
            adj=[x[i][g] for g in (c-1,c) if 0<=g<k-1]
            v=m.NewBoolVar(f'f{i}_{c}'); f[i][c]=v
            for a in adj: m.AddImplication(v,a.Not())
            m.AddBoolOr([v]+adj)
    def lit(i,e):
        if e<k: return f[i][e]
        return x[i][e-k] if e<2*k-1 else x[i][e-(2*k-1)]
    cache={}
    def pv(i,a,b):
        la,lb=lit(i,a),lit(i,b)
        if la is lb: return la
        key=(i,a,b)
        if key not in cache:
            v=m.NewBoolVar(f'p{i}_{a}_{b}'); m.AddImplication(v,la); m.AddImplication(v,lb); m.AddBoolOr([v,la.Not(),lb.Not()]); cache[key]=v
        return cache[key]
    for n,line in enumerate(cuts):
        rs=[]
        for i in range(t):
            r=m.NewBoolVar(f'r{n}_{i}'); rs.append(r)
            for cl in parse(line):
                for a in range(len(cl)):
                    for b in range(a+1,len(cl)): m.AddImplication(r,pv(i,cl[a],cl[b]).Not())
        m.AddBoolOr(rs)
    vals=[sum((1<<g)*x[i][g] for g in range(k-1)) for i in range(t)]
    for i in range(t-1): m.Add(vals[i]<vals[i+1])
    s=cp_model.CpSolver(); s.parameters.max_time_in_seconds=per; s.parameters.num_workers=8
    r=s.Solve(m)
    if r in (cp_model.OPTIMAL,cp_model.FEASIBLE): return 'SAT',[[g for g in range(k-1) if s.Value(x[i][g])] for i in range(t)]
    return s.StatusName(r),None
while time.time()-t0<budget:
    st,fam=solve()
    if fam is None: print("solver:",st,"with",len(cuts),"cuts",flush=True); break
    inp='\n'.join(' '.join(map(str,J)) for J in fam)+'\n'
    r=subprocess.run(['./defeating',str(k),'1500','1'],input=inp,capture_output=True,text=True)
    new=[l.strip() for l in r.stdout.split('\n') if l.strip()]
    print(r.stderr.strip(),"| cuts",len(cuts),flush=True); open(f"lastfam_k{k}.txt","w").write(repr(fam))
    if not new: print("FOUND",fam); break
    cuts.update(new); open(store,'w').write('\n'.join(sorted(cuts)))
