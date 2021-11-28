from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result=[]
        for i, e in enumerate(nums):
            if e==target:
                result.append(i)
        return result
                