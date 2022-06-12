from typing import List

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp = [[grid[y][x] for x in range(n)] for y in range(m)] 
        for y in range(1,m):
            for x in range(n):
                dp[y][x]+=min([dp[y-1][i]+moveCost[grid[y-1][i]][x] for i in range(n)])
        return min(dp[-1])
    
sln=Solution()
assert 6==sln.minPathCost(grid = [[5,1,2],[4,0,3]], moveCost = [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]])
assert 17==sln.minPathCost(grid = [[5,3],[4,0],[2,1]], moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]])
                    
