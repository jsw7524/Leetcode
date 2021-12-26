class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        if num%10==0:
            return False
        return True

sln=Solution()
assert True==sln.isSameAfterReversals(num = 526)
assert False==sln.isSameAfterReversals(num = 1800)
assert True==sln.isSameAfterReversals(num = 0)  