"""refV3: targeted formula-vs-lp.J validation where it matters most: the vertical closures (|a| >= 3) with the DEEPEST one-ended
cancellation of F = w_1 A + wV t^-3N B (the configurations a unit would need), n = 1..4 from R(6), |N| <= 8."""
import sys, time, pickle, random, multiprocessing as mp
sys.dont_write_bytecode=True
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/src')
OUT='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/'
import vc, lib, lpcheck
R6=lib.rational(6)
def depths(cmb,a,N):
    A,B=vc.Ypow(N,vc.starall([R6[i][1] for i in cmb]))
    W1=vc.add({1:1}, vc.mul(vc.tmono(a),vc.T2P1)); WV=vc.add(vc.shift(vc.tmono(a),1), vc.shift(vc.PHI5,3*a-1))
    S1=vc.mul(W1,A); S2=vc.mul(WV,B); F=vc.add(S1,S2)
    rt=(max(S1)-max(F)) if max(S1)==max(S2) else 0
    rb=(min(F)-min(S1)) if min(S1)==min(S2) else 0
    return rt,rb
if __name__=='__main__':
    rnd=random.Random(5)
    cands=[]
    for n in (1,2,3,4):
        for it in range({1:98,2:3000,3:3000,4:3000}[n]):
            cmb=(it,) if n==1 else tuple(sorted(rnd.randrange(len(R6)) for _ in range(n)))
            p=vc.starall([R6[i][1] for i in cmb]); A,B=p
            for a in [x for x in range(-9,10,2) if abs(x)>=3]:
                W1=vc.add({1:1}, vc.mul(vc.tmono(a),vc.T2P1)); WV=vc.add(vc.shift(vc.tmono(a),1), vc.shift(vc.PHI5,3*a-1))
                for x in (max(WV)+max(B)-max(W1)-max(A), min(WV)+min(B)-min(W1)-min(A)):
                    if x%3==0 and abs(x//3)<=8:
                        rt,rb=depths(cmb,a,x//3); cands.append((max(rt,rb),n,cmb,a,x//3,rt,rb))
    best={}
    for c in sorted(cands,reverse=True):
        if c[1] not in best: best[c[1]]=[]
        if len(best[c[1]])<15: best[c[1]].append(c)
    jobs=[]
    for n in best:
        print('n=%d deepest one-ended cancellations:'%n,[(c[0],c[3],c[4],c[5],c[6]) for c in best[n][:6]],flush=True)
        jobs+=[('deep',c[1],c[2],c[3],c[4]) for c in best[n]]
    t0=time.time(); bad=0; res=[]
    with mp.Pool(6) as pool:
        for r in pool.imap_unordered(lpcheck.job,jobs):
            res.append(r)
            if not r[6]: bad+=1; print('MISMATCH',r,flush=True)
    pickle.dump(res,open(OUT+'lpdeep.pkl','wb'))
    print('targeted deep-cancellation lp.J checks: %d, mismatches %d, %.0fs'%(len(res),bad,time.time()-t0),flush=True)
