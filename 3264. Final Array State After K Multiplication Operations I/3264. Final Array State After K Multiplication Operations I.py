from typing import List
import numpy

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            j=numpy.argmin(nums)
            nums[j]*=multiplier
        return nums
    
sln=Solution()
assert [16,8]==sln.getFinalState(nums = [1,2], k = 3, multiplier = 4)
assert [8,4,6,5,6]==sln.getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2)