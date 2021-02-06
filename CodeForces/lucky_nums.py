def f(n):
    if(n == 4 or n == 7):
        return True
def fun(n):
    arr=[]
    for i in range(4,n+1):
        while(i > 0):
            digit=i
            rem=i%10
            while(f(rem)):
                
            i=i//10
    return arr.index(n)+1
n=int(input())
print(fun(n))