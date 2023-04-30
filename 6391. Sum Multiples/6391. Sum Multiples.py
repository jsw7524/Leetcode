class Solution:
    def sumOfMultiples(self, n: int) -> int:
        result=0
        for i in range(3, n+1):
            result += i if ((i%3==0) or (i%5==0) or (i%7==0)) else 0
        return result

sln=Solution()
assert 30==sln.sumOfMultiples(n = 9)
assert 40==sln.sumOfMultiples(n = 10)
assert 21==sln.sumOfMultiples(n = 7)
            