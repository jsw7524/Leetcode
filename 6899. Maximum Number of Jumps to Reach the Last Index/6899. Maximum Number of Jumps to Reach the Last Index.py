from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        numsLength=len(nums)
        dp=[0]*numsLength
        for j in range(numsLength):
            for i in range(j):
                if dp[i]==0 and i !=0:
                    continue
                if abs(nums[j] - nums[i]) <= target:
                    dp[j]=max(dp[j], dp[i] + 1)
        return -1 if dp[numsLength-1]==0 else dp[numsLength-1]

sln=Solution()
assert -1==sln.maximumJumps(nums = [0,2,1,3], target = 1)
assert -1==sln.maximumJumps(nums = [1,3,6,4,1,2], target = 0)
assert 5==sln.maximumJumps(nums = [1,3,6,4,1,2], target = 3)
assert 3==sln.maximumJumps(nums = [1,3,6,4,1,2], target = 2)