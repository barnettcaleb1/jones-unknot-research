# Is the D-symbol a "sum over upstairs lifts" of a weight W on 3-chord diagrams on a circle with the two fixed points marked?
import json, re, itertools
from fractions import Fraction as F
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
import modrank
tab=json.load(open('dtable3.json')); wit=json.load(open('witness_D.json'))
Dp={t:F(v[3])/40 for t,v in tab.items()}
for t,d,v in wit: Dp[t]=F(d)
def parse(t): return re.findall(r'T\d[v^]|[a-h][+-]',t)
def lifts(t):
    toks=parse(t); n=len(toks)
    # positions along k: 1..n ; upstairs circle: f_t=0, K_+ points 1..n, f_b=n+1, K_- points n+2..2n+1 (mirror: p- = 2n+2-p)
    chords={}; Ts=[]
    for i,x in enumerate(toks,1):
        if x[0]=='T': Ts.append(i)
        else: chords.setdefault(x[0],[]).append((i,x[1]))
    names=sorted(chords)
    mir=lambda p: 2*n+2-p
    out=[]
    for choice in itertools.product([0,1],repeat=len(names)):
        ups=[]; sign=1
        for nm,ch in zip(names,choice):
            (p,l),(q,_)=chords[nm]
            if l=='+': c=(p,q) if ch==0 else (mir(p),mir(q))
            else:
                c=(p,mir(q)) if ch==0 else (mir(p),q); sign=-sign
            ups.append(tuple(sorted(c)))
        for tpos in Ts: ups.append(tuple(sorted((tpos,mir(tpos)))))
        out.append((sign,canon(ups,n)))
    return out
def canon(ups,n):
    N=2*n+2   # circle points 0..N-1 with 0=f_t, n+1=f_b
    def relabel(f):
        pts=sorted({f(p) for c in ups for p in c})
        return pts
    best=None
    for refl in (False,True):
        for swap in (False,True):
            def f(p):
                q=p
                if refl: q=(-q)%N           # reflection fixing 0 and n+1 (h)
                if swap: q=(q+(n+1))%N      # rotation by half: swaps f_t and f_b
                return q
            cs=[tuple(sorted((f(a),f(b)))) for a,b in ups]
            # encode cyclic word starting at f_t=0: sequence of chord ids by first appearance, with marker for f_b
            order=sorted({p for c in cs for p in c}|{0,n+1})
            ids={}; word=[]
            for p in order:
                if p==0: word.append('F')
                elif p==n+1: word.append('G')
                else:
                    c=next(c for c in cs if p in c); k=cs.index(c)
                    if k not in ids: ids[k]=len(ids)
                    word.append(ids[k])
            w=tuple(word)
            if best is None or str(w)<str(best): best=w
    return best
types=[t for t in Dp if len(parse(t))<=6]
cols={}
rowsA=[]; b=[]
for t in types:
    row={}
    for s,c in lifts(t):
        cols.setdefault(c,len(cols)); row[cols[c]]=row.get(cols[c],0)+s
    rowsA.append(row); b.append(Dp[t])
A=[[r.get(j,0) for j in range(len(cols))] for r in rowsA]
print('types',len(types),'distinct lifted diagrams',len(cols))
print('(rank A, rank [A|D]) mod primes:',modrank.in_span(A,b))
c=modrank.certificate(A,b)
print('certificate:',None if c is None else (len(c[0]),c[1]))
y,val=c
for i,coef in y.items(): print('  y=%s  type %s  D-symbol/8=%s'%(coef,types[i],b[i]))
