from typing import List

class info:
    nx=0
    ny=0
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        dp=[ [ info() for x in range(col)]  for y in range(row)]
        result=0
        #first cell
        if grid[0][0]=='X':
            dp[0][0].nx=1                             
        elif grid[0][0]=='Y':
            dp[0][0].ny=1      
        #first row
        for c in range(1,col):
            dp[0][c].ny=dp[0][c-1].ny
            dp[0][c].nx=dp[0][c-1].nx              
            if grid[0][c]=='X':
                dp[0][c].nx+=1                         
            elif grid[0][c]=='Y':
                dp[0][c].ny+=1

            if dp[0][c].ny>0 and dp[0][c].nx >0 and dp[0][c].ny == dp[0][c].nx:
                result+=1
                
        #first col
        for r in range(1,row):
            dp[r][0].ny=dp[r-1][0].ny
            dp[r][0].nx=dp[r-1][0].nx              
            
            if grid[r][0]=='X':
                dp[r][0].nx+=1                         
            elif grid[r][0]=='Y':
                dp[r][0].ny+=1 
                
            if dp[r][0].ny>0 and dp[r][0].nx >0 and dp[r][0].ny == dp[r][0].nx:
                result+=1
                
        #rest cells
        for r in range(1,row):                
            for c in range(1,col):
                dp[r][c].ny=dp[r][c-1].ny + (dp[r-1][c].ny -dp[r-1][c-1].ny)
                dp[r][c].nx=dp[r][c-1].nx + (dp[r-1][c].nx -dp[r-1][c-1].nx)               
                
                if grid[r][c]=='X':
                    dp[r][c].nx+=1                         
                elif grid[r][c]=='Y':
                    dp[r][c].ny+=1
                    
                if dp[r][c].ny>0 and dp[r][c].nx >0 and dp[r][c].ny == dp[r][c].nx:
                    result+=1
        return result
    
    
sln=Solution()
assert 1==sln.numberOfSubmatrices([[".","X"],[".","Y"]])
assert 1==sln.numberOfSubmatrices([[".","."],["Y","X"]])
assert 0==sln.numberOfSubmatrices(grid = [[".","."],[".","."]])
assert 0==sln.numberOfSubmatrices(grid = [["X","X"],["X","Y"]])
assert 3==sln.numberOfSubmatrices(grid = [["X","Y","."],["Y",".","."]])       