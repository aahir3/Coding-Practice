import math
n=int(input())
even_1=0
odd_1=0
if(n % 2 == 0):
    even_1=n//2
    odd_1=even_1
else:
    even_1=n//2
    odd_1=even_1+1
print(even_1,odd_1)
even=math.floor(n/2)
odd=math.ceil(n/2)
print(even,odd)