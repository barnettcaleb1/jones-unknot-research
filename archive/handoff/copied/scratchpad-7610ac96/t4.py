import sys, time, random
sys.path.insert(0,'$HOME/jones-lanes/theory-restart/mont/cx/cert')
import diagram, wirtinger, tietze, refs
rnd = random.Random(9)
found = 0; succ=0; T=0; finals={}
while found < 40:
    w = refs.rand_width2(rnd, rnd.randint(6, 12))
    if not refs.is_knot(w): continue
    pd = diagram.pd_from_halfword(w)
    if diagram.jones(pd) == {0:1}: continue
    found += 1
    g, r = wirtinger.wirtinger(pd)
    t0=time.time()
    ok, moves, fin, st = tietze.simplify(g, r, seed=1, time_budget=3, restarts=5)
    dt=time.time()-t0; T+=dt
    succ += ok
    k=(len(fin[0]), len(fin[1])); finals[k]=finals.get(k,0)+1
print('FALSE SUCCESSES', succ, 'of', found, 'time', round(T,1), 'final (gens,rels) histogram', finals)
