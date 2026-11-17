"""Known Burau-kernel words; commutator convention [a,b]=aba^-1b^-1."""
def inv(w): return [-s for s in reversed(w)]
def reduce(w):
    out=[]
    for s in w:
        if out and out[-1]==-s: out.pop()
        else: out.append(s)
    return out
def comm(a,b): return reduce(a+b+inv(a)+inv(b))
def conj(w,p): return reduce(inv(p)+w+p)
BIGELOW5_PSI1=[-3,2,1,1,2,4,4,4,3,2]
BIGELOW5_PSI2=[-4,3,2,-1,-1,2,1,1,2,2,1,4,4,4,4,4]
BIGELOW5=comm(conj([4],BIGELOW5_PSI1),conj([4,3,2,1,1,2,3,4],BIGELOW5_PSI2))
# Bigelow 1999 pp403-404, also Ren arXiv:2609.11084v2 section2.2.
BIGELOW6_PSI1=[4,-5,-2,1]
BIGELOW6_PSI2=[-4,5,5,2,-1,-1]
BIGELOW6_REN=comm(conj([3],BIGELOW6_PSI1),conj([3],BIGELOW6_PSI2))
# Transcribed visually from Long--Paton, Topology32(1993), p444 ExampleA.
LONG_PATON_PSI=[-5,-4,5,-3,4,-2,-3,-3,-3,1,1,1,5,4,-3,-2,1]
LONG_PATON6=comm(conj([5],LONG_PATON_PSI),[2,3,4,5]*5)
WORDS={'Bigelow5':(5,BIGELOW5),'Bigelow6_Ren':(6,BIGELOW6_REN),'LongPaton6':(6,LONG_PATON6)}
