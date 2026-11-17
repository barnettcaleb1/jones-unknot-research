#!/usr/bin/env python3
"""Compare the hybrid positive polynomial of the (Y,E)-normal form of a word with kht++ data:
   hybrid = shift * P_N + (1 + x^4/y) R,  R >= 0 ?   Also report the Newton polygon edge directions of N (data)."""
import sys,os,re,collections,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import run as R
from hybrid import hybrid
from mixed import divide
from hull_formula import hull,edges
def normal_form(sh):
    toks=[]   # ints for Y-powers, 'E'
    for m in re.finditer(r'([YyXx])(\d*)',sh):
        n=int(m.group(2)) if m.group(2) else 1
        for _ in range(n):
            L=m.group(1)
            if L=='Y': toks.append(1)
            elif L=='y': toks.append(-1)
            elif L=='X': toks+=['E',1]
            else: toks+=[-1,'E']
    # reduce
    out=[]
    for tk in toks:
        if tk=='E':
            if out and out[-1]=='E': out.pop()
            else: out.append('E')
        else:
            if out and out[-1]!='E':
                out[-1]+=tk
                if out[-1]==0:
                    out.pop()
                    # after removing a zero power, two E's may become adjacent
                    # (handled lazily below)
            else: out.append(tk)
        # collapse 'E','E' created by zero-removal
        while len(out)>=2 and out[-1]=='E' and out[-2]=='E': out.pop(); out.pop()
    # to sequence n_0, n_1, ..., n_{k-1}  (Y-powers before each E; missing = 0)
    ns=[]; cur=0
    for tk in out:
        if tk=='E': ns.append(cur); cur=0
        else: cur=tk
    return tuple(ns)   # trailing Y power dropped
def strip_prefix(ns):
    """remove degenerate prefix: n_0 = -1 (x at start) or (0,1,...) (X at start)"""
    ns=list(ns)
    while ns:
        if ns[0]==-1: ns=ns[1:]
        elif ns[0]==0 and len(ns)>=2 and ns[1]==1: ns=[0]+ns[2:]
        elif ns[0]==0 and len(ns)>=2:
            # E Y^n E ... starting with E: E(1,0)=(1,-1) = Y^-1 direction: (0,n,...) ~ (n-1,...)
            ns=[ns[1]-1]+ns[2:]
        elif ns[0]==0 and len(ns)==1: ns=[]
        else: break
    return tuple(ns)
if __name__=='__main__':
    C=json.load(open(R.CACHE))
    words=sys.argv[1:] or sorted(set(k.split('|')[0] for k in C))
    stats=collections.Counter(); dirs=collections.Counter()
    for key in words:
        w=key
        # shorthand from full word
        if w.startswith('s.'):
            body=w[len('s.l1.'):-len('.u2')].split('.') if w.startswith('s.l1.') else None
            if body is None or any(t not in ('y0','x0','x1','y1') for t in body): continue
            sh=''.join({'y0':'Y','x0':'y','x1':'X','y1':'x'}[t] for t in body)
        else: sh=w
        rec=R.run(w)
        if rec.get('bn') is None: continue
        an=R.analyse(rec); d=collections.Counter(an['N'])
        ns=strip_prefix(normal_form(sh))
        mixed=not (all(n>0 for n in ns) or all(n<0 for n in ns[1:]) and (not ns or ns[0]<=-2))
        if len(ns)==0:
            stats['trivial']+=1; continue
        try: Hp=hybrid(ns)
        except Exception as e:
            print(sh,ns,'hybrid error',e); continue
        ok=None
        for (a0,b0) in d:
            for (a1,b1) in Hp:
                s=(a1-a0,b1-b0)
                diff=collections.Counter(Hp)
                for (a,b),c in d.items(): diff[(a+s[0],b+s[1])]-=c
                Rr=divide(diff)
                if Rr is not None: ok=(s,sum(Rr.values())); break
            if ok: break
        eds=sorted(set(e[0] for e in edges(hull(list(d))))) if len(d)>2 else []
        for e in eds: dirs[e]+=1
        stats['ok' if ok else 'FAIL']+=1
        print('%-14s nf=%-22s dimN=%3d dimHyb=%3d %s  hull dirs %s'%(sh,ns,sum(d.values()),sum(Hp.values()),('cancel %d pairs'%ok[1]) if ok else 'FAIL',eds))
    print(dict(stats)); print('hull directions over these words:',dict(dirs))
