# paper's own unsimplified Moody polynomials, (sign, exponent) in order along beta
ex = {
 "Fig3.1b (B3, parity)": [(1,0),(-1,1),(1,2),(-1,1),(-1,-1),(1,0)],
 "Sec7 M_Phi (no parity)": [(1,0),(1,2),(1,4),(-1,3),(-1,1),(1,-3),(1,-1),(1,1)],
 "Sec7 M_PhiGamma (parity)": [(1,0),(1,2),(1,4),(-1,3),(-1,1),(1,-4),(1,-2),(1,0)],
 "Sec7 M_Gamma (parity)": [(-1,0),(-1,2),(1,1),(1,-1),(-1,0),(-1,2),(1,3),(1,1),(1,-1),(-1,-2),(-1,0),(1,-1),(1,-3),(-1,-2),(-1,0),(1,1),(1,-1),(1,-3),(-1,-2),(-1,0)],
}
for k,v in ex.items():
    s=[e*(-1)**(x%2) for e,x in v]
    W=[v[i+1][1]-v[i][1] for i in range(len(v)-1)]
    par=all((v[i][0]!=v[i+1][0])==(W[i]%2==1) for i in range(len(W)))
    print(k, "m=",len(v),"M(-1)=",sum(s),"single sign:",len(set(s))==1,"parity-consistent:",par)
