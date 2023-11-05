from typing import List

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n=len(grid)
        for i, g in enumerate(grid):
            if sum(g) == n-1:
                return i
        
sln=Solution()
assert 1==sln.findChampion(grid = [[0,0,1],[1,0,1],[0,0,0]])
assert 0==sln.findChampion(grid = [[0,1],[0,0]])
                