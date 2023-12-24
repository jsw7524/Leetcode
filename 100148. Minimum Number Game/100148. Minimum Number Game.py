from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0,len(nums),2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums

sln=Solution()
assert [5,2]==sln.numberGame(nums = [2,5])    
assert [3,2,5,4]==sln.numberGame(nums = [5,4,2,3])       