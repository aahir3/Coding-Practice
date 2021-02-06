def count(n):
    c=0
    while(n > 0):
        n=n&(n-1)
        c+=1
    return c

n=int(input())
print(count(n))