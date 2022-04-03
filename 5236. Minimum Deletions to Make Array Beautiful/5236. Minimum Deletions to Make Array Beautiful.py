from typing import List

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        answer=0
        for i in range(len(nums)):
            if 1 == (i+1) % 2:
                answer+=1
            else:
                if nums[i] == nums[i-1]:
                    answer+=1     
        return answer
    
sln=Solution()
assert 1==sln.minDeletion(nums = [1,1,2,3,5])