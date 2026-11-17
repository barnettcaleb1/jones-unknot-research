# Independent audit: arbitrary Taylor agreement without triviality

Fix a=σ1², b=σ2² in B3. Set c1=a and c_(r+1)=[c_r,b]=c_r b c_r^-1 b^-1. Let K_r be the ordinary braid closure of c_r σ1 σ2.

## Every K_r is a knot

Each c_r is pure. The permutation of σ1σ2 is a 3-cycle, so the braid closure has one component.

## Every K_r is nontrivial: all-r determinant proof

Use the reduced Burau representation at t=-1:

    S1=[[1,1],[0,1]], S2=[[1,0],[-1,1]],
    A=S1²=[[1,2],[0,1]], B=S2²=[[1,0],[-2,1]],
    R=S1 S2=[[0,1],[-1,1]].

Put C1=A, C_(r+1)=C_r B C_r^-1 B^-1. If C_r=[[a_r,b_r],[c_r,d_r]], direct multiplication gives

    C_(r+1) = [[1-2b_r d_r+4b_r², 2b_r²],
               [2-2d_r²+4b_r d_r, 1+2b_r d_r]].

In particular b_(r+1)=2b_r² and d_(r+1)=1+2b_r d_r. Starting with b1=2,d1=1, the bounds

    b_r/2 <= d_r < b_r

hold for every r. Indeed the lower bound is preserved since

    d_(r+1)-b_(r+1)/2=1+b_r(2d_r-b_r)>=1.

For the upper bound, integrality gives d_r<=b_r-1, hence

    d_(r+1)<=1+2b_r(b_r-1)<2b_r²=b_(r+1).

Now

    trace(C_(r+1)R)=3-2d_r²+6b_r d_r-2b_r².

Writing q=d_r/b_r in [1/2,1), the quadratic -q²+3q-1 is increasing and at least 1/4. Consequently

    trace(C_(r+1)R)>=3+b_r²/2>=5.

The Burau–Alexander formula at t=-1 gives

    det(K_r)=|det(I-C_rR)|=|2-trace(C_rR)|,

because C_rR lies in SL(2,Z). Therefore det(K_r)>=3 for every r>=2. For r=1 the determinant is 3 directly. Hence every K_r is nontrivial.

The first determinants, r=1,...,6, are

    3, 3, 63, 16319, 1069530111, 4593596851986104319.

The standard Burau–Alexander formula is Δ_cl(β)(t) ≍ (1-t)/(1-t³) det(I-ρ(β)); at t=-1 the prefactor is 1 and the unit ambiguity has absolute value 1. One current primary research reference stating the formula is Morier-Genoud, Ovsienko, Veselov, *Burau representation of braid groups and q-rationals*, IMRN 2024, §4: https://academic.oup.com/imrn/article/2024/10/8618/7525791 .

## Every finite Taylor cutoff is defeated

Write A=1+h, δ=-A²-A^-2, and use the writhe-normalized Temperley–Lieb generators

    R_i=-A^-2 I-A^-4 e_i,
    e_i²=δe_i,
    e1 e2 e1=e1, e2 e1 e2=e2.

Their squares satisfy

    R_i²=A^-4 I+(A^-6-A^-10)e_i = I+h(-4I+4e_i)+O(h²).

For invertible formal series X=I+O(h^r) and Y=I+O(h), [X,Y]=I+O(h^(r+1)). Induction therefore gives ρ(c_r)=I+O(h^r). The closure functional is regular at A=1 (δ=-2), and the closure of σ1σ2 is the unknot. Thus

    V_(K_r)(A^-4)=1+O((A-1)^r).

Since t=A^-4 is a local change of variable with dt/dA=-4 at A=1, this is equivalent to

    V_(K_r)(t)=1+O((t-1)^r).

Combining with the determinant proof: for EVERY prescribed finite N, K_(N+1) is nontrivial and has exactly the unknot's Jones derivatives through order N at t=1.

This does not exclude algorithms that use a complexity-dependent number of coefficients, nor does it show that the full Jones polynomial misses the unknot. It rules out any universal FIXED finite Taylor cutoff as an unknot test. This is a concrete instance of the familiar finite-type limitation; no novelty claim is made.

## Independent audit of the even-order leading coefficient

At A=1 the TL loop value is δ=-2. Put X=-4I+4e1 and Y=-4I+4e2. For r>=2, write

    ρ(c_r)=I+h^r C_r+O(h^(r+1)).

Then C2=[X,Y]=16[e1,e2] and C_(r+1)=[C_r,Y]. The identity ad_(e2)^3=δ² ad_(e2)=4 ad_(e2) implies C_(r+2)=64 C_r for r>=2, since C_r lies in the image of ad_(e2).

Let τ be the normalized ordinary closure functional on TL3. At δ=-2,

    τ(I)=4, τ(e1)=τ(e2)=-2, τ(e1e2)=τ(e2e1)=1.

The baseline ρ(σ1σ2) at A=1 is (I+e1)(I+e2). Direct multiplication using the TL relations gives

    τ([e1,e2](I+e1)(I+e2))=1-δ²=-3.

Therefore for every m>=1,

    V_(K_(2m))(A^-4)
      =1-48*64^(m-1)*(A-1)^(2m)+O((A-1)^(2m+1)).

The corresponding leading coefficient in t-1 is -3*4^(m-1). Thus the even-order vanishing is exactly 2m, while the odd-order trace vanishes and requires the next term. The all-r determinant proof avoids needing the next odd-order term.
