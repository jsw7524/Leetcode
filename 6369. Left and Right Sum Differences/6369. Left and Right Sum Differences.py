
from typing import List

class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        return [abs(sum(nums[:i]) - sum(nums[i+1:]))  for i in range(len(nums))]

sln=Solution()
assert [0]==sln.leftRigthDifference(nums = [1])
assert [15,1,11,22]==sln.leftRigthDifference(nums = [10,4,8,3])