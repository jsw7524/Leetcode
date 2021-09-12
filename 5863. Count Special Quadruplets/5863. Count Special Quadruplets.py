from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        numsLen=len(nums)
        count=0
        for a in range(numsLen):
            for b in range(a+1,numsLen): 
                for c in range(b+1,numsLen):
                    for d in range(c+1,numsLen):
                        if nums[a]+nums[b]+nums[c] == nums[d]:
                            count+=1
        return count
    
sln=Solution()
assert 4==sln.countQuadruplets(nums = [1,1,1,3,5])                    
assert 1==sln.countQuadruplets(nums = [1,2,3,6])
assert 0==sln.countQuadruplets(nums = [3,3,6,4,5])                        