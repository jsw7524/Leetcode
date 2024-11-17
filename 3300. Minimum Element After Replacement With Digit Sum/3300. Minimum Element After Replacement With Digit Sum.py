from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(int(d) for d in str(n)) for n in nums)
    
sln=Solution()
assert 10==sln.minElement(nums = [999,19,199])
assert 1==sln.minElement(nums = [1,2,3,4])
assert 1==sln.minElement(nums = [10,12,13,14])