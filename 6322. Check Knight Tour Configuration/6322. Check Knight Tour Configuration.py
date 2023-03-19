from typing import List

class Solution:
    
    def checking(self, y, x, step):
        if x < 0 or x >= self.n or y < 0 or y >= self.n:
            return False
        if self.grid[y][x] == step:
            return True
        return False
    
    def dfs(self, y, x, step):
        if False==self.checking(y, x, step):
            return False
        if step == self.maxStep:
            return True
        result=[
        self.dfs( y-2, x+1, step+1),
        self.dfs( y-1, x+2, step+1),        
        self.dfs( y+1, x+2, step+1), 
        self.dfs( y+2, x+1, step+1), 
        self.dfs( y-2, x-1, step+1),
        self.dfs( y-1, x-2, step+1),        
        self.dfs( y+1, x-2, step+1),
        self.dfs( y+2, x-1, step+1)]
        return len([r for r in result if r==True])>0
    
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        self.n=len(grid)
        self.maxStep=(self.n**2)-1
        self.grid=grid
        return self.dfs( 0, 0, 0)

sln=Solution()
assert False==sln.checkValidGrid(grid = [[0,3,6],[5,8,1],[2,7,4]])
assert True==sln.checkValidGrid(grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]])