class Solution:
    def countHousePlacements(self, n: int) -> int:
        if n==1:
            return 4
        if n==2:
            return 9
        
        dp=(n+1)*[0]
        dp[1]=2
        dp[2]=3
        for i in range(3, n+1):
            dp[i]=(dp[i-1]+dp[i-2])%(10**9 + 7)
            
        return (dp[n]**2)%(10**9 + 7)

sln=Solution()
assert 25 ==sln.countHousePlacements(n = 3)
assert 9 ==sln.countHousePlacements(n = 2)
assert 4 ==sln.countHousePlacements(n = 1)
            
            