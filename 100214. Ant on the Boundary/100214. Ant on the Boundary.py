from typing import List

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        return sum([1 if sum(nums[:i+1])==0 else 0 for i in range(len(nums))])
    
sln=Solution()
assert 0==sln.returnToBoundaryCount( nums = [3,2,-3,-4])   
assert 1==sln.returnToBoundaryCount( nums = [2,3,-5])           