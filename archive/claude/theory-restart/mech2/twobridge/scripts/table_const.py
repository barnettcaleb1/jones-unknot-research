#!/usr/bin/env python3
import sys,os,glob,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import chain, constituents as cs
import sympy as sp
t=cs.t
base='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si/'
def nat(s):
    import re
    return [int(x) if x.isdigit() else x for x in re.split(r'(\d+)',s)]
names=sorted([os.path.basename(f)[:-4] for f in glob.glob(base+'*.kht')],key=nat)
for nm in names:
    word=open(base+nm+'.kht').read().split('\n')[1].strip()
    fn=base+nm+'/cxBNr-c2-qs'
    if not os.path.exists(fn): print(nm,'no chain file'); continue
    comps=chain.parse_file(fn)
    N=[g for c in comps for g in c['gens'] if g[0]=='b']
    dimN=len(N)
    try:
        K,u,l=cs.consts(word)
    except Exception as e:
        print(nm,'ERR',e); continue
    det=lambda p: abs(int(p.subs(t,-1))) if p is not None else None
    arcs=[c for c in comps if not c['cyclic']]
    nb_arc=sum(1 for g in arcs[0]['gens'] if g[0]=='b') if arcs else None
    nsq=sum(1 for c in comps if c['cyclic'])
    flag=''
    if det(u) is not None and det(l) is not None and det(u)*det(l)!=dimN: flag+=' [detU*detL != dimN]'
    if det(K)!=dimN: flag+=' [detK != dimN]'
    print('%-8s dimN=%3d arc=%s sq=%d  detK=%s  detKu=%s detKl=%s  Ku=%s  Kl=%s %s'%(nm,dimN,nb_arc,nsq,det(K),det(u),det(l),u,l,flag))
