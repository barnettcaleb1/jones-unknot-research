#!/usr/bin/env python3
"""Compare J from kht++ (N(T) lattice set) with the matrix formula J_w, up to a unit +-t^n.  usage: jcheck.py word ..."""
import sys,os,re,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import run as R, jmatrix as JM
def blocks_of(sh):
    L=[]
    for m in re.finditer(r'([YyXx])(\d*)',sh):
        n=int(m.group(2)) if m.group(2) else 1
        L.append((m.group(1),n))
    # group into (a,b) blocks: letters alternate Y-type, X-type
    out=[]; i=0
    while i<len(L):
        a=0; b=0
        if L[i][0] in 'Yy': a=L[i][1]*(1 if L[i][0]=='Y' else -1); i+=1
        if i<len(L) and L[i][0] in 'Xx': b=L[i][1]*(1 if L[i][0]=='X' else -1); i+=1
        out.append((a,b))
    return out
def norm(J):
    J={e:c for e,c in J.items() if c}
    lo=min(J); s=1 if J[max(J)]>0 else -1
    return tuple(sorted((e-lo,c) for e,c in J.items())), tuple(sorted((e-lo,-c) for e,c in J.items()))
if __name__=='__main__':
    for w in sys.argv[1:]:
        rec=R.run(w,120)
        if rec.get('bn') is None: print(w,'no data'); continue
        an=R.analyse(rec)
        Jd=R.Jpoly(an)
        Jm=JM.Jw(blocks_of(w))
        a=norm(Jd); b=norm(Jm)
        print(w,'dimN=%d'%len(an['N']),'MATCH' if (a[0] in b) else 'DIFFER data=%s formula=%s'%(Jd,dict(sorted(Jm.items()))),flush=True)
