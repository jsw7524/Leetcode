from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()        
        minValue=nums[0]
        maxValue=nums[0]
        segments=1
        for n in nums[1:]:
            if n > maxValue:
                maxValue=n
            if n < minValue:
                minValue=n
            if maxValue-minValue>k:
                segments+=1
                maxValue=n
                minValue=n
        return segments
    
sln=Solution()
assert 2==sln.partitionArray(nums = [5,0], k = 0)
assert 4==sln.partitionArray(nums = [3,1,3,4,2], k = 0)
assert 3==sln.partitionArray(nums = [2,2,4,5], k = 0)
assert 2==sln.partitionArray(nums = [3,6,1,2,5], k = 2)
assert 2==sln.partitionArray(nums = [1,2,3], k = 1)