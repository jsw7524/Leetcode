import heapq
import math
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heapElm=[ -n for n in nums]
        heapq.heapify(heapElm)
        score=0
        for i in range(k):
            x=heapq.heappop(heapElm)
            score+=-x
            heapq.heappush(heapElm, math.floor(x/3.0))
        return score

sln=Solution()
assert 0==sln.maxKelements(nums = [0,0,0,0,0], k = 300)
assert 17==sln.maxKelements(nums = [1,10,3,3,3], k = 3)
assert 50==sln.maxKelements(nums = [10,10,10,10,10], k = 5)
            
            
            