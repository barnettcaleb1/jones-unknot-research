import sys; sys.path.insert(0,sys.argv[1])
from w60 import *
vc=[{2:1,-2:1},{0:1},{0:1},{2:1,-2:1},{4:1,0:1,-4:1}]
TC=[1,2]*3
for j in range(DIM):
    e=[{} for _ in range(DIM)]; e[j]={0:1}
    print(j,'H(vc,e_j)=',lstr(H(vc,e)))
print('H(vc,vc)=',lstr(H(vc,vc)))
e=[{} for _ in range(DIM)]; e[4]={0:1}
print('T_c^2 e_4 =',[lstr(x) for x in rvec(TC*2,e)])
