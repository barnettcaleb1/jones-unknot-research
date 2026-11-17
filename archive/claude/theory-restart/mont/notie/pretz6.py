from pretz import *
import itertools
bad=0; cnt=0
for m in range(2,7):
    for j in range(1,7):
        for q in (1,2,3):
            for ls in itertools.combinations_with_replacement(range(1,7),q):
                rows=[2*j+1]+[-(2*l+1) for l in ls]; n=len(rows)
                g=G(-m,rows); th=top(g)-2*n; sp=span(g)-2
                if sp!=3*n+sum(ls)+m-3+th: bad+=1
                cnt+=1
# also the mu>=1, p>=1 top formula: top(H) = J+ + mu + 2 + p
for mu in range(1,6):
    for ps in itertools.combinations_with_replacement(range(1,6),2):
        for ls in itertools.combinations_with_replacement(range(1,6),2):
            rows=[2*j+1 for j in ps]+[-(2*l+1) for l in ls]
            th=top(G(mu,rows))-2*len(rows)
            if th!=sum(ps)+mu+2+len(ps): bad+=1
            cnt+=1
print('checked',cnt,'bad',bad)
