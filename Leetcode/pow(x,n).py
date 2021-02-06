class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n == 0):
            return 1
        if(n == 1):
            return x
        elif(n%2 == 0):
            temp=pow(x,n//2)
            return temp*temp
        else:
            t=pow(x,(n-1)//2)
            return t*t*x
        