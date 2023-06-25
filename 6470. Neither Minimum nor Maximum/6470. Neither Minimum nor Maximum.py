from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return -1
        nums.sort()
        return nums[1]
        
sln=Solution()
assert 2==sln.findNonMinOrMax(nums = [2,1,3])
assert -1==sln.findNonMinOrMax(nums = [1,2])
assert 2==sln.findNonMinOrMax(nums = [3,2,1,4])