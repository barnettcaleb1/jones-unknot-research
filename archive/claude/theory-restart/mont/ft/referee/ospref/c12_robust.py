# robustness: flip the handedness of the K1 twists (x0 -> two crossings of the OPPOSITE letter); also K1 built by the builder's code
import sys, json
from fractions import Fraction as F
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from rlib import *
import sympy as sp
from c12_constit import toks, K2_right, K1_left
def K1_flip(word):
    ops=[('cap',0)]
    for c,i in toks(word):
        if c in 'lr': ops.append(('cap',i))
        elif c=='u': ops.append(('cup',i))
        elif i>=1: ops.append((c,i))
        else: d={'x':'y','y':'x'}[c]; ops+=[(d,0),(d,0)]
    ops.append(('cup',0)); return ops
rows=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident3_rows.json'))
A=[];B=[]
for w,M2,M3,M4,a2K,w3 in rows:
    v3K=-F(w3)/36; iota=(F(M3,36)-7*v3K)/5
    V1f=jones(K1_flip(w)); VR=jones(K2_right(w)); V1=jones(K1_left(w))
    A.append([1,v3K,v3_of(V1f),v3_of(VR),a2_of(V1f),a2_of(VR),F(a2K)]); B.append(iota-v3K)
M=sp.Matrix(A); b=sp.Matrix(B)
print('flipped-K1: rank',M.rank(),'->',M.row_join(b).rank())
