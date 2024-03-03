from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m=len(grid)
        n=len(grid[0])
        # make table
        table=[[0 for x in range(n)] for y in range(m)]
        for y in range(m):
            tmp=0
            for x in range(n):
                tmp+=grid[y][x]
                table[y][x]=tmp
        #algo
        result=0
        for x in range(n):
            matrixSum=0
            for y in range(m):
                matrixSum+=table[y][x]
                if matrixSum <= k:
                    result+=1
                else:
                    break
        return result
    
sln=Solution()
assert 6==sln.countSubmatrices(grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20)
assert 4==sln.countSubmatrices(grid = [[7,6,3],[6,6,1]], k = 18)
