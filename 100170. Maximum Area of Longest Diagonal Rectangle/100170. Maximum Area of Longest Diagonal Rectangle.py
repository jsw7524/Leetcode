from typing import List

import math
from functools import cmp_to_key
class Solution:
    def compare(self, x, y):
        xLen=math.sqrt(x[0]**2 + x[1]**2)
        yLen=math.sqrt(y[0]**2 + y[1]**2)       
        if ( xLen == yLen):
            return  1 if x[0]*x[1] > y[0]*y[1] else -1
        return  1 if xLen > yLen else -1
        
    
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        result=sorted(dimensions, key=cmp_to_key(self.compare))
        return result[-1][0]*result[-1][1]
        
        
sln= Solution()

assert 12==sln.areaOfMaxDiagonal(dimensions = [[3,4],[4,3]])
assert 48==sln.areaOfMaxDiagonal(dimensions = [[9,3],[8,6]])