"""Check of the decategorified recursion (Lemma 1) against a direct Kauffman-bracket computation of the quotient diagram.
Claim: with q = A^2, alpha = q^-6, beta = -q^2, omega = 1 - beta^-2,
   A-letter: Gam <- alpha*Gam + 1 + omega*G ;  B-letter: G <- beta*G + Gam    (inverse letters: the inverse affine maps)
   Jhat_w := (coefficient of [Q_0]) / <T_w(infinity)>  =  1 + q^-6 (1 - q^8) G_w .
"""
import sympy as sp, itertools, random
from tl import J_of_half, A
q=sp.symbols('q')
al=q**-6; be=-q**2; om=1-be**-2
def Ghat(word):
    G=sp.Integer(0); Gam=sp.Integer(0)
    for t,n in word:
        for _ in range(abs(n)):
            if t=='A':
                if n>0: Gam=al*Gam+1+om*G
                else: Gam=(Gam-1-om*G)/al
            else:
                if n>0: G=be*G+Gam
                else: G=(G-Gam)/be
    return sp.expand(sp.cancel(G))
def half_word(word):
    toks=['s','l1']
    for t,n in word:
        if t=='A': toks+=['y0' if n>0 else 'x0']*abs(n)
        else: toks+=['x1' if n>0 else 'y1']*abs(n)
    toks.append('u2')
    return '.'.join(toks)
if __name__=='__main__':
    random.seed(1)
    words=[[('A',1),('B',1)],[('A',2),('B',1)],[('A',1),('B',3)],[('A',3),('B',2)],[('A',1),('B',1),('A',1),('B',1)],
           [('A',2),('B',1),('A',1),('B',2)],[('A',1),('B',2),('A',2),('B',1),('A',1),('B',1)],
           [('A',-1),('B',-2)],[('A',2),('B',-1)],[('A',1),('B',-1),('A',-2),('B',1)],[('A',-1),('B',2),('A',1),('B',1),('A',-1),('B',-1)]]
    for _ in range(6):
        w=[]
        for i in range(random.randint(1,3)):
            w+= [('A',random.choice([-2,-1,1,2,3])),('B',random.choice([-2,-1,1,2]))]
        words.append(w)
    for w in words:
        Jtl=J_of_half(half_word(w)).subs(A,sp.sqrt(q))
        Jf=1+q**-6*(1-q**8)*Ghat(w)
        print(w, 'OK' if sp.simplify(Jtl-Jf)==0 else ('MISMATCH', sp.factor(Jtl), sp.factor(Jf)))
