def fib_bottom_up(n):
    if n== 0:
        return 0
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]
def fibosum(n,m):
    s=0
    for i in range(n,m+1):
        s=(s+fib_bottom_up(i))%1000000007
    return s
T=int(input())
while T > 0:
    n,m=list(map(int,input().split()))
    print(fibosum(n,m))
    T-=1