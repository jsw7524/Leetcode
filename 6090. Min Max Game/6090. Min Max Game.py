from typing import List

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        return nums[0]if 1==len(nums)else self.minMaxGame([(max if i%2 else min)(nums[2*i],nums[2*i+1]) for i in range(len(nums)//2)])

sln=Solution()
assert 3==sln.minMaxGame(nums = [3])
assert 1==sln.minMaxGame(nums = [1,3,5,2,4,8,2,2])