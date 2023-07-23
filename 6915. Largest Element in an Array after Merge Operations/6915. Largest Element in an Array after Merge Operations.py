from typing import List

class Solution:
    def merge(self, nums):
        stack=[nums[0]]
        numsLen=len(nums)
        for i in range(1,numsLen):
            if  nums[i-1] <= nums[i]:
                stack[-1]=stack[-1]+nums[i]
            else:
                stack.append(nums[i])
        return stack
        
    def maxArrayValue(self, nums: List[int]) -> int:
        tmp=[nums[-1]]
        numsLen=len(nums)
        for i in range(numsLen-2,-1,-1):
            if tmp[-1] >= nums[i]:
                tmp[-1]+=nums[i]
            else:
                tmp.append(nums[i])
        return max(tmp)
                

sln=Solution()
assert 781==sln.maxArrayValue(nums = [40,15,35,98,77,79,24,62,53,84,97,16,30,22,49])
assert 11==sln.maxArrayValue(nums = [5,3,3])
assert 21==sln.maxArrayValue(nums = [2,3,7,9,3])
                
                