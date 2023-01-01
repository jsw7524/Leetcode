class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        n=len(s)
        dp=[10**6]*n
        kLength=len(str(k))
        for i in range(kLength-1):
            dp[i]=1
        dp[kLength-1] = 1 if k >= int(s[0:kLength]) else 2
        for i in range(kLength,n):
            for j in range(0,kLength):
                v=int(s[i-j:i+1])
                if k >= v:
                    dp[i]=min(dp[i], dp[i-j-1]+1)
        return -1 if 10**6==dp[n-1] else dp[n-1]
    
sln=Solution()
assert -1==sln.minimumPartition(s = "238182", k = 5)
assert 4==sln.minimumPartition(s = "165462", k = 60)
                    
                    
            
            