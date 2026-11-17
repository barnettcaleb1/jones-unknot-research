"""What is the monomial u = y + delta x (infinity closure) that J_raw divides by? Does it depend on m and B separately?"""
import sys; sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/referee')
from pf_common import *
import flat_search as fs, alex
def u_of(word):
    half=alex.parse(word); y,x=fs.bracket_vector(half)
    u={}; fs.padd(u,y); fs.padd(u,fs.pdelta(x)); u={e:c for e,c in u.items() if c}
    return u, y
bs=gen_bodies_nontriv(77, 8)
for B in ['']+bs:
    row=[]
    for m in (-2,-1,0,1,2):
        u,y=u_of(jn('s.r2',tw(m),B,'u1'))
        row.append(u)
    print(B or '(empty)', row)
