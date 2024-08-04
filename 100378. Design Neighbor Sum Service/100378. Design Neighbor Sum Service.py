from typing import List

class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.adjacent={}
        self.diagonal={}
        self.row=len(grid)
        self.col=len(grid[0])        
        
        for r, content in enumerate(grid):
            content.append(0)
        grid.append([0 for _ in range(self.col+1)])
        
        for r, content in enumerate(grid[:-1]):
            for c, elm in enumerate(content[:-1]):
                self.adjacent[elm]=grid[r-1][c]+grid[r+1][c]+grid[r][c-1]+grid[r][c+1]
                self.diagonal[elm]=grid[r-1][c-1]+grid[r-1][c+1]+grid[r+1][c-1]+grid[r+1][c+1]
        return

    def adjacentSum(self, value: int) -> int:
        return self.adjacent[value]
        

    def diagonalSum(self, value: int) -> int:
        return self.diagonal[value]
    
sln=neighborSum([[0,1,2],[3,4,5],[6,7,8]])