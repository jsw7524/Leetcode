class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp=[ [0 for x in range(1000+1)] for i in range(n+1)]
        for j in range(1, k+1):
            dp[1][j]=1
        for i in range(2, n+1):
            for j in range(i, target+1):
                for d in range(1,k+1):
                    if (j-d >= i-1):
                        dp[i][j]=(dp[i][j]+dp[i-1][j-d])%(10**9+7)
        return dp[n][target]