
from typing import List
from collections import defaultdict
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dictResult=defaultdict(int)
        for id,v in nums1:
            dictResult[id]+=v
        for id,v in nums2:
            dictResult[id]+=v
        result=[ [id, v] for id, v in dictResult.items()]
        result.sort()
        return result

sln=Solution()
assert [[1,3],[2,4],[3,6],[4,3],[5,5]]==sln.mergeArrays(nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]])
assert [[1,6],[2,3],[3,2],[4,6]]==sln.mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]])
            
            
        