# Claim 12: iota - v3(K) versus v3 of the constituent knots. Own constructions:
#   K2 (arc u outer axis edge): RIGHT-side closure (different diagram from the builder's left closure), x0/y0 deleted;
#   K1 (arc u inner axis edge): left closure strand at position 0, each x0/y0 -> two crossings of that letter with the arc.
# Then exact rational linear algebra: is iota - v3(K) in span_Q{1, v3K, v3K1, v3K2}? (and variants)
import sys, json
from fractions import Fraction as F
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from rlib import *
import sympy as sp
def toks(word): return [(t[0],int(t[1:])) for t in word.split('.')[1:]]
def K2_right(word):
    ops=[('cap',0)]       # position 0 = arc start, position 1 = closure strand (stays rightmost)
    for c,i in toks(word):
        if c in 'lr': ops.append(('cap',i-1))
        elif c=='u': ops.append(('cup',i-1))
        elif i>=1: ops.append((c,i-1))
    ops.append(('cup',0))
    return ops
def K2_left(word):
    ops=[('cap',0)]
    for c,i in toks(word):
        if c in 'lr': ops.append(('cap',i))
        elif c=='u': ops.append(('cup',i))
        elif i>=1: ops.append((c,i))
    ops.append(('cup',0)); return ops
def K1_left(word):
    ops=[('cap',0)]
    for c,i in toks(word):
        if c in 'lr': ops.append(('cap',i))
        elif c=='u': ops.append(('cup',i))
        elif i>=1: ops.append((c,i))
        else: ops+=[(c,0),(c,0)]
    ops.append(('cup',0)); return ops
rows=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident3_rows.json'))
data=[]; agreeK2=0
for w,M2,M3,M4,a2K,w3 in rows:
    v3K=-F(w3)/36; iota=(F(M3,36)-7*v3K)/5
    VR=jones(K2_right(w)); VL=jones(K2_left(w)); V1=jones(K1_left(w))
    if VR==VL: agreeK2+=1
    data.append((iota,v3K,v3_of(V1),v3_of(VR),a2_of(V1),a2_of(VR),F(a2K)))
print('rows',len(data),' K2 right-closure V == left-closure V in',agreeK2,'rows')
print('iota integral:',all(d[0].denominator==1 for d in data))
def span_test(target, cols, names):
    M=sp.Matrix([[c(d) for c in cols] for d in data]); b=sp.Matrix([target(d) for d in data])
    rk=M.rank(); rk2=M.row_join(b).rank()
    out='in span' if rk==rk2 else 'NOT in span'
    sol=None
    if rk==rk2:
        sol=M.gauss_jordan_solve(b)[0].T
    print('  target in span_Q%s: %s (rank %d -> %d)%s'%(names,out,rk,rk2,'' if sol is None else '  coeffs '+str(sol)))
one=lambda d:1
print('target = iota - v3(K):')
span_test(lambda d:d[0]-d[1],[one,lambda d:d[1],lambda d:d[2],lambda d:d[3]],'{1,v3K,v3K1,v3K2}')
span_test(lambda d:d[0]-d[1],[one,lambda d:d[1],lambda d:d[2],lambda d:d[3],lambda d:d[4],lambda d:d[5],lambda d:d[6]],'{1,v3K,v3K1,v3K2,a2K1,a2K2,a2K}')
print('target = M3/36 (F3 convention):')
span_test(lambda d:7*d[1]+5*d[0],[one,lambda d:d[1],lambda d:d[2],lambda d:d[3],lambda d:d[4],lambda d:d[5],lambda d:d[6]],'{1,v3K,v3K1,v3K2,a2K1,a2K2,a2K}')
from collections import Counter
print('distinct (iota - v3K) values:',Counter(d[0]-d[1] for d in data).most_common(8))
