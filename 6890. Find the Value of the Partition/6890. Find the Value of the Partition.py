from typing import List

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        partitionValue=2*10**9
        for i in range(n-1):
            if nums[i+1]-nums[i] < partitionValue :
                partitionValue=nums[i+1]-nums[i]
        return partitionValue
    
sln=Solution()
assert 9==sln.findValueOfPartition(nums = [100,1,10])
assert 1==sln.findValueOfPartition(nums = [1,3,2,4])