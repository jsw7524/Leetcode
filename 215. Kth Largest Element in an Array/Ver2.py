from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = [ -n for n in nums]
        heapq.heapify(result)
        for i in range(k):
            val =  -1*heapq.heappop(result)
        return val