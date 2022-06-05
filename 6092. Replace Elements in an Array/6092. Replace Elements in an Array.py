from typing import List

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mapInfo=[-1]*(2+10**6)
        for i,v in enumerate(nums):
            mapInfo[v]=i        
        for op in operations:
            mapInfo[op[1]]=mapInfo[op[0]]   
            nums[mapInfo[op[0]]]=op[1]                     
            mapInfo[op[0]]=-1
        return nums
    
sln=Solution()
assert [2,1]==sln.arrayChange(nums = [1,2], operations = [[1,3],[2,1],[3,2]])
assert [3,2,7,1]==sln.arrayChange(nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]])

            
            
            