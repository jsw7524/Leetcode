from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result=set(nums[0])
        for data in nums[1:]:
            result=result&set(data)   
        return sorted([n for n in result])

sln=Solution()
assert [3,4]==sln.intersection(nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]])
assert []==sln.intersection(nums = [[1,2,3],[4,5,6]])            