from typing import List

class Solution:
    
    def minimumArea(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        top,down,left,right=1,1,1,1
        #top        
        for i in range(m):
            if sum(grid[i]) > 0:
                top=i
                break
        #left
        for j in range(n):
            for i in range(m):
                if grid[i][j]==1:
                    left=j
                    break
            else:
                continue
            break
                
        #down
        for i in range(m-1,-1,-1):
            if sum(grid[i]) > 0:
                down=i
                break
        #right   
        for j in range(n-1,-1,-1):        
            for i in range(m-1,-1,-1):              
                if grid[i][j]==1:
                    right=j
                    break
            else:
                continue
            break            
        return (down-top+1)*(right-left+1)
    
sln=Solution()

assert 4==sln.minimumArea(grid = [[0,0,0],[0,0,0],[0,0,1],[0,1,0]])  

assert 1==sln.minimumArea(grid = [[0,0],[1,0]])  
assert 6==sln.minimumArea(grid = [[0,1,0],[1,0,1]])        