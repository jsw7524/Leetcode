class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1=sum([  i for i in range(n+1) if i%m!=0])
        num2=sum([  i for i in range(n+1) if i%m==0])
        return num1-num2

sln=Solution()
assert -15==sln.differenceOfSums(n = 5, m = 1)
assert 15==sln.differenceOfSums(n = 5, m = 6)
assert 19==sln.differenceOfSums(n = 10, m = 3)