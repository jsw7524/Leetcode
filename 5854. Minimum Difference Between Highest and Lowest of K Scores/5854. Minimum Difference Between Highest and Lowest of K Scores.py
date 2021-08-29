from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # if 1==k:
        #     return 0
        nums.sort()
        minimumDifference=10**6
        numsLen=len(nums)
        for i in range(0,numsLen-k+1):
            if minimumDifference > nums[i+(k-1)] - nums[i]:
                minimumDifference = nums[i+(k-1)] - nums[i]
        return minimumDifference

sln=Solution()
assert 0==sln.minimumDifference(nums = [90], k = 1)
assert 2==sln.minimumDifference(nums = [9,4,1,7], k = 2)
            