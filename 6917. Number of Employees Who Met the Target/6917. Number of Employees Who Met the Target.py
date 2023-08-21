from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum([ 1 if h>=target else 0 for h in  hours])
    
sln=Solution()
assert 0==sln.numberOfEmployeesWhoMetTarget(hours = [5,1,4,2,2], target = 6)
assert 3==sln.numberOfEmployeesWhoMetTarget(hours = [0,1,2,3,4], target = 2)
        