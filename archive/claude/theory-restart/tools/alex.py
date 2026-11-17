#!/usr/bin/env python3
"""Alexander polynomial of the strongly invertible knot given by a kht++ half-diagram word 's.<...>'.
symmetrize() follows Tangle::complete_symmetry in kht++ (sources/modules/Tangles.cpp).
alex_eval(word, t) returns |Delta(t)| up to a power of |t| (None if the completed diagram is not a knot)."""
import sys
def parse(word):
    w=word.strip()
    if w.startswith('s.'): w=w[2:]
    return [(tok[0],int(tok[1:])) for tok in w.split('.') if tok]
def symmetrize(half):
    hw=1; full=[]
    for c,s in half:
        if s==0:
            if c not in 'xy': return None
            full.append((c,hw-1))
        elif c in 'xy':
            full.append((c,hw+s-1)); full.append((c,hw-s-1))
        elif c=='l':
            full.append(('l',hw+s-1)); full.append(('r',hw-s+1)); hw+=2
        elif c=='r':
            full.append(('r',hw+s-1)); full.append(('l',hw-s+1)); hw+=2
        elif c=='u':
            full.append(('u',hw+s-1)); full.append(('u',hw-s-1)); hw-=2
    full.append(('u',0))
    return full
class UF:
    def __init__(s): s.p={}
    def find(s,a):
        s.p.setdefault(a,a)
        while s.p[a]!=a:
            s.p[a]=s.p[s.p[a]]; a=s.p[a]
        return a
    def union(s,a,b): s.p[s.find(a)]=s.find(b)
def diagram(full):
    """returns list of crossings with oriented data, or None if invalid / not a knot"""
    uf=UF(); nid=[1]
    def new():
        nid[0]+=1; return nid[0]
    pos=[0,0]; cr=[]
    for c,i in full:
        if i<0: return None
        if c in 'xy':
            if i+1>=len(pos): return None
            a,b=pos[i],pos[i+1]; cc,d=new(),new(); pos[i],pos[i+1]=cc,d
            if c=='x': cr.append({'ot':a,'ob':d,'ut':b,'ub':cc,'ty':'x'})
            else:      cr.append({'ot':b,'ob':cc,'ut':a,'ub':d,'ty':'y'})
        elif c in 'lr':
            if i>len(pos): return None
            e=new(); pos.insert(i,e); pos.insert(i,e)
        elif c=='u':
            if i+1>=len(pos): return None
            uf.union(pos[i],pos[i+1]); del pos[i:i+2]
    if pos: return None
    n=len(cr)
    roots=set(uf.find(i) for i in range(nid[0]+1) if (i in uf.p or i==0))
    if n==0: return [] if len(roots)<=1 else None
    ends={}
    for k,x in enumerate(cr):
        for key in ('ot','ob','ut','ub'):
            x[key]=uf.find(x[key]); ends.setdefault(x[key],[]).append((k,key))
    if any(len(v)!=2 for v in ends.values()): return None
    if any(r not in ends for r in roots): return None
    # traverse
    k,s,down=0,'o',True; seen=0
    for x in cr: x['od']=None; x['ud']=None
    while True:
        x=cr[k]
        if x[s+'d'] is not None: break
        x[s+'d']=down; seen+=1
        out=(k,s+('b' if down else 't'))
        e=x[out[1]]
        a,b=ends[e]
        nxt=b if a==out else a
        if a==b: return None
        k=nxt[0]; s=nxt[1][0]; down=(nxt[1][1]=='t')
    if seen!=2*n: return None
    return cr
def alex_matrix(cr,t):
    uf=UF()
    for x in cr: uf.union(x['ot'],x['ob'])
    arcs={}
    def arc(e):
        r=uf.find(e)
        if r not in arcs: arcs[r]=len(arcs)
        return arcs[r]
    rows=[]
    for x in cr:
        ov=(1,-1) if x['ty']=='x' else (-1,-1)
        un=(-1,-1) if x['ty']=='x' else (1,-1)
        if not x['od']: ov=(-ov[0],-ov[1])
        if not x['ud']: un=(-un[0],-un[1])
        sign=1 if ov[0]*un[1]-ov[1]*un[0]>0 else -1
        o=arc(x['ot']); uin=arc(x['ut'] if x['ud'] else x['ub']); uout=arc(x['ub'] if x['ud'] else x['ut'])
        rows.append((sign,o,uin,uout))
    n=len(arcs)
    M=[[0]*n for _ in rows]
    for r,(sign,o,uin,uout) in enumerate(rows):
        if sign>0:
            M[r][uin]+=t; M[r][o]+=1-t; M[r][uout]-=1
        else:
            M[r][uin]+=1; M[r][o]+=t-1; M[r][uout]-=t
    return M,sum(s for s,_,_,_ in rows)
def bareiss(M):
    n=len(M)
    if n==0: return 1
    M=[r[:] for r in M]; sign=1; prev=1
    for k in range(n-1):
        if M[k][k]==0:
            sw=next((i for i in range(k+1,n) if M[i][k]!=0),None)
            if sw is None: return 0
            M[k],M[sw]=M[sw],M[k]; sign=-sign
        for i in range(k+1,n):
            for j in range(k+1,n):
                M[i][j]=(M[i][j]*M[k][k]-M[i][k]*M[k][j])//prev
        prev=M[k][k]
    return sign*M[n-1][n-1]
def strip(v,t):
    v=abs(v); t=abs(t)
    if v==0 or t<2: return v
    while v%t==0: v//=t
    return v
def alex_eval(word,t):
    full=symmetrize(parse(word))
    if full is None: return None
    cr=diagram(full)
    if cr is None: return None
    if not cr: return 1
    M,w=alex_matrix(cr,t)
    if len(M)!=len(M[0]): return None
    m=[r[:-1] for r in M[:-1]]
    return strip(bareiss(m),t)
def alex_poly(word):
    import sympy as sp
    t=sp.symbols('t')
    full=symmetrize(parse(word)); cr=diagram(full)
    if cr is None: return None
    if not cr: return sp.Integer(1)
    M,w=alex_matrix(cr,t)
    m=sp.Matrix([r[:-1] for r in M[:-1]])
    d=sp.factor(m.det(method='berkowitz'))
    return d
def writhe(word):
    full=symmetrize(parse(word)); cr=diagram(full)
    if cr is None: return None
    if not cr: return 0
    return alex_matrix(cr,2)[1]
if __name__=='__main__':
    for w in sys.argv[1:]:
        print(w,'det',alex_eval(w,-1),'D(2)',alex_eval(w,2),'D(3)',alex_eval(w,3),'writhe',writhe(w))
