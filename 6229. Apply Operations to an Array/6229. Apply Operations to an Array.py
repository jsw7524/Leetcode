from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        result=[n for n in nums if n > 0]                   
        return  result + [0]*(len(nums)-len(result))

sln= Solution()
assert [1,0]==sln.applyOperations(nums = [0,1])
assert [1,4,2,0,0,0]==sln.applyOperations(nums = [1,2,2,1,1,0])
            
                
            
            