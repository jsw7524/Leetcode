from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        v1=nums.index(max(nums))
        v2=nums.index(min(nums))
        if v1 > v2:
            v1, v2 = v2, v1
        return min(len(nums) - (v1), v2+1, (v1 +1) + (len(nums) - (v2)) )
    
sln=Solution()
assert 5==sln.minimumDeletions(nums = [2,10,7,5,4,1,8,6])
assert 3==sln.minimumDeletions(nums = [0,-4,19,1,8,-2,-3,5])
assert 1==sln.minimumDeletions(nums = [101])