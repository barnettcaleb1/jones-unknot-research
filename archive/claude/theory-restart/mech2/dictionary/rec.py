#!/usr/bin/env python3
"""Analyse a run record (from run_words.py) with bnchains: staircase, squares, J, Pi."""
import json,sys,collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech2/dictionary')
import chains
from gtilde import jset,valid
def analyse_chains(lines,khr):
    k,j,pts=jset(khr)
    comps=[c for c in (chains.parse_chain(l) for l in lines) if c]
    st=chains.structure(comps); g=st['gens']
    tgt=(8*j+k,24*j+2*k)
    idx=st['arc']['idx']
    rho=None
    for i in (idx[0],idx[-1]):
        if (g[i][0],g[i][1])==tgt: rho=i
    if rho is None: raise ValueError('rho not found %s %s'%(tgt,[(g[i][0],g[i][1]) for i in idx]))
    h0,q0,_=g[rho]
    def ab(i):
        dh=g[i][0]-h0; dq=g[i][1]-q0
        b=(2*dh-dq)//2; a=dh-5*b
        return (a,b)
    L=[ab(i) for i in range(len(g))]
    path=[L[i] for i in (idx if rho==idx[0] else idx[::-1])]
    squares=[];odd=[]
    for ci,c in enumerate(comps):
        if not c['cyclic']: continue
        mem=sorted(L[i] for i in range(len(g)) if g[i][2]==ci)
        if len(mem)==4 and mem==[(mem[0][0],mem[0][1]),(mem[0][0],mem[0][1]+1),(mem[0][0]+1,mem[0][1]),(mem[0][0]+1,mem[0][1]+1)]:
            squares.append(mem[0])
        else: odd.append(mem)
    return dict(k=k,j=j,L=L,path=path,squares=sorted(squares),odd=odd,other=st['other'],dD=[p for (_,_,p) in st['dD'] if p!=1],dP=[p for (_,_,p) in st['dP'] if p!=2])
def poly_str(p):
    return ' + '.join('%s%st^%d'%('' if c>0 else '-', '' if abs(c)==1 else abs(c), e) for e,c in sorted(p.items()) if c) or '0'
def Jpoly(L,k):
    p=collections.Counter()
    for a,b in L: p[k+a+4*b]+=(-1)**((a+b)%2)
    return {e:c for e,c in p.items() if c}
def Pi(squares):
    p=collections.Counter()
    for a,b in squares: p[a+4*b]+=(-1)**((a+b)%2)
    return {e:c for e,c in p.items() if c}
if __name__=='__main__':
    for fn in sys.argv[1:]:
        for line in open(fn):
            try: r=json.loads(line)
            except: continue
            khr=r.get('khr') or []
            if not khr or not valid(khr) or not r.get('bnchains'): continue
            a=analyse_chains(r['bnchains'],khr)
            print('==',r.get('word') or r.get('knot') or r.get('file'),'k',a['k'],'j',a['j'],'dim',len(a['L']))
            print('  arc path',a['path'])
            print('  squares',a['squares'], 'odd comps',a['odd'],'other',a['other'],a['dD'],a['dP'])
            print('  s_sq=sum(-1)^b:',sum((-1)**(b%2) for _,b in a['squares']),' squares by a+b:',sorted(collections.Counter(x+y for x,y in a['squares']).items()))
            print('  Pi(t) =',poly_str(Pi(a['squares'])))
            print('  J(t)  =',poly_str(Jpoly(a['L'],a['k'])))
