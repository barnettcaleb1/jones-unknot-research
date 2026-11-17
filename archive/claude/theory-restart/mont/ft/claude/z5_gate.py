# How restrictive is the new gate V_K(zeta_5) = 1 (forced by J = 1 via MOMENT-CYC10)? Compare with the a_2 gate.
import sys, random, cmath
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs, kauffman
src=open('check_cyc10.py').read(); exec(src[src.index('def VK'):src.index('roots=')])
z5=cmath.exp(2j*cmath.pi/5)
rnd=random.Random(23); n=a2z=z5one=both=0; vals=[]
while n<400:
    w=fs.gen(rnd,rnd.randint(6,18))
    if not w: continue
    Jn=lp.J(w)
    if Jn is None: continue
    V=VK(w)
    if V is None or len(V)==1: continue      # skip Jones-trivial (unknot) covering knots
    n+=1
    a2zero=(lp.a2(Jn)==0); v5=ev(V,z5); one=abs(v5-1)<1e-9
    a2z+=a2zero; z5one+=one; both+=(a2zero and one); vals.append(abs(v5))
print('nontrivial-V knots',n,'| a2=0:',a2z,'| V(z5)=1:',z5one,'| both:',both)
vals.sort(); print('|V_K(z5)| quartiles:',[round(vals[int(q*(len(vals)-1))],3) for q in (0,0.25,0.5,0.75,1)])
