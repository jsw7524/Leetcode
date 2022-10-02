class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans=0
        for i in range(1,min(a,b)+1):
            if a%i==0 and b%i==0:
                ans+=1
        return ans
sln=Solution()
assert 4==sln.commonFactors(a = 12, b = 6)
assert 2==sln.commonFactors(a = 25, b = 30)                