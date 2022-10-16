from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        info={n:1 for n in nums}
        nums.sort(reverse=True)
        for n in nums:
            if -n in info:
                return abs(n)
        return -1

sln=Solution()
assert -1==sln.findMaxK(nums = [-10,8,6,7,-2,-3])
assert 7==sln.findMaxK(nums = [-1,10,6,7,-7,1])
assert 3==sln.findMaxK(nums = [-1,2,-3,3])
        