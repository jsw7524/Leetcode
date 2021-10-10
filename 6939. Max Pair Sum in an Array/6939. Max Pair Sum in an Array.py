from typing import List

class Solution:
    def maxDigit(self, nums):
        return max([ n for n in str(nums)])
    
    def maxSum(self, nums: List[int]) -> int:
        length=len(nums)
        maxPair=-1
        for i in range(length):
            for j in range(i+1,length):
                if self.maxDigit(nums[i]) == self.maxDigit(nums[j]):
                    maxPair=max(nums[i]+nums[j],maxPair)
        return maxPair

sln=Solution()

assert -1==sln.maxSum(nums = [1,2,3,4])   
assert 88==sln.maxSum(nums = [51,71,17,24,42])                
                