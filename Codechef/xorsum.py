def fun(arr,m):
    if m <= 1:
        return sum(arr)%998
    else:
        return fun(arr,m-1)
n=int(input())
arr=list(map(int,input().split()))
for _ in range(int(input())):
    m=int(input())
    print(fun(arr,m))