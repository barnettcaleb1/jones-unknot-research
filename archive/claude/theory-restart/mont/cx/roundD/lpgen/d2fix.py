"""ONE (or two) d2pos boxes fixed + ANY multiset of top-300 classes + any n >= 0 rational boxes: uniform LP in the top-300
multiplicities.  Only the case-LPs open in the uniform top-300+d2pos run need checking (all others are closed for every k)."""
import sys, pickle, time, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
import classes, runner, lpg
from fractions import Fraction as Fr
from multiprocessing import Pool
U=pickle.load(open('uni_t300d2_n0.pkl','rb'))
OPENKEYS=sorted(set(k for k,v,info in U['res'] if v=='open'),key=str)
S=classes.top(300)+classes.d2pos()
NT=300
CL={cl['name']:cl for cl in lpg.closure_classes()}; TC={tc['name']:tc for tc in lpg.tie_classes()}
def run(fixD):
    """fixD: dict j->mult for d2pos indices (j >= NT); top multiplicities free (>= 0)."""
    extra=[('eq',{j:Fr(1)},Fr(v)) for j,v in fixD.items()]+[('eq',{j:Fr(1)},Fr(0)) for j in range(NT,len(S)) if j not in fixD]
    sigD=sum(S[j].sig*v for j,v in fixD.items())
    opn=[]
    for (cn,nm,m) in OPENKEYS:
        if nm=='tie':
            tc=TC[cn]
            L=lpg.build(S,dict(tc,end='top'),[],0,kmin=1,slice_m=0,nrule=tc['n'],extra=extra)
        else:
            cl=CL[cn]
            if m is None:
                L=lpg.build(S,cl,dict(lpg.case_rows(cl['p'],cl['q']))[nm],0,kmin=1,extra=extra)
            else:
                rows=dict(lpg.case_rows(cl['p'],cl['q'],m=m)).get(nm)
                if rows is None: continue
                L=lpg.build(S,cl,rows,0,kmin=1,slice_m=m,nrule=cl['d0n'],extra=extra)
        r=lpg.solve_primal(L)
        if r.status==0:
            kt=sum(r.x[:NT]); opn.append(((cn,nm,m),round(r.x[L.iN],2),round(kt,2)))
    # vertical d=0 slices 9 <= |m| <= 14 (beyond the uniform run's window; the generalised phi-lemma bounds the rest, REPORT s.4)
    for cl in lpg.closure_classes():
        if cl['kind']!='V': continue
        for m in [x for x in range(-14,15) if abs(x)>8]:
            for nm,rows in lpg.case_rows(cl['p'],cl['q'],m=Fr(m)):
                L=lpg.build(S,cl,rows,0,kmin=1,slice_m=Fr(m),nrule=cl['d0n'],extra=extra)
                r=lpg.solve_primal(L)
                if r.status==0: opn.append(((cl['name'],nm,m),round(r.x[L.iN],2),round(sum(r.x[:NT]),2)))
    return fixD,opn
if __name__=='__main__':
    t0=time.time()
    jobs=[{j:1} for j in range(NT,len(S))]
    with Pool(4) as P: res=P.map(run,jobs)
    lab=[c.label for c in S]
    clo=[lab[list(f)[0]] for f,o in res if not o]; op=[(lab[list(f)[0]],o) for f,o in res if o]
    print('ONE d2pos box + ANY top-300 multiset + any n: closed for %d/60 d2 classes (box weight %d)'%(len(clo),sum(S[lab.index(c)].w for c in clo)))
    print('closed:',clo)
    for l,o in op: print('  OPEN',l,[(k[0],k[1],k[2],n,kt) for k,n,kt in o][:6])
    pickle.dump(dict(res=res,labels=lab),open('d2fix1.pkl','wb'))
    print('time',round(time.time()-t0,1))
