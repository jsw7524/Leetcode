from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        record= { v:1 for v in nums}
        for v in nums:
            if v**2 in record:
                record[v**2]=record[v]+1
        answer=max(record.values())
        return -1 if 1==answer else answer
    
sln=Solution()
assert -1==sln.longestSquareStreak(nums = [2,3,5,6,7])
assert 3==sln.longestSquareStreak(nums = [4,3,6,16,8,2])
                