from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos, neg=0,0
        for n in nums:
            if n < 0:
                neg+=1
            elif n > 0:
                pos+=1
        return max(pos,neg)
    
sln=Solution()
assert 4==sln.maximumCount(nums = [5,20,66,1314])
assert 3==sln.maximumCount(nums = [-3,-2,-1,0,0,1,2])
assert 3==sln.maximumCount(nums = [-2,-1,-1,1,2,3])