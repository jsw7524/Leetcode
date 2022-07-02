from typing import List

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if 0==(i-j) or n == 1+(i+j):
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False 
        return True
    
sln=Solution()
assert False==sln.checkXMatrix(grid = [[5,7,0],[0,3,1],[0,5,0]])             
assert True==sln.checkXMatrix(grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]])             
                        
                    
                    
        