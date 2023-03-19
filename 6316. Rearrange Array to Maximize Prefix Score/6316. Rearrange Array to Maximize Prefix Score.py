from typing import List

import numpy as np
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        data=np.array(sorted(nums,reverse=True))
        prefix = np.add.accumulate(data)
        return  len(prefix[prefix > 0])

sln=Solution()
assert 0==sln.maxScore(nums = [-2,-3,0])
assert 6==sln.maxScore(nums = [2,-1,0,1,-3,3,-3])