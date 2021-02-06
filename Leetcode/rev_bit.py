class Solution:
    def reverseBits(self, n: int) -> int:
        temp=bin(n)
        rev=temp[2:]
        print(rev)
        rev=rev[::-1]
        rev=int(rev)
        return rev

c=Solution()
print(c.reverseBits(12))