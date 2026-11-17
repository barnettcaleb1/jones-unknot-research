"""Verify units from an e2 pickle (two-child roots): exact lp.J of the halfword (when short), det, Delta(2), Delta(3)."""
import sys, pickle, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import vc, lp, alex
def pair_tree(mu,N,T1,T2):
    kids=[T1,T2]+([('w',('Y' if N>0 else 'y')*abs(N))] if N else [])
    return ('n',-mu,kids)
def check(units, exactJ=True, maxlen=60):
    out=collections.Counter(); fl=[]
    for u in units:
        mu,N,T1,T2=u[:4]
        T=pair_tree(mu,N,T1,T2); w=vc.hw(T)
        Jc=vc.Jtree(T)
        det=alex.alex_eval(w,-1)
        Jd=lp.J(w) if (exactJ and len(w.split('.'))<=maxlen) else 'skip'
        tag=(Jc=={0:1}, Jd if Jd=='skip' else Jd=={0:1})
        if det is None: out['notknot']+=1; fl.append(('notknot',w)); continue
        if det!=1: out['NONTRIVIAL det']+=1; fl.append(('NONTRIVIAL det=%d'%det,w,tag)); continue
        d2=alex.alex_eval(w,2); d3=alex.alex_eval(w,3)
        if d2!=1 or d3!=1: out['NONTRIVIAL Delta']+=1; fl.append(('NONTRIVIAL D2=%s D3=%s'%(d2,d3),w,tag)); continue
        out['det=D2=D3=1']+=1; fl.append(('trivial-looking',w,tag))
    return out,fl
if __name__=='__main__':
    r=pickle.load(open(sys.argv[1],'rb'))
    out,fl=check(r['units'], exactJ=(len(sys.argv)>2))
    print(sys.argv[1],'units',len(r['units']),dict(out))
    for f in fl[:40]: print(f)
