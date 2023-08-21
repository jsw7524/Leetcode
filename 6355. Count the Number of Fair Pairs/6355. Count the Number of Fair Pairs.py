from typing import List

import bisect
class Solution:     
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sortingData=[nums[-1]]
        n=len(nums)
        answer=0
        for i in range(n-2, -1, -1):
            l=bisect.bisect_left(sortingData, lower-nums[i])
            u=bisect.bisect_right(sortingData, upper-nums[i])            
            answer+=(u-l)
            bisect.insort_left(sortingData, nums[i])
        return answer
    
sln=Solution()
assert 1==sln.countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11)
assert 6==sln.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6)