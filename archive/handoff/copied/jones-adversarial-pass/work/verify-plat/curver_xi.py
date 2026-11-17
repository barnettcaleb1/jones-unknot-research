import curver, sys
sys.path.insert(0, '')
M = curver.load(0, 6)
def w2s(w):  # sigma_i -> s_{i-1}; inverse -> S_{i-1}
    return '.'.join(('s_%d' % (g-1)) if g > 0 else ('S_%d' % (-g-1)) for g in w) or ''
def mc(w): return M(w2s(w)) if w else M('s_0.S_0')
def inv(w): return [-s for s in reversed(w)]
def red(w):
    out=[]
    for s in w:
        if out and out[-1]==-s: out.pop()
        else: out.append(s)
    return out
def comm(a,b): return red(a+b+inv(a)+inv(b))
def conj(w,p): return red(inv(p)+w+p)
PSI=[-5,-4,5,-3,4,-2,-3,-3,-3,1,1,1,5,4,-3,-2,1]
XI=comm(conj([5],PSI),[2,3,4,5]*5)
# sanity: braid relations among s_0..s_4 and identity test
print('s0 s1 s0 == s1 s0 s1:', mc([1,2,1]) == mc([2,1,2]))
print('s0 s2 == s2 s0:', mc([1,3]) == mc([3,1]))
print('s0 nontrivial:', not mc([1]).is_identity())
print('T=(s2s3s4s5)^5 identity in Mod(S_0,6):', mc([2,3,4,5]*5).is_identity())
print('Delta^2=(s1..s5)^6 identity:', mc([1,2,3,4,5]*6).is_identity())
print('sphere rel s1..s5 s5..s1 identity:', mc([1,2,3,4,5,5,4,3,2,1]).is_identity())
h = conj([5],PSI)
print('h=psi^-1 s5 psi nontrivial:', not mc(h).is_identity())
print('xi identity in Mod(S_0,6):', mc(XI).is_identity())
# control: a nontrivial commutator should NOT be identity
print('control [s1, s2 s3 s2] identity?:', mc(comm([1],[2,3,2])).is_identity())
