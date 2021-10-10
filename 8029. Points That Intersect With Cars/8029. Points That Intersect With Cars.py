from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        parking=[0]*101
        for car in nums:
            for i in range(car[0],car[1]+1):
                parking[i]=1
        return sum(parking)

sln=Solution()
assert 7==sln.numberOfPoints(nums = [[3,6],[1,5],[4,7]])
assert 7==sln.numberOfPoints(nums = [[1,3],[5,8]])                
            