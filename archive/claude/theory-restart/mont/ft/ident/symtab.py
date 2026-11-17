# symbol tables: for random singular configurations (half-word + m flip sites), the canonical symbol
#   sym(v) = prod(site signs) * sum_S (-1)^|S| v(w_S)
# of moments and constituent-knot invariants, grouped by the equivariant chord diagram type.
import sys, random, json, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import diag, lp, chord, flat_search as fs
from fractions import Fraction as F
def M(Jn,k): return sum(c*(-1)**(e%2)*e**k for e,c in Jn.items())
def flip(tokens, idxs):
    t=list(tokens)
    for i in idxs: a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
KEYS=['K','Kin','Kout','Uin','Uout']
def values(w, want_inv=True):
    J=lp.J(w)
    if J is None: return None
    vals={'M2':M(J,2),'M3':M(J,3),'M4':M(J,4),'M5':M(J,5)}
    if want_inv:
        inv=diag.all_invariants(w)
        if inv is None or any(inv[k] is None for k in KEYS): return None
        for k in KEYS:
            for q in ('a2','v3','j4','a4'): vals[k+'.'+q]=inv[k][q]
    return vals
def config_symbol(w, sites, want_inv=True):
    toks=w.split('.')            # toks[0]=='s'; letter index i <-> toks[i+1]
    alt={}
    for S in itertools.product([0,1],repeat=len(sites)):
        ww=flip(toks,[s+1 for s,b in zip(sites,S) if b])
        vals=values(ww,want_inv)
        if vals is None: return None
        sg=(-1)**sum(S)
        for kk,v in vals.items(): alt[kk]=alt.get(kk,0)+sg*v
    sg=chord.site_signs(w,sites); pr=1
    for s in sites: pr*=sg[s]
    return {k:pr*v for k,v in alt.items()}
if __name__=='__main__':
    seed=int(sys.argv[1]); m=int(sys.argv[2]); N=int(sys.argv[3]); want=(len(sys.argv)<5 or sys.argv[4]!='noinv')
    rnd=random.Random(seed); out=[]; tries=0
    while len(out)<N and tries<20000:
        tries+=1
        w=fs.gen(rnd,rnd.randint(6,14))
        if not w or lp.J(w) is None: continue
        toks=w.split('.')[1:]
        fl=[i for i,a in enumerate(toks) if a[0] in 'xy']
        if len(fl)<m: continue
        sites=sorted(rnd.sample(fl,m))
        d=chord.diagram(w,sites)
        if d is None: continue
        sym=config_symbol(w,sites,want)
        if sym is None: continue
        out.append(dict(w=w,sites=sites,type=chord.dstr(d),sym={k:str(v) for k,v in sym.items()}))
    json.dump(out,open('symtab_m%d_s%d.json'%(m,seed),'w'))
    # consistency report
    by={}
    for r in out: by.setdefault(r['type'],[]).append(r)
    print('m',m,'configs',len(out),'types',len(by))
    for ty in sorted(by,key=lambda t:(-len(by[t]),t)):
        rs=by[ty]
        line=[]
        for key in ['M2','M3','M4']+[k+'.a2' for k in KEYS]+[k+'.v3' for k in KEYS]:
            if key not in rs[0]['sym']: continue
            vs=sorted(set(F(r['sym'][key]) for r in rs))
            line.append('%s=%s'%(key,vs[0] if len(vs)==1 else ('{%d vals}'%len(vs))))
        print('%-14s n=%3d  '%(ty,len(rs))+' '.join(line))
