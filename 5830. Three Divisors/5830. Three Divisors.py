class Solution:
    def isThree(self, n: int) -> bool:
        divisors=1
        for i in range(1,n):
            if n % i ==0:
                divisors+=1
        return True if divisors==3 else False

sln=Solution()
assert False == sln.isThree(n=2)                  
assert True == sln.isThree(n=4)    