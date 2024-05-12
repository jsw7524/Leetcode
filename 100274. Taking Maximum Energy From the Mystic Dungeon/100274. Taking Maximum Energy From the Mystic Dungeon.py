from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n=len(energy)
        dp=[0 for i in range(n)]
        for i in range(n-1,-1,-1):
            if i+k >= n:
                dp[i]=energy[i]
            else:
                dp[i]=energy[i]+dp[i+k]
        return max(dp)

sln = Solution()
assert -1==sln.maximumEnergy(energy = [-2,-3,-1], k = 2)
assert 3==sln.maximumEnergy(energy = [5,2,-10,-5,1], k = 3)

           