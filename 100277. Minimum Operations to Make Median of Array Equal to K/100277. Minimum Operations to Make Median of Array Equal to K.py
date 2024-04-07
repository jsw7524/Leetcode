from typing import List

import math
class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        pass
        
sln=Solution()

assert 109==sln.minOperationsToMakeMedianK(nums = [91,88], k = 35)

assert 0==sln.minOperationsToMakeMedianK(nums = [1,2,3,4,5,6], k = 4)
assert 3==sln.minOperationsToMakeMedianK(nums = [2,5,6,8,5], k = 7)
assert 2==sln.minOperationsToMakeMedianK(nums = [2,5,6,8,5], k = 4)
        