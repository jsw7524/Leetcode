from typing import List

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        right, left = n-1, 0
        concatenationValue = 0
        while right > left:
            tmp=str(nums[left])+str(nums[right])
            concatenationValue+=int(tmp)
            right-=1
            left+=1
        if right == left:
            concatenationValue+=nums[right]
        return concatenationValue
    
sln=Solution()
assert 673==sln.findTheArrayConcVal(nums = [5,14,13,8,12])
assert 596==sln.findTheArrayConcVal(nums = [7,52,2,4])
        
