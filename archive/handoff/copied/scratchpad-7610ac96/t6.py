import sys, time, random, json
sys.path.insert(0,'$HOME/jones-lanes/theory-restart/mont/cx/cert')
import diagram, wirtinger, tietze, refs, replay, reps
t0=time.time()
for name, gg in reps.target_groups():
    els, rr = reps.class_reps(gg)
    print(name, 'order', len(els), 'classes', [(c[0], c[1]) for c in rr], round(time.time()-t0,2), flush=True)
# E3d Alexander-trivial words
ws=[]
for f in ['e3d_n20_s420.json','e3d_n30_s430.json','e3d_n40_s440.json']:
    d=json.load(open('$HOME/jones-lanes/theory-restart/mont/cx/engineB/out/'+f))
    ws += [x['word'] for x in d['best']]
print(len(ws), 'E3d words')
succ=0
for w in ws[:12]:
    pd = diagram.pd_from_halfword(w); A = diagram.alexander(pd)
    g, r = wirtinger.wirtinger(pd)
    t1=time.time()
    res = reps.find_rep(g, r, A, time_budget=60)
    dt=time.time()-t1
    if res:
        img, gname, note = res
        pair = reps.noncommuting_pair(img, g)
        cert = {'kind':'rep','halfword':w,'degree':len(img[1]),'images':{str(k):list(v) for k,v in img.items()},'noncommuting':list(pair),'group':gname}
        ok, msg = replay.check(cert)
        succ += ok
        print(pd.n, 'A', A, gname, note, round(dt,1), ok, flush=True)
    else:
        G2,R2,el = reps.reduce_for_reps(g, r)
        print(pd.n, 'A', A, 'NO REP', round(dt,1), 'reduced', len(G2), [len(x) for x in R2], flush=True)
print('succ', succ)
