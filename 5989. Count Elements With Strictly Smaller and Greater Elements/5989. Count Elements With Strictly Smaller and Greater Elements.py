
from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        counter=0
        for n in nums:
            if nums[0] < n <nums[-1]:
                counter+=1
        return counter
    
sln=Solution()
assert 2==sln.countElements(nums = [11,7,2,15])
assert 2==sln.countElements(nums = [-3,3,3,90])
assert 0==sln.countElements(nums = [5,5,5,5,5,5,5,5])