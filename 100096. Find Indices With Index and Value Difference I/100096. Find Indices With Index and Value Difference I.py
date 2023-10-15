from typing import List

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        numsLen=len(nums)
        for i in range(numsLen):
            for j in range(i,numsLen):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i,j]
        return [-1,-1]
    

sln=Solution()
assert [-1,-1]==sln.findIndices(nums = [1,2,3], indexDifference = 2, valueDifference = 4)
assert [0,0]==sln.findIndices(nums = [2,1], indexDifference = 0, valueDifference = 0)
assert [0,3]==sln.findIndices(nums = [5,1,4,1], indexDifference = 2, valueDifference = 4)