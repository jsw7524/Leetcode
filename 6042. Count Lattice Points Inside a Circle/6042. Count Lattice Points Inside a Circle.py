from typing import List

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:    
        record={}
        counter=0
        for x, y, r in circles:
            for i in range(x-r, x+r+1):
                for j in range(y-r, y+r+1):
                    if (i-x)**2 + (j-y)**2 <= r**2:
                        if (i,j) not in record:
                            counter += 1
                            record[(i,j)]=1
        return counter
    
sln=Solution()
assert 5==sln.countLatticePoints(circles = [[2,2,1]])
assert 16==sln.countLatticePoints(circles = [[2,2,2],[3,4,1]])         