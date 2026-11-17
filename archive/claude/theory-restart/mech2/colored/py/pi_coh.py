#!/usr/bin/env python3
"""For each double: is the square polynomial Pi(t) = sum over squares (-1)^(a+b) t^(a+4b) cancellation free?
Also: joint distribution check -- are squares determined by (e=a+4b, l=a+3b)? and sign pattern by level."""
import sys,os,glob,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from chains import lattice
D='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/dbl/examples/knots/2-bridge_knots'
names=sorted([os.path.basename(p)[:-4] for p in glob.glob(D+'/*.kht') if os.path.exists(os.path.join(p[:-4],'cxBNr-c2-d'))],key=lambda s:[int(x) for x in s[1:].split('_')])
for n in names:
    rho,arc,sq,other=lattice(os.path.join(D,n,'cxBNr-c2-d'))
    P=collections.Counter()
    for a,b in sq: P[a+4*b]+=(-1)**(a+b)
    absum=sum(abs(v) for v in P.values())
    # cancelling pairs of squares: same e, opposite parity
    pos=collections.Counter(); neg=collections.Counter()
    for a,b in sq:
        (pos if (a+b)%2==0 else neg)[a+4*b]+=1
    canc=sum(min(pos[e],neg[e]) for e in set(pos)|set(neg))
    mult=collections.Counter(sq)
    print('%-8s squares %3d  |Pi| %3d  cancelling square pairs %2d   max multiplicity of a square position %d'%(n,len(sq),absum,canc,max(mult.values())))
