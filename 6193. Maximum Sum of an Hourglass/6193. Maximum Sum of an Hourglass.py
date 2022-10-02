from typing import List

class Solution:
    def hourGlass(self, grid: List[List[int]], y:int, x: int)->int:
        return grid[y][x]+grid[y][x+1]+grid[y][x+2]+grid[y+1][x+1]+grid[y+2][x]+grid[y+2][x+1]+grid[y+2][x+2]
        
    def maxSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        ans=0
        for y in range(m-3+1):
            for x in range(n-3+1):
                ans=max(ans,self.hourGlass(grid, y, x))
        return ans
    
sln=Solution()
assert 35==sln.maxSum(grid = [[1,2,3],[4,5,6],[7,8,9]])
assert 30==sln.maxSum(grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]])
                
            