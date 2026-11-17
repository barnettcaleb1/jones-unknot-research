import sys, numpy as np
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/skein-dictionary')
from regmodel import *
def check_generic(q):
    s=np.sqrt(q+1/q)
    M=modules(q,s)
    out={}
    for a in (1,2):
        E,F,K=M['E'][a],M['F'][a],M['K'][a]
        out['UqRel%d'%a]=np.linalg.norm(E@F-F@E-(K-np.linalg.inv(K))/(q-1/q))
        out['KE%d'%a]=np.linalg.norm(K@E@np.linalg.inv(K)-q**2*E)
    for (a,b) in [(1,2),(2,1),(2,2),(1,1)]:
        B=Bmat(M,a,b,q)
        Ea,Fa,Ka=coprod(M,a,b); Eb,Fb,Kb=coprod(M,b,a)
        out['Bint%d%d'%(a,b)]=max(np.linalg.norm(B@X-Y@B) for X,Y in [(Ea,Eb),(Fa,Fb),(Ka,Kb)])
    coev,ev=cupcap2(q)
    E,F,K=coprod(M,2,2)
    out['coev_inv']=max(np.linalg.norm(E@coev),np.linalg.norm(F@coev),np.linalg.norm(K@coev-coev))
    out['ev_inv']=max(np.linalg.norm(ev@E),np.linalg.norm(ev@F),np.linalg.norm(ev@K-ev))
    C=coev.reshape(3,3); Ev=ev.reshape(3,3)
    out['snake']=max(np.linalg.norm(Ev@C-np.eye(3)),np.linalg.norm(C@Ev-np.eye(3)))
    out['circle-[3]']=abs(ev@coev-(q**2+1+q**-2))
    i,p=ip_maps(q,s)
    E12,F12,K12=coprod(M,1,2)
    out['i_int']=max(np.linalg.norm(E12@i-i@M['E'][1]),np.linalg.norm(F12@i-i@M['F'][1]),np.linalg.norm(K12@i-i@M['K'][1]))
    out['p_int']=max(np.linalg.norm(p@E12-M['E'][1]@p),np.linalg.norm(p@F12-M['F'][1]@p),np.linalg.norm(p@K12-M['K'][1]@p))
    out['pi=I']=np.linalg.norm(p@i-np.eye(2))
    # full twist eigen-relation (T-q^-4)(T-q^2)=0
    T=Bmat(M,2,1,q)@Bmat(M,1,2,q)
    out['(T-q^-4)(T-q^2)']=np.linalg.norm((T-q**-4*np.eye(6))@(T-q**2*np.eye(6)))
    # B22 eigenvalues
    ev22=np.linalg.eigvals(Bmat(M,2,2,q))
    out['B22 eig']=sorted([complex(round(x.real,6),round(x.imag,6)) for x in ev22],key=lambda z:(z.real,z.imag))
    out['expected q^-4,-q^-2,q^2']=[q**-4,-q**-2,q**2]
    # rotated crossing: (ev x id x id)(id x B22 x id)(id x id x coev)? -> check unoriented invariance: rotation of B22 vs B22^-1 (up to scalar)
    B22=Bmat(M,2,2,q); I3=np.eye(3)
    # rot(B) = (ev x 1 x 1) o (1 x B x 1) o (1 x 1 x coev) as map V2 x V2 -> V2 x V2 : use tensor network
    Bt=B22.reshape(3,3,3,3)   # [out1,out2,in1,in2]
    # rot: input (a,b); coev on new pair (c,d) appended right: (a,b,c,d); apply B on (b,c): (a,b',c',d); ev on (a,b'): leaves (c',d)
    rot=np.einsum('ab,cdbe,ef->cfad'.replace('ab,','ab,')) if False else None
    R=np.zeros((3,3,3,3),complex)  # R[c',d,a,b]
    for a_ in range(3):
        for b_ in range(3):
            for c_ in range(3):
                for d_ in range(3):
                    if C[c_,d_]==0: continue
                    for b2 in range(3):
                        for c2 in range(3):
                            val=C[c_,d_]*Bt[b2,c2,b_,c_]*Ev[a_,b2]
                            if val: R[c2,d_,a_,b_]+=val
    Rm=R.reshape(9,9)
    B22i=np.linalg.inv(B22)
    # compare with B22 and B22^-1 up to scalar
    def prop(X,Y):
        k=np.argmax(abs(Y)); lam=X.flat[k]/Y.flat[k]; return lam, np.linalg.norm(X-lam*Y)
    out['rot(B22) vs B22^-1']=prop(Rm,B22i)
    out['rot(B22) vs B22']=prop(Rm,B22)
    return out
for q in [1.3*np.exp(0.4j), 0.7*np.exp(1.1j)]:
    o=check_generic(q)
    for k,v in o.items(): print(k, v if not isinstance(v,float) else '%.2e'%v)
    print('---')
