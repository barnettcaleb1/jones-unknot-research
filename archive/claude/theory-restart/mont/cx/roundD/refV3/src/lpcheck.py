"""refV3: formula-vs-lp.J validation on explicit half-words of vertical closures (parallel).  Each job (n, combo of R(6) indices,
a, N): word = s.l1.(y0)^N.B(u_1)...B(u_n).(x2)^a.u1; compare lp.J(word) with vc.J_vert(a, Y^N(prod v_i)).  Mandatory jobs: all
exact units of the brute force (also det, |Delta(2)|, |Delta(3)| of K) and all non-unit survivors.  Random jobs: stratified."""
import sys, time, pickle, random, multiprocessing as mp
sys.dont_write_bytecode=True
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/src')
OUT='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/'
import vc, lib, lp, alex
R6=lib.rational(6)
def body(cmb,N):
    parts=[vc.word(R6[i][2]) for i in cmb]
    if N: parts=[('y0' if N>0 else 'x0')]*abs(N)+parts
    return '.'.join(x for x in parts if x)
def job(args):
    tag,n,cmb,a,N=args
    w=vc.vert_word(a,body(cmb,N))
    t=time.time()
    J=lp.J(w)
    dt=time.time()-t
    p=vc.Ypow(N,vc.starall([R6[i][1] for i in cmb]))
    J2=vc.J_vert(a,p)
    extra=None
    if tag=='unit' or (J is not None and len(J)==1):
        extra=(alex.alex_eval(w,-1),alex.alex_eval(w,2),alex.alex_eval(w,3))
    return (tag,n,cmb,a,N,w,J==J2,J,J2,round(dt,3),extra)
if __name__=='__main__':
    NJOB=int(sys.argv[1]) if len(sys.argv)>1 else 400
    seed=int(sys.argv[2]) if len(sys.argv)>2 else 7
    d=pickle.load(open(OUT+'brute_n2.pkl','rb'))
    jobs=[('unit',)+tuple(u[:4]) for u in d['exact_units']]
    units=set(tuple(u[:4]) for u in d['exact_units'])
    jobs+=[('surv',)+tuple(s) for s in d['surv'] if tuple(s) not in units]
    rnd=random.Random(seed)
    for i in range(NJOB):
        n=1+i%4
        cmb=tuple(sorted(rnd.randrange(len(R6)) for _ in range(n)))
        a=rnd.choice(list(range(-9,10,2))); N=rnd.randint(-12,12)
        if rnd.random()<0.5: N=rnd.randint(-3,3)
        jobs.append(('rand',n,cmb,a,N))
    print('jobs',len(jobs),flush=True)
    t0=time.time(); res=[]; bad=0
    with mp.Pool(8) as pool:
        for r in pool.imap_unordered(job,jobs):
            res.append(r)
            if not r[6]: bad+=1; print('MISMATCH',r,flush=True)
            if r[0]!='rand': print(r[0],r[1],r[2],'a=%d N=%d'%(r[3],r[4]),'match',r[6],'lpJ',r[7],'det/D2/D3',r[10],flush=True)
            if len(res)%50==0:
                pickle.dump(res,open(OUT+'lpcheck_s%d.pkl'%seed,'wb'))
                print('done %d/%d mismatches %d  %.0fs'%(len(res),len(jobs),bad,time.time()-t0),flush=True)
    pickle.dump(res,open(OUT+'lpcheck_s%d.pkl'%seed,'wb'))
    byn={}
    for r in res:
        if r[0]=='rand': byn[r[1]]=byn.get(r[1],0)+1
    print('FINAL: %d jobs, mismatches %d, random by n %s, %.0fs'%(len(res),bad,byn,time.time()-t0),flush=True)
