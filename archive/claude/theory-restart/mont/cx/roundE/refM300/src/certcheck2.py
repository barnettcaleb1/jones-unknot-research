"""generalised own checker: as certcheck.check_cert, plus extra equality rows fixing class multiplicities (k_j = value),
appended after the nrule row (lpgen build order: flows, case rows, slice, nrule-eq, extra-eq | kmin, nrule-ge)."""
import sys
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import certcheck as CC
def check_cert_fix(S,cl,nm,rows,m,nrule,kmin,nmin,u,w,fix=(),NS=19,want=False):
    ncase=len(rows); ns=1 if m is not None else 0; neq=1 if (nrule is not None and nrule[0]=='eq') else 0
    nge=1 if (nrule is not None and nrule[0]=='ge') else 0; nk=1 if kmin else 0; nf=len(fix)
    if len(u)!=NS+ncase+ns+neq+nf or len(w)!=nk+nge: return False,{'err':'length','lu':len(u),'lw':len(w)}
    if any(x<0 for x in w): return False,{'err':'negative w'}
    uc=u[NS:NS+ncase]; us=u[NS+ncase] if ns else Fr(0); un=u[NS+ncase+ns] if neq else Fr(0)
    uf=u[NS+ncase+ns+neq:]
    wk=w[0] if nk else Fr(0); wn=w[nk] if nge else Fr(0)
    off=Fr(nrule[1]) if nrule is not None else Fr(0)
    if ncase:
        msub=m if nm.startswith('d=0') else None
        mine=CC.my_rows(nm,cl['p'],cl['q'],m)
        th=[CC.their_vec(r,msub) for r in rows]
        for variant in mine:
            if not (CC.rank(variant+th)==CC.rank(variant)): return False,{'err':'row not implied by own derivation'}
    sigstar=cl['sigstar']
    ca=sum(ui*r[0][0] for ui,r in zip(uc,rows)); cq=sum(ui*r[0][1] for ui,r in zip(uc,rows))
    clq=sum(ui*r[0][2] for ui,r in zip(uc,rows)); cL=sum(ui*r[0][3] for ui,r in zip(uc,rows))
    g0=CC.gmin(ca,cq,clq,cL) if ncase else Fr(0)
    if g0 is None: return False,{'err':'G unbounded below on rational boxes'}
    end=cl.get('end','top'); fixd=dict()
    for (j,val),uu in zip(fix,uf): fixd[j]=(val,uu)
    minc=None; const_fix=Fr(0)
    for j,key in enumerate(S):
        top,bot,sig,dl=key; ra,la,rb,lb=(top if end=='top' else bot)
        v=sum(ui*(r[1][1]*ra+r[1][2]*la+r[1][3]*rb+r[1][4]*lb+r[1][5]*sig) for ui,r in zip(uc,rows))
        col=-v+us*sig-un*dl-wk+wn*dl
        if j in fixd:
            val,uu=fixd[j]; col+=uu; const_fix-=uu*val
        minc=col if minc is None else min(minc,col)
    cn=un-wn
    const=-sum(ui*(r[1][0]-r[1][5]*sigstar) for ui,r in zip(uc,rows))-us*((m if m is not None else 0)+sigstar)-un*off+wk*kmin+wn*off+const_fix
    ok=(minc>=0) and (g0+cn>=0) and ((g0+cn)*nmin+const>0)
    return ok,dict(g0=g0,mincol=minc,cn=cn,const=const)
