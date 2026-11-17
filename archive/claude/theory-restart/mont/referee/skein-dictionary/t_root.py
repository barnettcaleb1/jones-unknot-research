import sys, numpy as np
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/skein-dictionary')
from regmodel import *
def superflip():
    par=[1,0,1]   # w0 odd, w1 even, w2 odd
    P=np.zeros((9,9))
    for i in range(3):
        for j in range(3): P[j*3+i,i*3+j]=(-1)**(par[i]*par[j])
    return P
for h in [1e-4,1e-6,1e-8]:
    q=1j*np.exp(h/2); s=np.sqrt(q+1/q)
    M=modules(q,s)
    B22=Bmat(M,2,2,q); T=Bmat(M,2,1,q)@Bmat(M,1,2,q)
    T0=np.kron(np.eye(2),np.diag([-1,1,-1]))
    i,p=ip_maps(q,s); P1=i@p
    P1root=np.kron(np.eye(2),np.diag([0,1,0]))
    coev,ev=cupcap2(q); C=coev.reshape(3,3); Ev=ev.reshape(3,3)
    # curl: (id x ev)(B22 x id)(id x coev) : V2->V2
    Bt=B22.reshape(3,3,3,3)
    curl=np.einsum('jk,bcaj,ck->ba',C,Bt,Ev)   # out b ; B: (a,j)->(b,c); ev(c,k)
    curl2=np.einsum('jk,bcaj,ck->ba',C,np.linalg.inv(B22).reshape(3,3,3,3),Ev)
    print('h=%g |B22-superflip|=%.1e |B22^-1-superflip|=%.1e |T-T0|=%.1e |T^-1-T0|=%.1e |P1-Id x Pi_w1|=%.1e |curl-I|=%.1e |curl^-1-I|=%.1e |i_root|'%(
        h,np.linalg.norm(B22-superflip()),np.linalg.norm(np.linalg.inv(B22)-superflip()),np.linalg.norm(T-T0),np.linalg.norm(np.linalg.inv(T)-T0),
        np.linalg.norm(P1-P1root),np.linalg.norm(curl-np.eye(3)),np.linalg.norm(curl2-np.eye(3))))
# generic curl value
q=1.3*np.exp(0.4j); s=np.sqrt(q+1/q); M=modules(q,s); B22=Bmat(M,2,2,q)
coev,ev=cupcap2(q); C=coev.reshape(3,3); Ev=ev.reshape(3,3)
curl=np.einsum('jk,bcaj,ck->ba',C,B22.reshape(3,3,3,3),Ev)
print('generic curl / q^4 :',np.round(curl/q**4,10).diagonal(), ' curl/q^-4:',np.round(curl/q**-4,10).diagonal())
