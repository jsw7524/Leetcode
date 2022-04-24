from typing import List

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        grid = [[0 for x in range(201)] for y in range(201)]
        
        for x, y, r in circles:
            for i in range(x-r, x+r+1):
                for j in range(y-r, y+r+1):
                    if (i-x)**2 + (j-y)**2 <= r**2:
                        grid[i][j] = 1
        
        return sum(sum(row) for row in grid)
    
sln=Solution()
assert 5==sln.countLatticePoints(circles = [[2,2,1]])
assert 16==sln.countLatticePoints(circles = [[2,2,2],[3,4,1]])         