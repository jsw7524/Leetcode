from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        length=len(nums)
        diff = [0] * (length+1)
        for l, r in queries:
            diff[l]+=1
            diff[r+1]-=1
        current=0
        for i in range(length):
            current += diff[i]
            if current < nums[i]:
                return False
        return True

sln=Solution()
assert True == sln.isZeroArray(nums = [2], queries = [[0,0],[0,0],[0,0]])
assert False == sln.isZeroArray(nums = [4,3,2,1], queries = [[1,3],[0,2]])
assert True == sln.isZeroArray(nums = [1,0,1], queries = [[0,2]])
             