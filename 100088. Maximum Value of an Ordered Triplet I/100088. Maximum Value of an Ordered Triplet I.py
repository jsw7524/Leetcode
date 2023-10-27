from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        length = len(nums)
        maxValue=0
        for i in range(length):
            for j in range(i+1,length):
                for k in range(j+1,length):
                    maxValue=max((nums[i] - nums[j]) * nums[k],maxValue)
        return maxValue
                    