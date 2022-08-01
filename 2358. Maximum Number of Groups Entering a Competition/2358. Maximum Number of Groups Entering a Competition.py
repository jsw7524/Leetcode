from typing import List
import math

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n=len(grades)
        return math.ceil((-1 + (1-4*(-2*n))**0.5) //2)

sln=Solution()
assert 1==sln.maximumGroups(grades = [8,8])   
assert 3==sln.maximumGroups(grades = [10,6,12,7,3,5])
     
        
        