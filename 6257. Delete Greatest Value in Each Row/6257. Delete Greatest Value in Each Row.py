from typing import List

import numpy as np
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        answer=0
        data=np.array(grid)
        col=len(grid[0])
        for c in range(col):
            valMax=data.max(axis=1)
            answer+=valMax.max()
            posMax=data.argmax(axis=1)
            for r,p in enumerate(posMax):
                data[r][p]=0
        return answer
        
sln=Solution()
assert 10==sln.deleteGreatestValue(grid = [[10]])
assert 8==sln.deleteGreatestValue(grid = [[1,2,4],[3,3,1]])