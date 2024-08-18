from typing import List

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        dp = [ [0 for _ in range(n)], [0 for _ in range(n)]]
        dp[0][0]=energyDrinkA[0]
        dp[1][0]=energyDrinkB[0]
        dp[0][1]=energyDrinkA[0]+energyDrinkA[1]
        dp[1][1]=energyDrinkB[0]+energyDrinkB[1]
        for hr in range(2,n):
            dp[0][hr]=max(dp[0][hr-1],dp[1][hr-2])+energyDrinkA[hr]
            dp[1][hr]=max(dp[0][hr-2],dp[1][hr-1])+energyDrinkB[hr]
        return max(dp[0][n-1],dp[1][n-1])
    
sln=Solution()

assert 34==sln.maxEnergyBoost(energyDrinkA = [4,3,4,4,3,6,5,5], energyDrinkB = [4,6,4,4,5,3,4,4])

# assert 7==sln.maxEnergyBoost(energyDrinkA = [4,1,1], energyDrinkB = [1,1,3])
# assert 7==sln.maxEnergyBoost(energyDrinkA = [4,1,1], energyDrinkB = [1,1,3])
# assert 5==sln.maxEnergyBoost(energyDrinkA = [1,3,1], energyDrinkB = [3,1,1])

