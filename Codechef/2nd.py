from math import gcd
def lcm(a,b):
    return a*b//gcd(a,b)
def solve(A):
    ans=0
    for i in range(len(A)):
        l=len(A)
        mid=l//2
        a,b,c=lcm(A[0],A[l-1]),lcm(A[mid],A[l-1]),lcm(A[0],A[mid])
        m=max(a,b,c)
        if(m == a):
        ans+=m