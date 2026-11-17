#!/usr/bin/env python3
"""Constituent knots of the quotient theta-graph of a strongly invertible knot given by a kht++ half-diagram word.
theta-graph = A (axis image) u k (image of K).  A = A_u u A_l (the half-axes); K'_u = k u A_u, K'_l = k u A_l.
In the half-diagram: strand 0 = A_u (from the top fixed point at infinity down to the bottom fixed point); a crossing at
position 0 (one crossing of K on the axis) = one full turn of k around A = two crossings of the same type in the quotient.
A_l runs from the bottom fixed point down to infinity (no crossings)."""
import sys,collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex
import sympy as sp
t=sp.symbols('t')
def full_u(word):
    half=alex.parse(word); out=[]
    for c,i in half:
        if i==0: out+= [(c,0),(c,0)]
        else: out.append((c,i))
    out.append(('u',0)); return out
def full_l(word):
    half=alex.parse(word); out=[(c,i) for c,i in half if i!=0]
    out.append(('u',0)); return out
def full_K(word):
    return alex.symmetrize(alex.parse(word))
def poly(full):
    cr=alex.diagram([x for x in full])
    if cr is None: return None
    if not cr: return sp.Integer(1)
    n=len(cr)
    pts=[]
    for v in range(2,n+4):
        M,w=alex.alex_matrix(cr,v)
        m=[r[:-1] for r in M[:-1]]
        pts.append((v,alex.bareiss(m)))
    d=sp.expand(sp.interpolate(pts,t))
    return norm(d)
def norm(d):
    d=sp.expand(d)
    if d==0: return d
    p=sp.Poly(d,t)
    # strip powers of t and sign
    low=min(m[0] for m in p.monoms())
    d=sp.expand(d/t**low)
    p=sp.Poly(d,t)
    if p.LC()<0: d=-d
    # symmetrise sign: make value at 1 positive
    if d.subs(t,1)<0: d=-d
    return sp.expand(d)
def consts(word):
    return poly(full_K(word)),poly(full_u(word)),poly(full_l(word))
if __name__=='__main__':
    for w in sys.argv[1:]:
        K,u,l=consts(w)
        print(w); print('   Delta_K  =',K); print('   Delta_K_u=',u); print('   Delta_K_l=',l)
