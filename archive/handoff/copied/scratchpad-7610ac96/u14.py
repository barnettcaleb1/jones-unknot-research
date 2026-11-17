import sys, json, time
sys.path.insert(0,'$HOME/jones-lanes/theory-restart/mont/cx/cert')
sys.path.insert(0,'$HOME/jones-lanes/theory-restart/mont')
import lp, replay, diagram, wirtinger, tietze
ws = json.load(open('$HOME/jones-lanes/theory-restart/mont/cx/cert/out/mitm77_UNRESOLVED_14.json'))
for w in ws:
    J = lp.J(w); Vp = replay.VK_project(w); pd = diagram.pd_from_halfword(w)
    g, r = wirtinger.wirtinger(pd)
    t0 = time.time()
    ok, mv, fin, st = tietze.simplify(g, r, seed=7, time_budget=20, max_total=4000, restarts=200)
    print(w, 'J=1' if J == {0:1} else J, 'Vproj=1' if Vp == {0:1} else Vp, pd.n, 'tietze', ok, st['attempts'], (len(fin[0]), len(fin[1]), tietze.total_len(fin[1])), round(time.time()-t0,1), flush=True)
