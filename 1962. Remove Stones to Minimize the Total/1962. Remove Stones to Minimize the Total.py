from typing import List
import math
import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        lenPiles=len(piles)
        negPiles=list(map(lambda x : -1*x, piles) )
        heapq.heapify(negPiles)
        for i in range(k):
            maxVal=heapq.heappop(negPiles)
            heapq.heappush(negPiles, math.floor(maxVal/2))
        return -1*sum(negPiles)
    
sln=Solution()
assert 12==sln.minStoneSum(piles = [5,4,9], k = 2)
assert 12==sln.minStoneSum(piles = [4,3,6,7], k = 3)