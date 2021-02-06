import math
def fun(n,k,arr):
    solved=0
    rejected=False
    too_slow=False
    bot=False
    count_for_bot=0
    for i in range(n):
        if(arr[i] != -1):
            solved+=1
            if(arr[i] > k):
                too_slow=True
            if arr[i] <= 1:
                count_for_bot+=1
    rejected=solved < math.ceil(n/2)
    if(rejected):
        return "Rejected"
    if(not rejected and too_slow):
        return "Too Slow"
    if(count_for_bot == n):
        bot=True
        return "Bot"
    return "Accepted"
        
T=int(input())
while T > 0:
    n,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    print(fun(n,k,arr))
    T-=1