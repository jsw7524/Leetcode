from typing import List

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res=0
        for i in range(len(nums)):
            if bin(i).count('1')==k:
                res+=nums[i]
        return res

sln=Solution()
assert 1==sln.sumIndicesWithKSetBits(nums = [4,3,2,1], k = 2)
assert 13==sln.sumIndicesWithKSetBits(nums = [5,10,1,5,2], k = 1)
        