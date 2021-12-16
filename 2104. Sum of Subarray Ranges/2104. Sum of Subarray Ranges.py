from typing import List

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        lenNums=len(nums)
        subarrayRangeSum=0
        for i in range(lenNums):
            maxN=nums[i]
            minN=nums[i]
            for j in range(i,lenNums):
                maxN=max(maxN,nums[j])
                minN=min(minN,nums[j])
                subarrayRangeSum+=(maxN-minN)
        return subarrayRangeSum

sln=Solution()
assert 4==sln.subArrayRanges(nums = [1,2,3])
assert 59==sln.subArrayRanges(nums = [4,-2,-3,4,1])