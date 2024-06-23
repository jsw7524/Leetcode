from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        return min((nums[i] + nums[-(i+1)])/2  for i in range(len(nums)//2))
    
sln=Solution()
assert 5.0==sln.minimumAverage(nums = [1,2,3,7,8,9])
assert 5.5==sln.minimumAverage(nums = [1,9,8,3,10,5])
assert 5.5==sln.minimumAverage(nums = [7,8,3,4,15,13,4,1])