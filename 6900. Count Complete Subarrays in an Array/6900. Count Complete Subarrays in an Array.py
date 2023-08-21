from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        numsLen=len(nums)
        distinctNums=len(set(nums))
        result=0
        for i in range(numsLen):
            s=set()
            for j in range(i,numsLen):
                s.add(nums[j])
                if distinctNums==len(s):
                    result+=1
        return result
    
sln=Solution()
assert 10==sln.countCompleteSubarrays(nums = [5,5,5,5])
assert 4==sln.countCompleteSubarrays(nums = [1,3,1,2,2])
                    
                
                
                