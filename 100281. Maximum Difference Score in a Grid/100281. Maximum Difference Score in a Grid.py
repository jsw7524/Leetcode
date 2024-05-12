from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n, maxDiff = len(grid), len(grid[0]), -9999999
        info=[[ 0 for x in range(n) ] for y in range(m)]
        for y in range(m-1,-1,-1):
            for x in range(n-1,-1,-1):
                if y+1 >= m and x+1 >= n:
                    info[y][x]=grid[y][x]
                elif y+1 >= m:
                    info[y][x]=max(grid[y][x],info[y][x+1])
                    maxDiff=max(maxDiff, info[y][x+1]-grid[y][x])
                elif x+1 >= n:
                    info[y][x]=max(grid[y][x],info[y+1][x])
                    maxDiff=max(maxDiff, info[y+1][x]-grid[y][x])
                else:
                    info[y][x]=max(grid[y][x],info[y][x+1],info[y+1][x])
                    maxDiff=max(maxDiff, info[y+1][x]-grid[y][x], info[y][x+1]-grid[y][x])
        return maxDiff

sln=Solution()
assert -1==sln.maxScore( grid = [[4,3,2],[3,2,1]])
assert 9==sln.maxScore(grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]])