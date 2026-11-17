import sys, time, random
sys.path.insert(0,'$HOME/jones-lanes/theory-restart/mont/cx/cert')
sys.path.insert(0,'$HOME/jones-lanes/theory-restart/mont')
import diagram, wirtinger, tietze, refs, lp
rnd = random.Random(5)
found = 0; tot=0; succ=0; T=0
while found < 40:
    w = refs.rand_width2(rnd, rnd.randint(8, 12))
    if not refs.is_knot(w): continue
    J = lp.J(w)
    if J != {0:1}: continue
    pd = diagram.pd_from_halfword(w)
    if pd.n < 12: continue
    found += 1
    g, r = wirtinger.wirtinger(pd)
    t0=time.time()
    ok, moves, fin, st = tietze.simplify(g, r, seed=1, time_budget=10)
    dt=time.time()-t0; T+=dt
    succ += ok
    print(pd.n, ok, round(dt,2), (len(moves) if moves else None), st, 'final', len(fin[0]), tietze.total_len(fin[1]) if fin else None, flush=True)
print('succ', succ, 'of', found, 'time', round(T,1))
