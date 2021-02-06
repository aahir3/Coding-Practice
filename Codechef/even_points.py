T=int(input())
while T > 0:
    a,b=list(map(int,input().split()))
    if a % 2 == 0:
	    odd_a = a//2
	    even_a = a//2
    else:
        odd_a = (a+1)//2
        even_a = (a-1)//2
    if(b % 2 == 0):
	    odd_b = b//2
	    even_b = b//2
    else:
        odd_b = (b+1)//2
        even_b = (b-1)//2
    sum= odd_a*odd_b + even_a*even_b
    print(int(sum))
    T-=1