from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        result=[]
        for i in range(1,n-1):
            tmp=[]
            for j in range(1,n-1):
                tmp.append(max(grid[i-1][j-1],grid[i-1][j],grid[i-1][j+1],
                               grid[i][j-1],grid[i][j],grid[i][j+1],
                               grid[i+1][j-1],grid[i+1][j],grid[i+1][j+1]
                               ))
            result.append(tmp)
        return result

sln=Solution()
assert [[2,2,2],[2,2,2],[2,2,2]]==sln.largestLocal(grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]])
assert [[9,9],[8,6]]==sln.largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])
                
        