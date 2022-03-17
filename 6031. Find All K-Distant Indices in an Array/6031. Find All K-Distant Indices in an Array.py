from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result=set()
        for i, n in enumerate(nums):
            if n == key:
                for j in range(max(0,i-k),min(len(nums),i+k+1)):
                    result.add(j)
        return list(result)

sln=Solution()
assert [1,2,3,4,5,6]==sln.findKDistantIndices(nums = [3,4,9,1,3,9,5], key = 9, k = 1)
assert [0,1,2,3,4]==sln.findKDistantIndices(nums = [2,2,2,2,2], key = 2, k = 2)                