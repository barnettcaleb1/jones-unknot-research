import sys, random, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import diag, lp, kauffman, flat_search as fs
from fractions import Fraction as F
def VK(word):
    kb=kauffman.bracket(word)
    return diag.jones_from_bracket(kb)
rows=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident3_rows.json'))
bad=0; n=0
for r in rows[:60]:
    w=r[0]
    inv=diag.all_invariants(w)
    if inv is None: print('NONE',w); continue
    n+=1
    V1=VK(w); V2=inv['K']['V']
    if V1!=V2: bad+=1; print('V mismatch',w,V1,V2)
    for key in ('K','Kin','Kout','Uin','Uout'):
        d=inv[key]
        if d is None: print('none',key,w); bad+=1; continue
        if d['a2']!=d['a2c']: bad+=1; print('a2 mismatch',key,w,d['a2'],d['a2c'])
print('checked',n,'bad',bad)
