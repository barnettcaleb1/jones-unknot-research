"""per-combo exact verdicts for small multisets containing >= 1 d2pos class (S = top-50 + d2pos), only on the cases that are
open in the uniform run (all other cases are closed for every k by the uniform certificates)."""
import sys, time, pickle, itertools, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
import classes, runner, lpg
from fractions import Fraction as Fr
from multiprocessing import Pool
U=pickle.load(open('uni_t50d2_n0.pkl','rb'))
OPENKEYS=set(k for k,v,info in U['res'] if v=='open')
S=classes.top(50)+classes.d2pos()
CL={cl['name']:cl for cl in lpg.closure_classes()}; TC={tc['name']:tc for tc in lpg.tie_classes()}
def verdict(args):
    combo,nmin=args
    fixk=collections.Counter(combo)
    m_by={}
    opn=[]
    for (cn,nm,m) in OPENKEYS:
        if nm=='tie':
            tc=TC[cn]; mm=sum(S[j].sig*v for j,v in fixk.items())-tc['sigstar']
            if mm!=0: continue
            L=lpg.build(S,dict(tc,end='top'),[],nmin,slice_m=0,nrule=tc['n'],fixk=dict(fixk))
        else:
            cl=CL[cn]
            if m is None:
                rows=dict(lpg.case_rows(cl['p'],cl['q']))[nm]
                L=lpg.build(S,cl,rows,nmin,fixk=dict(fixk))
            else:
                mm=sum(S[j].sig*v for j,v in fixk.items())-cl['sigstar']
                if mm!=m: continue
                rows=dict(lpg.case_rows(cl['p'],cl['q'],m=m)).get(nm)
                if rows is None: continue
                L=lpg.build(S,cl,rows,nmin,slice_m=m,nrule=cl['d0n'],fixk=dict(fixk))
        r=lpg.solve_primal(L)
        if r.status==0: opn.append(((cn,nm,m),round(r.x[L.iN],3)))
    # d=0 slices with |m| > 8 are not in the uniform run: check them directly
    for cl in lpg.closure_classes():
        mm=sum(S[j].sig*v for j,v in fixk.items())-cl['sigstar']
        if abs(mm)<=8: continue
        for nm,rows in lpg.case_rows(cl['p'],cl['q'],m=mm):
            L=lpg.build(S,cl,rows,nmin,slice_m=mm,nrule=cl['d0n'],fixk=dict(fixk))
            r=lpg.solve_primal(L)
            if r.status==0: opn.append(((cl['name'],nm,mm),round(r.x[L.iN],3)))
    return combo,nmin,opn
if __name__=='__main__':
    t0=time.time()
    D=[j for j,c in enumerate(S) if c.label.startswith('d2')]; T=[j for j,c in enumerate(S) if not c.label.startswith('d2')]
    jobs=[((j,),0) for j in D]+[((j,),1) for j in D]
    pairs=[(i,j) for i in D for j in D if i<=j]+[(i,j) for i in D for j in T]
    jobs+=[(p,0) for p in pairs]
    with Pool(9) as P: res=P.map(verdict,jobs,chunksize=8)
    pickle.dump(dict(res=res,labels=[c.label for c in S]),open('pairs_d2.pkl','wb'))
    lab=[c.label for c in S]
    for kind,flt in (('single n>=0',lambda c,n:len(c)==1 and n==0),('single n>=1',lambda c,n:len(c)==1 and n==1),
                     ('d2 x d2 n>=0',lambda c,n:len(c)==2 and c[1] in D),('d2 x top50 n>=0',lambda c,n:len(c)==2 and c[1] in T)):
        sel=[(c,n,o) for c,n,o in res if flt(c,n)]
        no=[x for x in sel if x[2]]
        cc=collections.Counter()
        for c,n,o in no:
            for key,nn in o: cc[(key[0].split(' ')[0]+(' '+key[0].split(' ')[1] if key[0].startswith('H') else ''),key[1])]+=1
        print('%-16s combos %5d  LP-open %5d  closed %5d   open cases: %s'%(kind,len(sel),len(no),len(sel)-len(no),cc.most_common(8)))
    print('time',round(time.time()-t0,1))
