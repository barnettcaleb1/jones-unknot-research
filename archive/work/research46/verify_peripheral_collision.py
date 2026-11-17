"""Exact checks of the two cited Knot Atlas A-polynomial entries."""
from math import comb
import json
from pathlib import Path
# Entry indexed by L degree, then M degree. The common abelian factor is omitted.
p={8:{6:1},7:{20:1,18:-1,12:4,10:-4,8:-1,6:3},6:{22:-1,20:4,18:-5,16:-5,14:12,12:7,10:-9,8:-13,6:6,4:2},5:{24:-1,22:3,20:2,18:-7,16:-12,14:13,12:10,10:-9,8:-5,6:-4,4:4},4:{26:1,24:-7,22:7,20:13,18:-6,16:-18,14:-15,12:15,10:18,8:6,6:-13,4:-7,2:7,0:-1},3:{22:-4,20:4,18:5,16:9,14:-10,12:-13,10:12,8:7,6:-2,4:-3,2:1},2:{22:-2,20:-6,18:13,16:9,14:-7,12:-12,10:5,8:5,6:-4,4:1},1:{20:-3,18:1,16:4,14:-4,8:1,6:-1},0:{20:-1}}
m1={i:sum(row.values()) for i,row in p.items()}
factor={i:0 for i in range(9)}
for a in range(4):
 for b in range(6):factor[a+b]+=comb(3,a)*(-1)**(3-a)*comb(5,b)
assert m1==factor
point=sum(c*(-1024)**i*2**j for i,row in p.items() for j,c in row.items())
assert point!=0
# L-width is unchanged by Laurent units or simultaneous chirality inversion.
assert min(p)==0 and max(p)==8
out={'A_5_1':'L+M^10','A_10_132_coefficients':p,'L_widths':[1,8],'A10_at_M1':'(L-1)^3*(L+1)^5','A10_at_M2_Lminus1024':point,'scope':'Algebraic check of transcribed primary database entries; not an independent A-polynomial derivation.','sources':['https://katlas.org/wiki/Data:5_1/A-polynomial','https://katlas.org/wiki/Data:10_132/A-polynomial']}
Path(__file__).with_name('peripheral_collision.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: L-widths 1 and 8; A10(M=1)=(L-1)^3(L+1)^5; A10(-1024,2)=',point)
