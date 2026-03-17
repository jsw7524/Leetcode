from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = [ n for n in nums]
        heapq.heapify(result)
        return heapq.nlargest(k, result)[-1]
