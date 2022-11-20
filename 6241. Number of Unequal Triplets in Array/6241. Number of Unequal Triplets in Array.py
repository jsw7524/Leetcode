from typing import List

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        answer=0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]!=nums[j] and nums[i]!=nums[k] and nums[j]!=nums[k]:
                        answer+=1
        return answer
    
sln=Solution()
assert 0==sln.unequalTriplets(nums = [1,1,1,1,1])    
assert 3==sln.unequalTriplets(nums = [4,4,2,4,3])                        