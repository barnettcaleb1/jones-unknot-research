#!/usr/bin/env python3
"""Referee checks A6-A8 on WORDS in Y,X,y,x (L_1 first = nearest the cap):
 (A6) positive block words: span 3A+B, top (-1)^B t^B, bottom t^{-3A};
 (A7) J_w monomial <=> |p| = 1, p = (1,1)-entry of the integer matrix of w (Y -> [[1,1],[0,1]], X -> [[1,0],[2,1]]), i.e. K = unknot;
 (A8) independent reduction of w to a normal form (n_0..n_{k-1}) using only X = Y e-type rewriting and E^2 = scalar; J_w = unit * F(normal form);
      |p| = 1 <=> normal form all-degenerate."""
import sys, itertools, collections
from lp import *
IM={'Y':((1,1),(0,1)),'X':((1,0),(2,1)),'y':((1,-1),(0,1)),'x':((1,0),(-2,1))}
def imul(M,N): return tuple(tuple(M[i][0]*N[0][j]+M[i][1]*N[1][j] for j in range(2)) for i in range(2))
def pq(word):
    """word acts: continued fraction C(a_1,2b_1,...) = a_1 + 1/(2b_1 + ...) : matrix product in word order applied to (1,0)^T... p = M[0][0]"""
    M=((1,0),(0,1))
    for L in word: M=imul(M,IM[L])
    return M[0][0],M[1][0]
def normal_form(word):
    """matrix product is rho(L_m)...rho(L_1).  rho(X) = rho(Y) E, rho(x) = E^-1 rho(y) = t^-4 E rho(y).
    Build list (from right to left = L_1 first) of tokens: integers (powers of Y) and 'E'. returns sequence (n_0..n_{k-1}) ignoring final Y-power, and exponent of t from E^-1 = t^-4 E and from E E = t^4."""
    toks=[]; texp=0   # toks in order of application (first applied first)
    def pushY(n):
        if n==0: return
        if toks and toks[-1]!='E': toks[-1]+=n
        else: toks.append(n)
        if toks and toks[-1]==0: toks.pop()
    def pushE():
        nonlocal texp
        if toks and toks[-1]=='E': toks.pop(); texp+=4
        else: toks.append('E')
    for L in word:
        if L=='Y': pushY(1)
        elif L=='y': pushY(-1)
        elif L=='X': pushE(); pushY(1)        # rho(X) = rho(Y) E : apply E first, then Y
        elif L=='x': pushY(-1); pushE(); texp-=4  # rho(x) = t^-4 E rho(y): apply y first, then E
    # merge may leave things like ['E', 0-popped] handled; now re-normalise completely
    changed=True
    while changed:
        changed=False; out=[]
        for tk in toks:
            if tk=='E':
                if out and out[-1]=='E': out.pop(); texp+=4; changed=True
                else: out.append('E')
            else:
                if tk==0: changed=True; continue
                if out and out[-1]!='E':
                    out[-1]+=tk; changed=True
                    if out[-1]==0: out.pop()
                else: out.append(tk)
        toks=out
    # read sequence: n_0 (possibly 0), then E, n_1, E, ...
    seq=[]; cur=0
    for tk in toks:
        if tk=='E': seq.append(cur); cur=0
        else: cur=tk
    return tuple(seq),texp     # trailing Y-power 'cur' is dropped: (1 0) rho(Y)^n = (1 0)
def degenerate(seq):
    if not seq: return True
    return seq==(0,)+(1,)*(len(seq)-1) or seq==(-1,)*len(seq)
maxlen=int(sys.argv[1]) if len(sys.argv)>1 else 9
tot=0; bad_nf=0; bad_p=0; bad_deg=0; npos=0; bad_pos=0; nontriv=0; bad_coeff=0
for m in range(0,maxlen+1):
    for word in itertools.product('YXyx',repeat=m):
        w=''.join(word)
        # skip freely unreduced words? keep them all: the theorem is about all words
        tot+=1
        J=Jword(w); p,q=pq(w)
        seq,texp=normal_form(w)
        if mul(mon(texp),F(seq))!=J: bad_nf+=1; print('NF MISMATCH',w,seq,texp) if bad_nf<5 else None
        if is_unit(J)!=(abs(p)==1): bad_p+=1; print('P MISMATCH',w,p,J) if bad_p<5 else None
        if degenerate(seq)!=(abs(p)==1): bad_deg+=1; print('DEG MISMATCH',w,seq,p) if bad_deg<5 else None
        if not is_unit(J):
            nontriv+=1
            if abs(J[max(J)])!=1 or abs(J[min(J)])!=1: bad_coeff+=1
print('words of length <=',maxlen,':',tot)
print('J_w != t^texp F(normal form):',bad_nf)
print('[J monomial] != [|p|=1]:',bad_p,'   [normal form all-degenerate] != [|p|=1]:',bad_deg)
print('non-trivial words:',nontriv,' with an extreme coefficient not +-1:',bad_coeff)
# A6 positive block words
import random
for nb in (1,2,3):
    for blocks in itertools.product(itertools.product(range(1,5),repeat=2),repeat=nb):
        w=''.join('Y'*a+'X'*b for a,b in blocks); A=sum(a for a,b in blocks); B=sum(b for a,b in blocks)
        J=Jword(w); npos+=1
        if not (span(J)==3*A+B and max(J)==B and J[B]==(-1)**B and min(J)==-3*A and J[-3*A]==1): bad_pos+=1
print('positive block words (<=3 blocks, exponents 1..4):',npos,' violations of span 3A+B / top (-1)^B t^B / bottom t^-3A:',bad_pos)
