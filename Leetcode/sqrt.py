import math
class Solution:
    def mySqrt(self, x: int) -> int:
        #return int(math.sqrt(x))
        if x==0 or x==1:
            return x
        else:
            start = 0
            end = x  
            while (start <= end):
                mid = int((start + end) / 2)
                if (mid*mid == x):
                    return mid
                elif (mid*mid < x):
                    start = mid + 1
                    ans = mid
                else:
                    end = mid - 1
            return ans