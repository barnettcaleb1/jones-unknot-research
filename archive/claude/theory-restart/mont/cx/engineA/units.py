"""Verify units from a scan pickle: build halfword, exact lp.J (if word not too long), det, Delta(2), Delta(3)."""
import sys, pickle, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import vc, lp, alex
def unit_word(u):
    kind,par,N,T=u[0],u[1],u[2],u[3]
    if kind=='H':
        kids=[T]+([('w',('Y' if N>0 else 'y')*abs(N))] if N else [])
        return vc.hw(('n',-par,kids))
    else:
        body=vc.word(('p',[T]+([('w',('Y' if N>0 else 'y')*abs(N))] if N else [])))
        return vc.vert_word(par,body)
def check(units, maxlen=70, verbose=True):
    out=collections.Counter(); flagged=[]
    for u in units:
        w=unit_word(u)
        n=len(w.split('.'))
        det=alex.alex_eval(w,-1)
        if det is None: out['notknot?']+=1; flagged.append(('notknot',w)); continue
        if det!=1:
            out['det!=1']+=1; flagged.append(('NONTRIVIAL det=%d'%det,w)); continue
        d2=alex.alex_eval(w,2); d3=alex.alex_eval(w,3)
        if d2!=1 or d3!=1:
            out['Delta!=1']+=1; flagged.append(('NONTRIVIAL Delta(2)=%s Delta(3)=%s'%(d2,d3),w)); continue
        out['det=Delta=1']+=1
    return out, flagged
if __name__=='__main__':
    r=pickle.load(open(sys.argv[1],'rb'))
    out,fl=check(r['units'])
    print(sys.argv[1],'units',len(r['units']),dict(out))
    for f in fl[:20]: print(f)
