from nt import *
for n in (2,3,4,5,6):
    out=[]
    for N in range(-2,n+3):
        for mu in [m for m in range(-4,5) if m]:
            s1=span(neck(mu,N,[box((-2,))]*n)); s2=span(neck(mu,N,[box((1,))]*n))
            out.append((s1,'(-2,)^n',mu,N)); out.append((s2,'(1,)^n',mu,N))
    out.sort(); print(n, out[:4])
