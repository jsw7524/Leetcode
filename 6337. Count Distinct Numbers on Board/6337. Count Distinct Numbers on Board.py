class Solution:
    def distinctIntegers(self, n: int) -> int:
        if n <= 2:
            return 1
        return n-1
sln=Solution()
assert 1==sln.distinctIntegers(n=2)
assert 4==sln.distinctIntegers(n=5)