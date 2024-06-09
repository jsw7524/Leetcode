class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        dp = [1 for _ in range(n)]
        for i in range(k):
            for j in range(1,n):
                dp[j]+=dp[j-1]
        return dp[-1]%(10**9 + 7)
    
sln=Solution()
assert 84793457==sln.valueAfterKSeconds(n = 5, k = 1000)
assert 35==sln.valueAfterKSeconds(n = 5, k = 3)
assert 56==sln.valueAfterKSeconds(n = 4, k = 5)