from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        info=[]
        for i, n in enumerate(nums):
            if n==x:
                info.append(i)
        return [ info[q-1] if q-1 < len(info) else -1 for q in queries]
                
sln=Solution()
assert [-1]==sln.occurrencesOfElement( nums = [1,2,3], queries = [10], x = 5)
assert [0,-1,2,-1]==sln.occurrencesOfElement( nums = [1,3,1,7], queries = [1,3,2,4], x = 1)